from PySide2.QtCore import QObject, Signal
from uds import Uds
from ctypes import *
import os

class Model(QObject):
    sig_testerIpAddresslineEdit_changed = Signal(str)
    sig_diagMsgSendButton_changed = Signal(bool)
    sig_InfoPrintBrowser_changed = Signal(str)
    sig_DiagMsgPrintBrowser_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self._doip_connection_status = False
        self._ecu_ip_address = '172.31.7.1'
        self._ecu_logical_address = 0x1000
        self._tester_ip_address = '172.31.7.88'
        self._tester_logical_address = 0x0e80

    @property
    def ecu_ip_address(self):
        return self._ecu_ip_address

    @property
    def ecu_logical_address(self):
        return self._ecu_logical_address

    @property
    def tester_ip_address(self):
        return self._tester_ip_address

    @property
    def tester_logical_address(self):
        return self._tester_logical_address

    @ecu_ip_address.setter
    def ecu_ip_address(self, ecu_ip):
        self._ecu_ip_address = ecu_ip

    @ecu_logical_address.setter
    def ecu_logical_address(self, ecu_log_addr):
        self._ecu_logical_address = ecu_log_addr

    @tester_ip_address.setter
    def tester_ip_address(self, tester_ip):
        self._tester_ip_address = tester_ip

    @tester_logical_address.setter
    def tester_logical_address(self, tester_log_addr):
        self._tester_logical_address = tester_log_addr

    def print_parameters(self):
        print(self.ecu_logical_address, self.ecu_ip_address, self.tester_logical_address, self.tester_ip_address)

    def creat_uds_or_disconnect(self):
        if not self._doip_connection_status:
            try:
                self._client = Uds(transportProtocol="DoIP", ecu_ip=self._ecu_ip_address,
                               ecu_logical_address=self._ecu_logical_address,
                               client_logical_address=self._tester_logical_address)

                client_ip_addr, client_port = self._client.tp.DoIPClient.get_local_tcp_ip_and_port()

                self.sig_testerIpAddresslineEdit_changed.emit(client_ip_addr)
                self._doip_connection_status = True
                self.sig_diagMsgSendButton_changed.emit(self._doip_connection_status)
                self.sig_InfoPrintBrowser_changed.emit('doip connect!')
                # print('doip connect')
            except (ConnectionRefusedError, TimeoutError) as e:
                # print('doip connect error!')
                self.sig_InfoPrintBrowser_changed.emit('doip connect error!')

        else:

            self._doip_connection_status = False
            self._client.disconnect()
            self.sig_diagMsgSendButton_changed.emit(self._doip_connection_status)
            # print('doip disconnect!')
            self.sig_InfoPrintBrowser_changed.emit('doip disconnect!')


    def send_diagMsg_req_and_get_response(self, sid, diagContent):
        print(sid + diagContent)

        diagMsgReq = sid + diagContent
        diagMsgReq = Model.str_DiagMsg2_hex(diagMsgReq)

        if diagMsgReq:
            if diagMsgReq[0] == 0x27 and diagMsgReq[1] == 0x01:
                response = self.__send_doip_msg(diagMsgReq)
                if len(response) == 6 and response[0] == 0x67 and response[1] == 0x01:
                    reqWithKey = [0x27, 0x02]
                    key = keyGen(response[2:])
                    reqWithKey.extend(key)
                    self.__send_doip_msg(reqWithKey)
            else:
                self.__send_doip_msg(diagMsgReq)

    def __send_doip_msg(self, diagMsgReq):
        # print((diagMsgReq))
        self.sig_DiagMsgPrintBrowser_changed.emit('Tx: ' + self.hex_DiagMsg2_str(diagMsgReq))
        response = self._client.send(diagMsgReq)
        # print(response)
        self.sig_DiagMsgPrintBrowser_changed.emit('Rx: ' + self.hex_DiagMsg2_str(response))
        # self.__print_req_response_to_diagMsgPrintBrowser(diagMsgReq, response)
        return response

    @staticmethod
    def get_byte_split_msg(msg):
        assert isinstance(msg, str)
        msg = msg.replace(' ', '')

        if(len(msg)%2):
            msg = msg + '0'

        msg = [msg[i:i+2] for i in range(0, len(msg), 2)]

        return ' '.join(msg)

    @staticmethod
    def formatMsg(fmt, msg):
        return '{0}{1}'.format(fmt, msg)

    @staticmethod
    def str_DiagMsg2_hex(strMsg):
        try:
            strMsg = Model.get_byte_split_msg(strMsg)
            strMsg = strMsg.split(' ')
            # print(strMsg)
            hexMsg = [(int(x, 16)) for x in strMsg]
            # print(hexMsg)
        except TypeError as e:
            hexMsg = None

        return hexMsg

    @staticmethod
    def hex_DiagMsg2_str(hexMsg):


        diagRespData = [hex(x)[2:] for x in hexMsg]
        diagRespData = [x.zfill(2) for x in diagRespData]

        return ' '.join(diagRespData)

def keyGen(seed_input):
    #print(os.getcwd())
    lib = cdll.LoadLibrary(os.getcwd() + '\libkeygen.so')
    seed_data = c_char * 4
    seed = seed_data()

    for i in range(4):
        seed[i] = seed_input[i]

    key_data = c_char * 4
    key = key_data()

    lib.GenerateKeyEx(seed, 4, key)

    key_output = []
    for i in range(4):
        key_output.append(key[i][0])

    return key_output
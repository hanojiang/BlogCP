from PySide2.QtCore import QObject, Signal
from uds import Uds

class Model(QObject):
    sig_testerIpAddresslineEdit_changed = Signal(str)


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

    def creat_uds(self):
        try:
            self._client = Uds(transportProtocol="DoIP", ecu_ip=self._ecu_ip_address,
                           ecu_logical_address=self._ecu_logical_address,
                           client_logical_address=self._tester_logical_address)

            client_ip_addr, client_port = self._client.tp.DoIPClient.get_local_tcp_ip_and_port()

            self.sig_testerIpAddresslineEdit_changed.emit(client_ip_addr)
            # self.testerIpAddresslineEdit.setText(client_ip_addr)
            # self.__udsThread = Thread(target=self.__build_uds_connection)
            # self.__udsThread.start()

            # self.append_msg_to_infoPrintBrowser('doip connect ok!')
            # self.__set_pushbutton_status(True)
            # self.buildConnectionButton.setText('断开连接')
            # self.__doip_connection_status = True
        except (ConnectionRefusedError, TimeoutError) as e:
            print('doip connect error!')

        # self.append_msg_to_infoPrintBrowser('doip connect error!')

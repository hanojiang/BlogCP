from gui import Ui_MainWindow
from Ecu_Const import get_all_ecu, DIAG_SID, get_ecu_logical_address_by_index
from uds import Uds
from PySide2.QtCore import Signal,QObject
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextBrowser, QTableWidget, QTableWidgetItem
from PySide2.QtWidgets import QHeaderView
from threading import Thread
from ctypes import *
import os

class Main_Ui(Ui_MainWindow):

    def __init__(self, MainWindow):
        self.setupUi(MainWindow)

        self.__globalSignal = GlobalSigals()
        self.__init_all_components()
        self.__init_all_actions()
        # self.__init_uds_settings()

        self.__doip_connection_status = False


    def __init_uds_settings(self):
        self.__ecu_ip_address = self.ecuIpAddressLineEdit.text()
        self.__ecu_logical_address = int(self.ecuLogicalAddressLineEdit.text(), 16)
        self.__tester_ip_address = self.testerIpAddresslineEdit.text()
        self.__tester_logical_address = int(self.testerLogicalAddressLineEdit.text(),16)

        print(self.__ecu_ip_address, self.__ecu_logical_address)
        print(self.__tester_ip_address, self.__tester_logical_address)


    def __init_all_components(self):
        self.__init_sidSeclectBox()
        self.__init_ecuSeclectBox()
        self.__set_pushbutton_status(False)
        self.__init_all_signals()
        self.__init_multi_diag_msg_tableWidget()


    def __init_sidSeclectBox(self):
        self.sidSeclectBox.addItems(DIAG_SID)

    def __init_ecuSeclectBox(self):
        self.ecuSeclectBox.addItems(get_all_ecu())

    def __set_pushbutton_status(self, isEnable):
        self.sendDiagMsgButton.setEnabled(isEnable)
        self.sendDoipUdpMsgButton.setEnabled(isEnable)
        # self.buildConnectionButton.setEnabled(not isEnable)


    def __init_all_actions(self):
        self.buildConnectionButton.triggered.connect(self.__init_uds_client_action)
        self.sendDiagMsgButton.clicked.connect(self.__send_diagMsg_action)
        self.diagReqMsgLineEdit.returnPressed.connect(self.__send_diagMsg_action)

        self.addLinePushButton.clicked.connect(self.__add_Line_PushButton_action)
        self.clearPushButton.clicked.connect(self.__clear_tableWidget_PushButton_action)
        self.multiSendPushButton.clicked.connect(self.__multi_line_send_PushButton_action)

        # self.sendDoipUdpMsgButton.clicked.connect()
        # 具体菜单项
        msgClearOption = QAction(self.DiagMsgPrintBrowser)
        msgClearOption.setText("清空")
        msgClearOption.triggered.connect(self.__clear_all_print_textBrowser)  # 点击菜单中的“发送控制代码”执行的函数

        # tableView 添加具体的右键菜单
        self.DiagMsgPrintBrowser.addAction(msgClearOption)

    def __init_all_signals(self):
        self.__globalSignal.msgPrintBrowserSignal.connect(self.append_msg_to_textBrowser)

    def __init_multi_diag_msg_tableWidget(self):
        # self.multiLineTableWidget.insertRow(0)
        # qv = QHeaderView(Horizontal)
        # hh = self.multiLineTableWidget.horizontalHeader()
        # vh = self.multiLineTableWidget.verticalHeaderItem(0)
        # vh.setText('11111')
        # print(self.multiLineTableWidget.rowCount())
        #
        # self.multiLineTableWidget.setVerticalHeaderItem(1)
        # vh = self.multiLineTableWidget.takeVerticalHeaderItem(2)
        # # vh.setText('2222')
        # print(self.multiLineTableWidget.rowCount())

        # for i in range(5):
        #     self.multiLineTableWidget.insertRow(i)
        # print(self.multiLineTableWidget.rowCount())
        pass

    def __init_uds_client_action(self):
        try:
            if not self.__doip_connection_status:

                # self.ecu = Uds(transportProtocol="DoIP", ecu_ip="127.0.0.1")
                self.__init_uds_settings()
                self.ecu = Uds(transportProtocol="DoIP", ecu_ip=self.__ecu_ip_address, ecu_logical_address=self.__ecu_logical_address, client_logical_address=self.__tester_logical_address)
                # client_ip_addr, client_port = self.ecu.tp.get_lcoal_doip_connection_info()
                client_ip_addr, client_port = self.ecu.tp.DoIPClient.get_local_tcp_ip_and_port()
                self.testerIpAddresslineEdit.setText(client_ip_addr)
                # self.__udsThread = Thread(target=self.__build_uds_connection)
                # self.__udsThread.start()

                self.append_msg_to_infoPrintBrowser('doip connect ok!')
                self.__set_pushbutton_status(True)
                self.buildConnectionButton.setText('断开连接')
                self.__doip_connection_status = True
            else:
                self.ecu.disconnect()
                self.buildConnectionButton.setText('建立连接')
                self.__set_pushbutton_status(False)
                self.__doip_connection_status = False
                self.append_msg_to_infoPrintBrowser('doip disconnect ok!')
                # print('doip disconnect ok!')
        except (ConnectionRefusedError, TimeoutError) as e:
            # print('doip connect error!')
            self.append_msg_to_infoPrintBrowser('doip connect error!')

    # def __build_uds_connection(self):
    #     self.ecu = Uds(transportProtocol="DoIP", ecu_ip="127.0.0.1")

    def __send_diagMsg_action(self):
        print('send diag msg')
        sid = self.sidSeclectBox.currentText()
        # ecuName = self.ecuSeclectBox.currentText()
        ecuIndex = self.ecuSeclectBox.currentIndex()
        ecuLogicAddress = get_ecu_logical_address_by_index(ecuIndex)
        self.ecu.tp.DoIPClient.ecu_logical_address = ecuLogicAddress

        diagMsgContent = self.diagReqMsgLineEdit.text()

        self.diagReqMsgLineEdit.setText(Main_Ui.get_byte_split_msg(diagMsgContent))

        self.__send_diagMsg_req_and_get_response(sid, diagMsgContent)

    def __add_Line_PushButton_action(self):
        rowCnt = self.multiLineTableWidget.rowCount()
        sid = self.sidLineEdit.text()
        diagData = self.diagDataLineEdit.text()

        self.multiLineTableWidget.insertRow(rowCnt)
        self.multiLineTableWidget.setItem(rowCnt, 0, QTableWidgetItem(sid))
        self.multiLineTableWidget.setItem(rowCnt, 1, QTableWidgetItem(diagData))


    def __clear_tableWidget_PushButton_action(self):
        self.multiLineTableWidget.setRowCount(0)

    def __multi_line_send_PushButton_action(self):
        for i in range(self.multiLineTableWidget.rowCount()):
            sid = self.multiLineTableWidget.item(i, 0).text()
            diagData = self.multiLineTableWidget.item(i, 1).text()
            # diagMsg = sid + diagData
            # self.append_msg_to_diagMsgPrintBrowser(Main_Ui.formatMsg('Tx: ', Main_Ui.get_byte_split_msg(diagMsg)))
            self.__send_diagMsg_req_and_get_response(sid, diagData)

    def __clear_all_print_textBrowser(self):
        self.DiagMsgPrintBrowser.clear()
        self.InfoPrintBrowser.clear()

    def __send_diagMsg_req_and_get_response(self, sid, diagData):
        diagMsgReq = sid + diagData
        # self.append_msg_to_diagMsgPrintBrowser(Main_Ui.formatMsg('Tx: ', Main_Ui.get_byte_split_msg(diagMsgReq)))
        diagMsgReq = Main_Ui.str_DiagMsg2_hex(diagMsgReq)

        if diagMsgReq:
            if diagMsgReq[0] == 0x27 and diagMsgReq[1] == 0x01:
                # response = self.ecu.send(diagMsgReq)
                # self.append_msg_to_diagMsgPrintBrowser(Main_Ui.formatMsg('Rx: ', Main_Ui.get_byte_split_msg( Main_Ui.hex_DiagMsg2_str(response))))
                # self.__print_req_response_to_diagMsgPrintBrowser(diagMsgReq, response)
                response = self.__send_doip_msg(diagMsgReq)
                if len(response) == 6 and response[0] == 0x67 and response[1] == 0x01:
                    reqWithKey = [0x27, 0x02]
                    key = keyGen(response[2:])
                    reqWithKey.extend(key)
                    # response = self.ecu.send(reqWithKey)
                    # self.__print_req_response_to_diagMsgPrintBrowser(reqWithKey, response)
                    # self.append_msg_to_diagMsgPrintBrowser(Main_Ui.formatMsg('Rx: ', Main_Ui.get_byte_split_msg(Main_Ui.hex_DiagMsg2_str(response))))
                    self.__send_doip_msg(reqWithKey)
            else:
                # response = self.ecu.send(diagMsgReq)
                # self.__print_req_response_to_diagMsgPrintBrowser(diagMsgReq, response)
                # print(response)
                # self.append_msg_to_diagMsgPrintBrowser(Main_Ui.formatMsg('Rx: ', Main_Ui.get_byte_split_msg( Main_Ui.hex_DiagMsg2_str(response))))
                self.__send_doip_msg(diagMsgReq)

    def __send_doip_msg(self, diagMsgReq):
        response = self.ecu.send(diagMsgReq)
        self.__print_req_response_to_diagMsgPrintBrowser(diagMsgReq, response)

        return response

    def __print_req_response_to_diagMsgPrintBrowser(self, diagMsgReq, response):
        self.append_msg_to_diagMsgPrintBrowser(Main_Ui.formatMsg('Tx: ', Main_Ui.get_byte_split_msg(self.hex_DiagMsg2_str(diagMsgReq))))
        self.append_msg_to_diagMsgPrintBrowser(
            Main_Ui.formatMsg('Rx: ', Main_Ui.get_byte_split_msg(Main_Ui.hex_DiagMsg2_str(response))))

    def append_msg_to_diagMsgPrintBrowser(self, msg):
        self.__globalSignal.msgPrintBrowserSignal.emit(self.DiagMsgPrintBrowser, msg)

    def append_msg_to_infoPrintBrowser(self, msg):
        self.__globalSignal.msgPrintBrowserSignal.emit(self.InfoPrintBrowser, msg)


    def append_msg_to_textBrowser(self, textBrowser, msg):
        """
            append msg to textBrowser
        :param textBrowser:
        :param msg:
        """
        assert isinstance(textBrowser, QTextBrowser)
        textBrowser.append(msg)
        textBrowser.ensureCursorVisible()

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
            strMsg = Main_Ui.get_byte_split_msg(strMsg)
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

        return ''.join(diagRespData)

class GlobalSigals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    msgPrintBrowserSignal = Signal(QTextBrowser, str)

    # 还可以定义其他种类的信号
    #update_table = Signal(str)

    # changeConnectionButtor = Signal(QPushButton, str)


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
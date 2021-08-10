from gui import Ui_MainWindow
from Ecu_Const import get_all_ecu, DIAG_SID
from uds import Uds
from PySide2.QtCore import Signal,QObject
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextBrowser
from threading import Thread

class Main_Ui(Ui_MainWindow):

    def __init__(self, MainWindow):
        self.setupUi(MainWindow)

        self.__globalSignal = GlobalSigals()
        self.__init_all_components()
        self.__init_all_actions()

        self.__doip_connection_status = False

    def __init_all_components(self):
        self.__init_sidSeclectBox()
        self.__init_ecuSeclectBox()
        self.__set_pushbutton_status(False)
        self.__init_all_signals()

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
        # self.sendDoipUdpMsgButton.clicked.connect()

    def __init_all_signals(self):
        self.__globalSignal.msgPrintBrowserSignal.connect(self.append_msg_to_textBrowser)

    def __init_uds_client_action(self):
        try:
            if not self.__doip_connection_status:

                self.ecu = Uds(transportProtocol="DoIP", ecu_ip="127.0.0.1")
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
        ecuName = self.ecuSeclectBox.currentText()

        diagMsgContent = self.diagReqMsgLineEdit.text()

        self.diagReqMsgLineEdit.setText(Main_Ui.get_byte_split_msg(diagMsgContent))

        diagMsg = sid + diagMsgContent
        self.append_msg_to_diagMsgPrintBrowser(Main_Ui.formatMsg('Tx: ', Main_Ui.get_byte_split_msg(diagMsg)))
        diagMsg = Main_Ui.str_DiagMsg2_hex(diagMsg)

        if diagMsg:
            response = self.ecu.send(diagMsg)
            print(response)
            self.append_msg_to_diagMsgPrintBrowser(Main_Ui.formatMsg('Rx: ', Main_Ui.get_byte_split_msg( Main_Ui.hex_DiagMsg2_str(response))))


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
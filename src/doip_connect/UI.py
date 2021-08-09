from gui import Ui_MainWindow
from Ecu_Const import get_all_ecu, DIAG_SID
from uds import Uds
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextBrowser

class Main_Ui(Ui_MainWindow):

    def __init__(self, MainWindow):
        self.setupUi(MainWindow)

        self.__init_all_components()
        self.__init_all_actions()

        self.__doip_connection_status = False

    def __init_all_components(self):
        self.__init_sidSeclectBox()
        self.__init_ecuSeclectBox()
        self.__set_pushbutton_status(False)

    def __init_sidSeclectBox(self):
        self.sidSeclectBox.addItems(DIAG_SID)

    def __init_ecuSeclectBox(self):
        self.ecuSeclectBox.addItems(get_all_ecu())

    def __set_pushbutton_status(self, isEnable):
        self.sendDiagMsgButton.setEnabled(isEnable)
        self.sendDoipUdpMsgButton.setEnabled(isEnable)
        # self.buildConnectionButton.setEnabled(not isEnable)


    def __init_all_actions(self):
        self.buildConnectionButton.triggered.connect(self.__init_uds_client)


    def __init_uds_client(self):
        try:
            if not self.__doip_connection_status:

                # self.append_msg_to_infoPrintBrowser('doip connect start!')
                self.ecu = Uds(transportProtocol="DoIP", ecu_ip="127.0.0.1")
                # print('doip connect ok!')
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

    def append_msg_to_infoPrintBrowser(self, msg):
        self.append_msg_to_textBrowser(self.InfoPrintBrowser, msg)

    def append_msg_to_textBrowser(self, textBrowser, msg):
        """
            append msg to textBrowser
        :param textBrowser:
        :param msg:
        """
        assert isinstance(textBrowser, QTextBrowser)
        textBrowser.append(msg)
        textBrowser.ensureCursorVisible()
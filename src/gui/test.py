import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextBrowser
from PySide2.QtCore import QFile
from doip import Ui_MainWindow
from DoipJsonFormat import GW04_ALL_NODE
#from DoipClient import DoipClient
from uds import *
from threading import Thread
from GlobalSignals import GlobalSigals

global_ms = GlobalSigals()

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ecuConnectionStatus = False
        self.init_commponents()

        # self.ethTp = EthTp(self.ui.DoipMsgBrowser)

        global_ms.text_print.connect(self.textBrowserAppendMsg)
        global_ms.changeConnectionButtor.connect(self.changeButtonText)


    def init_commponents(self):
        """
            init all commponents
        """
        self.init_sidSeclectBox()
        self.init_MsgTxRxBrowser()
        self.init_ecuSeclectBox()
        self.init_payloadSecletBox()

        self.setPushButtons(False)

        self.init_action()

    def setPushButtons(self, status):
        self.ui.sendMsgButton.setEnabled(status)
        self.ui.sendDoipMsgButton.setEnabled(status)

    def init_sidSeclectBox(self):
        self.ui.sidSeclectBox.addItems(['10', '11', '22', '2E', '27', '31'])

    def init_ecuSeclectBox(self):
        self.ui.ecuSeclectBox.addItems(self.getAllEcuNode())

    def init_payloadSecletBox(self):
        payloadTypeStr = []

        for i in EthTp.repType.keys():
            payloadTypeStr.append('{}({})'.format(HeaderFormat[i], hex(i)))
        self.ui.payloadSecletBox.addItems(payloadTypeStr)

    def init_MsgTxRxBrowser(self):

        # 具体菜单项
        msg_clear_option = QAction(self.ui.DiagMsgTxRxBrowser)
        msg_clear_option.setText("清空")
        msg_clear_option.triggered.connect(self.clearMsgTxRxBrowser)  # 点击菜单中的“发送控制代码”执行的函数

        # tableView 添加具体的右键菜单
        self.ui.DiagMsgTxRxBrowser.addAction(msg_clear_option)

    def init_action(self):
        self.ui.action_buildConnection.triggered.connect(self.buildConnection)
        self.ui.sendMsgButton.clicked.connect(self.handleDiagMsgSend)
        self.ui.sendDoipMsgButton.clicked.connect(self.handleDoipMsgSend)


    def buildConnection(self):
        """
            build connection for connection push button
        """
        if(not self.ecuConnectionStatus):

            self.textBrowserAppendMsg(self.ui.InfoMsgBrowser, '正在建立ECU连接')



            self.ui.action_buildConnection.setEnabled(False)




            thread_deal_connection = Thread(target=self.msgRecvThreadFunc)
            thread_deal_connection.start()
        else:
            self.textBrowserAppendMsg(self.ui.InfoMsgBrowser, '断开ECU连接')

            self.ecuConnectionStatus = False
            self.changeButtonText(self.ui.action_buildConnection, '建立连接')

            self.ethTp.closeConnection()
            del self.ethTp

    def changeButtonText(self, button, str):
        """

        :param button: pushbutton
        :param str: change the text of button for this value
        """
        button.setText(str)

    def msgRecvThreadFunc(self):
        """
            thread function for build connection
        """


        try:
            self.ethTp = EthTp(self.ui.DoipMsgBrowser, self.ui.DiagMsgTxRxBrowser)
            self.ethTp.openConnection()
            pass
        except ConnectionRefusedError:
            global_ms.text_print.emit(self.ui.InfoMsgBrowser, 'ECU连接建立失败')
            self.ui.action_buildConnection.setEnabled(True)
            return


        msg = DoIPMessage(DOIP_VehIdReqMsg)
        self.ethTp.send(msg)

        msg = DoIPMessage(DOIP_RoutingActiveReq)
        self.ethTp.send(msg)

        vehAncResp = EthTp.recv(3, DOIP_VehIdReqMsg)
        routeActResp = EthTp.recv(3, DOIP_RoutingActiveReq)
        if(vehAncResp is None or routeActResp is None):
            global_ms.text_print.emit(self.ui.InfoMsgBrowser, 'ECU连接建立失败')
            self.setPushButtons(False)


        else:
            self.ecuConnectionStatus = True
            self.setPushButtons(True)
            global_ms.text_print.emit(self.ui.InfoMsgBrowser, 'ECU连接建立成功')
            #global_ms.text_print.emit(self.ui.DoipMsgBrowser, str(vehAncResp))
            #global_ms.text_print.emit(self.ui.DoipMsgBrowser, str(routeActResp))
            global_ms.changeConnectionButtor.emit(self.ui.action_buildConnection, '断开连接')
        self.ui.action_buildConnection.setEnabled(True)

    def handleDiagMsgSend(self):

        sidMsg = self.ui.sidSeclectBox.currentText()
        ecuName = self.ui.ecuSeclectBox.currentText()


        diag_msg = self.ui.msgLineEdit.text()
        self.ui.msgLineEdit.setText(self.formatMsg(diag_msg))

        self.textBrowserAppendMsg(self.ui.DiagMsgTxRxBrowser, 'Tx: ' + self.formatMsg(sidMsg + diag_msg))

        self.textBrowserAppendMsg(self.ui.InfoMsgBrowser, 'Diag:' + ecuName)

        msg = DoIPMessage(DOIP_DiagMsg)
        # msg.setDirection('tx')
        diagData= self.getListStr(sidMsg + diag_msg)
        msg.setDiagData([int(x, 16) for x in diagData])
        # print(msg)

        self.ethTp.send(msg)

        if(sidMsg == '27' and diag_msg == '01'):
            print(msg)
            print(self.ethTp.recv(1, DOIP_DiagMsg))

        # diagResp = self.ethTp.recv(3, DOIP_DiagMsg)
        # diagRespData = diagResp.getDiagData()
        #
        # diagRespData = [hex(x)[2:] for x in diagRespData]
        # diagRespData = [x.zfill(2) for x in diagRespData]
        # # print(diagRespData)
        # self.textBrowserAppendMsg(self.ui.DiagMsgTxRxBrowser, 'Rx: ' + self.formatMsg(''.join(diagRespData)))

    def handleDoipMsgSend(self):
        # print(self.ui.payloadSecletBox.currentIndex(), self.ui.payloadSecletBox.currentText())
        # print(list(EthTp.repType.keys())[self.ui.payloadSecletBox.currentIndex()])
        msg = DoIPMessage(list(EthTp.repType.keys())[self.ui.payloadSecletBox.currentIndex()])
        self.ethTp.send(msg)

    def clearMsgTxRxBrowser(self):
        """
            clear two qtextbrowser's text
        """
        self.ui.DiagMsgTxRxBrowser.clear()
        self.ui.InfoMsgBrowser.clear()
        self.ui.DoipMsgBrowser.clear()

    def textBrowserAppendMsg(self, textBrowser, msg):
        """
            append msg to textBrowser
        :param textBrowser:
        :param msg:
        """
        assert isinstance(textBrowser, QTextBrowser)
        textBrowser.append(msg)
        textBrowser.ensureCursorVisible()


    def getAllEcuNode(self):
        allNode = []
        for node in GW04_ALL_NODE:
            allNode.append('{:>6}({})'.format(node['MCU_NAME'], hex(node['LOGICAL_ADD'])))

        return allNode

    def getListStr(self, msg):
        assert isinstance(msg, str)
        msg = msg.replace(' ', '')

        if(len(msg)%2):
            msg = msg + '0'
        # print(msg)
        msg = [msg[i:i+2] for i in range(0, len(msg), 2)]
        #msg = ' '.join(msg)
        return msg

    def formatMsg(self, msg):
        msg = self.getListStr(msg)
        return ' '.join(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
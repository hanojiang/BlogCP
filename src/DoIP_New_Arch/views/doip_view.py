from PySide2.QtWidgets import QMainWindow, QAction, QTableWidgetItem
from PySide2.QtCore import Slot
from views.Doip_gui_view import Ui_MainWindow
from controllers.doip_controller import DoIP_Controller
from model.doip_model import Model
from Ecu_Const import *

class MainView(QMainWindow):
    def __init__(self, model:Model, controller:DoIP_Controller):
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.set_doip_parameter()

        self.__init_all_components()
        self.__init_all_actions()

    @Slot()
    def set_doip_parameter(self):
        ecu_ip_address = self._ui.ecuIpAddressLineEdit.text()
        ecu_logical_address = int(self._ui.ecuLogicalAddressLineEdit.text(), 16)
        tester_ip_address = self._ui.testerIpAddresslineEdit.text()
        tester_logical_address = int(self._ui.testerLogicalAddressLineEdit.text(), 16)
        self._controller.set_doip_parameter(ecu_ip_address, tester_ip_address, ecu_logical_address, tester_logical_address)

    @Slot()
    def on_loopbackIPSettingButton_pressed(self):
        ecu_ip_address = '127.0.0.1'
        tester_ip_address = '127.0.0.1'
        self._ui.ecuIpAddressLineEdit.setText(ecu_ip_address)
        self._ui.testerIpAddresslineEdit.setText(tester_ip_address)
        self.set_doip_parameter()


    def __init_all_components(self):
        self.__init_sidSeclectBox()
        self.__init_ecuSeclectBox()
        self.__set_pushbutton_status(False)

    def __init_sidSeclectBox(self):
        self._ui.sidSeclectBox.addItems(DIAG_SID)

    def __init_ecuSeclectBox(self):
        self._ui.ecuSeclectBox.addItems(get_all_ecu())

    def __set_pushbutton_status(self, isEnable):
        self._ui.sendDiagMsgButton.setEnabled(isEnable)
        self._ui.sendDoipUdpMsgButton.setEnabled(isEnable)
        if isEnable:
            self._ui.buildConnectionButton.setText('断开连接')
        else:
            self._ui.buildConnectionButton.setText('建立连接')

    def __init_all_actions(self):
        self._ui.buildConnectionButton.triggered.connect(self._controller.on_buildConnectionButton_pressed)
        self._ui.applySettingButton.clicked.connect(self.set_doip_parameter)
        self._ui.loopbackIPSettingButton.clicked.connect(self.on_loopbackIPSettingButton_pressed)
        self._ui.sendDiagMsgButton.clicked.connect(self.__on_sendDiagMsgButton_pressed)
        self._ui.addLinePushButton.clicked.connect(self.__on_add_Line_PushButton_pressed)
        self._ui.clearPushButton.clicked.connect(self.__on_clear_tableWidget_PushButton_pressed)
        self._ui.multiSendPushButton.clicked.connect(self.__on_multi_line_send_PushButton_pressed)
        self._ui.secAccessPushButton.clicked.connect(self.__on_secAccessPushButton_pressed)
        self._ui.portMirrorSettingPushButton.clicked.connect(self.__on_portMirrorSettingPushButton_pressed)


        self._model.sig_testerIpAddresslineEdit_changed.connect(self.__on_testerIpAddresslineEdit_changed)
        self._model.sig_diagMsgSendButton_changed.connect(self.__set_pushbutton_status)
        self._model.sig_InfoPrintBrowser_changed.connect(self.__on_InfoPrintBrowser_changed)
        self._model.sig_DiagMsgPrintBrowser_changed.connect(self.__on_DiagMsgPrintBrowser_changed)
        # self._ui.sendDiagMsgButton.clicked.connect(self.__send_diagMsg_action)
        # self._ui.diagReqMsgLineEdit.returnPressed.connect(self.__send_diagMsg_action)
        # self._ui.addLinePushButton.clicked.connect(self.__add_Line_PushButton_action)
        # self._ui.clearPushButton.clicked.connect(self.__clear_tableWidget_PushButton_action)
        # self._ui.multiSendPushButton.clicked.connect(self.__multi_line_send_PushButton_action)
        msgClearOption = QAction(self._ui.DiagMsgPrintBrowser)
        msgClearOption.setText("清空")
        msgClearOption.triggered.connect(self.__clear_all_print_textBrowser)  # 点击菜单中的“发送控制代码”执行的函数

        # tableView 添加具体的右键菜单
        self._ui.DiagMsgPrintBrowser.addAction(msgClearOption)

    def get_ecu_logical_address(self):
        ecuIndex = self._ui.ecuSeclectBox.currentIndex()
        ecuLogicAddress = get_ecu_logical_address_by_index(ecuIndex)
        return ecuLogicAddress

    @Slot(str)
    def __on_testerIpAddresslineEdit_changed(self, text):
        self._ui.testerIpAddresslineEdit.setText(text)

    @Slot(str)
    def __on_InfoPrintBrowser_changed(self, text):
        self._ui.InfoPrintBrowser.append(text)
        self._ui.InfoPrintBrowser.ensureCursorVisible()

    @Slot(str)
    def __on_DiagMsgPrintBrowser_changed(self, text):
        self._ui.DiagMsgPrintBrowser.append(text)
        self._ui.DiagMsgPrintBrowser.ensureCursorVisible()

    @Slot()
    def __clear_all_print_textBrowser(self):
        self._ui.DiagMsgPrintBrowser.clear()
        self._ui.InfoPrintBrowser.clear()


    @Slot()
    def __on_sendDiagMsgButton_pressed(self):
        sid = self._ui.sidSeclectBox.currentText()
        ecuLogicAddress = self.get_ecu_logical_address()
        diagMsgContent = self._ui.diagReqMsgLineEdit.text()
        self._controller.send_diag_msg(sid, ecuLogicAddress, diagMsgContent)

    @Slot()
    def __on_add_Line_PushButton_pressed(self):
        rowCnt = self._ui.multiLineTableWidget.rowCount()
        sid = self._ui.sidLineEdit.text()
        diagData = self._ui.diagDataLineEdit.text()

        self._ui.multiLineTableWidget.insertRow(rowCnt)
        self._ui.multiLineTableWidget.setItem(rowCnt, 0, QTableWidgetItem(sid))
        self._ui.multiLineTableWidget.setItem(rowCnt, 1, QTableWidgetItem(diagData))

    @Slot()
    def __on_clear_tableWidget_PushButton_pressed(self):
        self._ui.multiLineTableWidget.setRowCount(0)

    @Slot()
    def __on_multi_line_send_PushButton_pressed(self):
        for i in range(self._ui.multiLineTableWidget.rowCount()):
            sid = self._ui.multiLineTableWidget.item(i, 0).text()
            diagData = self._ui.multiLineTableWidget.item(i, 1).text()
            ecuAddr = self.get_ecu_logical_address()
            self._controller.send_diag_msg(sid, ecuAddr, diagData)

    @Slot()
    def __on_secAccessPushButton_pressed(self):

        ecuAddr = self.get_ecu_logical_address()
        self._controller.send_diag_msg('10', ecuAddr, '03')
        self._controller.send_diag_msg('27', ecuAddr, '01')

    @Slot()
    def __on_portMirrorSettingPushButton_pressed(self):
        portMirror = self._ui.portMirrorLineEdit.text()
        if portMirror is '':
            portMirror = '80ff'

        ecuAddr = self.get_ecu_logical_address()
        self._controller.send_diag_msg('10', ecuAddr, '03')
        self._controller.send_diag_msg('27', ecuAddr, '01')
        self._controller.send_diag_msg('2E', ecuAddr, 'CE06'+portMirror)
        self._controller.send_diag_msg('11', ecuAddr, '01')
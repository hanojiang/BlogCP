from PySide2.QtWidgets import QMainWindow
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

    def set_doip_parameter(self):
        ecu_ip_address = self._ui.ecuIpAddressLineEdit.text()
        ecu_logical_address = int(self._ui.ecuLogicalAddressLineEdit.text(), 16)
        tester_ip_address = self._ui.testerIpAddresslineEdit.text()
        tester_logical_address = int(self._ui.testerLogicalAddressLineEdit.text(), 16)
        self._controller.set_doip_parameter(ecu_ip_address, tester_ip_address, ecu_logical_address, tester_logical_address)

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

    def __init_all_actions(self):
        self._ui.buildConnectionButton.triggered.connect(self._controller.build_ecu_connect)
        self._model.sig_testerIpAddresslineEdit_changed.connect(self.__on_testerIpAddresslineEdit_changed)
        # self._ui.sendDiagMsgButton.clicked.connect(self.__send_diagMsg_action)
        # self._ui.diagReqMsgLineEdit.returnPressed.connect(self.__send_diagMsg_action)
        # self._ui.addLinePushButton.clicked.connect(self.__add_Line_PushButton_action)
        # self._ui.clearPushButton.clicked.connect(self.__clear_tableWidget_PushButton_action)
        # self._ui.multiSendPushButton.clicked.connect(self.__multi_line_send_PushButton_action)


    @Slot(str)
    def __on_testerIpAddresslineEdit_changed(self, text):
        self._ui.testerIpAddresslineEdit.setText(text)
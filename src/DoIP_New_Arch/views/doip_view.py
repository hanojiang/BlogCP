from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from views.Doip_gui_view import Ui_MainWindow
from controllers.doip_controller import DoIP_Controller

class MainView(QMainWindow):
    def __init__(self, model, controller:DoIP_Controller):
        super().__init__()

        self._model = model
        self._main_controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.set_doip_parameter()

    def set_doip_parameter(self):
        ecu_ip_address = self._ui.ecuIpAddressLineEdit.text()
        ecu_logical_address = int(self._ui.ecuLogicalAddressLineEdit.text(), 16)
        tester_ip_address = self._ui.testerIpAddresslineEdit.text()
        tester_logical_address = int(self._ui.testerLogicalAddressLineEdit.text(), 16)
        self._main_controller.set_doip_parameter(ecu_ip_address, tester_ip_address, ecu_logical_address, tester_logical_address)

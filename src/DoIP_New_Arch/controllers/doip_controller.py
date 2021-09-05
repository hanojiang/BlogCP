from PySide2.QtCore import QObject, Slot
from model.doip_model import Model

class DoIP_Controller(QObject):

    def __init__(self, model:Model):
        super(DoIP_Controller, self).__init__()
        self._model = model

    def set_doip_parameter(self, ecu_ip_address, tester_ip_address, ecu_logical_address, tester_logical_address):

        self._model.ecu_ip_address = ecu_ip_address
        self._model.tester_ip_address = tester_ip_address
        self._model.ecu_logical_address = ecu_logical_address
        self._model.tester_logical_address = tester_logical_address

        self._model.print_parameters()

    @Slot()
    def on_buildConnectionButton_pressed(self):

        self._model.creat_uds_or_disconnect()
        pass

    def send_diag_msg(self, sid, ecuAddr, content):
        self._model.ecu_logical_address = ecuAddr
        content = self._model.get_byte_split_msg(content)
        self._model.send_diagMsg_req_and_get_response(sid, content)

    # @Slot()
    # def on_applySettingButton_pressed(self):
    #     self.set_doip_parameter()
    #     pass
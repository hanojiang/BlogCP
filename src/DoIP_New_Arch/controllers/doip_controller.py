from PySide2.QtCore import QObject
from model.doip_model import Model

class DoIP_Controller(QObject):

    def __init__(self, model:Model):
        super(DoIP_Controller, self).__init__()
        self._model = model

    def set_doip_parameter(self, ecu_ip_address, tester_ip_address, ecu_logical_address, tester_logical_address):

        self._model.ecu_logical_address = ecu_ip_address
        self._model.tester_ip_address = tester_ip_address
        self._model.ecu_logical_address = ecu_logical_address
        self._model.tester_logical_address = tester_logical_address

        self._model.print_parameters()



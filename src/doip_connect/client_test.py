# import SomeLib.SomeCar.SomeModel as MyCar
# import udsoncan
# from doipclient import DoIPClient
# from doipclient.connectors import DoIPClientUDSConnector
# from udsoncan.client import Client
# from udsoncan.exceptions import *
# from udsoncan.services import *

# udsoncan.setup_logging()

# ecu_ip = '127.0.0.1'
# ecu_logical_address = 0x00E0
# doip_client = DoIPClient(ecu_ip, ecu_logical_address)
# conn = DoIPClientUDSConnector(doip_client)
# with Client(conn,  request_timeout=2, config=MyCar.config) as client:
#     try:
#         print('hhhh')
#         client.change_session(DiagnosticSessionControl.Session.extendedDiagnosticSession)  # integer with value of 3
#         #client.unlock_security_access(MyCar.debug_level)                                   # Fictive security level. Integer coming from fictive lib, let's say its value is 5
#         #client.write_data_by_identifier(udsoncan.DataIdentifier.VIN, 'ABC123456789')       # Standard ID for VIN is 0xF190. Codec is set in the client configuration
#         #print('Vehicle Identification Number successfully changed.')
#         #client.ecu_reset(ECUReset.ResetType.hardReset)                                     # HardReset = 0x01
#     except NegativeResponseException as e:
#         print('Server refused our request for service %s with code "%s" (0x%02x)' % (e.response.service.get_name(), e.response.code_name, e.response.code))
#     except InvalidResponseException as e:
#         print('Server sent an invalid payload : %s' % e.response.original_payload)

from uds import Uds
ecu = Uds(transportProtocol="DoIP", ecu_ip="172.31.7.1")
try:
    ecu.send([0x3E, 0x80], responseRequired=False)
    #print(response)  # This should be [0x7E, 0x00]
    for i in range(10):
        response = ecu.send([0x10, 0x03])
        #response = ecu.send([0x22, 0xf1, 0x90])
        #response = ecu.send([0x27, 0x01])
        print(response)

except:
    print("Send did not complete")

ecu.disconnect()

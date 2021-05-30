from DoipClient import DoipClient
from DoipJsonFormat import GW04_ALL_NODE
import time

def main():
    client = DoipClient()

    client.setTesterAddress(0xe80)

    client.creatUdpSoad()
    #client.sendMsgTest()
    client.sendVehAncMsg()
    client.sendRouteActiveReq()
    
    #client.sendDiagMsg()
    for node in GW04_ALL_NODE:#GW04_ALL_NODE[-1:]
        client.setTargetAddress(node['LOGICAL_ADD'])
        print('Target ECU {0}, {1}, {2}'.format(node['MCU_NAME'], hex(client._targetAddress), node['CAN_NAME']))
        client.sendDiagMsgToNode()
        time.sleep(1)

    client.closeUdpSoad() 
    client.closeTcpSoad() 


    # while(1):
    #     pass

if __name__ == "__main__":
    main()
    # print('hello')

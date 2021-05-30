from DoipHeader import *
import socket

class DoipClient:

    def __init__(self, testerAddress=0x0E80, targetAddress=0x1000, targetIP='172.31.6.1'):
        self._testerAddress = testerAddress
        self._targetAddress = targetAddress
        self._timeout = 3

        self._targetIP = targetIP
        self._addr = (targetIP, 13400)

        self._buffSize = 1024
        

    def creatUdpSoad(self):
        self._udpSoad = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._udpSoad.settimeout(self._timeout)
        
    def closeUdpSoad(self):
        self._udpSoad.close()

    def creatTcpSoad(self):
        self._tcpSoad = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._tcpSoad.settimeout(self._timeout)
        self._tcpSoad.connect(self._addr)

    def closeTcpSoad(self):
        self._tcpSoad.close()

    def socketConnect(self):
        self.creatUdpSoad()
        self.creatTcpSoad()

    def socketClose(self):
        self.closeTcpSoad()
        self.closeUdpSoad()

    def sendVehAncMsg(self):
        vehAncMsg = DoipHeader(DOIP_VehIdReqMsg)
        print(parseDoipHeader(vehAncMsg.getPayload(), 'tx'))
        self._udpSoad.sendto(vehAncMsg.getPayload(), self._addr)
        self.receiveUdpMsg()

    def sendMsgTest(self):
        for payloadType in payloadTypeDict.keys():
            msg = DoipHeader(payloadType)
            #print(vehAncMsg._payloadLength)
            self._udpSoad.sendto(msg.getPayload(), self._addr)
    
    def receiveUdpMsg(self):
        revData, ECUaddr = self._udpSoad.recvfrom(self._buffSize)
        print(parseDoipHeader(revData, 'rx'))

    def receiveTcpMsg(self):
        revData, ECUaddr = self._tcpSoad.recvfrom(self._buffSize)
        print(parseDoipHeader(revData, 'rx'))

    def sendDiagMsg(self):
        diagMsg = DoipHeader(DOIP_DiagMsg, 2)
        diagMsg.setDiagMsg([0x10, 0x03])
        print(parseDoipHeader(diagMsg.getPayload(), 'tx'))
        self._tcpSoad.send(diagMsg.getPayload())
        print("diag msg send success")
        self.receiveTcpMsg()
        self.receiveTcpMsg()

        readDid = DoipHeader(DOIP_DiagMsg, 3)
        readDid.setDiagMsg([0x22, 0xf1, 0xa8])
        self._tcpSoad.send(readDid.getPayload())
        self.receiveTcpMsg()
        self.receiveTcpMsg()

    def sendRouteActiveReq(self):
        routeActiveReqMsg = DoipHeader(DOIP_RoutingActiveReq)
        routeActiveReqMsg.setSourceAddress(self._testerAddress)
        print(parseDoipHeader(routeActiveReqMsg.getPayload(), 'tx'))
        self._tcpSoad.send(routeActiveReqMsg.getPayload())
        print("route active msg send success")
        self.receiveTcpMsg()
        
    def sendDiagMsgToNode(self):
        diagMsg = DoipHeader(DOIP_DiagMsg, 2)
        diagMsg.setDiagMsg([0x10, 0x03], self._testerAddress, self._targetAddress)
        print(parseDoipHeader(diagMsg.getPayload(), 'tx'))
        self._tcpSoad.send(diagMsg.getPayload())
        try: 
            self.receiveTcpMsg()# doip response
            self.receiveTcpMsg()# doip uds response
        except socket.timeout:
            print("****************************Receive timeout: {0}".format(self._targetAddress))
        
        

    def setTesterAddress(self, testerAddress):
        self._testerAddress = testerAddress
        
    def setTargetAddress(self, targetAddress):
        self._targetAddress = targetAddress

def main():
    client = DoipClient()
    client.creatUdpSoad()
    #client.sendMsgTest()
    client.sendVehAncMsg()
    client.sendRouteActiveReq()
    #client.sendDiagMsg()
    client.sendDiagMsgToNode()
    client.closeUdpSoad() 
    client.closeTcpSoad() 


    # while(1):
    #     pass

if __name__ == "__main__":
    main()
    # print('hello')

    
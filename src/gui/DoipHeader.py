

DOIP_GenericDoipNACK = 0x0000
DOIP_VehIdReqMsg = 0x0001
DOIP_VehIdReqMsgWithEID = 0x0002
DOIP_VehIdReqMsgWithVIN = 0x0003
DOIP_VehAncRespmsg = 0x0004
DOIP_RoutingActiveReq = 0x0005
DOIP_RoutingActiveResp = 0x0006
DOIP_AliveCheckReq = 0x0007
DOIP_AliveCheckResp = 0x0008
DOIP_DoipEntityStatusReq = 0x4001
DOIP_DoipEntityStatusResp = 0x4002
DOIP_DiagPWMReq = 0x4003
DOIP_DiagPWMResp = 0x4004
DOIP_DiagMsg = 0x8001
DOIP_DiagMsgPACK = 0x8002
DOIP_DiagMsgNACK = 0x8003

payloadTypeDict = {
DOIP_GenericDoipNACK : 0,
DOIP_VehIdReqMsg : 1,
DOIP_VehIdReqMsgWithEID : 2,
DOIP_VehIdReqMsgWithVIN : 3,
DOIP_VehAncRespmsg : 4,
DOIP_RoutingActiveReq : 5,
DOIP_RoutingActiveResp : 6,
DOIP_AliveCheckReq : 7,
DOIP_AliveCheckResp : 8,
DOIP_DoipEntityStatusReq : 9,
DOIP_DoipEntityStatusResp : 10,
DOIP_DiagPWMReq : 11,
DOIP_DiagPWMResp : 12,
DOIP_DiagMsg : 13,
DOIP_DiagMsgPACK : 14,
DOIP_DiagMsgNACK : 15,
}

HeaderFormat = [
    {
        'msgType' : 'GenericDoipNACK',
        'payloadType' : DOIP_GenericDoipNACK,
        'payloadLength' : 1,
    },
    {
        'msgType' : 'VehIdReqMsg',
        'payloadType' : DOIP_VehIdReqMsg,
        'payloadLength' : 0,
    },
    {
        'msgType' : 'VehIdReqMsgWithEID',
        'payloadType' : DOIP_VehIdReqMsgWithEID,
        'payloadLength' : 6,
    },
    {
        'msgType' : 'VehIdReqMsgWithVIN',
        'payloadType' : DOIP_VehIdReqMsgWithVIN,
        'payloadLength' : 17,
    },
    {
        'msgType' : 'VehAncRespmsg',
        'payloadType' : DOIP_VehAncRespmsg,
        'payloadLength' : 33,
    },
    {
        'msgType' : 'RoutingActiveReq',
        'payloadType' : DOIP_RoutingActiveReq,
        'payloadLength' : 11,
    },
    {
        'msgType' : 'RoutingActiveResp',
        'payloadType' : DOIP_RoutingActiveResp,
        'payloadLength' : 13,
    },
    {
        'msgType' : 'AliveCheckReq',
        'payloadType' : DOIP_AliveCheckReq,
        'payloadLength' : 0,
    },
    {
        'msgType' : 'AliveCheckResp',
        'payloadType' : DOIP_AliveCheckResp,
        'payloadLength' : 2,
    },
    {
        'msgType' : 'DoipEntityStatusReq',
        'payloadType' : DOIP_DoipEntityStatusReq,
        'payloadLength' : 0,
    },
    {
        'msgType' : 'DoipEntityStatusResp',
        'payloadType' : DOIP_DoipEntityStatusResp,
        'payloadLength' : 7,
    },
    {
        'msgType' : 'DiagPWMReq',
        'payloadType' : DOIP_DiagPWMReq,
        'payloadLength' : 0,
    },
    {
        'msgType' : 'DiagPWMResp',
        'payloadType' : DOIP_DiagPWMResp,
        'payloadLength' : 1,
    },
    {
        'msgType' : 'DiagMsg',
        'payloadType' : DOIP_DiagMsg,
        'payloadLength' : 0,
    },
    {
        'msgType' : 'DiagMsgPACK',
        'payloadType' : DOIP_DiagMsgPACK,
        'payloadLength' : 0,
    },
    {
        'msgType' : 'DiagMsgNACK',
        'payloadType' : DOIP_DiagMsgNACK,
        'payloadLength' : 0,
    }

]

class DoipHeader:

    def __init__(self, payloadType, diagMsgLength=0):
        
        if diagMsgLength:
            payloadLength = diagMsgLength + 4
        else:
            payloadLength = HeaderFormat[payloadTypeDict[payloadType]]['payloadLength']
        #print(payloadLength)
        self._payload = [0x0] * (payloadLength+8)
        self.setProtocolVerion()
        self.setPayloadType(payloadType)
        self.setPayloadLength(payloadLength)

    def setProtocolVerion(self):
        self._payload[0] = 0x02
        self._payload[1] = self._payload[0] ^ 0xff

    def setPayloadType(self, payloadType):
        if payloadType in payloadTypeDict.keys():
            self._payload[2] = payloadType // 256
            self._payload[3] = payloadType % 256
        else:
            self._payload[2] = 0x00
            self._payload[3] = 0x00
        self._payloadType = payloadTypeDict.get(payloadType, "payloadType Error!")

    def setPayloadLength(self, payloadLength):
        self._payloadLength = payloadLength
        self._payload[4] = payloadLength >> 8*3
        self._payload[5] = payloadLength >> 8*2
        self._payload[6] = payloadLength >> 8
        self._payload[7] = payloadLength % 256

    def setSourceAddress(self, testerAddress=0x0E80):
        if self._payloadType == payloadTypeDict.get(DOIP_RoutingActiveReq, "payloadType Error!"):
            self._payload[8] = testerAddress >> 8
            self._payload[9] = testerAddress % 256

    def __str__(self):
        payloadStr = ''.join(['%02x ' % v for v in self._payload])
        return payloadStr
    
    def getPayload(self):
        return bytes(self._payload)

    def setDiagMsg(self, diagMsg, testerAddress=0x0E80, targetAddress=0x1000):
        if (len(diagMsg) +4 + 8) != len(self._payload):
            print('ERROR: DIAG MSG Len error')
        else:
            self._payload[8] = testerAddress >> 8
            self._payload[9] = testerAddress % 256
            self._payload[10] = targetAddress >> 8
            self._payload[11] = targetAddress % 256
            for i in range(len(diagMsg)):
                self._payload[-(i+1)] = diagMsg[-(i+1)]

def parseDoipHeader(bytesData, dirrection):
    dataArray = list(bytesData)
    if dirrection == 'rx':
        dirrStr = 'receive'
    elif dirrection == 'tx':
        dirrStr = 'tranmit'
    else:
        dirrStr = 'ERROR'
    payloadType = (dataArray[2] << 8) + dataArray[3]
    if payloadType in payloadTypeDict.keys():
        payloadTypeStr = HeaderFormat[payloadTypeDict[payloadType]]['msgType']
        
        #parseData = '{0} DoIP message: {1}, payload length is{2}, and payload is {3}'.format(dirrStr, payloadTypeStr, dataArray[4:8], dataArray[8:])
        parseData = '{0} DoIP message: {1:>20}, payload length is {2:>5}, and payload is {3}'.format(dirrStr, payloadTypeStr, cmpLenFromList(dataArray[4:8]),formatDataList(dataArray[8:]))
        # parseDataAppend = [hex(i) for i in dataArray[8:]]
        
    else:
        parseData = 'Parse ERROR!'
        # print('receive DoIP message: {0}, payload is {1}'.format(payloadTypeStr, dataArray[4:]))
    
    return parseData

def cmpLenFromList(lenList):
    listLen = 0
    for i in range(len(lenList)):
        listLen += lenList[-i-1] << 8*i

    return listLen

def formatDataList(dataList):
    formatRes = ''
    for i in dataList:
        if i<16:
            res = '0' + hex(i)[2:]
        else:
            res = hex(i)[2:]
        formatRes = formatRes+res + ' '
    
    return formatRes

if __name__ == "__main__":
    testList = [0x2d, 0x57, 0xc2, 0x10]
    print(cmpLenFromList(testList))
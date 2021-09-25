from lxml import etree
import logging

class Arxml_Parser:

    def __init__(self, fileName):
        self._file_name = fileName
        self._name_space = {'test_ns':'http://autosar.org/schema/r4.0'}
        self._root = self.get_arxml_root()
        self._pdus = self._init_pdus()

    def _init_pdus(self):
        pdus = {}
        pdu_list = self.get_pdu()
        for pdu in pdu_list:
            pdu_info = self.parsePdu(pdu)
            pdus[pdu_info['pdu_name']] = pdu_info

        return pdus

    def get_pdu_info_by_pduname(self, pduname):
        return self._pdus[pduname]

    def get_fibex_element_by_class(self):
        fibex_element = self._root.xpath('.//test_ns:FIBEX-ELEMENT-REF', namespaces=self._name_space)
        # print(len(fibex_element))
        # print(fibex_element[0].get('DEST'))

        res = {}
        for element in fibex_element:
            dest_name = element.get('DEST')
            element_value = element.text
            idx = element_value.rfind('/') + 1
            element_value = element_value[idx:]

            if dest_name in res:
                res[dest_name].append(element_value)
            else:
                res[dest_name] = [element_value]

        # for k,v in res.items():
        #     print(k, v)

        return res

    def get_PR_port(self):
        sender_receiver = self._root.xpath('.//test_ns:SENDER-RECEIVER-TO-SIGNAL-MAPPING', namespaces=self._name_space)
        # sender_receiver = self._root.xpath('.//test_ns:SYSTEM-SIGNAL-REF', namespaces=self._name_space)
        # print(len(sender_receiver))
        # for i in sender_receiver:
            # print(i.text)

    def get_can_frame(self):
        can_frame = self._root.xpath('.//test_ns:CAN-FRAME', namespaces=self._name_space)
        # print(len(can_frame))
        return can_frame

    def get_pdu(self):
        pdu = []
        isignal_ipdu = self._root.xpath('.//test_ns:I-SIGNAL-I-PDU', namespaces=self._name_space)
        pdu.extend(isignal_ipdu)
        logging.debug('isignal_ipdu number is {}'.format(len(isignal_ipdu)))

        n_pdu = self._root.xpath('.//test_ns:N-PDU', namespaces=self._name_space)
        pdu.extend(n_pdu)
        logging.debug('n_pdu number is {}'.format(len(n_pdu)))

        nm_pdu = self._root.xpath('.//test_ns:NM-PDU', namespaces=self._name_space)
        pdu.extend(nm_pdu)
        logging.debug('nm_pdu number is {}'.format(len(nm_pdu)))

        container_ipdu = self._root.xpath('.//test_ns:CONTAINER-I-PDU', namespaces=self._name_space)
        pdu.extend(container_ipdu)
        logging.debug('container_ipdu number is {}'.format(len(container_ipdu)))

        return pdu

    def parseCanFrame(self, canFrame):
        canFrameInfo = {}
        SHORT_NAME = canFrame.xpath('.//test_ns:SHORT-NAME', namespaces=self._name_space)
        short_name_text = Arxml_Parser.getTextValue(SHORT_NAME)
        canFrameInfo['frame_name'] = short_name_text

        FRAME_LENGTH = canFrame.xpath('.//test_ns:FRAME-LENGTH', namespaces=self._name_space)
        frame_length_text = Arxml_Parser.getTextValue(FRAME_LENGTH)
        canFrameInfo['frame_len'] = int(frame_length_text)

        PDU_REF = canFrame.xpath('.//test_ns:PDU-REF', namespaces=self._name_space)
        pdu_name_text = Arxml_Parser.getTextValue(PDU_REF)
        idx = pdu_name_text.rfind('/')
        canFrameInfo['pdu_name'] = pdu_name_text[idx + 1:]
        #
        canFrameInfo['pdu_type'] = PDU_REF[0].get('DEST')
        # print(canFrameInfo)
        return canFrameInfo

    def parsePdu(self, pduElement):
        pduInfo = {}

        pdu_type = pduElement.tag
        idx = pdu_type.find('}')
        pduInfo['pdu_type'] = pdu_type[idx+1:]
        # logging.debug(pduInfo['pdu_type'])
        pduInfo['pdu_name'] = self.get_text_value_from_tag_by_format('.//test_ns:SHORT-NAME', pduElement)

        pduInfo['pdu_length'] = self.str2value(self.get_text_value_from_tag_by_format('.//test_ns:LENGTH', pduElement), int)

        period = self.get_text_value_from_tag_by_format('.//test_ns:TIME-PERIOD/test_ns:VALUE', pduElement)
        pduInfo['period'] = int(self.str2value(period, float) * 1000)

        if pduInfo['period'] == 0:
            pduInfo['period'] = self.parse_pdu_period_by_name(pduInfo['pdu_name'])

        # logging.debug(pduInfo)
        return pduInfo

    def parse_pdu_period_by_name(self, name):
        idx_ms = name.find('ms')
        if idx_ms != -1:
            idx_ = name.rfind('_', 0, idx_ms)
            if idx_ != -1:
                peroid = name[idx_+1:idx_ms]

                return self.str2value(peroid, int)
        else:
            return 0

    def get_can_frame_triggering(self):
        can_frame_triggering = self._root.xpath('.//test_ns:CAN-FRAME-TRIGGERING', namespaces=self._name_space)
        # print(len(can_frame_triggering))

        return can_frame_triggering

    def parseFrameTriggering(self, frameTriggering):
        frameInfo = {}
        FRAME_REF = frameTriggering.xpath('./test_ns:FRAME-REF', namespaces=self._name_space)

        frame_name_text = Arxml_Parser.getTextValue(FRAME_REF)
        idx = frame_name_text.rfind('/') + 1
        frameInfo['frame_name'] = frame_name_text[idx:]

        FRAME_PORT_REF = frameTriggering.xpath('.//test_ns:FRAME-PORT-REF', namespaces=self._name_space)
        frame_direct_text = Arxml_Parser.getTextValue(FRAME_PORT_REF)
        idx = frame_direct_text.rfind('/') + 1
        frameInfo['frame_direct'] = frame_direct_text[idx:]

        CAN_FD_SUPPORT = frameTriggering.xpath('.//test_ns:CAN-FD-FRAME-SUPPORT', namespaces=self._name_space)
        is_can_fd = Arxml_Parser.getTextValue(CAN_FD_SUPPORT)
        frameInfo['is_can_fd'] = is_can_fd

        PDU_TRIGGERING_REF = frameTriggering.xpath('.//test_ns:PDU-TRIGGERING-REF', namespaces=self._name_space)
        pdu_text = Arxml_Parser.getTextValue(PDU_TRIGGERING_REF)
        idx_1 = pdu_text.rfind('/')
        idx_2 = pdu_text.rfind('/', 0, idx_1)
        frameInfo['frame_pdu'] = pdu_text[idx_1 + 6:]
        frameInfo['frame_controller'] = pdu_text[idx_2 + 5:idx_1]

        IDENTIFIER = frameTriggering.xpath('.//test_ns:IDENTIFIER', namespaces=self._name_space)
        id_text = Arxml_Parser.getTextValue(IDENTIFIER)
        # print(id_text)
        id_num = hex(int(id_text))
        if len(id_num) < 6:
            id_num = '0x' + (6 - len(id_num)) * '0' + id_num[2:]
        frameInfo['frame_ID'] = id_num

        # print(frameInfo)
        return frameInfo

    def get_Pdu_container(self):
        ar_package = self._root.xpath('.//test_ns:AR-PACKAGE[contains(@UUID, "Communication-Pdu")]/test_ns:ELEMENTS', namespaces=self._name_space)
        logging.debug('find pdu container length is {}'.format(len(ar_package)))
        for pdu in ar_package[0]:
            logging.debug((pdu.tag))

    def get_text_value_from_tag_by_format(self, format, tag):
        filter_element = tag.xpath(format, namespaces=self._name_space)
        filter_element_text = Arxml_Parser.getTextValue(filter_element)
        return filter_element_text

    def str2value(self, src, fmt):

        try:
            dest = fmt(src)
        except ValueError as e:
            # logging.debug('value convert failed!')
            dest = 0
        return dest

    def get_arxml_root(self):
        parser = etree.XMLParser(remove_blank_text=True)
        etree.register_namespace('test_ns', self._name_space['test_ns'])
        tree = etree.parse(self._file_name, parser=parser)

        # etree.register_namespace(name, vaule)

        root = tree.getroot()
        # root.register_namespace(namesapce)
        return root

    @staticmethod
    def getTextValue(et_list):
        if len(et_list) == 0:
            return ''
        else:
            return et_list[0].text

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    ap = Arxml_Parser('SI_20210816-qy1-AS32_PP_GW-Arxml-V05.7-update.arxml')
    res = ap.get_fibex_element_by_class()

    can_frame = res['CAN-FRAME']
    pdu = res['I-SIGNAL-I-PDU']
    signal = res['I-SIGNAL']
    signal_grp = res['I-SIGNAL-GROUP']

    print('can frame number is ', len(can_frame))
    print('pdu number is ', len(pdu))
    print('signal number is ', len(signal))
    print('signal group number is ', len(signal_grp))

    ap.get_PR_port()
    frame_list = ap.get_can_frame()
    frame_triggering_list = ap.get_can_frame_triggering()

    logging.debug('frame number is {}'.format(len(frame_list)))
    ap.get_can_frame_triggering()
    ap.parseCanFrame(frame_list[0])
    ap.parseFrameTriggering(frame_triggering_list[0])

    # print(ap.str2value('0', int))
    # print(ap.str2value('0.1', float))
    # print(ap.str2value('', int))

    # pdu_list = ap.get_pdu()
    # for i in pdu_list:
    #     ap.parsePdu(i)

    # ap.parse_pdu_period_by_name('SCS_020ms_PDU15')

    ap.get_Pdu_container()
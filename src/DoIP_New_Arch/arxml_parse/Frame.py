from lxml import etree
from enum import IntEnum
from Arxml_Parser import Arxml_Parser
import logging

class Frame:

    class Packing_Byte_Order(IntEnum):
        MOST_SIGNIFICANT_BYTE_LAST = 0
        LEAST_SIGNIFICANT_BYTE_LAST = 1

    class Frame_Direction(IntEnum):
        FRAME_IN = 0
        FRAME_OUT = 1

    class Frame_Controller(IntEnum):
        PTCAN = 0
        PTEXTCANFD = 1
        CHCANFD = 2
        DIAGCAN = 3
        CNCAN = 4
        CFCAN = 5
        ADCANFD = 6
        CCP_Lin1Cluster = 7
        CCP_Lin2Cluster = 8
        PTEXTCAN2 = 9

    def __init__(self, frame_triggering_element, can_frame_element):
        self.frame_name = ''
        self.frame_length = 0
        self.pdu = None
        self.pdu_start_position = 0
        self.byte_order = Frame.Packing_Byte_Order.MOST_SIGNIFICANT_BYTE_LAST
        self.frame_direction = Frame.Frame_Direction.FRAME_IN
        self.identifier = 0x0
        # self.address_mode = STAND
        self.is_FD_frame = False
        self.controller = ''

        self._init_from_frame_triggering_element(frame_triggering_element)
        
        self._init_from_can_frame_element(can_frame_element)
        
    def _init_from_frame_triggering_element(self, frame_triggering_info):

        # frame_triggering_info = Arxml_Parser.parseFrameTriggering(frame_triggering_element)
        # print(frame_triggering_info)
        self.frame_name = frame_triggering_info['frame_name']
        if frame_triggering_info['frame_direct'] == 'FramePort_In':
            self.frame_direction = Frame.Frame_Direction.FRAME_IN
        else:
            self.frame_direction = Frame.Frame_Direction.FRAME_OUT
        self.identifier = frame_triggering_info['frame_ID']
        self.is_FD_frame = False

        self.controller = frame_triggering_info['frame_controller']

    def _init_from_can_frame_element(self, frame_info):
        # frame_info = Arxml_Parser.parseCanFrame(can_frame_element)
        # print(frame_info)
        self.frame_length = frame_info['frame_len']
        self.pdu = frame_info['pdu_name']

class Pdu:

    def __init__(self):
        self.pdu_name = ''
        self.pdu_length = 0
        self.period = 0
        self.signal_number = 0
        self.signals = None



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    ap = Arxml_Parser('SI_20210611-xx3-AS32_PPV_GW-Arxml-V05.6.arxml')
    frame_list = ap.get_can_frame()
    frame_triggering_list = ap.get_can_frame_triggering()
    frame_info = ap.parseCanFrame(frame_list[0])
    frame_triggering_info = ap.parseFrameTriggering(frame_triggering_list[0])
    logging.debug('frame len is {}, frame trigger len is {}'.format(len(frame_list), len(frame_triggering_list)))
    frame = Frame(frame_triggering_info, frame_info)

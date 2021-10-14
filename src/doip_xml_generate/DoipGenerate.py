from ArxmlBase import ArxmlBase
import logging
from DoipJsonFormat import *
import copy

class GenerateBase:

    def __init__(self, module, project):
        self._project = project
        self._template_file = 'GW04_{}_template.xml'.format(module)
        self._generate_xml_file = 'GW04_{}_ecuc_{}.arxml'.format(module, project)
        self._arxml_parse = ArxmlBase(self._template_file)
        self.get_ecu_node(project)
        # logging.debug(self.ecu_node)

    def get_ecu_node(self, project):
        # logging.debug(project)
        if project == 'AS32':
            self.ecu_node = GW04_ALL_NODE_AS32
        elif project == 'AS33':
            self.ecu_node = GW04_ALL_NODE_AS33

    def generate_arxml(self):
        self._arxml_parse.xml_write_to_file(self._generate_xml_file)

class DoIPGenerate(GenerateBase):

    # DOIP_TEMPLATE_FILE = 'GW04_DoIP_template.xml'

    def __init__(self, project):
        super(DoIPGenerate, self).__init__('DoIP', project)
        # self._generate_xml_file = 'GW04_DoIP_ecuc_{}.arxml'.format(project)
        # self._arxml_parse = ArxmlBase(self.TEMPLATE_FILE)
        # logging.debug(self.ecu_node)
        self.get_DoIPConfigSet_subcontainer()
        self.get_DoIPConnections_subcontainer()
        self.append_containers()
        self.generate_arxml()




    def get_DoIPConfigSet_subcontainer(self):
        sub_container = self._arxml_parse.get_first_child_by_xpath(self._arxml_parse.arxml_root, './/test_ns:CONTAINERS/test_ns:ECUC-CONTAINER-VALUE/test_ns:SUB-CONTAINERS')
        self._doipConfigsetSubcontainer = sub_container
        return sub_container

    def get_DoIPConnections_subcontainer(self):
        sub_container = self._arxml_parse.get_first_child_by_xpath(self._doipConfigsetSubcontainer, './test_ns:ECUC-CONTAINER-VALUE/test_ns:SUB-CONTAINERS')
        self._doipConnectionsSubcontainer = sub_container
        return sub_container

    def append_containers(self):
        self.append_connections()
        self.append_channel()
        self.append_route_activation()
        self.append_tester()

    def append_connections(self):
        for is_remote in range(2):
            for node_dir in self.ecu_node:
                new_target_addr_dir = creat_new_target_Address(node_dir, is_remote=is_remote)
                new_target_addr = etree.Element('ECUC-CONTAINER-VALUE')
                parseData(new_target_addr_dir['ECUC-CONTAINER-VALUE'], new_target_addr)
                self._doipConnectionsSubcontainer.append(new_target_addr)

            # func target address
            func_target_addr = creat_new_target_Address(GW04_FUNC_TARGET_ADDRESS_DIR, is_remote=is_remote)
            new_func_target_addr = etree.Element('ECUC-CONTAINER-VALUE')
            parseData(func_target_addr['ECUC-CONTAINER-VALUE'], new_func_target_addr)
            self._doipConnectionsSubcontainer.append(new_func_target_addr)

    def append_channel(self):
        # creat all phy node channel
        rx_start_id = 0
        tx_start_id = 0
        for is_remote in range(2):
            for channel_dir in self.ecu_node:
                channel_dir = creat_new_phy_channel(channel_dir, rx_start_id, tx_start_id, is_remote=is_remote)
                new_channel = etree.Element('ECUC-CONTAINER-VALUE')
                parseData(channel_dir['ECUC-CONTAINER-VALUE'], new_channel)
                rx_start_id = rx_start_id + 1
                tx_start_id = tx_start_id + 1

                self._doipConfigsetSubcontainer.append(new_channel)

        # creat func channel
        for is_remote in range(2):
            new_channel = etree.Element('ECUC-CONTAINER-VALUE')
            channel_dir = creat_new_fun_channel(GW04_FUN_DIR, rx_start_id, is_remote=is_remote)
            parseData(channel_dir['ECUC-CONTAINER-VALUE'], new_channel)
            rx_start_id = rx_start_id + 1

            self._doipConfigsetSubcontainer.append(new_channel)


    def append_route_activation(self):
        '''
        append route activation container to configset
        :return:
        '''
        for is_remote in range(2):
            new_DoIPRoutingActivation = etree.Element('ECUC-CONTAINER-VALUE')
            new_DoIPRoutingActivation_dir = creat_new_DoIPRoutingActivation(is_remote, is_remote=is_remote)
            parseData(new_DoIPRoutingActivation_dir['ECUC-CONTAINER-VALUE'], new_DoIPRoutingActivation)
            self._doipConfigsetSubcontainer.append(new_DoIPRoutingActivation)

    def append_tester(self):
        '''
        append tester container to configset
        :return:
        '''
        for is_remote in range(2):
            new_tester = etree.Element('ECUC-CONTAINER-VALUE')
            new_tester_dir = creat_new_Tester(GW04_TESTER_ADDR[is_remote], is_remote=is_remote)
            parseData(new_tester_dir['ECUC-CONTAINER-VALUE'], new_tester)
            self._doipConfigsetSubcontainer.append(new_tester)



class EcucGenerate(GenerateBase):


    def __init__(self, project):
        super().__init__('EcuC', project)
        # self._generate_xml_file = 'GW04_EcuC_{}.arxml'.format(project)
        self.get_Pdus()
        self.get_ecuc_container()
        self.get_ecuc_subcontainer()
        self.append_pdus()

        self.generate_arxml()


    def get_Pdus(self):
        pdu_names = []
        ## generate phys ecuc pdu names
        for is_remote in range(2):
            if is_remote:
                local_or_remote_str = 'Remote'
            else:
                local_or_remote_str = 'Local'

            for channel_dir in self.ecu_node:
                # if channel_dir['MCU_NAME'] == 'GW':
                #     continue


                pdu_names.append('DCM_DoIP_{0}_PhysReq_{1}_Rx'.format(local_or_remote_str, channel_dir['MCU_NAME']))
                pdu_names.append('DCM_DoIP_{0}_PhysResp_{1}_Tx'.format(local_or_remote_str, channel_dir['MCU_NAME']))

            pdu_names.append('DCM_DoIP_{0}_FuncReq_Rx'.format(local_or_remote_str))
            pdu_names.append('DCM_UDS_{0}_FuncReq_Rx'.format(local_or_remote_str))
            pdu_names.append('DCM_UDS_{0}_PhysReq_Rx'.format(local_or_remote_str))
            pdu_names.append('DCM_UDS_{0}_PhysResp_Tx'.format(local_or_remote_str))

        self._pdus = pdu_names

    def get_ecuc_container(self):
        sub_container = self._arxml_parse.get_first_child_by_xpath(self._arxml_parse.arxml_root,
                                                                   './/test_ns:SUB-CONTAINERS')
        self._subcontainer = sub_container
        return sub_container

    def get_ecuc_subcontainer(self):
        ecuc_container = self._arxml_parse.get_first_child_by_xpath(self._subcontainer,
                                                                   './test_ns:ECUC-CONTAINER-VALUE')
        self._ecu_container = ecuc_container
        return ecuc_container

    def append_pdus(self):
        logging.debug('**********************ECUC PDU GENERATE START**********************')
        logging.debug('ECUC: Add global pdu number is {}'.format(len(self._pdus)))
        for pdu_name in self._pdus[1:]:
            new_pdu_container = copy.deepcopy(self._ecu_container)
            # new_pdu_container_short_name = new_pdu_container.xpath('./test_ns:SHORT-NAME', namespaces=ns)
            new_pdu_container_short_name = self._arxml_parse.get_first_child_by_xpath(new_pdu_container,
                                                                   './test_ns:SHORT-NAME')
            new_pdu_container_short_name.text = pdu_name
            logging.debug('ECUC: Add global pdu {}'.format(pdu_name))
            self._subcontainer.append(new_pdu_container)

        logging.debug('**********************ECUC PDU GENERATE END**********************')
class PdurGenerate(GenerateBase):

    def __init__(self, project):
        super(PdurGenerate, self).__init__('PduR', project)
        # self.get_DoIPConfigSet_subcontainer()
        # self.get_DoIPConnections_subcontainer()
        self.get_subcontainer()
        self.append_containers()
        self.generate_arxml()


    def get_subcontainer(self):
        sub_container = self._arxml_parse.get_first_child_by_xpath(self._arxml_parse.arxml_root,
                                                                   './/test_ns:SUB-CONTAINERS/test_ns:ECUC-CONTAINER-VALUE/test_ns:SUB-CONTAINERS')
        self._pudrPathSubcontainer = sub_container
        return sub_container

    def append_containers(self):
        i = 0
        logging.debug('**********************PDUR PATH GENERATE START**********************')
        diag_pdus = self.get_ecuc_pdu_with_uuid('{}_GW04_EcuC_ecuc.arxml'.format(self._project))
        for is_remote in range(2):
            for node_dir in self.ecu_node:
                path_dir = creat_new_pudr_path(node_dir, diag_pdus, is_remote=is_remote)
                # logging.debug(len(path_dir))
                for path_dir_tmp in path_dir:
                    path = etree.Element('ECUC-CONTAINER-VALUE')
                    parseData(path_dir_tmp['ECUC-CONTAINER-VALUE'], path)
                    self._pudrPathSubcontainer.append(path)
                    i = i + 1
        logging.debug('PDUR: Add PDUR path number is {}'.format(i))
        logging.debug('**********************PDUR PATH GENERATE END**********************')

    def get_ecuc_pdu_with_uuid(self, ecuc_xml_file):
        diag_can_pdus = {}
        # i=0
        ecuc_arxml_parse = ArxmlBase(ecuc_xml_file)
        subcontainer = ecuc_arxml_parse.get_all_childs_by_xpath(ecuc_arxml_parse.arxml_root, './/test_ns:CONTAINERS/test_ns:ECUC-CONTAINER-VALUE/test_ns:SUB-CONTAINERS//test_ns:SHORT-NAME')
        for et in subcontainer:
            et_text = et.text
            if 'DCM_DIAG' in et_text:
                et_text_split = et_text.split('_')
                if len(et_text_split) == 6:
                    if et_text_split[3] == 'CCP':
                        key_str = 'GW' + '_' + et_text_split[2] + '_' + et_text_split[5]
                    else:
                        key_str = et_text_split[3] + '_' + et_text_split[2] + '_' + et_text_split[5]
                    diag_can_pdus[key_str] = et_text
                    logging.debug(key_str + '****' + diag_can_pdus[key_str])

        return diag_can_pdus

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    project = 'AS33'
    doip_generate = DoIPGenerate(project)
    ecuc_generate = EcucGenerate(project)
    pdur_generate = PdurGenerate(project)
    pdur_generate.get_ecuc_pdu_with_uuid('AS33_GW04_EcuC_ecuc.arxml')
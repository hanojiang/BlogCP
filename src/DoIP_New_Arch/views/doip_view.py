from PySide2.QtWidgets import QMainWindow, QAction, QTableWidgetItem, QFormLayout, QLabel, QLineEdit, QListWidgetItem, QFileDialog
from PySide2.QtCore import Slot
from views.Doip_gui_view import Ui_MainWindow
from controllers.doip_controller import DoIP_Controller
from model.doip_model import Model
from Ecu_Const import *
from xml_generate.DoipGenerate import *
import logging

class MainView(QMainWindow):
    def __init__(self, model:Model, controller:DoIP_Controller):
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.set_doip_parameter()

        self.__init_all_components()
        self.__init_all_actions()


    @Slot()
    def set_doip_parameter(self):
        ecu_ip_address = self._ui.ecuIpAddressLineEdit.text()
        ecu_logical_address = int(self._ui.ecuLogicalAddressLineEdit.text(), 16)
        tester_ip_address = self._ui.testerIpAddresslineEdit.text()
        tester_logical_address = int(self._ui.testerLogicalAddressLineEdit.text(), 16)
        self._controller.set_doip_parameter(ecu_ip_address, tester_ip_address, ecu_logical_address, tester_logical_address)

    @Slot()
    def on_loopbackIPSettingButton_pressed(self):
        ecu_ip_address = '127.0.0.1'
        tester_ip_address = '127.0.0.1'
        self._ui.ecuIpAddressLineEdit.setText(ecu_ip_address)
        self._ui.testerIpAddresslineEdit.setText(tester_ip_address)
        self.set_doip_parameter()


    def __init_all_components(self):
        self.__init_sidSeclectBox()
        self.__init_projectSeclectBox()
        self.__init_ecuSeclectBox()
        self.__init_canSeclectBox()
        self.__init_ecuNodeInfoListWidget()
        self.__init_logitic_data_read_table()
        self.__set_pushbutton_status(False)

    def __init_sidSeclectBox(self):

        self._ui.sidSeclectBox.addItems(DIAG_SID)

    def __init_ecuSeclectBox(self):
        self._ui.ecuSeclectBox.clear()
        # self._ui.ecuSeclectBox.addItems(get_all_ecu(self._ui.projectSelectCcomboBox.currentText()))
        self._ui.ecuSeclectBox.addItems(self._model.get_all_ecu(self._ui.projectSelectCcomboBox.currentText()))

    def __init_ecuNodeInfoListWidget(self):
        self._ui.nodeInfoTableWidget.setRowCount(0)
        ecu_node_infos = self._model.get_all_node(self._ui.prjSelectComboBox.currentText())

        # if len(ecu_node_infos) == 0:
        #     ecu_node_infos = self._import_project_ecu_node

        for node in ecu_node_infos:
            rowCnt = self._ui.nodeInfoTableWidget.rowCount()
            ecu_name = node['MCU_NAME']
            can_name = node['CAN_NAME']
            log_addr = '0x{:x}'.format(node['LOGICAL_ADD'])

            self._ui.nodeInfoTableWidget.insertRow(rowCnt)
            self._ui.nodeInfoTableWidget.setItem(rowCnt, 0, QTableWidgetItem(ecu_name))
            self._ui.nodeInfoTableWidget.setItem(rowCnt, 1, QTableWidgetItem(log_addr))
            self._ui.nodeInfoTableWidget.setItem(rowCnt, 2, QTableWidgetItem(can_name))

    def __init_canSeclectBox(self):
        # self._ui.canSelectComboBox.addItems(get_all_can())
        self._ui.canSelectComboBox.addItems(self._model.get_all_can())

    def __init_projectSeclectBox(self):
        self._ui.projectSelectCcomboBox.clear()
        self._ui.prjSelectComboBox.clear()
        # self._ui.projectSelectCcomboBox.addItems(get_all_project()) # tab diagnoisitic
        self._ui.projectSelectCcomboBox.addItems(self._model.get_all_project()) # tab diagnoisitic
        # self._ui.prjSelectComboBox.addItems(get_all_project())# tab configure generate
        self._ui.prjSelectComboBox.addItems(self._model.get_all_project())# tab configure generate

    def __init_logitic_data_read_table(self):

        # for did in logitic_data_did:
        #     self._controller.send_diag_msg('22', ecuAddr, did)
        did_cnt = 0
        for did, did_info in logitic_data_did.items():

            label_did = QLabel(self._ui.logiticDataTab)
            label_did.setObjectName(u"label_" + did)
            label_did.setText(did+'(' + did_info + ')')
            self._ui.formLayout.setWidget(did_cnt, QFormLayout.LabelRole, label_did)

            lineEdit_did = QLineEdit(self._ui.logiticDataTab)
            lineEdit_did.setObjectName(u"lineEdit_" + did)

            self._ui.formLayout.setWidget(did_cnt, QFormLayout.FieldRole, lineEdit_did)

            did_cnt = did_cnt + 1



    def __set_pushbutton_status(self, isEnable):
        self._ui.sendDiagMsgButton.setEnabled(isEnable)
        self._ui.sendDoipUdpMsgButton.setEnabled(isEnable)
        self._ui.diagRouteTestButton.setEnabled(isEnable)
        if isEnable:
            self._ui.buildConnectionButton.setText('断开连接')
        else:
            self._ui.buildConnectionButton.setText('建立连接')

    def __init_all_actions(self):
        self._ui.buildConnectionButton.triggered.connect(self._controller.on_buildConnectionButton_pressed)
        self._ui.applySettingButton.clicked.connect(self.set_doip_parameter)
        self._ui.loopbackIPSettingButton.clicked.connect(self.on_loopbackIPSettingButton_pressed)
        self._ui.sendDiagMsgButton.clicked.connect(self.__on_sendDiagMsgButton_pressed)
        self._ui.addLinePushButton.clicked.connect(self.__on_add_Line_PushButton_pressed)
        self._ui.clearPushButton.clicked.connect(self.__on_clear_tableWidget_PushButton_pressed)
        self._ui.multiSendPushButton.clicked.connect(self.__on_multi_line_send_PushButton_pressed)
        self._ui.secAccessPushButton.clicked.connect(self.__on_secAccessPushButton_pressed)
        self._ui.portMirrorSettingPushButton.clicked.connect(self.__on_portMirrorSettingPushButton_pressed)
        self._ui.diagReqMsgLineEdit.returnPressed.connect(self.__on_sendDiagMsgButton_pressed)
        self._ui.logiticDataReadPushButton.clicked.connect(self.__on_logiticDataReadPushButton_pressed)
        self._ui.diagRouteTestButton.clicked.connect(self.__on_diagRouteTestPushButton_pressed)
        self._ui.generateCfgPushButton.clicked.connect(self.__on_generateCfgPushButton_pressed)
        # self._ui.ecucFileSelectPushButton.clicked.connect(self.__on_ecucFileSelectPushButton_pressed)
        self._ui.transformPushButton.clicked.connect(self.__on_transformPushButton_pressed)
        self._ui.allignCompPushButton.clicked.connect(self.__on_allignCompPushButton_pressed)
        self._ui.prjImportPushButton.clicked.connect(self.__on_prjImportPushButton_pressed)


        self._ui.projectSelectCcomboBox.currentIndexChanged.connect(self.__on_projectSelectCcomboBox_changed)
        self._ui.prjSelectComboBox.currentIndexChanged.connect(self.__on_genTabPrjSelectCcomboBox_changed)

        self._model.sig_testerIpAddresslineEdit_changed.connect(self.__on_testerIpAddresslineEdit_changed)
        self._model.sig_diagMsgSendButton_changed.connect(self.__set_pushbutton_status)
        self._model.sig_InfoPrintBrowser_changed.connect(self.__on_InfoPrintBrowser_changed)
        self._model.sig_DiagMsgPrintBrowser_changed.connect(self.__on_DiagMsgPrintBrowser_changed)
        # self._ui.sendDiagMsgButton.clicked.connect(self.__send_diagMsg_action)
        # self._ui.diagReqMsgLineEdit.returnPressed.connect(self.__send_diagMsg_action)
        # self._ui.addLinePushButton.clicked.connect(self.__add_Line_PushButton_action)
        # self._ui.clearPushButton.clicked.connect(self.__clear_tableWidget_PushButton_action)
        # self._ui.multiSendPushButton.clicked.connect(self.__multi_line_send_PushButton_action)
        msgClearOption = QAction(self._ui.DiagMsgPrintBrowser)
        msgClearOption.setText("清空")
        msgClearOption.triggered.connect(self.__clear_all_print_textBrowser)  # 点击菜单中的“发送控制代码”执行的函数

        # tableView 添加具体的右键菜单
        self._ui.DiagMsgPrintBrowser.addAction(msgClearOption)

    def get_ecu_logical_address(self):
        ecuIndex = self._ui.ecuSeclectBox.currentIndex()
        ecuLogicAddress = self._model.get_ecu_logical_address_by_index(ecuIndex, self._ui.projectSelectCcomboBox.currentText())
        return ecuLogicAddress

    def get_test_can_name(self):
        can_name = self._ui.canSelectComboBox.currentText()
        return can_name

    @Slot(int)
    def __on_projectSelectCcomboBox_changed(self, int):
        if self._ui.projectSelectCcomboBox.currentText() == '':
            pass
        else:
            self.__init_ecuSeclectBox()

    @Slot(int)
    def __on_genTabPrjSelectCcomboBox_changed(self, int):
        if self._ui.projectSelectCcomboBox.currentText() == '':
            pass
        else:
            self.__init_ecuNodeInfoListWidget()

    @Slot(str)
    def __on_testerIpAddresslineEdit_changed(self, text):
        self._ui.testerIpAddresslineEdit.setText(text)

    @Slot(str)
    def __on_InfoPrintBrowser_changed(self, text):
        self._ui.InfoPrintBrowser.append(text)
        self._ui.InfoPrintBrowser.ensureCursorVisible()

    @Slot(str)
    def __on_DiagMsgPrintBrowser_changed(self, text):
        self._ui.DiagMsgPrintBrowser.append(text)
        self._ui.DiagMsgPrintBrowser.ensureCursorVisible()

    @Slot()
    def __clear_all_print_textBrowser(self):
        self._ui.DiagMsgPrintBrowser.clear()
        self._ui.InfoPrintBrowser.clear()


    @Slot()
    def __on_sendDiagMsgButton_pressed(self):
        sid = self._ui.sidSeclectBox.currentText()
        ecuLogicAddress = self.get_ecu_logical_address()
        diagMsgContent = self._ui.diagReqMsgLineEdit.text()
        self._controller.send_diag_msg(sid, ecuLogicAddress, diagMsgContent)

    @Slot()
    def __on_add_Line_PushButton_pressed(self):
        rowCnt = self._ui.multiLineTableWidget.rowCount()
        sid = self._ui.sidLineEdit.text()
        diagData = self._ui.diagDataLineEdit.text()

        self._ui.multiLineTableWidget.insertRow(rowCnt)
        self._ui.multiLineTableWidget.setItem(rowCnt, 0, QTableWidgetItem(sid))
        self._ui.multiLineTableWidget.setItem(rowCnt, 1, QTableWidgetItem(diagData))

    @Slot()
    def __on_clear_tableWidget_PushButton_pressed(self):
        self._ui.multiLineTableWidget.setRowCount(0)

    @Slot()
    def __on_multi_line_send_PushButton_pressed(self):
        for i in range(self._ui.multiLineTableWidget.rowCount()):
            sid = self._ui.multiLineTableWidget.item(i, 0).text()
            diagData = self._ui.multiLineTableWidget.item(i, 1).text()
            ecuAddr = self.get_ecu_logical_address()
            self._controller.send_diag_msg(sid, ecuAddr, diagData)

    @Slot()
    def __on_secAccessPushButton_pressed(self):

        ecuAddr = self.get_ecu_logical_address()
        self._controller.send_diag_msg('10', ecuAddr, '03')
        self._controller.send_diag_msg('27', ecuAddr, '01')

    @Slot()
    def __on_portMirrorSettingPushButton_pressed(self):
        portMirror = self._ui.portMirrorLineEdit.text()
        if portMirror == '':
            portMirror = '80ff'

        ecuAddr = self.get_ecu_logical_address()
        self._controller.send_diag_msg('10', ecuAddr, '03')
        self._controller.send_diag_msg('27', ecuAddr, '01')
        self._controller.send_diag_msg('2E', ecuAddr, 'CE06'+portMirror)
        self._controller.send_diag_msg('11', ecuAddr, '01')

    @Slot()
    def __on_logiticDataReadPushButton_pressed(self):
        self.__clear_logiticData_lineEdit()
        for did, did_info in logitic_data_did.items():
            ecuAddr = self.get_ecu_logical_address()
            resp = self._controller.send_diag_msg('22', ecuAddr, did)
            # print(resp[1:])
            rest_str = self._model.hex_DiagMsg2_str(resp[1:])
            lineEdit: QLineEdit = self._ui.logiticDataTab.findChild(QLineEdit, u"lineEdit_"+did)
            if lineEdit is not None:
                # print(rest_str)
                lineEdit.setText(rest_str.upper())

    def __clear_logiticData_lineEdit(self):
        for did, did_info in logitic_data_did.items():
            lineEdit: QLineEdit = self._ui.logiticDataTab.findChild(QLineEdit, u"lineEdit_" + did)
            lineEdit.setText('')

    @Slot()
    def __on_diagRouteTestPushButton_pressed(self):

        test_can_name = self.get_test_can_name()

        for node in self._model.get_all_node(self._ui.projectSelectCcomboBox.currentText()):
            ecuAddr = node['LOGICAL_ADD']
            canName = node['CAN_NAME']
            ecuName = node['MCU_NAME']
            if ecuAddr != 0x1000 and canName == test_can_name:
                self.__on_InfoPrintBrowser_changed('Send Diag Req Msg on {} {}: 0x{:x}'.format(canName, ecuName, ecuAddr))
                try:
                    resp = self._controller.send_diag_msg('10', ecuAddr, '03')
                    self.__on_InfoPrintBrowser_changed(
                        '{} 0x{:x} Response OK'.format(ecuName, ecuAddr+8))
                except TimeoutError as e:
                    self.__on_InfoPrintBrowser_changed(
                        '{} 0x{:x} Response ERROR'.format(ecuName, ecuAddr+8))


    @Slot()
    def __on_generateCfgPushButton_pressed(self):
        project = self._ui.prjSelectComboBox.currentText()

        ecuc_file_choose = QFileDialog.getOpenFileName(self,"选取EcuC文件", os.getcwd(), "Arxml Files (*.arxml);;All Files (*)")  # 起始路径
        pdur_file_choose = QFileDialog.getOpenFileName(self,"选取PDUR文件", os.getcwd(), "Arxml Files (*.arxml);;All Files (*)")  # 起始路径

        if ecuc_file_choose[0] == '' or pdur_file_choose[0] == '':
            return

        logging.debug('ECUC FILE CHOOSE: ' + ecuc_file_choose[0])
        logging.debug('PDUR FILE CHOOSE: ' + pdur_file_choose[0])

        try :
            doip_generate = DoIPGenerate(project, self._model)
            ecuc_generate = EcucGenerate(project, self._model)
            pdur_generate = PdurGenerate(project, self._model, ecuc_file_choose[0])
            pdur_parser = PudrParser(project, self._model, pdur_file_choose[0], pdur_generate.diag_pdus)

        except KeyError as e:
            logging.debug('KeyError:{}'.format(e))

        format_can_node_list = self._model.get_format_all_ecu_node(project)
        # logging.debug(format_can_node_list)
        write_to_txt(format_can_node_list, './output/ecu_info_{}.txt'.format(project))

    def __on_transformPushButton_pressed(self):

        def string2ascii(ascii_text):
            ascii_text_list = list(ascii_text)
            return ''.join([hex(ord(i))[2:] for i in ascii_text_list])

        def ascii2string(hex_string_text):
            hex_string_text_list = self._model.str_DiagMsg2_hex(hex_string_text)
            return ''.join([chr(i) for i in hex_string_text_list])

        ascii_input = self._ui.asciiCodeInputLineEdit.text()
        string_input = self._ui.stringInputLineEdit.text()

        if(ascii_input != ''):
            self._ui.stringInputLineEdit.setText(ascii2string(ascii_input))
        elif(string_input != ''):
            self._ui.asciiCodeInputLineEdit.setText(string2ascii(string_input))
        else:
            pass

    def __on_allignCompPushButton_pressed(self):
        allign_address = int(self._ui.allignAddressLineEdit.text(), 16)
        allign_size = int(self._ui.allignSizeLineEdit.text())
        logging.debug('allign address is {}, size is {}'.format(allign_address, allign_size))

        allign_result = hex((allign_address+allign_size-1)&(~(allign_size-1)))
        self._ui.allignResultLineEdit.setText(allign_result)

    def __on_prjImportPushButton_pressed(self):
        project_file_choose = QFileDialog.getOpenFileName(self, "选取项目文件", os.getcwd(),
                                                       "文本文档 (*.txt);;All Files (*)")  # 起始路径
        project_file_choose = project_file_choose[0]
        project = project_file_choose.split('/')[-1].split('_')[0]
        logging.debug('Input project file: {}'.format(project))

        project_node_info = []
        with open(project_file_choose, 'r') as f:
            while True:
                line_str = f.readline()
                line_str = line_str.replace('\n', '')
                if line_str == '':
                    break
                else:
                    node = line_str.split(' ')
                    # logging.debug(node)
                    node_dict = {}
                    node_dict['MCU_NAME'] = node[0]
                    node_dict['CAN_NAME'] = node[2]
                    node_dict['LOGICAL_ADD'] = int(node[1], 16)
                    if node[3] == 'Y':
                        node_dict['CAN_FD'] = True
                    else:
                        node_dict['CAN_FD'] = False
                    project_node_info.append(node_dict)

            f.close()
        # self._import_project_ecu_node = project_node_info
        # print(project_node_info)
        self._model.all_projects_info[project] = project_node_info
        self.__init_projectSeclectBox()

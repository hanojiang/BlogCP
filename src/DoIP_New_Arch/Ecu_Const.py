# AS32
GW04_ALL_NODE_AS32 = [

    # GW
    {
        'CAN_NAME': 'GW04',
        'MCU_NAME': 'GW',
        'LOGICAL_ADD': 0x1000,
        'CAN_FD' : False
    },

    # CNCAN 1
    {
        'CAN_NAME' : 'CN',
        'MCU_NAME' : 'TBOX',
        'LOGICAL_ADD' : 0x711,
        'CAN_FD' : False
    },

    # PTCAN 4
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'ACU',
        'LOGICAL_ADD' : 0x772,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'ECM',
        'LOGICAL_ADD' : 0x7E0,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'SCU',
        'LOGICAL_ADD' : 0x771,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'TCM',
        'LOGICAL_ADD' : 0x7E1,
        'CAN_FD' : False
    },

    # PTEXTCANFD 1
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'SDM',
        'LOGICAL_ADD' : 0x730,
        'CAN_FD' : True
    },

    # CHCANFD 4
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'EPS',
        'LOGICAL_ADD' : 0x721,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'SCS',
        'LOGICAL_ADD' : 0x720,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'SAS',
        'LOGICAL_ADD' : 0x722,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'LADS',
        'LOGICAL_ADD' : 0x736,
        'CAN_FD' : True
    },

    # ADCANFD 9
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'FDR',
        'LOGICAL_ADD' : 0x734,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'FVCM',
        'LOGICAL_ADD' : 0x733,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'LHRDA',
        'LOGICAL_ADD' : 0x732,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'RHRDA',
        'LOGICAL_ADD' : 0x756,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'HADS',
        'LOGICAL_ADD' : 0x735,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'LFSDA',
        'LOGICAL_ADD' : 0x737,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'RFSDA',
        'LOGICAL_ADD' : 0x757,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'HDM',
        'LOGICAL_ADD' : 0x755,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'DMS',
        'LOGICAL_ADD' : 0x754,
        'CAN_FD' : True
    },

    ## CFCAN 10
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AC',
        'LOGICAL_ADD' : 0x750,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AMP',
        'LOGICAL_ADD' : 0x765,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'SDAVM',
        'LOGICAL_ADD' : 0x764,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'BCM',
        'LOGICAL_ADD' : 0x740,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'BPEPS',
        'LOGICAL_ADD' : 0x7A7,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'FICM',
        'LOGICAL_ADD' : 0x761,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'IPK',
        'LOGICAL_ADD' : 0x760,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'PEPS',
        'LOGICAL_ADD' : 0x745,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'TPMS',
        'LOGICAL_ADD' : 0x724,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'PGM',
        'LOGICAL_ADD' : 0x753,
        'CAN_FD' : False
    },

]

#AS33
GW04_ALL_NODE_AS33 = [
    # GW04
    {
        'CAN_NAME' : 'GW04',
        'MCU_NAME' : 'GW',
        'LOGICAL_ADD' : 0x1000,
        'CAN_FD' : False
    },

    # CNCAN
    {
        'CAN_NAME' : 'CN',
        'MCU_NAME' : 'TBOX',
        'LOGICAL_ADD' : 0x711,
        'CAN_FD' : False
    },

    # PTCAN
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'ACU',
        'LOGICAL_ADD' : 0x772,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'CCEOP',
        'LOGICAL_ADD' : 0x780,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'SCU',
        'LOGICAL_ADD' : 0x771,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'TCM',
        'LOGICAL_ADD' : 0x7E1,
        'CAN_FD' : False
    },

    # PTEXTCANFD
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'SDM',
        'LOGICAL_ADD' : 0x730,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'ECM',
        'LOGICAL_ADD' : 0x7E0,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'ELSDCM',
        'LOGICAL_ADD' : 0x770,
        'CAN_FD' : True
    },

    # CHCANFD
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'SCM',
        'LOGICAL_ADD' : 0x727,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'EPS',
        'LOGICAL_ADD' : 0x721,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'SCS',
        'LOGICAL_ADD' : 0x720,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'SAS',
        'LOGICAL_ADD' : 0x722,
        'CAN_FD' : True
    },
    ## TO DO NODE MISSING IN COM MATRIX
    # {
    #     'CAN_NAME' : 'CHCANFD',
    #     'MCU_NAME' : 'LADS',
    #     'LOGICAL_ADD' : 0x736
    # },

    # ADCANFD
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'FDR',
        'LOGICAL_ADD' : 0x734,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'FVCM',
        'LOGICAL_ADD' : 0x733,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'LHRDA',
        'LOGICAL_ADD' : 0x732,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'RHRDA',
        'LOGICAL_ADD' : 0x756,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'HADS',
        'LOGICAL_ADD' : 0x735,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'LFSDA',
        'LOGICAL_ADD' : 0x737,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'RFSDA',
        'LOGICAL_ADD' : 0x757,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'HDM',
        'LOGICAL_ADD' : 0x755,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'DMS',
        'LOGICAL_ADD' : 0x754,
        'CAN_FD' : True
    },

    ## CFCAN
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AC',
        'LOGICAL_ADD' : 0x750,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AMP',
        'LOGICAL_ADD' : 0x765,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AVM',
        'LOGICAL_ADD' : 0x764,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'BCM',
        'LOGICAL_ADD' : 0x740,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'BPEPS',
        'LOGICAL_ADD' : 0x7A7,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'ICM',
        'LOGICAL_ADD' : 0x761,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'IPK',
        'LOGICAL_ADD' : 0x760,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'PGM',
        'LOGICAL_ADD' : 0x753,
        'CAN_FD' : False
    },
## TO DO NODE MISSING IN COM MATRIX
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'MSM',
        'LOGICAL_ADD' : 0x746,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'PLCM',
        'LOGICAL_ADD' : 0x741,
        'CAN_FD' : False
    },
# # GW04
#     {
#         'CAN_NAME' : 'GW04',
#         'MCU_NAME' : 'GW',
#         'LOGICAL_ADD' : 0x1000
#     },

]

#AS33P
GW04_ALL_NODE_AS33P = [
    # GW04
    {
        'CAN_NAME' : 'GW04',
        'MCU_NAME' : 'GW',
        'LOGICAL_ADD' : 0x1000,
        'CAN_FD' : False
    },

    # CNCAN
    {
        'CAN_NAME' : 'CN',
        'MCU_NAME' : 'TBOX',
        'LOGICAL_ADD' : 0x711,
        'CAN_FD' : False
    },

    # PTCAN FD
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'ECM',
        'LOGICAL_ADD' : 0x7E0,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'VCU',
        'LOGICAL_ADD' : 0x7E3,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'ISC',
        'LOGICAL_ADD' : 0x7E7,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'BMS',
        'LOGICAL_ADD' : 0x7E5,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'CCU',
        'LOGICAL_ADD' : 0x784,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'SDM',
        'LOGICAL_ADD' : 0x730,
        'CAN_FD' : True
    },

    # PTEXTCAN
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'SCU',
        'LOGICAL_ADD' : 0x771,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'CMM',
        'LOGICAL_ADD' : 0x774,
        'CAN_FD' : False
    },

    # CHCANFD
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'EPS',
        'LOGICAL_ADD' : 0x721,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'SCS',
        'LOGICAL_ADD' : 0x720,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'FDR',
        'LOGICAL_ADD' : 0x734,
        'CAN_FD' : True
    },

    # ADCANFD

    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'FVCM',
        'LOGICAL_ADD' : 0x733,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'LHRDA',
        'LOGICAL_ADD' : 0x732,
        'CAN_FD' : True
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'RHRDA',
        'LOGICAL_ADD' : 0x756,
        'CAN_FD' : True
    },

    ## CFCAN
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AC',
        'LOGICAL_ADD' : 0x750,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AMP',
        'LOGICAL_ADD' : 0x765,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'BCM',
        'LOGICAL_ADD' : 0x740,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'ICM',
        'LOGICAL_ADD' : 0x761,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'IPK',
        'LOGICAL_ADD' : 0x760,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'ESCL',
        'LOGICAL_ADD' : 0x742,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'PACM',
        'LOGICAL_ADD' : 0x763,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'FLSM',
        'LOGICAL_ADD' : 0x746,
        'CAN_FD' : False
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'PLCM',
        'LOGICAL_ADD' : 0x741,
        'CAN_FD' : False
    },
# # GW04
#     {
#         'CAN_NAME' : 'GW04',
#         'MCU_NAME' : 'GW',
#         'LOGICAL_ADD' : 0x1000
#     },
]

DIAG_SID = [
    '10', '11', '14', '19', '22', '27', '28', '2E', '31', '85'
]

logitic_data_did = {
            'F100' : '软件校验信息域',
            'F110' : '刷新信息域',
            'F120' : '网络信息域-出厂数据',
            'F121' : '网络信息域-当前数据',
            'F183' : 'FBL软件参考号',
            'F187' : 'ECU零件号',
            'F18A' : '系统供应商标识号',
            'F18B' : 'ECU制造日期',
            'F18C' : 'ECU序列号',
            'F190' : 'VIN',
            'F191' : 'ECU硬件号',
            'F192' : '供应商ECU硬件参考号',
            'F194' : '供应商ECU软件参考号',
            'F198' : '配置跟踪域',
            'F1A0' : 'ECU应用软件号',
            'F1A1' : 'ECU标定软件号',
            'F1A2' : 'ECU NCF参考号',
            'F1A5' : 'ECU索引信息',
            'F1A8' : '车辆特征信息',
            'F1A9' : 'ECU配置文件号',
            'F1AA' : 'ECU刷新流程文件号'}

def get_all_ecu(project):

    allNode = []


    for node in get_all_node(project):
        allNode.append('{:>6}({})'.format(node['MCU_NAME'], hex(node['LOGICAL_ADD'])))

    return allNode

def get_all_can():

    # allCan = ['CF', 'CN', 'PT', 'CH', 'AD', 'PTEXT']
    allCan = ['BDCAN', 'INFOCAN', 'PTCANFD', 'CHCAN2', 'CHCANFD', 'PTEXTCAN', 'ADCANFD']
    return allCan

def get_all_project():
    allProject = ['AS32', 'AS33', 'AS33P']

    return allProject

def get_all_node(project):
    GW04_ALL_NODE = []

    if project == 'AS32':
        GW04_ALL_NODE = GW04_ALL_NODE_AS32
    elif project == 'AS33':
        GW04_ALL_NODE = GW04_ALL_NODE_AS33
    elif project == 'AS33P':
        GW04_ALL_NODE = GW04_ALL_NODE_AS33P
    else:
        pass

    return GW04_ALL_NODE

def get_format_all_ecu_node(project):
    all_node = get_all_node(project)
    format_node_list = []
    format_node_list_info_can = []
    format_node_list_info_fd = []
    format_node_list_case_can = []
    format_node_list_case_fd = []
    for node in all_node:
        if node['MCU_NAME'] == 'GW':
            continue
        if node['CAN_FD'] == True:
            format_node_list_info_fd.append('{} = {},//{}CANFD'.format(node['MCU_NAME'], hex(node['LOGICAL_ADD']), node['CAN_NAME']))
        else:
            format_node_list_info_can.append('{} = {},//{}CAN'.format(node['MCU_NAME'], hex(node['LOGICAL_ADD']), node['CAN_NAME']))

    for node in all_node:
        if node['MCU_NAME'] == 'GW':
            continue
        if node['CAN_FD'] == True:
            format_node_list_case_fd.append('case {}://{}CANFD'.format(node['MCU_NAME'], node['CAN_NAME']))
        else:
            format_node_list_case_can.append('case {}://{}CAN'.format(node['MCU_NAME'], node['CAN_NAME']))

    format_node_list.extend(format_node_list_info_can)
    format_node_list.extend(format_node_list_info_fd)
    format_node_list.extend(format_node_list_case_can)
    format_node_list.extend(format_node_list_case_fd)
    return format_node_list
def get_ecu_logical_address_by_index(index, project):
    GW04_ALL_NODE = get_all_node(project)

    return GW04_ALL_NODE[index]['LOGICAL_ADD']

def write_to_txt(str_list, filename):
    with open(filename, 'w') as f:
        for str_i in str_list:
            f.write(str_i)
            f.write('\n')

        f.close()

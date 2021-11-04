# AS32
GW04_ALL_NODE_AS32 = [

    # GW
    {
        'CAN_NAME': 'GW04',
        'MCU_NAME': 'GW',
        'LOGICAL_ADD': 0x1000
    },

    # CNCAN 1
    {
        'CAN_NAME' : 'CNCAN',
        'MCU_NAME' : 'TBOX',
        'LOGICAL_ADD' : 0x711
    },

    # PTCAN 4
    {
        'CAN_NAME' : 'PTCAN',
        'MCU_NAME' : 'ACU',
        'LOGICAL_ADD' : 0x772
    },
    {
        'CAN_NAME' : 'PTCAN',
        'MCU_NAME' : 'ECM',
        'LOGICAL_ADD' : 0x7E0
    },
    {
        'CAN_NAME' : 'PTCAN',
        'MCU_NAME' : 'SCU',
        'LOGICAL_ADD' : 0x771
    },
    {
        'CAN_NAME' : 'PTCAN',
        'MCU_NAME' : 'TCM',
        'LOGICAL_ADD' : 0x7E1
    },

    # PTEXTCANFD 1
    {
        'CAN_NAME' : 'PTEXTCANFD',
        'MCU_NAME' : 'SDM',
        'LOGICAL_ADD' : 0x730
    },

    # CHCANFD 4
    {
        'CAN_NAME' : 'CHCANFD',
        'MCU_NAME' : 'EPS',
        'LOGICAL_ADD' : 0x721
    },
    {
        'CAN_NAME' : 'CHCANFD',
        'MCU_NAME' : 'SCS',
        'LOGICAL_ADD' : 0x720
    },
    {
        'CAN_NAME' : 'CHCANFD',
        'MCU_NAME' : 'SAS',
        'LOGICAL_ADD' : 0x722
    },
    {
        'CAN_NAME' : 'CHCANFD',
        'MCU_NAME' : 'LADS',
        'LOGICAL_ADD' : 0x736
    },

    # ADCANFD 9
    {
        'CAN_NAME' : 'ADCANFD',
        'MCU_NAME' : 'FDR',
        'LOGICAL_ADD' : 0x734
    },
    {
        'CAN_NAME' : 'ADCANFD',
        'MCU_NAME' : 'FVCM',
        'LOGICAL_ADD' : 0x733
    },
    {
        'CAN_NAME' : 'ADCANFD',
        'MCU_NAME' : 'LHRDA',
        'LOGICAL_ADD' : 0x732
    },
    {
        'CAN_NAME' : 'ADCANFD',
        'MCU_NAME' : 'RHRDA',
        'LOGICAL_ADD' : 0x756
    },
    {
        'CAN_NAME' : 'ADCANFD',
        'MCU_NAME' : 'HADS',
        'LOGICAL_ADD' : 0x735
    },
    {
        'CAN_NAME' : 'ADCANFD',
        'MCU_NAME' : 'LFSDA',
        'LOGICAL_ADD' : 0x737
    },
    {
        'CAN_NAME' : 'ADCANFD',
        'MCU_NAME' : 'RFSDA',
        'LOGICAL_ADD' : 0x757
    },
    {
        'CAN_NAME' : 'ADCANFD',
        'MCU_NAME' : 'HDM',
        'LOGICAL_ADD' : 0x755
    },
    {
        'CAN_NAME' : 'ADCANFD',
        'MCU_NAME' : 'DMS',
        'LOGICAL_ADD' : 0x754
    },

    ## CFCAN 10
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'AC',
        'LOGICAL_ADD' : 0x750
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'AMP',
        'LOGICAL_ADD' : 0x765
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'SDAVM',
        'LOGICAL_ADD' : 0x764
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'BCM',
        'LOGICAL_ADD' : 0x740
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'BPEPS',
        'LOGICAL_ADD' : 0x7A7
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'FICM',
        'LOGICAL_ADD' : 0x761
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'IPK',
        'LOGICAL_ADD' : 0x760
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'PEPS',
        'LOGICAL_ADD' : 0x745#######
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'TPMS',
        'LOGICAL_ADD' : 0x724#######
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'PGM',
        'LOGICAL_ADD' : 0x753#######
    },

]

#AS33
GW04_ALL_NODE_AS33 = [
    # # GW04
    # {
    #     'CAN_NAME' : 'GW04',
    #     'MCU_NAME' : 'GW',
    #     'LOGICAL_ADD' : 0x1000
    # },

    # CNCAN
    {
        'CAN_NAME' : 'CN',
        'MCU_NAME' : 'TBOX',
        'LOGICAL_ADD' : 0x711
    },

    # PTCAN
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'ACU',
        'LOGICAL_ADD' : 0x772
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'CCEOP',
        'LOGICAL_ADD' : 0x780
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'SCU',
        'LOGICAL_ADD' : 0x771
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'TCM',
        'LOGICAL_ADD' : 0x7E1
    },

    # PTEXTCANFD
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'SDM',
        'LOGICAL_ADD' : 0x730
    },
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'ECM',
        'LOGICAL_ADD' : 0x7E0
    },
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'ELSDCM',
        'LOGICAL_ADD' : 0x770
    },

    # CHCANFD
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'SCM',
        'LOGICAL_ADD' : 0x727
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'EPS',
        'LOGICAL_ADD' : 0x721
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'SCS',
        'LOGICAL_ADD' : 0x720
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'SAS',
        'LOGICAL_ADD' : 0x722
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
        'LOGICAL_ADD' : 0x734
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'FVCM',
        'LOGICAL_ADD' : 0x733
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'LHRDA',
        'LOGICAL_ADD' : 0x732
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'RHRDA',
        'LOGICAL_ADD' : 0x756
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'HADS',
        'LOGICAL_ADD' : 0x735
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'LFSDA',
        'LOGICAL_ADD' : 0x737
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'RFSDA',
        'LOGICAL_ADD' : 0x757
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'HDM',
        'LOGICAL_ADD' : 0x755
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'DMS',
        'LOGICAL_ADD' : 0x754
    },

    ## CFCAN
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AC',
        'LOGICAL_ADD' : 0x750
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AMP',
        'LOGICAL_ADD' : 0x765
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AVM',
        'LOGICAL_ADD' : 0x764
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'BCM',
        'LOGICAL_ADD' : 0x740
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'BPEPS',
        'LOGICAL_ADD' : 0x7A7
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'ICM',
        'LOGICAL_ADD' : 0x761
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'IPK',
        'LOGICAL_ADD' : 0x760
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'PGM',
        'LOGICAL_ADD' : 0x753
    },
## TO DO NODE MISSING IN COM MATRIX
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'MSM',
        'LOGICAL_ADD' : 0x746
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'PLCM',
        'LOGICAL_ADD' : 0x741
    },
# GW04
    {
        'CAN_NAME' : 'GW04',
        'MCU_NAME' : 'GW',
        'LOGICAL_ADD' : 0x1000
    },

]

#AS33P
GW04_ALL_NODE_AS33P = [


    # CNCAN
    {
        'CAN_NAME' : 'CN',
        'MCU_NAME' : 'TBOX',
        'LOGICAL_ADD' : 0x711
    },

    # PTCAN FD
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'ECM',
        'LOGICAL_ADD' : 0x7E0
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'VCU',
        'LOGICAL_ADD' : 0x7E3
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'ISC',
        'LOGICAL_ADD' : 0x7E7
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'BMS',
        'LOGICAL_ADD' : 0x7E5
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'CCU',
        'LOGICAL_ADD' : 0x784
    },
    {
        'CAN_NAME' : 'PT',
        'MCU_NAME' : 'SDM',
        'LOGICAL_ADD' : 0x730
    },

    # PTEXTCAN
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'SCU',
        'LOGICAL_ADD' : 0x771
    },
    {
        'CAN_NAME' : 'PTEXT',
        'MCU_NAME' : 'CMM',
        'LOGICAL_ADD' : 0x774
    },

    # CHCANFD
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'EPS',
        'LOGICAL_ADD' : 0x721
    },
    {
        'CAN_NAME' : 'CH',
        'MCU_NAME' : 'SCS',
        'LOGICAL_ADD' : 0x720
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'FDR',
        'LOGICAL_ADD' : 0x734
    },

    # ADCANFD

    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'FVCM',
        'LOGICAL_ADD' : 0x733
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'LHRDA',
        'LOGICAL_ADD' : 0x732
    },
    {
        'CAN_NAME' : 'AD',
        'MCU_NAME' : 'RHRDA',
        'LOGICAL_ADD' : 0x756
    },

    ## CFCAN
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AC',
        'LOGICAL_ADD' : 0x750
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'AMP',
        'LOGICAL_ADD' : 0x765
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'BCM',
        'LOGICAL_ADD' : 0x740
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'ICM',
        'LOGICAL_ADD' : 0x761
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'IPK',
        'LOGICAL_ADD' : 0x760
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'ESCL',
        'LOGICAL_ADD' : 0x742
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'PACM',
        'LOGICAL_ADD' : 0x763
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'FLSM',
        'LOGICAL_ADD' : 0x746
    },
    {
        'CAN_NAME' : 'CF',
        'MCU_NAME' : 'PLCM',
        'LOGICAL_ADD' : 0x741
    },
# GW04
    {
        'CAN_NAME' : 'GW04',
        'MCU_NAME' : 'GW',
        'LOGICAL_ADD' : 0x1000
    },
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

    allCan = ['CF', 'CN', 'PT', 'CH', 'AD', 'PTEXT']

    return allCan

def get_all_project():
    allProject = ['AS32', 'AS33', 'AS33P']

    return allProject

def get_all_node(project):
    GW04_ALL_NODE = {}

    if project == 'AS32':
        GW04_ALL_NODE = GW04_ALL_NODE_AS32

    elif project == 'AS33':
        GW04_ALL_NODE = GW04_ALL_NODE_AS33
    elif project == 'AS33P':
        GW04_ALL_NODE = GW04_ALL_NODE_AS33P
    else:
        pass

    return GW04_ALL_NODE
def get_ecu_logical_address_by_index(index, project):
    GW04_ALL_NODE = get_all_node(project)

    return GW04_ALL_NODE[index]['LOGICAL_ADD']

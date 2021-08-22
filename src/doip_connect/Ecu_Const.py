GW04_ALL_NODE = [

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

DIAG_SID = [
    '10', '11', '14', '19', '22', '27', '28', '2E', '85'
]

def get_all_ecu():

    allNode = []

    for node in GW04_ALL_NODE:
        allNode.append('{:>6}({})'.format(node['MCU_NAME'], hex(node['LOGICAL_ADD'])))

    return allNode

def get_ecu_logical_address_by_index(index):
    return GW04_ALL_NODE[index]['LOGICAL_ADD']
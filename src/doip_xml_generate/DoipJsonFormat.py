from Utils import parseData
from lxml import etree
import logging
import copy

DoIPChannel_Func = {
    "ECUC-CONTAINER-VALUE": {
        "SHORT-NAME": "DoIPChannel_Func_Remote",
        "DEFINITION-REF": {
            "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
            "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel"
        },
        "REFERENCE-VALUES": {
            "ECUC-REFERENCE-VALUE": [
                {
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-REFERENCE-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPChannelSARef"
                    },
                    "VALUE-REF": {
                        "-DEST": "ECUC-CONTAINER-VALUE",
                        "#text": "/ActiveEcuC/DoIP/DoIPConfigSet/Remote_Tester"
                    }
                },
                {
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-REFERENCE-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPChannelTARef"
                    },
                    "VALUE-REF": {
                        "-DEST": "ECUC-CONTAINER-VALUE",
                        "#text": "/ActiveEcuC/DoIP/DoIPConfigSet/DoIPConnections/DoIPTargetAddress_Func_Remote"
                    }
                }
            ]
        },
        "SUB-CONTAINERS": {
            "ECUC-CONTAINER-VALUE": {
                "SHORT-NAME": "DoIPPduRRxPdu_Func_RX_001",
                "DEFINITION-REF": {
                    "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
                    "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPPduRRxPdu"
                },
                "PARAMETER-VALUES": {
                    "ECUC-NUMERICAL-PARAM-VALUE": {
                        "DEFINITION-REF": {
                            "-DEST": "ECUC-INTEGER-PARAM-DEF",
                            "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPPduRRxPdu/DoIPPduRRxPduId"
                        },
                        "VALUE": "0"
                    }
                },
                "REFERENCE-VALUES": {
                    "ECUC-REFERENCE-VALUE": {
                        "DEFINITION-REF": {
                            "-DEST": "ECUC-REFERENCE-DEF",
                            "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPPduRRxPdu/DoIPPduRRxPduRef"
                        },
                        "VALUE-REF": {
                            "-DEST": "ECUC-CONTAINER-VALUE",
                            "#text": "/ActiveEcuC/EcuC/EcucPduCollection/DCM_DoIP_PhysReq_GW_Func_Rx_Remote_001"
                        }
                    }
                }
            }
        }
    }
}

DoIPChannel_Phy = {
    "ECUC-CONTAINER-VALUE": {
        "SHORT-NAME": "DoIPChannel_Phy_Remote_CCP",
        "DEFINITION-REF": {
            "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
            "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel"
        },
        "REFERENCE-VALUES": {
            "ECUC-REFERENCE-VALUE": [
                {
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-REFERENCE-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPChannelSARef"
                    },
                    "VALUE-REF": {
                        "-DEST": "ECUC-CONTAINER-VALUE",
                        "#text": "/ActiveEcuC/DoIP/DoIPConfigSet/Remote_Tester"
                    }
                },
                {
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-REFERENCE-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPChannelTARef"
                    },
                    "VALUE-REF": {
                        "-DEST": "ECUC-CONTAINER-VALUE",
                        "#text": "/ActiveEcuC/DoIP/DoIPConfigSet/DoIPConnections/DoIPTargetAddress_CCP_Local_Remote"
                    }
                }
            ]
        },
        "SUB-CONTAINERS": {
            "ECUC-CONTAINER-VALUE": [
                {
                    "SHORT-NAME": "DoIPPduRRxPdu_Phy_CCP_RX_Remote_001",
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPPduRRxPdu"
                    },
                    "PARAMETER-VALUES": {
                        "ECUC-NUMERICAL-PARAM-VALUE": {
                            "DEFINITION-REF": {
                                "-DEST": "ECUC-INTEGER-PARAM-DEF",
                                "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPPduRRxPdu/DoIPPduRRxPduId"
                            },
                            "VALUE": "1"
                        }
                    },
                    "REFERENCE-VALUES": {
                        "ECUC-REFERENCE-VALUE": {
                            "DEFINITION-REF": {
                                "-DEST": "ECUC-REFERENCE-DEF",
                                "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPPduRRxPdu/DoIPPduRRxPduRef"
                            },
                            "VALUE-REF": {
                                "-DEST": "ECUC-CONTAINER-VALUE",
                                "#text": "/ActiveEcuC/EcuC/EcucPduCollection/DCM_DoIP_PhysReq_GW_Rx_Remote_001"
                            }
                        }
                    }
                },
                {
                    "SHORT-NAME": "DoIPPduRTxPdu_Phy_CCP_TX_Remote_001",
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPPduRTxPdu"
                    },
                    "PARAMETER-VALUES": {
                        "ECUC-NUMERICAL-PARAM-VALUE": {
                            "DEFINITION-REF": {
                                "-DEST": "ECUC-INTEGER-PARAM-DEF",
                                "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPPduRTxPdu/DoIPPduRTxPduId"
                            },
                            "VALUE": "0"
                        },
                        "ECUC-TEXTUAL-PARAM-VALUE": {
                            "DEFINITION-REF": {
                                "-DEST": "ECUC-ENUMERATION-PARAM-DEF",
                                "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPPduRTxPdu/DoIPPduType"
                            },
                            "VALUE": "DOIP_TPPDU"
                        }
                    },
                    "REFERENCE-VALUES": {
                        "ECUC-REFERENCE-VALUE": {
                            "DEFINITION-REF": {
                                "-DEST": "ECUC-REFERENCE-DEF",
                                "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPChannel/DoIPPduRTxPdu/DoIPPduRTxPduRef"
                            },
                            "VALUE-REF": {
                                "-DEST": "ECUC-CONTAINER-VALUE",
                                "#text": "/ActiveEcuC/EcuC/EcucPduCollection/DCM_DoIP_PhysResp_GW_Tx_Remote_001"
                            }
                        }
                    }
                }
            ]
        }
    }
}

DoIPRoutingActivation = {
    "ECUC-CONTAINER-VALUE": {
        "SHORT-NAME": "DoIPRoutingActivation_Remote",
        "DEFINITION-REF": {
            "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
            "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPRoutingActivation"
        },
        "PARAMETER-VALUES": {
            "ECUC-NUMERICAL-PARAM-VALUE": {
                "DEFINITION-REF": {
                    "-DEST": "ECUC-INTEGER-PARAM-DEF",
                    "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPRoutingActivation/DoIPRoutingActivationNumber"
                },
                "VALUE": "0"
            }
        },
        "REFERENCE-VALUES": {
            "ECUC-REFERENCE-VALUE": [
                {
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-REFERENCE-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPRoutingActivation/DoIPTargetAddressRef"
                    },
                    "VALUE-REF": {
                        "-DEST": "ECUC-CONTAINER-VALUE",
                        "#text": "/ActiveEcuC/DoIP/DoIPConfigSet/DoIPConnections/DoIPTargetAddress_CCP_Local_Remote"
                    }
                }
            ]
        }
    }
}
DoIPTargetAddress = {
    "ECUC-CONTAINER-VALUE": {
        "SHORT-NAME": "DoIPTargetAddress_Func_Remote",
        "DEFINITION-REF": {
            "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
            "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPConnections/DoIPTargetAddress"
        },
        "PARAMETER-VALUES": {
            "ECUC-NUMERICAL-PARAM-VALUE": [
                {
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-INTEGER-PARAM-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPConnections/DoIPTargetAddress/DoIPTargetAddressValue"
                    },
                    "VALUE": "19968"
                },
                {
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-BOOLEAN-PARAM-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPConnections/DoIPTargetAddress/DoIPTargetAddressVerification"
                    },
                    "VALUE": "false"
                },
                {
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-INTEGER-PARAM-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPConnections/DoIPTargetAddress/DoIPTargetMaxBufSize"
                    },
                    "VALUE": "4091"
                }
            ]
        }
    }
}

# DoIPTcpConnection
# DoIPUdpConnection
# DoIPUdpVehicleAnnouncementConnection
# DoIPIpAddressAssignment
DoIPTester = {
    "ECUC-CONTAINER-VALUE": {
        "SHORT-NAME": "Remote_Tester",
        "DEFINITION-REF": {
            "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
            "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPTester"
        },
        "PARAMETER-VALUES": {
            "ECUC-NUMERICAL-PARAM-VALUE": [
                {
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-INTEGER-PARAM-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPTester/DoIPNumByteDiagAckNack"
                    },
                    "VALUE": "256"
                },
                {
                    "DEFINITION-REF": {
                        "-DEST": "ECUC-INTEGER-PARAM-DEF",
                        "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPTester/DoIPTesterSA"
                    },
                    "VALUE": "225"
                }
            ]
        },
        "REFERENCE-VALUES": {
            "ECUC-REFERENCE-VALUE": {
                "DEFINITION-REF": {
                    "-DEST": "ECUC-REFERENCE-DEF",
                    "#text": "/MICROSAR/DoIP/DoIPConfigSet/DoIPTester/DoIPRoutingActivationRef"
                },
                "VALUE-REF": {
                    "-DEST": "ECUC-CONTAINER-VALUE",
                    "#text": "/ActiveEcuC/DoIP/DoIPConfigSet/DoIPRoutingActivation_Remote"
                }
            }
        }
    }
}

PduRPath = {
  "ECUC-CONTAINER-VALUE": {
    "SHORT-NAME": "DoIP_Tester2TBOX_Phys_Req_Local",# para 1
    "ANNOTATIONS": {
      "ANNOTATION": { "ANNOTATION-ORIGIN": "DV:ExportedElementRoot" }
    },
    "DEFINITION-REF": {
      "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
      "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath"
    },
    "PARAMETER-VALUES": {
      "ECUC-TEXTUAL-PARAM-VALUE": {
        "DEFINITION-REF": {
          "-DEST": "ECUC-ENUMERATION-PARAM-DEF",
          "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRRoutingPathCommunicationType"
        },
        "VALUE": "TRANSPORT_PROTOCOL"
      },
      "ECUC-NUMERICAL-PARAM-VALUE": {
        "DEFINITION-REF": {
          "-DEST": "ECUC-BOOLEAN-PARAM-DEF",
          "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRMulticoreRoutingPath"
        },
        "VALUE": "false"
      }
    },
    "REFERENCE-VALUES": {
      "ECUC-REFERENCE-VALUE": {
        "DEFINITION-REF": {
          "-DEST": "ECUC-REFERENCE-DEF",
          "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRLockRef"
        },
        "VALUE-REF": {
          "-DEST": "ECUC-CONTAINER-VALUE",
          "#text": "/ActiveEcuC/PduR/PduRRoutingTables/PduRLock_PduRExclusiveArea"
        }
      }
    },
    "SUB-CONTAINERS": {
      "ECUC-CONTAINER-VALUE": [
        {
          "SHORT-NAME": "PduRSrcPdu_GW_Phys_001",# para 2
          "DEFINITION-REF": {
            "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
            "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRSrcPdu"
          },
          "PARAMETER-VALUES": {
            "ECUC-NUMERICAL-PARAM-VALUE": {
              "DEFINITION-REF": {
                "-DEST": "ECUC-INTEGER-PARAM-DEF",
                "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRSrcPdu/PduRSourcePduHandleId"
              },
              "VALUE": "65535"
            },
            "ECUC-TEXTUAL-PARAM-VALUE": {
              "DEFINITION-REF": {
                "-DEST": "ECUC-ENUMERATION-PARAM-DEF",
                "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRSrcPdu/PduRSrcPduDirection"
              },
              "VALUE": "RECEIVE"
            }
          },
          "REFERENCE-VALUES": {
            "ECUC-REFERENCE-VALUE": [
              {
                "DEFINITION-REF": {
                  "-DEST": "ECUC-REFERENCE-DEF",
                  "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRSrcPdu/PduRSrcPduRef"
                },
                "VALUE-REF": {
                  "-DEST": "ECUC-CONTAINER-VALUE",
                  "#text": "/ActiveEcuC/EcuC/EcucPduCollection/DCM_DoIP_Local_PhysReq_TBOX_Rx"# para 3
                }
              },
              {
                "DEFINITION-REF": {
                  "-DEST": "ECUC-REFERENCE-DEF",
                  "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRSrcPdu/PduRSrcPduPduRBswModulesRef"
                },
                "VALUE-REF": {
                  "-DEST": "ECUC-CONTAINER-VALUE",
                  "#text": "/ActiveEcuC/PduR/DoIP"
                }
              }
            ]
          }
        },
        {
          "SHORT-NAME": "PduRDestPdu_014",# para 4
          "DEFINITION-REF": {
            "-DEST": "ECUC-PARAM-CONF-CONTAINER-DEF",
            "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRDestPdu"
          },
          "PARAMETER-VALUES": {
            "ECUC-NUMERICAL-PARAM-VALUE": {
              "DEFINITION-REF": {
                "-DEST": "ECUC-INTEGER-PARAM-DEF",
                "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRDestPdu/PduRDestPduHandleId"
              },
              "VALUE": "65535"
            },
            "ECUC-TEXTUAL-PARAM-VALUE": [
              {
                "DEFINITION-REF": {
                  "-DEST": "ECUC-ENUMERATION-PARAM-DEF",
                  "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRDestPdu/PduRDestPduDirection"
                },
                "VALUE": "TRANSMIT"
              },
              {
                "DEFINITION-REF": {
                  "-DEST": "ECUC-ENUMERATION-PARAM-DEF",
                  "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRDestPdu/PduRDestPduRoutingType"
                },
                "VALUE": "GATEWAY_ROUTING"
              },
              {
                "DEFINITION-REF": {
                  "-DEST": "ECUC-ENUMERATION-PARAM-DEF",
                  "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRDestPdu/PduRDestPduDataProcessing"
                },
                "VALUE": "IMMEDIATE"
              },
              {
                "DEFINITION-REF": {
                  "-DEST": "ECUC-ENUMERATION-PARAM-DEF",
                  "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRDestPdu/PduRPduLengthHandlingStrategy"
                },
                "VALUE": "UNUSED"
              }
            ]
          },
          "REFERENCE-VALUES": {
            "ECUC-REFERENCE-VALUE": [
              {
                "DEFINITION-REF": {
                  "-DEST": "ECUC-REFERENCE-DEF",
                  "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRDestPdu/PduRDestPduRef"
                },
                "VALUE-REF": {
                  "-DEST": "ECUC-CONTAINER-VALUE",
                  "#text": "/ActiveEcuC/EcuC/EcucPduCollection/DCM_DIAGCAN_PhysReq_TBOX_7365f3cf_Tx"# para 5
                }
              },
              {
                "DEFINITION-REF": {
                  "-DEST": "ECUC-REFERENCE-DEF",
                  "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRDestPdu/PduRDestPduPduRBswModulesRef"
                },
                "VALUE-REF": {
                  "-DEST": "ECUC-CONTAINER-VALUE",
                  "#text": "/ActiveEcuC/PduR/CanTp"
                }
              },
              {
                "DEFINITION-REF": {
                  "-DEST": "ECUC-REFERENCE-DEF",
                  "#text": "/MICROSAR/PduR/PduRRoutingTables/PduRRoutingTable/PduRRoutingPath/PduRDestPdu/PduRQueueRef"
                },
                "VALUE-REF": {
                  "-DEST": "ECUC-CONTAINER-VALUE",
                  "#text": "/ActiveEcuC/PduR/PduRRoutingTables/PduRQueue_TP"
                }
              }
            ]
          }
        }
      ]
    }
  }
}

GW04_ALL_NODE_AS32 = [
    # CNCAN
    {
        'CAN_NAME' : 'CNCAN',
        'MCU_NAME' : 'TBOX',
        'LOGICAL_ADD' : 0x711
    },

    # PTCAN
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

    # PTEXTCANFD
    {
        'CAN_NAME' : 'PTEXTCANFD',
        'MCU_NAME' : 'SDM',
        'LOGICAL_ADD' : 0x730
    },

    # CHCANFD
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

    # ADCANFD
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

    ## CFCAN
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
        'LOGICAL_ADD' : 0x745
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'TPMS',
        'LOGICAL_ADD' : 0x724
    },
    {
        'CAN_NAME' : 'CFCAN',
        'MCU_NAME' : 'PGM',
        'LOGICAL_ADD' : 0x753
    },

    # GW04
    {
        'CAN_NAME' : 'GW04',
        'MCU_NAME' : 'GW',
        'LOGICAL_ADD' : 0x1000
    },
]
GW04_ALL_NODE_AS33 = [
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
## TO DO NODE MISSING IN COM MATRIX FLSM
    {
        'CAN_NAME' : 'CFCAN',
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
# GW04 FUNC
GW04_FUN_DIR = {
        'CAN_NAME' : 'GW04',
        'MCU_NAME' : 'GW',
        'LOGICAL_ADD' : 0xEFFF
    }
# GW04 FUNC TARGET ADDRESS
GW04_FUNC_TARGET_ADDRESS_DIR = {
        'CAN_NAME' : 'GW04',
        'MCU_NAME' : 'Func_GW',
        'LOGICAL_ADD' : 0xEFFF
    }


GW04_TESTER_ADDR = [0xE80, 0xF00]
def xml_write(et, filename):
    tree = etree.ElementTree(et)
    tree.write(filename, pretty_print=True, xml_declaration=True, encoding='utf-8')

def creat_phy_pudr_path_req(mcu_name, mcu_can, local_or_remote, global_pdu, pdu_key):
    pudrPath_tmp = copy.deepcopy(PduRPath)
    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SHORT-NAME'] = 'DoIP_Tester2{}_Phys_Req_{}'.format(mcu_name,
                                                                                              local_or_remote)
    logging.debug('GENERATE PUDR PATH: DoIP_Tester2{}_Phys_Req_{}'.format(mcu_name, local_or_remote))
    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][0][
        'SHORT-NAME'] = 'PduRSrcPdu_{}_{}_Phys_Req'.format(local_or_remote, mcu_name)
    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][0]['REFERENCE-VALUES'][
        'ECUC-REFERENCE-VALUE'][0]['VALUE-REF'][
        '#text'] = '/ActiveEcuC/EcuC/EcucPduCollection/DCM_DoIP_{}_PhysReq_{}_Rx'.format(local_or_remote,
                                                                                         mcu_name)
    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1][
        'SHORT-NAME'] = 'PduRDestPdu_{}_{}_Phys_Req'.format(local_or_remote, mcu_name)

    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
        'ECUC-REFERENCE-VALUE'][0]['VALUE-REF']['#text'] = '/ActiveEcuC/EcuC/EcucPduCollection/{}'.format(
        global_pdu[pdu_key])
    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
        'ECUC-REFERENCE-VALUE'][2]['VALUE-REF']['#text'] = '/ActiveEcuC/PduR/PduRRoutingTables/PduRQueue_req_{}'.format(
        mcu_can)
    if mcu_name == 'GW':
        pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
            'ECUC-REFERENCE-VALUE'][1]['VALUE-REF']['#text'] = '/ActiveEcuC/PduR/Dcm'
        pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
            'ECUC-REFERENCE-VALUE'][0]['VALUE-REF']['#text'] = '/ActiveEcuC/EcuC/EcucPduCollection/DCM_UDS_{}_PhysReq_Rx'.format(local_or_remote)
        pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
            'ECUC-REFERENCE-VALUE'][2]['VALUE-REF']['#text'] = ''
    return pudrPath_tmp

def creat_phy_pudr_path_resp(mcu_name, mcu_can, local_or_remote, global_pdu, pdu_key):

    pudrPath_tmp = copy.deepcopy(PduRPath)
    # pudrPath_tmp['ECUC-CONTAINER-VALUE']['SHORT-NAME'] = 'DoIP_Tester2{}_Phys_Req_{}'.format(mcu_name,local_or_remote)
    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SHORT-NAME'] = 'DoIP_{}2Tester_Phys_Resp_{}'.format(mcu_name, local_or_remote)
    logging.debug('GENERATE PUDR PATH: DoIP_{}2Tester_Phys_Resp_{}'.format(mcu_name, local_or_remote))

    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][0][
        'SHORT-NAME'] = 'PduRSrcPdu_{}_{}_Phys_Resp'.format(local_or_remote, mcu_name)
    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][0]['REFERENCE-VALUES'][
        'ECUC-REFERENCE-VALUE'][0]['VALUE-REF'][
        '#text'] = '/ActiveEcuC/EcuC/EcucPduCollection/DCM_UDS_{}_PhysResp_Tx'.format(local_or_remote)
    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][0]['REFERENCE-VALUES'][
        'ECUC-REFERENCE-VALUE'][1]['VALUE-REF'][
        '#text'] = '/ActiveEcuC/PduR/Dcm'

    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1][
        'SHORT-NAME'] = 'PduRDestPdu_{}_{}_Phys_Resp'.format(local_or_remote, mcu_name)

    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
        'ECUC-REFERENCE-VALUE'][0]['VALUE-REF']['#text'] = '/ActiveEcuC/EcuC/EcucPduCollection/DCM_DoIP_{}_PhysResp_{}_Tx'.format(local_or_remote, mcu_name)

    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
        'ECUC-REFERENCE-VALUE'][1]['VALUE-REF']['#text'] = '/ActiveEcuC/PduR/DoIP'
    pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
        'ECUC-REFERENCE-VALUE'][2]['VALUE-REF']['#text'] = ''#queue

    return pudrPath_tmp

def creat_func_pudr_path( mcu_name, local_or_remote):
    if mcu_name != 'GW':
        pass
    else:
        pudrPath_tmp = copy.deepcopy(PduRPath)
        pudrPath_tmp['ECUC-CONTAINER-VALUE']['SHORT-NAME'] = 'DoIP_Tester2{}_Func_Req_{}'.format(mcu_name,
                                                                                             local_or_remote)
        logging.debug('GENERATE PUDR PATH: DoIP_Tester2{}_Func_Req_{}'.format(mcu_name,local_or_remote))
        pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][0][
            'SHORT-NAME'] = 'PduRSrcPdu_{}_{}_Func_Req'.format(local_or_remote, mcu_name)
        pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][0]['REFERENCE-VALUES'][
            'ECUC-REFERENCE-VALUE'][0]['VALUE-REF'][
            '#text'] = '/ActiveEcuC/EcuC/EcucPduCollection/DCM_DoIP_{}_FuncReq_Rx'.format(local_or_remote,
                                                                                             mcu_name)
        pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1][
            'SHORT-NAME'] = 'PduRDestPdu_{}_{}_Func_Req'.format(local_or_remote, mcu_name)

        pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
            'ECUC-REFERENCE-VALUE'][0]['VALUE-REF']['#text'] = '/ActiveEcuC/EcuC/EcucPduCollection/DCM_UDS_{}_FuncReq_Rx'.format(local_or_remote)
        pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
                'ECUC-REFERENCE-VALUE'][1]['VALUE-REF']['#text'] = '/ActiveEcuC/PduR/Dcm'
        pudrPath_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES'][
            'ECUC-REFERENCE-VALUE'][2]['VALUE-REF']['#text'] = ''  # queue

        # print(pudrPath_tmp)
    return pudrPath_tmp

def creat_new_pudr_path(mcu_node_dir, diag_pdus, is_remote=True):
    mcu_name = mcu_node_dir['MCU_NAME']
    mcu_can = mcu_node_dir['CAN_NAME']

    if is_remote:
        local_or_remote_str = 'Remote'
    else:
        local_or_remote_str = 'Local'
    pdur_path_ret = []

    if mcu_name == 'GW':

        pdu_key = '{}_PhysReq_Rx'.format(mcu_name)
        pdur_path_phy = creat_phy_pudr_path_req(mcu_name, mcu_can, local_or_remote_str, diag_pdus, pdu_key)
        pdur_path_func = creat_func_pudr_path(mcu_name, local_or_remote_str)
        pdur_path_phy_resp = creat_phy_pudr_path_resp(mcu_name, mcu_can, local_or_remote_str, diag_pdus, pdu_key)
        # print(pdur_path_phy)
        # print(pdur_path_func)
        # print(pdur_path_phy_resp)
        pdur_path_ret.append(pdur_path_phy)# 使用deep copy ,负责list中存放相同的字典值
        pdur_path_ret.append(pdur_path_phy_resp)
        pdur_path_ret.append(pdur_path_func)
    else:
        pdu_key = '{}_PhysReq_Tx'.format(mcu_name)
        pdur_path_phy = creat_phy_pudr_path_req(mcu_name, mcu_can, local_or_remote_str, diag_pdus, pdu_key)
        pdur_path_ret.append(pdur_path_phy)
    return pdur_path_ret

def creat_new_phy_channel(mcu_node_dir, rxpdu_id, txpdu_id, is_remote=True):
    mcu_name = mcu_node_dir['MCU_NAME']
    channel_tmp = DoIPChannel_Phy
    local_or_remote_str = ''
    if is_remote:
        local_or_remote_str = 'Remote'
    else:
        local_or_remote_str = 'Local'

    channel_tmp['ECUC-CONTAINER-VALUE']['SHORT-NAME'] = 'DoIPChannel_Phy_{0}_{1}'.format(local_or_remote_str, mcu_name)
    channel_tmp['ECUC-CONTAINER-VALUE']['REFERENCE-VALUES']['ECUC-REFERENCE-VALUE'][0]['VALUE-REF']['#text'] = '/ActiveEcuC/DoIP/DoIPConfigSet/{0}_Tester'.format(local_or_remote_str)
    channel_tmp['ECUC-CONTAINER-VALUE']['REFERENCE-VALUES']['ECUC-REFERENCE-VALUE'][1]['VALUE-REF']['#text'] = '/ActiveEcuC/DoIP/DoIPConfigSet/DoIPConnections/DoIPTargetAddress_{0}_{1}'.format(mcu_name, local_or_remote_str)
    
    # rx pdu name
    channel_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][0]['SHORT-NAME'] = 'DoIPPduRRxPdu_Phy_{0}_Rx_{1}'.format(mcu_name, local_or_remote_str)
    
    # rx pdu id
    channel_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][0]['PARAMETER-VALUES']['ECUC-NUMERICAL-PARAM-VALUE']['VALUE'] = str(rxpdu_id)
    channel_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][0]['REFERENCE-VALUES']['ECUC-REFERENCE-VALUE']['VALUE-REF']['#text'] = '/ActiveEcuC/EcuC/EcucPduCollection/DCM_DoIP_{0}_PhysReq_{1}_Rx'.format(local_or_remote_str, mcu_name)

    # tx pdu name
    channel_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['SHORT-NAME'] = 'DoIPPduRTxPdu_Phy_{0}_Tx_{1}'.format(mcu_name, local_or_remote_str)
    
    # rx pdu id
    channel_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['PARAMETER-VALUES']['ECUC-NUMERICAL-PARAM-VALUE']['VALUE'] = str(txpdu_id)
    channel_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE'][1]['REFERENCE-VALUES']['ECUC-REFERENCE-VALUE']['VALUE-REF']['#text'] = '/ActiveEcuC/EcuC/EcucPduCollection/DCM_DoIP_{0}_PhysResp_{1}_Tx'.format(local_or_remote_str, mcu_name)

    return channel_tmp

def creat_new_fun_channel(mcu_node_dir, rxpdu_id, is_remote=True):
    mcu_name = mcu_node_dir['MCU_NAME']
    channel_tmp = DoIPChannel_Func
    local_or_remote_str = ''
    if is_remote:
        local_or_remote_str = 'Remote'
    else:
        local_or_remote_str = 'Local'

    channel_tmp['ECUC-CONTAINER-VALUE']['SHORT-NAME'] = 'DoIPChannel_Func_{0}_{1}'.format(local_or_remote_str, mcu_name)
    channel_tmp['ECUC-CONTAINER-VALUE']['REFERENCE-VALUES']['ECUC-REFERENCE-VALUE'][0]['VALUE-REF']['#text'] = '/ActiveEcuC/DoIP/DoIPConfigSet/{0}_Tester'.format(local_or_remote_str)
    channel_tmp['ECUC-CONTAINER-VALUE']['REFERENCE-VALUES']['ECUC-REFERENCE-VALUE'][1]['VALUE-REF']['#text'] = '/ActiveEcuC/DoIP/DoIPConfigSet/DoIPConnections/DoIPTargetAddress_Func_{0}_{1}'.format(mcu_name, local_or_remote_str)
    
    # rx pdu name
    channel_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE']['SHORT-NAME'] = 'DoIPPduRRxPdu_Func_{0}_Rx_{1}'.format(mcu_name, local_or_remote_str)
    
    # rx pdu id
    channel_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE']['PARAMETER-VALUES']['ECUC-NUMERICAL-PARAM-VALUE']['VALUE'] = str(rxpdu_id)
    channel_tmp['ECUC-CONTAINER-VALUE']['SUB-CONTAINERS']['ECUC-CONTAINER-VALUE']['REFERENCE-VALUES']['ECUC-REFERENCE-VALUE']['VALUE-REF']['#text'] = '/ActiveEcuC/EcuC/EcucPduCollection/DCM_DoIP_{0}_FuncReq_Rx'.format(local_or_remote_str)

    return channel_tmp

def creat_new_DoIPRoutingActivation(routingActvationID, is_remote=True):
    local_or_remote_str = ''
    if is_remote:
        local_or_remote_str = 'Remote'
    else:
        local_or_remote_str = 'Local'
    
    DoIPRoutingActivation_tmp = DoIPRoutingActivation
    DoIPRoutingActivation_tmp['ECUC-CONTAINER-VALUE']['SHORT-NAME'] = 'DoIPRoutingActivation_{0}'.format(local_or_remote_str)
    #DoIPRoutingActivation_tmp['ECUC-CONTAINER-VALUE']['PARAMETER-VALUES']['ECUC-NUMERICAL-PARAM-VALUE']['VALUE'] = str(routingActvationID)
    return DoIPRoutingActivation_tmp

def creat_new_Tester(testerLogicalAddr, is_remote=True):
    local_or_remote_str = ''
    if is_remote:
        local_or_remote_str = 'Remote'
    else:
        local_or_remote_str = 'Local'
    
    DoIPTester_tmp = DoIPTester
    DoIPTester_tmp['ECUC-CONTAINER-VALUE']['SHORT-NAME'] = '{0}_Tester'.format(local_or_remote_str)
    DoIPTester_tmp['ECUC-CONTAINER-VALUE']['PARAMETER-VALUES']['ECUC-NUMERICAL-PARAM-VALUE'][1]['VALUE'] = str(testerLogicalAddr)
    DoIPTester_tmp['ECUC-CONTAINER-VALUE']['REFERENCE-VALUES']['ECUC-REFERENCE-VALUE']['VALUE-REF']['#text'] = '/ActiveEcuC/DoIP/DoIPConfigSet/DoIPRoutingActivation_{0}'.format(local_or_remote_str)
    return DoIPTester_tmp

def creat_new_target_Address(mcu_node_dir, is_remote):
    mcu_name = mcu_node_dir['MCU_NAME']
    target_address_tmp = DoIPTargetAddress
    local_or_remote_str = ''
    if is_remote:
        local_or_remote_str = 'Remote'
    else:
        local_or_remote_str = 'Local'

    target_address_tmp['ECUC-CONTAINER-VALUE']['SHORT-NAME'] = 'DoIPTargetAddress_{0}_{1}'.format(mcu_name, local_or_remote_str)
    target_address_tmp['ECUC-CONTAINER-VALUE']['PARAMETER-VALUES']['ECUC-NUMERICAL-PARAM-VALUE'][0]['VALUE'] = str(mcu_node_dir['LOGICAL_ADD'])

    return target_address_tmp

def test():
    root = etree.Element('ECUC-CONTAINER-VALUE')
    parseData(DoIPTester['ECUC-CONTAINER-VALUE'], root)
    xml_write(root, 'test.xml')


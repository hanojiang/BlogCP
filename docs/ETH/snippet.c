
/**********************************************************************************************************************
 *  EthSwt_30_88Q5050_LL_GetHwPortAddr()
 *********************************************************************************************************************/
/*! \brief       Transforms the configuration port identifier (SNV) to the hardware port register offset (used in registers)
 *  \details     -
 *  \param[in]   swtIdx   Identifier of the switch
 *  \param[in]   portIdx  Identifier of the port (SNV)
 *  \return      Hardware port address (used in registers)
 *  \pre         -
 *  \context     ANY
 *  \reentrant   TRUE
 *  \synchronous TRUE
 *********************************************************************************************************************/


ETHSWT_30_88Q5050_LL_HWACCESS_LOCAL_INLINE_FUNC(uint8) EthSwt_30_88Q5050_LL_GetHwPortAddr( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
    uint8 swtIdx,
    uint8 portIdx)
{
  uint8 address;

  /* #10 If the switch variant is 88Q5050 */
  if( EthSwt_30_88Q5050_Cfg_GetDeviceId(swtIdx) == ETHSWT_30_88Q5050_88Q5050_DEVICEID )
  {
    /* #100 The Hardware Port Address offset of the 88Q5050 hardware is set */
    address = EthSwt_30_88Q5050_Cfg_GetPortHandling(swtIdx)->ConfigToHwPortIdxMap[portIdx];
  }
  /* #20 Otherwise */
  else
  {
    /* #200 The Hardware Port Address offset of the 88EA6321 hardware is set by adding 0x10 to Port Address offset of the 88Q5050 */
    address = EthSwt_30_88Q5050_Cfg_GetPortHandling(swtIdx)->ConfigToHwPortIdxMap[portIdx] + ETHSWT_30_88Q5050_88EA6321_PORT_INDEXSHIFT;
  }

  return address;
}

ETHSWT_30_88Q5050_LOCAL CONST(uint8, ETHSWT_30_88Q5050_CONST) EthSwt_30_88Q5050_SnvToHwPortMap_LEthernetSwitch_A_3bf3cdb3[8] =
{
  ETHSWT_PORT_1, 
  ETHSWT_PORT_2, 
  ETHSWT_PORT_3, 
  ETHSWT_PORT_4, 
  ETHSWT_PORT_5, 
  ETHSWT_PORT_6, 
  ETHSWT_PORT_7, 
  ETHSWT_PORT_8
};

ETHSWT_30_88Q5050_LL_LOCAL_INLINE_FUNC(boolean) EthSwt_30_88Q5050_LL_IsDeviceAccessPossible( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
  uint8 swtIdx)
{
  boolean result = FALSE;
  EthSwt_30_88Q5050_LL_RegAddrType regAddr;

  /* read the EType Register of Port 1 because it is one of the rare registers having a defined default value that
   * can be used to check if device is accessible */
  regAddr.DevAddr = EthSwt_30_88Q5050_LL_GetHwPortAddr(swtIdx, ETHSWT_30_88Q5050_REG_PORT1_DEVICE_ADDR);//这里直接传ETHSWT_30_88Q5050_REG_PORT1_DEVICE_ADDR，和实际的不对应。
  regAddr.RegAddr = ETHSWT_30_88Q5050_REG_PORT_N_PORT_ETYPE_REG_ADDR;

  if( EthSwt_30_88Q5050_LL_Reg_SyncReadU16(swtIdx, &regAddr) == ETHSWT_30_88Q5050_REG_PORT_N_PORT_ETYPE_DEFAULT_VAL )
  {
    result = TRUE;
  }
  regAddr.DevAddr = EthSwt_30_88Q5050_LL_GetHwPortAddr(swtIdx, ETHSWT_30_88Q5050_REG_PORT1_DEVICE_ADDR);
  regAddr.RegAddr = ETHSWT_30_88Q5050_REG_PORT_N_SWITCH_IDENTIFIER_REG_ADDR;

  if( (EthSwt_30_88Q5050_LL_Reg_SyncReadU16(swtIdx, &regAddr) & ETHSWT_30_88Q5050_REG_PORT_N_SWITCH_IDENTIFIER_PRODUCT_MASK) == (uint16)EthSwt_30_88Q5050_Cfg_GetDeviceId(swtIdx) )
  {
    result = TRUE;
  }

  return result;
} /* EthSwt_30_88Q5050_LL_IsDeviceAccessPossible() */


/**********************************************************************************************************************
 *  EthSwt_30_88Q5050_LL_Reg_SyncReadU16()
 *********************************************************************************************************************/
/*! \brief       Reads an uint16 register in a synchronous way
 *  \details     -
 *  \param[in]   swtIdx   Identifier of the switch
 *  \param[in]   regAddr  Addressing data of the register
 *  \return      Register value read
 *  \pre         -
 *  \context     ANY
 *  \reentrant   FALSE
 *  \synchronous TRUE
 *********************************************************************************************************************/

ETHSWT_30_88Q5050_LL_HWACCESS_LOCAL_INLINE_FUNC(uint16) EthSwt_30_88Q5050_LL_Reg_SyncReadU16( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
          uint8                                                                 swtIdx,
  P2CONST(EthSwt_30_88Q5050_LL_RegAddrType, AUTOMATIC, ETHSWT_30_88Q5050_CONST) regAddr)
{
  uint16 regVal = 0;

  /* #10 Single-chip addressing mode is used */
  if( EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(swtIdx)->MiiAddress == ETHSWT_30_88Q5050_LL_SINGLE_CHIP_ADDRESSING_MODE )
  {
    /* #100 Use configured MII function to read data directly */
    (void)EthSwt_30_88Q5050_Cfg_ReadMii(swtIdx, regAddr->DevAddr, regAddr->RegAddr, &regVal);
  }
  /* #20 Multi-chip addressing mode is used */
  else
  {
    /* #200 Read data indirectly */
    (void)EthSwt_30_88Q5050_LL_ReadMultiChipAddressingMode(swtIdx, regAddr->DevAddr, regAddr->RegAddr, &regVal);
  }

  return regVal;
} 


ETHSWT_30_88Q5050_LL_HWACCESS_LOCAL_INLINE_FUNC(Std_ReturnType) EthSwt_30_88Q5050_LL_ReadMultiChipAddressingMode( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
        uint8                                                          swtIdx,
        uint8                                                          miiAddr,
        uint8                                                          regAddr,
  P2VAR(uint16, ETHSWT_30_88Q5050_CONST, ETHSWT_30_88Q5050_VAR_NOINIT) regValPtr)
{
  Std_ReturnType retVal;
  uint16 smiCmd;

  /* #10 Enter Exclusive Area (Reason: Prevent interruption of SMI command sequence in multi chip adressing mode which
   *     could result in read of arbitrary registers) */
  EthSwt_EnterExclusiveArea(88Q5050, SMI_MULTI_CHIP_ACCESS); /* PRQA S 3109 临界区 */ /* MD_MSR_14.3 */

  /* #20 Wait for access to SMI_CMD register */
  retVal = EthSwt_30_88Q5050_LL_SmiCmdAccess_SynchronizeSmiAccess(swtIdx);

  if( retVal == E_OK )
  {
    /* #210 Prepare SMI_CMD register data */
    smiCmd  = ETHSWT_30_88Q5050_LL_SMI_BUSY;
    smiCmd |= ETHSWT_30_88Q5050_LL_SMI_MODE_1;
    smiCmd |= ETHSWT_30_88Q5050_LL_SMI_OP_READ;
    smiCmd |= (miiAddr << ETHSWT_30_88Q5050_LL_SMI_DEV_ADDR_SHIFT_LEFT) & ETHSWT_30_88Q5050_LL_SMI_DEV_ADDR_MASK;
    smiCmd |= (regAddr & ETHSWT_30_88Q5050_LL_SMI_REG_ADDR_MASK);

    /* #220 Write command */
    retVal = EthSwt_30_88Q5050_Cfg_WriteMii(swtIdx,
                                            EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(swtIdx)->MiiAddress,
                                            ETHSWT_30_88Q5050_LL_SMI_CMD,
                                            smiCmd);

    if( retVal == E_OK )
    {
      /* #2210 Wait for end of previous command */
      retVal = EthSwt_30_88Q5050_LL_SmiCmdAccess_SynchronizeSmiAccess(swtIdx);

      if( retVal == E_OK )
      {
        /* #22110 Read data */
        retVal = EthSwt_30_88Q5050_Cfg_ReadMii(swtIdx,
                                               EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(swtIdx)->MiiAddress,
                                               ETHSWT_30_88Q5050_LL_SMI_DATA,
                                               regValPtr);
      }
    }
  }

  /* #30 Leave Exclusive Area */
  EthSwt_ExitExclusiveArea(88Q5050, SMI_MULTI_CHIP_ACCESS); /* PRQA S 3109 */ /* MD_MSR_14.3 */

  return retVal;
} /* EthSwt_30_88Q5050_LL_ReadMultiChipAddressingMode() */

ETHSWT_30_88Q5050_LL_HWACCESS_LOCAL_INLINE_FUNC(Std_ReturnType) EthSwt_30_88Q5050_LL_SmiCmdAccess_SynchronizeSmiAccess( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
  uint8 swtIdx)
{
  uint32_least cnt;
  uint16 regVal = 0;
  Std_ReturnType result = E_NOT_OK;

  /* #10 Try to read register until timeout */
  for( cnt = 0; cnt < EthSwt_30_88Q5050_Cfg_GetHwAccessTries(); cnt++ )
  {
    /* #100 Read register */
    (void)EthSwt_30_88Q5050_Cfg_ReadMii(swtIdx,
                                        EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(swtIdx)->MiiAddress,
                                        ETHSWT_30_88Q5050_LL_SMI_CMD,
                                        &regVal);

    /* #110 Exit loop when register is free */
    if( (regVal & ETHSWT_30_88Q5050_LL_SMI_BUSY) == 0u )
    {
      result = E_OK;
      break;
    }
  }

#  if (ETHSWT_30_88Q5050_DEV_ERROR_DETECT == STD_ON)
  if( result == E_NOT_OK )
  {
    uint8 errorId = ETHSWT_30_88Q5050_E_HW_ACCESS_TIMEOUT;
#   if (ETHSWT_30_88Q5050_DEV_ERROR_REPORT == STD_ON)
    (void)Det_ReportError(ETHSWT_30_VECTOR_MODULE_ID, swtIdx, ETHSWT_30_88Q5050_SID_INTERNAL_SYNCHRONIZE_SMI_CMD_ACCESS, errorId);
#   else
    ETHSWT_30_88Q5050_DUMMY_STATEMENT(errorId); /* PRQA S 3112, 3199 */ /* MD_MSR_14.2 */ /*lint !e438 */
#   endif
  }
#  endif

  return result;
} /* EthSwt_30_88Q5050_LL_SmiCmdAccess_SynchronizeSmiAccess() */

ETHSWT_30_88Q5050_LL_HWACCESS_LOCAL_INLINE_FUNC(void) EthSwt_30_88Q5050_LL_Reg_SyncWriteU16( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
          uint8                                                                 swtIdx,
  P2CONST(EthSwt_30_88Q5050_LL_RegAddrType, AUTOMATIC, ETHSWT_30_88Q5050_CONST) regAddr,
          uint16                                                                regVal)
{
  /* #10 Single-chip addressing mode is used */
  if( EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(swtIdx)->MiiAddress == ETHSWT_30_88Q5050_LL_SINGLE_CHIP_ADDRESSING_MODE )
  {
    /* #100 Use configured MII function to write data directly */
    (void)EthSwt_30_88Q5050_Cfg_WriteMii(swtIdx, regAddr->DevAddr, regAddr->RegAddr, regVal);
  }
  /* #20 Multi-chip addressing mode is used */
  else
  {
    /* #200 Write data indirectly */
    (void)EthSwt_30_88Q5050_LL_WriteMultiChipAddressingMode(swtIdx, regAddr->DevAddr, regAddr->RegAddr, regVal);
  }
} /* EthSwt_30_88Q5050_LL_Reg_SyncWriteU16() */

ETHSWT_30_88Q5050_CFGACCESS_INT_LOCAL_INLINE_FUNC(Std_ReturnType) EthSwt_30_88Q5050_Cfg_ReadMii( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
               uint8                 swtIdx,
               uint8                 miiAddr,
               uint8                 regAddr,
  P2VAR(uint16, ETHSWT_30_88Q5050_CONST, ETHSWT_30_88Q5050_VAR_NOINIT) regVal)
{
  return EthSwt_30_88Q5050_Cfg_GetMiiHwAccess(swtIdx)->ReadMii(EthSwt_30_88Q5050_Cfg_GetMiiHwAccess(swtIdx)->CtrlIdx,
                                                               miiAddr,
                                                               regAddr,
                                                               regVal);
} /* EthSwt_30_88Q5050_Cfg_ReadMii() */

/**********************************************************************************************************************
 *  EthSwt_30_88Q5050_Cfg_WriteMii()
 *********************************************************************************************************************/
/*!
 * Internal comment removed.
 *
 *
 */
ETHSWT_30_88Q5050_CFGACCESS_INT_LOCAL_INLINE_FUNC(Std_ReturnType) EthSwt_30_88Q5050_Cfg_WriteMii( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
  uint8  swtIdx,
  uint8  miiAddr,
  uint8  regAddr,
  uint16 regVal)
{
  return EthSwt_30_88Q5050_Cfg_GetMiiHwAccess(swtIdx)->WriteMii(EthSwt_30_88Q5050_Cfg_GetMiiHwAccess(swtIdx)->CtrlIdx,
                                                                miiAddr,
                                                                regAddr,
                                                                regVal);
} /* EthSwt_30_88Q5050_Cfg_WriteMii() */


ETHSWT_30_88Q5050_LOCAL_INLINE_FUNC(Std_ReturnType) EthSwt_30_88Q5050_ResetDevice(
  uint8 swtIdx)
{
  Std_ReturnType retVal = E_OK;
  uint32_least   resetTries = EthSwt_30_88Q5050_Cfg_GetResetTries();
  boolean        resetResult;

  EthSwt_30_88Q5050_LL_TriggerDeviceReset(swtIdx); /*lint !e522 */

  do
  {
    resetResult = EthSwt_30_88Q5050_LL_IsDeviceResetFinished(swtIdx); /*lint !e522 */
    resetTries--;
  }
  while( (resetResult == FALSE) && (resetTries > 0) );

  if( (resetResult == FALSE) && (resetTries == 0) )
  {
    retVal = E_NOT_OK;
  }

  return retVal;
} /* EthSwt_30_88Q5050_ResetDevice() */


ETHSWT_30_88Q5050_LL_LOCAL_INLINE_FUNC(Std_ReturnType) EthSwt_30_88Q5050_LL_DownloadConfiguration( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
  uint8 swtIdx)
{
  Std_ReturnType retVal;

  /* #10 Setup RMU Access and enable RMU communication for download of configuration */
  EthSwt_30_88Q5050_LL_SetupRmuAccess(swtIdx);
  EthSwt_30_88Q5050_LL_EnableRmuComBeforeDownload(swtIdx);

  /* #20 register download */
  retVal = EthSwt_30_88Q5050_LL_RmuAccess_DownloadRegisterCommands(swtIdx,
                                                                EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(swtIdx)->DownloadRegs,
                                                                EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(swtIdx)->DownloadRegNum);

  /* #30 Check if the Register command list request user callout is configured */
  if ((EthSwt_30_88Q5050_Cfg_GetLlModuleConfig()->RegCmdListReqUserCallout != NULL_PTR) && (retVal == E_OK))
  {
    P2VAR (uint32, AUTOMATIC, ETHSWT_30_88Q5050_CONST) regCommands   = NULL_PTR;
           uint16                                      regCommandNum = 0;
    
    /* #310 Call the Register command list request user call out to retrieve Register commands and Number of Register Commands*/
    EthSwt_30_88Q5050_Cfg_GetLlModuleConfig()->RegCmdListReqUserCallout(swtIdx, &regCommands, &regCommandNum);

    /* #320 Validate the returned regCommands */
    if (regCommands != NULL_PTR)
    {
      /* #3210 If regCommands and regCommandNum is valid then perform the Register commands download */
      retVal = EthSwt_30_88Q5050_LL_RmuAccess_DownloadRegisterCommands(swtIdx, regCommands, regCommandNum);
    }
  }

  /* #40 Tear down download setup */
  EthSwt_30_88Q5050_LL_DisableRmuComAfterDownload(swtIdx);

  return retVal;
} /* EthSwt_30_88Q5050_LL_DownloadConfiguration() */


ETHSWT_30_88Q5050_LL_HWACCESS_LOCAL_INLINE_FUNC(void) EthSwt_30_88Q5050_LL_SetupRmuAccess( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
  uint8 swtIdx)
{
  uint8_least macIdx;
  EthSwt_30_88Q5050_LL_RegAddrType regAddr;

  /* Set MAC address of switch for RMU communication */
  regAddr.DevAddr = ETHSWT_30_88Q5050_REG_GLOBAL2_DEVICE_ADDR;
  regAddr.RegAddr = ETHSWT_30_88Q5050_REG_GLOBAL2_SWITCH_MAC_WOL_WOF_REG_ADDR;

  for( macIdx = 0; macIdx < ETH_PHYS_ADDR_LEN_BYTE; macIdx++ )
  {
    EthSwt_30_88Q5050_LL_Reg_SyncWriteU16(swtIdx, &regAddr, (uint16)(0x8000 | (macIdx << 8) | EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(swtIdx)->RmuMac[macIdx]));
  }

  /* Set device ID of switch for RMU communication */
  regAddr.DevAddr = ETHSWT_30_88Q5050_REG_GLOBAL1_DEVICE_ADDR;
  regAddr.RegAddr = ETHSWT_30_88Q5050_REG_GLOBAL1_GLB_CTRL2_REG_ADDR;
  EthSwt_30_88Q5050_LL_Reg_SyncWriteU16(swtIdx, &regAddr, EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(swtIdx)->RmuSetupSwtGlbCtrl2RegVal);
} /* EthSwt_30_88Q5050_LL_PrepareRmuAccess() */



ETHSWT_30_88Q5050_LL_HWACCESS_LOCAL_INLINE_FUNC(void) EthSwt_30_88Q5050_LL_EnableRmuComBeforeDownload( /* PRQA S 3219 */ /* MD_EthSwt_30_88Q5050_3219 */
  uint8 swtIdx)
{
  uint8 ctrlIdx;
  EthSwt_30_88Q5050_LL_RegAddrType regAddr;
  boolean repeat;

  uint8 curSwt = swtIdx;

  /* #10 Configure switch cascade from current switch to switch connected to host controller to enable
   *     RMU communication from current switch to switch connected to host controller */
  do
  {
    uint8 hostCpuCfgPort;
    uint8 hostCpuHwPort;
    uint16 regVal;

    repeat = FALSE;
    hostCpuCfgPort = EthSwt_30_88Q5050_Cfg_GetPortToHostCpu(curSwt);
    hostCpuHwPort = EthSwt_30_88Q5050_LL_GetHwPortAddr(curSwt, hostCpuCfgPort);

    /* #110 Set DSA mode for management port of current switch */
    regAddr.DevAddr = hostCpuHwPort;
    regAddr.RegAddr = ETHSWT_30_88Q5050_REG_PORT_N_PORT_CTRL_REG_ADDR;
    regVal          = EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(curSwt)->RmuSetupHostPortPortCtrlRegVal;
    EthSwt_30_88Q5050_LL_Reg_SyncWriteU16(curSwt, &regAddr, regVal);
    /* #120 Force a link on the port so communication is possible */
    regAddr.RegAddr = ETHSWT_30_88Q5050_REG_PORT_N_PHY_CTRL_REG_ADDR;
    regVal          = EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(curSwt)->RmuSetupHostPortPhyCtrlRegVal;
    EthSwt_30_88Q5050_LL_Reg_SyncWriteU16(curSwt, &regAddr, regVal);
    /* #130 Setup Fiber Control register and trigger reset if SGMII is the xMII connection type for the host port -
     *      This is only applicable for 88Q5050 because there can be no SGMII host port for 88EA632X derivatives */
    if( EthSwt_30_88Q5050_Cfg_GetDeviceId(curSwt) == ETHSWT_30_88Q5050_88Q5050_DEVICEID )
    {
      if( EthSwt_30_88Q5050_Cfg_GetPortXMiiConnectionType(curSwt, hostCpuCfgPort) == ETHSWT_SGMII)
      {
        regAddr.RegAddr = ETHSWT_30_88Q5050_88EA6321_REG_SERDES_FIBERCONTROL_REG_ADDR;
        regVal = EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(curSwt)->RmuSetupHostPortFiberCtrlRegVal;
        (void)EthSwt_30_88Q5050_LL_PhyAccess_WriteRegSmi(curSwt,
                                                         regAddr.DevAddr,
                                                         regAddr.RegAddr,
                                                         regVal,
                                                         ETHSWT_30_88Q5050_LL_ACCESS_INTERNAL_PHY);
      }
    }

    /* #140 If the cascading level of the current switch is greater than zero the uplink port of the
     *      corresponding uplink switch needs to be configured */
    if( EthSwt_30_88Q5050_Cfg_GetCascMap(curSwt)->CascadingLevel > 0 )
    {
      uint8 uplinkSwt;
      uint8 uplinkPort;
      uint8 uplinkPortCfg;

      /* #1410 Get next switch in cascade and its port connected to the current switch */
      uplinkSwt  = EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(curSwt)->RmuSetupUplinkSwitch;
      uplinkPort = EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(curSwt)->RmuSetupUplinkPort;

      /* #1420 Get the smi device address for port connected to current switch */
      if( EthSwt_30_88Q5050_Cfg_GetDeviceId(uplinkSwt) == ETHSWT_30_88Q5050_88Q5050_DEVICEID )
      {
        regAddr.DevAddr = uplinkPort;
      }
      else
      {
        regAddr.DevAddr = uplinkPort + ETHSWT_30_88Q5050_88EA6321_PORT_INDEXSHIFT;
      }
      /* #1430 Set DSA mode for port connected to current switch */
      regAddr.RegAddr = ETHSWT_30_88Q5050_REG_PORT_N_PORT_CTRL_REG_ADDR;
      regVal          = EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(curSwt)->RmuSetupUplinkPortPortCtrlRegVal;
      EthSwt_30_88Q5050_LL_Reg_SyncWriteU16(uplinkSwt, &regAddr, regVal);

      /* #1440 Force a link on the port connected to current switch so communication is possible */
      regAddr.RegAddr = ETHSWT_30_88Q5050_REG_PORT_N_PHY_CTRL_REG_ADDR;
      regVal          = EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(curSwt)->RmuSetupUplinkPortPhyCtrlRegVal;
      EthSwt_30_88Q5050_LL_Reg_SyncWriteU16(uplinkSwt, &regAddr, regVal);

      /* #1450 Setup Fiber Control register and trigger reset if SGMII is the xMII connection type for port
       *       connected to current switch */
      uplinkPortCfg = EthSwt_30_88Q5050_Cfg_GetConfigFromHwPortIdx(uplinkSwt, uplinkPort);

      if( EthSwt_30_88Q5050_Cfg_GetPortXMiiConnectionType(uplinkSwt, uplinkPortCfg) == ETHSWT_SGMII)
      {
        /* #14510 For 88EA632X derivatives the page needs to be selected first and the device address needs to me adapted */
        if( EthSwt_30_88Q5050_Cfg_GetDeviceId(uplinkSwt) != ETHSWT_30_88Q5050_88Q5050_DEVICEID )
        {
          regAddr.DevAddr = uplinkPort + ETHSWT_30_88Q5050_88EA6321_REG_SERDES_DEVICE_ADDR_OFFS;

          /* #145110 Set page 1 to access Fiber Control register */
          regAddr.RegAddr = ETHSWT_30_88Q5050_88EA6321_REG_SERDES_PAGE_SELECT_REG_ADDR;
          regVal = ETHSWT_30_88Q5050_88EA6321_REG_SERDES_PAGE_SELECT_PAGE1_VAL;
          (void)EthSwt_30_88Q5050_LL_PhyAccess_WriteRegSmi(uplinkSwt,
                                                           regAddr.DevAddr,
                                                           regAddr.RegAddr,
                                                           regVal,
                                                           ETHSWT_30_88Q5050_LL_ACCESS_INTERNAL_PHY);
        }
        /* #14520 Write to fiber control register */
        regAddr.RegAddr = ETHSWT_30_88Q5050_88EA6321_REG_SERDES_FIBERCONTROL_REG_ADDR;
        regVal = EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(curSwt)->RmuSetupUplinkPortFiberCtrlRegVal;
        (void)EthSwt_30_88Q5050_LL_PhyAccess_WriteRegSmi(uplinkSwt,
                                                         regAddr.DevAddr,
                                                         regAddr.RegAddr,
                                                         regVal,
                                                         ETHSWT_30_88Q5050_LL_ACCESS_INTERNAL_PHY);
      }

      /* #1460 Configure device map table to enable DSA forwarding in switch connected to current switch -
       *       (target device is the switch where the configuration will be downloaded -> swtIdx) */
      regAddr.DevAddr = ETHSWT_30_88Q5050_REG_GLOBAL2_DEVICE_ADDR;
      regAddr.RegAddr = ETHSWT_30_88Q5050_REG_GLOBAL2_DEVICE_MAP_TABLE_REG_ADDR;
      regVal          = (uint16)(ETHSWT_30_88Q5050_REG_GLOBAL2_DEVICE_MAP_TABLE_UPDATE_DATA_MASK |
                                 (uint16)((uint32)EthSwt_30_88Q5050_Cfg_GetLlSwtConfig(swtIdx)->MiiAddress <<
                                     ETHSWT_30_88Q5050_REG_GLOBAL2_DEVICE_MAP_TABLE_TARGET_DEV_VAL_SHIFT) |
                                 uplinkPort);
      EthSwt_30_88Q5050_LL_Reg_SyncWriteU16(uplinkSwt, &regAddr, regVal);

      /* #1470 Configure CPU destination in switch connected to current switch */
      hostCpuHwPort = EthSwt_30_88Q5050_LL_GetHwPortAddr(uplinkSwt, EthSwt_30_88Q5050_Cfg_GetPortToHostCpu(uplinkSwt));
      regAddr.DevAddr = ETHSWT_30_88Q5050_REG_GLOBAL1_DEVICE_ADDR;
      regAddr.RegAddr = ETHSWT_30_88Q5050_REG_GLOBAL1_MON_MGMT_CTRL_REG_ADDR;
      if( EthSwt_30_88Q5050_Cfg_GetDeviceId(uplinkSwt) == ETHSWT_30_88Q5050_88Q5050_DEVICEID )
      {
        regVal = (uint16)(ETHSWT_30_88Q5050_REG_GLOBAL1_MON_MGMT_CTRL_UPDATE_DATA_MASK |
                          ETHSWT_30_88Q5050_REG_GLOBAL1_CPU_DESTINATION_REGISTER_MASK |
                          hostCpuHwPort);
      }
      else
      {
        regVal = (uint16)(ETHSWT_30_88Q5050_88EA6321_REG_GLOBAL1_DISABLE_MIRROR_MASK |
                          (uint16)((hostCpuHwPort - ETHSWT_30_88Q5050_88EA6321_PORT_INDEXSHIFT) <<
                                   ETHSWT_30_88Q5050_88EA6321_REG_GLOBAL1_CPU_DEST_SHIFT));
      }
      EthSwt_30_88Q5050_LL_Reg_SyncWriteU16(uplinkSwt, &regAddr, regVal);

      /* #1480 Continue configuration with cascaded switch */
      curSwt = uplinkSwt;
      repeat = TRUE;
    }
  } while( repeat == TRUE );

  /* #20 Enable Ethernet controller */
  ctrlIdx = EthSwt_30_88Q5050_Cfg_GetMgmtEntityForSwt(swtIdx)->EthCtrlIdx;
  (void)EthSwt_30_88Q5050_Cfg_GetLlMgmtEntityForSwt(swtIdx)->CtrlInit(ctrlIdx, 0u);
  (void)EthSwt_30_88Q5050_Cfg_GetLlMgmtEntityForSwt(swtIdx)->SetCtrlMode(ctrlIdx, ETH_MODE_ACTIVE);
} /* EthSwt_30_88Q5050_LL_EnableRmuComBeforeDownload() */ /* PRQA S 6050 */



SchM_Enter_EthTrcv_30_Ethmii_ETHTRCV_30_ETHMII_EXCLUSIVE_AREA_SEQUENCE

EthTrcv_30_Ethmii_Internal_TransceiverInit
EthTrcv_30_Ethmii_SetTransceiverMode
EthTrcv_30_Ethmii_GetTransceiverMode
EthTrcv_30_Ethmii_StartAutoNegotiation
EthTrcv_30_Ethmii_GetLinkState
EthTrcv_30_Ethmii_GetBaudRate
EthTrcv_30_Ethmii_GetDuplexMode
EthTrcv_30_Ethmii_SetPhyTestMode
EthTrcv_30_Ethmii_SetPhyLoopbackMode
EthTrcv_30_Ethmii_GetPhySignalQuality
EthTrcv_30_Ethmii_SetPhyTxMode
EthTrcv_30_Ethmii_GetCableDiagnosticsResult
EthTrcv_30_Ethmii_Internal_ReadCl45TrcvReg
EthTrcv_30_Ethmii_Internal_WriteCl45TrcvReg

SchM_Enter_EthTrcv_30_88Q1010_ETHTRCV_30_88Q1010_EXCLUSIVE_AREA_SEQUENCE
EthTrcv_30_88Q1010_Internal_TransceiverInit 1
EthTrcv_30_88Q1010_SetTransceiverMode ON
EthTrcv_30_88Q1010_GetTransceiverMode OFF
EthTrcv_30_88Q1010_StartAutoNegotiation OFF
EthTrcv_30_88Q1010_GetLinkState OFF
EthTrcv_30_88Q1010_GetBaudRate OFF
EthTrcv_30_88Q1010_GetDuplexMode OFF
EthTrcv_30_88Q1010_SetPhyTestMode OFF
EthTrcv_30_88Q1010_SetPhyLoopbackMode OFF
EthTrcv_30_88Q1010_GetPhySignalQuality OFF
EthTrcv_30_88Q1010_SetPhyTxMode OFF
EthTrcv_30_88Q1010_GetCableDiagnosticsResult OFF
EthTrcv_30_88Q1010_Internal_ReadCl45TrcvReg 1 1 1 1 1 //4
EthTrcv_30_88Q1010_Internal_WriteCl45TrcvReg 1 1 1 1 1 //5

EthTrcv_30_88Q1010_Internal_ReadCl45TrcvReg调用
EthTrcv_30_88Q1010_Internal_WriteTrcvReg 3次
EthTrcv_30_88Q1010_Internal_ReadTrcvReg 1次

EthTrcv_30_88Q1010_Internal_WriteCl45TrcvReg调用
EthTrcv_30_88Q1010_Internal_WriteTrcvReg 3次
EthTrcv_30_88Q1010_Internal_WriteTrcvReg 1次

共调用
EthTrcv_30_88Q1010_Internal_WriteTrcvReg 5*3 + 5*4 = 35 //5*3+4*3
EthTrcv_30_88Q1010_Internal_ReadTrcvReg 5*1 = 5

EthTrcv_30_88Q1010_Internal_WriteTrcvReg调用
Eth_30_Enet_Internal_ReadMii
Eth_30_Enet_Internal_WriteMii

EthTrcv_30_88Q1010_Internal_ReadTrcvReg调用
Eth_30_Enet_Internal_ReadMii
Eth_30_Enet_Internal_WriteMii
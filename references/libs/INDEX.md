# ctrlX PLC library reference — index

Generated from `R911430583_01_EN_ctrlX PLC Engineering, PLC Libraries 03VRS, Reference Book.pdf` by `scripts/pdf_to_libref.py`. Search this index (or grep the files) for a name, then read just that section.

## 4 Standard  →  `04_Standard.md` (16 KB, p. 30–46)

CONCAT, DELETE, FIND, INSERT, LEFT, LEN, MID, REPLACE, RIGHT, RS, SR, F_TRIG, R_TRIG, CTD, CTU, CTUD, RTC, TOF, TON, TP

## 5 Standard64  →  `05_Standard64.md` (8 KB, p. 46–57)

WCONCAT, WDELETE, WFIND, WINSERT, WLEFT, WLEN, WMID, WREPLACE, WRIGHT, LTOF, LTON, LTP

## 6 Util  →  `06_Util.md` (19 KB, p. 57–72)

BCD_TO_INT, INT_TO_BCD, EXTRACT, PACK, PUTBIT, UNPACK, DERIVATIVE, INTEGRAL, LIN_TRAFO, STATISTICS_INT, STATISTICS_REAL, VARIANCE, PD, PID, PID_FIXCYCLE, BLINK, FREQ_MEASURE, GEN, CHARCURVE, RAMP_INT, RAMP_REAL, HYSTERESIS, LIMITALARM

## 7 CXA_CommonTypes  →  `07_CXA_CommonTypes.md` (11 KB, p. 72–78)

CXA_PLC_MAINDIAG_ERROR, CXA_PLC_DETAILDIAG_ERROR, AXIS_REF, AXES_GROUP_REF, DEVICE_REF, IL_HANDLE, ERROR_CODE, ERROR_STRUCT, ERROR_TABLE, SYS_TIME64, SYS_TIME_DATE, EXT_SYS_TIME_DATE

## 8 CXA_Crosscut  →  `08_CXA_Crosscut.md` (49 KB, p. 78–95)

MB_CORR_PROFILE (ENUM), MB_POINT_TABLE_DATA (STRUCT), MB_PUSH_OUT_CONFIG (STRUCT), MB_RESOLUTION (ENUM), MB_STEP_MOTION_LAW (ENUM), MB_STOP_CONFIG (STRUCT), MB_CrossCutType01, MB_CrossCutCalcType01, MB_WriteCrossCutProfile

## 9 CXA_ctrlXIO  →  `09_CXA_ctrlXIO.md` (6 KB, p. 95–99)

IH_XISerialCom

## 10 CXA_DataLayer  →  `10_CXA_DataLayer.md` (86 KB, p. 99–139)

DL_BrowseNode, DL_CreateNode, DL_ReadNode, DL_WriteNode, DL_DeleteNode, DL_NodeValue, DL_CreateNodeValue, DL_ReadNodeValue, DL_ReadNodeValueType02, DL_WriteNodeValue, DL_MetaDataNodeValue, DL_BulkBrowseNodeValues, DL_BulkCreateNodeValues, DL_BulkDeleteNodeValues, DL_BulkMetaDataNodeValues, DL_BulkReadNodeValues, DL_BulkWriteNodeValues, DL_BulkRequest, DL_BulkResponse, DL_ConvertDLTimestamp, DL_CreateSubscription, DL_CreateEventSubscription, DL_Subscribe, BaseEventType, Example of a subscription, Example of an event, Example of an event with subscription, CreateMemory, DeleteMemory, SetMemoryMap, BeginAccess, EndAccess, GetMemoryMap, GetSize, GetType, Example DL_MemOwner, CloseMemory, OpenMemory, BeginAccess, EndAccess, GetMemoryMap, GetSize, GetType, Example DL_MemUser, WSTRING data type, FlatBuffer

## 11 CXAC_Diagnostics  →  `11_CXAC_Diagnostics.md` (7 KB, p. 139–146)

RegisterDiagnostics, UnregisterDiagnostics, SetDiagnostics, ResetDiagnostics, ClearDiagnostics, ClearAllPendingDiagnostics, GetPendingDiagnostics

## 12 CXA_DriveUtil  →  `12_CXA_DriveUtil.md` (74 KB, p. 146–182)

MB_PowerSupplyDriveIntegrated, MB_ECATSoEPowerSupplyStandalone, MB_ECATSoEPowerSupplyDcDcIslandGrid, MB_ECATCoEFreqConv, MB_ECATCoEFreqConvCtrlWordEnCoding, MB_ECATCoE402FreqConv, MB_ECATCoEFreqConv402CtrlWordEnCoding, MB_ECATCoETorque, MB_ECATCoEFreqConvTorqueCtrlWordEnCoding, MB_ECATCoEFreqConv_FnT, MB_ECATCoEFreqConvCtrlWordEnCoding_FnT

## 13 CXA_EthercatMaster  →  `13_CXA_EthercatMaster.md` (210 KB, p. 182–258)

IL_ECATSoeRead, IL_ECATSoeWrite, IL_ECATSoeCommand, IL_ECATCoeReadSdo, IL_ECATCoeWriteSdo, IL_ECATAoeGetConfigInfo, IL_ECATAoeRead, IL_ECATAoeWrite, IL_ECATVoeRead, IL_ECATVoeWrite, IL_ECATReadRegister, IL_ECATWriteRegister, IL_ECATGetConfigEthercatAddrList, IL_ECATGetEthercatAddrByName, IL_ECATGetNumConfigMailboxSlaves, IL_ECATGetNumConfigSlaves, IL_ECATGetNumOnlineDcSlaves, IL_ECATGetNumOnlineSlaves, IL_ECATGetSlaveConfigInfo, IL_ECATGetSlaveOnlineInfo, IL_ECATMasterState, IL_ECATRemoteSlaveState, IL_ECATGetDcSlaveConfigInfo, IL_ECATGetMasterFrameStatisticCounters, IL_ECATGetMasterMailboxStatisticCounters, IL_ECATResetMasterFrameStatisticCounters, IL_ECATGetSlaveStatisticAutoMode, IL_ECATGetSlaveStatisticCounters, IL_ECATResetSlaveStatisticCounters, IL_ECATSetSlaveStatisticAutoMode, IL_ECATSetSlaveStatisticAutoModeEnable, IL_ECATSetSlaveStatisticAutoModeIdleTime, IL_ECATMasterGetBusState, IL_ECATMasterSetBusState, IL_ECATRemoteSlaveGetDevState, IL_ECATRemoteSlaveSetDevState, IL_ECATSoeAttributeDecoding, IL_ECATSoeIdnCoding, IL_ECAT_ADDRESS_TYPE, IL_ECAT_BASE_DATA_TYPE, IL_ECAT_DC_SLAVE_CONFIG_INFO, IL_ECAT_PORT_ERROR_COUNTERS, IL_ECAT_SLAVE_STATISTIC_COUNTERS, IL_ECAT_SOE_ATTRIBUTE, IL_ECAT_SOE_DATA_LENGTH, IL_ECAT_SOE_DATA_STATUS, IL_ECAT_SOE_DATA_TYPE, IL_ECAT_SOE_ELEMENT, IL_ECAT_SOE_PARAM_TYPE, IL_ECAT_STATE, IL_ECAT_DL_STATUS, IL_ECAT_ESC_FEATURES, IL_ECAT_MASTER_FRAME_STATISTIC_COUNTERS, IL_ECAT_MASTER_MAILBOX_STATISTIC_COUNTERS, IL_ECAT_MASTER_PROTOCOL_STATISTIC, IL_ECAT_MASTER_PROTOCOL_STATISTIC_COUNTERS, IL_ECAT_MASTER_PROTOCOL_STATISTIC_PERIOD_COUNTERS, IL_ECAT_MASTER_STATE, IL_ECAT_MASTER_STATE_BITS, IL_ECAT_MBX_CONFIG_PROTOCOLS, IL_ECAT_MBX_ONLINE_PROTOCOLS, IL_ECAT_MBX_SIZE_INFO, IL_ECAT_MEMORY_INFO, IL_ECAT_PORT_STATE, IL_ECAT_RESET_MASTER_FRAME_STATISTIC_COUNTERS, IL_ECAT_RESET_MASTER_FRAME_STATISTIC_COUNTERS_BITS, IL_ECAT_SLAVE_CONFIG_INFO, IL_ECAT_SLAVE_IDENTITY_INFO, IL_ECAT_SLAVE_ONLINE_INFO, IL_ECAT_SLAVE_STATE, IL_ECAT_SLAVE_STATE_BITS

## 14 CXA_FileAsync  →  `14_CXA_FileAsync.md` (60 KB, p. 258–280)

Malfunction, IL_FileAsync, IL_FileReadAsync, IL_FileWriteAsync, IL_FileGetPosAsync, IL_FileSeekAsync, IL_FileCopyAsync, IL_FileRenameAsync, IL_FileDeleteAsync, IL_FileGetSizeAsync, IL_FileGetTimeAsync, IL_DirCreateAsync, IL_DirDeleteAsync, IL_DirRenameAsync, IL_DirGetCurrentAsync, IL_DirSetCurrentAsync, IL_DirReadAsync, IL_DIR_INFO (ENUM), IL_DIR_FILE_ASYNCSTATE (ENUM), IL_DIR_ENTRY_TYPE (ENUM), IL_DIR_FILE_TIME (STRUCT), IL_FILE_ACCESS_MODE (ENUM)

## 15 CXA_MBus  →  `15_CXA_MBus.md` (12 KB, p. 280–288)

Possible transmission rates, General information, Telegram types, Telegram description, Troubleshooting

## 16 CXA_ModbusRTU  →  `16_CXA_ModbusRTU.md` (222 KB, p. 288–388)

IH_MBGetCommEventCounter, IH_MBGetCommEventLog, IH_MBMaskWriteRegister, IH_MBReadCoils, IH_MBReadDeviceIdentification, IH_MBReadDiagnostics, IH_MBReadDiscreteInputs, IH_MBReadExceptionStatus, IH_MBReadFIFOQue, IH_MBReadFileRecord, IH_MBReadHoldingRegisters, IH_MBReadInputRegisters, IH_MBReadWriteMultipleRegisters, IH_S20MBRTUMaster, IH_S20MBRTUSlave, IH_XIMBRTUMaster, IH_XIMBRTUSlave, IH_MBWriteFileRecord, IH_MBWriteMultipleCoils, IH_MBWriteMultipleRegisters, IH_MBWriteSingleCoil, IH_MBWriteSingleRegister, IH_INLN_MB_DATA, IH_INLN_MB_DEV_IDCODE, IH_INLN_MB_FIFODATA, IH_S20_MB_CONFIG, IH_INLN_MB_TOKEN, IH_INLN_MB_SUBREQUESTS, IH_INLN_MB_RECORD, IH_INLN_MB_EVENTLOG

## 17 CXA_ModbusTCP  →  `17_CXA_ModbusTCP.md` (115 KB, p. 388–439)

Configuring with Siemens WinCC-flexible 2007, Configuring with Pro-face GP-Pro EX 2.2, IL_ModbusTCPServer, IL_ModbusTCPServerType02, IL_MODBUS_STATS, IL_ModbusTCPClient, IL_ModbusTCPReadCoils, IL_ModbusTCPReadDiscreteInputs, IL_ModbusTCPReadHoldingRegisters, IL_ModbusTCPReadInputRegisters, IL_ModBusTCPWriteSingleCoil, IL_ModBusTCPWriteSingleRegister, IL_ModBusTCPWriteMultipleCoils, IL_ModbusTCPWriteMultipleRegisters, IL_ModBusTCPReadWriteMultipleRegisters, IL_ModbusTCPReadDeviceIdentification

## 18 CXA_MotionCore_fbs  →  `18_CXA_MotionCore_fbs.md` (7 KB, p. 439–444)

Reading axis configuration, Writing an axis configuration

## 19 CXA_MotionInterface  →  `19_CXA_MotionInterface.md` (270 KB, p. 444–557)

MotionInterface - Initial configuration, MB_AxisInit, MB_AxisInterfaceBase, Operation mode “Drive ready”, Operation mode “Drive Halt”, Operation mode "Setup", Operation mode “Absolute positioning”, “Relative positioning” operation mode, Operation modes “Additive positioning”, Operation mode “Robot Control”, Operation mode “Gantry”, Operation mode “Interrupt", Operation mode “Continue”, Operation mode "AxsHoming", Operation mode "MoveVelocity", Operation mode "ModeStop", Operation mode "ModeFixedStop", Operation mode "ModeCyclicSetPoint", "ModeSyncPos" operation mode, "ModeSyncVel" operation mode, "ModeFlexProfile" operation mode, "ModeCamIn" operation mode, Operation mode “External function block”, "ModeTorque" operation mode, Functions for multiple operation modes, User-defined operation modes, AxisInterface - Global variables, Programming template "AxisInterface", TE_AxisInterfaceMainProg, TE_AxisInitAllAxes, TE_AxisInterface, TE_GetAxisInterfaceIndex, System overview - Visualization, Extending the arAxisCtrl_gb[ ] structure, Extending the arAxisStatus_gb[ ] structure, Extending the function block, Using the user-defined operation mode, Accessing axis data, Adjusting the maximum number of axes, Adjusting the assignment AxisName <>AxisIndex, Adding an axis, Removing/renaming an axis, AxisInterface - Extensions, MB_KinematicsInit, MB_KinematicsInterfaceBase, Operation modes “Kinematic ready”, Operation mode “Kinematic halt", Operation mode "Setup", Operation mode “Absolute linear positioning”, Operation mode “Relative linear positioning”, Operation mode “Absolute direct positioning”, Operation mode “Relative direct positioning”, "Asynchronous direct positioning” operation mode, MB_KIN_END_POINT (STRUCT), ML_KinCmdPosePair (STRUCT), MB_KIN_CIRCLE_PARAM (STRUCT), ML_KinCmdCircleDataPair (STRUCT), Operation mode "2D Circular moving in counterclockwise", Operation mode “Standby", Operation mode “Interrupt”, Operation mode “Continue”, Operation mode "SlopeType", "Half jump up" operation mode, "Half jump down" operation mode, Operation mode "AccelerationOverride", Operation mode "ModeCoordStopping", Operation mode “External function block”, BeltSync, VelocityOverride, PCS, PCSTool, Blending, ActivePlane, ActivatePathSmooth, KinematicInterface - Global variables, Programming template "KinematicInterface and AxisInterface", TE_KinInterfaceMainProg, TE_KinematicsInitAllKinematics, TE_KinematicsInterface, System overview - Visualization, Extending the arKinCtrl_gb[ ] structure, Extending the arKinStatus_gb[ ] structure, Extending the function block, Accessing kinematic data, Adjusting the maximum number of kinematics, Adjusting the assignment KinematicName <>KinematicIndex, Adding a kinematics, Removing/renaming kinematics, KinematicInterface - Extensions

## 20 CXA_MotionPrinting  →  `20_CXA_MotionPrinting.md` (76 KB, p. 557–594)

MB_CAMTABLE, MB_CAMPROF, MB_PilgrimStepCalcType01, MB_FlexLockPrepareType01, MB_FlexLockType01, MB_PositionMonitoring_GantryCant, MB_TensionControlLoadCellType01, MB_TENSION_CONTROL_MATERIAL (STRUCT), MB_TENSION_CONTROL_MATERIAL_TYPE (ENUM), MB_TENSION_CONTROL_MODE (ENUM), MB_FLEXLOCK_PARAMETER, MB_FLEXLOCK_PROFILETYPE, MB_POS_MON_GANTRY_CANT

## 21 CXA_LoopControl  →  `21_CXA_LoopControl.md` (338 KB, p. 594–743)

Time-discrete function blocks, Event-controlled function blocks, IL_PIDType01, IL_PIDType02, IL_PIDType03, IL_PIDType04, IL_PIType01, IL_PIType02, IL_DeadtimeType01, IL_DeadtimeType02, IL_DeviationResponseCurve, IL_DT1Type01, IL_DT1Type02, IL_PDT1Type01, IL_PDT1Type02, IL_PT1Type01, IL_PT1Type02, IL_TransportDelayType01, IL_TransportDelayType02, IL_ValueLimit, IL_ValueWindow, IL_FIRType01, IL_FIRType02, IL_IIRType01, IL_IIRType02, IL_StateVariableType01, IL_StateVariableType02, IL_FILTER_TYPE, IL_FIR_COEFF, IL_IIR_COEFF, IL_NoiseGeneratorType01, IL_NoiseGeneratorType02, IL_PRBSGeneratorType01, IL_PRBSGeneratorType02, IL_AngleGeneratorType01, IL_AngleGeneratorType02, IL_PhaseController, IL_SignalGeneratorType01, IL_SignalGeneratorType02, IL_AmplitudeControllerType01, IL_AmplitudeControllerType02, IL_CURVETYPE, IL_CENTERLINE_CONTROL, IL_AMP_CONTROL, IL_HistogramType01, IL_HistogramType02, IL_StatisticType01, IL_StatisticType02, IL_SuppressionType01, IL_SuppressionType02, IL_SuppressionType03, IL_SuppressionType04, IL_TempControl, IL_TEMPCONTROL_CONTROL_TYPE, IL_TEMPCONTROL_CONTROL_MODE, IL_TEMPCONTROL_EXTENDED_SETTINGS, IL_TEMPCONTROL_MODEL_PARAM, IL_TEMPCONTROL_CONTR_PARAM, IL_TEMPCONTROL_LIMITS, IL_TwoPosCtrlType01, IL_SUPPRESSION_LIMITS, IL_SUPPRESSION_MODE, IL_COORD_TYPE01

## 22 CXA_OpcUaClient  →  `22_CXA_OpcUaClient.md` (1 KB, p. 743–744)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 23 CXA_OpcUaClient_fbs  →  `23_CXA_OpcUaClient_fbs.md` (1 KB, p. 744–744)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 24 CXA_OpcUaCommon  →  `24_CXA_OpcUaCommon.md` (1 KB, p. 744–744)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 25 CXA_OpcUaExt  →  `25_CXA_OpcUaExt.md` (1 KB, p. 744–744)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 26 CXA_OpcUaServer  →  `26_CXA_OpcUaServer.md` (1 KB, p. 744–744)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 27 CXA_OpcUaServer_fbs  →  `27_CXA_OpcUaServer_fbs.md` (1 KB, p. 744–745)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 28 CXA_PLCopen  →  `28_CXA_PLCopen.md` (388 KB, p. 745–913)

Malfunction, MB_AxsContinue, MB_AxsInterrupt, MB_AxsWaitPrepare, MB_CtrlBasedGantryHoming, MB_CyclicSetPoint, MB_FixStop, MB_ResetFixStop, MC_Home, MC_Inch, MC_Jog, MC_MoveAbsolute, MC_MoveAdditive, MC_MoveRelative, MC_MoveVelocity, MC_Power, MC_Reset, MC_SetOverride, MC_Halt, MC_Stop, MB_TorqueControl, MB_AxsGetBeltValueRT, MC_ReadStatus, MC_ReadActualPosition, MC_ReadActualVelocity, MC_ReadActualTorque, MB_AxsGetIpoValues, MC_ReadStatus_RT, MC_ReadAxisInfo_RT, PoseAttributes (ARRAY), EnableTargetPose (BOOL), MB_KinMoveHalfJump, MB_KinBeltSyncP, MC_AddAxisToGroup, MC_RemoveAxisFromGroup, MC_GroupEnable, MC_GroupDisable, MC_GroupReset, MC_MoveLinearAbsolute, MC_MoveLinearRelative, MC_GroupStop, MC_GroupSetOverride, MC_GroupReadStatus, MC_GroupReadActualPosition, MC_GroupReadActualVelocity, MC_GroupReadActualAcceleration, MB_KinInterrupt, MC_MoveDirectAbsolute, MC_MoveDirectRelative, MB_MoveCircle2D, MB_ActiveKinMCSP, MB_DeactiveKinMCSP, MB_PCSTeachIn, MB_InitTouchProbe, MB_TouchProbeContinuousType01, MB_UpdateTouchProbeParameter, MC_AbortTrigger, MC_TouchProbe, MB_AxsProbeEx, MB_GetSignal, MB_ResetSignal, MB_ResetSignalCmd, MB_SetSignal, MB_SetSignalCmd, MB_SetSignalCmdOpt, MB_WaitForSignalCmd, MB_CamIn, MB_WriteSyncOffsetRT, MB_FlexProfile, MB_GearInPos, MB_GearInVel, MB_DigitalCamSwitch, Data types of the MB_DigitalCamSwitch, MC_BUFFER_MODE (ENUM), ML_DynSyncDirection (ENUM), ML_SyncMode (ENUM), ML_SyncSource (ENUM), MB_GROUP_POSEPAIR_OPTION (STRUCT), MC_MEANING_ATTRIBUTE (ENUM), MB_GROUP_BELTSYNC_STATE (ENUM), MB_GROUP_CIRCLE_PARAM (STRUCT), MB_GROUP_END_POINT (STRUCT), MB_TRANSITION_MODE (ENUM), MC_COORD_SYSTEM (ENUM), MB_SYNC_DYNVALUES (STRUCT), MB_SYNC_FlexProfile (STRUCT), MB_SYNC_OFFSET (STRUCT), MB_SYNC_PROCESS_CTRL (STRUCT), MB_SYNC_PROCESS_OFFSET (STRUCT), MB_SYNC_CamIn (STRUCT), MB_KIN_CIRCLE_PARAM, MB_KIN_END_POINT, ML_KinCmdCircleDataPair, ML_KinCmdPosePair, MB_SYNC_OFFSET_STATE (STRUCT), MB_SYNC_VEL_OFFSET_STATE (STRUCT), CXA_PLCopen - Error codes

## 29 CXA_Python  →  `29_CXA_Python.md` (22 KB, p. 913–924)

IL_ScriptInstance, IL_StartScript, IL_StartScriptFile, IL_CreateScriptInstance, IL_DeleteScriptInstance, IL_AbortScript, IL_ResetInstance, IL_ReadInstanceDiagnostics, IL_ReadInstanceState, IL_ScriptInstanceStatus, INSTANCE_STATE, INSTANCE_RESET_CMD_STATE, INSTANCE_ABORT_CMD_STATE

## 30 CXA_RegisterControl  →  `30_CXA_RegisterControl.md` (67 KB, p. 924–952)

MB_CORRECTION_DATA (STRUCT), MB_CORRECTION_MODE (ENUM), MB_CORRECTION_TYPE (ENUM), MB_PICONTROL_DATA (STRUCT), MB_RegiSetpointLockType01, MB_RegiMeasuringType01, MB_RegiMeasuringType02, MB_RegiRegulateType01, MB_RegiRegulateType02, MB_RegisterControllerType01, MB_RegisterControllerSideType01

## 31 CXA_S20  →  `31_CXA_S20.md` (25 KB, p. 952–965)

IH_S20ComConfiguration, IH_S20ComInterfaceType02, IH_S20AI4IUType02, IH_S20RSComType02

## 32 CXA_S20_DALI  →  `32_CXA_S20_DALI.md` (140 KB, p. 965–1029)

IH_DaliDim, IH_DaliAddress, IH_DaliCallScene, IH_DaliRemoveFromGroup, IH_DaliDirectPower, IH_DaliRemoveFromScene, IH_DaliQueryStatus, IH_S20DaliReadWrite, IH_DaliQueryActualLevel, IH_DaliAddToGroup, IH_DaliAddToScene, IH_DaliOff, IH_DaliOn, IH_DaliSearchAddress, IH_DaliQuerySceneLevel, IH_DaliProgramShortAddress, IH_DaliStoreParameter, IH_DaliReset, IH_DaliQueryDTR, IH_DaliQueryParameter, IH_DaliQueryGroup, IH_DaliQueryRandomAddress, IH_INLN_DALI_TOKEN, IH_INLN_DALI_ADDRTYPE, IH_INLN_DALI_DIMMODE, IH_INLN_DALI_LIGHTLEVEL, IH_INLN_DALI_OPMODE, IH_INLN_DALI_PARAMETER, Troubleshooting

## 33 CXA_S20_KNX  →  `33_CXA_S20_KNX.md` (27 KB, p. 1029–1045)

Application example

## 34 CXA_ScriptInterpreter  →  `34_CXA_ScriptInterpreter.md` (24 KB, p. 1045–1056)

IL_ScriptInstance, IL_StartScript, IL_StartScriptFile, IL_CreateScriptInstance, IL_DeleteScriptInstance, IL_AbortScript, IL_ResetInstance, IL_ReadInstanceDiagnostics, IL_ReadInstanceState, IL_ScriptInstanceStatus, INSTANCE_STATE, INSTANCE_RESET_CMD_STATE, INSTANCE_ABORT_CMD_STATE

## 35 CXA_SocketComm  →  `35_CXA_SocketComm.md` (187 KB, p. 1056–1133)

IL_TCPConnectionAsync, IL_TCPSendAsync, IL_TCPRecvAsync, IL_TCPRecvPacketAsync, IL_TCPInitial, IL_TCPSend, IL_TCPRecv, IL_TCPRecvPacket, IL_TCPClose, IL_UDPSocketAsync, IL_UDPSendtoAsync, IL_UDPRecvfromAsync, IL_UDPInitial, IL_UDPSendto, IL_UDPRecvfrom, IL_UDPClose, IL_PingAsync, IL_Ping, IL_FTPGetAsync, IL_FTPPutAsync, IL_FTPGetFileAsync, IL_FTPPutFileAsync, IL_TFTPGetFileAsync, IL_TFTPPutFileAsync, IL_TCPCyclic, IL_UDPCyclic, IL_CONN_MODE, IL_CONN_STATUS, ETHERNET_TABLE, General, ETHERNET_TABLE, General, 16#00000001-16#00000212, ETHERNET_TABLE, IL_TcpCyclic, IL_UdpCyclic, 16#00001001-16#00001002, ETHERNET_TABLE, IL_FTPGetAsync, IL_FTPPutAsync, IL_FTPGetFileAsync, IL_FTP_PutFileAsync, 16#00002001-16#00002004, ETHERNET_TABLE, IL_TFTPGetFileAsync, IL_TFTPPutFileAsync, 16#00002101-16#00002108, CXA_SocketComm - Error codes of the CXA_Table

## 36 CXA_Utilities  →  `36_CXA_Utilities.md` (267 KB, p. 1133–1272)

IL_ContinuousAdjustType01, IL_ContinuousAdjustType02, IL_IncrementalAdjustType01, IL_EnableDoneBase, IL_EnableInOpBase, IL_EnableInOpShutdownBase, IL_ExecuteDoneBase, IL_ExecuteInOpBase, IL_ExecuteDoneAbortedBase, IL_ExecuteDoneAbortedShutdownBase, IL_FB_STATES, IL_BoolToByte, IL_BoolToDWord, IL_BoolToWord, IL_ByteToDWord, IL_ConcatByte, IL_ConcatWord, IL_ByteToBool, IL_DWordToBool, IL_DWordToByte, IL_HighByte, IL_LowByte, IL_HighWord, IL_LowWord, IL_WordToBool, IL_SwapDWord, IL_SwapWord, IL_CRC16, IL_AsciiToByte, IL_ByteToAscii, IL_RealToString, IL_LRealToString, IL_HighResTimeDiff, IL_HighResTimeTick, IL_Toggle, IL_InterpolationLinear, IL_MaxValue, IL_COORD_PAIR_TYPE01, IL_StrLower, IL_StrUpper, IL_StrCompare, IL_StrCompareNoCase, IL_StrNCompare, IL_StrNCompareNoCase, IL_AsciiStreamToBase64, IL_Base64ToAsciiStream, IL_BufferToString, IL_StringToBuffer, IL_StrCopy, IL_StrNCopy, IL_CONCAT, IL_DELETE, IL_FIND, IL_INSERT, IL_LEFT, IL_LEN, IL_MID, IL_REPLACE, IL_RIGHT, IL_Ascii_To_Char, IL_Char_To_Ascii, IL_Int_To_Str, ENUM_INT_OPTION, IL_Real_To_Str, ENUM_REAL_OPTION, IL_String_To_Unicode, ENUM_OPT_UTF, IL_Unicode_To_String, IL_BufferGetElementCount, IL_Code, IL_StrInverse, IL_StrSetEndOfString, IL_StrGetElement, IL_StrLChr, IL_StrRChr, IL_StrSetElement, IL_StrSplit, IL_StrTrimAll, IL_StrTrimSpace, ENUM_TRIM_OPT, IL_Date, IL_DateAndTime, IL_TimeOfDay, IL_ExtSysTimeDate, IL_LocalTime, IL_SysTime64, IL_SysTimeDateToSysTime64, IL_SysTimeDate, IL_SysTime64ToSysTimeDate, IL_TIMEZONE, IL_LinkedList, IL_LINKED_LIST_MAINTENANCE, IL_LINKED_LIST_MODE, IL_DegToRad, IL_RadToDeg, IL_GetModuloType01, IL_GetModuloType02, IL_GetModuloType03, IL_GetModuloType04, IL_DegToRad, IL_RadToDeg

## 37 CXA_Winder  →  `37_CXA_Winder.md` (107 KB, p. 1272–1314)

MB_PIDCONTROL_DATA (STRUCT), MB_WIND_CTRL_TYPE (ENUM), MB_WIND_DANCER_LIMITS (STRUCT), MB_WIND_DIAM_CALC_MODE (ENUM), MB_WIND_DIAMETER (STRUCT), MB_WIND_DIRECTION (ENUM), MB_WIND_FRICTION (STRUCT), MB_WIND_TENS_DIAG (STRUCT), MB_WIND_TENSION (STRUCT), MB_WIND_TENSION_MODE (ENUM), MB_WIND_TOURQUE_LIMITS (STRUCT), MB_WinderSpeedAdapter, MB_CalculateInertiaLimit, MB_DiameterMeasurement, MB_DiameterCalculator, MB_DancerControl, MB_WinderDancerCtrlType01, MB_WinderTensionCtrlType01, MB_WinderTensionCtrlType02

## 38 CXA_TechBase  →  `38_CXA_TechBase.md` (24 KB, p. 1314–1325)

MB_PROFILE_NAME (STRUCT), MB_CAMIN_PROFILE_STATE (STRUCT), MB_WriteFlexProfile, MB_WriteFlexProfileType02, MB_ReadFlexProfile, MB_GetPointTableNames, MB_IsPointTableExists, MB_DeletePointTable, MB_WritePointTable, MB_WritePointTableType02, MB_AxsValidateCamIn, MB_ReadValidateCamIn, MB_ReadCamInStateInfo

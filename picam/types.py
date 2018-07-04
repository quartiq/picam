# -*- coding: utf-8 -*-
#
# TARGET arch is: []
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import os
import ctypes

"""PICam library types.

This module defines the PICam library function signatures, enums
and structures offered and used by the PICam API.

They are all extensively documented in the PICam documentation available in the
SDK package (ftp.princetoninstruments.com/Public/Software/Official/PICam)

This file (apart from this docstring) was generated using ctypeslib2
(https://github.com/trolldbois/ctypeslib) with: ::

    clang2py.py -l libpicam.so.0 Picam_SDK/pi/includes/pi* > picam/types.py
"""


# if local wordsize is same as target, keep ctypes pointer function.
if ctypes.sizeof(ctypes.c_void_p) == 8:
    POINTER_T = ctypes.POINTER
else:
    # required to access _ctypes
    import _ctypes
    # Emulate a pointer class using the approriate c_int32/c_int64 type
    # The new class should have :
    # ['__module__', 'from_param', '_type_', '__dict__', '__weakref__', '__doc__']
    # but the class should be submitted to a unique instance for each base type
    # to that if A == B, POINTER_T(A) == POINTER_T(B)
    ctypes._pointer_t_type_cache = {}
    def POINTER_T(pointee):
        # a pointer should have the same length as LONG
        fake_ptr_base_type = ctypes.c_uint64 
        # specific case for c_void_p
        if pointee is None: # VOID pointer type. c_void_p.
            pointee = type(None) # ctypes.c_void_p # ctypes.c_ulong
            clsname = 'c_void'
        else:
            clsname = pointee.__name__
        if clsname in ctypes._pointer_t_type_cache:
            return ctypes._pointer_t_type_cache[clsname]
        # make template
        class _T(_ctypes._SimpleCData,):
            _type_ = 'L'
            _subtype_ = pointee
            def _sub_addr_(self):
                return self.value
            def __repr__(self):
                return '%s(%d)'%(clsname, self.value)
            def contents(self):
                raise TypeError('This is not a ctypes pointer.')
            def __init__(self, **args):
                raise TypeError('This is not a ctypes pointer. It is not instanciable.')
        _class = type('LP_%d_%s'%(8, clsname), (_T,),{}) 
        ctypes._pointer_t_type_cache[clsname] = _class
        return _class

_libraries = {}
if os.name == "nt":
    libpicam_name = "picam.dll"
else:
    libpicam_name = "libpicam.so.0"
_libraries['libpicam.so.0'] = ctypes.CDLL(libpicam_name)
c_int128 = ctypes.c_ubyte*16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 16:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte*16




# values for enumeration 'PicamError'
PicamError_None = 0
PicamError_UnexpectedError = 4
PicamError_UnexpectedNullPointer = 3
PicamError_InvalidPointer = 35
PicamError_InvalidCount = 39
PicamError_InvalidOperation = 42
PicamError_OperationCanceled = 43
PicamError_LibraryNotInitialized = 1
PicamError_LibraryAlreadyInitialized = 5
PicamError_InvalidEnumeratedType = 16
PicamError_EnumerationValueNotDefined = 17
PicamError_NotDiscoveringCameras = 18
PicamError_AlreadyDiscoveringCameras = 19
PicamError_NotDiscoveringAccessories = 48
PicamError_AlreadyDiscoveringAccessories = 49
PicamError_NoCamerasAvailable = 34
PicamError_CameraAlreadyOpened = 7
PicamError_InvalidCameraID = 8
PicamError_NoAccessoriesAvailable = 45
PicamError_AccessoryAlreadyOpened = 46
PicamError_InvalidAccessoryID = 47
PicamError_InvalidHandle = 9
PicamError_DeviceCommunicationFailed = 15
PicamError_DeviceDisconnected = 23
PicamError_DeviceOpenElsewhere = 24
PicamError_InvalidDemoModel = 6
PicamError_InvalidDemoSerialNumber = 21
PicamError_DemoAlreadyConnected = 22
PicamError_DemoNotSupported = 40
PicamError_ParameterHasInvalidValueType = 11
PicamError_ParameterHasInvalidConstraintType = 13
PicamError_ParameterDoesNotExist = 12
PicamError_ParameterValueIsReadOnly = 10
PicamError_InvalidParameterValue = 2
PicamError_InvalidConstraintCategory = 38
PicamError_ParameterValueIsIrrelevant = 14
PicamError_ParameterIsNotOnlineable = 25
PicamError_ParameterIsNotReadable = 26
PicamError_ParameterIsNotWaitableStatus = 50
PicamError_InvalidWaitableStatusParameterTimeOut = 51
PicamError_InvalidParameterValues = 28
PicamError_ParametersNotCommitted = 29
PicamError_InvalidAcquisitionBuffer = 30
PicamError_InvalidReadoutCount = 36
PicamError_InvalidReadoutTimeOut = 37
PicamError_InsufficientMemory = 31
PicamError_AcquisitionInProgress = 20
PicamError_AcquisitionNotInProgress = 27
PicamError_TimeOutOccurred = 32
PicamError_AcquisitionUpdatedHandlerRegistered = 33
PicamError_InvalidAcquisitionState = 44
PicamError_NondestructiveReadoutEnabled = 41
PicamError_ShutterOverheated = 52
PicamError_CenterWavelengthFaulted = 54
PicamError_CameraFaulted = 53
PicamError = ctypes.c_int # enum
Picam_GetVersion = _libraries['libpicam.so.0'].Picam_GetVersion
Picam_GetVersion.restype = PicamError
Picam_GetVersion.argtypes = [POINTER_T(ctypes.c_int32), POINTER_T(ctypes.c_int32), POINTER_T(ctypes.c_int32), POINTER_T(ctypes.c_int32)]
Picam_IsLibraryInitialized = _libraries['libpicam.so.0'].Picam_IsLibraryInitialized
Picam_IsLibraryInitialized.restype = PicamError
Picam_IsLibraryInitialized.argtypes = [POINTER_T(ctypes.c_int32)]
Picam_InitializeLibrary = _libraries['libpicam.so.0'].Picam_InitializeLibrary
Picam_InitializeLibrary.restype = PicamError
Picam_InitializeLibrary.argtypes = []
Picam_UninitializeLibrary = _libraries['libpicam.so.0'].Picam_UninitializeLibrary
Picam_UninitializeLibrary.restype = PicamError
Picam_UninitializeLibrary.argtypes = []
Picam_DestroyString = _libraries['libpicam.so.0'].Picam_DestroyString
Picam_DestroyString.restype = PicamError
Picam_DestroyString.argtypes = [POINTER_T(ctypes.c_char)]

# values for enumeration 'PicamEnumeratedType'
PicamEnumeratedType_Error = 1
PicamEnumeratedType_EnumeratedType = 29
PicamEnumeratedType_Model = 2
PicamEnumeratedType_ComputerInterface = 3
PicamEnumeratedType_DiscoveryAction = 26
PicamEnumeratedType_HandleType = 27
PicamEnumeratedType_ValueType = 4
PicamEnumeratedType_ConstraintType = 5
PicamEnumeratedType_Parameter = 6
PicamEnumeratedType_ActiveShutter = 53
PicamEnumeratedType_AdcAnalogGain = 7
PicamEnumeratedType_AdcQuality = 8
PicamEnumeratedType_CcdCharacteristicsMask = 9
PicamEnumeratedType_CenterWavelengthStatus = 51
PicamEnumeratedType_CoolingFanStatus = 56
PicamEnumeratedType_EMIccdGainControlMode = 42
PicamEnumeratedType_GateTrackingMask = 36
PicamEnumeratedType_GatingMode = 34
PicamEnumeratedType_GatingSpeed = 38
PicamEnumeratedType_GratingCoating = 48
PicamEnumeratedType_GratingType = 49
PicamEnumeratedType_IntensifierOptionsMask = 35
PicamEnumeratedType_IntensifierStatus = 33
PicamEnumeratedType_LaserOutputMode = 45
PicamEnumeratedType_LaserStatus = 54
PicamEnumeratedType_LightSource = 46
PicamEnumeratedType_LightSourceStatus = 47
PicamEnumeratedType_ModulationTrackingMask = 41
PicamEnumeratedType_OrientationMask = 10
PicamEnumeratedType_OutputSignal = 11
PicamEnumeratedType_PhosphorType = 39
PicamEnumeratedType_PhotocathodeSensitivity = 40
PicamEnumeratedType_PhotonDetectionMode = 43
PicamEnumeratedType_PixelFormat = 12
PicamEnumeratedType_ReadoutControlMode = 13
PicamEnumeratedType_SensorTemperatureStatus = 14
PicamEnumeratedType_SensorType = 15
PicamEnumeratedType_ShutterStatus = 52
PicamEnumeratedType_ShutterTimingMode = 16
PicamEnumeratedType_ShutterType = 50
PicamEnumeratedType_TimeStampsMask = 17
PicamEnumeratedType_TriggerCoupling = 30
PicamEnumeratedType_TriggerDetermination = 18
PicamEnumeratedType_TriggerResponse = 19
PicamEnumeratedType_TriggerSource = 31
PicamEnumeratedType_TriggerStatus = 55
PicamEnumeratedType_TriggerTermination = 32
PicamEnumeratedType_VacuumStatus = 57
PicamEnumeratedType_ValueAccess = 20
PicamEnumeratedType_DynamicsMask = 28
PicamEnumeratedType_ConstraintScope = 21
PicamEnumeratedType_ConstraintSeverity = 22
PicamEnumeratedType_ConstraintCategory = 23
PicamEnumeratedType_RoisConstraintRulesMask = 24
PicamEnumeratedType_AcquisitionErrorsMask = 25
PicamEnumeratedType_AcquisitionState = 37
PicamEnumeratedType_AcquisitionStateErrorsMask = 44
PicamEnumeratedType = ctypes.c_int # enum
piint = ctypes.c_int32
Picam_GetEnumerationString = _libraries['libpicam.so.0'].Picam_GetEnumerationString
Picam_GetEnumerationString.restype = PicamError
Picam_GetEnumerationString.argtypes = [PicamEnumeratedType, piint, POINTER_T(POINTER_T(ctypes.c_char))]

# values for enumeration 'PicamModel'
PicamModel_PIMteSeries = 1400
PicamModel_PIMte1024Series = 1401
PicamModel_PIMte1024F = 1402
PicamModel_PIMte1024B = 1403
PicamModel_PIMte1024BR = 1405
PicamModel_PIMte1024BUV = 1404
PicamModel_PIMte1024FTSeries = 1406
PicamModel_PIMte1024FT = 1407
PicamModel_PIMte1024BFT = 1408
PicamModel_PIMte1300Series = 1412
PicamModel_PIMte1300B = 1413
PicamModel_PIMte1300R = 1414
PicamModel_PIMte1300BR = 1415
PicamModel_PIMte2048Series = 1416
PicamModel_PIMte2048B = 1417
PicamModel_PIMte2048BR = 1418
PicamModel_PIMte2KSeries = 1409
PicamModel_PIMte2KB = 1410
PicamModel_PIMte2KBUV = 1411
PicamModel_PixisSeries = 0
PicamModel_Pixis100Series = 1
PicamModel_Pixis100F = 2
PicamModel_Pixis100B = 6
PicamModel_Pixis100R = 3
PicamModel_Pixis100C = 4
PicamModel_Pixis100BR = 5
PicamModel_Pixis100BExcelon = 54
PicamModel_Pixis100BRExcelon = 55
PicamModel_PixisXO100B = 7
PicamModel_PixisXO100BR = 8
PicamModel_PixisXB100B = 68
PicamModel_PixisXB100BR = 69
PicamModel_Pixis256Series = 26
PicamModel_Pixis256F = 27
PicamModel_Pixis256B = 29
PicamModel_Pixis256E = 28
PicamModel_Pixis256BR = 30
PicamModel_PixisXB256BR = 31
PicamModel_Pixis400Series = 37
PicamModel_Pixis400F = 38
PicamModel_Pixis400B = 40
PicamModel_Pixis400R = 39
PicamModel_Pixis400BR = 41
PicamModel_Pixis400BExcelon = 56
PicamModel_Pixis400BRExcelon = 57
PicamModel_PixisXO400B = 42
PicamModel_PixisXB400BR = 70
PicamModel_Pixis512Series = 43
PicamModel_Pixis512F = 44
PicamModel_Pixis512B = 45
PicamModel_Pixis512BUV = 46
PicamModel_Pixis512BExcelon = 58
PicamModel_PixisXO512F = 49
PicamModel_PixisXO512B = 50
PicamModel_PixisXF512F = 48
PicamModel_PixisXF512B = 47
PicamModel_Pixis1024Series = 9
PicamModel_Pixis1024F = 10
PicamModel_Pixis1024B = 11
PicamModel_Pixis1024BR = 13
PicamModel_Pixis1024BUV = 12
PicamModel_Pixis1024BExcelon = 59
PicamModel_Pixis1024BRExcelon = 60
PicamModel_PixisXO1024F = 16
PicamModel_PixisXO1024B = 14
PicamModel_PixisXO1024BR = 15
PicamModel_PixisXF1024F = 17
PicamModel_PixisXF1024B = 18
PicamModel_PixisXB1024BR = 71
PicamModel_Pixis1300Series = 51
PicamModel_Pixis1300F = 52
PicamModel_Pixis1300F_2 = 75
PicamModel_Pixis1300B = 53
PicamModel_Pixis1300BR = 73
PicamModel_Pixis1300BExcelon = 61
PicamModel_Pixis1300BRExcelon = 62
PicamModel_PixisXO1300B = 65
PicamModel_PixisXF1300B = 66
PicamModel_PixisXB1300R = 72
PicamModel_Pixis2048Series = 20
PicamModel_Pixis2048F = 21
PicamModel_Pixis2048B = 22
PicamModel_Pixis2048BR = 67
PicamModel_Pixis2048BExcelon = 63
PicamModel_Pixis2048BRExcelon = 74
PicamModel_PixisXO2048B = 23
PicamModel_PixisXF2048F = 25
PicamModel_PixisXF2048B = 24
PicamModel_Pixis2KSeries = 32
PicamModel_Pixis2KF = 33
PicamModel_Pixis2KB = 34
PicamModel_Pixis2KBUV = 36
PicamModel_Pixis2KBExcelon = 64
PicamModel_PixisXO2KB = 35
PicamModel_QuadroSeries = 100
PicamModel_Quadro4096 = 101
PicamModel_Quadro4096_2 = 103
PicamModel_Quadro4320 = 102
PicamModel_ProEMSeries = 200
PicamModel_ProEM512Series = 203
PicamModel_ProEM512B = 201
PicamModel_ProEM512BK = 205
PicamModel_ProEM512BExcelon = 204
PicamModel_ProEM512BKExcelon = 206
PicamModel_ProEM1024Series = 207
PicamModel_ProEM1024B = 202
PicamModel_ProEM1024BExcelon = 208
PicamModel_ProEM1600Series = 209
PicamModel_ProEM1600xx2B = 212
PicamModel_ProEM1600xx2BExcelon = 210
PicamModel_ProEM1600xx4B = 213
PicamModel_ProEM1600xx4BExcelon = 211
PicamModel_ProEMPlusSeries = 600
PicamModel_ProEMPlus512Series = 603
PicamModel_ProEMPlus512B = 601
PicamModel_ProEMPlus512BK = 605
PicamModel_ProEMPlus512BExcelon = 604
PicamModel_ProEMPlus512BKExcelon = 606
PicamModel_ProEMPlus1024Series = 607
PicamModel_ProEMPlus1024B = 602
PicamModel_ProEMPlus1024BExcelon = 608
PicamModel_ProEMPlus1600Series = 609
PicamModel_ProEMPlus1600xx2B = 612
PicamModel_ProEMPlus1600xx2BExcelon = 610
PicamModel_ProEMPlus1600xx4B = 613
PicamModel_ProEMPlus1600xx4BExcelon = 611
PicamModel_ProEMHSSeries = 1200
PicamModel_ProEMHS512Series = 1201
PicamModel_ProEMHS512B = 1202
PicamModel_ProEMHS512BK = 1207
PicamModel_ProEMHS512BExcelon = 1203
PicamModel_ProEMHS512BKExcelon = 1208
PicamModel_ProEMHS512B_2 = 1216
PicamModel_ProEMHS512BExcelon_2 = 1217
PicamModel_ProEMHS1024Series = 1204
PicamModel_ProEMHS1024B = 1205
PicamModel_ProEMHS1024BExcelon = 1206
PicamModel_ProEMHS1024B_2 = 1212
PicamModel_ProEMHS1024BExcelon_2 = 1213
PicamModel_ProEMHS1024B_3 = 1214
PicamModel_ProEMHS1024BExcelon_3 = 1215
PicamModel_ProEMHS1K10Series = 1209
PicamModel_ProEMHS1KB10 = 1210
PicamModel_ProEMHS1KB10Excelon = 1211
PicamModel_PIMax3Series = 300
PicamModel_PIMax31024I = 301
PicamModel_PIMax31024x256 = 302
PicamModel_PIMax4Series = 700
PicamModel_PIMax41024ISeries = 703
PicamModel_PIMax41024I = 701
PicamModel_PIMax41024IRF = 704
PicamModel_PIMax41024FSeries = 710
PicamModel_PIMax41024F = 711
PicamModel_PIMax41024FRF = 712
PicamModel_PIMax41024x256Series = 705
PicamModel_PIMax41024x256 = 702
PicamModel_PIMax41024x256RF = 706
PicamModel_PIMax42048Series = 716
PicamModel_PIMax42048F = 717
PicamModel_PIMax42048B = 718
PicamModel_PIMax42048FRF = 719
PicamModel_PIMax42048BRF = 720
PicamModel_PIMax4512EMSeries = 708
PicamModel_PIMax4512EM = 707
PicamModel_PIMax4512BEM = 709
PicamModel_PIMax41024EMSeries = 713
PicamModel_PIMax41024EM = 715
PicamModel_PIMax41024BEM = 714
PicamModel_PylonSeries = 400
PicamModel_Pylon100Series = 418
PicamModel_Pylon100F = 404
PicamModel_Pylon100B = 401
PicamModel_Pylon100BR = 407
PicamModel_Pylon100BExcelon = 425
PicamModel_Pylon100BRExcelon = 426
PicamModel_Pylon256Series = 419
PicamModel_Pylon256F = 409
PicamModel_Pylon256B = 410
PicamModel_Pylon256E = 411
PicamModel_Pylon256BR = 412
PicamModel_Pylon400Series = 420
PicamModel_Pylon400F = 405
PicamModel_Pylon400B = 402
PicamModel_Pylon400BR = 408
PicamModel_Pylon400BExcelon = 427
PicamModel_Pylon400BRExcelon = 428
PicamModel_Pylon1024Series = 421
PicamModel_Pylon1024B = 417
PicamModel_Pylon1024BExcelon = 429
PicamModel_Pylon1300Series = 422
PicamModel_Pylon1300F = 406
PicamModel_Pylon1300B = 403
PicamModel_Pylon1300R = 438
PicamModel_Pylon1300BR = 432
PicamModel_Pylon1300BExcelon = 430
PicamModel_Pylon1300BRExcelon = 433
PicamModel_Pylon2048Series = 423
PicamModel_Pylon2048F = 415
PicamModel_Pylon2048B = 434
PicamModel_Pylon2048BR = 416
PicamModel_Pylon2048BExcelon = 435
PicamModel_Pylon2048BRExcelon = 436
PicamModel_Pylon2KSeries = 424
PicamModel_Pylon2KF = 413
PicamModel_Pylon2KB = 414
PicamModel_Pylon2KBUV = 437
PicamModel_Pylon2KBExcelon = 431
PicamModel_PylonirSeries = 900
PicamModel_Pylonir1024Series = 901
PicamModel_Pylonir102422 = 902
PicamModel_Pylonir102417 = 903
PicamModel_PionirSeries = 500
PicamModel_Pionir640 = 501
PicamModel_NirvanaSeries = 800
PicamModel_Nirvana640 = 801
PicamModel_NirvanaSTSeries = 1300
PicamModel_NirvanaST640 = 1301
PicamModel_NirvanaLNSeries = 1100
PicamModel_NirvanaLN640 = 1101
PicamModel_SophiaSeries = 1800
PicamModel_Sophia2048Series = 1801
PicamModel_Sophia2048B = 1802
PicamModel_Sophia2048BExcelon = 1803
PicamModel_SophiaXO2048B = 1804
PicamModel_SophiaXF2048B = 1805
PicamModel_SophiaXB2048B = 1806
PicamModel_Sophia2048135Series = 1807
PicamModel_Sophia2048135 = 1808
PicamModel_Sophia2048B135 = 1809
PicamModel_Sophia2048BR135 = 1810
PicamModel_Sophia2048B135Excelon = 1811
PicamModel_Sophia2048BR135Excelon = 1812
PicamModel_SophiaXO2048B135 = 1813
PicamModel_SophiaXO2048BR135 = 1814
PicamModel_BlazeSeries = 1500
PicamModel_Blaze100Series = 1507
PicamModel_Blaze100B = 1501
PicamModel_Blaze100BR = 1505
PicamModel_Blaze100HR = 1503
PicamModel_Blaze100BRLD = 1509
PicamModel_Blaze100BExcelon = 1511
PicamModel_Blaze100BRExcelon = 1513
PicamModel_Blaze100HRExcelon = 1515
PicamModel_Blaze100BRLDExcelon = 1517
PicamModel_Blaze400Series = 1508
PicamModel_Blaze400B = 1502
PicamModel_Blaze400BR = 1506
PicamModel_Blaze400HR = 1504
PicamModel_Blaze400BRLD = 1510
PicamModel_Blaze400BExcelon = 1512
PicamModel_Blaze400BRExcelon = 1514
PicamModel_Blaze400HRExcelon = 1516
PicamModel_Blaze400BRLDExcelon = 1518
PicamModel_FergieSeries = 1600
PicamModel_Fergie256Series = 1601
PicamModel_Fergie256B = 1602
PicamModel_Fergie256BR = 1607
PicamModel_Fergie256BExcelon = 1603
PicamModel_Fergie256BRExcelon = 1608
PicamModel_Fergie256FTSeries = 1604
PicamModel_Fergie256FFT = 1609
PicamModel_Fergie256BFT = 1605
PicamModel_Fergie256BRFT = 1610
PicamModel_Fergie256BFTExcelon = 1606
PicamModel_Fergie256BRFTExcelon = 1611
PicamModel_FergieAccessorySeries = 1700
PicamModel_FergieLampSeries = 1701
PicamModel_FergieAEL = 1702
PicamModel_FergieQTH = 1703
PicamModel_FergieLaserSeries = 1704
PicamModel_FergieLaser785 = 1705
PicamModel_KuroSeries = 1900
PicamModel_Kuro1200B = 1901
PicamModel_Kuro1608B = 1902
PicamModel_Kuro2048B = 1903
PicamModel = ctypes.c_int # enum

# values for enumeration 'PicamComputerInterface'
PicamComputerInterface_Usb2 = 1
PicamComputerInterface_1394A = 2
PicamComputerInterface_GigabitEthernet = 3
PicamComputerInterface_Usb3 = 4
PicamComputerInterface = ctypes.c_int # enum

# values for enumeration 'PicamStringSize'
PicamStringSize_SensorName = 64
PicamStringSize_SerialNumber = 64
PicamStringSize_FirmwareName = 64
PicamStringSize_FirmwareDetail = 256
PicamStringSize = ctypes.c_int # enum
class struct_PicamCameraID(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('model', PicamModel),
    ('computer_interface', PicamComputerInterface),
    ('sensor_name', ctypes.c_char * 64),
    ('serial_number', ctypes.c_char * 64),
     ]

PicamCameraID = struct_PicamCameraID
Picam_DestroyCameraIDs = _libraries['libpicam.so.0'].Picam_DestroyCameraIDs
Picam_DestroyCameraIDs.restype = PicamError
Picam_DestroyCameraIDs.argtypes = [POINTER_T(struct_PicamCameraID)]
Picam_GetAvailableCameraIDs = _libraries['libpicam.so.0'].Picam_GetAvailableCameraIDs
Picam_GetAvailableCameraIDs.restype = PicamError
Picam_GetAvailableCameraIDs.argtypes = [POINTER_T(POINTER_T(struct_PicamCameraID)), POINTER_T(ctypes.c_int32)]
Picam_GetUnavailableCameraIDs = _libraries['libpicam.so.0'].Picam_GetUnavailableCameraIDs
Picam_GetUnavailableCameraIDs.restype = PicamError
Picam_GetUnavailableCameraIDs.argtypes = [POINTER_T(POINTER_T(struct_PicamCameraID)), POINTER_T(ctypes.c_int32)]
Picam_IsCameraIDConnected = _libraries['libpicam.so.0'].Picam_IsCameraIDConnected
Picam_IsCameraIDConnected.restype = PicamError
Picam_IsCameraIDConnected.argtypes = [POINTER_T(struct_PicamCameraID), POINTER_T(ctypes.c_int32)]
Picam_IsCameraIDOpenElsewhere = _libraries['libpicam.so.0'].Picam_IsCameraIDOpenElsewhere
Picam_IsCameraIDOpenElsewhere.restype = PicamError
Picam_IsCameraIDOpenElsewhere.argtypes = [POINTER_T(struct_PicamCameraID), POINTER_T(ctypes.c_int32)]
PicamHandle = POINTER_T(None)
Picam_DestroyHandles = _libraries['libpicam.so.0'].Picam_DestroyHandles
Picam_DestroyHandles.restype = PicamError
Picam_DestroyHandles.argtypes = [POINTER_T(POINTER_T(None))]
Picam_OpenFirstCamera = _libraries['libpicam.so.0'].Picam_OpenFirstCamera
Picam_OpenFirstCamera.restype = PicamError
Picam_OpenFirstCamera.argtypes = [POINTER_T(POINTER_T(None))]
Picam_OpenCamera = _libraries['libpicam.so.0'].Picam_OpenCamera
Picam_OpenCamera.restype = PicamError
Picam_OpenCamera.argtypes = [POINTER_T(struct_PicamCameraID), POINTER_T(POINTER_T(None))]
Picam_CloseCamera = _libraries['libpicam.so.0'].Picam_CloseCamera
Picam_CloseCamera.restype = PicamError
Picam_CloseCamera.argtypes = [PicamHandle]
Picam_GetOpenCameras = _libraries['libpicam.so.0'].Picam_GetOpenCameras
Picam_GetOpenCameras.restype = PicamError
Picam_GetOpenCameras.argtypes = [POINTER_T(POINTER_T(POINTER_T(None))), POINTER_T(ctypes.c_int32)]
Picam_IsCameraConnected = _libraries['libpicam.so.0'].Picam_IsCameraConnected
Picam_IsCameraConnected.restype = PicamError
Picam_IsCameraConnected.argtypes = [PicamHandle, POINTER_T(ctypes.c_int32)]
Picam_IsCameraFaulted = _libraries['libpicam.so.0'].Picam_IsCameraFaulted
Picam_IsCameraFaulted.restype = PicamError
Picam_IsCameraFaulted.argtypes = [PicamHandle, POINTER_T(ctypes.c_int32)]
Picam_GetCameraID = _libraries['libpicam.so.0'].Picam_GetCameraID
Picam_GetCameraID.restype = PicamError
Picam_GetCameraID.argtypes = [PicamHandle, POINTER_T(struct_PicamCameraID)]
class struct_PicamFirmwareDetail(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('name', ctypes.c_char * 64),
    ('detail', ctypes.c_char * 256),
     ]

PicamFirmwareDetail = struct_PicamFirmwareDetail
Picam_DestroyFirmwareDetails = _libraries['libpicam.so.0'].Picam_DestroyFirmwareDetails
Picam_DestroyFirmwareDetails.restype = PicamError
Picam_DestroyFirmwareDetails.argtypes = [POINTER_T(struct_PicamFirmwareDetail)]
Picam_GetFirmwareDetails = _libraries['libpicam.so.0'].Picam_GetFirmwareDetails
Picam_GetFirmwareDetails.restype = PicamError
Picam_GetFirmwareDetails.argtypes = [POINTER_T(struct_PicamCameraID), POINTER_T(POINTER_T(struct_PicamFirmwareDetail)), POINTER_T(ctypes.c_int32)]
class struct_PicamCalibrationPoint(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('x', ctypes.c_double),
    ('y', ctypes.c_double),
     ]

PicamCalibrationPoint = struct_PicamCalibrationPoint
class struct_PicamCalibration(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('point_array', POINTER_T(struct_PicamCalibrationPoint)),
    ('point_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

PicamCalibration = struct_PicamCalibration
Picam_DestroyCalibrations = _libraries['libpicam.so.0'].Picam_DestroyCalibrations
Picam_DestroyCalibrations.restype = PicamError
Picam_DestroyCalibrations.argtypes = [POINTER_T(struct_PicamCalibration)]
Picam_DestroyModels = _libraries['libpicam.so.0'].Picam_DestroyModels
Picam_DestroyModels.restype = PicamError
Picam_DestroyModels.argtypes = [POINTER_T(PicamModel)]
Picam_GetAvailableDemoCameraModels = _libraries['libpicam.so.0'].Picam_GetAvailableDemoCameraModels
Picam_GetAvailableDemoCameraModels.restype = PicamError
Picam_GetAvailableDemoCameraModels.argtypes = [POINTER_T(POINTER_T(PicamModel)), POINTER_T(ctypes.c_int32)]
Picam_ConnectDemoCamera = _libraries['libpicam.so.0'].Picam_ConnectDemoCamera
Picam_ConnectDemoCamera.restype = PicamError
Picam_ConnectDemoCamera.argtypes = [PicamModel, POINTER_T(ctypes.c_char), POINTER_T(struct_PicamCameraID)]
Picam_DisconnectDemoCamera = _libraries['libpicam.so.0'].Picam_DisconnectDemoCamera
Picam_DisconnectDemoCamera.restype = PicamError
Picam_DisconnectDemoCamera.argtypes = [POINTER_T(struct_PicamCameraID)]
Picam_IsDemoCamera = _libraries['libpicam.so.0'].Picam_IsDemoCamera
Picam_IsDemoCamera.restype = PicamError
Picam_IsDemoCamera.argtypes = [POINTER_T(struct_PicamCameraID), POINTER_T(ctypes.c_int32)]

# values for enumeration 'PicamValueType'
PicamValueType_Integer = 1
PicamValueType_Boolean = 3
PicamValueType_Enumeration = 4
PicamValueType_LargeInteger = 6
PicamValueType_FloatingPoint = 2
PicamValueType_Rois = 5
PicamValueType_Pulse = 7
PicamValueType_Modulations = 8
PicamValueType = ctypes.c_int # enum

# values for enumeration 'PicamConstraintType'
PicamConstraintType_None = 1
PicamConstraintType_Range = 2
PicamConstraintType_Collection = 3
PicamConstraintType_Rois = 4
PicamConstraintType_Pulse = 5
PicamConstraintType_Modulations = 6
PicamConstraintType = ctypes.c_int # enum

# values for enumeration 'PicamParameter'
PicamParameter_ExposureTime = 33685527
PicamParameter_ShutterTimingMode = 50593816
PicamParameter_ShutterOpeningDelay = 33685550
PicamParameter_ShutterClosingDelay = 33685529
PicamParameter_ShutterDelayResolution = 50462767
PicamParameter_InternalShutterType = 17039499
PicamParameter_InternalShutterStatus = 17039513
PicamParameter_ExternalShutterType = 17039512
PicamParameter_ExternalShutterStatus = 17039514
PicamParameter_ActiveShutter = 50593947
PicamParameter_InactiveShutterTimingModeResult = 17039516
PicamParameter_GatingMode = 50593885
PicamParameter_RepetitiveGate = 84344926
PicamParameter_SequentialStartingGate = 84344927
PicamParameter_SequentialEndingGate = 84344928
PicamParameter_SequentialGateStepCount = 33947745
PicamParameter_SequentialGateStepIterations = 33947746
PicamParameter_DifStartingGate = 84344934
PicamParameter_DifEndingGate = 84344935
PicamParameter_EnableIntensifier = 50528342
PicamParameter_IntensifierStatus = 17039447
PicamParameter_IntensifierGain = 33620056
PicamParameter_EMIccdGainControlMode = 50593915
PicamParameter_EMIccdGain = 33620092
PicamParameter_PhosphorDecayDelay = 33685593
PicamParameter_PhosphorDecayDelayResolution = 50462810
PicamParameter_BracketGating = 50528356
PicamParameter_IntensifierOptions = 17039461
PicamParameter_EnableModulation = 50528367
PicamParameter_ModulationDuration = 33685622
PicamParameter_ModulationFrequency = 33685616
PicamParameter_RepetitiveModulationPhase = 33685617
PicamParameter_SequentialStartingModulationPhase = 33685618
PicamParameter_SequentialEndingModulationPhase = 33685619
PicamParameter_CustomModulationSequence = 101187703
PicamParameter_PhotocathodeSensitivity = 17039467
PicamParameter_GatingSpeed = 17039468
PicamParameter_PhosphorType = 17039469
PicamParameter_IntensifierDiameter = 16908398
PicamParameter_AdcSpeed = 50462753
PicamParameter_AdcBitDepth = 50397218
PicamParameter_AdcAnalogGain = 50593827
PicamParameter_AdcQuality = 50593828
PicamParameter_AdcEMGain = 33620021
PicamParameter_CorrectPixelBias = 50528362
PicamParameter_TriggerSource = 50593871
PicamParameter_TriggerResponse = 50593822
PicamParameter_TriggerDetermination = 50593823
PicamParameter_TriggerFrequency = 33685584
PicamParameter_TriggerTermination = 50593873
PicamParameter_TriggerCoupling = 50593874
PicamParameter_TriggerThreshold = 33685587
PicamParameter_TriggerDelay = 33685668
PicamParameter_OutputSignal = 50593824
PicamParameter_InvertOutputSignal = 50528308
PicamParameter_OutputSignal2 = 50593942
PicamParameter_InvertOutputSignal2 = 50528407
PicamParameter_EnableAuxOutput = 50528417
PicamParameter_AuxOutput = 84344923
PicamParameter_EnableSyncMaster = 50528340
PicamParameter_SyncMaster2Delay = 33685589
PicamParameter_EnableModulationOutputSignal = 50528372
PicamParameter_ModulationOutputSignalFrequency = 33685621
PicamParameter_ModulationOutputSignalAmplitude = 33685624
PicamParameter_AnticipateTrigger = 50528387
PicamParameter_DelayFromPreTrigger = 33685636
PicamParameter_ReadoutControlMode = 50593818
PicamParameter_ReadoutTimeCalculation = 16908315
PicamParameter_ReadoutPortCount = 50397212
PicamParameter_ReadoutOrientation = 17039414
PicamParameter_KineticsWindowHeight = 33620024
PicamParameter_SeNsRWindowHeight = 33620131
PicamParameter_VerticalShiftRate = 50462733
PicamParameter_Accumulations = 33947740
PicamParameter_EnableNondestructiveReadout = 50528384
PicamParameter_NondestructiveReadoutPeriod = 33685633
PicamParameter_Rois = 67436581
PicamParameter_NormalizeOrientation = 50528295
PicamParameter_DisableDataFormatting = 50528311
PicamParameter_ReadoutCount = 33947688
PicamParameter_ExactReadoutCountMaximum = 17170509
PicamParameter_PhotonDetectionMode = 50593917
PicamParameter_PhotonDetectionThreshold = 33685630
PicamParameter_PixelFormat = 50593833
PicamParameter_FrameSize = 16842794
PicamParameter_FrameStride = 16842795
PicamParameter_FramesPerReadout = 16842796
PicamParameter_ReadoutStride = 16842797
PicamParameter_PixelBitDepth = 16842800
PicamParameter_ReadoutRateCalculation = 16908338
PicamParameter_OnlineReadoutRateCalculation = 16908387
PicamParameter_FrameRateCalculation = 16908339
PicamParameter_Orientation = 17039398
PicamParameter_TimeStamps = 50593860
PicamParameter_TimeStampResolution = 50724933
PicamParameter_TimeStampBitDepth = 50397254
PicamParameter_TrackFrames = 50528327
PicamParameter_FrameTrackingBitDepth = 50397256
PicamParameter_GateTracking = 50593896
PicamParameter_GateTrackingBitDepth = 50397289
PicamParameter_ModulationTracking = 50593913
PicamParameter_ModulationTrackingBitDepth = 50397306
PicamParameter_SensorType = 17039417
PicamParameter_CcdCharacteristics = 17039418
PicamParameter_SensorActiveWidth = 16842811
PicamParameter_SensorActiveHeight = 16842812
PicamParameter_SensorActiveExtendedHeight = 16842911
PicamParameter_SensorActiveLeftMargin = 16842813
PicamParameter_SensorActiveTopMargin = 16842814
PicamParameter_SensorActiveRightMargin = 16842815
PicamParameter_SensorActiveBottomMargin = 16842816
PicamParameter_SensorMaskedHeight = 16842817
PicamParameter_SensorMaskedTopMargin = 16842818
PicamParameter_SensorMaskedBottomMargin = 16842819
PicamParameter_SensorSecondaryMaskedHeight = 16842801
PicamParameter_SensorSecondaryActiveHeight = 16842826
PicamParameter_PixelWidth = 16908297
PicamParameter_PixelHeight = 16908298
PicamParameter_PixelGapWidth = 16908299
PicamParameter_PixelGapHeight = 16908300
PicamParameter_ActiveWidth = 33619969
PicamParameter_ActiveHeight = 33619970
PicamParameter_ActiveExtendedHeight = 33620128
PicamParameter_ActiveLeftMargin = 33619971
PicamParameter_ActiveTopMargin = 33619972
PicamParameter_ActiveRightMargin = 33619973
PicamParameter_ActiveBottomMargin = 33619974
PicamParameter_MaskedHeight = 33619975
PicamParameter_MaskedTopMargin = 33619976
PicamParameter_MaskedBottomMargin = 33620041
PicamParameter_SecondaryMaskedHeight = 33620043
PicamParameter_SecondaryActiveHeight = 33620044
PicamParameter_CleanSectionFinalHeight = 33619985
PicamParameter_CleanSectionFinalHeightCount = 33619986
PicamParameter_CleanSerialRegister = 50528275
PicamParameter_CleanCycleCount = 33619988
PicamParameter_CleanCycleHeight = 33619989
PicamParameter_CleanBeforeExposure = 50528334
PicamParameter_CleanUntilTrigger = 50528278
PicamParameter_StopCleaningOnPreTrigger = 50528386
PicamParameter_SensorTemperatureSetPoint = 33685518
PicamParameter_SensorTemperatureReading = 16908303
PicamParameter_SensorTemperatureStatus = 17039376
PicamParameter_DisableCoolingFan = 50528285
PicamParameter_CoolingFanStatus = 17039522
PicamParameter_EnableSensorWindowHeater = 50528383
PicamParameter_VacuumStatus = 17039525
PicamParameter_CenterWavelengthSetPoint = 33685644
PicamParameter_CenterWavelengthReading = 16908429
PicamParameter_CenterWavelengthStatus = 17039509
PicamParameter_GratingType = 17039502
PicamParameter_GratingCoating = 17039503
PicamParameter_GratingGrooveDensity = 16908432
PicamParameter_GratingBlazingWavelength = 16908433
PicamParameter_FocalLength = 16908434
PicamParameter_InclusionAngle = 16908435
PicamParameter_SensorAngle = 16908436
PicamParameter_LightSource = 50593925
PicamParameter_LightSourceStatus = 17039494
PicamParameter_Age = 16908423
PicamParameter_LifeExpectancy = 16908424
PicamParameter_LaserOutputMode = 50593929
PicamParameter_LaserPower = 33685642
PicamParameter_LaserStatus = 17039517
PicamParameter_InputTriggerStatus = 17039518
PicamParameter = ctypes.c_int # enum
Picam_GetParameterIntegerValue = _libraries['libpicam.so.0'].Picam_GetParameterIntegerValue
Picam_GetParameterIntegerValue.restype = PicamError
Picam_GetParameterIntegerValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_int32)]
Picam_SetParameterIntegerValue = _libraries['libpicam.so.0'].Picam_SetParameterIntegerValue
Picam_SetParameterIntegerValue.restype = PicamError
Picam_SetParameterIntegerValue.argtypes = [PicamHandle, PicamParameter, piint]
Picam_CanSetParameterIntegerValue = _libraries['libpicam.so.0'].Picam_CanSetParameterIntegerValue
Picam_CanSetParameterIntegerValue.restype = PicamError
Picam_CanSetParameterIntegerValue.argtypes = [PicamHandle, PicamParameter, piint, POINTER_T(ctypes.c_int32)]
Picam_GetParameterLargeIntegerValue = _libraries['libpicam.so.0'].Picam_GetParameterLargeIntegerValue
Picam_GetParameterLargeIntegerValue.restype = PicamError
Picam_GetParameterLargeIntegerValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_int64)]
pi64s = ctypes.c_int64
Picam_SetParameterLargeIntegerValue = _libraries['libpicam.so.0'].Picam_SetParameterLargeIntegerValue
Picam_SetParameterLargeIntegerValue.restype = PicamError
Picam_SetParameterLargeIntegerValue.argtypes = [PicamHandle, PicamParameter, pi64s]
Picam_CanSetParameterLargeIntegerValue = _libraries['libpicam.so.0'].Picam_CanSetParameterLargeIntegerValue
Picam_CanSetParameterLargeIntegerValue.restype = PicamError
Picam_CanSetParameterLargeIntegerValue.argtypes = [PicamHandle, PicamParameter, pi64s, POINTER_T(ctypes.c_int32)]
Picam_GetParameterFloatingPointValue = _libraries['libpicam.so.0'].Picam_GetParameterFloatingPointValue
Picam_GetParameterFloatingPointValue.restype = PicamError
Picam_GetParameterFloatingPointValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_double)]
piflt = ctypes.c_double
Picam_SetParameterFloatingPointValue = _libraries['libpicam.so.0'].Picam_SetParameterFloatingPointValue
Picam_SetParameterFloatingPointValue.restype = PicamError
Picam_SetParameterFloatingPointValue.argtypes = [PicamHandle, PicamParameter, piflt]
Picam_CanSetParameterFloatingPointValue = _libraries['libpicam.so.0'].Picam_CanSetParameterFloatingPointValue
Picam_CanSetParameterFloatingPointValue.restype = PicamError
Picam_CanSetParameterFloatingPointValue.argtypes = [PicamHandle, PicamParameter, piflt, POINTER_T(ctypes.c_int32)]
class struct_PicamRoi(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('x', ctypes.c_int32),
    ('width', ctypes.c_int32),
    ('x_binning', ctypes.c_int32),
    ('y', ctypes.c_int32),
    ('height', ctypes.c_int32),
    ('y_binning', ctypes.c_int32),
     ]

PicamRoi = struct_PicamRoi
class struct_PicamRois(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('roi_array', POINTER_T(struct_PicamRoi)),
    ('roi_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

PicamRois = struct_PicamRois
Picam_DestroyRois = _libraries['libpicam.so.0'].Picam_DestroyRois
Picam_DestroyRois.restype = PicamError
Picam_DestroyRois.argtypes = [POINTER_T(struct_PicamRois)]
Picam_GetParameterRoisValue = _libraries['libpicam.so.0'].Picam_GetParameterRoisValue
Picam_GetParameterRoisValue.restype = PicamError
Picam_GetParameterRoisValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamRois))]
Picam_SetParameterRoisValue = _libraries['libpicam.so.0'].Picam_SetParameterRoisValue
Picam_SetParameterRoisValue.restype = PicamError
Picam_SetParameterRoisValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(struct_PicamRois)]
Picam_CanSetParameterRoisValue = _libraries['libpicam.so.0'].Picam_CanSetParameterRoisValue
Picam_CanSetParameterRoisValue.restype = PicamError
Picam_CanSetParameterRoisValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(struct_PicamRois), POINTER_T(ctypes.c_int32)]
class struct_PicamPulse(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('delay', ctypes.c_double),
    ('width', ctypes.c_double),
     ]

PicamPulse = struct_PicamPulse
Picam_DestroyPulses = _libraries['libpicam.so.0'].Picam_DestroyPulses
Picam_DestroyPulses.restype = PicamError
Picam_DestroyPulses.argtypes = [POINTER_T(struct_PicamPulse)]
Picam_GetParameterPulseValue = _libraries['libpicam.so.0'].Picam_GetParameterPulseValue
Picam_GetParameterPulseValue.restype = PicamError
Picam_GetParameterPulseValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamPulse))]
Picam_SetParameterPulseValue = _libraries['libpicam.so.0'].Picam_SetParameterPulseValue
Picam_SetParameterPulseValue.restype = PicamError
Picam_SetParameterPulseValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(struct_PicamPulse)]
Picam_CanSetParameterPulseValue = _libraries['libpicam.so.0'].Picam_CanSetParameterPulseValue
Picam_CanSetParameterPulseValue.restype = PicamError
Picam_CanSetParameterPulseValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(struct_PicamPulse), POINTER_T(ctypes.c_int32)]
class struct_PicamModulation(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('duration', ctypes.c_double),
    ('frequency', ctypes.c_double),
    ('phase', ctypes.c_double),
    ('output_signal_frequency', ctypes.c_double),
     ]

PicamModulation = struct_PicamModulation
class struct_PicamModulations(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('modulation_array', POINTER_T(struct_PicamModulation)),
    ('modulation_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

PicamModulations = struct_PicamModulations
Picam_DestroyModulations = _libraries['libpicam.so.0'].Picam_DestroyModulations
Picam_DestroyModulations.restype = PicamError
Picam_DestroyModulations.argtypes = [POINTER_T(struct_PicamModulations)]
Picam_GetParameterModulationsValue = _libraries['libpicam.so.0'].Picam_GetParameterModulationsValue
Picam_GetParameterModulationsValue.restype = PicamError
Picam_GetParameterModulationsValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamModulations))]
Picam_SetParameterModulationsValue = _libraries['libpicam.so.0'].Picam_SetParameterModulationsValue
Picam_SetParameterModulationsValue.restype = PicamError
Picam_SetParameterModulationsValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(struct_PicamModulations)]
Picam_CanSetParameterModulationsValue = _libraries['libpicam.so.0'].Picam_CanSetParameterModulationsValue
Picam_CanSetParameterModulationsValue.restype = PicamError
Picam_CanSetParameterModulationsValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(struct_PicamModulations), POINTER_T(ctypes.c_int32)]

# values for enumeration 'PicamActiveShutter'
PicamActiveShutter_None = 1
PicamActiveShutter_Internal = 2
PicamActiveShutter_External = 3
PicamActiveShutter = ctypes.c_int # enum

# values for enumeration 'PicamAdcAnalogGain'
PicamAdcAnalogGain_Low = 1
PicamAdcAnalogGain_Medium = 2
PicamAdcAnalogGain_High = 3
PicamAdcAnalogGain = ctypes.c_int # enum

# values for enumeration 'PicamAdcQuality'
PicamAdcQuality_LowNoise = 1
PicamAdcQuality_HighCapacity = 2
PicamAdcQuality_HighSpeed = 4
PicamAdcQuality_ElectronMultiplied = 3
PicamAdcQuality = ctypes.c_int # enum

# values for enumeration 'PicamCcdCharacteristicsMask'
PicamCcdCharacteristicsMask_None = 0
PicamCcdCharacteristicsMask_BackIlluminated = 1
PicamCcdCharacteristicsMask_DeepDepleted = 2
PicamCcdCharacteristicsMask_OpenElectrode = 4
PicamCcdCharacteristicsMask_UVEnhanced = 8
PicamCcdCharacteristicsMask_ExcelonEnabled = 16
PicamCcdCharacteristicsMask_SecondaryMask = 32
PicamCcdCharacteristicsMask_Multiport = 64
PicamCcdCharacteristicsMask_AdvancedInvertedMode = 128
PicamCcdCharacteristicsMask_HighResistivity = 256
PicamCcdCharacteristicsMask = ctypes.c_int # enum

# values for enumeration 'PicamCenterWavelengthStatus'
PicamCenterWavelengthStatus_Moving = 1
PicamCenterWavelengthStatus_Stationary = 2
PicamCenterWavelengthStatus_Faulted = 3
PicamCenterWavelengthStatus = ctypes.c_int # enum

# values for enumeration 'PicamCoolingFanStatus'
PicamCoolingFanStatus_Off = 1
PicamCoolingFanStatus_On = 2
PicamCoolingFanStatus_ForcedOn = 3
PicamCoolingFanStatus = ctypes.c_int # enum

# values for enumeration 'PicamEMIccdGainControlMode'
PicamEMIccdGainControlMode_Optimal = 1
PicamEMIccdGainControlMode_Manual = 2
PicamEMIccdGainControlMode = ctypes.c_int # enum

# values for enumeration 'PicamGateTrackingMask'
PicamGateTrackingMask_None = 0
PicamGateTrackingMask_Delay = 1
PicamGateTrackingMask_Width = 2
PicamGateTrackingMask = ctypes.c_int # enum

# values for enumeration 'PicamGatingMode'
PicamGatingMode_Disabled = 4
PicamGatingMode_Repetitive = 1
PicamGatingMode_Sequential = 2
PicamGatingMode_Custom = 3
PicamGatingMode = ctypes.c_int # enum

# values for enumeration 'PicamGatingSpeed'
PicamGatingSpeed_Fast = 1
PicamGatingSpeed_Slow = 2
PicamGatingSpeed = ctypes.c_int # enum

# values for enumeration 'PicamGratingCoating'
PicamGratingCoating_Al = 1
PicamGratingCoating_AlMgF2 = 4
PicamGratingCoating_Ag = 2
PicamGratingCoating_Au = 3
PicamGratingCoating = ctypes.c_int # enum

# values for enumeration 'PicamGratingType'
PicamGratingType_Ruled = 1
PicamGratingType_HolographicVisible = 2
PicamGratingType_HolographicNir = 3
PicamGratingType_HolographicUV = 4
PicamGratingType_Mirror = 5
PicamGratingType = ctypes.c_int # enum

# values for enumeration 'PicamIntensifierOptionsMask'
PicamIntensifierOptionsMask_None = 0
PicamIntensifierOptionsMask_McpGating = 1
PicamIntensifierOptionsMask_SubNanosecondGating = 2
PicamIntensifierOptionsMask_Modulation = 4
PicamIntensifierOptionsMask = ctypes.c_int # enum

# values for enumeration 'PicamIntensifierStatus'
PicamIntensifierStatus_PoweredOff = 1
PicamIntensifierStatus_PoweredOn = 2
PicamIntensifierStatus = ctypes.c_int # enum

# values for enumeration 'PicamLaserOutputMode'
PicamLaserOutputMode_Disabled = 1
PicamLaserOutputMode_ContinuousWave = 2
PicamLaserOutputMode_Pulsed = 3
PicamLaserOutputMode = ctypes.c_int # enum

# values for enumeration 'PicamLaserStatus'
PicamLaserStatus_Disarmed = 1
PicamLaserStatus_Unarmed = 2
PicamLaserStatus_Arming = 3
PicamLaserStatus_Armed = 4
PicamLaserStatus = ctypes.c_int # enum

# values for enumeration 'PicamLightSource'
PicamLightSource_Disabled = 1
PicamLightSource_Hg = 2
PicamLightSource_NeAr = 3
PicamLightSource_Qth = 4
PicamLightSource = ctypes.c_int # enum

# values for enumeration 'PicamLightSourceStatus'
PicamLightSourceStatus_Unstable = 1
PicamLightSourceStatus_Stable = 2
PicamLightSourceStatus = ctypes.c_int # enum

# values for enumeration 'PicamModulationTrackingMask'
PicamModulationTrackingMask_None = 0
PicamModulationTrackingMask_Duration = 1
PicamModulationTrackingMask_Frequency = 2
PicamModulationTrackingMask_Phase = 4
PicamModulationTrackingMask_OutputSignalFrequency = 8
PicamModulationTrackingMask = ctypes.c_int # enum

# values for enumeration 'PicamOrientationMask'
PicamOrientationMask_Normal = 0
PicamOrientationMask_FlippedHorizontally = 1
PicamOrientationMask_FlippedVertically = 2
PicamOrientationMask = ctypes.c_int # enum

# values for enumeration 'PicamOutputSignal'
PicamOutputSignal_Acquiring = 6
PicamOutputSignal_AlwaysHigh = 5
PicamOutputSignal_AlwaysLow = 4
PicamOutputSignal_AuxOutput = 14
PicamOutputSignal_Busy = 3
PicamOutputSignal_EffectivelyExposing = 9
PicamOutputSignal_EffectivelyExposingAlternation = 15
PicamOutputSignal_Exposing = 8
PicamOutputSignal_Gate = 13
PicamOutputSignal_InternalTriggerT0 = 12
PicamOutputSignal_NotReadingOut = 1
PicamOutputSignal_ReadingOut = 10
PicamOutputSignal_ShiftingUnderMask = 7
PicamOutputSignal_ShutterOpen = 2
PicamOutputSignal_WaitingForTrigger = 11
PicamOutputSignal = ctypes.c_int # enum

# values for enumeration 'PicamPhosphorType'
PicamPhosphorType_P43 = 1
PicamPhosphorType_P46 = 2
PicamPhosphorType = ctypes.c_int # enum

# values for enumeration 'PicamPhotocathodeSensitivity'
PicamPhotocathodeSensitivity_RedBlue = 1
PicamPhotocathodeSensitivity_SuperRed = 7
PicamPhotocathodeSensitivity_SuperBlue = 2
PicamPhotocathodeSensitivity_UV = 3
PicamPhotocathodeSensitivity_SolarBlind = 10
PicamPhotocathodeSensitivity_Unigen2Filmless = 4
PicamPhotocathodeSensitivity_InGaAsFilmless = 9
PicamPhotocathodeSensitivity_HighQEFilmless = 5
PicamPhotocathodeSensitivity_HighRedFilmless = 8
PicamPhotocathodeSensitivity_HighBlueFilmless = 6
PicamPhotocathodeSensitivity = ctypes.c_int # enum

# values for enumeration 'PicamPhotonDetectionMode'
PicamPhotonDetectionMode_Disabled = 1
PicamPhotonDetectionMode_Thresholding = 2
PicamPhotonDetectionMode_Clipping = 3
PicamPhotonDetectionMode = ctypes.c_int # enum

# values for enumeration 'PicamPixelFormat'
PicamPixelFormat_Monochrome16Bit = 1
PicamPixelFormat_Monochrome32Bit = 2
PicamPixelFormat = ctypes.c_int # enum

# values for enumeration 'PicamReadoutControlMode'
PicamReadoutControlMode_FullFrame = 1
PicamReadoutControlMode_FrameTransfer = 2
PicamReadoutControlMode_Interline = 5
PicamReadoutControlMode_RollingShutter = 8
PicamReadoutControlMode_Kinetics = 3
PicamReadoutControlMode_SpectraKinetics = 4
PicamReadoutControlMode_Dif = 6
PicamReadoutControlMode_SeNsR = 7
PicamReadoutControlMode = ctypes.c_int # enum

# values for enumeration 'PicamSensorTemperatureStatus'
PicamSensorTemperatureStatus_Unlocked = 1
PicamSensorTemperatureStatus_Locked = 2
PicamSensorTemperatureStatus_Faulted = 3
PicamSensorTemperatureStatus = ctypes.c_int # enum

# values for enumeration 'PicamSensorType'
PicamSensorType_Ccd = 1
PicamSensorType_InGaAs = 2
PicamSensorType_Cmos = 3
PicamSensorType = ctypes.c_int # enum

# values for enumeration 'PicamShutterStatus'
PicamShutterStatus_NotConnected = 1
PicamShutterStatus_Connected = 2
PicamShutterStatus_Overheated = 3
PicamShutterStatus = ctypes.c_int # enum

# values for enumeration 'PicamShutterTimingMode'
PicamShutterTimingMode_Normal = 1
PicamShutterTimingMode_AlwaysClosed = 2
PicamShutterTimingMode_AlwaysOpen = 3
PicamShutterTimingMode_OpenBeforeTrigger = 4
PicamShutterTimingMode = ctypes.c_int # enum

# values for enumeration 'PicamShutterType'
PicamShutterType_None = 1
PicamShutterType_VincentCS25 = 2
PicamShutterType_VincentCS45 = 3
PicamShutterType_VincentCS90 = 9
PicamShutterType_VincentDSS10 = 8
PicamShutterType_VincentVS25 = 4
PicamShutterType_VincentVS35 = 5
PicamShutterType_ProntorMagnetic0 = 6
PicamShutterType_ProntorMagneticE40 = 7
PicamShutterType = ctypes.c_int # enum

# values for enumeration 'PicamTimeStampsMask'
PicamTimeStampsMask_None = 0
PicamTimeStampsMask_ExposureStarted = 1
PicamTimeStampsMask_ExposureEnded = 2
PicamTimeStampsMask = ctypes.c_int # enum

# values for enumeration 'PicamTriggerCoupling'
PicamTriggerCoupling_AC = 1
PicamTriggerCoupling_DC = 2
PicamTriggerCoupling = ctypes.c_int # enum

# values for enumeration 'PicamTriggerDetermination'
PicamTriggerDetermination_PositivePolarity = 1
PicamTriggerDetermination_NegativePolarity = 2
PicamTriggerDetermination_RisingEdge = 3
PicamTriggerDetermination_FallingEdge = 4
PicamTriggerDetermination_AlternatingEdgeRising = 5
PicamTriggerDetermination_AlternatingEdgeFalling = 6
PicamTriggerDetermination = ctypes.c_int # enum

# values for enumeration 'PicamTriggerResponse'
PicamTriggerResponse_NoResponse = 1
PicamTriggerResponse_StartOnSingleTrigger = 5
PicamTriggerResponse_ReadoutPerTrigger = 2
PicamTriggerResponse_ShiftPerTrigger = 3
PicamTriggerResponse_GatePerTrigger = 6
PicamTriggerResponse_ExposeDuringTriggerPulse = 4
PicamTriggerResponse = ctypes.c_int # enum

# values for enumeration 'PicamTriggerSource'
PicamTriggerSource_None = 3
PicamTriggerSource_Internal = 2
PicamTriggerSource_External = 1
PicamTriggerSource = ctypes.c_int # enum

# values for enumeration 'PicamTriggerStatus'
PicamTriggerStatus_NotConnected = 1
PicamTriggerStatus_Connected = 2
PicamTriggerStatus = ctypes.c_int # enum

# values for enumeration 'PicamTriggerTermination'
PicamTriggerTermination_FiftyOhms = 1
PicamTriggerTermination_HighImpedance = 2
PicamTriggerTermination = ctypes.c_int # enum

# values for enumeration 'PicamVacuumStatus'
PicamVacuumStatus_Sufficient = 1
PicamVacuumStatus_Low = 2
PicamVacuumStatus = ctypes.c_int # enum
Picam_GetParameterIntegerDefaultValue = _libraries['libpicam.so.0'].Picam_GetParameterIntegerDefaultValue
Picam_GetParameterIntegerDefaultValue.restype = PicamError
Picam_GetParameterIntegerDefaultValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_int32)]
Picam_GetParameterLargeIntegerDefaultValue = _libraries['libpicam.so.0'].Picam_GetParameterLargeIntegerDefaultValue
Picam_GetParameterLargeIntegerDefaultValue.restype = PicamError
Picam_GetParameterLargeIntegerDefaultValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_int64)]
Picam_GetParameterFloatingPointDefaultValue = _libraries['libpicam.so.0'].Picam_GetParameterFloatingPointDefaultValue
Picam_GetParameterFloatingPointDefaultValue.restype = PicamError
Picam_GetParameterFloatingPointDefaultValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_double)]
Picam_GetParameterRoisDefaultValue = _libraries['libpicam.so.0'].Picam_GetParameterRoisDefaultValue
Picam_GetParameterRoisDefaultValue.restype = PicamError
Picam_GetParameterRoisDefaultValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamRois))]
Picam_GetParameterPulseDefaultValue = _libraries['libpicam.so.0'].Picam_GetParameterPulseDefaultValue
Picam_GetParameterPulseDefaultValue.restype = PicamError
Picam_GetParameterPulseDefaultValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamPulse))]
Picam_GetParameterModulationsDefaultValue = _libraries['libpicam.so.0'].Picam_GetParameterModulationsDefaultValue
Picam_GetParameterModulationsDefaultValue.restype = PicamError
Picam_GetParameterModulationsDefaultValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamModulations))]
Picam_RestoreParametersToDefaultValues = _libraries['libpicam.so.0'].Picam_RestoreParametersToDefaultValues
Picam_RestoreParametersToDefaultValues.restype = PicamError
Picam_RestoreParametersToDefaultValues.argtypes = [PicamHandle]
Picam_CanSetParameterOnline = _libraries['libpicam.so.0'].Picam_CanSetParameterOnline
Picam_CanSetParameterOnline.restype = PicamError
Picam_CanSetParameterOnline.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_int32)]
Picam_SetParameterIntegerValueOnline = _libraries['libpicam.so.0'].Picam_SetParameterIntegerValueOnline
Picam_SetParameterIntegerValueOnline.restype = PicamError
Picam_SetParameterIntegerValueOnline.argtypes = [PicamHandle, PicamParameter, piint]
Picam_SetParameterFloatingPointValueOnline = _libraries['libpicam.so.0'].Picam_SetParameterFloatingPointValueOnline
Picam_SetParameterFloatingPointValueOnline.restype = PicamError
Picam_SetParameterFloatingPointValueOnline.argtypes = [PicamHandle, PicamParameter, piflt]
Picam_SetParameterPulseValueOnline = _libraries['libpicam.so.0'].Picam_SetParameterPulseValueOnline
Picam_SetParameterPulseValueOnline.restype = PicamError
Picam_SetParameterPulseValueOnline.argtypes = [PicamHandle, PicamParameter, POINTER_T(struct_PicamPulse)]
Picam_CanReadParameter = _libraries['libpicam.so.0'].Picam_CanReadParameter
Picam_CanReadParameter.restype = PicamError
Picam_CanReadParameter.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_int32)]
Picam_ReadParameterIntegerValue = _libraries['libpicam.so.0'].Picam_ReadParameterIntegerValue
Picam_ReadParameterIntegerValue.restype = PicamError
Picam_ReadParameterIntegerValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_int32)]
Picam_ReadParameterFloatingPointValue = _libraries['libpicam.so.0'].Picam_ReadParameterFloatingPointValue
Picam_ReadParameterFloatingPointValue.restype = PicamError
Picam_ReadParameterFloatingPointValue.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_double)]
Picam_CanWaitForStatusParameter = _libraries['libpicam.so.0'].Picam_CanWaitForStatusParameter
Picam_CanWaitForStatusParameter.restype = PicamError
Picam_CanWaitForStatusParameter.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_int32)]
class struct_PicamStatusPurview(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('values_array', POINTER_T(ctypes.c_int32)),
    ('values_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

PicamStatusPurview = struct_PicamStatusPurview
Picam_DestroyStatusPurviews = _libraries['libpicam.so.0'].Picam_DestroyStatusPurviews
Picam_DestroyStatusPurviews.restype = PicamError
Picam_DestroyStatusPurviews.argtypes = [POINTER_T(struct_PicamStatusPurview)]
Picam_GetStatusParameterPurview = _libraries['libpicam.so.0'].Picam_GetStatusParameterPurview
Picam_GetStatusParameterPurview.restype = PicamError
Picam_GetStatusParameterPurview.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamStatusPurview))]
Picam_EstimateTimeToStatusParameterValue = _libraries['libpicam.so.0'].Picam_EstimateTimeToStatusParameterValue
Picam_EstimateTimeToStatusParameterValue.restype = PicamError
Picam_EstimateTimeToStatusParameterValue.argtypes = [PicamHandle, PicamParameter, piint, POINTER_T(ctypes.c_int32)]
Picam_WaitForStatusParameterValue = _libraries['libpicam.so.0'].Picam_WaitForStatusParameterValue
Picam_WaitForStatusParameterValue.restype = PicamError
Picam_WaitForStatusParameterValue.argtypes = [PicamHandle, PicamParameter, piint, piint]
Picam_DestroyParameters = _libraries['libpicam.so.0'].Picam_DestroyParameters
Picam_DestroyParameters.restype = PicamError
Picam_DestroyParameters.argtypes = [POINTER_T(PicamParameter)]
Picam_GetParameters = _libraries['libpicam.so.0'].Picam_GetParameters
Picam_GetParameters.restype = PicamError
Picam_GetParameters.argtypes = [PicamHandle, POINTER_T(POINTER_T(PicamParameter)), POINTER_T(ctypes.c_int32)]
Picam_DoesParameterExist = _libraries['libpicam.so.0'].Picam_DoesParameterExist
Picam_DoesParameterExist.restype = PicamError
Picam_DoesParameterExist.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_int32)]
Picam_IsParameterRelevant = _libraries['libpicam.so.0'].Picam_IsParameterRelevant
Picam_IsParameterRelevant.restype = PicamError
Picam_IsParameterRelevant.argtypes = [PicamHandle, PicamParameter, POINTER_T(ctypes.c_int32)]
Picam_GetParameterValueType = _libraries['libpicam.so.0'].Picam_GetParameterValueType
Picam_GetParameterValueType.restype = PicamError
Picam_GetParameterValueType.argtypes = [PicamHandle, PicamParameter, POINTER_T(PicamValueType)]
Picam_GetParameterEnumeratedType = _libraries['libpicam.so.0'].Picam_GetParameterEnumeratedType
Picam_GetParameterEnumeratedType.restype = PicamError
Picam_GetParameterEnumeratedType.argtypes = [PicamHandle, PicamParameter, POINTER_T(PicamEnumeratedType)]

# values for enumeration 'PicamValueAccess'
PicamValueAccess_ReadOnly = 1
PicamValueAccess_ReadWriteTrivial = 3
PicamValueAccess_ReadWrite = 2
PicamValueAccess = ctypes.c_int # enum
Picam_GetParameterValueAccess = _libraries['libpicam.so.0'].Picam_GetParameterValueAccess
Picam_GetParameterValueAccess.restype = PicamError
Picam_GetParameterValueAccess.argtypes = [PicamHandle, PicamParameter, POINTER_T(PicamValueAccess)]
Picam_GetParameterConstraintType = _libraries['libpicam.so.0'].Picam_GetParameterConstraintType
Picam_GetParameterConstraintType.restype = PicamError
Picam_GetParameterConstraintType.argtypes = [PicamHandle, PicamParameter, POINTER_T(PicamConstraintType)]

# values for enumeration 'PicamConstraintScope'
PicamConstraintScope_Independent = 1
PicamConstraintScope_Dependent = 2
PicamConstraintScope = ctypes.c_int # enum

# values for enumeration 'PicamConstraintSeverity'
PicamConstraintSeverity_Error = 1
PicamConstraintSeverity_Warning = 2
PicamConstraintSeverity = ctypes.c_int # enum

# values for enumeration 'PicamConstraintCategory'
PicamConstraintCategory_Capable = 1
PicamConstraintCategory_Required = 2
PicamConstraintCategory_Recommended = 3
PicamConstraintCategory = ctypes.c_int # enum
class struct_PicamCollectionConstraint(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('scope', PicamConstraintScope),
    ('severity', PicamConstraintSeverity),
    ('values_array', POINTER_T(ctypes.c_double)),
    ('values_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

PicamCollectionConstraint = struct_PicamCollectionConstraint
Picam_DestroyCollectionConstraints = _libraries['libpicam.so.0'].Picam_DestroyCollectionConstraints
Picam_DestroyCollectionConstraints.restype = PicamError
Picam_DestroyCollectionConstraints.argtypes = [POINTER_T(struct_PicamCollectionConstraint)]
Picam_GetParameterCollectionConstraint = _libraries['libpicam.so.0'].Picam_GetParameterCollectionConstraint
Picam_GetParameterCollectionConstraint.restype = PicamError
Picam_GetParameterCollectionConstraint.argtypes = [PicamHandle, PicamParameter, PicamConstraintCategory, POINTER_T(POINTER_T(struct_PicamCollectionConstraint))]
class struct_PicamRangeConstraint(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('scope', PicamConstraintScope),
    ('severity', PicamConstraintSeverity),
    ('empty_set', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('minimum', ctypes.c_double),
    ('maximum', ctypes.c_double),
    ('increment', ctypes.c_double),
    ('excluded_values_array', POINTER_T(ctypes.c_double)),
    ('excluded_values_count', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('outlying_values_array', POINTER_T(ctypes.c_double)),
    ('outlying_values_count', ctypes.c_int32),
    ('PADDING_2', ctypes.c_ubyte * 4),
     ]

PicamRangeConstraint = struct_PicamRangeConstraint
Picam_DestroyRangeConstraints = _libraries['libpicam.so.0'].Picam_DestroyRangeConstraints
Picam_DestroyRangeConstraints.restype = PicamError
Picam_DestroyRangeConstraints.argtypes = [POINTER_T(struct_PicamRangeConstraint)]
Picam_GetParameterRangeConstraint = _libraries['libpicam.so.0'].Picam_GetParameterRangeConstraint
Picam_GetParameterRangeConstraint.restype = PicamError
Picam_GetParameterRangeConstraint.argtypes = [PicamHandle, PicamParameter, PicamConstraintCategory, POINTER_T(POINTER_T(struct_PicamRangeConstraint))]

# values for enumeration 'PicamRoisConstraintRulesMask'
PicamRoisConstraintRulesMask_None = 0
PicamRoisConstraintRulesMask_XBinningAlignment = 1
PicamRoisConstraintRulesMask_YBinningAlignment = 2
PicamRoisConstraintRulesMask_HorizontalSymmetry = 4
PicamRoisConstraintRulesMask_VerticalSymmetry = 8
PicamRoisConstraintRulesMask_SymmetryBoundsBinning = 16
PicamRoisConstraintRulesMask = ctypes.c_int # enum
class struct_PicamRoisConstraint(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('scope', PicamConstraintScope),
    ('severity', PicamConstraintSeverity),
    ('empty_set', ctypes.c_int32),
    ('rules', PicamRoisConstraintRulesMask),
    ('maximum_roi_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('x_constraint', PicamRangeConstraint),
    ('width_constraint', PicamRangeConstraint),
    ('x_binning_limits_array', POINTER_T(ctypes.c_int32)),
    ('x_binning_limits_count', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('y_constraint', PicamRangeConstraint),
    ('height_constraint', PicamRangeConstraint),
    ('y_binning_limits_array', POINTER_T(ctypes.c_int32)),
    ('y_binning_limits_count', ctypes.c_int32),
    ('PADDING_2', ctypes.c_ubyte * 4),
     ]

PicamRoisConstraint = struct_PicamRoisConstraint
Picam_DestroyRoisConstraints = _libraries['libpicam.so.0'].Picam_DestroyRoisConstraints
Picam_DestroyRoisConstraints.restype = PicamError
Picam_DestroyRoisConstraints.argtypes = [POINTER_T(struct_PicamRoisConstraint)]
Picam_GetParameterRoisConstraint = _libraries['libpicam.so.0'].Picam_GetParameterRoisConstraint
Picam_GetParameterRoisConstraint.restype = PicamError
Picam_GetParameterRoisConstraint.argtypes = [PicamHandle, PicamParameter, PicamConstraintCategory, POINTER_T(POINTER_T(struct_PicamRoisConstraint))]
class struct_PicamPulseConstraint(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('scope', PicamConstraintScope),
    ('severity', PicamConstraintSeverity),
    ('empty_set', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('delay_constraint', PicamRangeConstraint),
    ('width_constraint', PicamRangeConstraint),
    ('minimum_duration', ctypes.c_double),
    ('maximum_duration', ctypes.c_double),
     ]

PicamPulseConstraint = struct_PicamPulseConstraint
Picam_DestroyPulseConstraints = _libraries['libpicam.so.0'].Picam_DestroyPulseConstraints
Picam_DestroyPulseConstraints.restype = PicamError
Picam_DestroyPulseConstraints.argtypes = [POINTER_T(struct_PicamPulseConstraint)]
Picam_GetParameterPulseConstraint = _libraries['libpicam.so.0'].Picam_GetParameterPulseConstraint
Picam_GetParameterPulseConstraint.restype = PicamError
Picam_GetParameterPulseConstraint.argtypes = [PicamHandle, PicamParameter, PicamConstraintCategory, POINTER_T(POINTER_T(struct_PicamPulseConstraint))]
class struct_PicamModulationsConstraint(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('scope', PicamConstraintScope),
    ('severity', PicamConstraintSeverity),
    ('empty_set', ctypes.c_int32),
    ('maximum_modulation_count', ctypes.c_int32),
    ('duration_constraint', PicamRangeConstraint),
    ('frequency_constraint', PicamRangeConstraint),
    ('phase_constraint', PicamRangeConstraint),
    ('output_signal_frequency_constraint', PicamRangeConstraint),
     ]

PicamModulationsConstraint = struct_PicamModulationsConstraint
Picam_DestroyModulationsConstraints = _libraries['libpicam.so.0'].Picam_DestroyModulationsConstraints
Picam_DestroyModulationsConstraints.restype = PicamError
Picam_DestroyModulationsConstraints.argtypes = [POINTER_T(struct_PicamModulationsConstraint)]
Picam_GetParameterModulationsConstraint = _libraries['libpicam.so.0'].Picam_GetParameterModulationsConstraint
Picam_GetParameterModulationsConstraint.restype = PicamError
Picam_GetParameterModulationsConstraint.argtypes = [PicamHandle, PicamParameter, PicamConstraintCategory, POINTER_T(POINTER_T(struct_PicamModulationsConstraint))]
Picam_AreParametersCommitted = _libraries['libpicam.so.0'].Picam_AreParametersCommitted
Picam_AreParametersCommitted.restype = PicamError
Picam_AreParametersCommitted.argtypes = [PicamHandle, POINTER_T(ctypes.c_int32)]
Picam_CommitParameters = _libraries['libpicam.so.0'].Picam_CommitParameters
Picam_CommitParameters.restype = PicamError
Picam_CommitParameters.argtypes = [PicamHandle, POINTER_T(POINTER_T(PicamParameter)), POINTER_T(ctypes.c_int32)]
class struct_PicamAvailableData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('initial_readout', POINTER_T(None)),
    ('readout_count', ctypes.c_int64),
     ]

PicamAvailableData = struct_PicamAvailableData

# values for enumeration 'PicamAcquisitionErrorsMask'
PicamAcquisitionErrorsMask_None = 0
PicamAcquisitionErrorsMask_CameraFaulted = 16
PicamAcquisitionErrorsMask_ConnectionLost = 2
PicamAcquisitionErrorsMask_ShutterOverheated = 8
PicamAcquisitionErrorsMask_DataLost = 1
PicamAcquisitionErrorsMask_DataNotArriving = 4
PicamAcquisitionErrorsMask = ctypes.c_int # enum
Picam_Acquire = _libraries['libpicam.so.0'].Picam_Acquire
Picam_Acquire.restype = PicamError
Picam_Acquire.argtypes = [PicamHandle, pi64s, piint, POINTER_T(struct_PicamAvailableData), POINTER_T(PicamAcquisitionErrorsMask)]
Picam_StartAcquisition = _libraries['libpicam.so.0'].Picam_StartAcquisition
Picam_StartAcquisition.restype = PicamError
Picam_StartAcquisition.argtypes = [PicamHandle]
Picam_StopAcquisition = _libraries['libpicam.so.0'].Picam_StopAcquisition
Picam_StopAcquisition.restype = PicamError
Picam_StopAcquisition.argtypes = [PicamHandle]
Picam_IsAcquisitionRunning = _libraries['libpicam.so.0'].Picam_IsAcquisitionRunning
Picam_IsAcquisitionRunning.restype = PicamError
Picam_IsAcquisitionRunning.argtypes = [PicamHandle, POINTER_T(ctypes.c_int32)]
class struct_PicamAcquisitionStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('running', ctypes.c_int32),
    ('errors', PicamAcquisitionErrorsMask),
    ('readout_rate', ctypes.c_double),
     ]

PicamAcquisitionStatus = struct_PicamAcquisitionStatus
Picam_WaitForAcquisitionUpdate = _libraries['libpicam.so.0'].Picam_WaitForAcquisitionUpdate
Picam_WaitForAcquisitionUpdate.restype = PicamError
Picam_WaitForAcquisitionUpdate.argtypes = [PicamHandle, piint, POINTER_T(struct_PicamAvailableData), POINTER_T(struct_PicamAcquisitionStatus)]
class struct_PicamAccessoryID(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('model', PicamModel),
    ('computer_interface', PicamComputerInterface),
    ('serial_number', ctypes.c_char * 64),
     ]

PicamAccessoryID = struct_PicamAccessoryID
PicamAccessory_DestroyAccessoryIDs = _libraries['libpicam.so.0'].PicamAccessory_DestroyAccessoryIDs
PicamAccessory_DestroyAccessoryIDs.restype = PicamError
PicamAccessory_DestroyAccessoryIDs.argtypes = [POINTER_T(struct_PicamAccessoryID)]
PicamAccessory_GetAvailableAccessoryIDs = _libraries['libpicam.so.0'].PicamAccessory_GetAvailableAccessoryIDs
PicamAccessory_GetAvailableAccessoryIDs.restype = PicamError
PicamAccessory_GetAvailableAccessoryIDs.argtypes = [POINTER_T(POINTER_T(struct_PicamAccessoryID)), POINTER_T(ctypes.c_int32)]
PicamAccessory_GetUnavailableAccessoryIDs = _libraries['libpicam.so.0'].PicamAccessory_GetUnavailableAccessoryIDs
PicamAccessory_GetUnavailableAccessoryIDs.restype = PicamError
PicamAccessory_GetUnavailableAccessoryIDs.argtypes = [POINTER_T(POINTER_T(struct_PicamAccessoryID)), POINTER_T(ctypes.c_int32)]
PicamAccessory_IsAccessoryIDConnected = _libraries['libpicam.so.0'].PicamAccessory_IsAccessoryIDConnected
PicamAccessory_IsAccessoryIDConnected.restype = PicamError
PicamAccessory_IsAccessoryIDConnected.argtypes = [POINTER_T(struct_PicamAccessoryID), POINTER_T(ctypes.c_int32)]
PicamAccessory_IsAccessoryIDOpenElsewhere = _libraries['libpicam.so.0'].PicamAccessory_IsAccessoryIDOpenElsewhere
PicamAccessory_IsAccessoryIDOpenElsewhere.restype = PicamError
PicamAccessory_IsAccessoryIDOpenElsewhere.argtypes = [POINTER_T(struct_PicamAccessoryID), POINTER_T(ctypes.c_int32)]

# values for enumeration 'PicamDiscoveryAction'
PicamDiscoveryAction_Found = 1
PicamDiscoveryAction_Lost = 2
PicamDiscoveryAction_Faulted = 3
PicamDiscoveryAction = ctypes.c_int # enum
PicamAccessoryDiscoveryCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(struct_PicamAccessoryID), POINTER_T(None), PicamDiscoveryAction))
PicamAccessory_RegisterForDiscovery = _libraries['libpicam.so.0'].PicamAccessory_RegisterForDiscovery
PicamAccessory_RegisterForDiscovery.restype = PicamError
PicamAccessory_RegisterForDiscovery.argtypes = [PicamAccessoryDiscoveryCallback]
PicamAccessory_UnregisterForDiscovery = _libraries['libpicam.so.0'].PicamAccessory_UnregisterForDiscovery
PicamAccessory_UnregisterForDiscovery.restype = PicamError
PicamAccessory_UnregisterForDiscovery.argtypes = [PicamAccessoryDiscoveryCallback]
PicamAccessory_DiscoverAccessories = _libraries['libpicam.so.0'].PicamAccessory_DiscoverAccessories
PicamAccessory_DiscoverAccessories.restype = PicamError
PicamAccessory_DiscoverAccessories.argtypes = []
PicamAccessory_StopDiscoveringAccessories = _libraries['libpicam.so.0'].PicamAccessory_StopDiscoveringAccessories
PicamAccessory_StopDiscoveringAccessories.restype = PicamError
PicamAccessory_StopDiscoveringAccessories.argtypes = []
PicamAccessory_IsDiscoveringAccessories = _libraries['libpicam.so.0'].PicamAccessory_IsDiscoveringAccessories
PicamAccessory_IsDiscoveringAccessories.restype = PicamError
PicamAccessory_IsDiscoveringAccessories.argtypes = [POINTER_T(ctypes.c_int32)]
PicamAccessory_OpenFirstAccessory = _libraries['libpicam.so.0'].PicamAccessory_OpenFirstAccessory
PicamAccessory_OpenFirstAccessory.restype = PicamError
PicamAccessory_OpenFirstAccessory.argtypes = [POINTER_T(POINTER_T(None))]
PicamAccessory_OpenAccessory = _libraries['libpicam.so.0'].PicamAccessory_OpenAccessory
PicamAccessory_OpenAccessory.restype = PicamError
PicamAccessory_OpenAccessory.argtypes = [POINTER_T(struct_PicamAccessoryID), POINTER_T(POINTER_T(None))]
PicamAccessory_CloseAccessory = _libraries['libpicam.so.0'].PicamAccessory_CloseAccessory
PicamAccessory_CloseAccessory.restype = PicamError
PicamAccessory_CloseAccessory.argtypes = [PicamHandle]
PicamAccessory_GetOpenAccessories = _libraries['libpicam.so.0'].PicamAccessory_GetOpenAccessories
PicamAccessory_GetOpenAccessories.restype = PicamError
PicamAccessory_GetOpenAccessories.argtypes = [POINTER_T(POINTER_T(POINTER_T(None))), POINTER_T(ctypes.c_int32)]
PicamAccessory_IsAccessoryConnected = _libraries['libpicam.so.0'].PicamAccessory_IsAccessoryConnected
PicamAccessory_IsAccessoryConnected.restype = PicamError
PicamAccessory_IsAccessoryConnected.argtypes = [PicamHandle, POINTER_T(ctypes.c_int32)]
PicamAccessory_GetAccessoryID = _libraries['libpicam.so.0'].PicamAccessory_GetAccessoryID
PicamAccessory_GetAccessoryID.restype = PicamError
PicamAccessory_GetAccessoryID.argtypes = [PicamHandle, POINTER_T(struct_PicamAccessoryID)]
PicamAccessory_GetLightSourceReference = _libraries['libpicam.so.0'].PicamAccessory_GetLightSourceReference
PicamAccessory_GetLightSourceReference.restype = PicamError
PicamAccessory_GetLightSourceReference.argtypes = [PicamHandle, POINTER_T(POINTER_T(struct_PicamCalibration))]
PicamAccessory_GetFirmwareDetails = _libraries['libpicam.so.0'].PicamAccessory_GetFirmwareDetails
PicamAccessory_GetFirmwareDetails.restype = PicamError
PicamAccessory_GetFirmwareDetails.argtypes = [POINTER_T(struct_PicamAccessoryID), POINTER_T(POINTER_T(struct_PicamFirmwareDetail)), POINTER_T(ctypes.c_int32)]
PicamDiscoveryCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(struct_PicamCameraID), POINTER_T(None), PicamDiscoveryAction))
PicamAdvanced_RegisterForDiscovery = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForDiscovery
PicamAdvanced_RegisterForDiscovery.restype = PicamError
PicamAdvanced_RegisterForDiscovery.argtypes = [PicamDiscoveryCallback]
PicamAdvanced_UnregisterForDiscovery = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForDiscovery
PicamAdvanced_UnregisterForDiscovery.restype = PicamError
PicamAdvanced_UnregisterForDiscovery.argtypes = [PicamDiscoveryCallback]
PicamAdvanced_DiscoverCameras = _libraries['libpicam.so.0'].PicamAdvanced_DiscoverCameras
PicamAdvanced_DiscoverCameras.restype = PicamError
PicamAdvanced_DiscoverCameras.argtypes = []
PicamAdvanced_StopDiscoveringCameras = _libraries['libpicam.so.0'].PicamAdvanced_StopDiscoveringCameras
PicamAdvanced_StopDiscoveringCameras.restype = PicamError
PicamAdvanced_StopDiscoveringCameras.argtypes = []
PicamAdvanced_IsDiscoveringCameras = _libraries['libpicam.so.0'].PicamAdvanced_IsDiscoveringCameras
PicamAdvanced_IsDiscoveringCameras.restype = PicamError
PicamAdvanced_IsDiscoveringCameras.argtypes = [POINTER_T(ctypes.c_int32)]

# values for enumeration 'PicamHandleType'
PicamHandleType_CameraDevice = 1
PicamHandleType_CameraModel = 2
PicamHandleType_EMCalibration = 3
PicamHandleType_Accessory = 4
PicamHandleType = ctypes.c_int # enum
PicamAdvanced_GetHandleType = _libraries['libpicam.so.0'].PicamAdvanced_GetHandleType
PicamAdvanced_GetHandleType.restype = PicamError
PicamAdvanced_GetHandleType.argtypes = [PicamHandle, POINTER_T(PicamHandleType)]
PicamAdvanced_OpenCameraDevice = _libraries['libpicam.so.0'].PicamAdvanced_OpenCameraDevice
PicamAdvanced_OpenCameraDevice.restype = PicamError
PicamAdvanced_OpenCameraDevice.argtypes = [POINTER_T(struct_PicamCameraID), POINTER_T(POINTER_T(None))]
PicamAdvanced_CloseCameraDevice = _libraries['libpicam.so.0'].PicamAdvanced_CloseCameraDevice
PicamAdvanced_CloseCameraDevice.restype = PicamError
PicamAdvanced_CloseCameraDevice.argtypes = [PicamHandle]
PicamAdvanced_GetOpenCameraDevices = _libraries['libpicam.so.0'].PicamAdvanced_GetOpenCameraDevices
PicamAdvanced_GetOpenCameraDevices.restype = PicamError
PicamAdvanced_GetOpenCameraDevices.argtypes = [POINTER_T(POINTER_T(POINTER_T(None))), POINTER_T(ctypes.c_int32)]
PicamAdvanced_GetCameraModel = _libraries['libpicam.so.0'].PicamAdvanced_GetCameraModel
PicamAdvanced_GetCameraModel.restype = PicamError
PicamAdvanced_GetCameraModel.argtypes = [PicamHandle, POINTER_T(POINTER_T(None))]
PicamAdvanced_GetCameraDevice = _libraries['libpicam.so.0'].PicamAdvanced_GetCameraDevice
PicamAdvanced_GetCameraDevice.restype = PicamError
PicamAdvanced_GetCameraDevice.argtypes = [PicamHandle, POINTER_T(POINTER_T(None))]
PicamAdvanced_GetUserState = _libraries['libpicam.so.0'].PicamAdvanced_GetUserState
PicamAdvanced_GetUserState.restype = PicamError
PicamAdvanced_GetUserState.argtypes = [PicamHandle, POINTER_T(POINTER_T(None))]
PicamAdvanced_SetUserState = _libraries['libpicam.so.0'].PicamAdvanced_SetUserState
PicamAdvanced_SetUserState.restype = PicamError
PicamAdvanced_SetUserState.argtypes = [PicamHandle, POINTER_T(None)]
class struct_PicamPixelLocation(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('x', ctypes.c_int16),
    ('y', ctypes.c_int16),
     ]

PicamPixelLocation = struct_PicamPixelLocation
class struct_PicamColumnDefect(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('start', PicamPixelLocation),
    ('height', ctypes.c_int32),
     ]

PicamColumnDefect = struct_PicamColumnDefect
class struct_PicamRowDefect(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('start', PicamPixelLocation),
    ('width', ctypes.c_int32),
     ]

PicamRowDefect = struct_PicamRowDefect
class struct_PicamPixelDefectMap(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('column_defect_array', POINTER_T(struct_PicamColumnDefect)),
    ('column_defect_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('row_defect_array', POINTER_T(struct_PicamRowDefect)),
    ('row_defect_count', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('point_defect_array', POINTER_T(struct_PicamPixelLocation)),
    ('point_defect_count', ctypes.c_int32),
    ('PADDING_2', ctypes.c_ubyte * 4),
     ]

PicamPixelDefectMap = struct_PicamPixelDefectMap
PicamAdvanced_DestroyPixelDefectMaps = _libraries['libpicam.so.0'].PicamAdvanced_DestroyPixelDefectMaps
PicamAdvanced_DestroyPixelDefectMaps.restype = PicamError
PicamAdvanced_DestroyPixelDefectMaps.argtypes = [POINTER_T(struct_PicamPixelDefectMap)]
PicamAdvanced_GetPixelDefectMap = _libraries['libpicam.so.0'].PicamAdvanced_GetPixelDefectMap
PicamAdvanced_GetPixelDefectMap.restype = PicamError
PicamAdvanced_GetPixelDefectMap.argtypes = [PicamHandle, POINTER_T(POINTER_T(struct_PicamPixelDefectMap))]
PicamIntegerValueChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, ctypes.c_int32))
PicamAdvanced_RegisterForIntegerValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForIntegerValueChanged
PicamAdvanced_RegisterForIntegerValueChanged.restype = PicamError
PicamAdvanced_RegisterForIntegerValueChanged.argtypes = [PicamHandle, PicamParameter, PicamIntegerValueChangedCallback]
PicamAdvanced_UnregisterForIntegerValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForIntegerValueChanged
PicamAdvanced_UnregisterForIntegerValueChanged.restype = PicamError
PicamAdvanced_UnregisterForIntegerValueChanged.argtypes = [PicamHandle, PicamParameter, PicamIntegerValueChangedCallback]
PicamAdvanced_RegisterForExtrinsicIntegerValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForExtrinsicIntegerValueChanged
PicamAdvanced_RegisterForExtrinsicIntegerValueChanged.restype = PicamError
PicamAdvanced_RegisterForExtrinsicIntegerValueChanged.argtypes = [PicamHandle, PicamParameter, PicamIntegerValueChangedCallback]
PicamAdvanced_UnregisterForExtrinsicIntegerValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForExtrinsicIntegerValueChanged
PicamAdvanced_UnregisterForExtrinsicIntegerValueChanged.restype = PicamError
PicamAdvanced_UnregisterForExtrinsicIntegerValueChanged.argtypes = [PicamHandle, PicamParameter, PicamIntegerValueChangedCallback]
PicamLargeIntegerValueChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, ctypes.c_int64))
PicamAdvanced_RegisterForLargeIntegerValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForLargeIntegerValueChanged
PicamAdvanced_RegisterForLargeIntegerValueChanged.restype = PicamError
PicamAdvanced_RegisterForLargeIntegerValueChanged.argtypes = [PicamHandle, PicamParameter, PicamLargeIntegerValueChangedCallback]
PicamAdvanced_UnregisterForLargeIntegerValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForLargeIntegerValueChanged
PicamAdvanced_UnregisterForLargeIntegerValueChanged.restype = PicamError
PicamAdvanced_UnregisterForLargeIntegerValueChanged.argtypes = [PicamHandle, PicamParameter, PicamLargeIntegerValueChangedCallback]
PicamFloatingPointValueChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, ctypes.c_double))
PicamAdvanced_RegisterForFloatingPointValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForFloatingPointValueChanged
PicamAdvanced_RegisterForFloatingPointValueChanged.restype = PicamError
PicamAdvanced_RegisterForFloatingPointValueChanged.argtypes = [PicamHandle, PicamParameter, PicamFloatingPointValueChangedCallback]
PicamAdvanced_UnregisterForFloatingPointValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForFloatingPointValueChanged
PicamAdvanced_UnregisterForFloatingPointValueChanged.restype = PicamError
PicamAdvanced_UnregisterForFloatingPointValueChanged.argtypes = [PicamHandle, PicamParameter, PicamFloatingPointValueChangedCallback]
PicamAdvanced_RegisterForExtrinsicFloatingPointValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForExtrinsicFloatingPointValueChanged
PicamAdvanced_RegisterForExtrinsicFloatingPointValueChanged.restype = PicamError
PicamAdvanced_RegisterForExtrinsicFloatingPointValueChanged.argtypes = [PicamHandle, PicamParameter, PicamFloatingPointValueChangedCallback]
PicamAdvanced_UnregisterForExtrinsicFloatingPointValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForExtrinsicFloatingPointValueChanged
PicamAdvanced_UnregisterForExtrinsicFloatingPointValueChanged.restype = PicamError
PicamAdvanced_UnregisterForExtrinsicFloatingPointValueChanged.argtypes = [PicamHandle, PicamParameter, PicamFloatingPointValueChangedCallback]
PicamRoisValueChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, POINTER_T(struct_PicamRois)))
PicamAdvanced_RegisterForRoisValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForRoisValueChanged
PicamAdvanced_RegisterForRoisValueChanged.restype = PicamError
PicamAdvanced_RegisterForRoisValueChanged.argtypes = [PicamHandle, PicamParameter, PicamRoisValueChangedCallback]
PicamAdvanced_UnregisterForRoisValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForRoisValueChanged
PicamAdvanced_UnregisterForRoisValueChanged.restype = PicamError
PicamAdvanced_UnregisterForRoisValueChanged.argtypes = [PicamHandle, PicamParameter, PicamRoisValueChangedCallback]
PicamPulseValueChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, POINTER_T(struct_PicamPulse)))
PicamAdvanced_RegisterForPulseValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForPulseValueChanged
PicamAdvanced_RegisterForPulseValueChanged.restype = PicamError
PicamAdvanced_RegisterForPulseValueChanged.argtypes = [PicamHandle, PicamParameter, PicamPulseValueChangedCallback]
PicamAdvanced_UnregisterForPulseValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForPulseValueChanged
PicamAdvanced_UnregisterForPulseValueChanged.restype = PicamError
PicamAdvanced_UnregisterForPulseValueChanged.argtypes = [PicamHandle, PicamParameter, PicamPulseValueChangedCallback]
PicamModulationsValueChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, POINTER_T(struct_PicamModulations)))
PicamAdvanced_RegisterForModulationsValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForModulationsValueChanged
PicamAdvanced_RegisterForModulationsValueChanged.restype = PicamError
PicamAdvanced_RegisterForModulationsValueChanged.argtypes = [PicamHandle, PicamParameter, PicamModulationsValueChangedCallback]
PicamAdvanced_UnregisterForModulationsValueChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForModulationsValueChanged
PicamAdvanced_UnregisterForModulationsValueChanged.restype = PicamError
PicamAdvanced_UnregisterForModulationsValueChanged.argtypes = [PicamHandle, PicamParameter, PicamModulationsValueChangedCallback]
PicamWhenStatusParameterValueCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, ctypes.c_int32, PicamError))
PicamAdvanced_NotifyWhenStatusParameterValue = _libraries['libpicam.so.0'].PicamAdvanced_NotifyWhenStatusParameterValue
PicamAdvanced_NotifyWhenStatusParameterValue.restype = PicamError
PicamAdvanced_NotifyWhenStatusParameterValue.argtypes = [PicamHandle, PicamParameter, piint, PicamWhenStatusParameterValueCallback]
PicamAdvanced_CancelNotifyWhenStatusParameterValue = _libraries['libpicam.so.0'].PicamAdvanced_CancelNotifyWhenStatusParameterValue
PicamAdvanced_CancelNotifyWhenStatusParameterValue.restype = PicamError
PicamAdvanced_CancelNotifyWhenStatusParameterValue.argtypes = [PicamHandle, PicamParameter, piint, PicamWhenStatusParameterValueCallback]
PicamIsRelevantChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, ctypes.c_int32))
PicamAdvanced_RegisterForIsRelevantChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForIsRelevantChanged
PicamAdvanced_RegisterForIsRelevantChanged.restype = PicamError
PicamAdvanced_RegisterForIsRelevantChanged.argtypes = [PicamHandle, PicamParameter, PicamIsRelevantChangedCallback]
PicamAdvanced_UnregisterForIsRelevantChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForIsRelevantChanged
PicamAdvanced_UnregisterForIsRelevantChanged.restype = PicamError
PicamAdvanced_UnregisterForIsRelevantChanged.argtypes = [PicamHandle, PicamParameter, PicamIsRelevantChangedCallback]
PicamValueAccessChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, PicamValueAccess))
PicamAdvanced_RegisterForValueAccessChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForValueAccessChanged
PicamAdvanced_RegisterForValueAccessChanged.restype = PicamError
PicamAdvanced_RegisterForValueAccessChanged.argtypes = [PicamHandle, PicamParameter, PicamValueAccessChangedCallback]
PicamAdvanced_UnregisterForValueAccessChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForValueAccessChanged
PicamAdvanced_UnregisterForValueAccessChanged.restype = PicamError
PicamAdvanced_UnregisterForValueAccessChanged.argtypes = [PicamHandle, PicamParameter, PicamValueAccessChangedCallback]

# values for enumeration 'PicamDynamicsMask'
PicamDynamicsMask_None = 0
PicamDynamicsMask_Value = 1
PicamDynamicsMask_ValueAccess = 2
PicamDynamicsMask_IsRelevant = 4
PicamDynamicsMask_Constraint = 8
PicamDynamicsMask = ctypes.c_int # enum
PicamAdvanced_GetParameterDynamics = _libraries['libpicam.so.0'].PicamAdvanced_GetParameterDynamics
PicamAdvanced_GetParameterDynamics.restype = PicamError
PicamAdvanced_GetParameterDynamics.argtypes = [PicamHandle, PicamParameter, POINTER_T(PicamDynamicsMask)]
PicamAdvanced_GetParameterExtrinsicDynamics = _libraries['libpicam.so.0'].PicamAdvanced_GetParameterExtrinsicDynamics
PicamAdvanced_GetParameterExtrinsicDynamics.restype = PicamError
PicamAdvanced_GetParameterExtrinsicDynamics.argtypes = [PicamHandle, PicamParameter, POINTER_T(PicamDynamicsMask)]
PicamAdvanced_GetParameterCollectionConstraints = _libraries['libpicam.so.0'].PicamAdvanced_GetParameterCollectionConstraints
PicamAdvanced_GetParameterCollectionConstraints.restype = PicamError
PicamAdvanced_GetParameterCollectionConstraints.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamCollectionConstraint)), POINTER_T(ctypes.c_int32)]
PicamDependentCollectionConstraintChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, POINTER_T(struct_PicamCollectionConstraint)))
PicamAdvanced_RegisterForDependentCollectionConstraintChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForDependentCollectionConstraintChanged
PicamAdvanced_RegisterForDependentCollectionConstraintChanged.restype = PicamError
PicamAdvanced_RegisterForDependentCollectionConstraintChanged.argtypes = [PicamHandle, PicamParameter, PicamDependentCollectionConstraintChangedCallback]
PicamAdvanced_UnregisterForDependentCollectionConstraintChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForDependentCollectionConstraintChanged
PicamAdvanced_UnregisterForDependentCollectionConstraintChanged.restype = PicamError
PicamAdvanced_UnregisterForDependentCollectionConstraintChanged.argtypes = [PicamHandle, PicamParameter, PicamDependentCollectionConstraintChangedCallback]
PicamAdvanced_GetParameterRangeConstraints = _libraries['libpicam.so.0'].PicamAdvanced_GetParameterRangeConstraints
PicamAdvanced_GetParameterRangeConstraints.restype = PicamError
PicamAdvanced_GetParameterRangeConstraints.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamRangeConstraint)), POINTER_T(ctypes.c_int32)]
PicamDependentRangeConstraintChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, POINTER_T(struct_PicamRangeConstraint)))
PicamAdvanced_RegisterForDependentRangeConstraintChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForDependentRangeConstraintChanged
PicamAdvanced_RegisterForDependentRangeConstraintChanged.restype = PicamError
PicamAdvanced_RegisterForDependentRangeConstraintChanged.argtypes = [PicamHandle, PicamParameter, PicamDependentRangeConstraintChangedCallback]
PicamAdvanced_UnregisterForDependentRangeConstraintChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForDependentRangeConstraintChanged
PicamAdvanced_UnregisterForDependentRangeConstraintChanged.restype = PicamError
PicamAdvanced_UnregisterForDependentRangeConstraintChanged.argtypes = [PicamHandle, PicamParameter, PicamDependentRangeConstraintChangedCallback]
PicamAdvanced_GetParameterRoisConstraints = _libraries['libpicam.so.0'].PicamAdvanced_GetParameterRoisConstraints
PicamAdvanced_GetParameterRoisConstraints.restype = PicamError
PicamAdvanced_GetParameterRoisConstraints.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamRoisConstraint)), POINTER_T(ctypes.c_int32)]
PicamDependentRoisConstraintChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, POINTER_T(struct_PicamRoisConstraint)))
PicamAdvanced_RegisterForDependentRoisConstraintChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForDependentRoisConstraintChanged
PicamAdvanced_RegisterForDependentRoisConstraintChanged.restype = PicamError
PicamAdvanced_RegisterForDependentRoisConstraintChanged.argtypes = [PicamHandle, PicamParameter, PicamDependentRoisConstraintChangedCallback]
PicamAdvanced_UnregisterForDependentRoisConstraintChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForDependentRoisConstraintChanged
PicamAdvanced_UnregisterForDependentRoisConstraintChanged.restype = PicamError
PicamAdvanced_UnregisterForDependentRoisConstraintChanged.argtypes = [PicamHandle, PicamParameter, PicamDependentRoisConstraintChangedCallback]
PicamAdvanced_GetParameterPulseConstraints = _libraries['libpicam.so.0'].PicamAdvanced_GetParameterPulseConstraints
PicamAdvanced_GetParameterPulseConstraints.restype = PicamError
PicamAdvanced_GetParameterPulseConstraints.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamPulseConstraint)), POINTER_T(ctypes.c_int32)]
PicamDependentPulseConstraintChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, POINTER_T(struct_PicamPulseConstraint)))
PicamAdvanced_RegisterForDependentPulseConstraintChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForDependentPulseConstraintChanged
PicamAdvanced_RegisterForDependentPulseConstraintChanged.restype = PicamError
PicamAdvanced_RegisterForDependentPulseConstraintChanged.argtypes = [PicamHandle, PicamParameter, PicamDependentPulseConstraintChangedCallback]
PicamAdvanced_UnregisterForDependentPulseConstraintChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForDependentPulseConstraintChanged
PicamAdvanced_UnregisterForDependentPulseConstraintChanged.restype = PicamError
PicamAdvanced_UnregisterForDependentPulseConstraintChanged.argtypes = [PicamHandle, PicamParameter, PicamDependentPulseConstraintChangedCallback]
PicamAdvanced_GetParameterModulationsConstraints = _libraries['libpicam.so.0'].PicamAdvanced_GetParameterModulationsConstraints
PicamAdvanced_GetParameterModulationsConstraints.restype = PicamError
PicamAdvanced_GetParameterModulationsConstraints.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamModulationsConstraint)), POINTER_T(ctypes.c_int32)]
PicamDependentModulationsConstraintChangedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamParameter, POINTER_T(struct_PicamModulationsConstraint)))
PicamAdvanced_RegisterForDependentModulationsConstraintChanged = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForDependentModulationsConstraintChanged
PicamAdvanced_RegisterForDependentModulationsConstraintChanged.restype = PicamError
PicamAdvanced_RegisterForDependentModulationsConstraintChanged.argtypes = [PicamHandle, PicamParameter, PicamDependentModulationsConstraintChangedCallback]
PicamAdvanced_UnregisterForDependentModulationsConstraintChanged = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForDependentModulationsConstraintChanged
PicamAdvanced_UnregisterForDependentModulationsConstraintChanged.restype = PicamError
PicamAdvanced_UnregisterForDependentModulationsConstraintChanged.argtypes = [PicamHandle, PicamParameter, PicamDependentModulationsConstraintChangedCallback]
class struct_PicamValidationResult(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('is_valid', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('failed_parameter', POINTER_T(PicamParameter)),
    ('failed_error_constraint_scope', POINTER_T(PicamConstraintScope)),
    ('failed_warning_constraint_scope', POINTER_T(PicamConstraintScope)),
    ('error_constraining_parameter_array', POINTER_T(PicamParameter)),
    ('error_constraining_parameter_count', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('warning_constraining_parameter_array', POINTER_T(PicamParameter)),
    ('warning_constraining_parameter_count', ctypes.c_int32),
    ('PADDING_2', ctypes.c_ubyte * 4),
     ]

PicamValidationResult = struct_PicamValidationResult
Picam_DestroyValidationResult = _libraries['libpicam.so.0'].Picam_DestroyValidationResult
Picam_DestroyValidationResult.restype = PicamError
Picam_DestroyValidationResult.argtypes = [POINTER_T(struct_PicamValidationResult)]
class struct_PicamValidationResults(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('is_valid', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('validation_result_array', POINTER_T(struct_PicamValidationResult)),
    ('validation_result_count', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
     ]

PicamValidationResults = struct_PicamValidationResults
Picam_DestroyValidationResults = _libraries['libpicam.so.0'].Picam_DestroyValidationResults
Picam_DestroyValidationResults.restype = PicamError
Picam_DestroyValidationResults.argtypes = [POINTER_T(struct_PicamValidationResults)]
PicamAdvanced_ValidateParameter = _libraries['libpicam.so.0'].PicamAdvanced_ValidateParameter
PicamAdvanced_ValidateParameter.restype = PicamError
PicamAdvanced_ValidateParameter.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamValidationResult))]
PicamAdvanced_ValidateParameters = _libraries['libpicam.so.0'].PicamAdvanced_ValidateParameters
PicamAdvanced_ValidateParameters.restype = PicamError
PicamAdvanced_ValidateParameters.argtypes = [PicamHandle, POINTER_T(POINTER_T(struct_PicamValidationResults))]
class struct_PicamFailedDependentParameter(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('failed_parameter', PicamParameter),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('failed_error_constraint_scope', POINTER_T(PicamConstraintScope)),
    ('failed_warning_constraint_scope', POINTER_T(PicamConstraintScope)),
     ]

PicamFailedDependentParameter = struct_PicamFailedDependentParameter
class struct_PicamDependentValidationResult(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('is_valid', ctypes.c_int32),
    ('constraining_parameter', PicamParameter),
    ('failed_dependent_parameter_array', POINTER_T(struct_PicamFailedDependentParameter)),
    ('failed_dependent_parameter_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

PicamDependentValidationResult = struct_PicamDependentValidationResult
Picam_DestroyDependentValidationResult = _libraries['libpicam.so.0'].Picam_DestroyDependentValidationResult
Picam_DestroyDependentValidationResult.restype = PicamError
Picam_DestroyDependentValidationResult.argtypes = [POINTER_T(struct_PicamDependentValidationResult)]
PicamAdvanced_ValidateDependentParameter = _libraries['libpicam.so.0'].PicamAdvanced_ValidateDependentParameter
PicamAdvanced_ValidateDependentParameter.restype = PicamError
PicamAdvanced_ValidateDependentParameter.argtypes = [PicamHandle, PicamParameter, POINTER_T(POINTER_T(struct_PicamDependentValidationResult))]
PicamAdvanced_CommitParametersToCameraDevice = _libraries['libpicam.so.0'].PicamAdvanced_CommitParametersToCameraDevice
PicamAdvanced_CommitParametersToCameraDevice.restype = PicamError
PicamAdvanced_CommitParametersToCameraDevice.argtypes = [PicamHandle]
PicamAdvanced_RefreshParameterFromCameraDevice = _libraries['libpicam.so.0'].PicamAdvanced_RefreshParameterFromCameraDevice
PicamAdvanced_RefreshParameterFromCameraDevice.restype = PicamError
PicamAdvanced_RefreshParameterFromCameraDevice.argtypes = [PicamHandle, PicamParameter]
PicamAdvanced_RefreshParametersFromCameraDevice = _libraries['libpicam.so.0'].PicamAdvanced_RefreshParametersFromCameraDevice
PicamAdvanced_RefreshParametersFromCameraDevice.restype = PicamError
PicamAdvanced_RefreshParametersFromCameraDevice.argtypes = [PicamHandle]
class struct_PicamAcquisitionBuffer(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('memory', POINTER_T(None)),
    ('memory_size', ctypes.c_int64),
     ]

PicamAcquisitionBuffer = struct_PicamAcquisitionBuffer
PicamAdvanced_GetAcquisitionBuffer = _libraries['libpicam.so.0'].PicamAdvanced_GetAcquisitionBuffer
PicamAdvanced_GetAcquisitionBuffer.restype = PicamError
PicamAdvanced_GetAcquisitionBuffer.argtypes = [PicamHandle, POINTER_T(struct_PicamAcquisitionBuffer)]
PicamAdvanced_SetAcquisitionBuffer = _libraries['libpicam.so.0'].PicamAdvanced_SetAcquisitionBuffer
PicamAdvanced_SetAcquisitionBuffer.restype = PicamError
PicamAdvanced_SetAcquisitionBuffer.argtypes = [PicamHandle, POINTER_T(struct_PicamAcquisitionBuffer)]
PicamAcquisitionUpdatedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), POINTER_T(struct_PicamAvailableData), POINTER_T(struct_PicamAcquisitionStatus)))
PicamAdvanced_RegisterForAcquisitionUpdated = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForAcquisitionUpdated
PicamAdvanced_RegisterForAcquisitionUpdated.restype = PicamError
PicamAdvanced_RegisterForAcquisitionUpdated.argtypes = [PicamHandle, PicamAcquisitionUpdatedCallback]
PicamAdvanced_UnregisterForAcquisitionUpdated = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForAcquisitionUpdated
PicamAdvanced_UnregisterForAcquisitionUpdated.restype = PicamError
PicamAdvanced_UnregisterForAcquisitionUpdated.argtypes = [PicamHandle, PicamAcquisitionUpdatedCallback]

# values for enumeration 'PicamAcquisitionState'
PicamAcquisitionState_ReadoutStarted = 1
PicamAcquisitionState_ReadoutEnded = 2
PicamAcquisitionState = ctypes.c_int # enum

# values for enumeration 'PicamAcquisitionStateErrorsMask'
PicamAcquisitionStateErrorsMask_None = 0
PicamAcquisitionStateErrorsMask_LostCount = 1
PicamAcquisitionStateErrorsMask = ctypes.c_int # enum
PicamAdvanced_CanRegisterForAcquisitionStateUpdated = _libraries['libpicam.so.0'].PicamAdvanced_CanRegisterForAcquisitionStateUpdated
PicamAdvanced_CanRegisterForAcquisitionStateUpdated.restype = PicamError
PicamAdvanced_CanRegisterForAcquisitionStateUpdated.argtypes = [PicamHandle, PicamAcquisitionState, POINTER_T(ctypes.c_int32)]
class struct_PicamAcquisitionStateCounters(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('readout_started_count', ctypes.c_int64),
    ('readout_ended_count', ctypes.c_int64),
     ]

PicamAcquisitionStateCounters = struct_PicamAcquisitionStateCounters
PicamAcquisitionStateUpdatedCallback = POINTER_T(ctypes.CFUNCTYPE(PicamError, POINTER_T(None), PicamAcquisitionState, POINTER_T(struct_PicamAcquisitionStateCounters), PicamAcquisitionStateErrorsMask))
PicamAdvanced_RegisterForAcquisitionStateUpdated = _libraries['libpicam.so.0'].PicamAdvanced_RegisterForAcquisitionStateUpdated
PicamAdvanced_RegisterForAcquisitionStateUpdated.restype = PicamError
PicamAdvanced_RegisterForAcquisitionStateUpdated.argtypes = [PicamHandle, PicamAcquisitionState, PicamAcquisitionStateUpdatedCallback]
PicamAdvanced_UnregisterForAcquisitionStateUpdated = _libraries['libpicam.so.0'].PicamAdvanced_UnregisterForAcquisitionStateUpdated
PicamAdvanced_UnregisterForAcquisitionStateUpdated.restype = PicamError
PicamAdvanced_UnregisterForAcquisitionStateUpdated.argtypes = [PicamHandle, PicamAcquisitionState, PicamAcquisitionStateUpdatedCallback]
PicamAdvanced_HasAcquisitionBufferOverrun = _libraries['libpicam.so.0'].PicamAdvanced_HasAcquisitionBufferOverrun
PicamAdvanced_HasAcquisitionBufferOverrun.restype = PicamError
PicamAdvanced_HasAcquisitionBufferOverrun.argtypes = [PicamHandle, POINTER_T(ctypes.c_int32)]
PicamAdvanced_CanClearReadoutCountOnline = _libraries['libpicam.so.0'].PicamAdvanced_CanClearReadoutCountOnline
PicamAdvanced_CanClearReadoutCountOnline.restype = PicamError
PicamAdvanced_CanClearReadoutCountOnline.argtypes = [PicamHandle, POINTER_T(ctypes.c_int32)]
PicamAdvanced_ClearReadoutCountOnline = _libraries['libpicam.so.0'].PicamAdvanced_ClearReadoutCountOnline
PicamAdvanced_ClearReadoutCountOnline.restype = PicamError
PicamAdvanced_ClearReadoutCountOnline.argtypes = [PicamHandle, POINTER_T(ctypes.c_int32)]
PicamEMCalibration_OpenCalibration = _libraries['libpicam.so.0'].PicamEMCalibration_OpenCalibration
PicamEMCalibration_OpenCalibration.restype = PicamError
PicamEMCalibration_OpenCalibration.argtypes = [POINTER_T(struct_PicamCameraID), POINTER_T(POINTER_T(None))]
PicamEMCalibration_CloseCalibration = _libraries['libpicam.so.0'].PicamEMCalibration_CloseCalibration
PicamEMCalibration_CloseCalibration.restype = PicamError
PicamEMCalibration_CloseCalibration.argtypes = [PicamHandle]
PicamEMCalibration_GetOpenCalibrations = _libraries['libpicam.so.0'].PicamEMCalibration_GetOpenCalibrations
PicamEMCalibration_GetOpenCalibrations.restype = PicamError
PicamEMCalibration_GetOpenCalibrations.argtypes = [POINTER_T(POINTER_T(POINTER_T(None))), POINTER_T(ctypes.c_int32)]
PicamEMCalibration_GetCameraID = _libraries['libpicam.so.0'].PicamEMCalibration_GetCameraID
PicamEMCalibration_GetCameraID.restype = PicamError
PicamEMCalibration_GetCameraID.argtypes = [PicamHandle, POINTER_T(struct_PicamCameraID)]
class struct_PicamEMCalibrationDate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('year', ctypes.c_int32),
    ('month', ctypes.c_int32),
    ('day', ctypes.c_int32),
     ]

PicamEMCalibrationDate = struct_PicamEMCalibrationDate
PicamEMCalibration_GetCalibrationDate = _libraries['libpicam.so.0'].PicamEMCalibration_GetCalibrationDate
PicamEMCalibration_GetCalibrationDate.restype = PicamError
PicamEMCalibration_GetCalibrationDate.argtypes = [PicamHandle, POINTER_T(struct_PicamEMCalibrationDate)]
PicamEMCalibration_ReadSensorTemperatureReading = _libraries['libpicam.so.0'].PicamEMCalibration_ReadSensorTemperatureReading
PicamEMCalibration_ReadSensorTemperatureReading.restype = PicamError
PicamEMCalibration_ReadSensorTemperatureReading.argtypes = [PicamHandle, POINTER_T(ctypes.c_double)]
PicamEMCalibration_ReadSensorTemperatureStatus = _libraries['libpicam.so.0'].PicamEMCalibration_ReadSensorTemperatureStatus
PicamEMCalibration_ReadSensorTemperatureStatus.restype = PicamError
PicamEMCalibration_ReadSensorTemperatureStatus.argtypes = [PicamHandle, POINTER_T(PicamSensorTemperatureStatus)]
PicamEMCalibration_GetSensorTemperatureSetPoint = _libraries['libpicam.so.0'].PicamEMCalibration_GetSensorTemperatureSetPoint
PicamEMCalibration_GetSensorTemperatureSetPoint.restype = PicamError
PicamEMCalibration_GetSensorTemperatureSetPoint.argtypes = [PicamHandle, POINTER_T(ctypes.c_double)]
PicamEMCalibration_SetSensorTemperatureSetPoint = _libraries['libpicam.so.0'].PicamEMCalibration_SetSensorTemperatureSetPoint
PicamEMCalibration_SetSensorTemperatureSetPoint.restype = PicamError
PicamEMCalibration_SetSensorTemperatureSetPoint.argtypes = [PicamHandle, piflt]
PicamEMCalibration_GetSensorTemperatureSetPointConstraint = _libraries['libpicam.so.0'].PicamEMCalibration_GetSensorTemperatureSetPointConstraint
PicamEMCalibration_GetSensorTemperatureSetPointConstraint.restype = PicamError
PicamEMCalibration_GetSensorTemperatureSetPointConstraint.argtypes = [PicamHandle, POINTER_T(POINTER_T(struct_PicamRangeConstraint))]
PicamEMCalibrationCallback = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_int32, POINTER_T(None), ctypes.c_double, POINTER_T(None)))
PicamEMCalibration_Calibrate = _libraries['libpicam.so.0'].PicamEMCalibration_Calibrate
PicamEMCalibration_Calibrate.restype = PicamError
PicamEMCalibration_Calibrate.argtypes = [PicamHandle, PicamEMCalibrationCallback, POINTER_T(None)]
PicamSpecial_CanEraseResidual = _libraries['libpicam.so.0'].PicamSpecial_CanEraseResidual
PicamSpecial_CanEraseResidual.restype = PicamError
PicamSpecial_CanEraseResidual.argtypes = [PicamHandle, POINTER_T(ctypes.c_int32)]
PicamSpecial_EraseResidual = _libraries['libpicam.so.0'].PicamSpecial_EraseResidual
PicamSpecial_EraseResidual.restype = PicamError
PicamSpecial_EraseResidual.argtypes = [PicamHandle]
pibln = ctypes.c_int32
pichar = ctypes.c_char
pibyte = ctypes.c_ubyte
pi8s = ctypes.c_byte
pi8u = ctypes.c_ubyte
pi16s = ctypes.c_int16
pi16u = ctypes.c_uint16
pi32s = ctypes.c_int32
pi32u = ctypes.c_uint32
pi64u = ctypes.c_uint64
pi32f = ctypes.c_float
pi64f = ctypes.c_double
__all__ = \
    ['PicamAccessoryDiscoveryCallback', 'PicamAccessoryID',
    'PicamAccessory_CloseAccessory',
    'PicamAccessory_DestroyAccessoryIDs',
    'PicamAccessory_DiscoverAccessories',
    'PicamAccessory_GetAccessoryID',
    'PicamAccessory_GetAvailableAccessoryIDs',
    'PicamAccessory_GetFirmwareDetails',
    'PicamAccessory_GetLightSourceReference',
    'PicamAccessory_GetOpenAccessories',
    'PicamAccessory_GetUnavailableAccessoryIDs',
    'PicamAccessory_IsAccessoryConnected',
    'PicamAccessory_IsAccessoryIDConnected',
    'PicamAccessory_IsAccessoryIDOpenElsewhere',
    'PicamAccessory_IsDiscoveringAccessories',
    'PicamAccessory_OpenAccessory',
    'PicamAccessory_OpenFirstAccessory',
    'PicamAccessory_RegisterForDiscovery',
    'PicamAccessory_StopDiscoveringAccessories',
    'PicamAccessory_UnregisterForDiscovery', 'PicamAcquisitionBuffer',
    'PicamAcquisitionErrorsMask',
    'PicamAcquisitionErrorsMask_CameraFaulted',
    'PicamAcquisitionErrorsMask_ConnectionLost',
    'PicamAcquisitionErrorsMask_DataLost',
    'PicamAcquisitionErrorsMask_DataNotArriving',
    'PicamAcquisitionErrorsMask_None',
    'PicamAcquisitionErrorsMask_ShutterOverheated',
    'PicamAcquisitionState', 'PicamAcquisitionStateCounters',
    'PicamAcquisitionStateErrorsMask',
    'PicamAcquisitionStateErrorsMask_LostCount',
    'PicamAcquisitionStateErrorsMask_None',
    'PicamAcquisitionStateUpdatedCallback',
    'PicamAcquisitionState_ReadoutEnded',
    'PicamAcquisitionState_ReadoutStarted', 'PicamAcquisitionStatus',
    'PicamAcquisitionUpdatedCallback', 'PicamActiveShutter',
    'PicamActiveShutter_External', 'PicamActiveShutter_Internal',
    'PicamActiveShutter_None', 'PicamAdcAnalogGain',
    'PicamAdcAnalogGain_High', 'PicamAdcAnalogGain_Low',
    'PicamAdcAnalogGain_Medium', 'PicamAdcQuality',
    'PicamAdcQuality_ElectronMultiplied',
    'PicamAdcQuality_HighCapacity', 'PicamAdcQuality_HighSpeed',
    'PicamAdcQuality_LowNoise',
    'PicamAdvanced_CanClearReadoutCountOnline',
    'PicamAdvanced_CanRegisterForAcquisitionStateUpdated',
    'PicamAdvanced_CancelNotifyWhenStatusParameterValue',
    'PicamAdvanced_ClearReadoutCountOnline',
    'PicamAdvanced_CloseCameraDevice',
    'PicamAdvanced_CommitParametersToCameraDevice',
    'PicamAdvanced_DestroyPixelDefectMaps',
    'PicamAdvanced_DiscoverCameras',
    'PicamAdvanced_GetAcquisitionBuffer',
    'PicamAdvanced_GetCameraDevice', 'PicamAdvanced_GetCameraModel',
    'PicamAdvanced_GetHandleType',
    'PicamAdvanced_GetOpenCameraDevices',
    'PicamAdvanced_GetParameterCollectionConstraints',
    'PicamAdvanced_GetParameterDynamics',
    'PicamAdvanced_GetParameterExtrinsicDynamics',
    'PicamAdvanced_GetParameterModulationsConstraints',
    'PicamAdvanced_GetParameterPulseConstraints',
    'PicamAdvanced_GetParameterRangeConstraints',
    'PicamAdvanced_GetParameterRoisConstraints',
    'PicamAdvanced_GetPixelDefectMap', 'PicamAdvanced_GetUserState',
    'PicamAdvanced_HasAcquisitionBufferOverrun',
    'PicamAdvanced_IsDiscoveringCameras',
    'PicamAdvanced_NotifyWhenStatusParameterValue',
    'PicamAdvanced_OpenCameraDevice',
    'PicamAdvanced_RefreshParameterFromCameraDevice',
    'PicamAdvanced_RefreshParametersFromCameraDevice',
    'PicamAdvanced_RegisterForAcquisitionStateUpdated',
    'PicamAdvanced_RegisterForAcquisitionUpdated',
    'PicamAdvanced_RegisterForDependentCollectionConstraintChanged',
    'PicamAdvanced_RegisterForDependentModulationsConstraintChanged',
    'PicamAdvanced_RegisterForDependentPulseConstraintChanged',
    'PicamAdvanced_RegisterForDependentRangeConstraintChanged',
    'PicamAdvanced_RegisterForDependentRoisConstraintChanged',
    'PicamAdvanced_RegisterForDiscovery',
    'PicamAdvanced_RegisterForExtrinsicFloatingPointValueChanged',
    'PicamAdvanced_RegisterForExtrinsicIntegerValueChanged',
    'PicamAdvanced_RegisterForFloatingPointValueChanged',
    'PicamAdvanced_RegisterForIntegerValueChanged',
    'PicamAdvanced_RegisterForIsRelevantChanged',
    'PicamAdvanced_RegisterForLargeIntegerValueChanged',
    'PicamAdvanced_RegisterForModulationsValueChanged',
    'PicamAdvanced_RegisterForPulseValueChanged',
    'PicamAdvanced_RegisterForRoisValueChanged',
    'PicamAdvanced_RegisterForValueAccessChanged',
    'PicamAdvanced_SetAcquisitionBuffer',
    'PicamAdvanced_SetUserState',
    'PicamAdvanced_StopDiscoveringCameras',
    'PicamAdvanced_UnregisterForAcquisitionStateUpdated',
    'PicamAdvanced_UnregisterForAcquisitionUpdated',
    'PicamAdvanced_UnregisterForDependentCollectionConstraintChanged',
    'PicamAdvanced_UnregisterForDependentModulationsConstraintChanged',
    'PicamAdvanced_UnregisterForDependentPulseConstraintChanged',
    'PicamAdvanced_UnregisterForDependentRangeConstraintChanged',
    'PicamAdvanced_UnregisterForDependentRoisConstraintChanged',
    'PicamAdvanced_UnregisterForDiscovery',
    'PicamAdvanced_UnregisterForExtrinsicFloatingPointValueChanged',
    'PicamAdvanced_UnregisterForExtrinsicIntegerValueChanged',
    'PicamAdvanced_UnregisterForFloatingPointValueChanged',
    'PicamAdvanced_UnregisterForIntegerValueChanged',
    'PicamAdvanced_UnregisterForIsRelevantChanged',
    'PicamAdvanced_UnregisterForLargeIntegerValueChanged',
    'PicamAdvanced_UnregisterForModulationsValueChanged',
    'PicamAdvanced_UnregisterForPulseValueChanged',
    'PicamAdvanced_UnregisterForRoisValueChanged',
    'PicamAdvanced_UnregisterForValueAccessChanged',
    'PicamAdvanced_ValidateDependentParameter',
    'PicamAdvanced_ValidateParameter',
    'PicamAdvanced_ValidateParameters', 'PicamAvailableData',
    'PicamCalibration', 'PicamCalibrationPoint', 'PicamCameraID',
    'PicamCcdCharacteristicsMask',
    'PicamCcdCharacteristicsMask_AdvancedInvertedMode',
    'PicamCcdCharacteristicsMask_BackIlluminated',
    'PicamCcdCharacteristicsMask_DeepDepleted',
    'PicamCcdCharacteristicsMask_ExcelonEnabled',
    'PicamCcdCharacteristicsMask_HighResistivity',
    'PicamCcdCharacteristicsMask_Multiport',
    'PicamCcdCharacteristicsMask_None',
    'PicamCcdCharacteristicsMask_OpenElectrode',
    'PicamCcdCharacteristicsMask_SecondaryMask',
    'PicamCcdCharacteristicsMask_UVEnhanced',
    'PicamCenterWavelengthStatus',
    'PicamCenterWavelengthStatus_Faulted',
    'PicamCenterWavelengthStatus_Moving',
    'PicamCenterWavelengthStatus_Stationary',
    'PicamCollectionConstraint', 'PicamColumnDefect',
    'PicamComputerInterface', 'PicamComputerInterface_1394A',
    'PicamComputerInterface_GigabitEthernet',
    'PicamComputerInterface_Usb2', 'PicamComputerInterface_Usb3',
    'PicamConstraintCategory', 'PicamConstraintCategory_Capable',
    'PicamConstraintCategory_Recommended',
    'PicamConstraintCategory_Required', 'PicamConstraintScope',
    'PicamConstraintScope_Dependent',
    'PicamConstraintScope_Independent', 'PicamConstraintSeverity',
    'PicamConstraintSeverity_Error',
    'PicamConstraintSeverity_Warning', 'PicamConstraintType',
    'PicamConstraintType_Collection',
    'PicamConstraintType_Modulations', 'PicamConstraintType_None',
    'PicamConstraintType_Pulse', 'PicamConstraintType_Range',
    'PicamConstraintType_Rois', 'PicamCoolingFanStatus',
    'PicamCoolingFanStatus_ForcedOn', 'PicamCoolingFanStatus_Off',
    'PicamCoolingFanStatus_On',
    'PicamDependentCollectionConstraintChangedCallback',
    'PicamDependentModulationsConstraintChangedCallback',
    'PicamDependentPulseConstraintChangedCallback',
    'PicamDependentRangeConstraintChangedCallback',
    'PicamDependentRoisConstraintChangedCallback',
    'PicamDependentValidationResult', 'PicamDiscoveryAction',
    'PicamDiscoveryAction_Faulted', 'PicamDiscoveryAction_Found',
    'PicamDiscoveryAction_Lost', 'PicamDiscoveryCallback',
    'PicamDynamicsMask', 'PicamDynamicsMask_Constraint',
    'PicamDynamicsMask_IsRelevant', 'PicamDynamicsMask_None',
    'PicamDynamicsMask_Value', 'PicamDynamicsMask_ValueAccess',
    'PicamEMCalibrationCallback', 'PicamEMCalibrationDate',
    'PicamEMCalibration_Calibrate',
    'PicamEMCalibration_CloseCalibration',
    'PicamEMCalibration_GetCalibrationDate',
    'PicamEMCalibration_GetCameraID',
    'PicamEMCalibration_GetOpenCalibrations',
    'PicamEMCalibration_GetSensorTemperatureSetPoint',
    'PicamEMCalibration_GetSensorTemperatureSetPointConstraint',
    'PicamEMCalibration_OpenCalibration',
    'PicamEMCalibration_ReadSensorTemperatureReading',
    'PicamEMCalibration_ReadSensorTemperatureStatus',
    'PicamEMCalibration_SetSensorTemperatureSetPoint',
    'PicamEMIccdGainControlMode', 'PicamEMIccdGainControlMode_Manual',
    'PicamEMIccdGainControlMode_Optimal', 'PicamEnumeratedType',
    'PicamEnumeratedType_AcquisitionErrorsMask',
    'PicamEnumeratedType_AcquisitionState',
    'PicamEnumeratedType_AcquisitionStateErrorsMask',
    'PicamEnumeratedType_ActiveShutter',
    'PicamEnumeratedType_AdcAnalogGain',
    'PicamEnumeratedType_AdcQuality',
    'PicamEnumeratedType_CcdCharacteristicsMask',
    'PicamEnumeratedType_CenterWavelengthStatus',
    'PicamEnumeratedType_ComputerInterface',
    'PicamEnumeratedType_ConstraintCategory',
    'PicamEnumeratedType_ConstraintScope',
    'PicamEnumeratedType_ConstraintSeverity',
    'PicamEnumeratedType_ConstraintType',
    'PicamEnumeratedType_CoolingFanStatus',
    'PicamEnumeratedType_DiscoveryAction',
    'PicamEnumeratedType_DynamicsMask',
    'PicamEnumeratedType_EMIccdGainControlMode',
    'PicamEnumeratedType_EnumeratedType', 'PicamEnumeratedType_Error',
    'PicamEnumeratedType_GateTrackingMask',
    'PicamEnumeratedType_GatingMode',
    'PicamEnumeratedType_GatingSpeed',
    'PicamEnumeratedType_GratingCoating',
    'PicamEnumeratedType_GratingType',
    'PicamEnumeratedType_HandleType',
    'PicamEnumeratedType_IntensifierOptionsMask',
    'PicamEnumeratedType_IntensifierStatus',
    'PicamEnumeratedType_LaserOutputMode',
    'PicamEnumeratedType_LaserStatus',
    'PicamEnumeratedType_LightSource',
    'PicamEnumeratedType_LightSourceStatus',
    'PicamEnumeratedType_Model',
    'PicamEnumeratedType_ModulationTrackingMask',
    'PicamEnumeratedType_OrientationMask',
    'PicamEnumeratedType_OutputSignal',
    'PicamEnumeratedType_Parameter',
    'PicamEnumeratedType_PhosphorType',
    'PicamEnumeratedType_PhotocathodeSensitivity',
    'PicamEnumeratedType_PhotonDetectionMode',
    'PicamEnumeratedType_PixelFormat',
    'PicamEnumeratedType_ReadoutControlMode',
    'PicamEnumeratedType_RoisConstraintRulesMask',
    'PicamEnumeratedType_SensorTemperatureStatus',
    'PicamEnumeratedType_SensorType',
    'PicamEnumeratedType_ShutterStatus',
    'PicamEnumeratedType_ShutterTimingMode',
    'PicamEnumeratedType_ShutterType',
    'PicamEnumeratedType_TimeStampsMask',
    'PicamEnumeratedType_TriggerCoupling',
    'PicamEnumeratedType_TriggerDetermination',
    'PicamEnumeratedType_TriggerResponse',
    'PicamEnumeratedType_TriggerSource',
    'PicamEnumeratedType_TriggerStatus',
    'PicamEnumeratedType_TriggerTermination',
    'PicamEnumeratedType_VacuumStatus',
    'PicamEnumeratedType_ValueAccess',
    'PicamEnumeratedType_ValueType', 'PicamError',
    'PicamError_AccessoryAlreadyOpened',
    'PicamError_AcquisitionInProgress',
    'PicamError_AcquisitionNotInProgress',
    'PicamError_AcquisitionUpdatedHandlerRegistered',
    'PicamError_AlreadyDiscoveringAccessories',
    'PicamError_AlreadyDiscoveringCameras',
    'PicamError_CameraAlreadyOpened', 'PicamError_CameraFaulted',
    'PicamError_CenterWavelengthFaulted',
    'PicamError_DemoAlreadyConnected', 'PicamError_DemoNotSupported',
    'PicamError_DeviceCommunicationFailed',
    'PicamError_DeviceDisconnected', 'PicamError_DeviceOpenElsewhere',
    'PicamError_EnumerationValueNotDefined',
    'PicamError_InsufficientMemory', 'PicamError_InvalidAccessoryID',
    'PicamError_InvalidAcquisitionBuffer',
    'PicamError_InvalidAcquisitionState',
    'PicamError_InvalidCameraID',
    'PicamError_InvalidConstraintCategory', 'PicamError_InvalidCount',
    'PicamError_InvalidDemoModel',
    'PicamError_InvalidDemoSerialNumber',
    'PicamError_InvalidEnumeratedType', 'PicamError_InvalidHandle',
    'PicamError_InvalidOperation', 'PicamError_InvalidParameterValue',
    'PicamError_InvalidParameterValues', 'PicamError_InvalidPointer',
    'PicamError_InvalidReadoutCount',
    'PicamError_InvalidReadoutTimeOut',
    'PicamError_InvalidWaitableStatusParameterTimeOut',
    'PicamError_LibraryAlreadyInitialized',
    'PicamError_LibraryNotInitialized',
    'PicamError_NoAccessoriesAvailable',
    'PicamError_NoCamerasAvailable',
    'PicamError_NondestructiveReadoutEnabled', 'PicamError_None',
    'PicamError_NotDiscoveringAccessories',
    'PicamError_NotDiscoveringCameras',
    'PicamError_OperationCanceled',
    'PicamError_ParameterDoesNotExist',
    'PicamError_ParameterHasInvalidConstraintType',
    'PicamError_ParameterHasInvalidValueType',
    'PicamError_ParameterIsNotOnlineable',
    'PicamError_ParameterIsNotReadable',
    'PicamError_ParameterIsNotWaitableStatus',
    'PicamError_ParameterValueIsIrrelevant',
    'PicamError_ParameterValueIsReadOnly',
    'PicamError_ParametersNotCommitted',
    'PicamError_ShutterOverheated', 'PicamError_TimeOutOccurred',
    'PicamError_UnexpectedError', 'PicamError_UnexpectedNullPointer',
    'PicamFailedDependentParameter', 'PicamFirmwareDetail',
    'PicamFloatingPointValueChangedCallback', 'PicamGateTrackingMask',
    'PicamGateTrackingMask_Delay', 'PicamGateTrackingMask_None',
    'PicamGateTrackingMask_Width', 'PicamGatingMode',
    'PicamGatingMode_Custom', 'PicamGatingMode_Disabled',
    'PicamGatingMode_Repetitive', 'PicamGatingMode_Sequential',
    'PicamGatingSpeed', 'PicamGatingSpeed_Fast',
    'PicamGatingSpeed_Slow', 'PicamGratingCoating',
    'PicamGratingCoating_Ag', 'PicamGratingCoating_Al',
    'PicamGratingCoating_AlMgF2', 'PicamGratingCoating_Au',
    'PicamGratingType', 'PicamGratingType_HolographicNir',
    'PicamGratingType_HolographicUV',
    'PicamGratingType_HolographicVisible', 'PicamGratingType_Mirror',
    'PicamGratingType_Ruled', 'PicamHandle', 'PicamHandleType',
    'PicamHandleType_Accessory', 'PicamHandleType_CameraDevice',
    'PicamHandleType_CameraModel', 'PicamHandleType_EMCalibration',
    'PicamIntegerValueChangedCallback', 'PicamIntensifierOptionsMask',
    'PicamIntensifierOptionsMask_McpGating',
    'PicamIntensifierOptionsMask_Modulation',
    'PicamIntensifierOptionsMask_None',
    'PicamIntensifierOptionsMask_SubNanosecondGating',
    'PicamIntensifierStatus', 'PicamIntensifierStatus_PoweredOff',
    'PicamIntensifierStatus_PoweredOn',
    'PicamIsRelevantChangedCallback',
    'PicamLargeIntegerValueChangedCallback', 'PicamLaserOutputMode',
    'PicamLaserOutputMode_ContinuousWave',
    'PicamLaserOutputMode_Disabled', 'PicamLaserOutputMode_Pulsed',
    'PicamLaserStatus', 'PicamLaserStatus_Armed',
    'PicamLaserStatus_Arming', 'PicamLaserStatus_Disarmed',
    'PicamLaserStatus_Unarmed', 'PicamLightSource',
    'PicamLightSourceStatus', 'PicamLightSourceStatus_Stable',
    'PicamLightSourceStatus_Unstable', 'PicamLightSource_Disabled',
    'PicamLightSource_Hg', 'PicamLightSource_NeAr',
    'PicamLightSource_Qth', 'PicamModel', 'PicamModel_Blaze100B',
    'PicamModel_Blaze100BExcelon', 'PicamModel_Blaze100BR',
    'PicamModel_Blaze100BRExcelon', 'PicamModel_Blaze100BRLD',
    'PicamModel_Blaze100BRLDExcelon', 'PicamModel_Blaze100HR',
    'PicamModel_Blaze100HRExcelon', 'PicamModel_Blaze100Series',
    'PicamModel_Blaze400B', 'PicamModel_Blaze400BExcelon',
    'PicamModel_Blaze400BR', 'PicamModel_Blaze400BRExcelon',
    'PicamModel_Blaze400BRLD', 'PicamModel_Blaze400BRLDExcelon',
    'PicamModel_Blaze400HR', 'PicamModel_Blaze400HRExcelon',
    'PicamModel_Blaze400Series', 'PicamModel_BlazeSeries',
    'PicamModel_Fergie256B', 'PicamModel_Fergie256BExcelon',
    'PicamModel_Fergie256BFT', 'PicamModel_Fergie256BFTExcelon',
    'PicamModel_Fergie256BR', 'PicamModel_Fergie256BRExcelon',
    'PicamModel_Fergie256BRFT', 'PicamModel_Fergie256BRFTExcelon',
    'PicamModel_Fergie256FFT', 'PicamModel_Fergie256FTSeries',
    'PicamModel_Fergie256Series', 'PicamModel_FergieAEL',
    'PicamModel_FergieAccessorySeries', 'PicamModel_FergieLampSeries',
    'PicamModel_FergieLaser785', 'PicamModel_FergieLaserSeries',
    'PicamModel_FergieQTH', 'PicamModel_FergieSeries',
    'PicamModel_Kuro1200B', 'PicamModel_Kuro1608B',
    'PicamModel_Kuro2048B', 'PicamModel_KuroSeries',
    'PicamModel_Nirvana640', 'PicamModel_NirvanaLN640',
    'PicamModel_NirvanaLNSeries', 'PicamModel_NirvanaST640',
    'PicamModel_NirvanaSTSeries', 'PicamModel_NirvanaSeries',
    'PicamModel_PIMax31024I', 'PicamModel_PIMax31024x256',
    'PicamModel_PIMax3Series', 'PicamModel_PIMax41024BEM',
    'PicamModel_PIMax41024EM', 'PicamModel_PIMax41024EMSeries',
    'PicamModel_PIMax41024F', 'PicamModel_PIMax41024FRF',
    'PicamModel_PIMax41024FSeries', 'PicamModel_PIMax41024I',
    'PicamModel_PIMax41024IRF', 'PicamModel_PIMax41024ISeries',
    'PicamModel_PIMax41024x256', 'PicamModel_PIMax41024x256RF',
    'PicamModel_PIMax41024x256Series', 'PicamModel_PIMax42048B',
    'PicamModel_PIMax42048BRF', 'PicamModel_PIMax42048F',
    'PicamModel_PIMax42048FRF', 'PicamModel_PIMax42048Series',
    'PicamModel_PIMax4512BEM', 'PicamModel_PIMax4512EM',
    'PicamModel_PIMax4512EMSeries', 'PicamModel_PIMax4Series',
    'PicamModel_PIMte1024B', 'PicamModel_PIMte1024BFT',
    'PicamModel_PIMte1024BR', 'PicamModel_PIMte1024BUV',
    'PicamModel_PIMte1024F', 'PicamModel_PIMte1024FT',
    'PicamModel_PIMte1024FTSeries', 'PicamModel_PIMte1024Series',
    'PicamModel_PIMte1300B', 'PicamModel_PIMte1300BR',
    'PicamModel_PIMte1300R', 'PicamModel_PIMte1300Series',
    'PicamModel_PIMte2048B', 'PicamModel_PIMte2048BR',
    'PicamModel_PIMte2048Series', 'PicamModel_PIMte2KB',
    'PicamModel_PIMte2KBUV', 'PicamModel_PIMte2KSeries',
    'PicamModel_PIMteSeries', 'PicamModel_Pionir640',
    'PicamModel_PionirSeries', 'PicamModel_Pixis100B',
    'PicamModel_Pixis100BExcelon', 'PicamModel_Pixis100BR',
    'PicamModel_Pixis100BRExcelon', 'PicamModel_Pixis100C',
    'PicamModel_Pixis100F', 'PicamModel_Pixis100R',
    'PicamModel_Pixis100Series', 'PicamModel_Pixis1024B',
    'PicamModel_Pixis1024BExcelon', 'PicamModel_Pixis1024BR',
    'PicamModel_Pixis1024BRExcelon', 'PicamModel_Pixis1024BUV',
    'PicamModel_Pixis1024F', 'PicamModel_Pixis1024Series',
    'PicamModel_Pixis1300B', 'PicamModel_Pixis1300BExcelon',
    'PicamModel_Pixis1300BR', 'PicamModel_Pixis1300BRExcelon',
    'PicamModel_Pixis1300F', 'PicamModel_Pixis1300F_2',
    'PicamModel_Pixis1300Series', 'PicamModel_Pixis2048B',
    'PicamModel_Pixis2048BExcelon', 'PicamModel_Pixis2048BR',
    'PicamModel_Pixis2048BRExcelon', 'PicamModel_Pixis2048F',
    'PicamModel_Pixis2048Series', 'PicamModel_Pixis256B',
    'PicamModel_Pixis256BR', 'PicamModel_Pixis256E',
    'PicamModel_Pixis256F', 'PicamModel_Pixis256Series',
    'PicamModel_Pixis2KB', 'PicamModel_Pixis2KBExcelon',
    'PicamModel_Pixis2KBUV', 'PicamModel_Pixis2KF',
    'PicamModel_Pixis2KSeries', 'PicamModel_Pixis400B',
    'PicamModel_Pixis400BExcelon', 'PicamModel_Pixis400BR',
    'PicamModel_Pixis400BRExcelon', 'PicamModel_Pixis400F',
    'PicamModel_Pixis400R', 'PicamModel_Pixis400Series',
    'PicamModel_Pixis512B', 'PicamModel_Pixis512BExcelon',
    'PicamModel_Pixis512BUV', 'PicamModel_Pixis512F',
    'PicamModel_Pixis512Series', 'PicamModel_PixisSeries',
    'PicamModel_PixisXB100B', 'PicamModel_PixisXB100BR',
    'PicamModel_PixisXB1024BR', 'PicamModel_PixisXB1300R',
    'PicamModel_PixisXB256BR', 'PicamModel_PixisXB400BR',
    'PicamModel_PixisXF1024B', 'PicamModel_PixisXF1024F',
    'PicamModel_PixisXF1300B', 'PicamModel_PixisXF2048B',
    'PicamModel_PixisXF2048F', 'PicamModel_PixisXF512B',
    'PicamModel_PixisXF512F', 'PicamModel_PixisXO100B',
    'PicamModel_PixisXO100BR', 'PicamModel_PixisXO1024B',
    'PicamModel_PixisXO1024BR', 'PicamModel_PixisXO1024F',
    'PicamModel_PixisXO1300B', 'PicamModel_PixisXO2048B',
    'PicamModel_PixisXO2KB', 'PicamModel_PixisXO400B',
    'PicamModel_PixisXO512B', 'PicamModel_PixisXO512F',
    'PicamModel_ProEM1024B', 'PicamModel_ProEM1024BExcelon',
    'PicamModel_ProEM1024Series', 'PicamModel_ProEM1600Series',
    'PicamModel_ProEM1600xx2B', 'PicamModel_ProEM1600xx2BExcelon',
    'PicamModel_ProEM1600xx4B', 'PicamModel_ProEM1600xx4BExcelon',
    'PicamModel_ProEM512B', 'PicamModel_ProEM512BExcelon',
    'PicamModel_ProEM512BK', 'PicamModel_ProEM512BKExcelon',
    'PicamModel_ProEM512Series', 'PicamModel_ProEMHS1024B',
    'PicamModel_ProEMHS1024BExcelon',
    'PicamModel_ProEMHS1024BExcelon_2',
    'PicamModel_ProEMHS1024BExcelon_3', 'PicamModel_ProEMHS1024B_2',
    'PicamModel_ProEMHS1024B_3', 'PicamModel_ProEMHS1024Series',
    'PicamModel_ProEMHS1K10Series', 'PicamModel_ProEMHS1KB10',
    'PicamModel_ProEMHS1KB10Excelon', 'PicamModel_ProEMHS512B',
    'PicamModel_ProEMHS512BExcelon',
    'PicamModel_ProEMHS512BExcelon_2', 'PicamModel_ProEMHS512BK',
    'PicamModel_ProEMHS512BKExcelon', 'PicamModel_ProEMHS512B_2',
    'PicamModel_ProEMHS512Series', 'PicamModel_ProEMHSSeries',
    'PicamModel_ProEMPlus1024B', 'PicamModel_ProEMPlus1024BExcelon',
    'PicamModel_ProEMPlus1024Series',
    'PicamModel_ProEMPlus1600Series', 'PicamModel_ProEMPlus1600xx2B',
    'PicamModel_ProEMPlus1600xx2BExcelon',
    'PicamModel_ProEMPlus1600xx4B',
    'PicamModel_ProEMPlus1600xx4BExcelon', 'PicamModel_ProEMPlus512B',
    'PicamModel_ProEMPlus512BExcelon', 'PicamModel_ProEMPlus512BK',
    'PicamModel_ProEMPlus512BKExcelon',
    'PicamModel_ProEMPlus512Series', 'PicamModel_ProEMPlusSeries',
    'PicamModel_ProEMSeries', 'PicamModel_Pylon100B',
    'PicamModel_Pylon100BExcelon', 'PicamModel_Pylon100BR',
    'PicamModel_Pylon100BRExcelon', 'PicamModel_Pylon100F',
    'PicamModel_Pylon100Series', 'PicamModel_Pylon1024B',
    'PicamModel_Pylon1024BExcelon', 'PicamModel_Pylon1024Series',
    'PicamModel_Pylon1300B', 'PicamModel_Pylon1300BExcelon',
    'PicamModel_Pylon1300BR', 'PicamModel_Pylon1300BRExcelon',
    'PicamModel_Pylon1300F', 'PicamModel_Pylon1300R',
    'PicamModel_Pylon1300Series', 'PicamModel_Pylon2048B',
    'PicamModel_Pylon2048BExcelon', 'PicamModel_Pylon2048BR',
    'PicamModel_Pylon2048BRExcelon', 'PicamModel_Pylon2048F',
    'PicamModel_Pylon2048Series', 'PicamModel_Pylon256B',
    'PicamModel_Pylon256BR', 'PicamModel_Pylon256E',
    'PicamModel_Pylon256F', 'PicamModel_Pylon256Series',
    'PicamModel_Pylon2KB', 'PicamModel_Pylon2KBExcelon',
    'PicamModel_Pylon2KBUV', 'PicamModel_Pylon2KF',
    'PicamModel_Pylon2KSeries', 'PicamModel_Pylon400B',
    'PicamModel_Pylon400BExcelon', 'PicamModel_Pylon400BR',
    'PicamModel_Pylon400BRExcelon', 'PicamModel_Pylon400F',
    'PicamModel_Pylon400Series', 'PicamModel_PylonSeries',
    'PicamModel_Pylonir102417', 'PicamModel_Pylonir102422',
    'PicamModel_Pylonir1024Series', 'PicamModel_PylonirSeries',
    'PicamModel_Quadro4096', 'PicamModel_Quadro4096_2',
    'PicamModel_Quadro4320', 'PicamModel_QuadroSeries',
    'PicamModel_Sophia2048135', 'PicamModel_Sophia2048135Series',
    'PicamModel_Sophia2048B', 'PicamModel_Sophia2048B135',
    'PicamModel_Sophia2048B135Excelon',
    'PicamModel_Sophia2048BExcelon', 'PicamModel_Sophia2048BR135',
    'PicamModel_Sophia2048BR135Excelon',
    'PicamModel_Sophia2048Series', 'PicamModel_SophiaSeries',
    'PicamModel_SophiaXB2048B', 'PicamModel_SophiaXF2048B',
    'PicamModel_SophiaXO2048B', 'PicamModel_SophiaXO2048B135',
    'PicamModel_SophiaXO2048BR135', 'PicamModulation',
    'PicamModulationTrackingMask',
    'PicamModulationTrackingMask_Duration',
    'PicamModulationTrackingMask_Frequency',
    'PicamModulationTrackingMask_None',
    'PicamModulationTrackingMask_OutputSignalFrequency',
    'PicamModulationTrackingMask_Phase', 'PicamModulations',
    'PicamModulationsConstraint',
    'PicamModulationsValueChangedCallback', 'PicamOrientationMask',
    'PicamOrientationMask_FlippedHorizontally',
    'PicamOrientationMask_FlippedVertically',
    'PicamOrientationMask_Normal', 'PicamOutputSignal',
    'PicamOutputSignal_Acquiring', 'PicamOutputSignal_AlwaysHigh',
    'PicamOutputSignal_AlwaysLow', 'PicamOutputSignal_AuxOutput',
    'PicamOutputSignal_Busy', 'PicamOutputSignal_EffectivelyExposing',
    'PicamOutputSignal_EffectivelyExposingAlternation',
    'PicamOutputSignal_Exposing', 'PicamOutputSignal_Gate',
    'PicamOutputSignal_InternalTriggerT0',
    'PicamOutputSignal_NotReadingOut', 'PicamOutputSignal_ReadingOut',
    'PicamOutputSignal_ShiftingUnderMask',
    'PicamOutputSignal_ShutterOpen',
    'PicamOutputSignal_WaitingForTrigger', 'PicamParameter',
    'PicamParameter_Accumulations',
    'PicamParameter_ActiveBottomMargin',
    'PicamParameter_ActiveExtendedHeight',
    'PicamParameter_ActiveHeight', 'PicamParameter_ActiveLeftMargin',
    'PicamParameter_ActiveRightMargin',
    'PicamParameter_ActiveShutter', 'PicamParameter_ActiveTopMargin',
    'PicamParameter_ActiveWidth', 'PicamParameter_AdcAnalogGain',
    'PicamParameter_AdcBitDepth', 'PicamParameter_AdcEMGain',
    'PicamParameter_AdcQuality', 'PicamParameter_AdcSpeed',
    'PicamParameter_Age', 'PicamParameter_AnticipateTrigger',
    'PicamParameter_AuxOutput', 'PicamParameter_BracketGating',
    'PicamParameter_CcdCharacteristics',
    'PicamParameter_CenterWavelengthReading',
    'PicamParameter_CenterWavelengthSetPoint',
    'PicamParameter_CenterWavelengthStatus',
    'PicamParameter_CleanBeforeExposure',
    'PicamParameter_CleanCycleCount',
    'PicamParameter_CleanCycleHeight',
    'PicamParameter_CleanSectionFinalHeight',
    'PicamParameter_CleanSectionFinalHeightCount',
    'PicamParameter_CleanSerialRegister',
    'PicamParameter_CleanUntilTrigger',
    'PicamParameter_CoolingFanStatus',
    'PicamParameter_CorrectPixelBias',
    'PicamParameter_CustomModulationSequence',
    'PicamParameter_DelayFromPreTrigger',
    'PicamParameter_DifEndingGate', 'PicamParameter_DifStartingGate',
    'PicamParameter_DisableCoolingFan',
    'PicamParameter_DisableDataFormatting',
    'PicamParameter_EMIccdGain',
    'PicamParameter_EMIccdGainControlMode',
    'PicamParameter_EnableAuxOutput',
    'PicamParameter_EnableIntensifier',
    'PicamParameter_EnableModulation',
    'PicamParameter_EnableModulationOutputSignal',
    'PicamParameter_EnableNondestructiveReadout',
    'PicamParameter_EnableSensorWindowHeater',
    'PicamParameter_EnableSyncMaster',
    'PicamParameter_ExactReadoutCountMaximum',
    'PicamParameter_ExposureTime',
    'PicamParameter_ExternalShutterStatus',
    'PicamParameter_ExternalShutterType',
    'PicamParameter_FocalLength',
    'PicamParameter_FrameRateCalculation', 'PicamParameter_FrameSize',
    'PicamParameter_FrameStride',
    'PicamParameter_FrameTrackingBitDepth',
    'PicamParameter_FramesPerReadout', 'PicamParameter_GateTracking',
    'PicamParameter_GateTrackingBitDepth',
    'PicamParameter_GatingMode', 'PicamParameter_GatingSpeed',
    'PicamParameter_GratingBlazingWavelength',
    'PicamParameter_GratingCoating',
    'PicamParameter_GratingGrooveDensity',
    'PicamParameter_GratingType',
    'PicamParameter_InactiveShutterTimingModeResult',
    'PicamParameter_InclusionAngle',
    'PicamParameter_InputTriggerStatus',
    'PicamParameter_IntensifierDiameter',
    'PicamParameter_IntensifierGain',
    'PicamParameter_IntensifierOptions',
    'PicamParameter_IntensifierStatus',
    'PicamParameter_InternalShutterStatus',
    'PicamParameter_InternalShutterType',
    'PicamParameter_InvertOutputSignal',
    'PicamParameter_InvertOutputSignal2',
    'PicamParameter_KineticsWindowHeight',
    'PicamParameter_LaserOutputMode', 'PicamParameter_LaserPower',
    'PicamParameter_LaserStatus', 'PicamParameter_LifeExpectancy',
    'PicamParameter_LightSource', 'PicamParameter_LightSourceStatus',
    'PicamParameter_MaskedBottomMargin',
    'PicamParameter_MaskedHeight', 'PicamParameter_MaskedTopMargin',
    'PicamParameter_ModulationDuration',
    'PicamParameter_ModulationFrequency',
    'PicamParameter_ModulationOutputSignalAmplitude',
    'PicamParameter_ModulationOutputSignalFrequency',
    'PicamParameter_ModulationTracking',
    'PicamParameter_ModulationTrackingBitDepth',
    'PicamParameter_NondestructiveReadoutPeriod',
    'PicamParameter_NormalizeOrientation',
    'PicamParameter_OnlineReadoutRateCalculation',
    'PicamParameter_Orientation', 'PicamParameter_OutputSignal',
    'PicamParameter_OutputSignal2',
    'PicamParameter_PhosphorDecayDelay',
    'PicamParameter_PhosphorDecayDelayResolution',
    'PicamParameter_PhosphorType',
    'PicamParameter_PhotocathodeSensitivity',
    'PicamParameter_PhotonDetectionMode',
    'PicamParameter_PhotonDetectionThreshold',
    'PicamParameter_PixelBitDepth', 'PicamParameter_PixelFormat',
    'PicamParameter_PixelGapHeight', 'PicamParameter_PixelGapWidth',
    'PicamParameter_PixelHeight', 'PicamParameter_PixelWidth',
    'PicamParameter_ReadoutControlMode',
    'PicamParameter_ReadoutCount',
    'PicamParameter_ReadoutOrientation',
    'PicamParameter_ReadoutPortCount',
    'PicamParameter_ReadoutRateCalculation',
    'PicamParameter_ReadoutStride',
    'PicamParameter_ReadoutTimeCalculation',
    'PicamParameter_RepetitiveGate',
    'PicamParameter_RepetitiveModulationPhase', 'PicamParameter_Rois',
    'PicamParameter_SeNsRWindowHeight',
    'PicamParameter_SecondaryActiveHeight',
    'PicamParameter_SecondaryMaskedHeight',
    'PicamParameter_SensorActiveBottomMargin',
    'PicamParameter_SensorActiveExtendedHeight',
    'PicamParameter_SensorActiveHeight',
    'PicamParameter_SensorActiveLeftMargin',
    'PicamParameter_SensorActiveRightMargin',
    'PicamParameter_SensorActiveTopMargin',
    'PicamParameter_SensorActiveWidth', 'PicamParameter_SensorAngle',
    'PicamParameter_SensorMaskedBottomMargin',
    'PicamParameter_SensorMaskedHeight',
    'PicamParameter_SensorMaskedTopMargin',
    'PicamParameter_SensorSecondaryActiveHeight',
    'PicamParameter_SensorSecondaryMaskedHeight',
    'PicamParameter_SensorTemperatureReading',
    'PicamParameter_SensorTemperatureSetPoint',
    'PicamParameter_SensorTemperatureStatus',
    'PicamParameter_SensorType',
    'PicamParameter_SequentialEndingGate',
    'PicamParameter_SequentialEndingModulationPhase',
    'PicamParameter_SequentialGateStepCount',
    'PicamParameter_SequentialGateStepIterations',
    'PicamParameter_SequentialStartingGate',
    'PicamParameter_SequentialStartingModulationPhase',
    'PicamParameter_ShutterClosingDelay',
    'PicamParameter_ShutterDelayResolution',
    'PicamParameter_ShutterOpeningDelay',
    'PicamParameter_ShutterTimingMode',
    'PicamParameter_StopCleaningOnPreTrigger',
    'PicamParameter_SyncMaster2Delay',
    'PicamParameter_TimeStampBitDepth',
    'PicamParameter_TimeStampResolution', 'PicamParameter_TimeStamps',
    'PicamParameter_TrackFrames', 'PicamParameter_TriggerCoupling',
    'PicamParameter_TriggerDelay',
    'PicamParameter_TriggerDetermination',
    'PicamParameter_TriggerFrequency',
    'PicamParameter_TriggerResponse', 'PicamParameter_TriggerSource',
    'PicamParameter_TriggerTermination',
    'PicamParameter_TriggerThreshold', 'PicamParameter_VacuumStatus',
    'PicamParameter_VerticalShiftRate', 'PicamPhosphorType',
    'PicamPhosphorType_P43', 'PicamPhosphorType_P46',
    'PicamPhotocathodeSensitivity',
    'PicamPhotocathodeSensitivity_HighBlueFilmless',
    'PicamPhotocathodeSensitivity_HighQEFilmless',
    'PicamPhotocathodeSensitivity_HighRedFilmless',
    'PicamPhotocathodeSensitivity_InGaAsFilmless',
    'PicamPhotocathodeSensitivity_RedBlue',
    'PicamPhotocathodeSensitivity_SolarBlind',
    'PicamPhotocathodeSensitivity_SuperBlue',
    'PicamPhotocathodeSensitivity_SuperRed',
    'PicamPhotocathodeSensitivity_UV',
    'PicamPhotocathodeSensitivity_Unigen2Filmless',
    'PicamPhotonDetectionMode', 'PicamPhotonDetectionMode_Clipping',
    'PicamPhotonDetectionMode_Disabled',
    'PicamPhotonDetectionMode_Thresholding', 'PicamPixelDefectMap',
    'PicamPixelFormat', 'PicamPixelFormat_Monochrome16Bit',
    'PicamPixelFormat_Monochrome32Bit', 'PicamPixelLocation',
    'PicamPulse', 'PicamPulseConstraint',
    'PicamPulseValueChangedCallback', 'PicamRangeConstraint',
    'PicamReadoutControlMode', 'PicamReadoutControlMode_Dif',
    'PicamReadoutControlMode_FrameTransfer',
    'PicamReadoutControlMode_FullFrame',
    'PicamReadoutControlMode_Interline',
    'PicamReadoutControlMode_Kinetics',
    'PicamReadoutControlMode_RollingShutter',
    'PicamReadoutControlMode_SeNsR',
    'PicamReadoutControlMode_SpectraKinetics', 'PicamRoi',
    'PicamRois', 'PicamRoisConstraint',
    'PicamRoisConstraintRulesMask',
    'PicamRoisConstraintRulesMask_HorizontalSymmetry',
    'PicamRoisConstraintRulesMask_None',
    'PicamRoisConstraintRulesMask_SymmetryBoundsBinning',
    'PicamRoisConstraintRulesMask_VerticalSymmetry',
    'PicamRoisConstraintRulesMask_XBinningAlignment',
    'PicamRoisConstraintRulesMask_YBinningAlignment',
    'PicamRoisValueChangedCallback', 'PicamRowDefect',
    'PicamSensorTemperatureStatus',
    'PicamSensorTemperatureStatus_Faulted',
    'PicamSensorTemperatureStatus_Locked',
    'PicamSensorTemperatureStatus_Unlocked', 'PicamSensorType',
    'PicamSensorType_Ccd', 'PicamSensorType_Cmos',
    'PicamSensorType_InGaAs', 'PicamShutterStatus',
    'PicamShutterStatus_Connected', 'PicamShutterStatus_NotConnected',
    'PicamShutterStatus_Overheated', 'PicamShutterTimingMode',
    'PicamShutterTimingMode_AlwaysClosed',
    'PicamShutterTimingMode_AlwaysOpen',
    'PicamShutterTimingMode_Normal',
    'PicamShutterTimingMode_OpenBeforeTrigger', 'PicamShutterType',
    'PicamShutterType_None', 'PicamShutterType_ProntorMagnetic0',
    'PicamShutterType_ProntorMagneticE40',
    'PicamShutterType_VincentCS25', 'PicamShutterType_VincentCS45',
    'PicamShutterType_VincentCS90', 'PicamShutterType_VincentDSS10',
    'PicamShutterType_VincentVS25', 'PicamShutterType_VincentVS35',
    'PicamSpecial_CanEraseResidual', 'PicamSpecial_EraseResidual',
    'PicamStatusPurview', 'PicamStringSize',
    'PicamStringSize_FirmwareDetail', 'PicamStringSize_FirmwareName',
    'PicamStringSize_SensorName', 'PicamStringSize_SerialNumber',
    'PicamTimeStampsMask', 'PicamTimeStampsMask_ExposureEnded',
    'PicamTimeStampsMask_ExposureStarted', 'PicamTimeStampsMask_None',
    'PicamTriggerCoupling', 'PicamTriggerCoupling_AC',
    'PicamTriggerCoupling_DC', 'PicamTriggerDetermination',
    'PicamTriggerDetermination_AlternatingEdgeFalling',
    'PicamTriggerDetermination_AlternatingEdgeRising',
    'PicamTriggerDetermination_FallingEdge',
    'PicamTriggerDetermination_NegativePolarity',
    'PicamTriggerDetermination_PositivePolarity',
    'PicamTriggerDetermination_RisingEdge', 'PicamTriggerResponse',
    'PicamTriggerResponse_ExposeDuringTriggerPulse',
    'PicamTriggerResponse_GatePerTrigger',
    'PicamTriggerResponse_NoResponse',
    'PicamTriggerResponse_ReadoutPerTrigger',
    'PicamTriggerResponse_ShiftPerTrigger',
    'PicamTriggerResponse_StartOnSingleTrigger', 'PicamTriggerSource',
    'PicamTriggerSource_External', 'PicamTriggerSource_Internal',
    'PicamTriggerSource_None', 'PicamTriggerStatus',
    'PicamTriggerStatus_Connected', 'PicamTriggerStatus_NotConnected',
    'PicamTriggerTermination', 'PicamTriggerTermination_FiftyOhms',
    'PicamTriggerTermination_HighImpedance', 'PicamVacuumStatus',
    'PicamVacuumStatus_Low', 'PicamVacuumStatus_Sufficient',
    'PicamValidationResult', 'PicamValidationResults',
    'PicamValueAccess', 'PicamValueAccessChangedCallback',
    'PicamValueAccess_ReadOnly', 'PicamValueAccess_ReadWrite',
    'PicamValueAccess_ReadWriteTrivial', 'PicamValueType',
    'PicamValueType_Boolean', 'PicamValueType_Enumeration',
    'PicamValueType_FloatingPoint', 'PicamValueType_Integer',
    'PicamValueType_LargeInteger', 'PicamValueType_Modulations',
    'PicamValueType_Pulse', 'PicamValueType_Rois',
    'PicamWhenStatusParameterValueCallback', 'Picam_Acquire',
    'Picam_AreParametersCommitted', 'Picam_CanReadParameter',
    'Picam_CanSetParameterFloatingPointValue',
    'Picam_CanSetParameterIntegerValue',
    'Picam_CanSetParameterLargeIntegerValue',
    'Picam_CanSetParameterModulationsValue',
    'Picam_CanSetParameterOnline', 'Picam_CanSetParameterPulseValue',
    'Picam_CanSetParameterRoisValue',
    'Picam_CanWaitForStatusParameter', 'Picam_CloseCamera',
    'Picam_CommitParameters', 'Picam_ConnectDemoCamera',
    'Picam_DestroyCalibrations', 'Picam_DestroyCameraIDs',
    'Picam_DestroyCollectionConstraints',
    'Picam_DestroyDependentValidationResult',
    'Picam_DestroyFirmwareDetails', 'Picam_DestroyHandles',
    'Picam_DestroyModels', 'Picam_DestroyModulations',
    'Picam_DestroyModulationsConstraints', 'Picam_DestroyParameters',
    'Picam_DestroyPulseConstraints', 'Picam_DestroyPulses',
    'Picam_DestroyRangeConstraints', 'Picam_DestroyRois',
    'Picam_DestroyRoisConstraints', 'Picam_DestroyStatusPurviews',
    'Picam_DestroyString', 'Picam_DestroyValidationResult',
    'Picam_DestroyValidationResults', 'Picam_DisconnectDemoCamera',
    'Picam_DoesParameterExist',
    'Picam_EstimateTimeToStatusParameterValue',
    'Picam_GetAvailableCameraIDs',
    'Picam_GetAvailableDemoCameraModels', 'Picam_GetCameraID',
    'Picam_GetEnumerationString', 'Picam_GetFirmwareDetails',
    'Picam_GetOpenCameras', 'Picam_GetParameterCollectionConstraint',
    'Picam_GetParameterConstraintType',
    'Picam_GetParameterEnumeratedType',
    'Picam_GetParameterFloatingPointDefaultValue',
    'Picam_GetParameterFloatingPointValue',
    'Picam_GetParameterIntegerDefaultValue',
    'Picam_GetParameterIntegerValue',
    'Picam_GetParameterLargeIntegerDefaultValue',
    'Picam_GetParameterLargeIntegerValue',
    'Picam_GetParameterModulationsConstraint',
    'Picam_GetParameterModulationsDefaultValue',
    'Picam_GetParameterModulationsValue',
    'Picam_GetParameterPulseConstraint',
    'Picam_GetParameterPulseDefaultValue',
    'Picam_GetParameterPulseValue',
    'Picam_GetParameterRangeConstraint',
    'Picam_GetParameterRoisConstraint',
    'Picam_GetParameterRoisDefaultValue',
    'Picam_GetParameterRoisValue', 'Picam_GetParameterValueAccess',
    'Picam_GetParameterValueType', 'Picam_GetParameters',
    'Picam_GetStatusParameterPurview',
    'Picam_GetUnavailableCameraIDs', 'Picam_GetVersion',
    'Picam_InitializeLibrary', 'Picam_IsAcquisitionRunning',
    'Picam_IsCameraConnected', 'Picam_IsCameraFaulted',
    'Picam_IsCameraIDConnected', 'Picam_IsCameraIDOpenElsewhere',
    'Picam_IsDemoCamera', 'Picam_IsLibraryInitialized',
    'Picam_IsParameterRelevant', 'Picam_OpenCamera',
    'Picam_OpenFirstCamera', 'Picam_ReadParameterFloatingPointValue',
    'Picam_ReadParameterIntegerValue',
    'Picam_RestoreParametersToDefaultValues',
    'Picam_SetParameterFloatingPointValue',
    'Picam_SetParameterFloatingPointValueOnline',
    'Picam_SetParameterIntegerValue',
    'Picam_SetParameterIntegerValueOnline',
    'Picam_SetParameterLargeIntegerValue',
    'Picam_SetParameterModulationsValue',
    'Picam_SetParameterPulseValue',
    'Picam_SetParameterPulseValueOnline',
    'Picam_SetParameterRoisValue', 'Picam_StartAcquisition',
    'Picam_StopAcquisition', 'Picam_UninitializeLibrary',
    'Picam_WaitForAcquisitionUpdate',
    'Picam_WaitForStatusParameterValue', 'pi16s', 'pi16u', 'pi32f',
    'pi32s', 'pi32u', 'pi64f', 'pi64s', 'pi64u', 'pi8s', 'pi8u',
    'pibln', 'pibyte', 'pichar', 'piflt', 'piint',
    'struct_PicamAccessoryID', 'struct_PicamAcquisitionBuffer',
    'struct_PicamAcquisitionStateCounters',
    'struct_PicamAcquisitionStatus', 'struct_PicamAvailableData',
    'struct_PicamCalibration', 'struct_PicamCalibrationPoint',
    'struct_PicamCameraID', 'struct_PicamCollectionConstraint',
    'struct_PicamColumnDefect',
    'struct_PicamDependentValidationResult',
    'struct_PicamEMCalibrationDate',
    'struct_PicamFailedDependentParameter',
    'struct_PicamFirmwareDetail', 'struct_PicamModulation',
    'struct_PicamModulations', 'struct_PicamModulationsConstraint',
    'struct_PicamPixelDefectMap', 'struct_PicamPixelLocation',
    'struct_PicamPulse', 'struct_PicamPulseConstraint',
    'struct_PicamRangeConstraint', 'struct_PicamRoi',
    'struct_PicamRois', 'struct_PicamRoisConstraint',
    'struct_PicamRowDefect', 'struct_PicamStatusPurview',
    'struct_PicamValidationResult', 'struct_PicamValidationResults']

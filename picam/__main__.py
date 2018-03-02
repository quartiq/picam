from . import *

cam = picam()
cam.loadLibrary()
cam.getAvailableCameras()
cam.connect()

# cool down CCD
cam.setParameter("SensorTemperatureSetPoint", -75)

# shortest expoure
cam.setParameter("ExposureTime", 0)

# readout mode
cam.setParameter("ReadoutControlMode", PicamReadoutControlMode["FullFrame"])

# custom chip settings
cam.setROI(0, 1340, 1, 0, 100, 100)
cam.setParameter("ActiveWidth", 1340)
cam.setParameter("ActiveHeight", 100)
cam.setParameter("ActiveLeftMargin", 0)
cam.setParameter("ActiveRightMargin", 0)
cam.setParameter("ActiveTopMargin", 8)
cam.setParameter("ActiveBottomMargin", 8)
cam.setParameter("VerticalShiftRate", 3.2)    # select fastest

# set logic out to not ready
cam.setParameter("OutputSignal", PicamOutputSignal["Busy"])

# shutter delays; open before trigger corresponds to shutter opening pre delay
cam.setParameter("ShutterTimingMode", PicamShutterTimingMode["Normal"])
cam.setParameter("ShutterClosingDelay", 0)

# sensor cleaning
cam.setParameter("CleanSectionFinalHeightCount", 1)
cam.setParameter("CleanSectionFinalHeight", 100)
cam.setParameter("CleanSerialRegister", False)
cam.setParameter("CleanCycleCount", 1)
cam.setParameter("CleanCycleHeight", 100)
cam.setParameter("CleanUntilTrigger", True)

# sensor gain settings
# according to manual, Pixis supports 100kHz and 2MHz; select fastest
cam.setParameter("AdcSpeed", 2.0)
cam.setParameter("AdcAnalogGain", PicamAdcAnalogGain["Low"])
cam.setParameter("AdcQuality", PicamAdcQuality["HighCapacity"])

# trigger and timing settings
cam.setParameter("TriggerDetermination", PicamTriggerDetermination["PositivePolarity"])
cam.setParameter("TriggerResponse", PicamTriggerResponse["ReadoutPerTrigger"])

# send configuration
cam.sendConfiguration()

# get readout speed
print("Estimated readout time = %f ms" % cam.getParameter("ReadoutTimeCalculation"))

cam.disconnect()
cam.unloadLibrary()

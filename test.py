import logging

import numpy as np

import pi


logger = logging.getLogger(__name__)


def main(cam, num_frames=3):
    cid = cam.get_id()
    model = pi.get_string(pi.PicamEnumeratedType_Model, cid.model)
    logger.info("model: %s, serial: %s, sensor: %s", model,
                cid.serial_number.decode(), cid.sensor_name.decode())

    for i in cam.get_parameters():
        name = pi.get_string(pi.PicamEnumeratedType_Parameter, i)
        access = pi.get_string(
            pi.PicamEnumeratedType_ValueAccess,
            cam.get_parameter_value_access(i))
        typ = cam.get_parameter_constraint_type(i)
        constraint = pi.get_string(
            pi.PicamEnumeratedType_ConstraintType,
            typ)
        logger.info("parameter '%s', access: %s, constraint: %s",
                    name, access, constraint)
        logger.info("value: %s", cam.get(i))
        if typ == pi.PicamConstraintType_Range:
            logger.info("range from %f to %f, incr %f",
                        *cam.get_parameter_range_constraint(i))
        elif typ == pi.PicamConstraintType_Collection:
            logger.info("collection %s",
                        cam.get_parameter_collection_constraint(i))

    temp = cam.get(pi.PicamParameter_SensorTemperatureReading)
    logger.info("temp: %g C", temp)
    st = pi.get_string(
        pi.PicamEnumeratedType_SensorTemperatureStatus,
        cam.get(pi.PicamParameter_SensorTemperatureStatus))
    logger.info("temp status: %s", st)
    cam.set(pi.PicamParameter_DisableCoolingFan, False)
    cam.set(pi.PicamParameter_SensorTemperatureSetPoint, -70.)
    cam.set(pi.PicamParameter_ReadoutControlMode,
            pi.PicamReadoutControlMode_FrameTransfer)
    if True:
        cam.set(pi.PicamParameter_AdcQuality,
                pi.PicamAdcQuality_LowNoise)
        cam.set(pi.PicamParameter_AdcSpeed, 1.)  # MHz
        cam.set(pi.PicamParameter_AdcEMGain, 1)
        cam.set(pi.PicamParameter_AdcAnalogGain,
                pi.PicamAdcAnalogGain_High)
    else:
        cam.set(pi.PicamParameter_AdcQuality,
                pi.PicamAdcQuality_ElectronMultiplied)
        cam.set(pi.PicamParameter_AdcSpeed, 5.)  # MHz
        cam.set(pi.PicamParameter_AdcEMGain, 20)
        cam.set(pi.PicamParameter_AdcAnalogGain,
                pi.PicamAdcAnalogGain_Low)

    cam.set(pi.PicamParameter_ExposureTime, 100.)  # ms
    cam.set(pi.PicamParameter_ReadoutCount, 1)
    cam.set(pi.PicamParameter_NormalizeOrientation, True)
    cam.set(pi.PicamParameter_CorrectPixelBias, True)
    cam.set(pi.PicamParameter_ShutterTimingMode,
            pi.PicamShutterTimingMode_AlwaysClosed)
    if True:
        cam.set(pi.PicamParameter_Rois, [((0, 512, 1), (0, 512, 1))])
    else:
        cam.set(pi.PicamParameter_Rois, [((250, 20, 1), (250, 20, 1))])
    try:
        cam.commit()
    except pi.Error as err:
        logger.info("failed commit: %s", [
            pi.get_string(pi.PicamEnumeratedType_Parameter, i)
            for i in err.fails])

    logger.info("rois %s", cam.get(pi.PicamParameter_Rois))
    logger.debug("exposure %s ms",
                    cam.get(pi.PicamParameter_ExposureTime))

    readout_stride = cam.get(pi.PicamParameter_ReadoutStride)
    frames = np.empty((100, 512, 512), "<u2")
    for i in range(num_frames):
        data, errors = cam.acquire(1)
        if errors.value:
            errors = pi.get_string(
                pi.PicamEnumeratedType_AcquisitionErrorsMask, errors)
            logger.warning("acquisition errors %s", errors)
        data = pi.get_data(data, readout_stride).view("<u2")
        logger.info("frames %s: %s", data.shape, data[:, :10])
        frames[i] = data.reshape(frames.shape[1:])
    np.savez("pi_frames.npz", frames=frames)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s")
    with pi.Library(), pi.Camera().open_first() as cam:
        main(cam)

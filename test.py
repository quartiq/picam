import logging

import numpy as np

import pi


logger = logging.getLogger(__name__)


def configure_cam(lib, cam):
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
            lib.get_string(pi.PicamEnumeratedType_Parameter, i)
            for i in err.fails])


def print_parameter_info(lib, cam, i):
    logger.info("parameter '%s'",
        lib.get_string(pi.PicamEnumeratedType_Parameter, i))
    access = cam.get_parameter_value_access(i)
    logger.info("  access: %s",
        lib.get_string(pi.PicamEnumeratedType_ValueAccess, access))
    value_typ = cam.get_parameter_value_type(i)
    logger.info("  typ: %s",
        lib.get_string(pi.PicamEnumeratedType_ValueType, value_typ))
    value = cam.get(i)
    if value_typ == pi.PicamValueType_Enumeration:
        value = lib.get_string(cam.get_parameter_enumerated_type(i), value)
    logger.info("  value: %s", value)
    constraint_typ = cam.get_parameter_constraint_type(i)
    logger.info("  constraint: %s", lib.get_string(
        pi.PicamEnumeratedType_ConstraintType, constraint_typ))
    if constraint_typ == pi.PicamConstraintType_Range:
        logger.info("    from %f to %f, incr %f",
                    *cam.get_parameter_range_constraint(i))
    elif constraint_typ == pi.PicamConstraintType_Collection:
        coll = cam.get_parameter_collection_constraint(i)
        if (value_typ ==
                pi.PicamValueType_Enumeration):
            coll = [lib.get_string(
                cam.get_parameter_enumerated_type(i), int(j))
                for j in coll]
        logger.info("    collection %s", coll)


def acquire(lib, cam, num_frames=3):
    readout_stride = cam.get(pi.PicamParameter_ReadoutStride)
    readout_count = cam.get(pi.PicamParameter_ReadoutCount)
    frames = np.empty((num_frames, readout_count, 512, 512), "<u2")
    for i in range(num_frames):
        data, errors = cam.acquire(readout_count)
        if errors.value:
            errors = lib.get_string(
                pi.PicamEnumeratedType_AcquisitionErrorsMask, errors)
            logger.warning("acquisition errors %s", errors)
        data = pi.get_data(data, readout_stride).view("<u2")
        logger.info("frames %s: %s", data.shape, data[:, :10])
        frames[i] = data.reshape(frames.shape[1:])
    np.savez("pi_frames.npz", frames=frames)


def main():
    with pi.Library() as lib, pi.Camera().open_first() as cam:
        cid = cam.get_id()
        model = lib.get_string(pi.PicamEnumeratedType_Model, cid.model)
        logger.info("model: %s, serial: %s, sensor: %s", model,
                    cid.serial_number.decode(), cid.sensor_name.decode())

        configure_cam(lib, cam)

        for i in cam.get_parameters():
            print_parameter_info(lib, cam, i)

        acquire(lib, cam)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-13s %(name)-5s %(levelname)-3s %(message)s")
    main()

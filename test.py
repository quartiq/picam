import logging

import pi


logger = logging.getLogger(__name__)


def main(cam):
    NUM_FRAMES = 3

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
        logger.info("param %s, access: %s, constraint %s",
                    name, access, constraint)
        if typ == pi.PicamConstraintType_Range:
            try:
                logger.info("range from %f to %f, incr %f",
                            *cam.get_parameter_range_constraint(i))
            except pi.Error:
                logger.warning("invalid constraint")
        elif typ == pi.PicamConstraintType_Collection:
            logger.info("collection %s",
                        cam.get_parameter_collection_constraint(i))

    temp = cam.get(pi.PicamParameter_SensorTemperatureReading)
    logger.info("temp: %g C", temp)
    st = pi.get_string(
        pi.PicamEnumeratedType_SensorTemperatureStatus,
        cam.get(pi.PicamParameter_SensorTemperatureStatus))
    logger.info("temp status: %s", st)
    cam.set(pi.PicamParameter_SensorTemperatureSetPoint, -20.)
    cam.set(pi.PicamParameter_AdcAnalogGain,
            pi.PicamAdcAnalogGain_Low)
    cam.set(pi.PicamParameter_ExposureTime, 30.)  # ms
    cam.set(pi.PicamParameter_ReadoutCount, 1)
    cam.set(pi.PicamParameter_Rois, [((0, 512, 1), (0, 512, 1))])
    fails = cam.commit()
    if fails:
        logger.info("failed commit: %s", [
            pi.get_string(pi.PicamEnumeratedType_Parameter, i)
            for i in fails])

    logger.info("rois %s", cam.get(pi.PicamParameter_Rois))
    logger.debug("exposure %s ms",
                    cam.get(pi.PicamParameter_ExposureTime))

    readout_stride = cam.get(pi.PicamParameter_ReadoutStride)
    for i in range(NUM_FRAMES):
        data, errors = cam.acquire(1)
        if errors.value:
            errors = pi.get_string(
                pi.PicamEnumeratedType_AcquisitionErrorsMask, errors)
            logger.warning("acquisition errors %s", errors)
        data = pi.get_data(data, readout_stride).view("<u2")
        logger.info("frames %s: %s", data.shape, data[:, :10])


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s")
    with pi.Library(), pi.Camera().open_first() as cam:
        main(cam)

import logging

import pi


logger = logging.getLogger(__name__)


def main():
    NUM_FRAMES = 3

    with pi.Library() as lib, pi.Camera().open_first() as cam:
        cid = cam.get_id()
        model = pi.get_string(pi.PicamEnumeratedType_Model, cid.model)
        logger.info("model: %s, serial: %s, sensor: %s", model,
                    cid.serial_number.decode(), cid.sensor_name.decode())
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
        logger.info("rois %s", cam.get(pi.PicamParameter_Rois))
        if fails:
            logger.info("failed commit: %s", [
                pi.get_string(pi.PicamEnumeratedType_Parameter, i)
                for i in fails])
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
    main()

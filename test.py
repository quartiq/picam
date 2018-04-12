import logging

import pi


logger = logging.getLogger(__name__)


def main():
    NUM_FRAMES = 3

    with pi.Library() as lib, pi.Camera().open_first() as cam:
        cid = cam.get_id()
        model = pi.get_string(pi.PicamEnumeratedType_Model, cid.model)
        logger.info("model: %s, serial: %s, sensor: %s",
                    model, cid.serial_number, cid.sensor_name)
        temp = cam.get_float(pi.PicamParameter_SensorTemperatureReading)
        logger.info("temp: %g C", temp)
        st = pi.get_string(
            pi.PicamEnumeratedType_SensorTemperatureStatus,
            cam.get_int(pi.PicamParameter_SensorTemperatureStatus))
        logger.info("temp status: %s", st)
        cam.set_float(pi.PicamParameter_SensorTemperatureSetPoint, -20.)
        cam.set_int(pi.PicamParameter_AdcAnalogGain,
                    pi.PicamAdcAnalogGain_Low)
        cam.set_float(pi.PicamParameter_ExposureTime, 30.)  # ms
        cam.set_long(pi.PicamParameter_ReadoutCount, 1)
        logger.info("failed commit: %s", cam.commit())
        readoutstride = cam.get_int(pi.PicamParameter_ReadoutStride)
        logger.debug("exposure %s ms",
                      cam.get_float(pi.PicamParameter_ExposureTime))
        for i in range(NUM_FRAMES):
            data, errors = cam.acquire(num_frames=1)
            if errors is not None:
                logger.warning("acquisition errors %s", errors)
            data = pi.get_data(
                data.initial_readout, data.readout_count, readoutstride)
            logger.info("frames %s: %s", data.shape, data[:, :10])


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s")
    main()

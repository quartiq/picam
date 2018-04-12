import logging

from ctypes import byref, POINTER, cast, c_char_p, pythonapi, py_object
import numpy as np

import picam as pi


pythonapi.PyMemoryView_FromMemory.restype = py_object

logger = logging.getLogger(__name__)


def print_data(data, num, length):
    # read only buffer
    data = pythonapi.PyMemoryView_FromMemory(data, num*length.value, 0x100)
    data = np.ndarray((num, length.value//2), ">u2", data, order="C")
    logger.info("frames %s: %s", data.shape, data[:, :10])


def main():
    NUM_FRAMES = 5
    NO_TIMEOUT = -1

    logger.debug("init")
    pi.Picam_InitializeLibrary()
    try:
        camera = pi.PicamHandle()
        logger.debug("open")
        if pi.Picam_OpenFirstCamera(byref(camera)) == pi.PicamError_None:
            try:
                cid = pi.PicamCameraID()
                logger.debug("get_id")
                pi.Picam_GetCameraID(camera, byref(cid))
                logger.debug("model")
                string = POINTER(pi.pichar)()
                pi.Picam_GetEnumerationString(pi.PicamEnumeratedType_Model,
                        cid.model, string)
                logger.info("model: %s, serial: %s, sensor: %s",
                            cast(string, c_char_p).value,
                            cid.serial_number, cid.sensor_name)
                pi.Picam_DestroyString(string)

                readoutstride = pi.piint(0)
                logger.debug("stride")
                pi.Picam_GetParameterIntegerValue(camera,
                        pi.PicamParameter_ReadoutStride, byref(readoutstride))
                data = pi.PicamAvailableData()
                errors = pi.PicamAcquisitionErrorsMask()
                logger.debug("acquire")
                if pi.Picam_Acquire(camera, NUM_FRAMES, NO_TIMEOUT, byref(data),
                    byref(errors)):
                    logger.error("Only have %i frames", data.readout_count)
                else:
                    logger.debug("data")
                    print_data(data.initial_readout, data.readout_count,
                               readoutstride)
                for i in range(NUM_FRAMES):
                    logger.debug("acquire")
                    if pi.Picam_Acquire(camera, 1, NO_TIMEOUT, byref(data),
                                        byref(errors)):
                        logger.error("Only have %i frames", data.readout_count)
                    else:
                        logger.debug("data")
                        print_data(data.initial_readout, 1, readoutstride)
            finally:
                logger.debug("close")
                pi.Picam_CloseCamera(camera)
    finally:
        logger.debug("uninit")
        pi.Picam_UninitializeLibrary()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s")
    main()

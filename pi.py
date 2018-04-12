import logging

from ctypes import byref, POINTER, cast, c_char_p, string_at
import numpy as np

import picam as pi


logger = logging.getLogger(__name__)


class Error(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return "Error({}): {}".format(
           self.error, get_string(pi.PicamEnumeratedType_Error, self.error))

    @classmethod
    def check(cls, err):
        if err == pi.PicamError_None:
            return
        raise cls(err)


def get_string(typ, val):
    string = POINTER(pi.pichar)()
    Error.check(pi.Picam_GetEnumerationString(
        typ, val, byref(string)))
    ret = cast(string, c_char_p).value.decode()  # decode copies
    Error.check(pi.Picam_DestroyString(string))
    return ret


def get_data(data, num, length, dtype=">u2"):
    data = (pi.pibyte*(num*length)).from_address(data)
    return np.ctypeslib.as_array(data).reshape(num, length).view(dtype)


class Library:
    def initialized(self):
        val = pi.pibln()
        Error.check(pi.Picam_IsLibraryInitialized(byref(val)))
        return val.value

    def initialize(self):
        logger.debug("initialize")
        Error.check(pi.Picam_InitializeLibrary())

    def uninitialize(self):
        logger.debug("uninitialize")
        Error.check(pi.Picam_UninitializeLibrary())

    def __enter__(self):
        if self.initialized():
            raise ValueError("already initialized")
        self.initialize()

    def __exit__(self, exc_type, exc_value, traceback):
        self.uninitialize()


class Camera:
    def __init__(self):
        self._handle = pi.PicamHandle()

    def open_first(self):
        logger.debug("open_first")
        Error.check(pi.Picam_OpenFirstCamera(byref(self._handle)))
        return self

    def __enter__(self):
        assert self._handle
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        logger.debug("close")
        Error.check(pi.Picam_CloseCamera(self._handle))

    def get_id(self):
        cid = pi.PicamCameraID()
        logger.debug("get_id")
        Error.check(pi.Picam_GetCameraID(self._handle, byref(cid)))
        return cid

    def get_integer(self, typ):
        val = pi.piint()
        Error.check(pi.Picam_GetParameterIntegerValue(
            self._handle, typ, byref(val)))
        return val.value

    def acquire(self, num_frames=1, timeout=-1):
        data = pi.PicamAvailableData()
        errors = pi.PicamAcquisitionErrorsMask()
        logger.debug("acquire")
        Error.check(pi.Picam_Acquire(self._handle, num_frames, timeout,
                                   byref(data), byref(errors)))
        return data, errors


def main():
    NUM_FRAMES = 5

    with Library() as lib, Camera().open_first() as cam:
        cid = cam.get_id()
        model = get_string(pi.PicamEnumeratedType_Model, cid.model)
        logger.info("model: %s, serial: %s, sensor: %s",
                    model, cid.serial_number, cid.sensor_name)
        readoutstride = cam.get_integer(pi.PicamParameter_ReadoutStride)
        for i in range(NUM_FRAMES):
            data, errors = cam.acquire(num_frames=1)
            data = get_data(
                data.initial_readout, data.readout_count, readoutstride)
            logger.info("frames %s: %s", data.shape, data[:, :10])


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s")
    main()

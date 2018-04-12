import logging

from ctypes import byref, POINTER, cast, c_char_p, string_at, c_double
import numpy as np

import picam as pi


logger = logging.getLogger(__name__)


class Error(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        try:
            string = get_string(pi.PicamEnumeratedType_Error, self.error)
        except:
            string = "<unknown error>"
        return "Error({}): {}".format(self.error, string)

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

    def get_int(self, typ):
        val = pi.piint()
        Error.check(pi.Picam_GetParameterIntegerValue(
            self._handle, typ, byref(val)))
        return val.value

    def get_long(self, typ):
        val = pi.pi64s()
        Error.check(pi.Picam_GetParameterIntegerValue(
            self._handle, typ, byref(val)))
        return val.value

    def get_float(self, typ):
        val = pi.piflt()
        Error.check(pi.Picam_GetParameterFloatingPointValue(
            self._handle, typ, byref(val)))
        return val.value

    def set_int(self, typ, value):
        Error.check(pi.Picam_SetParameterIntegerValue(
            self._handle, typ, pi.piint(value)))

    def set_long(self, typ, value):
        Error.check(pi.Picam_SetParameterLargeIntegerValue(
            self._handle, typ, pi.pi64s(value)))

    def set_float(self, typ, value):
        Error.check(pi.Picam_SetParameterFloatingPointValue(
            self._handle, typ, pi.piflt(value)))

    def comitted(self):
        ret = pi.pibln()
        Error.check(pi.Picam_AreParametersCommitted(
            self._handle, byref(ret)))
        return ret.value

    def commit(self):
        failed = POINTER(pi.PicamParameter)()
        failed_count = pi.piint()
        Error.check(pi.Picam_CommitParameters(
            self._handle, byref(failed), byref(failed_count)))
        failed_names = [get_string(pi.PicamEnumeratedType_Parameter,
            failed[i]) for i in range(failed_count.value)]
        Error.check(pi.Picam_DestroyParameters(failed))
        return failed_names

    def acquire(self, num_frames=1, timeout=-1):
        data = pi.PicamAvailableData()
        errors = pi.PicamAcquisitionErrorsMask()
        logger.debug("acquire")
        Error.check(pi.Picam_Acquire(self._handle, num_frames, timeout,
                                   byref(data), byref(errors)))
        if errors.value == pi.PicamAcquisitionErrorsMask_None:
            errors = None
        else:
            errors = get_string(pi.PicamEnumeratedType_AcquisitionErrorsMask,
                                errors)
        return data, errors


def main():
    NUM_FRAMES = 3

    with Library() as lib, Camera().open_first() as cam:
        cid = cam.get_id()
        model = get_string(pi.PicamEnumeratedType_Model, cid.model)
        logger.info("model: %s, serial: %s, sensor: %s",
                    model, cid.serial_number, cid.sensor_name)
        readoutstride = cam.get_int(pi.PicamParameter_ReadoutStride)
        logger.debug("exposure %s ms",
                      cam.get_float(pi.PicamParameter_ExposureTime))
        cam.set_int(pi.PicamParameter_AdcAnalogGain,
                    pi.PicamAdcAnalogGain_Low)
        cam.set_float(pi.PicamParameter_ExposureTime, 30.)  # ms
        cam.set_long(pi.PicamParameter_ReadoutCount, 1)
        cam.commit()
        for i in range(NUM_FRAMES):
            data, errors = cam.acquire(num_frames=1)
            if errors is not None:
                logger.warning("acquisition errors %s", errors)
            data = get_data(
                data.initial_readout, data.readout_count, readoutstride)
            logger.info("frames %s: %s", data.shape, data[:, :10])


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s")
    main()

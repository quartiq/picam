import logging

from ctypes import byref, POINTER, cast, c_char_p, string_at, c_double
import numpy as np

from picam import *


logger = logging.getLogger(__name__)


class Error(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        try:
            string = get_string(PicamEnumeratedType_Error, self.error)
            return "pi.Error({}): {}".format(self.error, string)
        except:
            return "pi.Error({})".format(self.error)

    @classmethod
    def check(cls, err):
        if err == PicamError_None:
            return
        raise cls(err)


def get_string(typ, val):
    string = POINTER(pichar)()
    Error.check(Picam_GetEnumerationString(typ, val, byref(string)))
    ret = cast(string, c_char_p).value.decode()  # decode copies
    Error.check(Picam_DestroyString(string))
    return ret


def get_data(data, num, length, dtype="<u2"):
    data = (pibyte*(num*length)).from_address(data)
    return np.ctypeslib.as_array(data).reshape(num, length).view(dtype)


class Library:
    def initialized(self):
        val = pibln()
        Error.check(Picam_IsLibraryInitialized(byref(val)))
        return val.value

    def initialize(self):
        logger.debug("initialize")
        Error.check(Picam_InitializeLibrary())

    def uninitialize(self):
        logger.debug("uninitialize")
        Error.check(Picam_UninitializeLibrary())

    def __enter__(self):
        if self.initialized():
            raise ValueError("already initialized")
        self.initialize()

    def __exit__(self, exc_type, exc_value, traceback):
        self.uninitialize()


class Camera:
    def __init__(self):
        self._handle = PicamHandle()

    def open_first(self):
        logger.debug("open_first")
        Error.check(Picam_OpenFirstCamera(byref(self._handle)))
        return self

    def __enter__(self):
        assert self._handle
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        logger.debug("close")
        Error.check(Picam_CloseCamera(self._handle))

    def get_id(self):
        cid = PicamCameraID()
        logger.debug("get_id")
        Error.check(Picam_GetCameraID(self._handle, byref(cid)))
        return cid

    def get_int(self, typ):
        val = piint()
        Error.check(Picam_GetParameterIntegerValue(
            self._handle, typ, byref(val)))
        return val.value

    def get_long(self, typ):
        val = pi64s()
        Error.check(Picam_GetParameterIntegerValue(
            self._handle, typ, byref(val)))
        return val.value

    def get_float(self, typ):
        val = piflt()
        Error.check(Picam_GetParameterFloatingPointValue(
            self._handle, typ, byref(val)))
        return val.value

    def set_int(self, typ, value):
        Error.check(Picam_SetParameterIntegerValue(
            self._handle, typ, piint(value)))

    def set_long(self, typ, value):
        Error.check(Picam_SetParameterLargeIntegerValue(
            self._handle, typ, pi64s(value)))

    def set_float(self, typ, value):
        Error.check(Picam_SetParameterFloatingPointValue(
            self._handle, typ, piflt(value)))

    def comitted(self):
        ret = pibln()
        Error.check(Picam_AreParametersCommitted(
            self._handle, byref(ret)))
        return ret.value

    def commit(self):
        failed = POINTER(PicamParameter)()
        failed_count = piint()
        Error.check(Picam_CommitParameters(
            self._handle, byref(failed), byref(failed_count)))
        fails = [failed[i].value for i in range(failed_count.value)]
        Error.check(Picam_DestroyParameters(failed))
        # get_string(PicamEnumeratedType_Parameter, ...)
        return fails

    def acquire(self, num_frames=1, timeout=-1):
        data = PicamAvailableData()
        errors = PicamAcquisitionErrorsMask()
        logger.debug("acquire")
        Error.check(Picam_Acquire(
            self._handle, num_frames, timeout, byref(data), byref(errors)))
        # get_string(PicamEnumeratedType_AcquisitionErrorsMask, errors)
        return data, errors

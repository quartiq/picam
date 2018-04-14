import logging
from contextlib import contextmanager
from ctypes import byref, POINTER, cast, c_char_p

import numpy as np

from picam import *


logger = logging.getLogger(__name__)


class Error(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        try:
            string = Library.get_string(PicamEnumeratedType_Error, self.error)
        except:
            string = "<failed to retrieve error description>"
        return "{} ({})".format(self.error, string)

    @classmethod
    def check(cls, err):
        if err == PicamError_None:
            return
        raise cls(err)


def get_data(data, readout_stride):
    mem = (pibyte*(data.readout_count*readout_stride)).from_address(
        data.initial_readout)
    return np.ctypeslib.as_array(mem).reshape(data.readout_count, -1)


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
            raise ValueError("already initialized elsewhere")
        self.initialize()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.uninitialize()

    @staticmethod
    def get_string(typ, val):
        """Resolve a PiCam enum to a human readable string"""
        string = POINTER(pichar)()
        Error.check(Picam_GetEnumerationString(typ, val, byref(string)))
        ret = cast(string, c_char_p).value.decode()  # decode copies
        Error.check(Picam_DestroyString(string))
        return ret


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

    def get_int(self, parameter):
        val = piint()
        Error.check(Picam_GetParameterIntegerValue(
            self._handle, parameter, byref(val)))
        return val.value

    def get_long(self, parameter):
        val = pi64s()
        Error.check(Picam_GetParameterLargeIntegerValue(
            self._handle, parameter, byref(val)))
        return val.value

    def get_float(self, parameter):
        val = piflt()
        Error.check(Picam_GetParameterFloatingPointValue(
            self._handle, parameter, byref(val)))
        return val.value

    def get_rois(self, parameter=PicamParameter_Rois):
        val = POINTER(PicamRois)()
        Error.check(Picam_GetParameterRoisValue(
            self._handle, parameter, byref(val)))
        vals = val.contents
        roip = vals.roi_array
        rois = []
        for i in range(vals.roi_count):
            x = roip[i].x, roip[i].width, roip[i].x_binning
            y = roip[i].y, roip[i].height, roip[i].y_binning
            rois.append((x, y))
        Error.check(Picam_DestroyRois(val))
        return rois

    def set_int(self, parameter, value):
        Error.check(Picam_SetParameterIntegerValue(
            self._handle, parameter, piint(value)))

    def set_long(self, parameter, value):
        Error.check(Picam_SetParameterLargeIntegerValue(
            self._handle, parameter, pi64s(value)))

    def set_float(self, parameter, value):
        Error.check(Picam_SetParameterFloatingPointValue(
            self._handle, parameter, piflt(value)))

    def set_rois(self, parameter, value):
        val = (PicamRoi*len(value))()
        for i, (x, y) in enumerate(value):
            val[i].x, val[i].width, val[i].x_binning = x
            val[i].y, val[i].height, val[i].y_binning = y
        Error.check(Picam_SetParameterRoisValue(
            self._handle, parameter, byref(PicamRois(val, len(value)))))

    def get_parameter_value_type(self, parameter):
        typ = PicamValueType()
        Error.check(Picam_GetParameterValueType(
            self._handle, parameter, byref(typ)))
        return typ.value

    def get(self, parameter):
        typ = self.get_parameter_value_type(parameter)
        if typ in (
                PicamValueType_Integer,
                PicamValueType_Boolean,
                PicamValueType_Enumeration):
            return self.get_int(parameter)
        elif typ == PicamValueType_LargeInteger:
            return self.get_long(parameter)
        elif typ == PicamValueType_FloatingPoint:
            return self.get_float(parameter)
        elif typ == PicamValueType_Rois:
            return self.get_rois(parameter)
        elif typ == PicamValueType_Pulse:
            return self.get_pulse(parameter)
        elif typ == PicamValueType_Modulations:
            return self.get_modulations(parameter)
        else:
            raise ValueError("unknown parameter value type")

    def set(self, parameter, value):
        typ = self.get_parameter_value_type(parameter)
        if typ in (
                PicamValueType_Integer,
                PicamValueType_Boolean,
                PicamValueType_Enumeration):
            return self.set_int(parameter, value)
        elif typ == PicamValueType_LargeInteger:
            return self.set_long(parameter, value)
        elif typ == PicamValueType_FloatingPoint:
            return self.set_float(parameter, value)
        elif typ == PicamValueType_Rois:
            return self.set_rois(parameter, value)
        elif typ == PicamValueType_Pulse:
            return self.set_pulse(parameter, value)
        elif typ == PicamValueType_Modulations:
            return self.set_modulations(parameter, value)
        else:
            raise ValueError("unknown parameter value type")

    def get_parameters(self):
        parameters = POINTER(PicamParameter)()
        parameters_count = piint()
        Error.check(Picam_GetParameters(
            self._handle, byref(parameters), byref(parameters_count)))
        params = parameters[:parameters_count.value]  # copies
        Error.check(Picam_DestroyParameters(parameters))
        return params

    def get_parameter_value_access(self, parameter):
        val = piint()
        Error.check(Picam_GetParameterValueAccess(
            self._handle, parameter, byref(val)))
        return val.value

    def get_parameter_enumerated_type(self, parameter):
        val = PicamEnumeratedType()
        Error.check(Picam_GetParameterEnumeratedType(
            self._handle, parameter, byref(val)))
        return val.value

    def get_parameter_constraint_type(self, parameter):
        val = piint()
        Error.check(Picam_GetParameterConstraintType(
            self._handle, parameter, byref(val)))
        return val.value

    def get_parameter_range_constraint(
            self, parameter, category=PicamConstraintCategory_Capable):
        c = POINTER(PicamRangeConstraint)()
        Error.check(Picam_GetParameterRangeConstraint(
            self._handle, parameter, category, byref(c)))
        constraint = (c[0].minimum, c[0].maximum, c[0].increment)
        Error.check(Picam_DestroyRangeConstraints(c))
        return constraint

    def get_parameter_collection_constraint(
            self, parameter, category=PicamConstraintCategory_Capable):
        c = POINTER(PicamCollectionConstraint)()
        Error.check(Picam_GetParameterCollectionConstraint(
            self._handle, parameter, category, byref(c)))
        constraint = [c[0].values_array[i] for i in range(c[0].values_count)]
        Error.check(Picam_DestroyCollectionConstraints(c))
        return constraint

    def comitted(self):
        ret = pibln()
        Error.check(Picam_AreParametersCommitted(
            self._handle, byref(ret)))
        return ret.value

    def commit(self):
        failed = POINTER(PicamParameter)()
        failed_count = piint()
        logger.debug("commit")
        try:
            Error.check(Picam_CommitParameters(
                self._handle, byref(failed), byref(failed_count)))
        except Error as err:
            err.fails = [failed[i] for i in range(failed_count.value)]
            raise
        finally:
            Error.check(Picam_DestroyParameters(failed))

    def acquire(self, readout_count=1, timeout=-1):
        data = PicamAvailableData()
        errors = PicamAcquisitionErrorsMask()
        logger.debug("acquire")
        Error.check(Picam_Acquire(
            self._handle, readout_count, timeout, byref(data), byref(errors)))
        return data, errors

    def start_acquisition(self):
        logger.debug("start acquisition")
        Error.check(Picam_StartAcquisition(self._handle))

    def stop_acquisition(self):
        logger.debug("stop acquisition")
        Error.check(Picam_StopAcquisition(self._handle))

    def wait_for_acquisition_update(self, timeout=-1):
        data = PicamAvailableData()
        status = PicamAcquisitionStatus()
        Error.check(Picam_WaitForAcquisitionUpdate(
            self._handle, timeout, byref(data), byref(status)))
        return data, status

    @contextmanager
    def acquisition(self):
        self.start_acquisition()
        try:
            yield
        finally:
            self.stop_acquisition()

import picam as pi
from ctypes import byref, POINTER, cast, c_char_p
import numpy as np

NUM_FRAMES = 5
NO_TIMEOUT = -1

camera = pi.PicamHandle()
cid = pi.PicamCameraID()
string = POINTER(pi.pichar)()
data = pi.PicamAvailableData()
errors = pi.PicamAcquisitionErrorsMask()
readoutstride = pi.piint(0);

def print_data(data, num, length):
    data = cast(data, POINTER(pi.pibyte))
    data = np.asarray(data[:num*length.value], np.dtype(">u2"))
    data = data.reshape(num, -1)
    print(data.shape, data[:, :10])

pi.Picam_InitializeLibrary()
try:
    if pi.Picam_OpenFirstCamera(byref(camera)) == pi.PicamError_None:
        try:
            pi.Picam_GetCameraID(camera, byref(cid))
            pi.Picam_GetEnumerationString(pi.PicamEnumeratedType_Model,
                    cid.model, string)
            print(cast(string, c_char_p).value, cid.serial_number, cid.sensor_name)
            pi.Picam_DestroyString(string)

            pi.Picam_GetParameterIntegerValue(camera,
                    pi.PicamParameter_ReadoutStride, byref(readoutstride))
            if pi.Picam_Acquire(camera, NUM_FRAMES, NO_TIMEOUT, byref(data),
                byref(errors)):
                print("Error: Camera only collected {} frames".format(data.readout_count))
            else:
                print_data(data.initial_readout, NUM_FRAMES, readoutstride)
            for i in range(NUM_FRAMES):
                if pi.Picam_Acquire(camera, 1, NO_TIMEOUT, byref(data), byref(errors)):
                    print("Error: Camera only collected {} frames".format(data.readout_count))
                else:
                    print_data(data.initial_readout, 1, readoutstride)
        finally:
            pi.Picam_CloseCamera(camera)
finally:
    pi.Picam_UninitializeLibrary()

from ctypes import string_at
import sys
import clr
import numpy as np

from System.Runtime.InteropServices import GCHandle, GCHandleType


assembly_path = r".\BeamageCsh\BeamageApi\bin\Debug"
sys.path.append(assembly_path)
clr.AddReference("BeamageSDK")

from BeamageApiCode import BSDK

BSDK = BSDK() # Init class Beamage from C# dll

class Beamage:
    def __init__(self): # Init properties of the class
        self.connect = BSDK.AutoConnect() # Connect to the camera
        self.width, self.height = 2048, 2048 # Init size of the area
        self.beforArray = np.zeros(( self.width, self.height ))

    def __grab_image(self): # Method of geting array from buffer (fast)
        arr = BSDK.camera.camImg.GetLastImageArray()
        src_hndl = GCHandle.Alloc(arr, GCHandleType.Pinned)
        try:
            src_ptr = src_hndl.AddrOfPinnedObject().ToInt64()
            dest = np.fromstring(string_at(src_ptr, len(arr)*8)) # note: 8 is size of double...
        finally:
            if src_hndl.IsAllocated: 
                src_hndl.Free()
                #self.stop()

        return dest.reshape(self.height, self.width)


    def grab(self): # grab new image with check rewrite last image from buffer
        k = 0
        dataNew = self.__grab_image()
        while ( np.array_equal( dataNew, self.beforArray ) ):
            dataNew = self.__grab_image()
            k+=1
            #print("Они равны")
        #print("Они не равны", k)
        self.beforArray = dataNew
        return dataNew.T, dataNew.max()/4096 * 100

    def autoExposition(self, saturation, flag=False):
        if (flag):
            q = 4
            if ( saturation > 95 ):
                t0 = BSDK.camSettings.cameraExposureTime 
                t = t0 / q
                BSDK.camera.SetCameraManualExposureTime(t)
            elif ( saturation < 80 ):
                t0 = BSDK.camSettings.cameraExposureTime 
                t = t0 * q
                BSDK.camera.SetCameraManualExposureTime(t)


    def start(self):
        BSDK.camera.Run()

    def stop(self):
        BSDK.camera.StopRun()

    def save(self, path, name):
        buffer = 0
        for i in np.arange(0, 9):
            buffer += self.grab()[0]
        buffer /= i
        np.savez_compressed(str(path) + '/' + str(name) + '.npz', a=buffer)

    def setExposition(self, value):
        BSDK.camera.SetCameraManualExposureTime(value)

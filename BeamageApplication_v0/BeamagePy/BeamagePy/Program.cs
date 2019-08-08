using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using BeamageApi; // import reference from namespace BeamageApi

namespace BeamagePyC
{
    public class BeamageSdk
    {
        BSDK bsdk; // Beamage SDK object
        public void BeamageConnect()
        {
            bsdk = new BSDK(); // Create Beamage SDK
            bsdk.AutoConnect(); // This method will connect the first camera found by the drivers
                                // Resize the picture box if we have a Beamage-4M sensor
            bsdk.camera.SetToAutoExposure(false);
            bsdk.AttachedStateChanged += new EventHandler(attachedEvent);
            bsdk.RemoveStateChanged += new EventHandler(removeEvent);
        }
        public void BeamageRun()
        {
            bsdk.camera.Run();
        }
        public void BeamageStop()
        {
            bsdk.camera.StopRun();
        }

        public string BeamageObtaineExpositionTime()
        {
            return bsdk.camera.cameraFps.ToString("0.00");
        }

        public int[] BeamageGrubImage()
        {
            return Convert.ToInt64(bsdk.camera.camImg.GetLastImageArray());
        }
        public int[] BeamageGrubSize()
        {
            int[] size = new int[2];
            size[0] = bsdk.camera.camImg.width;
            size[1] = bsdk.camera.camImg.height;
            return size;
        }
        public void SetExposureTime(float exposureTime)
        {
            bsdk.camera.SetCameraManualExposureTime(exposureTime);
        }
        private void removeEvent(object sender, EventArgs e)
        {
            // A camera has been disconnect from this PC

            // add code
        }

        private void attachedEvent(object sender, EventArgs e)
        {
            // A camera has been connect from this PC

            // add code
        }
    }   
}

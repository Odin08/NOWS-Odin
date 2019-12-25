// Decompiled with JetBrains decompiler
// Type: BeamageApi.BCamProperties
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

using CyUSB;
using System.Text;

namespace BeamageApiCode
{
  public class BCamProperties
  {
    internal BCamCalibration calibration = new BCamCalibration();

    internal bool sensor4M { get; set; }

    internal string VendorID { get; private set; }

    internal string ProductID { get; private set; }

    internal string FriendlyName { get; private set; }

    internal BCamProperties()
    {
      this.Reset();
    }

    internal void Reset()
    {
      this.sensor4M = false;
    }

    internal void Init(CyUSBDevice usbDevice)
    {
      this.FriendlyName = usbDevice.FriendlyName;
      this.ProductID = usbDevice.ProductID.ToString();
      this.VendorID = usbDevice.VendorID.ToString();
    }

    public string GetSerialNumber()
    {
      return Encoding.UTF8.GetString(this.calibration.lpszSerialNumber);
    }

    public bool Is4mSensor()
    {
      return this.sensor4M;
    }
  }
}

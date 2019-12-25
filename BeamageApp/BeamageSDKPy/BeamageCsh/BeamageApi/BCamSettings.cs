// Decompiled with JetBrains decompiler
// Type: BeamageApi.BCamSettings
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

namespace BeamageApiCode
{
  public class BCamSettings
  {

    internal int addressignValue { get; set; }

    internal int addressignValueTemp { get; set; }

    internal int bitDepth { get; set; }

    internal int pixAdressingMode { get; set; }

    internal int pixAdressingModeTemp { get; set; }

    internal float cameraExposureTime { get; set; }

    internal bool externalTrigger { get; set; }

    public BCamSettings()
    {
      this.bitDepth = 12;
      this.addressignValueTemp = 1;
      this.addressignValue = 1;
      this.pixAdressingMode = 0;
      this.pixAdressingModeTemp = 0;
      this.externalTrigger = false;
    }

    public bool HasAdressingChanged()
    {
      if (this.addressignValue == this.addressignValueTemp)
        return this.pixAdressingMode != this.pixAdressingModeTemp;
      return true;
    }

    internal void ChangeAdressing()
    {
      this.addressignValue = this.addressignValueTemp;
      this.pixAdressingMode = this.pixAdressingModeTemp;
    }
  }
}

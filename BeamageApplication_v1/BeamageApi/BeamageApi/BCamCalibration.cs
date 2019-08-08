// Decompiled with JetBrains decompiler
// Type: BeamageApi.BCamCalibration
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

namespace BeamageApiCode
{
  internal class BCamCalibration
  {
    internal byte[] lpszSerialNumber = new byte[6];
    internal byte[] calibrationTime = new byte[8];
    internal byte nVersion;
    internal byte nReserved1;
    internal byte nVersionFirmwareMajor;
    internal byte nVersionFirmwareMinor;
    internal byte nReserved2;
    internal byte lpszRegister98_10;
    internal byte lpszRegister99_10;
    internal byte lpszRegister100_10;
    internal byte lpszRegister101_10;
    internal byte lpszRegister102_10;
    internal byte lpszRegister103_10;
    internal byte lpszRegister98_12;
    internal byte lpszRegister99_12;
    internal byte lpszRegister100_12;
    internal byte lpszRegister101_12;
    internal byte lpszRegister102_12;
    internal byte lpszRegister103_12;
    internal byte dontKnow;
    internal byte lpszRegister121_10;
    internal byte lpszRegister121_12;

    internal BCamCalibration()
    {
      this.lpszRegister98_10 = (byte) 108;
      this.lpszRegister99_10 = (byte) 108;
      this.lpszRegister100_10 = (byte) 139;
      this.lpszRegister101_10 = (byte) 63;
      this.lpszRegister102_10 = (byte) 1;
      this.lpszRegister103_10 = (byte) 57;
      this.lpszRegister121_10 = (byte) 0;
      this.lpszRegister98_12 = (byte) 109;
      this.lpszRegister99_12 = (byte) 109;
      this.lpszRegister100_12 = (byte) 134;
      this.lpszRegister101_12 = (byte) 62;
      this.lpszRegister102_12 = (byte) 1;
      this.lpszRegister103_12 = (byte) 57;
      this.lpszRegister121_12 = (byte) 0;
      this.lpszSerialNumber[0] = (byte) 0;
      this.lpszSerialNumber[1] = (byte) 0;
      this.lpszSerialNumber[2] = (byte) 0;
      this.lpszSerialNumber[3] = (byte) 0;
      this.lpszSerialNumber[4] = (byte) 0;
      this.lpszSerialNumber[5] = (byte) 0;
      this.nVersion = (byte) 2;
      this.nVersionFirmwareMajor = (byte) 1;
      this.nVersionFirmwareMinor = (byte) 0;
    }

    internal void Read(byte[] registerTemp)
    {
      this.nVersion = registerTemp[(int) byte.MaxValue];
      this.nReserved1 = registerTemp[254];
      this.nVersionFirmwareMajor = registerTemp[253];
      this.nVersionFirmwareMinor = registerTemp[252];
      this.nReserved2 = registerTemp[251];
      this.lpszRegister98_10 = registerTemp[250];
      this.lpszRegister99_10 = registerTemp[249];
      this.lpszRegister100_10 = registerTemp[248];
      this.lpszRegister101_10 = registerTemp[247];
      this.lpszRegister102_10 = registerTemp[246];
      this.lpszRegister103_10 = registerTemp[245];
      this.lpszRegister98_12 = registerTemp[244];
      this.lpszRegister99_12 = registerTemp[243];
      this.lpszRegister100_12 = registerTemp[242];
      this.lpszRegister101_12 = registerTemp[241];
      this.lpszRegister102_12 = registerTemp[240];
      this.lpszRegister103_12 = registerTemp[239];
      this.lpszSerialNumber[0] = registerTemp[238];
      this.lpszSerialNumber[1] = registerTemp[237];
      this.lpszSerialNumber[2] = registerTemp[236];
      this.lpszSerialNumber[3] = registerTemp[235];
      this.lpszSerialNumber[4] = registerTemp[234];
      this.lpszSerialNumber[5] = registerTemp[233];
      this.dontKnow = registerTemp[232];
      this.calibrationTime[0] = registerTemp[231];
      this.calibrationTime[1] = registerTemp[230];
      this.calibrationTime[2] = registerTemp[229];
      this.calibrationTime[3] = registerTemp[228];
      this.calibrationTime[4] = registerTemp[227];
      this.calibrationTime[5] = registerTemp[226];
      this.calibrationTime[6] = registerTemp[225];
      this.calibrationTime[7] = registerTemp[224];
      if (this.nVersion != (byte) 2)
      {
        this.lpszRegister121_10 = (byte) 0;
        this.lpszRegister121_12 = (byte) 0;
      }
      else
      {
        this.lpszRegister121_10 = registerTemp[223];
        this.lpszRegister121_12 = registerTemp[222];
      }
    }

    internal void Write(byte[] registerTemp)
    {
      registerTemp[(int) byte.MaxValue] = this.nVersion;
      registerTemp[254] = this.nReserved1;
      registerTemp[253] = this.nVersionFirmwareMajor;
      registerTemp[252] = this.nVersionFirmwareMinor;
      registerTemp[251] = this.nReserved2;
      registerTemp[250] = this.lpszRegister98_10;
      registerTemp[249] = this.lpszRegister99_10;
      registerTemp[248] = this.lpszRegister100_10;
      registerTemp[247] = this.lpszRegister101_10;
      registerTemp[246] = this.lpszRegister102_10;
      registerTemp[245] = this.lpszRegister103_10;
      registerTemp[244] = this.lpszRegister98_12;
      registerTemp[243] = this.lpszRegister99_12;
      registerTemp[242] = this.lpszRegister100_12;
      registerTemp[241] = this.lpszRegister101_12;
      registerTemp[240] = this.lpszRegister102_12;
      registerTemp[239] = this.lpszRegister103_12;
      registerTemp[238] = this.lpszSerialNumber[0];
      registerTemp[237] = this.lpszSerialNumber[1];
      registerTemp[236] = this.lpszSerialNumber[2];
      registerTemp[235] = this.lpszSerialNumber[3];
      registerTemp[234] = this.lpszSerialNumber[4];
      registerTemp[233] = this.lpszSerialNumber[5];
      registerTemp[232] = this.dontKnow;
      registerTemp[231] = this.calibrationTime[0];
      registerTemp[230] = this.calibrationTime[1];
      registerTemp[229] = this.calibrationTime[2];
      registerTemp[228] = this.calibrationTime[3];
      registerTemp[227] = this.calibrationTime[4];
      registerTemp[226] = this.calibrationTime[5];
      registerTemp[225] = this.calibrationTime[6];
      registerTemp[224] = this.calibrationTime[7];
      if (this.nVersion != (byte) 2)
      {
        registerTemp[223] = (byte) 0;
        registerTemp[222] = (byte) 0;
      }
      else
      {
        registerTemp[223] = this.lpszRegister121_10;
        registerTemp[222] = this.lpszRegister121_12;
      }
    }
  }
}

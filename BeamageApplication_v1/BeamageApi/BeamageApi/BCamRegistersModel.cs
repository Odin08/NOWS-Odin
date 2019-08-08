// Decompiled with JetBrains decompiler
// Type: BeamageApi.BCamRegistersModel
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

using System.Collections.Generic;
using System.Linq;

namespace BeamageApiCode
{
  public class BCamRegistersModel
  {
    public byte[] registers = new byte[256];
    public byte[] registerTemp = new byte[256];

    public BCamRegistersModel(bool sensor4M)
    {
      this.Reset(sensor4M);
    }

    public void Reset(bool sensor4M)
    {
      this.registerTemp = Enumerable.Repeat<byte>((byte) 0, 256).ToArray<byte>();
      if (sensor4M)
      {
        this.registers[1] = (byte) 0;
        this.registers[2] = (byte) 8;
        this.registers[86] = (byte) 14;
      }
      else
      {
        this.registers[1] = (byte) 64;
        this.registers[2] = (byte) 4;
        this.registers[86] = (byte) 8;
      }
      this.registers[39] = (byte) 1;
      this.registers[41] = (byte) 0;
      this.registers[42] = (byte) 175;
      this.registers[43] = (byte) 75;
      this.registers[44] = (byte) 0;
      this.registers[48] = (byte) 1;
      this.registers[51] = (byte) 1;
      this.registers[54] = (byte) 1;
      this.registers[55] = (byte) 1;
      this.registers[56] = (byte) 175;
      this.registers[57] = (byte) 75;
      this.registers[58] = (byte) 0;
      this.registers[62] = (byte) 1;
      this.registers[65] = (byte) 1;
      this.registers[68] = (byte) 1;
      this.registers[69] = (byte) 1;
      this.registers[70] = (byte) 1;
      this.registers[72] = (byte) 2;
      this.registers[73] = (byte) 10;
      this.registers[74] = (byte) 1;
      this.registers[75] = (byte) 8;
      this.registers[76] = (byte) 8;
      this.registers[78] = (byte) 85;
      this.registers[80] = (byte) 34;
      this.registers[81] = (byte) 34;
      this.registers[82] = (byte) 7;
      this.registers[83] = (byte) 8;
      this.registers[84] = (byte) 4;
      this.registers[85] = (byte) 1;
      this.registers[87] = (byte) 12;
      this.registers[88] = (byte) 64;
      this.registers[89] = (byte) 96;
      this.registers[90] = (byte) 96;
      this.registers[91] = (byte) 64;
      this.registers[92] = (byte) 96;
      this.registers[93] = (byte) 96;
      this.registers[94] = (byte) 101;
      this.registers[95] = (byte) 106;
      this.registers[96] = (byte) 96;
      this.registers[97] = (byte) 96;
      this.registers[98] = (byte) 109;
      this.registers[99] = (byte) 109;
      this.registers[100] = (byte) 134;
      this.registers[101] = (byte) 62;
      this.registers[102] = (byte) 1;
      this.registers[103] = (byte) 57;
      this.registers[104] = (byte) 8;
      this.registers[105] = (byte) 8;
      this.registers[106] = (byte) 8;
      this.registers[107] = (byte) 8;
      this.registers[108] = (byte) 2;
      this.registers[109] = (byte) 4;
      this.registers[111] = (byte) 0;
      this.registers[112] = (byte) 2;
      this.registers[113] = (byte) 1;
      this.registers[114] = (byte) 1;
      this.registers[115] = (byte) 1;
      this.registers[116] = (byte) 43;
      this.registers[117] = (byte) 4;
      this.registers[118] = (byte) 0;
      this.registers[123] = (byte) 98;
      this.registers[129] = (byte) 0;
      this.registers[134] = (byte) 1;
      this.registers[140] = (byte) 1;
    }

    internal object GetRegisterValue(int index)
    {
      return (object) this.registers[index];
    }

    internal void SetNoExternalTrigger()
    {
      this.registers[128] |= (byte) 128;
      this.registers[134] &= (byte) 223;
      this.registers[129] &= (byte) 191;
    }

    internal void SetExternalTrigger()
    {
      this.registers[134] |= (byte) 32;
      this.registers[129] |= (byte) 64;
    }

    internal void FinishUpdateBitDepth()
    {
      this.registers[74] = (byte) 1;
      this.registers[82] = (byte) 7;
      this.registers[113] = (byte) 1;
      this.registers[114] = (byte) 1;
      this.registers[115] = (byte) 1;
    }

    internal void GrabFrameBeginWithExternalTrigger(int nCounter)
    {
      this.registers[146] = (byte) (nCounter >> 16 & (int) byte.MaxValue);
      this.registers[145] = (byte) (nCounter >> 8 & (int) byte.MaxValue);
      this.registers[144] = (byte) (nCounter & (int) byte.MaxValue);
    }

    internal void Set12BitDepthRegisters(ref BCamCalibration calibration)
    {
      this.registers[72] = (byte) 2;
      this.registers[80] = (byte) 34;
      this.registers[81] = (byte) 34;
      this.registers[98] = calibration.lpszRegister98_12;
      this.registers[99] = calibration.lpszRegister99_12;
      this.registers[100] = calibration.lpszRegister100_12;
      this.registers[101] = calibration.lpszRegister101_12;
      this.registers[102] = calibration.lpszRegister102_12;
      this.registers[103] = calibration.lpszRegister103_12;
      this.registers[121] = calibration.lpszRegister121_12;
      this.registers[111] = (byte) 0;
      this.registers[112] = (byte) 2;
      this.registers[116] = (byte) 43;
      this.registers[117] = (byte) 4;
      this.registers[129] = (byte) 0;
    }

    internal void SetPixelAdressingAverage(bool sensor4M)
    {
      this.registers[1] = sensor4M ? (byte) 0 : (byte) 64;
      this.registers[2] = sensor4M ? (byte) 8 : (byte) 4;
      this.registers[35] = (byte) 0;
      this.registers[37] = (byte) 0;
      this.registers[140] = (byte) 1;
      this.registers[134] |= (byte) 128;
    }

    internal void SetPixelAdressingDecimate(bool sensor4M)
    {
      this.registers[1] = sensor4M ? (byte) 0 : (byte) 32;
      this.registers[2] = sensor4M ? (byte) 4 : (byte) 2;
      this.registers[35] = (byte) 1;
      this.registers[37] = (byte) 1;
      this.registers[140] = (byte) 2;
      this.registers[134] &= (byte) 127;
    }

    internal void SetPixelAdressingNone(bool sensor4M)
    {
      this.registers[1] = sensor4M ? (byte) 0 : (byte) 64;
      this.registers[2] = sensor4M ? (byte) 8 : (byte) 4;
      this.registers[35] = (byte) 0;
      this.registers[37] = (byte) 0;
      this.registers[140] = (byte) 1;
      this.registers[134] &= (byte) 127;
    }

    internal void Set10BitDepthRegisters(ref BCamCalibration calibration)
    {
      this.registers[72] = (byte) 0;
      this.registers[80] = byte.MaxValue;
      this.registers[81] = byte.MaxValue;
      this.registers[98] = calibration.lpszRegister98_10;
      this.registers[99] = calibration.lpszRegister99_10;
      this.registers[100] = calibration.lpszRegister100_10;
      this.registers[101] = calibration.lpszRegister101_10;
      this.registers[102] = calibration.lpszRegister102_10;
      this.registers[121] = calibration.lpszRegister121_10;
      this.registers[103] = calibration.lpszRegister103_10;
      this.registers[111] = (byte) 1;
      this.registers[112] = (byte) 0;
      this.registers[116] = (byte) 41;
      this.registers[117] = (byte) 8;
      this.registers[129] = (byte) 8;
    }

    internal int GetCount()
    {
      return ((IEnumerable<byte>) this.registers).Count<byte>();
    }

    internal void SetExposureTime(int nRegister)
    {
      this.registers[44] = (byte) (nRegister >> 16 & (int) byte.MaxValue);
      this.registers[43] = (byte) (nRegister >> 8 & (int) byte.MaxValue);
      this.registers[42] = (byte) (nRegister & (int) byte.MaxValue);
    }
  }
}

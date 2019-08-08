// Decompiled with JetBrains decompiler
// Type: BeamageApi.BCamComLayer
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

using CyUSB;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;

namespace BeamageApiCode
{
  internal class BCamComLayer
  {
    internal byte[] overlap = new byte[16];
    internal BCamRegistersModel camRegisters;
    internal BDebugOutput debugOutput;
    internal byte[] buffers;
    internal byte[] captureImageBuffer;
    internal int cameraBufferLength;
    internal int cameraBufferHeight;
    private CyFX3Device fx3Device;
    private CyUSBEndPoint OutEndpt;
    private CyUSBEndPoint InEndpt;

    internal bool USB3 { get; set; }

    internal bool bootLoaderCurrentlyRunning { get; private set; }

    internal BCamComLayer(CyFX3Device cyFX3Device, bool sensor4M)
    {
      this.fx3Device = cyFX3Device;
      this.debugOutput = new BDebugOutput();
      this.camRegisters = new BCamRegistersModel(sensor4M);
      this.LoadBemageFirmwareImg();
      Thread.Sleep(10);
    }

    internal bool SendRegisters()
    {
      if (this.debugOutput.debugOutput)
        this.debugOutput.ExportRegistersCommands(ref this.camRegisters);
      int count = this.camRegisters.GetCount();
      Thread.Sleep(5);
      return this.OutEndpt.XferData(ref this.camRegisters.registers, ref count);
    }

    private void InitEndInPoints(CyUSBDevice usbDevice)
    {
      int endPointCount = (int) usbDevice.EndPointCount;
      int index1 = 0;
      int index2 = 0;
      for (int index3 = 1; index3 < endPointCount; ++index3)
      {
        if (((int) usbDevice.EndPoints[index3].Address & 128) == 128)
          index1 = index3;
        else
          index2 = index3;
      }
      if (endPointCount == 3)
      {
        this.InEndpt = usbDevice.USBCfgs[0].Interfaces[0].EndPoints[index1];
        this.OutEndpt = usbDevice.USBCfgs[0].Interfaces[0].EndPoints[index2];
      }
      else
      {
        this.InEndpt = (CyUSBEndPoint) null;
        this.OutEndpt = (CyUSBEndPoint) null;
      }
    }

    internal void Init(CyUSBDevice usbDevice)
    {
      this.USB3 = usbDevice.bSuperSpeed;
      this.InitEndInPoints(usbDevice);
      this.cameraBufferLength = this.InEndpt.MaxPktSize;
      this.USB3 = this.cameraBufferLength != 512;
      this.buffers = new byte[this.cameraBufferLength];
    }

    internal bool ReadCMOSRegisters(ref BCamProperties camProperties, int maxCameraHeightSize)
    {
      if (!this.SendRegisters())
        return false;
      this.camRegisters.registers[128] = (byte) 2;
      if (!this.SendRegisters())
        return false;
      this.camRegisters.registerTemp = Enumerable.Repeat<byte>((byte) 0, 256).ToArray<byte>();
      Thread.Sleep(100);
      int len = ((IEnumerable<byte>) this.camRegisters.registerTemp).Count<byte>();
      if (!this.InEndpt.XferData(ref this.camRegisters.registerTemp, ref len))
        return false;
      camProperties.sensor4M = this.camRegisters.registerTemp[125] > (byte) 60;
      this.cameraBufferHeight = maxCameraHeightSize;
      this.camRegisters.registers[128] = (byte) 0;
      return true;
    }

    internal void SendCalibration(ref BCamCalibration calibration)
    {
      this.camRegisters.registerTemp = Enumerable.Repeat<byte>((byte) 0, 256).ToArray<byte>();
      calibration.Write(this.camRegisters.registerTemp);
      for (int index = 216; index <= (int) byte.MaxValue; ++index)
        this.camRegisters.registers[index] = this.camRegisters.registerTemp[index];
      this.SendRegisters();
    }

    internal bool ReadCalibration(ref BCamCalibration calibration)
    {
      if (!this.SendRegisters())
        return false;
      this.camRegisters.registers[129] &= (byte) 254;
      this.camRegisters.registers[128] = (byte) 0;
      if (!this.SendRegisters())
        return false;
      this.camRegisters.registerTemp = Enumerable.Repeat<byte>((byte) 0, 256).ToArray<byte>();
      this.ReadEEPROM(ref calibration);
      return true;
    }

    private bool ReadEEPROM(ref BCamCalibration calibration)
    {
      this.camRegisters.registers[129] |= (byte) 1;
      if (!this.SendRegisters())
        return false;
      if (this.USB3)
        Thread.Sleep(20);
      else
        Thread.Sleep(100);
      this.camRegisters.registerTemp = Enumerable.Repeat<byte>((byte) 0, 256).ToArray<byte>();
      int len = ((IEnumerable<byte>) this.camRegisters.registerTemp).Count<byte>();
      if (this.InEndpt.XferData(ref this.camRegisters.registerTemp, ref len))
        this.camRegisters.registers[129] &= (byte) 253;
      this.camRegisters.registers[129] &= (byte) 254;
      if (!this.SendRegisters())
        return false;
      calibration.Read(this.camRegisters.registerTemp);
      for (int index = 148; index < 224; ++index)
        this.camRegisters.registers[index] = this.camRegisters.registerTemp[index];
      return true;
    }

    private void LoadBemageFirmwareImg()
    {
      this.bootLoaderCurrentlyRunning = this.fx3Device.IsBootLoaderRunning();
      if (!this.bootLoaderCurrentlyRunning)
        return;
      this.fx3Device.GetFwErrorString(this.fx3Device.DownloadFw("Beamage.img", FX3_FWDWNLOAD_MEDIA_TYPE.RAM));
    }

    internal void GrabBuffer(int NumberOfLinesToTransfer)
    {
      bool flag = true;
      int num = 0;
      byte[] numArray = new byte[this.cameraBufferLength];
      for (; num < NumberOfLinesToTransfer & flag; ++num)
      {
        flag = this.InEndpt.XferData(ref this.buffers, ref this.cameraBufferLength);
        Array.Copy((Array) this.buffers, 0, (Array) this.captureImageBuffer, num * this.cameraBufferLength, this.cameraBufferLength);
      }
    }

    internal void InitBuffers(int maxHeightSize)
    {
      this.captureImageBuffer = new byte[2048 * maxHeightSize * 2];
    }

    internal void SetExternalTrigger()
    {
      this.camRegisters.SetExternalTrigger();
      this.SendRegisters();
    }

    internal void SetNoExternalTrigger()
    {
      this.camRegisters.SetNoExternalTrigger();
      this.SendRegisters();
      Thread.Sleep(1);
      this.camRegisters.registers[128] &= (byte) 127;
      this.SendRegisters();
    }

    internal void UpdateROI(int _nLine, int _nLineStart)
    {
      this.camRegisters.registers[1] = (byte) (_nLine & (int) byte.MaxValue);
      this.camRegisters.registers[2] = (byte) (_nLine >> 8);
      this.camRegisters.registers[3] = (byte) (_nLineStart & (int) byte.MaxValue);
      this.camRegisters.registers[4] = (byte) (_nLineStart >> 8);
    }
  }
}

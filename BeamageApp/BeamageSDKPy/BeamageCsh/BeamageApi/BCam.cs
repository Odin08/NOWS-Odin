// Decompiled with JetBrains decompiler
// Type: BeamageApi.BCam
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

using CyUSB;
using System;
using System.Diagnostics;
using System.Threading;

namespace BeamageApiCode
{
  public class BCam : IDisposable
  {
    private bool firstAcquisition = true;
    private float imageDelayedMaxValue = -1f;
    public BCamImg camImg;
    public BCamProperties camProperties;
    public BCamSettings camSettings;
    internal BCamComLayer camComLayer;
    private bool singleFrame;
    private bool capture;

    public float cameraFps { get; private set; }

    internal bool exposureTimeHasBeenChanged { get; private set; }

    public bool Disposed { get; private set; }

    internal BCam(CyFX3Device cyFX3Device)
    {
      this.camProperties = new BCamProperties();
      this.camSettings = new BCamSettings();
      this.camComLayer = new BCamComLayer(cyFX3Device, this.camProperties.sensor4M);
    }

    public event EventHandler NewImageEvent;

    protected virtual void OnNewImageEvent()
    {
      if (this.NewImageEvent == null)
        return;
      this.NewImageEvent((object) this, EventArgs.Empty);
    }

    public void Dispose()
    {
      this.Dispose(true);
      GC.SuppressFinalize((object) this);
    }

    protected virtual void Dispose(bool disposing)
    {
      if (this.Disposed)
        return;
      if (disposing)
        this.camImg.Dispose();
      this.Disposed = true;
    }

    internal void Init(CyUSBDevice usbDevice)
    {
      this.camProperties.Init(usbDevice);
      this.camComLayer.Init(usbDevice);
      this.ReadCMOSRegisters();
      this.ReadCalibration();
      this.camComLayer.SendCalibration(ref this.camProperties.calibration);
      this.camImg = new BCamImg(2048, this.GetImageMaxHeightSize());
    }

    private bool ReadCMOSRegisters()
    {
      this.UpdateBitDepth();
      this.UpdatePixAdressingMode();
      return this.camComLayer.ReadCMOSRegisters(ref this.camProperties, this.GetImageMaxHeightSize());
    }

    private bool ReadCalibration()
    {
      this.UpdateBitDepth();
      this.UpdatePixAdressingMode();
      return this.camComLayer.ReadCalibration(ref this.camProperties.calibration);
    }

    internal void Connect()
    {
      this.camSettings.cameraExposureTime = 200f;
      this.SetTexp(200f);
      this.camComLayer.InitBuffers(this.GetImageMaxHeightSize());
      this.exposureTimeHasBeenChanged = false;
    }

    public void SetCameraManualExposureTime(float exposureTime)
    {
      this.camSettings.cameraExposureTime = exposureTime;
      this.exposureTimeHasBeenChanged = true;
    }

    private int GetImageMaxHeightSize()
    {
      return !this.camProperties.sensor4M ? 1088 : 2048;
    }

    private void SetROI(int top, int left, int bottom, int right)
    {
    }

    internal void UpdateBitDepth()
    {
      switch (this.camSettings.bitDepth)
      {
        case 10:
          this.camComLayer.camRegisters.Set10BitDepthRegisters(ref this.camProperties.calibration);
          break;
        case 12:
          this.camComLayer.camRegisters.Set12BitDepthRegisters(ref this.camProperties.calibration);
          break;
      }
      this.camComLayer.camRegisters.FinishUpdateBitDepth();
    }

    internal void GrabFrameBegin()
    {
      this.UpdateROI(0, 0, this.GetImageMaxHeightSize(), 2048);
      this.UpdateBitDepth();
      this.UpdatePixAdressingMode();
      this.UpdateTrigger();
      if (this.camSettings.externalTrigger)
      {
        this.camComLayer.camRegisters.GrabFrameBeginWithExternalTrigger((int) ((double) this.camSettings.cameraExposureTime * 150000000.0 / (double) this.camSettings.bitDepth));
        this.camComLayer.SendRegisters();
      }
      this.camComLayer.camRegisters.registers[128] |= (byte) 1;
      this.camComLayer.SendRegisters();
    }

    internal void UpdatePixAdressingMode()
    {
      if (!this.camSettings.HasAdressingChanged())
        return;
      this.camSettings.ChangeAdressing();
      switch (this.camSettings.pixAdressingMode)
      {
        case 0:
          this.camComLayer.camRegisters.SetPixelAdressingNone(this.camProperties.sensor4M);
          this.SetROI(0, this.GetImageMaxHeightSize(), 2048, 2048);
          break;
        case 1:
          this.camComLayer.camRegisters.SetPixelAdressingAverage(this.camProperties.sensor4M);
          this.SetROI(this.GetImageMaxHeightSize() / 2, 0, this.GetImageMaxHeightSize(), 1024);
          break;
        case 2:
          this.camComLayer.camRegisters.SetPixelAdressingDecimate(this.camProperties.sensor4M);
          this.SetROI(this.GetImageMaxHeightSize() / 2, 0, this.GetImageMaxHeightSize(), 1024);
          break;
      }
    }

    public void Run()
    {
      this.capture = true;
      this.singleFrame = false;
      new Thread(new ThreadStart(this.Grab)).Start();
    }

    public void StopRun()
    {
      this.capture = false;
    }


    private void SetTexp(float fExposureTime)
    {
      if ((double) fExposureTime < 0.0599999986588955)
        fExposureTime = 0.06f;
      if ((double) fExposureTime > 5000.0)
        fExposureTime = 5000f;
      this.camSettings.cameraExposureTime = fExposureTime;
      fExposureTime /= 1000f;
      int nRegister = (int) ((double) fExposureTime / (129.0 * (1.0 / (150000000.0 / (double) this.camSettings.bitDepth))) - 4.3);
      if (nRegister < 1)
        nRegister = 1;
      if (nRegister >= 0)
        this.camComLayer.camRegisters.SetExposureTime(nRegister);
      this.camComLayer.SendRegisters();
    }

    private void ChangeExposureTime()
    {
      if (!this.exposureTimeHasBeenChanged)
        return;
      this.SetTexp(this.camSettings.cameraExposureTime);
      this.exposureTimeHasBeenChanged = false;
      this.imageDelayedMaxValue = -1f;
      
    }

    public void GrabOneFrame()
    {
      this.capture = true;
      this.singleFrame = true;
      new Thread(new ThreadStart(this.Grab)).Start();
    }

    internal void Grab()
    {
      Stopwatch stopwatch = new Stopwatch();
      while (this.capture)
      {
        stopwatch.Reset();
        stopwatch.Start();
        if (this.firstAcquisition)
        {
          this.UpdatePixAdressingMode();
          this.camComLayer.SendRegisters();
          this.firstAcquisition = false;
        }
        this.ChangeExposureTime();
        this.GrabFrameBegin();
        this.camComLayer.GrabBuffer(this.GetNumberOfLinesToTransfer());
        this.GrabFrameEnd();
        this.camComLayer.captureImageBuffer.CopyTo((Array) this.camImg.imageBuffer, 0);
        if (this.singleFrame)
          this.capture = false;
        stopwatch.Stop();
        this.cameraFps = 1000f / (float) stopwatch.ElapsedMilliseconds;
        this.OnNewImageEvent();
      }
    }

    private void GrabFrameEnd()
    {
      this.camComLayer.camRegisters.registers[128] = (byte) 0;
      this.camComLayer.SendRegisters();
    }

    private int GetNumberOfLinesToTransfer()
    {
      return 4096 * this.GetImageMaxHeightSize() / this.camComLayer.cameraBufferLength;
    }

    private void UpdateROI(int top, int left, int bottom, int right)
    {
      int _nLineStart = this.GetImageMaxHeightSize() - bottom;
      int _nLine = (int) (32.0 * Math.Ceiling((double) (bottom - top) / 32.0));
      if (_nLine >= this.GetImageMaxHeightSize())
        _nLine = this.GetImageMaxHeightSize();
      this.camComLayer.UpdateROI(_nLine, _nLineStart);
    }

    private void UpdateTrigger()
    {
      if (this.camSettings.externalTrigger)
        this.camComLayer.SetExternalTrigger();
      else
        this.camComLayer.SetNoExternalTrigger();
    }
  }
}

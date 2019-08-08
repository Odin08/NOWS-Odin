// Decompiled with JetBrains decompiler
// Type: BeamageApi.BSDK
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

using CyUSB;
using System;
using System.Collections.Generic;
using System.Threading;

namespace BeamageApiCode
{
  public class BSDK : IDisposable
  {
    public BErrorsManager errorManager = new BErrorsManager();
    public int cameraNumber = -1;
    private USBDeviceList usbDevices = new USBDeviceList((byte) 1);
    private List<BCam> cameras = new List<BCam>();
    private bool isConnected;

    public event EventHandler AttachedStateChanged;

    public event EventHandler RemoveStateChanged;

    public bool Disposed { get; private set; }


    public BSDK(bool autoConnect = false, int serialNumber = 0)
    {
      this.CyUSBDll();
      this.usbDevices.DeviceAttached += new EventHandler(this.usbDevices_DeviceAttached);
      this.usbDevices.DeviceRemoved += new EventHandler(this.usbDevices_DeviceRemoved);
    }

    private void CyUSBDll()
    {
    }

    public BCam camera
    {
      get
      {
        return this.cameras[this.cameraNumber];
      }
      private set
      {
        this.camera = this.cameras[this.cameraNumber];
      }
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
      {
        this.cameras.ForEach((Action<BCam>) (a => a.Dispose()));
        this.usbDevices.Dispose();
      }
      this.Disposed = true;
    }

    public void DetectCameras()
    {
      this.cameras.Clear();
      for (int index = 0; index < this.usbDevices.Count; ++index)
        this.InitCamera(index);
      if (!this.isConnected)
        return;
      this.cameras[this.cameraNumber].Connect();
    }

    public void AutoConnect()
    {
      this.DetectCameras();
      if (this.cameras.Count <= 0)
        return;
      this.cameraNumber = 0;
      this.cameras[this.cameraNumber].Connect();
      this.isConnected = true;
    }

    private void InitCamera(int item)
    {
      BCam bcam = new BCam(this.usbDevices[item] as CyFX3Device);
      if (bcam.camComLayer.bootLoaderCurrentlyRunning)
      {
        Thread.Sleep(100);
        for (this.usbDevices = new USBDeviceList((byte) 1); this.usbDevices.Count == 0; this.usbDevices = new USBDeviceList((byte) 1))
          Thread.Sleep(100);
        bcam = new BCam(this.usbDevices[item] as CyFX3Device);
      }
      bcam.Init(this.usbDevices[item] as CyUSBDevice);
      this.cameras.Add(bcam);
    }

    private void usbDevices_DeviceAttached(object sender, EventArgs e)
    {
      this.DetectCameras();
      this.OnAttachedStateChanged();
    }

    private void usbDevices_DeviceRemoved(object sender, EventArgs e)
    {
      this.DetectCameras();
      this.OnRemoveStateChanged();
    }

    protected virtual void OnAttachedStateChanged()
    {
      if (this.AttachedStateChanged == null)
        return;
      this.AttachedStateChanged((object) this, EventArgs.Empty);
    }

    protected virtual void OnRemoveStateChanged()
    {
      if (this.RemoveStateChanged == null)
        return;
      this.RemoveStateChanged((object) this, EventArgs.Empty);
    }

    public void ConnectTo(int cameraNumber)
    {
      this.cameraNumber = cameraNumber;
      this.cameras[cameraNumber].Connect();
      this.isConnected = true;
    }

    public void ConnectTo(string serialNumber)
    {
      this.cameras.Clear();
      this.cameraNumber = -1;
      for (int index = 0; index < this.usbDevices.Count; ++index)
      {
        this.InitCamera(index);
        if (this.cameras[index].camProperties.GetSerialNumber() == serialNumber)
          this.cameraNumber = index;
      }
      if (this.cameraNumber != -1)
      {
        this.cameras[this.cameraNumber].Connect();
        this.isConnected = true;
      }
      else
        this.errorManager.Error = "BSDK.ConnectTo() : Camera serial number is not connected or not detected.";
    }
  }
}

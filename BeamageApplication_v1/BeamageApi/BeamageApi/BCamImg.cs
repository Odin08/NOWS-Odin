// Decompiled with JetBrains decompiler
// Type: BeamageApi.BCamImg
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

using System;

namespace BeamageApiCode
{
  public class BCamImg : IDisposable
  {
    internal double[] imageFinal;
    internal byte[] imageBuffer;

    public int width { private set; get; }

    public int height { private set; get; }

    public bool Disposed { get; private set; }

    internal BCamImg(int _width, int _height)
    {
      this.width = _width;
      this.height = _height;
      this.imageBuffer = new byte[_width * _height * 2];
      this.imageFinal = new double[_width * _height];
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
      this.Disposed = true;
    }

    public double[] GetLastImageArray()
    {
      this.TranslateCameraImageBufferToArray();
      return this.imageFinal;
    }

    private void TranslateCameraImageBufferToArray()
    {
      int index1 = 0;
      for (int index2 = 0; index2 < this.height; ++index2)
      {
        for (int index3 = 0; index3 < 512; ++index3)
        {
          for (int index4 = 0; index4 < 4; ++index4)
          {
            int num = ((int) this.imageBuffer[index1] << 8) + (int) this.imageBuffer[index1 + 1];
            int index5 = 2047 - index3 - 512 * index4 + index2 * 2048;
            this.imageFinal[index5] = num;
            index1 += 2;
          }
        }
      }
    }
  }
}

// Decompiled with JetBrains decompiler
// Type: BeamageApi.BCamImages
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

using System;
using System.Collections.Generic;

namespace BeamageApiCode
{
  internal class BCamImages : IDisposable
  {
    public List<BCamImg> images = new List<BCamImg>();

    public bool Disposed { get; private set; }

    public void Dispose()
    {
      this.Dispose(true);
      GC.SuppressFinalize((object) this);
    }

    public void Dispose(bool disposing)
    {
      if (this.Disposed)
        return;
      if (disposing)
        this.images.ForEach((Action<BCamImg>) (a => a.Dispose()));
      this.Disposed = true;
    }
  }
}

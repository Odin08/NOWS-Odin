// Decompiled with JetBrains decompiler
// Type: BeamageApi.BErrorsManager
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

using System;
using System.Collections.Generic;

namespace BeamageApiCode
{
  public class BErrorsManager
  {
    private List<string> errors = new List<string>();
    private string _Error;

    public BErrorsManager()
    {
      this.ErrorStateChanged += new EventHandler(this.ErrorStateProcess);
    }

    public event EventHandler ErrorStateChanged;

    public event EventHandler ErrorValueChanged;

    public string Error
    {
      get
      {
        return this._Error;
      }
      set
      {
        this._Error = value;
        this.OnErrorStateChanged();
        this.OnErrorValueChanged();
      }
    }

    protected virtual void OnErrorStateChanged()
    {
      if (this.ErrorStateChanged == null)
        return;
      this.ErrorStateChanged((object) this, EventArgs.Empty);
    }

    public int Count()
    {
      return this.errors.Count;
    }

    public void Clear()
    {
      this.errors.Clear();
    }

    protected virtual void OnErrorValueChanged()
    {
      if (this.ErrorValueChanged == null)
        return;
      this.ErrorValueChanged((object) this, EventArgs.Empty);
    }

    private void ErrorStateProcess(object sender, EventArgs e)
    {
      this.errors.Add(this._Error);
    }
  }
}

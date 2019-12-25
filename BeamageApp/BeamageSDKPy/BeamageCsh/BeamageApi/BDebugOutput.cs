// Decompiled with JetBrains decompiler
// Type: BeamageApi.BDebugOutput
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace BeamageApiCode
{
  internal class BDebugOutput
  {
    private int column;

    public BDebugOutput()
    {
      this.debugOutput = false;
      this.Reset();
    }

    public bool debugOutput { get; private set; }

    public void Reset()
    {
      if (!this.debugOutput)
        return;
      string path = Environment.CurrentDirectory + "\\exportSDK.csv";
      StringBuilder stringBuilder = new StringBuilder();
      stringBuilder.AppendLine("");
      for (int index = 0; index < 256; ++index)
        stringBuilder.AppendLine("");
      File.WriteAllText(path, stringBuilder.ToString());
    }

    public void ExportRegistersCommands(ref BCamRegistersModel registers)
    {
      string path = Environment.CurrentDirectory + "\\exportSDK.csv";
      List<string> list = File.ReadLines(path).ToList<string>();
      using (TextWriter text = (TextWriter) File.CreateText(path))
      {
        TextWriter textWriter1 = text;
        List<string> stringList1 = list;
        List<string> stringList2 = stringList1;
        string str1 = stringList1[0];
        int index1 = ++this.column;
        string str2 = index1.ToString();
        string str3;
        string str4 = str3 = str1 + ";" + str2;
        stringList2[0] = str3;
        string str5 = str4;
        textWriter1.WriteLine(str5);
        for (int index2 = 0; index2 < registers.GetCount(); ++index2)
        {
          TextWriter textWriter2 = text;
          List<string> stringList3 = list;
          index1 = index2 + 1;
          string str6 = stringList3[index1] = stringList3[index1] + ";" + registers.GetRegisterValue(index2).ToString();
          textWriter2.WriteLine(str6);
        }
      }
    }
  }
}

// Decompiled with JetBrains decompiler
// Type: BeamageApi.BExtensions
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

namespace BeamageApiCode
{
  internal static class BExtensions
  {
    public static void Populate(byte[] arr, byte value)
    {
      for (int index = 0; index < arr.Length; ++index)
        arr[index] = value;
    }
  }
}

using System;
using TestAssembly.Math;

var m = new DoMath();
Console.WriteLine($"Testing C# Library: {m.Add(21, 21)}");
Console.WriteLine($"Testing C# Library: {m.Solve()}");
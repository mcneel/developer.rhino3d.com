#r "nuget: MathNet.Numerics, 5.0.0"

using System;
using MathNet.Numerics;
using MathNet.Numerics.LinearAlgebra;

using TestAssembly.Math.Types;

#if !LIBRARY
var m = new TestAssembly.Math.DoMath();
if (m.Add(21, 21) > 0)
    Console.WriteLine("[ OK ] Addition Ok");

if (m.Solve() > 0)
    Console.WriteLine("[ OK ] Addition Ok");
#endif

namespace TestAssembly.Math
{
  public sealed class DoMath
  {
    public int Add(int x, int y)
    {
#if DEBUG
        return 500;
#else
        return x + y + 10;
#endif
    }

    public double Solve()
    {
        var m = Matrix<double>.Build.Random(500, 500);
        var v = Vector<double>.Build.Random(500);
        var y = m.Solve(v);

        return y[0];
    }
  }
}

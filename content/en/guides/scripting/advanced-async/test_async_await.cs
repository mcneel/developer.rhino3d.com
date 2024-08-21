// #! csharp
// async: true
using System;
using System.Threading.Tasks;

using Rhino;

async Task<bool> Compute()
{
    await Task.Delay(TimeSpan.FromMilliseconds(3000));
    return true;
}

int res = 0;

// int res = await Compute();
// int res = Compute().GetAwaiter().GetResult();

if (await Compute())
{
    res = 42;
}

RhinoApp.WriteLine($"Result: {res}");


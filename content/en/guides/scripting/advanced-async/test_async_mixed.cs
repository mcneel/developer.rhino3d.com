// #! csharp
// async: true
using System;
using System.Threading;
using System.Threading.Tasks;

using Rhino;
using Rhino.UI;
using Eto.Forms;

// Part A: runs on UI thread (blocking)
Application.Instance.Invoke(() => {
    // CAN MAKE CHANGES TO RHINO or DOCUMENT HERE
    StatusBar.ShowProgressMeter(0, 5, "Progress", true, false);
});

// Part B: runs on Non-UI thread
int result = Task.Run(() => {
    for (int i = 0; i < 5; i++)
    {
        Thread.Sleep(1 * 1000);
        StatusBar.UpdateProgressMeter("Progress", i, true);
        // DO NOT CALL THIS SINCE WE ARE NOT ON UI THREAD
        // Application.Instance.RunIteration();
    }

    return 42;
}).GetAwaiter().GetResult();

// Part C: runs on UI thread (blocking)
Application.Instance.Invoke(() => {
    // CAN MAKE CHANGES TO RHINO or DOCUMENT HERE
    RhinoApp.WriteLine($"Result: {result}");
    StatusBar.HideProgressMeter();
});
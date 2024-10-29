// #! csharp
using System;
using System.Threading;

using Rhino;
using Rhino.UI;
using Eto.Forms;

// setup the progress indicator with expected range, and a message
StatusBar.ShowProgressMeter(0, 5, "Progress", embedLabel: true, showPercentComplete: false);
RhinoApp.WriteLine("Start Task");
for (int i = 0; i < 5; i++)
{
    Thread.Sleep(1000); // simulate work

    // update progress
    StatusBar.UpdateProgressMeter("Progress", i, true);
    // call this method to force Rhino UI to update itself
    Application.Instance.RunIteration();
}

// do not forget to hide the progress when done
StatusBar.HideProgressMeter();
RhinoApp.WriteLine("End Task");
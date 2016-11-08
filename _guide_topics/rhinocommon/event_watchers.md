---
title: Event Watchers
description: This guide covers how to synchronize a control's appearance with what is going on in Rhino using event watchers.
author: ['Dale Fugier', '@dale']
apis: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/dotneteventwatcher
order: 4
keywords: ['RhinoCommon', 'Event', 'Watchers', 'UI']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## UI Thread

Applications can not update any user interface controls from any thread other than the main UI thread. Changing a property on a windows control typically causes the control to immediately update its display. But if the call is made from another thread then the UI thread windows will crash the application.

If you are updating a control from inside your event handler, you should check to see if `CheckAccess()` on the Dispatcher associated with your control evaluates to `True`. If this is the case, you must invoke a delegate that handles the UI updating and make sure that this delegate is called from the UI thread. This is actually easier than it sounds.

Here is a C# sample of `RhinoDoc.AddRhinoObject` event handler that handles the thrown exception when called from a thread other than the UI thread...

```cs
private void rhinoObjectAdded(Object sender, Rhino.DocObjects.RhinoObjectEventArgs e)
{
  var msg = String.Format("thread id = {0}, obj id = {1}",
        Thread.CurrentThread.ManagedThreadId,
        e.ObjectId.ToString());

  RhinoApp.WriteLine(msg);

  try {
    // when a sphere is added from a secondary thread this line will
    // throw an exception because UI controls can only be accessed from
    // the main UI thread
    _label.Content = msg;
  } catch (InvalidOperationException ioe) {RhinoApp.WriteLine(ioe.Message);}
}
```

## Other Threads

But... I really do need to update my control's state, even when in the wrong thread!

This is where `Dispatcher.Invoke` or `Dispatcher.BeginInvoke` comes into play. You can force the code that modifies the control to run from the UI thread. Here is a C# sample of how to do this...

```cs
private void rhinoObjectAddedSafe(Object sender, Rhino.DocObjects.RhinoObjectEventArgs e)
{
  var msg = String.Format("thread id = {0}, obj id = {1}",
        Thread.CurrentThread.ManagedThreadId,
        e.ObjectId.ToString());

  RhinoApp.WriteLine(msg);

  // checks if the calling thread is the thread the dispatcher is associated with.
  // In other words, checks if the calling thread is the UI thread
  if (_label.Dispatcher.CheckAccess())
    // if we're on the UI thread then just update the component
    _label.Content = msg;
  else
  {
    // invoke the setLabelTextDelegate on the thread the dispatcher is associated with, i.e., the UI thread
    var setLabelTextDelegate = new Action<string>(txt => _label.Content = txt);
    _label.Dispatcher.Invoke(setLabelTextDelegate, new String[] { msg });
  }
}
```

The above function could be rewritten to just always call the delegate...

```cs
private void rhinoObjectAddedSafe(Object sender, Rhino.DocObjects.RhinoObjectEventArgs e)
{
  var msg = String.Format("thread id = {0}, obj id = {1}",
        Thread.CurrentThread.ManagedThreadId,
        e.ObjectId.ToString());

  RhinoApp.WriteLine(msg);

  // invoke the setLabelTextDelegate on the thread the dispatcher is associated with, i.e., the UI thread
  var setLabelTextDelegate = new Action<string>(txt => _label.Content = txt);
  _label.Dispatcher.Invoke(setLabelTextDelegate, new String[] { msg });
}
```

**NOTE**: If Windows Forms (on Windows) is used instead of WPF then `_label.Dispatcher.CheckAccess()` becomes `_label.InvokeRequired` and `_label.Dispatcher.Invoke(...)` becomes `_label.Invoke(...)`.

Here is the complete example:

```cs
using System;
using Rhino;
using Rhino.Commands;
using Rhino.DocObjects;
using Rhino.Geometry;
using System.Threading;
using System.Windows;
using System.Windows.Controls;

namespace examples_cs
{
  [System.Runtime.InteropServices.Guid("E4A93905-6E61-43BB-9FF0-4D5F6AF76704")]
  public class ChangeUiFromDifferentThreadCommand : Command
  {
    public override string EnglishName { get { return "csChangeUIFromDifferentThread"; } }
    private RhinoDoc _doc;
    private Label _label;
    private Window _window;

    protected override Result RunCommand(RhinoDoc doc, RunMode mode)
    {
      _doc = doc;

      _window = new Window {Title = "Object ID and Thread ID", Width = 500, Height = 75};
      _label = new Label();
      _window.Content = _label;
      new System.Windows.Interop.WindowInteropHelper(_window).Owner = Rhino.RhinoApp.MainWindowHandle();
      _window.Show();


      // register the rhinoObjectAdded method with the AddRhinoObject event
      RhinoDoc.AddRhinoObject += RhinoObjectAdded;

      // add a sphere from the main UI thread.  All is good
      AddSphere(new Point3d(0,0,0));

      // add a sphere from a secondary thread. Not good: the rhinoObjectAdded method
      // doesn't work well when called from another thread
      var addSphereDelegate = new Action<Point3d>(AddSphere);
      addSphereDelegate.BeginInvoke(new Point3d(0, 10, 0), null, null);

      // handle the AddRhinoObject event with rhinoObjectAddedSafe which is
      // desgined to work no matter which thread the call is comming from.
      RhinoDoc.AddRhinoObject -= RhinoObjectAdded;
      RhinoDoc.AddRhinoObject += RhinoObjectAddedSafe;

      // try again adding a sphere from a secondary thread.  All is good!
      addSphereDelegate.BeginInvoke(new Point3d(0, 20, 0), null, null);

      doc.Views.Redraw();

      return Result.Success;
    }

    private void AddSphere(Point3d center) {
      _doc.Objects.AddSphere(new Sphere(center, 3));
    }

    private void RhinoObjectAdded(Object sender, RhinoObjectEventArgs e)
    {
      var message = String.Format("thread id = {0}, obj id = {1}",
            Thread.CurrentThread.ManagedThreadId,
            e.ObjectId.ToString());

      RhinoApp.WriteLine(message);

      try {
        // when a sphere is added from a secondary thread this line will
        // throw an exception because UI controls can only be accessed from
        // the main UI thread
        _label.Content = message;
      } catch (InvalidOperationException ioe) {RhinoApp.WriteLine(ioe.Message);}
    }

    private void RhinoObjectAddedSafe(Object sender, RhinoObjectEventArgs e)
    {
      var message = String.Format("thread id = {0}, obj id = {1}",
            Thread.CurrentThread.ManagedThreadId,
            e.ObjectId.ToString());

      RhinoApp.WriteLine(message);

      // checks if the calling thread is the thread the dispatcher is associated with.
      // In other words, checks if the calling thread is the UI thread
      if (_label.Dispatcher.CheckAccess())
        // if we're on the UI thread then just update the component
        _label.Content = message;
      else
      {
        // invoke the setLabelTextDelegate on the thread the dispatcher is associated with, i.e., the UI thread
        var setLabelTextDelegate = new Action<string>(txt => _label.Content = txt);
        _label.Dispatcher.BeginInvoke(setLabelTextDelegate, new String[] { message });
      }
    }
  }
}
```

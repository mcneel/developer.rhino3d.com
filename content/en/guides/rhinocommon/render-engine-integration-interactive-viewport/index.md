+++
aliases = ["/5/guides/rhinocommon/render-engine-integration-interactive-viewport/", "/6/guides/rhinocommon/render-engine-integration-interactive-viewport/", "/7/guides/rhinocommon/render-engine-integration-interactive-viewport/", "/wip/guides/rhinocommon/render-engine-integration-interactive-viewport/"]
authors = [ "nathan" ]
categories = [ "Rendering" ]
description = "This guide, the fourth of a series, covers integrating render engines in Rhino's viewport."
keywords = [ "renderer", "integration", "RhinoCommon", "interactive", "viewport" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Render Engine Integration - Interactive Viewport"
type = "guides"
weight = 4
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://www.letworyinteractive.com/b/2016/10/integrating-a-render-engine-in-rhinoceros-3d-using-rhinocommon-mockingbird-interactive-rendering/"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Overview

This is part four in the series on render engine integration in Rhinoceros 3D using RhinoCommon.

1. [Setting up the plug-in](/guides/rhinocommon/render-engine-integration-introduction/)
1. [Modal Rendering](/guides/rhinocommon/render-engine-integration-modal/)
1. [ChangeQueue](/guides/rhinocommon/render-engine-integration-changequeue/)
1. Interactive render - viewport integration (this guide)
1. Preview render *(forthcoming)*

If you have not already read the first three parts, please do so before proceeding.

## Realtime Display

For this plug-in we are going to do things in a slightly different way. Not because it is a must, but because it gives an interesting possibility for plug-in developers who want to integrate their own render engines, but without exposing it to the `_Render` command. We do that with a generic utility plug-in. There won't be an API to implement for the `_Render` command, instead we'll implement two new classes. One derived from `Rhino.Render.RealtimeDisplayMode` and one derived from `Rhino.Render.RealtimeDisplayModeClassInfo`.

Together these will effectively create and register a conduit that is used during the drawing process of a viewport to display the result of the render engine.

For this example a `ChangeQueue` implementation is used, but as said in earlier articles it is possible to do your data conversion directly from the `RhinoDoc`. If the render engine to be integrated is one using mesh data for geometry I advise strongly to use the `ChangeQueue`.

### Utility plug-in

```cs
public class MockingViewportPlugIn : Rhino.PlugIns.PlugIn
{
	public MockingViewportPlugIn()
	{
		if (Instance == null) Instance = this;
	}

	public static MockingViewportPlugIn Instance { get; private set; }

	protected override LoadReturnCode OnLoad(ref string errorMessage)
	{
		// RealtimeDisplayMode.RegisterDisplayModes(this);
		// call to RegisterDisplayModes no longer necessary, it is automatically called.
		return LoadReturnCode.Success;
	}
}

```

The plug-in code is very lean, only `LoadRetunCode OnLoad()` needs to be overridden.  With a proper RealtimeDisplayModeClassInfo and RealtimeDisplayMode implementation the new viewport mode will be registered with Rhino. It'll show up in the viewport mode dropdown list.

### Registering with Rhino

```cs
public class MockingRealtimeDisplayModeInfo : RealtimeDisplayModeClassInfo
{
	public override string Name => "MockingRealtimeMode";

	public override Guid GUID => new Guid("F14A3A24-C2FB-4216-9D2A-9636EF3869FA");

	public override Type RealtimeDisplayModeType => typeof (MockingRealtimeDisplayMode);
}

```

Implement a class derived from `Rhino.Render.RealtimeDisplayModeClassInfo`. When the plug-in is loaded the automatic registration procedure of the plug-in ensures that this information is used to identify the `RealtimeDisplayMode` implementation of the plug-in.

All of the properties of the class are important, but pay especially close attention to `Guid GUID`. This has to be unique from other plug-ins, so don't ever copy-paste Guids from sample code.

The `Type RealtimeDisplayModeType`property should return the type of your `RealtimeDisplayMode` implementation.

After the plug-in is loaded the viewport mode can be found from the mode drop-down list.

![viewports modes droplist](/images/mockingbird//mockingbird_viewport_001_viewport_modes_droplist.png)


### The viewport implementation

The actual viewport integration is done with a class deriving from `RealtimeDisplayMode`. When deriving from that class, which we do with `MockingRealtimeDisplayMode`, Visual Studio will tell that several abstract methods need to be implemented. These methods are the minimum required functions to ensure proper functioning of the integration. The entire class can be found in the <a href="https://github.com/mcneel/rhino-developer-samples/blob/6/rhinocommon/cs/SampleCsRendererIntegration/MockingBird/MockingBirdViewport/MockingRealtimeDisplayMode.cs">Git repository here</a>. Lets step through the process what happens when the user selects the display mode for the viewport.

First of all an instance of our class will be created. If there is the need for initialisation a public default constructor can be implemented where such initialisation can be done. For `MockingRealtimeDisplayMode` we don't need that. During the start up phase of the mode switch the underlying system will be querying whether our engine is started, and whether there are results available. Because this can happen already before we've actually managed to start our engine and get some results we'll be using a boolean flag `_started` to communicate our state through the functions `IsRendererStarted()` and `IsFrameBufferAvailable()`. Our real entry into the rendering process happens with `StartRenderer()`.

```cs
public override bool StartRenderer(int w, int h, RhinoDoc doc, ViewInfo view, ViewportInfo viewportInfo, bool forCapture,
	RenderWindow renderWindow)
{
	_started = true;
	// prepare render, get a changequeue
	_width = (int)w;
	_height = (int)h;
	reng = new MockingRender(Rhino.PlugIns.PlugIn.IdFromName("MockingBirdViewport"), doc.RuntimeSerialNumber, view, renderWindow)
	{
		MaxPasses = 50
	};
	reng.MaxPassesCompleted += Reng_MaxPassesCompleted;
	reng.PassRendered += Reng_PassRendered;
	reng.RenderReset += Reng_RenderReset;
	reng.RenderStarted += Reng_RenderStarted;
	MaxPassesChanged += MockingRealtimeDisplayMode_MaxPassesChanged;

	// start rendering
	_startTime = DateTime.Now;

	_isCompleted = false;
	_theThread = new Thread(reng.ColorPixels) {Name = "MockingBirdViewport thread"};
	_theThread.Start();

	return true;
}
```

For this example I opted to implement a very simple 'render engine' to show how working with threads in this environment can be done. So I start by creating an instance of that engine `MockingRender`. This engine uses a `ChangeQueue` internally, so I give the plug-in ID, Rhino document runtime serial number, the `ViewInfo` instance and the `RenderWindow` instance to it.

To make communication between the `MockingRealtimeDisplayMode` and `MockingRender` easy I have added several events to `MockingRender`. I register necessary handlers for those.

Once the render engine has completed a pass it fires the `PassRendered` event. In the handler the underlying system gets notified about that fact by calling the `SignalDraw()` function provided by the base class `RealtimeDisplayMode`.

```cs
private void Reng_PassRendered(object sender, PassRenderedEventArgs e)
{
	_currentPass = e.Pass;
	SignalRedraw();
}
```

The actual rendering

The <a href="https://github.com/mcneel/rhino-developer-samples/blob/6/rhinocommon/cs/SampleCsRendererIntegration/MockingBird/MockingBirdViewport/MockingRender.cs">`MockingRender` class</a> is responsible for generating the pixel data for the viewport. Its entry function is ColorPixels().

```cs
public void ColorPixels()
{

	RenderStarting?.Invoke(this, EventArgs.Empty);
	Passes = 0;

	RenderStarted?.Invoke(this, EventArgs.Empty);

	while (true)
	{
		while (Passes < MaxPasses)
		{

			ColorPass(Passes);
			Thread.Sleep(10);
			if (_shutdown) break;
			Passes += 1;
		}
		if (!_completionTriggered &amp;&amp; Passes >= MaxPasses)
		{
			_completionTriggered = true;
			MaxPassesCompleted?.Invoke(this, EventArgs.Empty);

		}
		Thread.Sleep(10);
		if (_shutdown) break;
	}
}
```

It essentially goes into an eternal loop that runs until the `_shutdown` flag is set. The render process goes through each pass (and simulates some extra workload by sleeping a whopping 10 milliseconds), then essentially waits for `Passes` to get reset or `MaxPasses` change such that `Passes < MaxPasses`. `ColorPass()` then fills the pixel buffer, presented to the render engine by means of the `RenderWindow`. Increasing `Passes` will also fire the `PassRendered` event.

{{< div class="line-numbers" >}}
```cs
private void ColorPass(int pass)
{
	var fac = pass/(float)MaxPasses;
	var c = Color4f.FromArgb(1.0f, _color.R*fac, _color.G*fac, _color.B*fac);
	using (var channel = rw.OpenChannel(RenderWindow.StandardChannels.RGBA))
	{
		var size = rw.Size();
		for (var x = 0; x < size.Width; x++)
		{
			for (var y = 0; y < size.Height; y++)
			{
				channel.SetValue(x, y, c);
			}
			if (_shutdown) break;
		}
	}
}
```
{{< /div >}}

In `ColorPass()` above the most important part to look at is line 5. With the `using` idiom the necessary channel from the `RenderWindow` is opened (`RGBA` in general, there are other channels too, though, but not in the scope of this article series), then filled with color data per pixel. The using idiom ensures the opened channel is properly disposed of.

Note that the simplest possible pixel buffer filling code would be to have the channel `SetValue` loop directly in `StartRenderer()` and leave out the entire `MockingRender` and `Thread` construct.

## Next Steps

*Congratulations!*  These are the steps necessary to integrate a new render engine into Rhino viewport for interactive, real-time rendering using the RhinoCommon SDK.  *Now what?*

This is part four in the series on render engine integration in Rhinoceros using RhinoCommon.  The next guide (forthcoming) will demonstrate implementing a preview render.

## Related Topics

- [Render Engine Integration - Introduction](/guides/rhinocommon/render-engine-integration-introduction/)
- [Render Engine Integration - Modal](/guides/rhinocommon/render-engine-integration-modal/)
- [Render Engine Integration - ChangeQueue](/guides/rhinocommon/render-engine-integration-changequeue/)
- Preview render *(forthcoming)*

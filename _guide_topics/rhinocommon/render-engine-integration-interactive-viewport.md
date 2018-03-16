---
title: Render Engine Integration - Interactive Viewport
description: This guide, the 4th of a series, covers integrating render engines in Rhino's viewport.
authors: ['Nathan Letwory']
author_contacts: ['nathanletwory']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Rendering']
origin: http://www.letworyinteractive.com/b/2016/10/integrating-a-render-engine-in-rhinoceros-3d-using-rhinocommon-mockingbird-interactive-rendering/
order: 4
keywords: ['renderer', 'integration', 'RhinoCommon', 'interactive', 'viewport']
layout: toc-guide-page
redirect_from: "/guides/rhinocommon/mockingbird-interactive/"
---


This is part 4 in the series on render engine integration in Rhinoceros 3D using RhinoCommon (v6).

* [Setting up the plug-in]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-introduction/)
* [Modal Rendering]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-modal/)
* [ChangeQueue]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-changequeue/)
* [Interactive render - viewport integration (this guide)]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-interactive-viewport/)
* Preview render (forthcoming)

For this plug-in we are going to do things in a slightly different way. Not because it is a must, but because it gives an interesting possibility for plug-in developers who want to integrate their own render engines, but without exposing it to the `_Render`{:.language-cs}  command. We do that with a generic utility plug-in. There won't be an API to implement for the `_Render`{:.language-cs}  command, instead we'll implement two new classes. One derived from `Rhino.Render.RealtimeDisplayMode`{:.language-cs}  and one derived from `Rhino.Render.RealtimeDisplayModeClassInfo`{:.language-cs} .

Together these will effectively create and register a conduit that is used during the drawing process of a viewport to display the result of the render engine.

For this example a `ChangeQueue`{:.language-cs}  implementation is used, but as said in earlier articles it is possible to do your data conversion directly from the `RhinoDoc`{:.language-cs} . If the render engine to be integrated is one using mesh data for geometry I advise strongly to use the `ChangeQueue`{:.language-cs} .
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

The plug-in code is very lean, only `LoadRetunCode OnLoad()`{:.language-cs}  needs to be overridden. (<del>In this function a call on line 9 to `RealtimeDisplayMode.RegisterDisplayModes()`{:.language-cs}  with the plug-in itself as parameter ensures the Rhino plug-in loading mechanism checks for display mode implementations</del>. With latest Rhino WIP (and what will go into v6)  it is no longer necessary to explicitly call `RegisterDisplayModes()`{:.language-cs} , since that is done automatically. ) With a proper RealtimeDisplayModeClassInfo and RealtimeDisplayMode implementation the new viewport mode will be registered with Rhino. It'll show up in the viewport mode dropdown list.
### Registering with Rhino

```cs
public class MockingRealtimeDisplayModeInfo : RealtimeDisplayModeClassInfo
{
	public override string Name => "MockingRealtimeMode";

	public override Guid GUID => new Guid("F14A3A24-C2FB-4216-9D2A-9636EF3869FA");

	public override Type RealtimeDisplayModeType => typeof (MockingRealtimeDisplayMode);
}

```

Implement a class derived from `Rhino.Render.RealtimeDisplayModeClassInfo`{:.language-cs} . When the plug-in is loaded the automatic registration procedure of the plug-in ensures that this information is used to identify the `RealtimeDisplayMode`{:.language-cs}  implementation of the plug-in.

All of the properties of the class are important, but pay especially close attention to `Guid GUID`{:.language-cs} . This has to be unique from other plug-ins, so don't ever copy-paste Guids from sample code.

The `Type RealtimeDisplayModeType`{:.language-cs} property should return the type of your `RealtimeDisplayMode`{:.language-cs}  implementation.

After the plug-in is loaded the viewport mode can be found from the mode drop-down list.

![viewports modes droplist]({{ site.baseurl }}/images/mockingbird//mockingbird_viewport_001_viewport_modes_droplist.png)


### The viewport implementation

The actual viewport integration is done with a class deriving from `RealtimeDisplayMode`{:.language-cs} . When deriving from that class, which we do with `MockingRealtimeDisplayMode`{:.language-cs} , Visual Studio will tell that several abstract methods need to be implemented. These methods are the minimum required functions to ensure proper functioning of the integration. The entire class can be found in the <a href="https://github.com/mcneel/rhino-developer-samples/blob/6/rhinocommon/cs/SampleCsRendererIntegration/MockingBird/MockingBirdViewport/MockingRealtimeDisplayMode.cs">Git repository here</a>. Lets step through the process what happens when the user selects the display mode for the viewport.

First of all an instance of our class will be created. If there is the need for initialisation a public default constructor can be implemented where such initialisation can be done. For `MockingRealtimeDisplayMode`{:.language-cs}  we don't need that. During the start up phase of the mode switch the underlying system will be querying whether our engine is started, and whether there are results available. Because this can happen already before we've actually managed to start our engine and get some results we'll be using a boolean flag `_started`{:.language-cs}  to communicate our state through the functions `IsRendererStarted()`{:.language-cs}  and `IsFrameBufferAvailable()`{:.language-cs} . Our real entry into the rendering process happens with `StartRenderer()`{:.language-cs} .

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

For this example I opted to implement a very simple 'render engine' to show how working with threads in this environment can be done. So I start by creating an instance of that engine `MockingRender`{:.language-cs} . This engine uses a `ChangeQueue`{:.language-cs}  internally, so I give the plug-in ID, Rhino document runtime serial number, the `ViewInfo`{:.language-cs}  instance and the `RenderWindow`{:.language-cs}  instance to it.

To make communication between the `MockingRealtimeDisplayMode`{:.language-cs}  and `MockingRender`{:.language-cs}  easy I have added several events to `MockingRender`{:.language-cs} . I register necessary handlers for those.

Once the render engine has completed a pass it fires the `PassRendered`{:.language-cs}  event. In the handler the underlying system gets notified about that fact by calling the `SignalDraw()`{:.language-cs}  function provided by the base class `RealtimeDisplayMode`{:.language-cs} .

```cs
private void Reng_PassRendered(object sender, PassRenderedEventArgs e)
{
	_currentPass = e.Pass;
	SignalRedraw();
}
```

The actual rendering

The <a href="https://github.com/mcneel/rhino-developer-samples/blob/6/rhinocommon/cs/SampleCsRendererIntegration/MockingBird/MockingBirdViewport/MockingRender.cs">`MockingRender`{:.language-cs}  class</a> is responsible for generating the pixel data for the viewport. Its entry function is ColorPixels().

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

It essentially goes into an eternal loop that runs until the `_shutdown`{:.language-cs}  flag is set. The render process goes through each pass (and simulates some extra workload by sleeping a whopping 10 milliseconds), then essentially waits for `Passes`{:.language-cs}  to get reset or `MaxPasses`{:.language-cs}  change such that `Passes < MaxPasses`{:.language-cs} . `ColorPass()`{:.language-cs}  then fills the pixel buffer, presented to the render engine by means of the `RenderWindow`{:.language-cs} . Increasing `Passes`{:.language-cs}  will also fire the `PassRendered`{:.language-cs}  event.

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

In `ColorPass()`{:.language-cs}  above the most important part to look at is line 5. With the `using`{:.language-cs}  idiom the necessary channel from the `RenderWindow`{:.language-cs}  is opened (`RGBA`{:.language-cs}  in general, there are other channels too, though, but not in the scope of this article series), then filled with color data per pixel. The using idiom ensures the opened channel is properly disposed of.

Note that the simplest possible pixel buffer filling code would be to have the channel `SetValue`{:.language-cs}  loop directly in `StartRenderer()`{:.language-cs}  and leave out the entire `MockingRender`{:.language-cs}  and `Thread`{:.language-cs}  construct.

These are the steps necessary to integrate a new render engine into Rhinoceros 3D (v6) viewport for interactive, real-time rendering using the RhinoCommon SDK.

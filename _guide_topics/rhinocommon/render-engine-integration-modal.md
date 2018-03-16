---
title: Render Engine Integration - Modal
description: This guide, the 2nd of a series, demonstrates integrating a modal rendering engine using RhinoCommon.
authors: ['Nathan Letwory']
author_contacts: ['nathanletwory']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Rendering']
origin: http://www.letworyinteractive.com/b/2016/08/integrating-a-render-engine-in-rhinoceros-3d-using-rhinocommon-mockingbird-modal-rendering-25/
order: 2
keywords: ['renderer', 'integration', 'RhinoCommon']
layout: toc-guide-page
redirect_from: "/guides/rhinocommon/mockingbird-modal/"
---


## Overview

This is part 2 in the series on render engine integration in Rhinoceros 3D using RhinoCommon.

1. [Setting up the plug-in]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-introduction/)
1. Modal Rendering (this guide)
1. [ChangeQueue]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-changequeue/)
1. [Interactive render - viewport integration]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-interactive-viewport/)
1. Preview render *(forthcoming)*

To implement a modal rendering solution for Rhinoceros there are two particular pieces you'll need to create, which will allow you to render into a separate render window: a custom implementation of a `Rhino.Render.AsyncRenderContext`{:.language-cs} , and a `Rhino.Render.RenderPipeline`{:.language-cs}.

The full source code of this plug-in can be found [here](https://github.com/mcneel/rhino-developer-samples/tree/6/rhinocommon/cs/SampleCsRendererIntegration/MockingBird/MockingBirdModal).

## Render

The rendering will start when giving the Rhino command `Render`{:.language-cs}. This will result in a call into the `Render()`{:.language-cs}  of your Render plug-in implementation.

```cs
protected override Result Render(RhinoDoc doc, RunMode mode, bool fastPreview)
{
	// initialise our render context
	MockingRenderContext rc = new MockingRenderContext();

	// initialise our pipeline implementation
	RenderPipeline pipeline = new MockingRenderPipeline(doc, mode, this, rc);

	// query for render resolution
	var renderSize = RenderPipeline.RenderSize(doc);

	// set up view info
	ViewInfo viewInfo = new ViewInfo(doc.Views.ActiveView.ActiveViewport);

	// set up render window
	rc.RenderWindow = pipeline.GetRenderWindow();
	// add a wireframe channel for curves/wireframes/annotation etc.
	rc.RenderWindow.AddWireframeChannel(doc, viewInfo.Viewport, renderSize, new Rectangle(0, 0, renderSize.Width, renderSize.Height));
	// set correct size
	rc.RenderWindow.SetSize(renderSize);

	// now fire off render thread.
	var renderCode = pipeline.Render();

	// note that the rendering isn't complete yet, rather the pipeline.Render()
	// call starts a rendering thread. Here we essentially check whether
	// starting that thread went ok.
	if (renderCode != RenderPipeline.RenderReturnCode.Ok)
	{
		RhinoApp.WriteLine("Rendering failed:" + rc.ToString());
		return Result.Failure;
	}
	// all ok, so we are apparently rendering.
	return Result.Success;
}

```
{: .line-numbers}

In our `Render()`{:.language-cs}  function we start by initialising our render context (line 4) and render pipeline (line 7). The render context will be essentially where our actual rendering code will be hosted. The render pipeline starts and stops our engine (context) as necessary.

In `Render()`{:.language-cs}  we also ensure we have a `RenderWindow`{:.language-cs} , set to the requested render resolution (lines 10-20).

As said, for the modal rendering to get hooked up  two classes need to be implemented. An implementation of a RenderPipeline is used to communicate start and stop events between Rhino and the second class, an implementation of AsyncRenderContext. The latter is essentially where a custom render engine will be hooked up to the Rhino world.

RenderPipeline requires several functions to be overridden. For our modal (production) render case we are interested mostly in `OnRenderBegin()`{:.language-cs} , `OnRenderEnd()`{:.language-cs}  and `ContinueModal()`{:.language-cs} .

```cs
public class MockingRenderPipeline : RenderPipeline
{
	private readonly MockingRenderContext m_rc;
	public MockingRenderPipeline(RhinoDoc doc, RunMode mode, RenderPlugIn plugin, MockingRenderContext rc)
		: base(doc, mode, plugin, RenderSize(doc),
				"MockingBird (modal)", Rhino.Render.RenderWindow.StandardChannels.RGBA, false, false)
	{
		m_rc = rc;
	}

	protected override bool OnRenderBegin()
	{
		m_rc.Thread = new Thread(m_rc.Renderer)
		{
			Name = "MockingBird Modal Rendering thread"
		};
		m_rc.Thread.Start();
		return true;
	}

	protected override bool OnRenderBeginQuiet(Size imageSize)
	{
		return OnRenderBegin();
	}

	protected override bool OnRenderWindowBegin(RhinoView view, Rectangle rectangle)
	{
		return false;
	}

	protected override void OnRenderEnd(RenderEndEventArgs e)
	{
		// stop render engine here.
		m_rc.StopRendering();
	}

	protected override bool ContinueModal()
	{
		return !m_rc.Done;
	}
}
```

On our implementation of AsyncRenderContext we need to override one function, `StopRendering()`{:.language-cs} . Obviously we have one extra function, which is the main entry to our rendering code, `Renderer()`{:.language-cs} .

```cs
/// <summary>
/// The render context essentially hosts our render engine. It'll contain the
/// main render entry function that gets called by the RenderPipeline
/// mechanism.
/// </summary>
public class MockingRenderContext : AsyncRenderContext
{
	/// <summary>
	/// Hold on to the thread
	/// </summary>
	public Thread Thread { get; set; }
	/// <summary>
	/// Hold on to the render window (note, may be moved to base class
	/// AsyncRenderContext
	/// </summary>
	public RenderWindow RenderWindow { get; set; }
	public bool Done { get; private set; }
	private bool Cancel { get; set; }

	/// <summary>
	/// Called when through UI interaction the render process is to be
	/// stopped.
	/// </summary>
	public override void StopRendering()
	{
		Cancel = true;
	}

	// our main rendering function.
	public void Renderer()
	{
		RhinoApp.WriteLine("Starting modal MockingBird");

		Done = false;
		using (var channel = RenderWindow.OpenChannel(RenderWindow.StandardChannels.RGBA))
		{
			var size = RenderWindow.Size();
			var max = (float)size.Width*size.Height;
			var rendered = 0;
			for (var x = 0; x < size.Width; x++)
			{
				for (var y = 0; y < size.Height; y++)
				{
					channel.SetValue(x, y, Color4f.FromArgb(1.0f, 1.0f, 0.75f, 0.5f));
					rendered++;
					Thread.Sleep(1);
					RenderWindow.SetProgress("rendering...", rendered/max);
				}
				if (Cancel) break;
			}
		}

		// must set progress to 1.0f to signal RenderWindow (and pipeline/rc)
		// that rendering is now done.
		RenderWindow.SetProgress("MockingBird Modal done", 1.0f);

		// and send completion signal
		RenderWindow.EndAsyncRender(RenderWindow.RenderSuccessCode.Completed);

		Done = true;
		RhinoApp.WriteLine("... done");
	}
}

```

---
title: Render Engine Integration - ChangeQueue
description: This guide, the third of a series, discusses using the ChangeQueue to digest file content for a render engine.
authors: ['nathan_letwory']
author_contacts: ['nathanletwory']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Rendering']
origin: http://www.letworyinteractive.com/b/2016/08/integrating-a-render-engine-in-hinoceros-3d-using-rhinocommon-mockingbird-changequeue/
order: 3
keywords: ['renderer', 'integration', 'RhinoCommon']
layout: toc-guide-page
redirect_from: "/guides/rhinocommon/mockingbird-changequeue/"
---


## Overview

This is part three in the series on render engine integration in Rhinoceros 3D using RhinoCommon (v6).

1. [Setting up the plug-in]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-introduction/)
1. [Modal Rendering]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-modal/)
1. ChangeQueue (this guide)
1. [Interactive render - viewport integration]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-interactive-viewport/)
1. Preview render *(forthcoming)*

If you have not already read parts [one](({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-introduction/)) and [two](({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-modal/)), please do so before proceeding.

## Converting the Document

When it comes to converting a 3dm document to a form our render engine understands there are two options: the hard way, or the easy way.

The hard way would be to just take the `RhinoDoc`{:.language-cs}  given in the `Render()`{:.language-cs}  function and then iterate over the many different tables with `DocObjects`{:.language-cs}  and do the conversion then and there. For geometry and render content it probably won't be too hard, but when it comes to Blocks and Block instances it all becomes quite complex very quickly.

Since I don't like complex I'll just go with the easy way.

The [code for this plug-in version](https://github.com/mcneel/rhino-developer-samples/tree/6/rhinocommon/cs/SampleCsRendererIntegration/MockingBird/MockingBirdChangeQueue) can be found at [the MockingBird Git repository](https://github.com/mcneel/rhino-developer-samples/tree/6/rhinocommon/cs/SampleCsRendererIntegration/MockingBird).

## ChangeQueue

The `ChangeQueue`{:.language-cs}  is a central way of getting the 3dm in an already pre-digested format. Among things it will handle Blocks and their instances all for you. The `ChangeQueue`{:.language-cs}  is also usable for both production (modal) rendering and interactive real-time rendering in the viewport. Even preview scene rendering can be done through the `ChangeQueue`{:.language-cs}  mechanism, meaning that preview rendering can be easily added without too much hassle. We'll come to that later though.

Setting up the `ChangeQueue`{:.language-cs}  is pretty straight-forward. A class deriving from `Rhino.Render.ChangeQueue.ChangeQueue`{:.language-cs}  is needed and a set off Apply-functions need to be implemented.

```cs
public class MockingChangeQueue : ChangeQueue
{
	// for a regular rhino document (i.e. currently
	// active)
	// The constructor can look like you want, as long as the plugin ID,
	// document serial number and view info are given, needed for
	// the base class
	public MockingChangeQueue(Guid pluginId, uint docRuntimeSerialNumber, ViewInfo viewinfo)
		: base(pluginId, docRuntimeSerialNumber, viewinfo)
	{
	}

	/// <summary>
	/// The camera information.
	/// </summary>
	/// <param name="viewInfo">new viewport info</param>
	protected override void ApplyViewChange(ViewInfo viewInfo)
	{
		var vp = viewInfo.Viewport;
		int near, far;
		var screenport = vp.GetScreenPort(out near, out far);
		RhinoApp.WriteLine($"Camera @ {vp.CameraLocation}, direction {vp.CameraDirection}");
		RhinoApp.WriteLine($"\twith near {near} and far {far}");
		RhinoApp.WriteLine($"\tand {screenport}");
	}

	protected override void ApplyEnvironmentChanges(RenderEnvironment.Usage usage)
	{
		// background - when camera ray doesn't hit any geometry
		// skylight - image-based lighting
		// reflection - what is seen in reflections
		var env = EnvironmentForid(EnvironmentIdForUsage(usage));
		RhinoApp.WriteLine(env != null ? $"{usage} {env.Name}" : $"No env for {usage}");
		// retrieving textures is with RenderMaterial, refer to HandleRenderMaterial()
	}

	/// <summary>
	/// Lights in the scene, including any automatic lighting
	/// (will be CameraDirectional)
	/// </summary>
	/// <param name="lightChanges">List of <code>Light</code>s</param>
	protected override void ApplyLightChanges(List<Light> lightChanges)
	{
		foreach (var light in lightChanges)
		{
			RhinoApp.WriteLine($"A {light.ChangeType} light. {light.Data.Name}, {light.Data.LightStyle}");
			if (light.Data.LightStyle == LightStyle.CameraDirectional)
			{
				RhinoApp.WriteLine("Use ChangeQueue.ConvertCameraBasedLightToWorld() to convert light transform to world");
				RhinoApp.WriteLine($"\told location {light.Data.Location}, direction {light.Data.Direction}");
				ConvertCameraBasedLightToWorld(this, light, GetQueueView());
				RhinoApp.WriteLine($"\tnew location {light.Data.Location}, direction {light.Data.Direction}");
			}
		}
	}

	/// <summary>
	/// Get all geometry data.
	/// </summary>
	/// <param name="deleted">List of Mesh instance IDs</param>
	/// <param name="added">List of <code>Mesh</code>es to add</param>
	protected override void ApplyMeshChanges(Guid[] deleted, List<Mesh> added)
	{
		RhinoApp.WriteLine($"Received {added.Count} new meshes, {deleted.Length} for deletion");
		foreach (var m in added)
		{
			var totalVerts = 0;
			var totalFaces = 0;
			var totalQuads = 0;
			var meshIndex = 0;
			RhinoApp.WriteLine($"\t{m.Id()} with {m.GetMeshes().Length} submeshes");
			foreach (var sm in m.GetMeshes())
			{
				RhinoApp.WriteLine($"\t\tmesh index {meshIndex} mesh with {sm.Vertices.Count} verts, {sm.Faces.Count} faces ({sm.Faces.QuadCount} quads).");
				totalVerts += sm.Vertices.Count;
				totalFaces += sm.Faces.Count;
				totalQuads += sm.Faces.QuadCount;
				RhinoApp.WriteLine($"\t\tFor material we remember ({m.Id()},{meshIndex}) as identifier. Connect dots in ApplyMeshInstanceChanged");
				meshIndex++;
			}
			RhinoApp.WriteLine($"\t{totalVerts} verts, {totalFaces} faces (of which {totalQuads} quads)");
		}
	}

	/// <summary>
	/// Mesh instances added or deleted. Mesh instances here really means the
	/// objects in a scene. More than one object can reference the same geometry.
	/// For a single-shot render (production render) this is also where
	/// materials for the scene are provided.
	/// </summary>
	/// <param name="deleted">Objects to delete, a list of unsigned ints</param>
	/// <param name="addedOrChanged">List of MeshInstances (objects)</param>
	protected override void ApplyMeshInstanceChanges(List<uint> deleted, List<MeshInstance> addedOrChanged)
	{
		RhinoApp.WriteLine($"Received {addedOrChanged.Count} mesh instances to be either added or changed");
		foreach (var mi in addedOrChanged)
		{
			var mat = MaterialFromId(mi.MaterialId);
			RhinoApp.WriteLine($"\tAdd or change object {mi.InstanceId} uses mesh <{mi.MeshId}, {mi.MeshIndex}>, and material {mi.MaterialId}, named {mat.Name})");
			HandleRenderMaterial(mat);

		}
		// For single-shot rendering there won't be deletions.
	}

	private void HandleRenderMaterial(RenderMaterial material)
	{
		RhinoApp.WriteLine($"\t\tMaterial {material.Name} is a {material.TypeName} ({material.TypeDescription})");

		var diffchan = material.TextureChildSlotName(RenderMaterial.StandardChildSlots.Diffuse);
		var difftex = material.FindChild(diffchan) as RenderTexture;
		if (difftex != null)
		{
			RhinoApp.WriteLine($"\t\t\ta diffuse texture was found {difftex.Name}, hash {difftex.RenderHashWithoutLocalMapping}");
			RhinoApp.WriteLine($"\t\t\tprojection {difftex.GetProjectionMode()}, env mapping {difftex.GetInternalEnvironmentMappingMode()}");
			RhinoApp.WriteLine($"\t\t\tlocal mapping xform {difftex.LocalMappingTransform}");
			var texeval = difftex.CreateEvaluator(RenderTexture.TextureEvaluatorFlags.DisableLocalMapping);
			int u, v, w;
			difftex.PixelSize(out u, out v, out w);
			// for procedural textures there's no u/v/w, so check for that and set
			// to some acceptable defaults.
			if (u == 0) u = 1024;
			if (v == 0) v = 1024;
			if (w == 0) w = 1;
			RhinoApp.WriteLine($"\t\t\tTexture size {u}x{v}x{w}");
		}

	}
}

```

The function in the given snippet are the most basic apply functions one should need to integrate a production render engine. The functions all have been provided with clear documenting comments.

An instance of this new `MockingChangeQueue`{:.language-cs}  will be created when the `MockingRenderContext`{:.language-cs}  is instantiated.

```cs
public MockingChangeQueue ChangeQueue { get; private set; }

public MockingRenderContext(PlugIn plugIn, RhinoDoc doc)
{
	// set up view info
	ViewInfo viewInfo = new ViewInfo(doc.Views.ActiveView.ActiveViewport);
	ChangeQueue = new MockingChangeQueue(plugIn.Id, doc.RuntimeSerialNumber, viewInfo);
}

```

To use this new `ChangeQueue`{:.language-cs}  the `Render()`{:.language-cs} function needs to be adapted slightly - the `CreateWorld()`{:.language-cs}  function on our `MockingChangeQueue`{:.language-cs}  instance should be called once on the main thread. This is to ensure proper functionality of the `ChangeQueue`{:.language-cs}  mechanism.

```cs
protected override Result Render(RhinoDoc doc, RunMode mode, bool fastPreview)
{
	// initialise our render context
	MockingRenderContext rc = new MockingRenderContext(this, doc);

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

	// prime the ChangeQueue. We do it here, since this *has* to
	// happen on the main thread.
	rc.ChangeQueue.CreateWorld();

	// now fire off render thread.
	var renderCode = pipeline.Render();

	// note that the rendering isn't complete yet, rather the pipeline.Render()
	// call starts a rendering thread. Here we essentially check whether
	// starting that thread went ok.
	if (renderCode != RenderPipeline.RenderReturnCode.Ok)
	{
		RhinoApp.WriteLine("Rendering (mockingbird modal+changequeue) failed:" + rc.ToString());
		return Result.Failure;
	}

	// all ok, so we are apparently rendering.
	return Result.Success;
}

```

Loading the <a href="https://github.com/mcneel/rhino-developer-samples/blob/6/rhinocommon/cs/SampleCsRendererIntegration/MockingBird/TestFiles/MockingBirdTest.3dm">3dm test file</a> and running the `_Render`{:.language-cs}  command will yield output something like:

```sh
Command: _Render
Camera @ 43.1114947706824,-74.6734897875561,49.7823265250374, direction -43.3,75,-50
	with near 0 and far 1
	and {X=0,Y=0,Width=781,Height=387}
No env for Background
Skylighting Studio
ReflectionAndRefraction Studio
Received 2 new meshes, 0 for deletion
	0c35babb-ca2a-4b09-9ab6-72610f38717f with 6 submeshes
		mesh index 0 mesh with 4 verts, 2 faces (0 quads).
		For material we remember (0c35babb-ca2a-4b09-9ab6-72610f38717f,0) as identifier. Connect dots in ApplyMeshInstanceChanged
		mesh index 1 mesh with 4 verts, 2 faces (0 quads).
		For material we remember (0c35babb-ca2a-4b09-9ab6-72610f38717f,1) as identifier. Connect dots in ApplyMeshInstanceChanged
		mesh index 2 mesh with 4 verts, 2 faces (0 quads).
		For material we remember (0c35babb-ca2a-4b09-9ab6-72610f38717f,2) as identifier. Connect dots in ApplyMeshInstanceChanged
		mesh index 3 mesh with 4 verts, 2 faces (0 quads).
		For material we remember (0c35babb-ca2a-4b09-9ab6-72610f38717f,3) as identifier. Connect dots in ApplyMeshInstanceChanged
		mesh index 4 mesh with 4 verts, 2 faces (0 quads).
		For material we remember (0c35babb-ca2a-4b09-9ab6-72610f38717f,4) as identifier. Connect dots in ApplyMeshInstanceChanged
		mesh index 5 mesh with 4 verts, 2 faces (0 quads).
		For material we remember (0c35babb-ca2a-4b09-9ab6-72610f38717f,5) as identifier. Connect dots in ApplyMeshInstanceChanged
	24 verts, 12 faces (of which 0 quads)
	47bcaad4-c0c0-461b-be76-42a312a566db with 1 submeshes
		mesh index 0 mesh with 9557 verts, 9944 faces (8136 quads).
		For material we remember (47bcaad4-c0c0-461b-be76-42a312a566db,0) as identifier. Connect dots in ApplyMeshInstanceChanged
	9557 verts, 9944 faces (of which 8136 quads)
Received 7 mesh instances to be either added or changed
	Add or change object 4184240262 uses mesh <0c35babb-ca2a-4b09-9ab6-72610f38717f, 0>, and material 2763457527, named Custom 001)
		Material Custom 001 is a Custom (Custom material.)
			a diffuse texture was found 3D Checker Texture 001, hash 2924537820
			projection MappingChannel, env mapping Automatic
			local mapping xform R0=(1,0,0,0), R1=(0,1,0,0), R2=(0,0,1,0), R3=(0,0,0,1)
			Texture size 1024x1024x1
	Add or change object 1104812003 uses mesh <0c35babb-ca2a-4b09-9ab6-72610f38717f, 1>, and material 1789231709, named Plaster 001)
		Material Plaster 001 is a Plaster (Plaster material.)
	Add or change object 2271356598 uses mesh <47bcaad4-c0c0-461b-be76-42a312a566db, 0>, and material 2348445746, named Metal 001)
		Material Metal 001 is a Metal (Metal material.)
	Add or change object 3468198068 uses mesh <0c35babb-ca2a-4b09-9ab6-72610f38717f, 5>, and material 2304042105, named Gem 001)
		Material Gem 001 is a Gem (Gem material.)
	Add or change object 1980032977 uses mesh <0c35babb-ca2a-4b09-9ab6-72610f38717f, 4>, and material 2304042105, named Gem 001)
		Material Gem 001 is a Gem (Gem material.)
	Add or change object 1399830541 uses mesh <0c35babb-ca2a-4b09-9ab6-72610f38717f, 2>, and material 2304042105, named Gem 001)
		Material Gem 001 is a Gem (Gem material.)
	Add or change object 3956531048 uses mesh <0c35babb-ca2a-4b09-9ab6-72610f38717f, 3>, and material 2304042105, named Gem 001)
		Material Gem 001 is a Gem (Gem material.)
```

---

## Next Steps

This is part three in the series on render engine integration in Rhinoceros using RhinoCommon.  The next guide is [Render Engine Integration - Interactive Viewport]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-interactive-viewport/).

---

## Related Topics

- [Render Engine Integration - Introduction]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-introduction/)
- [Render Engine Integration - Modal]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-modal/)
- [Render Engine Integration - Interactive Viewport]({{ site.baseurl }}/guides/rhinocommon/render-engine-integration-interactive-viewport/).
- Preview render *(forthcoming)*

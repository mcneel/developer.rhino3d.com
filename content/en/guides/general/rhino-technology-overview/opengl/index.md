+++
aliases = []
authors = [ "steve" ]
categories = [ "Overview" ]
description = "Rhino 9 no longer uses OpenGL as its default display technology. What that means if your plugin calls OpenGL directly."
keywords = [ "developer", "graphics", "deprecated", "opengl", "direct3d", "directx", "metal", "display" ]
languages = [ "C++", "C#" ]
sdk = [ "General" ]
title = "OpenGL in Rhino 9"
type = "guides"
weight = 10

[admin]
TODO = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 9

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true
+++

## Summary

**Rhino 9 no longer uses OpenGL as its default display technology.**

- On **Windows**, Rhino uses **Direct3D 11** by default; OpenGL is available.
- On **macOS**, Rhino only uses **Metal**.

The OpenGL display pipeline still ships in Rhino 9 and users can still switch to it. Nothing in the C++ SDK or RhinoCommon has been marked deprecated or obsolete — your code will still compile without new warnings.

What has changed is the *default*. If your plugin directly calls OpenGL, you need to make sure that OpenGL is active. **Code that assumes an OpenGL context will not draw anything for most Rhino 9 users and in worst cases will crash Rhino.**

If your plugin only draws through functions provided by `CRhinoDisplayPipeline` / `CRhinoDisplayEngine` (C++) or `Rhino.Display.DisplayPipeline` (RhinoCommon), you are safe as these functions were written to have different low level implementations based on the active GPU techology.

## Why Rhino moved away from OpenGL

The primary reason is **stability**. From the [Direct3D Display announcement](https://discourse.mcneel.com/t/rhino-beta-feature-direct3d-display/206910):

> The primary reason for switching to Direct3D is stability. McNeel technical support has had to deal with many OpenGL driver issues over the years. This is also why we could not support Windows ARM or virtualization systems like Parallels or VMware. The OpenGL drivers on those systems were very problematic and would often crash.

Moving to Direct3D on Windows lets Rhino run on hardware and in environments that were previously unsupported, most notably Windows on ARM and virtual machines such as Parallels, VMware, and Remote Desktop.

On macOS, the move was forced by Apple. Apple deprecated OpenGL in macOS 10.14, and `AGL.framework` was removed entirely in macOS 26.

Rhino 9 targets Direct3D 11 rather than Direct3D 12, because D3D11 has everything Rhino currently needs and still supports older GPUs that are widely in use. There may be a Direct3D 12 display available in a future version of Rhino.

## Is OpenGL going away?

There is no removal date and no announced plan to remove OpenGL support. That said, OpenGL is now the path that receives the least testing among the user community. Treat OpenGL as legacy: it is fine for it to remain a fallback, but you should not write new code that depends on it.

## What this means for your plugin

### Do not assume an OpenGL context is current

The most common failure mode is a display conduit that issues `gl*` calls directly. Under Direct3D or Metal there is no current OpenGL context, so this drawing simply does not appear or potentially even crashes Rhino.

There is no shim that translates OpenGL calls to Direct3D. You need to either detect the active technology and skip your OpenGL path, or move your drawing to use Rhino's SDKs. If there is functionality missing from the Rhino SDK that you were only able to implement with OpenGL, **please let McNeel** know so they can try to add this.

### Detect the active display technology

In C++, use `CRhinoDisplayPipeline::EngineTechnology()` (available as of Rhino 8.35) with the pipeline's engine:

```cpp
bool CMyDisplayConduit::ExecConduit(CRhinoDisplayPipeline& pipeline, UINT channel, bool& terminate)
{
  CRhinoDisplayPipeline::DisplayTechnologies tech =
     CRhinoDisplayPipeline::EngineTechnology(pipeline.Engine());

  if (CRhinoDisplayPipeline::DisplayTechnologies::OpenGL != tech)
  {
    // No OpenGL context is current. Skip any raw gl* drawing.
    return true;
  }

  // ... existing OpenGL drawing ...
  return true;
}
```

In RhinoCommon, use the `DisplayPipeline.Technology` property:

```cs
private void OnPostDrawObjects(object sender, DrawEventArgs e)
{
  if (e.Display.Technology != DisplayTechnology.OpenGL)
  {
    // No OpenGL context is current. Skip any raw GL drawing.
    return;
  }

  // ... existing OpenGL drawing ...
}
```

`DisplayPipeline.Technology` is available in **Rhino 8.35 and later**, so the same check compiles and behaves correctly against both Rhino 8 and Rhino 9.

## Switching display technology

Users choose the display technology in **Options > View > GPU**. This is an application-wide setting, not per-viewport or per-display-mode. Restarting Rhino after switching is recommended.

The `SystemInfo` command reports which technology is active, which is useful when helping a user diagnose a display problem in your plugin.


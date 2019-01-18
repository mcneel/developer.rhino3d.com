---
title: RDK Rendering
description: This document describes how to use the RDK's rendering classes in C/C++.
authors: ['john_croudy']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin', 'Rendering']
layout: toc-guide-page
---
### Introduction
Even before the RDK existed, Rhino had a rendering pipeline and a _Render_ command which would allow the current render engine (e.g., Rhino Render or Flamingo) to render the scene. The RDK builds on and enhances this system to provide the following features:

* An extensible Render Window UI.
* A frame buffer with both built-in and customizable channels.
* An extensible post effect system.
* Exposure and color adjustment controls.
* Asynchronous rendering.

In addition to the built-in functionality, plug-in developers have the ability to add their own UI panes, custom channels, and post effects. The asynchronous rendering feature frees users from being locked out of Rhino while rendering proceeds and actually allows multiple renders to run at the same time using different render engines, if so desired.

### The many faces of a render window.
The term _render window_ can be a source of confusion, because there are several different objects in the RDK that could be called by that name:

* The physical render window that the user sees on the screen.
* The data and structures that lie behind the `IRhRdkRenderWindow` interface.
* The `RenderWindow()` SDK method (on `CRhinoSdkRender` and `CRhRdkSdkRender`).
* The RenderWindow command.

In order to avoid confusion, the physical render window will be called the _render frame_ in this article. Elsewhere, the phrase 'render window' will mean the `IRhRdkRenderWindow` interface. If the method is mentioned, it will be written in this form: `RenderWindow()` including the parentheses. The command will be referred to as the RenderWindow _command_.

### Getting started
Let's start at the top and follow the _synchronous_ rendering process from the moment the user presses the Render button until the render frame is closed. You must first create a subclass of `CRhRdkSdkRender`:
```cpp
class CExampleSdkRender : public CRhRdkSdkRender
{
public:
	CExampleSdkRender(const CRhinoCommandContext& context, CRhinoRenderPlugIn& plugIn,
	                  bool bPreview, const ON_wString& sCaption, UINT uIconId);

	virtual CRhinoSdkRender::RenderReturnCodes Render(const ON_2iSize& sizeImage) override;
	virtual CRhinoSdkRender::RenderReturnCodes RenderWindow(CRhinoView* pView,
	                         const LPRECT pRect, bool bInPopupWindow) override;
	...
};
```
The first thing you'll notice are the `Render()` and `RenderWindow()` methods. These will be called in response to the _Render_ and _RenderWindow_ commands respectively. In the following discussion, when we refer to the Render command or the `Render()` method, we are also referring to the RenderWindow command and the `RenderWindow()` method, depending on which one the user chose.

In the constructor of CExampleSdkRender you do your basic initialization. This may include adding channels to the render window.
```cpp
CExampleSdkRender::CExampleSdkRender(const CRhinoCommandContext& context, CRhinoRenderPlugIn& plugIn,
                                     const ON_wString& sCaption, UINT uIconId, bool bPreview)
	:
	CRhRdkSdkRender(context, plugIn, sCaption, uIconId)
{
	// The RDK only adds the red, green, blue and alpha channels by default,
	// but it provides several other built-in channels. Let's add some.

	// First, get the render window.
	auto& rw = GetRenderWindow();

	// If this render window is being reused, remove any non-fixed channels
	// that were added last time.
	rw.ClearChannels();

	// Add a channel for use as a z-buffer.
	rw.AddChannel(IRhRdkRenderWindow::chanDistanceFromCamera, sizeof(float));

	// Add channels for normals (X, Y, Z).
	rw.AddChannel(IRhRdkRenderWindow::chanNormalX, sizeof(float));
	rw.AddChannel(IRhRdkRenderWindow::chanNormalY, sizeof(float));
	rw.AddChannel(IRhRdkRenderWindow::chanNormalZ, sizeof(float));
}
```
In the code example above, getting the render window for the first time will cause it to be created. This also causes the creation of a _render session_ which is an object that the RDK uses to keep track of rendering progress for each render window. As rendering proceeds, the render session goes through a set of states, defined by the `IRhRdkRenderSession::Status` enum. This includes states such as _Initializing_, _Rendering_ and _Completed_, among others. As long as the user sees a render frame on the screen, the render session and render window objects will exist and be associated with the render frame. When the user closes the render frame, the render session will become _disposed_. In this state, the session is waiting in a list to be deleted at the end of the command. This system prevents problems causes by deleting the session while the plug-in may still be using it, perhaps from a worker thread. At the end of the command, all disposed sessions will be deleted.

### The rendering process
Being a Rhino render engine, your plug-in must include a class derived from CRhinoRenderPlugIn. When the user runs the Render command, if yours is the current render engine, Rhino will call your plug-in's `Render()` method. Your implementation of this method must instantiate your CExampleSdkRender object on the stack as a local variable and call its `Render()` method, passing the desired image size. This size can be obtained by calling the base sdkRender's `RenderSize()` method. This will return the size according to the user's settings in the Rendering panel:
```cpp
CRhinoCommand::result CExampleRhinoPlugIn::Render(const CRhinoCommandContext& context, bool bPreview)
{
	const auto* pDoc = context.Document();
	if (nullptr == pDoc)
		return CRhinoCommand::failure;

	// If you need to check for a valid license, do that first.
	if (!CheckLicense())
		return CRhinoCommand::failure;

	// Instantiate your SDK Render object.
	CExampleSdkRender sdkRender(context, *this, L"Example", IDI_EXAMPLE, bPreview);

	// Get the size of the image to render.
	const auto size = sdkRender.RenderSize(*pDoc, true);

	// Do the rendering.
	const auto result = sdkRender.Render(size);

	if (CRhinoSdkRender::render_ok == result)
		return CRhinoCommand::success;

	return CRhinoCommand::failure;
```
<!--*This comment fixes Atom's syntax highlighter after the lone asterisk above*-->
 `CExampleSdkRender::Render()` can do some more 'heavy' initialization that was not done in the constructor, such as creating render meshes or opening a progress window. After that, it calls `CRhRdkSdkRender::Render()` to do the actual rendering:
```cpp
CRhinoSdkRender::RenderReturnCodes CExampleSdkRender::Render(const ON_2iSize& sizeImage)
{
	auto* pView = RhinoApp().ActiveView(); // This is old and wrong. Ask Andy.
	if (nullptr == pView)
		return CRhinoSdkRender::render_no_active_view;

	// Force render meshes to be created on the main thread.
	const auto& vp = pView->ActiveViewport().VP();
	auto* pIterator = NewRenderMeshIterator(vp, true, false);
	pIterator->EnsureRenderMeshesCreated();

	// You can now use this iterator to get all of the meshes in the scene.
	// While the iterator is alive, all meshes are guaranteed to be available
	// which means you don't need to copy them during the rendering process.
	CRhRdkRenderMesh rm;
	pIterator->Reset();
	while (pIterator->Next(rm))
	{
		// TODO: Use the mesh. This might be the point at which you create
		// your acceleration structure or, if you are writing a renderer
		// that uses its own mesh representation, you might do the
 		// conversion here. One thing to remember - the
 		// IRhRdkSdkRenderMeshIterator::Next function is not, at this time,
		// thread safe, so please don't pass the iterator's pointer into
		// multiple render threads and use it to query the mesh list.
		// In any case, it's not really optimized for in-render access.
	}

	// Once everything is set up, do the actual rendering.
	// By keeping the iterator alive, we ensure the meshes
	// don't get deleted.
	const auto result = __super::Render(sizeImage);

	// After rendering, delete the iterator and the render meshes.
	delete pIterator;

	return result;
}
```
The call to `__super::Render(sizeImage)` above does the actual rendering using the Rhino render pipeline. This works by calling into virtual functions on your CExampleSdkRender object at various stages of the process. When Rhino calls the various functions on the SDK Render object, the RDK gets in between and forwards some of the calls directly to you; other calls it processes itself. The calls that are directly forwarded are the original render pipeline functions that have been in Rhino since the beginning:
* `NeedToProcessLightTable()`
* `AddLightToScene()`
* `NeedToProcessGeometryTable()`
* `IgnoreRhinoObject()`
* `AddRenderMeshToScene()`
* `RenderSceneWithNoMeshes()`
* `RenderPreCreateWindow()`
* `StartRendering()`
* `RenderEnterModalLoop()`
* `RenderContinueModal()`
* `RenderExitModalLoop()`

The first override to be called is `NeedToProcessLightTable()`. This generally returns true unless you have implemented a light cache or other optimization. Then, for each light in the scene, Rhino will call your override of `AddLightToScene()` in which you will set up your light structures for the rendering process to use. Next, Rhino calls `NeedToProcessGeometryTable()`. If you return true, Rhino will call `AddRenderMeshToScene()` for each object. If your renderer needs to set up any structures, it can do that now. If not, it does not need to override that function, but be aware that if you want rendering to proceed, you must override `RenderSceneWithNoMeshes()` (which is called next) to return true. Note that if Rhino encounters an object that is not meshable (e.g., a point or curve), it will call `IgnoreRhinoObject()`. If your renderer knows how to render objects without meshes, you can return false. Otherwise it's a good idea to return true so that the object is skipped.

After lights and meshes have been processed, Rhino creates the render frame on the screen, but just before it does, it calls `RenderPreCreateWindow()`. This is probably not useful but was kept for backward compatibility. Now Rhino creates the render frame on the screen and calls `StartRendering()`. In this override, you should create one or more worker threads to do the actual rendering.

Because Rhino itself is not aware of the asynchronous option (it's an RDK concept), it calls `RenderEnterModalLoop()` to ask if you want to go into a loop while waiting for rendering to finish. Unless there has been some kind of error, you must always return true (even in the asynchronous case), otherwise Rhino will abort. After that, Rhino will enter a loop calling `RenderContinueModal()` until it returns false. This is the point where synchronous and asynchronous renderers use different logic. Synchronous renderers will return true until rendering finishes, but asynchronous renderers will return false because they don't want to go into a modal loop, they want the pipeline to exit leaving the render frame open on the screen so that rendering can proceed in the background. Finally, Rhino will call `RenderExitModalLoop()` and generally your override will return true in order for Rhino to return a successful result code.

### Rendering, pausing, resuming and canceling
In the synchronous case, rendering proceeds in one or more worker threads while Rhino sits in the modal loop pumping messages and keeping the UI alive. During this time, the user can use the menu and tool bars in the render frame. The RDK calls the `SupportsPause()` method on your sdkRender object to determine if the pause button should be enabled on the screen. If you return true, you will be expected to also implement `PauseRendering()` and `ResumeRendering()`. These functions can be as simple as setting and clearing a flag which the render threads check periodically. Pausing is most useful when the renderer is asynchronous because the user can continue using Rhino while rendering is paused and continue rendering later.

If the user chooses the _Stop_ option, `StopRendering()` will be called on your sdkRender object. Your override should take whatever action is necessary to immediately stop rendering. It should tell any render threads to abort and wait for them to exit before returning. If a thread continues after this function returns, Rhino may crash because it assumes that the client is no longer using any of the rendering objects or meshes.

### Asynchronous rendering
We touched on the differences between synchronous and asynchronous rendering above, but now we will examine them in more detail. One of the main differences with asynchronous rendering is the existence of an object called an _async render context_. This is represented by the `IRhRdkAsyncRenderContext` interface. It is an object that takes over the role of the sdkRender object after that object goes off the stack. Recall that as soon as asynchronous rendering begins, the renderer asks Rhino to _not_ continue the modal loop. This causes Rhino to exit the render pipeline and the sdkRender object goes off the stack and is deleted. The async render context persists, owned by the associated render session and enables communication between the RDK and the render engine, allowing requests such as pause, resume and stop to pass to the renderer in the absence of the sdkRender object.

The async render context should be created in your sdkRender constructor, before any access to the render session or render window. It is the call to `SetAsyncRenderContext()` that establishes the render session as being asynchronous rather than synchronous.
```cpp
CExampleSdkRender::CExampleSdkRender(const CRhinoCommandContext& context, CRhinoRenderPlugIn& plugIn,
                                     const ON_wString& sCaption, UINT uIconId, bool bPreview)
	:
	CRhRdkSdkRender(context, plugIn, sCaption, id)
{
	// It is critical that the render context is created first, before any calls to GetRenderWindow().
	SetAsyncRenderContext(new CExampleAsyncRenderContext(...));

	// Get the render window.
	auto& rw = GetRenderWindow(); // Note: GetRenderWindow() uses the async render context set above.

	...
}
```
The implementation of `IRhRdkAsyncRenderContext` is usually fairly simple. An example is shown below. You just have to handle a few functions for pausing, resuming and stopping rendering. This Windows-centric example assumes you have a single thread and you have stored its handle in `m_hRenderThread`.
```cpp
class CExampleAsyncRenderContext : public IRhRdkAsyncRenderContext
{
public:
	CExampleAsyncRenderContext(...);
	virtual ~CExampleAsyncRenderContext();

public: // Implement IRhRdkAsyncRenderContext.
	virtual void StopRendering(void) override;
	virtual bool SupportsPause(void) const override { return true; }
	virtual void PauseRendering(void) override { m_bPause = true; }
	virtual void ResumeRendering(void) override { m_bPause = false; }
	virtual void OnQuietRenderFinished(const IRhRdkRenderSession& session) override;
	virtual void DeleteThis(void) override { delete this; }
	virtual void* EVF(const wchar_t*, void*) override { return nullptr; }

private:
	HANDLE m_hRenderThread = NULL;
	bool m_bPause = false;
	bool m_bCancel = false;
};

void CExampleAsyncRenderContext::StopRendering(void)
{
	// Because the cancel flag is in this object, the render thread(s)
	// will need access to the object so they can check the flag.

	// If rendering is in progress, cancel it and wait for it to stop.
	if (NULL != m_hRenderThread)
	{
		m_bCancel = true;

		::WaitForSingleObject(m_hRenderThread, INFINITE);
		::CloseHandle(m_hRenderThread);
		m_hRenderThread = NULL;
	}
}
```
When rendering ends, the render frame remains on the screen. The user can choose to save the rendering, view the different channels, apply exposure or post-effects, or close the render frame. The render session associated with this render frame is now in one of the following states:

* _Completed_ ~ Rendering has completed successfully.
* _Canceled_  ~ Rendering was canceled by the user.
* _Aborted_   ~ Rendering was aborted. Happens when an async render aborts because the document is closed.
* _Failed_    ~ Rendering failed (but not because it was canceled).

The user can also choose to clone the render frame. What this means under the hood is that the render session will be cloned and a new render frame will be opened for that session. This allows the user to compare the renderings while viewing different channels or using different exposures or post-effects.

Eventually, the user will close the render frame (or close Rhino, which will, of course, close all render frames). When the render frame is closed, the render session goes into the 'Disposed' state, ready to be deleted at the end of the next command. If the user closes the render frame while rendering is underway, `StopRendering()` will be called before the render frame is closed.

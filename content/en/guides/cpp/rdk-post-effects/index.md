+++
authors = [ "john.croudy" ]
categories = [ "RDK" ]
description = "This document describes how to use the RDK's post effect classes in C/C++."
keywords = [ "RDK", "Rhino", "Renderer", "Development", "Plugin", "Rendering", "Post Effects" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "RDK Post Effect Classes"
type = "guides"
weight = 1
override_last_modified = "2020-08-11T17:33:46Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/labs/rendererdevelopmentkit10"
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

This is preliminary documentation. The functionality described below is not yet available.

### Introduction
Starting with Rhino 7, the RDK includes a new post effect system which allows plug-in developers to create their own post effects. Although this was possible prior to Rhino 7, earlier versions required the post effects to apply changes to the final RGBA bitmap pixels. This meant that the post effects could only work on low dynamic range (8-bit) color components. Furthermore, all processing had to be done on the CPU which could be very slow for some effects. The new _post effect pipeline_ allows post effects to process the original high dynamic range channel data and also allows this to be done on the _GPU_ if so desired. CPU post effects are, of course, still supported.

### The Post Effect pipeline
The new post effect system operates as a pipeline. The post effects selected by the user are run one after the other. The process begins with the rendered image which exists as a set of channels in the frame buffer. As each effect runs, it processes the output of the previous one. Each post effect can operate on any of the available channels, such as RGBA, distance-from-camera, etc.

### Post Effects
A post effect is an object that runs in the Render Window to process the rendered frame buffer image and create a modified version of it. The RDK comes with several built-in post effects such as Fog and Depth-of-field. After rendering, the user can choose which post effects to apply and in what order to apply them. Every post effect has a _type_ which determines when in the pipeline it is run. There are three of these types; _Early_, _Tone Mapping_ and _Late_ and the pipeline runs them in that order. Early post effects can operate on the original high dynamic range image. Tone mapping post effects perform _tone mapping_ on the high dynamic range image to produce a low dynamic range image. The pipeline then runs a process which clamps the values in the RGBA channels to the range 0..1. Finally, the late post effects process this low dynamic range image to produce a final image which the pipeline converts to an 8-bit image. It is this final image which is displayed to the user in the Render Frame.

### Writing a Post Effect

To write a post effect, a developer needs to create a subclass of one of the post effect base classes. Which base class you use depends on the type of your post effect.

If your post effect is intended to process the high dynamic range image, it must be derived from `CRhRdkNewEarlyPostEffectPlugIn`. If it is a tone mapper, it must be derived from `CRhRdkNewToneMappingPostEffectPlugIn`. If it operates on the low dynamic range image, it must be derived from `CRhRdkNewLatePostEffectPlugIn`.

The following is an example of an early post effect. All post effects follow this general style.

```
class CExamplePostEffect : public CRhRdkEarlyPostEffect
{
public:
	CExamplePostEffect() { InternalResetToFactoryDefaults(); }

	static UUID Ident(void);

	virtual UUID Id(void) const override { return Ident(); }
	virtual ON_wString LocalName(void) const override;
	virtual unsigned int BitFlags(void) const override { uf_ExecuteForProductionRendering | uf_ExecuteForRealtimeRendering; }
	virtual void RequiredChannels(OUT ON_SimpleArray<UUID>& aChan) const override;
	virtual bool Execute(IRhRdkNewPostEffectPipeline& pipeline, const ON_4iRect& rect) const override;
	virtual ExecuteWhileRenderingOptions GetExecuteWhileRenderingOption(void) const override { return ExecuteWhileRenderingOptions::Always; }
	virtual bool GetParameter(const wchar_t* wszName, OUT CRhRdkVariant& vValue) const override;
	virtual bool SetParameter(const wchar_t* wszName, const CRhRdkVariant& vValue) override;
	virtual bool ReadState(const IState& state) override;
	virtual bool WriteState(IState& state) const override;
	virtual void AddUISections(IRhRdkPostEffectUI& ui) override;
	virtual void ResetToFactoryDefaults(void) override { InternalResetToFactoryDefaults(); }
	virtual bool DisplayHelp(void) const override { return false; }
	virtual bool CanDisplayHelp(void) const override { return false; }

private:
	void InternalResetToFactoryDefaults(void);
};
```

Each post effect has a unique id and a localized name which are returned by the `Id()` and `LocalName()` methods respectively. Next you specify a set of usage flags by implementing the `BitFlags()` method. This tells the RDK certain facts about the post effect, including under which circumstances the post effect should be executed, which is done by calling the `Execute()` method. The implementation of `Execute()` will be described in detail later. The pipeline executes some post effects while rendering is proceeding. To let it know if your post effect can support this, you implement `GetExecuteWhileRenderingOption()`. This can be one of the following:

* 'Never' means the post effect does not support execution while rendering.
* 'Always' means the post effect supports execution while rendering.
* 'UseDelay' means the post effect supports execution while rendering, but only after a delay the first time.

Which of these you return depends on how time-consuming your post effect is and whether or not it requires the final rendered image to work properly. For example, the Fog effect works on single pixels and does not need the surrounding pixels in order to work. It is also quite fast. Therefore, it returns `ExecuteWhileRenderingOptions::Always`. On the other hand, the Watermark post effect needs to know how long the rendering took to complete, so it returns `ExecuteWhileRenderingOptions::Never` as it should only be run at the end, after rendering finishes.

#### Channels

Your post effect will, of course, need to use existing channels to get its source data. You should implement `RequiredChannels()` to tell the RDK which channels it is planning to use. This information is needed if the user chooses 'Automatic' in the Render Channels section of the Rendering panel:

```
void CExamplePostEffect::RequiredChannels(OUT ON_SimpleArray<UUID>& aChan) const
{
	CRhRdkEarlyPostEffect::RequiredChannels(aChan); // Be sure to call the base class.

	aChan.Append(IRhRdkRenderWindow::chanRGBA);

	...
}
```

#### Parameters

If your post effect has options or _parameters_ that the user can set, it will have some private members for these values. It must also implement the following methods:

* `GetParameter()` This is called by the user interface when it needs to display a value.
* `SetParameter()` This is called by the user interface when the user changes a value.
* `ReadState()` This is called when the post effect is read in during document loading.
* `WriteState()` This is called when the post effect is written out during document saving.
* `AddUISections()` This is called by the framework when the user interface is created. It allows the post effect to add sections (AKA roll-ups) to the user interface.
* `ResetToFactoryDefaults()` This resets the settings to their initial default values.

#### Help

Finally, your post effect can optionally provide a help page. If it does, it should implement `CanDisplayHelp()` to return _true_, and it must also implement `DisplayHelp()` to actually display the help page. Built-in post effects do this by opening a page from the Rhino documentation in the user's web browser.

Once you have defined your post effect class, you must create a factory for it and register the factory with the RDK:

#### Registration

```
class CExamplePostEffectPlugInFactory : public CRhRdkNewPostEffectPlugInFactory
{
public:
	virtual IRhRdkNewPostEffectPlugIn* NewPostEffectPlugIn(void) const override { return new CExamplePostEffect; }
	virtual UUID PlugInId(void) const final override; // Return your render plug-in's id.
};
```
Registration of the factory is done in your override of `CRhRdkRenderPlugIn::RegisterExtensions()` as follows:

```
void CMyRdkPlugIn::RegisterExtensions(void)
{
	...
	AddExtension(new CExamplePostEffectPlugInFactory);
	...
}
```

#### Implementation

The bulk of your post effect's implementation will be in the `Execute()` method. In this example, we will assume you are writing a CPU-based post effect.

All post effects read channel data (pixels), do some calculations, and create new channel data. Very often, this will involve reading RGBA data, processing it, and writing RGBA data. The `Execute()` method has a parameter of type `IRhRdkNewPostEffectPipeline&` and another of type `const ON_4iRect&`. The post effect queries the pipeline for existing channels (the input), asks it to create new channels (the output) and then iterates over pixels within the specified rectangle to create the output form the input. Sometimes the rectangle will be for the whole rendering, and sometimes (during rendering) it will be small areas of the rendering. You don't need to worry about this; you just need to process that exact rectangle of pixels.

In order to get input channels to process, the post effect must call `GetChannel()` specifying the channel identifier. Note that post effects are only allowed to access the color component channels (red, green, blue and alpha) by asking for the RGBA composite channel. Requests for the individual components (chanRed etc) are not allowed. So, to get the RGBA channel, the post effect does the following:

```
	// Get the RGBA channel.
	const auto* pRGBA = pepl.GetChannelForRead(RW::chanRGBA, 0);
	if (nullptr == pRGBA)
		return false;
```

At this point you decide if you want to run on the CPU or the GPU and obtain the correct interface, as follows. We are running on the CPU, so we write:

```
	const auto* pRGBA_CPU = pRGBA->CPU();
	if (nullptr == pRGBA_CPU)
		return false;

```

Having got the input channel, we now need to get a new output channel:

```
	// Create a new RGBA channel.
	auto* pNewRGBA = pepl.GetChannelForWrite(RW::chanRGBA, 0);
	if (nullptr == pNewRGBA)
		return false;
```

We also need to get the CPU interface:

```
	auto* pNewRGBA_CPU = pNewRGBA->CPU();
	if (nullptr == pNewRGBA_CPU)
		return false;
```

Now we are ready to enter the main pixel loop. Inside the loop, you read the input pixels by calling `pRGBA_CPU->GetValue()` or `pRGBA_CPU->GetValueEx()`. The latter is preferred because it's faster than the former which was only retained for backward compatibility. You write the output pixels by calling `pNewRGBA_CPU->SetValue()`. The iteration is best done by iterating over y and then x. You should include a call to `IRhRdkNewPostEffectPipeline::ReportProgress()` in the _y_ loop.

```
	// Iterate over all the pixels in the area.
	for (int y = rect.top; y < rect.bottom; y++)
	{
		for (int x = rect.left; x < rect.right; x++)
		{
			float in[4];
			if (pRGBA_CPU->GetValueEx(x, y, in))
			{
				float out[4];
				// Do calculations and create 'out' from 'in'.
				pNewRGBA_CPU->SetValue(x, y, ComponentOrder::RGBA, out);
			}
		}

		// Report progress and abort if requested to.
		if (!pipeline.ReportProgress(y))
			break;
	}
```

Finally, the new channel must be committed. This causes the pipeline to replace the current version of the channel with your new version. If you don't do this, you changes will be discarded.
```
	// Commit the changes.
	pipeline.Commit(pNewRGBA);
```

Your changes are now in the pipeline and the next post effect to run will use your pixel data as its input, assuming it's also working on RGBA data.

#### CPU vs GPU channels.

As mentioned above, post effects can run on the GPU instead of the CPU. By calling for the correct interface (`CPU()` or `GPU()`) you can transparently get access to the data you need. The pipeline takes care of managing the data and converting / moving it from CPU memory to GPU memory as needed. If several post effects run on the GPU, the data will be moved to the GPU and it will stay there while those post effects run. It will only be moved back to main CPU memory if a post effect calls `CPU()`.

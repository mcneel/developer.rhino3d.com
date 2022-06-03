+++
authors = [ "john.croudy" ]
categories = [ "RDK" ]
description = "This document describes how to use the RDK dithering class in C/C++."
keywords = [ "RDK", "Rhino", "Renderer", "Development", "Plugin", "Dithering" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "RDK Dithering"
type = "guides"
weight = 1
override_last_modified = "2019-01-16T16:52:27Z"

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
### Introduction
Image _dithering_ is a process in which some form of noise is added to an image in order to reduce color banding and other artifacts. This is commonly used when a display device is unable to display the full range of colors. The image below shows an extreme example. A photo was converted to use only two colors. On the left, no dithering was used and a lot of detail has been lost. On the right, Floyd-Steinberg dithering was used and the amount of detail is much improved. Although modern displays don't usually require any dithering, there are cases where it can make a subtle difference to the final quality of an image. For this reason, the RDK provides two kinds of dithering, _Simple Noise_ and _Floyd Steinberg_.

![Dithering](/images/rdk-dithering.png)
<small><small><small>Photo by John Croudy.</small></small></small>

### The Document Dithering Settings
The _RDK Document Dithering settings_ is a document-resident dithering object which affects renderings. If you have a Rhino document, you can read and write that document's dithering settings through the document's [IRhRdkDithering](/api/cpp/class_i_rh_rdk_dithering.html) interface. Any changes you make will appear in the Dithering and Color Adjustment section of the Rendering panel and will also be stored in the 3dm file. Getting the dithering settings from a document always returns a const reference. To write to the settings, you must begin a batch of write operations and afterwards end the batch. This is done using the RDK's standard BeginChange / EndChange system. The following is an example of how to access and change the document dithering settings:
```cpp
static class CDitheringExampleCommand : public CRhinoTestCommand
{
protected:
	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"DitheringExample"); }
	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
}
theDitheringExampleCommand;

using DM = IRhRdkDithering::Methods;

static const wchar_t* StringFromDitheringMethod(DM dm)
{
	switch (dm)
	{
	case DM::FloydSteinberg: return L"Floyd-Steinberg"; break;
	case DM::SimpleNoise:    return L"Simple noise"; break;
	}

	return L"None";
}

CRhinoCommand::result CDitheringExampleCommand::RunCommand(const CRhinoCommandContext& context)
{
	auto* pDoc = context.Document();
	if (nullptr == pDoc)
		return failure;

	const auto& dither = pDoc->Dithering();

	RhinoApp().Print(L"Dithering before: %s\n", StringFromDitheringMethod(dither.Method()));

	auto& write_dither = dither.BeginChange(RhRdkChangeContext::Program);
	write_dither.SetMethod(DM::FloydSteinberg);
	write_dither.EndChange();

	RhinoApp().Print(L"Dithering after: %s\n", StringFromDitheringMethod(dither.Method()));

	return success;
}
```

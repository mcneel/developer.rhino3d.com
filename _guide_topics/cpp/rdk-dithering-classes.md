---
title: RDK Dithering
description: This document describes how to use the RDK dithering classes in C/C++.
authors: ['john_croudy']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin', 'Dithering']
layout: toc-guide-page
---
### Introduction
_Dithering_ is a process which reduces color artifacts caused by a display device being unable to display the full range of colors in an image. This was very important back in the days before graphics cards supported 24-bit color. A picture would be dithered to simulate 24-bit color on, for example, an 8-bit display. The image below shows an extreme example. Each pictures uses only two colors. On the left, no dithering was used and a lot of detail has been lost. On the right, _floyd-steinberg_ dithering was used and the amount of detail is much improved. Today, dithering is not usually required, but there are cases where it can make a subtle difference to the final quality of an image.

![Dithering]({{ site.baseurl }}/images/rdk-dithering.png)

### The Document Dithering Settings
The _RDK Document Dithering settings_ is a document-resident dithering object which affects renderings. If you have a Rhino document, you can read and write that document's dithering settings through the document's [IRhRdkDithering]({{ site.baseurl }}/api/cpp/class_i_rh_rdk_dithering.html) interface. Any changes you make will appear in the Dithering and Color Adjustment section of the Rendering panel and will also be stored in the 3dm file. Getting the dithering settings from a document always returns a const reference. To write to the settings, you must begin a batch of write operations and afterwards end the batch. This is done using the RDK's standard BeginChange / EndChange system. The following is an example of how to access and change the document dithering settings:
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

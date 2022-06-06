+++
aliases = ["/5/guides/cpp/rdk-skylight-classes/", "/6/guides/cpp/rdk-skylight-classes/", "/7/guides/cpp/rdk-skylight-classes/", "/wip/guides/cpp/rdk-skylight-classes/"]
authors = [ "john.croudy" ]
categories = [ "RDK" ]
description = "This document describes how to use the RDK skylight class in C/C++."
keywords = [ "RDK", "Rhino", "Renderer", "Development", "Plugin", "Skylight" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "RDK Skylight"
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
The _skylight_ is a feature that allows a scene to be rendered realistically, as if the objects in the scene were in a real environment under a real sky. When the skylight is used, the objects in the scene are lit not only by the scene's lights (or the sun), but also by the environment. The image below shows a comparison of a scene rendered with the skylight disabled (left) and enabled (right). Notice the subtly different coloring and the softer more diffuse shadows in the sky-lit image. The disadvantage of the skylight is that it is very CPU-intensive and renderings are much slower when it is enabled.

![Road](/images/rdk-skylight.jpg)

### The Document Skylight
The _RDK Document Skylight_ is a document-resident skylight which affects viewports and renderings. If you have a Rhino document, you can read and write that document's skylight through the document's [IRhRdkSkylight](/api/cpp/class_i_rh_rdk_skylight.html) interface. Any changes you make will appear in the Lighting section of the Rendering panel and will also be stored in the 3dm file. Getting the skylight from a document always returns a const reference. To write to the skylight, you must begin a batch of write operations and afterwards end the batch. This is done using the RDK's standard BeginChange / EndChange system. The following is an example of how to access and change the document skylight:
```cpp
static class CSkylightExampleCommand : public CRhinoTestCommand
{
protected:
	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"MySkylightCmd"); }
	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
}
theSkylightExampleCommand;

CRhinoCommand::result CSkylightExampleCommand::RunCommand(const CRhinoCommandContext& context)
{
	auto* pDoc = context.Document();
	if (nullptr == pDoc)
		return failure;

	const auto& sl = pDoc->Skylight();

	RhinoApp().Print(L"Skylight before: %s\n", sl.On() ? L"on" : L"off");

	auto& write_sl = sl.BeginChange(RhRdkChangeContext::Program);
	write_sl.SetOn(false);
	write_sl.EndChange();

	RhinoApp().Print(L"Skylight after: %s\n", sl.On() ? L"on" : L"off");

	return success;
}
```

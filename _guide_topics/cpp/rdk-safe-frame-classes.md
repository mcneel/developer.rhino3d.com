---
title: RDK Safe Frame classes
description: This document describes how to use the RDK safe frame classes in C/C++.
authors: ['john_croudy']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin', 'Safe Frame']
layout: toc-guide-page
---
### Introduction
A _Safe Frame_ is a guide to help ensure that the most important elements of a scene will appear inside a certain region of the rendered image. The name comes from movie and TV production where a camera operator sees one or more rectangles in the camera's viewfinder which shows limits inside which an actor or prop is guaranteed to be visible on all viewer's screens.

![Road]({{ site.baseurl }}/images/rdk-safeframe.jpg)

### The Document Safe Frame
The _RDK Document Safe Frame_ is a document-resident safe frame  which can be displayed in viewports. If you have a Rhino document, you can read and write that document's safe frame through the document's [IRhRdkSafeFrame]({{ site.baseurl }}/api/cpp/class_i_rh_rdk_safeframe.html) interface. Any changes you make will appear in the Safe Frame UI and will also be stored in the 3dm file. Getting the safe frame from a document always returns a const reference. To write to the safe frame, you must begin a batch of write operations and afterwards end the batch. This is done using the RDK's standard BeginChange / EndChange system. The following is an example of how to access and change the document safe frame:
```cpp
static class CSafeFrameExampleCommand : public CRhinoTestCommand
{
protected:
	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"MySafeFrameCmd"); }
	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
}
theSafeFrameExampleCommand;

CRhinoCommand::result CSafeFrameExampleCommand::RunCommand(const CRhinoCommandContext& context)
{
	auto* pDoc = context.Document();
	if (nullptr == pDoc)
		return failure;

	const auto& sf = pDoc->SafeFrame();

	RhinoApp().Print(L"Safe frame before: %s\n", sf.On() ? L"on" : L"off");

	auto& write_sf = sf.BeginChange(RhRdkChangeContext::Program);
	write_sf.SetOn(false);
	write_sf.EndChange();

	RhinoApp().Print(L"Safe frame after: %s\n", sf.On() ? L"on" : L"off");

	return success;
}
```

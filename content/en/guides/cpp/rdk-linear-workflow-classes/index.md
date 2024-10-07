+++
aliases = ["/en/5/guides/cpp/rdk-linear-workflow-classes/", "/en/6/guides/cpp/rdk-linear-workflow-classes/", "/en/7/guides/cpp/rdk-linear-workflow-classes/", "/en/wip/guides/cpp/rdk-linear-workflow-classes/"]
authors = [ "john.croudy" ]
categories = [ "RDK" ]
description = "This document describes how to use the RDK linear workflow class in C/C++."
keywords = [ "RDK", "Rhino", "Renderer", "Development", "Plugin", "Linear Workflow" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "RDK Linear Workflow"
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
Many consumer digital cameras output JPEG files which use the sRGB color space. This color space incorporates gamma correction which makes it possible to directly display the images on a computer monitor without even knowing that gamma correction exists. This means that many available photographic textures have already been gamma-corrected. Working with these images can give unsatisfactory results when intermediate processing and rendering works in a linear fashion. This problem can be avoided by using a _Linear Workflow_. This means that the gamma correction is removed from the images before they are used for rendering, and reapplied afterwards for display.

### The Document Linear Workflow
The _RDK Document Linear Workflow_ is a document-resident linear workflow object which affects renderings and viewports. If you have a Rhino document, you can read and write that document's linear workflow settings through the document's [IRhRdkLinearWorkflow](/api/cpp/class_i_rh_rdk_linear_workflow.html) interface. Any changes you make will appear in the Rendering UI and will also be stored in the 3dm file. Getting the linear workflow from a document always returns a const reference. To write to the linear workflow, you must begin a batch of write operations and afterwards end the batch. This is done using the RDK's standard BeginChange / EndChange system. The following is an example of how to access and change the document linear workflow settings:
```cpp
static class CLinearWorkflowExampleCommand : public CRhinoTestCommand
{
protected:
	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"LinearWorkflowExample"); }
	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
}
theLinearWorkflowExampleCommand;

CRhinoCommand::result CLinearWorkflowExampleCommand::RunCommand(const CRhinoCommandContext& context)
{
	auto* pDoc = context.Document();
	if (nullptr == pDoc)
		return failure;

	const auto& lw = pDoc->LinearWorkflow();

	RhinoApp().Print(L"LW gamma before: %.1f\n", lw.PreProcessGamma());

	auto& write_lw = lw.BeginChange(RhRdkChangeContext::Program);
	write_lw.SetPreProcessGamma(3.5f);
	write_lw.EndChange();

	RhinoApp().Print(L"LW gamma after: %.1f\n", lw.PreProcessGamma());

	return success;
}
```

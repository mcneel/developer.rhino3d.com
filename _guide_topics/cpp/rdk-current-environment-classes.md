---
title: RDK Current Environment classes
description: This document describes how to use the RDK current environment classes in C/C++.
authors: ['john_croudy']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin', 'Current Environment']
layout: toc-guide-page
---
### Introduction
The _Current Environment_ is a document-resident environment which has been selected for use during rendering. There are currently three such environments which are identified by _usage_. These are:

* 360 backdrop environment. This is the environment that appears to surround the scene.
* Custom reflective environment. This is an environment that can be used to override the environment that appears in reflections. If this is not enabled, the backdrop environment is used.
* Custom skylight environment. This is an environment that can be used to override the environment used for skylighting. If this is not enabled, the backdrop environment is used.

When accessing these environments using the SDK, you sometimes need to specify the _purpose_ of the access. These purposes are:

* _Simple_. This is used to directly get and set the environment instance id.
* _Render_. This is used by renderers. It uses special logic which defers to other environments when one is not available.

![Environment]({{ site.baseurl }}/images/rdk-environment.jpg)
<small><small><small>Photo by John Croudy.</small></small></small>

### The Document Current Environment
The _RDK Document Current Environment_ is actually a set of _three_ document-resident current environments which affect renderings and the viewports. If you have a Rhino document, you can read and write that document's current environments through the document's [IRhRdkCurrentEnvironment]({{ site.baseurl }}/api/cpp/class_i_rh_rdk_current_environment.html) interface. Any changes you make will appear in the Rendering UI and will also be stored in the 3dm file. Getting a current environment from a document always returns a const reference. To write to the current environment, you must begin a batch of write operations and afterwards end the batch. This is done using the RDK's standard BeginChange / EndChange system. The following is an example of how to access and change the document's current 'custom reflective' environment:
```cpp
static class CCurrentEnvironmentExampleCommand : public CRhinoTestCommand
{
protected:
	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"MyCurrentEnvCmd"); }
	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
}
theCurrentEnvironmentExampleCommand;

CRhinoCommand::result CCurrentEnvironmentExampleCommand::RunCommand(const CRhinoCommandContext& context)
{
	auto* pDoc = context.Document();
	if (nullptr == pDoc)
		return failure;

	// We will test using the custom reflective environment.
	const auto usage = IRhRdkCurrentEnvironment::Usage::Reflection;
	const auto purpose = IRhRdkCurrentEnvironment::Purpose::Simple;

	const auto& ce = pDoc->CurrentEnvironment();

	ON_wString sUuid;
	auto uuid = ce.Get(usage, purpose);
	ON_UuidToString(uuid, sUuid);
	const auto* wszUuid = static_cast<const wchar_t*>(sUuid);
	RhinoApp().Print(L"Custom refl. env before: %s [%s]\n", ce.On(usage) ? L"on" : L"off", wszUuid);

	// Create a new basic environment.
	auto* pEnvironment = ::RhRdkNewBasicEnvironment(pDoc);
	if (nullptr != pEnvironment)
	{
		// Attach it to the document.
		auto& write_contents = pDoc->Contents().BeginChange(RhRdkChangeContext::Program);
		write_contents.Attach(*pEnvironment);
		write_contents.EndChange();

		// Turn on the environment and set it as the new basic environment.
		auto& write_ce = ce.BeginChange(RhRdkChangeContext::Program);
		write_ce.SetOn(usage, true);
		write_ce.Set(usage, pEnvironment->InstanceId());
		write_ce.EndChange();
	}

	uuid = ce.Get(usage, purpose);
	ON_UuidToString(uuid, sUuid);
	wszUuid = static_cast<const wchar_t*>(sUuid);
	RhinoApp().Print(L"Custom refl. env after:  %s [%s]\n", ce.On(usage) ? L"on" : L"off", wszUuid);

	return success;
}
```

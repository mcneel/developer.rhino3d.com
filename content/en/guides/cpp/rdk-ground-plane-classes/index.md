+++
aliases = ["/en/5/guides/cpp/rdk-ground-plane-classes/", "/en/6/guides/cpp/rdk-ground-plane-classes/", "/en/7/guides/cpp/rdk-ground-plane-classes/", "/wip/guides/cpp/rdk-ground-plane-classes/"]
authors = [ "john.croudy" ]
categories = [ "RDK" ]
description = "This document describes how to use the RDK ground plane class in C/C++."
keywords = [ "RDK", "Rhino", "Renderer", "Development", "Plugin", "Ground Plane" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "RDK Ground Plane"
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
When rendering real-world scenes, it is very often the case that the rendering will include a large area of ground or flooring. This could be modeled by using a plane, but this is inconvenient because the ground tends to stretch as far as the eye can see. To circumvent this problem, the RDK provides a set of _ground plane_ services to make it easier to add a ground or floor to your scene. A ground plane has an _altitude_, which is usually the same as its position along the z-axis. It can also have a material assigned to it, which will appear in renderings and in the viewport, much as materials assigned to objects do. If the _auto-altitude_ option is enabled, the ground plane will adjust itself to sit below the objects in the scene.

![Road](/images/rdk-ground-plane-road.jpg)
<small><small><small>Interstate 15, Nevada, USA ~ Photo by John Croudy.</small></small></small>

### The Document Ground Plane
The _RDK Document Ground Plane_ is a document-resident ground plane which affects viewports and renderings. If you have a Rhino document, you can read and write that document's ground plane through the document's [IRhRdkGroundPlane](/api/cpp/class_i_rh_rdk_ground_plane.html) interface. Any changes you make will appear in the main ground plane UI and will also be stored in the 3dm file. Getting the ground plane from a document always returns a const reference. To write to the ground plane, you must begin a batch of write operations and afterwards end the batch. This is done using the RDK's standard BeginChange / EndChange system. The following is an example of how to access and change the document ground plane:
```cpp
static class CGroundPlaneExampleCommand: public CRhinoTestCommand
{
protected:
	virtual UUID CommandUUID() override { static const UUID uuid = { your_uuid_here } }; return uuid; }
	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"MyGroundPlaneCmd"); }
	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
}
theGroundPlaneExampleCommand;

CRhinoCommand::result CGroundPlaneExampleCommand::RunCommand(const CRhinoCommandContext& context)
{
	auto* pDoc = context.Document();
	if (nullptr == pDoc)
		return failure;

	// Get the document ground plane.
	const auto& gp = pDoc->GroundPlane();

	RhinoApp().Print(L"Ground plane altitude before: %.1f\n", gp.Altitude());

	// Begin a change bracket on the ground plane.
	auto& write_gp = gp.BeginChange(RhRdkChangeContext::Program);

	// Set the ground plane's altitude manually.
	write_gp.SetAutoAltitude(false);
	write_gp.SetAltitude(10.0);

	// Create a new custom material.
	ON_Material mat;
	mat.SetDiffuse(ON_Color(185, 14, 14));
	auto* pMaterial = ::RhRdkNewBasicMaterial(mat, pDoc);
	if (nullptr != pMaterial)
	{
		auto& write_contents = pDoc->Contents().BeginChange(RhRdkChangeContext::Program);
		write_contents.Attach(*pMaterial);
		write_contents.EndChange();

		write_gp.SetOn(true);
		write_gp.SetShadowOnly(false);
		write_gp.SetMaterialInstanceId(pMaterial->InstanceId());
	}

	// End the ground plane change bracket.
	write_gp.EndChange();

	RhinoApp().Print(L"Ground plane altitude after: %.1f\n", gp.Altitude());

	return success;
}
```

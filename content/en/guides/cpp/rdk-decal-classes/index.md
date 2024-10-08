+++
aliases = ["/en/5/guides/cpp/rdk-decal-classes/", "/en/6/guides/cpp/rdk-decal-classes/", "/en/7/guides/cpp/rdk-decal-classes/", "/en/wip/guides/cpp/rdk-decal-classes/"]
authors = [ "john.croudy" ]
categories = [ "RDK" ]
description = "This document describes how to use the RDK decal classes in C/C++."
keywords = [ "RDK", "Rhino", "Renderer", "Development", "Plugin", "Decal" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "RDK Decals"
type = "guides"
weight = 1
override_last_modified = "2019-01-16T17:20:12Z"

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
### IRhRdkDecal
<a name="IRhRdkDecal"></a>
_IRhRdkDecal_ is an abstract decal interface. It provides access to all the properties of a Decal.

### CRhRdkObjectDataAccess
<a name="CRhRdkObjectDataAccess"></a>
_CRhRdkObjectDataAccess_ is a wrapper around an object or layer which makes it easy to get RDK-specific information from that object or layer. When the wrapped object is a Rhino object, it can be used for accessing the object's decals using the following methods:

* `AddDecal()` Adds a new decal to the object.
* `RemoveDecal()` Remove a particular decal from the object.
* `RemoveAllDecals()` Removes all decals from the object.
* `NewDecalIterator()` Obtains an iterator for accessing the object's decals.

A particularly important property of decals is the _decal CRC_. This value identifies a decal by its state. Multiple decals which would be exactly the same would have the same CRC and are culled from the system. If you store this value with the intention of using it to find the decal again later, you must update your stored value whenever the decal state changes.

The following is an example of how to access decals already on an object. It uses NewDecalIterator() to get IRhRdkDecal and lists decal information on every object in the document. To keep the example short it does not list _every_ piece of information available from IRhRdkDecal but should be enough to get you started:
```cpp
using OI = CRhinoObjectIterator;

int objCount = 1;

CRhinoObjectIterator it(*pDoc, OI::undeleted_objects, OI::active_and_reference_objects);
const auto* pObject = it.First();
while (nullptr != pObject)
{
	CRhRdkObjectDataAccess da(pObject);

	auto* pDI = da.NewDecalIterator();
	if (nullptr != pDI)
	{
		const auto* pDecal = pDI->NextDecal();
		while (nullptr != pDecal)
		{
			const auto m = pDecal->Mapping();

			const wchar_t* wszMapping = L"";
			switch (m)
			{
			case IRhRdkDecal::mapUV:          wszMapping = L"UV";          break;
			case IRhRdkDecal::mapPlanar:      wszMapping = L"Planar";      break;
			case IRhRdkDecal::mapCylindrical: wszMapping = L"Cylindrical"; break;
			case IRhRdkDecal::mapSpherical:   wszMapping = L"Spherical";   break;
			}

			const auto pt = pDecal->Origin();
			RhinoApp().Print(L"Object %u: Decal %08X, mapping: %s, origin: (%.1f, %.1f, %.1f)",
			                 objCount, pDecal->CRC(), wszMapping, pt.x, pt.y, pt.z);

			if ((IRhRdkDecal::mapSpherical == m) || (IRhRdkDecal::mapCylindrical == m))
			{
				RhinoApp().Print(L", Radius: %.1f", pDecal->Radius());

				if (IRhRdkDecal::mapCylindrical == m)
				{
					RhinoApp().Print(L", Height: %.1f", pDecal->Height());
				}
			}

			RhinoApp().Print(L"\n");

			pDecal = pDI->NextDecal();
		}

		delete pDI;
	}

	pObject = it.Next();

	objCount++;
}
```

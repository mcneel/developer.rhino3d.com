+++
aliases = ["/en/5/guides/cpp/getting-object-uuid/", "/en/6/guides/cpp/getting-object-uuid/", "/en/7/guides/cpp/getting-object-uuid/", "/wip/guides/cpp/getting-object-uuid/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates how to get an object's UUID using C/C++."
keywords = [ "rhino", "uuid", "guid" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Getting Object UUIDs"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/getuuid"
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

 
## Overview

Rhino can create and manipulate many geometric objects, including points, point clouds, curves, surfaces, Breps, extrusions, subds, meshes, lights, annotations and more.

A universally unique identifier, or [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier), is assigned to each object in the Rhino document when the objects are created. The object's UUID uniquely identifies the object.

Because UUIDs are saved in the 3DM file, an object's unique identifier will persist between editing sessions.

## Sample

The following code sample demonstrates how to obtain an object's unique identifier, or UUID, using C/C++:

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoGetObject go;
  go.SetCommandPrompt(L"Select object");
  go.GetObjects(1, 1);
  if (go.CommandResult() != CRhinoCommand::success)
    return go.CommandResult();

  const CRhinoObjRef& ref = go.Object(0);
  const CRhinoObject* obj = ref.Object();
  if (nullptr == obj)
    return CRhinoCommand::failure;

  ON_UUID uuid = obj->ModelObjectId();
  ON_wString str;
  ON_UuidToString(uuid, str);
  RhinoApp().Print(L"The object's unique identifier is \"%s\".\n", str);

  return CRhinoCommand::success;
}
```

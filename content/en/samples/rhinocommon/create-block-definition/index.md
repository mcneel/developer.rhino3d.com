+++
aliases = ["/en/5/samples/rhinocommon/create-block-definition/", "/en/6/samples/rhinocommon/create-block-definition/", "/en/7/samples/rhinocommon/create-block-definition/", "/en/wip/samples/rhinocommon/create-block-definition/"]
authors = [ "steve" ]
categories = [ "Adding Objects", "Blocks" ]
description = "Demonstrates how to create a block definition from scratch from user-specified objects, base-point, and name."
keywords = [ "add", "block", "definition" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Create Block Definition"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/createblock"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0
+++

<div class="codetab-content" id="cs">

```cs
partial class Examples
{
  public static Rhino.Commands.Result CreateBlock(Rhino.RhinoDoc doc)
  {
    // Select objects to define block
    var go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt( "Select objects to define block" );
    go.ReferenceObjectSelect = false;
    go.SubObjectSelect = false;
    go.GroupSelect = true;

    // Phantoms, grips, lights, etc., cannot be in blocks.
    const ObjectType forbidden_geometry_filter = Rhino.DocObjects.ObjectType.Light |
                                                 Rhino.DocObjects.ObjectType.Grip | Rhino.DocObjects.ObjectType.Phantom;
    const ObjectType geometry_filter = forbidden_geometry_filter ^ Rhino.DocObjects.ObjectType.AnyObject;
    go.GeometryFilter = geometry_filter;
    go.GetMultiple(1, 0);
    if (go.CommandResult() != Rhino.Commands.Result.Success)
      return go.CommandResult();

    // Block base point
    Rhino.Geometry.Point3d base_point;
    var rc = Rhino.Input.RhinoGet.GetPoint("Block base point", false, out base_point);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    // Block definition name
    string idef_name = "";
    rc = Rhino.Input.RhinoGet.GetString("Block definition name", false, ref idef_name);
    if (rc != Rhino.Commands.Result.Success)
      return rc;
    // Validate block name
    idef_name = idef_name.Trim();
    if (string.IsNullOrEmpty(idef_name))
      return Rhino.Commands.Result.Nothing;

    // See if block name already exists
    Rhino.DocObjects.InstanceDefinition existing_idef = doc.InstanceDefinitions.Find(idef_name);
    if (existing_idef != null)
    {
      Rhino.RhinoApp.WriteLine("Block definition {0} already exists", idef_name);
      return Rhino.Commands.Result.Nothing;
    }

    // Gather all of the selected objects
    var geometry = new System.Collections.Generic.List<Rhino.Geometry.GeometryBase>();
    var attributes = new System.Collections.Generic.List<Rhino.DocObjects.ObjectAttributes>();
    for (int i = 0; i < go.ObjectCount; i++)
    {
      var rhinoObject = go.Object(i).Object();
      if (rhinoObject != null)
      {
        geometry.Add(rhinoObject.Geometry);
        attributes.Add(rhinoObject.Attributes);
      }
    }

    // Gather all of the selected objects
    int idef_index = doc.InstanceDefinitions.Add(idef_name, string.Empty, base_point, geometry, attributes);

    if( idef_index < 0 )
    {
      Rhino.RhinoApp.WriteLine("Unable to create block definition", idef_name);
      return Rhino.Commands.Result.Failure;
    }
    return Rhino.Commands.Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def CreateBlock():
    # Select objects to define block
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt( "Select objects to define block" )
    go.ReferenceObjectSelect = False
    go.SubObjectSelect = False
    go.GroupSelect = True

    # Phantoms, grips, lights, etc., cannot be in blocks.
    forbidden_geometry_filter = Rhino.DocObjects.ObjectType.Light | Rhino.DocObjects.ObjectType.Grip | Rhino.DocObjects.ObjectType.Phantom
    geometry_filter = forbidden_geometry_filter ^ Rhino.DocObjects.ObjectType.AnyObject
    go.GeometryFilter = geometry_filter
    go.GetMultiple(1, 0)
    if go.CommandResult() != Rhino.Commands.Result.Success:
        return go.CommandResult()

    # Block base point
    rc, base_point = Rhino.Input.RhinoGet.GetPoint("Block base point", False)
    if rc != Rhino.Commands.Result.Success: return rc

    # Block definition name
    rc, idef_name = Rhino.Input.RhinoGet.GetString("Block definition name", False, "")
    if rc != Rhino.Commands.Result.Success: return rc
    # Validate block name
    idef_name = idef_name.strip()
    if not idef_name: return Rhino.Commands.Result.Nothing

    # See if block name already exists
    existing_idef = scriptcontext.doc.InstanceDefinitions.Find(idef_name, True)
    if existing_idef:
        print("Block definition", idef_name, "already exists")
        return Rhino.Commands.Result.Nothing

    # Gather all of the selected objects
    objrefs = go.Objects()
    geometry = [item.Object().Geometry for item in objrefs]
    attributes = [item.Object().Attributes for item in objrefs]

    # Add the instance definition
    idef_index = scriptcontext.doc.InstanceDefinitions.Add(idef_name, "", base_point, geometry, attributes)

    if idef_index<0:
        print("Unable to create block definition", idef_name)
        return Rhino.Commands.Result.Failure
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    CreateBlock()
```

</div>

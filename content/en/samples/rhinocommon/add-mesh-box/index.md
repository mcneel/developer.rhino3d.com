+++
aliases = ["/en/5/samples/rhinocommon/add-mesh-box/", "/en/6/samples/rhinocommon/add-mesh-box/", "/en/7/samples/rhinocommon/add-mesh-box/", "/en/wip/samples/rhinocommon/add-mesh-box/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to construct a mesh box from a Brep box."
keywords = [ "add", "mesh" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Add Mesh Box"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
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
  public static Rhino.Commands.Result AddMeshBox(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Box box;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetBox(out box);
    if (rc == Rhino.Commands.Result.Success)
    {
      Rhino.Geometry.Mesh mesh = Rhino.Geometry.Mesh.CreateFromBox(box, 2, 2, 2);
      if (null != mesh)
      {
        doc.Objects.AddMesh(mesh);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }

    return Rhino.Commands.Result.Failure;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>

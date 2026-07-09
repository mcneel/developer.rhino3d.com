+++
aliases = ["/en/5/samples/rhinocommon/extract-render-mesh/", "/en/6/samples/rhinocommon/extract-render-mesh/", "/en/7/samples/rhinocommon/extract-render-mesh/", "/en/wip/samples/rhinocommon/extract-render-mesh/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to extract the render mesh from a surface or polysurface."
keywords = [ "extract", "render", "mesh" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Extract Render Mesh"
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
  public static Rhino.Commands.Result ExtractRenderMesh(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objRef = null;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", false, Rhino.DocObjects.ObjectType.Brep, out objRef);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    Rhino.DocObjects.RhinoObject obj = objRef.Object();
    if (null == obj)
      return Rhino.Commands.Result.Failure;

    System.Collections.Generic.List<Rhino.DocObjects.RhinoObject> objList = new System.Collections.Generic.List<Rhino.DocObjects.RhinoObject>(1);
    objList.Add(obj);

    Rhino.DocObjects.ObjRef[] meshObjRefs = Rhino.DocObjects.RhinoObject.GetRenderMeshes(objList, true, false);
    if (null != meshObjRefs)
    {
      for (int i = 0; i < meshObjRefs.Length; i++)
      {
        Rhino.DocObjects.ObjRef meshObjRef = meshObjRefs[i];
        if (null != meshObjRef)
        {
          Rhino.Geometry.Mesh mesh = meshObjRef.Mesh();
          if (null != mesh)
            doc.Objects.AddMesh(mesh);
        }
      }
      doc.Views.Redraw();
    }

    return Rhino.Commands.Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import System
import scriptcontext as sc

def RunCommand():
    rc, objRef = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", False, Rhino.DocObjects.ObjectType.Brep)
    if rc != Rhino.Commands.Result.Success:
        return rc

    obj = objRef.Object()
    if obj is None:
        return Rhino.Commands.Result.Failure

    objList = System.Collections.Generic.List[Rhino.DocObjects.RhinoObject](1)
    objList.Add(obj)

    meshObjRefs = Rhino.DocObjects.RhinoObject.GetRenderMeshes(objList, True, False)
    if meshObjRefs is not None:
        for i in range(meshObjRefs.Length):
            meshObjRef = meshObjRefs[i]
            if meshObjRef is not None:
                mesh = meshObjRef.Mesh()
                if mesh is not None:
                    sc.doc.Objects.AddMesh(mesh)
        sc.doc.Views.Redraw()

    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>

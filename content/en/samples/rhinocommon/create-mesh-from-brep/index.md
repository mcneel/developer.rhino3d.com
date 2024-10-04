+++
aliases = ["/en/5/samples/rhinocommon/create-mesh-from-brep/", "/en/6/samples/rhinocommon/create-mesh-from-brep/", "/en/7/samples/rhinocommon/create-mesh-from-brep/", "/wip/samples/rhinocommon/create-mesh-from-brep/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to create a mesh from a selected surface or polysurface."
keywords = [ "create", "meshes", "brep" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Create Mesh from Brep"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/createmeshfrombrep"
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
  public static Result CreateMeshFromBrep(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select surface or polysurface to mesh", true, ObjectType.Surface | ObjectType.PolysrfFilter, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var brep = obj_ref.Brep();
    if (null == brep)
      return Result.Failure;

    // you could choose anyone of these for example
    var jagged_and_faster = MeshingParameters.Coarse;
    var smooth_and_slower = MeshingParameters.Smooth;
    var default_mesh_params = MeshingParameters.Default;
    var minimal = MeshingParameters.Minimal;

    var meshes = Mesh.CreateFromBrep(brep, smooth_and_slower);
    if (meshes == null || meshes.Length == 0)
      return Result.Failure;

    var brep_mesh = new Mesh();
    foreach (var mesh in meshes)
      brep_mesh.Append(mesh);
    doc.Objects.AddMesh(brep_mesh);
    doc.Views.Redraw();

    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function CreateMeshFromBrep(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select surface or polysurface to mesh", True, ObjectType.Surface Or ObjectType.PolysrfFilter, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim brep = obj_ref.Brep()
	If Nothing Is brep Then
	  Return Result.Failure
	End If

	' you could choose anyone of these for example
	Dim jagged_and_faster = MeshingParameters.Coarse
	Dim smooth_and_slower = MeshingParameters.Smooth
	Dim default_mesh_params = MeshingParameters.Default
	Dim minimal = MeshingParameters.Minimal

	Dim meshes = Mesh.CreateFromBrep(brep, smooth_and_slower)
	If meshes Is Nothing OrElse meshes.Length = 0 Then
	  Return Result.Failure
	End If

	Dim brep_mesh = New Mesh()
	For Each mesh In meshes
	  brep_mesh.Append(mesh)
	Next mesh
	doc.Objects.AddMesh(brep_mesh)
	doc.Views.Redraw()

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
from Rhino.Geometry import *
from Rhino.Input import RhinoGet
from Rhino.Commands import Result
from Rhino.DocObjects import ObjectType
import rhinoscriptsyntax as rs
from scriptcontext import doc

def RunCommand():
    rc, objRef = RhinoGet.GetOneObject("Select surface or polysurface to mesh", True, ObjectType.Surface | ObjectType.PolysrfFilter)
    if rc != Result.Success:
        return rc
    brep = objRef.Brep()
    if None == brep:
        return Result.Failure

    jaggedAndFaster = MeshingParameters.Coarse
    smoothAndSlower = MeshingParameters.Smooth
    defaultMeshParams = MeshingParameters.Default
    minimal = MeshingParameters.Minimal

    meshes = Mesh.CreateFromBrep(brep, smoothAndSlower)
    if meshes == None or meshes.Length == 0:
        return Result.Failure

    brepMesh = Mesh()
    for mesh in meshes:
        brepMesh.Append(mesh)
    doc.Objects.AddMesh(brepMesh)
    doc.Views.Redraw()

if __name__ == "__main__":
    RunCommand()
```

</div>

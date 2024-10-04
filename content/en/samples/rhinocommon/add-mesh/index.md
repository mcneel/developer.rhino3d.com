+++
aliases = ["/en/5/samples/rhinocommon/add-mesh/", "/en/6/samples/rhinocommon/add-mesh/", "/en/7/samples/rhinocommon/add-mesh/", "/wip/samples/rhinocommon/add-mesh/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to construct a mesh from a list of vertices and faces."
keywords = [ "add", "mesh" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Mesh"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addmesh"
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
  public static Rhino.Commands.Result AddMesh(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Mesh mesh = new Rhino.Geometry.Mesh();
    mesh.Vertices.Add(0.0, 0.0, 1.0); //0
    mesh.Vertices.Add(1.0, 0.0, 1.0); //1
    mesh.Vertices.Add(2.0, 0.0, 1.0); //2
    mesh.Vertices.Add(3.0, 0.0, 0.0); //3
    mesh.Vertices.Add(0.0, 1.0, 1.0); //4
    mesh.Vertices.Add(1.0, 1.0, 2.0); //5
    mesh.Vertices.Add(2.0, 1.0, 1.0); //6
    mesh.Vertices.Add(3.0, 1.0, 0.0); //7
    mesh.Vertices.Add(0.0, 2.0, 1.0); //8
    mesh.Vertices.Add(1.0, 2.0, 1.0); //9
    mesh.Vertices.Add(2.0, 2.0, 1.0); //10
    mesh.Vertices.Add(3.0, 2.0, 1.0); //11

    mesh.Faces.AddFace(0, 1, 5, 4);
    mesh.Faces.AddFace(1, 2, 6, 5);
    mesh.Faces.AddFace(2, 3, 7, 6);
    mesh.Faces.AddFace(4, 5, 9, 8);
    mesh.Faces.AddFace(5, 6, 10, 9);
    mesh.Faces.AddFace(6, 7, 11, 10);
    mesh.Normals.ComputeNormals();
    mesh.Compact();
    if (doc.Objects.AddMesh(mesh) != Guid.Empty)
    {
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
    return Rhino.Commands.Result.Failure;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddMesh(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim mesh As New Rhino.Geometry.Mesh()
	mesh.Vertices.Add(0.0, 0.0, 1.0) '0
	mesh.Vertices.Add(1.0, 0.0, 1.0) '1
	mesh.Vertices.Add(2.0, 0.0, 1.0) '2
	mesh.Vertices.Add(3.0, 0.0, 0.0) '3
	mesh.Vertices.Add(0.0, 1.0, 1.0) '4
	mesh.Vertices.Add(1.0, 1.0, 2.0) '5
	mesh.Vertices.Add(2.0, 1.0, 1.0) '6
	mesh.Vertices.Add(3.0, 1.0, 0.0) '7
	mesh.Vertices.Add(0.0, 2.0, 1.0) '8
	mesh.Vertices.Add(1.0, 2.0, 1.0) '9
	mesh.Vertices.Add(2.0, 2.0, 1.0) '10
	mesh.Vertices.Add(3.0, 2.0, 1.0) '11

	mesh.Faces.AddFace(0, 1, 5, 4)
	mesh.Faces.AddFace(1, 2, 6, 5)
	mesh.Faces.AddFace(2, 3, 7, 6)
	mesh.Faces.AddFace(4, 5, 9, 8)
	mesh.Faces.AddFace(5, 6, 10, 9)
	mesh.Faces.AddFace(6, 7, 11, 10)
	mesh.Normals.ComputeNormals()
	mesh.Compact()
	If doc.Objects.AddMesh(mesh) <> Guid.Empty Then
	  doc.Views.Redraw()
	  Return Rhino.Commands.Result.Success
	End If
	Return Rhino.Commands.Result.Failure
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Guid

def AddMesh():
    mesh = Rhino.Geometry.Mesh()
    mesh.Vertices.Add(0.0, 0.0, 1.0) #0
    mesh.Vertices.Add(1.0, 0.0, 1.0) #1
    mesh.Vertices.Add(2.0, 0.0, 1.0) #2
    mesh.Vertices.Add(3.0, 0.0, 0.0) #3
    mesh.Vertices.Add(0.0, 1.0, 1.0) #4
    mesh.Vertices.Add(1.0, 1.0, 2.0) #5
    mesh.Vertices.Add(2.0, 1.0, 1.0) #6
    mesh.Vertices.Add(3.0, 1.0, 0.0) #7
    mesh.Vertices.Add(0.0, 2.0, 1.0) #8
    mesh.Vertices.Add(1.0, 2.0, 1.0) #9
    mesh.Vertices.Add(2.0, 2.0, 1.0) #10
    mesh.Vertices.Add(3.0, 2.0, 1.0) #11

    mesh.Faces.AddFace(0, 1, 5, 4)
    mesh.Faces.AddFace(1, 2, 6, 5)
    mesh.Faces.AddFace(2, 3, 7, 6)
    mesh.Faces.AddFace(4, 5, 9, 8)
    mesh.Faces.AddFace(5, 6, 10, 9)
    mesh.Faces.AddFace(6, 7, 11, 10)
    mesh.Normals.ComputeNormals()
    mesh.Compact()
    if scriptcontext.doc.Objects.AddMesh(mesh)!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure


if __name__=="__main__":
    AddMesh()
```

</div>

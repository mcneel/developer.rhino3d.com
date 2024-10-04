+++
aliases = ["/en/5/samples/rhinocommon/unroll-surface-and-mesh/", "/en/6/samples/rhinocommon/unroll-surface-and-mesh/", "/en/7/samples/rhinocommon/unroll-surface-and-mesh/", "/wip/samples/rhinocommon/unroll-surface-and-mesh/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Unroll developable surface and associated mesh"
keywords = [ "unroll", "developable", "surface", "associated", "mesh" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Unroll Surface and Mesh"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/unrollsurface2"
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
  public static Rhino.Commands.Result UnrollSurface2(Rhino.RhinoDoc doc)
  {
    const ObjectType filter = Rhino.DocObjects.ObjectType.Brep | Rhino.DocObjects.ObjectType.Surface;
    Rhino.DocObjects.ObjRef objref;
    Result rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", false, filter, out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;
    Rhino.Geometry.Unroller unroll=null;
    Rhino.Geometry.Brep brep = objref.Brep();
    Rhino.Geometry.Mesh mesh=null;
    if (brep != null)
    {
      unroll = new Rhino.Geometry.Unroller(brep);
      mesh = brep.Faces[0].GetMesh(Rhino.Geometry.MeshType.Render);
    }
    else
    {
      Rhino.Geometry.Surface srf = objref.Surface();
      if (srf != null)
      {
        unroll = new Rhino.Geometry.Unroller(srf);
      }
    }
    if (unroll == null || mesh==null)
      return Rhino.Commands.Result.Cancel;

    unroll.AddFollowingGeometry(mesh.Vertices.ToPoint3dArray());

    unroll.ExplodeOutput = false;
    Rhino.Geometry.Curve[] curves;
    Rhino.Geometry.Point3d[] points;
    Rhino.Geometry.TextDot[] dots;
    unroll.PerformUnroll(out curves, out points, out dots);

    // change the mesh vertices to the flattened form and add it to the document
    if( points.Length == mesh.Vertices.Count )
    {
      for( int i=0; i<points.Length; i++ )
        mesh.Vertices.SetVertex(i, points[i]);
      mesh.Normals.ComputeNormals();
    }
    doc.Objects.AddMesh(mesh, objref.Object().Attributes);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function UnrollSurface2(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Brep Or Rhino.DocObjects.ObjectType.Surface
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Result = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", False, filter, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If
	Dim unroll As Rhino.Geometry.Unroller=Nothing
	Dim brep As Rhino.Geometry.Brep = objref.Brep()
	Dim mesh As Rhino.Geometry.Mesh=Nothing
	If brep IsNot Nothing Then
	  unroll = New Rhino.Geometry.Unroller(brep)
	  mesh = brep.Faces(0).GetMesh(Rhino.Geometry.MeshType.Render)
	Else
	  Dim srf As Rhino.Geometry.Surface = objref.Surface()
	  If srf IsNot Nothing Then
		unroll = New Rhino.Geometry.Unroller(srf)
	  End If
	End If
	If unroll Is Nothing OrElse mesh Is Nothing Then
	  Return Rhino.Commands.Result.Cancel
	End If

	unroll.AddFollowingGeometry(mesh.Vertices.ToPoint3dArray())

	unroll.ExplodeOutput = False
	Dim curves() As Rhino.Geometry.Curve = Nothing
	Dim points() As Rhino.Geometry.Point3d = Nothing
	Dim dots() As Rhino.Geometry.TextDot = Nothing
	unroll.PerformUnroll(curves, points, dots)

	' change the mesh vertices to the flattened form and add it to the document
	If points.Length = mesh.Vertices.Count Then
	  For i As Integer = 0 To points.Length - 1
		mesh.Vertices.SetVertex(i, points(i))
	  Next i
	  mesh.Normals.ComputeNormals()
	End If
	doc.Objects.AddMesh(mesh, objref.Object().Attributes)
	doc.Views.Redraw()
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def UnrollSurface2():
    filter = Rhino.DocObjects.ObjectType.Brep | Rhino.DocObjects.ObjectType.Surface
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", False, filter)
    if rc!=Rhino.Commands.Result.Success: return rc;

    unroll = Rhino.Geometry.Unroller(objref.Geometry())
    mesh = objref.Brep().Faces[0].GetMesh(0)
    if not mesh: return Rhino.Commands.Result.Cancel

    unroll.AddFollowingGeometry(mesh.Vertices.ToPoint3dArray())
    unroll.ExplodeOutput = False
    breps, curves, points, dots = unroll.PerformUnroll()
    # change the mesh vertices to the flattened form and add it to the document
    if points.Length==mesh.Vertices.Count:
        for i, point in enumerate(points): mesh.Vertices.SetVertex(i, point)
        mesh.Normals.ComputeNormals()
    scriptcontext.doc.Objects.AddMesh(mesh, objref.Object().Attributes)
    scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    UnrollSurface2()
```

</div>

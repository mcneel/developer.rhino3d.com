+++
authors = [ "steve" ]
categories = [ "Draw" ]
description = "Demonstrates how to create a mesh from an existing surface and draw it in a display conduit."
keywords = [ "draw", "mesh" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Draw Mesh"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/meshdrawing"
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
  public static Result DrawMesh(RhinoDoc doc)
  {
    var gs = new GetObject();
    gs.SetCommandPrompt("select sphere");
    gs.GeometryFilter = ObjectType.Surface;
    gs.DisablePreSelect();
    gs.SubObjectSelect = false;
    gs.Get();
    if (gs.CommandResult() != Result.Success)
      return gs.CommandResult();

    Sphere sphere;
    gs.Object(0).Surface().TryGetSphere(out sphere);
    if (sphere.IsValid)
    {
      var mesh = Mesh.CreateFromSphere(sphere, 10, 10);
      if (mesh == null)
        return Result.Failure;

      var conduit = new DrawBlueMeshConduit(mesh) {Enabled = true};
      doc.Views.Redraw();

      var in_str = "";
      Rhino.Input.RhinoGet.GetString("press <Enter> to continue", true, ref in_str);

      conduit.Enabled = false;
      doc.Views.Redraw();
      return Result.Success;
    }
    else
      return Result.Failure;
  }
}

class DrawBlueMeshConduit : DisplayConduit
{
  readonly Mesh m_mesh;
  readonly Color m_color;
  readonly DisplayMaterial m_material;
  readonly BoundingBox m_bbox;

  public DrawBlueMeshConduit(Mesh mesh)
  {
    // set up as much data as possible so we do the minimum amount of work possible inside
    // the actual display code
    m_mesh = mesh;
    m_color = System.Drawing.Color.Blue;
    m_material = new DisplayMaterial();
    m_material.Diffuse = m_color;
    if (m_mesh != null && m_mesh.IsValid)
      m_bbox = m_mesh.GetBoundingBox(true);
  }

  // this is called every frame inside the drawing code so try to do as little as possible
  // in order to not degrade display speed. Don't create new objects if you don't have to as this
  // will incur an overhead on the heap and garbage collection.
  protected override void CalculateBoundingBox(CalculateBoundingBoxEventArgs e)
  {
    base.CalculateBoundingBox(e);
    // Since we are dynamically drawing geometry, we needed to override
    // CalculateBoundingBox. Otherwise, there is a good chance that our
    // dynamically drawing geometry would get clipped.

    // Union the mesh's bbox with the scene's bounding box
    e.BoundingBox.Union(m_bbox);
  }

  protected override void PreDrawObjects(DrawEventArgs e)
  {
    base.PreDrawObjects(e);
    var vp = e.Display.Viewport;
    if (vp.DisplayMode.EnglishName.ToLower() == "wireframe")
      e.Display.DrawMeshWires(m_mesh, m_color);
    else
      e.Display.DrawMeshShaded(m_mesh, m_material);
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function DrawMesh(ByVal doc As RhinoDoc) As Result
	Dim gs = New GetObject()
	gs.SetCommandPrompt("select sphere")
	gs.GeometryFilter = ObjectType.Surface
	gs.DisablePreSelect()
	gs.SubObjectSelect = False
	gs.Get()
	If gs.CommandResult() <> Result.Success Then
	  Return gs.CommandResult()
	End If

	Dim sphere As Sphere = Nothing
	gs.Object(0).Surface().TryGetSphere(sphere)
	If sphere.IsValid Then
	  Dim mesh = Mesh.CreateFromSphere(sphere, 10, 10)
	  If mesh Is Nothing Then
		Return Result.Failure
	  End If

	  Dim conduit = New DrawBlueMeshConduit(mesh) With {.Enabled = True}
	  doc.Views.Redraw()

	  Dim in_str = ""
	  Rhino.Input.RhinoGet.GetString("press <Enter> to continue", True, in_str)

	  conduit.Enabled = False
	  doc.Views.Redraw()
	  Return Result.Success
	Else
	  Return Result.Failure
	End If
  End Function
End Class

Friend Class DrawBlueMeshConduit
	Inherits DisplayConduit

  Private ReadOnly m_mesh As Mesh
  Private ReadOnly m_color As Color
  Private ReadOnly m_material As DisplayMaterial
  Private ReadOnly m_bbox As BoundingBox

  Public Sub New(ByVal mesh As Mesh)
	' set up as much data as possible so we do the minimum amount of work possible inside
	' the actual display code
	m_mesh = mesh
	m_color = System.Drawing.Color.Blue
	m_material = New DisplayMaterial()
	m_material.Diffuse = m_color
	If m_mesh IsNot Nothing AndAlso m_mesh.IsValid Then
	  m_bbox = m_mesh.GetBoundingBox(True)
	End If
  End Sub

  ' this is called every frame inside the drawing code so try to do as little as possible
  ' in order to not degrade display speed. Don't create new objects if you don't have to as this
  ' will incur an overhead on the heap and garbage collection.
  Protected Overrides Sub CalculateBoundingBox(ByVal e As CalculateBoundingBoxEventArgs)
	MyBase.CalculateBoundingBox(e)
	' Since we are dynamically drawing geometry, we needed to override
	' CalculateBoundingBox. Otherwise, there is a good chance that our
	' dynamically drawing geometry would get clipped.

	' Union the mesh's bbox with the scene's bounding box
	e.BoundingBox.Union(m_bbox)
  End Sub

  Protected Overrides Sub PreDrawObjects(ByVal e As DrawEventArgs)
	MyBase.PreDrawObjects(e)
	Dim vp = e.Display.Viewport
	If vp.DisplayMode.EnglishName.ToLower() = "wireframe" Then
	  e.Display.DrawMeshWires(m_mesh, m_color)
	Else
	  e.Display.DrawMeshShaded(m_mesh, m_material)
	End If
  End Sub
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs
from scriptcontext import doc
import Rhino
import System
import System.Drawing

def RunCommand():
    gs = Rhino.Input.Custom.GetObject()
    gs.SetCommandPrompt("select sphere")
    gs.GeometryFilter = Rhino.DocObjects.ObjectType.Surface
    gs.DisablePreSelect()
    gs.SubObjectSelect = False
    gs.Get()
    if gs.CommandResult() != Rhino.Commands.Result.Success:
        return gs.CommandResult()

    b, sphere = gs.Object(0).Surface().TryGetSphere()
    if sphere.IsValid:
        mesh = Rhino.Geometry.Mesh.CreateFromSphere(sphere, 10, 10)
        if mesh == None:
            return Rhino.Commands.Result.Failure

        conduit = DrawBlueMeshConduit(mesh)
        conduit.Enabled = True
        doc.Views.Redraw()

        inStr = rs.GetString("press <Enter> to continue")

        conduit.Enabled = False
        doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    else:
        return Rhino.Commands.Result.Failure

class DrawBlueMeshConduit(Rhino.Display.DisplayConduit):
    def __init__(self, mesh):
        self.mesh = mesh
        self.color = System.Drawing.Color.Blue
        self.material = Rhino.Display.DisplayMaterial()
        self.material.Diffuse = self.color
        if mesh != None and mesh.IsValid:
            self.bbox = mesh.GetBoundingBox(True)

    def CalculateBoundingBox(self, calculateBoundingBoxEventArgs):
        #super.CalculateBoundingBox(calculateBoundingBoxEventArgs)
        calculateBoundingBoxEventArgs.BoundingBox.Union(self.bbox)

    def PreDrawObjects(self, drawEventArgs):
        #base.PreDrawObjects(rawEventArgs)
        gvp = drawEventArgs.Display.Viewport
        if gvp.DisplayMode.EnglishName.ToLower() == "wireframe":
            drawEventArgs.Display.DrawMeshWires(self.mesh, self.color)
        else:
            drawEventArgs.Display.DrawMeshShaded(self.mesh, self.material)

if __name__ == "__main__":
    RunCommand()
```

</div>

---
layout: code-sample
title: Mesh Drawing
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['mesh', 'drawing']
order: 110
description:  
---



```cs
public class MeshDrawingCommand : Command
{
  public override string EnglishName { get { return "csDrawMesh"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class MeshDrawingCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbDrawMesh"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim gs = New GetObject()
    gs.SetCommandPrompt("select sphere")
    gs.GeometryFilter = ObjectType.Surface
    gs.DisablePreSelect()
    gs.SubObjectSelect = False
    gs.[Get]()
    If gs.CommandResult() <> Result.Success Then
      Return gs.CommandResult()
    End If

    Dim sphere As Sphere
    gs.[Object](0).Surface().TryGetSphere(sphere)
    If sphere.IsValid Then
      Dim mesh__1 = Mesh.CreateFromSphere(sphere, 10, 10)
      If mesh__1 Is Nothing Then
        Return Result.Failure
      End If
      Dim conduit = New DrawBlueMeshConduit(mesh__1)
      conduit.Enabled = True

      doc.Views.Redraw()

      Dim inStr As String = ""
      Rhino.Input.RhinoGet.GetString("press <Enter> to continue", True, inStr)

      conduit.Enabled = False
      doc.Views.Redraw()
      Return Result.Success
    Else
      Return Result.Failure
    End If
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


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
{: #py .tab-pane .fade .in}



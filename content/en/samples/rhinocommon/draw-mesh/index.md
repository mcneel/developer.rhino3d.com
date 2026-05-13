+++
aliases = ["/en/5/samples/rhinocommon/draw-mesh/", "/en/6/samples/rhinocommon/draw-mesh/", "/en/7/samples/rhinocommon/draw-mesh/", "/en/wip/samples/rhinocommon/draw-mesh/"]
authors = [ "steve" ]
categories = [ "Draw" ]
description = "Demonstrates how to create a mesh from an existing surface and draw it in a display conduit."
keywords = [ "draw", "mesh" ]
languages = [ "C#", "Python" ]
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

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import System
import scriptcontext as sc
 
def RunCommand():
    gs = Rhino.Input.Custom.GetObject()
    gs.SetCommandPrompt("Select sphere")
    gs.GeometryFilter = Rhino.DocObjects.ObjectType.Surface
    gs.SubObjectSelect = False
    gs.Get()
    if gs.CommandResult() != Rhino.Commands.Result.Success:
        return gs.CommandResult()
 
    rc, sphere = gs.Object(0).Surface().TryGetSphere()
    if not rc or not sphere.IsValid:
        return Rhino.Commands.Result.Cancel

    mesh = Rhino.Geometry.Mesh.CreateFromSphere(sphere, 10, 10)
    if not mesh:
        return Rhino.Commands.Result.Failure

    conduit = DrawBlueMeshConduit(mesh)
    conduit.Enabled = True
    sc.doc.Views.Redraw()

    out_str = ""
    rc = Rhino.Input.RhinoGet.GetString("Press <Enter> to continue", True, out_str);

    conduit.Enabled = False
    sc.doc.Views.Redraw()
    
    return Rhino.Commands.Result.Success
 
class DrawBlueMeshConduit(Rhino.Display.DisplayConduit):
    def __init__(self, mesh):
        super().__init__()
        self.mesh = mesh
        self.color = System.Drawing.Color.Blue
        self.material = Rhino.Display.DisplayMaterial()
        self.material.Diffuse = self.color
        if mesh != None and mesh.IsValid:
            self.bbox = mesh.GetBoundingBox(True)
 
    def CalculateBoundingBox(self, args):
        args.BoundingBox.Union(self.bbox)
 
    def PreDrawObjects(self, drawEventArgs):
        gvp = drawEventArgs.Display.Viewport
        if gvp.DisplayMode.Id != Rhino.Display.DisplayModeDescription.WireframeId:
            drawEventArgs.Display.DrawMeshShaded(self.mesh, self.material)
        drawEventArgs.Display.DrawMeshWires(self.mesh, self.color)
 
if __name__ == "__main__":
    RunCommand()
```

</div>

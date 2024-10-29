+++
aliases = ["/en/5/samples/rhinocommon/add-material/", "/en/6/samples/rhinocommon/add-material/", "/en/7/samples/rhinocommon/add-material/", "/en/wip/samples/rhinocommon/add-material/"]
authors = [ "steve", "andy", "john.croudy" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add a material to the document and apply it to a sphere object."
keywords = [ "add", "basic", "material" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Material"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addmaterial"
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
  public static Rhino.Commands.Result AddMaterial(Rhino.RhinoDoc doc)
  {
    // Create a Rhino material with a texture.
    var rhino_material = new Material
    {
      Name = "Chocolate",
      DiffuseColor = System.Drawing.Color.Chocolate,
      SpecularColor = System.Drawing.Color.CadetBlue
    };

    var texture = new Texture
    {
      FileName = "my_image.jpg"
    };
    rhino_material.SetTexture(texture, TextureType.Bitmap);

    // Use the Rhino material to create a Render material.
    var render_material = RenderMaterial.CreateBasicMaterial(rhino_material, doc);
    doc.RenderMaterials.Add(render_material);

    // Create a sphere.
    var sphere = new Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 5);

    // Add the sphere to the document.
    var id = doc.Objects.AddSphere(sphere);
    var obj = doc.Objects.FindId(id);
    if (obj != null)
    {
      // Assign the render material to the sphere object.
      obj.RenderMaterial = render_material;
      obj.CommitChanges();
    }

    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddMaterial(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result

    Dim index As Integer = doc.Materials.Add()
    Dim mat As Rhino.DocObjects.Material = New Rhino.DocObjects.Material
    mat.DiffuseColor = System.Drawing.Color.Chocolate
    mat.SpecularColor = System.Drawing.Color.CadetBlue

    Dim texture As Rhino.DocObjects.Texture = New Rhino.DocObjects.Texture()
    texture.FileName = "my_image.jpg"
    mat.SetTexture(texture, TextureType.Bitmap)

    Dim rm As Rhino.Render.RenderMaterial = Rhino.Render.RenderMaterial.CreateBasicMaterial(mat, doc)
    doc.RenderMaterials.Add(rm)

    Dim sp As New Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 5)
    Dim id As Guid = doc.Objects.AddSphere(sp)
    Dim rhinoObject As RhinoObject = doc.Objects.Find(id)
    rhinoObject.RenderMaterial = rm
    rhinoObject.CommitChanges()

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
import System.Drawing

def AddMaterial():

    # Create a Rhino material.
    rhino_material = Rhino.DocObjects.Material();
    rhino_material.Name = "Chocolate";
    rhino_material.DiffuseColor = System.Drawing.Color.Chocolate;
    rhino_material.SpecularColor = System.Drawing.Color.CadetBlue;
    
    texture = Rhino.DocObjects.Texture()
    texture.FileName = "my_image.jpg"
    rhino_material.SetTexture(texture, Rhino.DocObjects.TextureType.Bitmap)

    # Use the Rhino material to create a Render material.
    render_material = Rhino.Render.RenderMaterial.CreateBasicMaterial(rhino_material, scriptcontext.doc)
    scriptcontext.doc.RenderMaterials.Add(render_material);

    # Create a sphere.
    sphere = Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 5);

    # Add the sphere to the document with a material.
    id = scriptcontext.doc.Objects.AddSphere(sphere);
    obj = scriptcontext.doc.Objects.FindId(id);
    if obj is not None:
      # Assign the render material to the sphere object.
      obj.RenderMaterial = render_material;
      obj.CommitChanges();

    scriptcontext.doc.Views.Redraw();

    return Rhino.Commands.Result.Success;

if __name__=="__main__":
    AddMaterial()
```

</div>

---
title: Add Material
description: Demonstrates how to add a material to the document's material table and apply it to a sphere object.
authors: ['steve_baer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/addmaterial
order: 1
keywords: ['add', 'basic', 'material']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddMaterial(Rhino.RhinoDoc doc)
  {
    // materials are stored in the document's material table
    var mat = new Material();
    mat.DiffuseColor = System.Drawing.Color.Chocolate;
    mat.SpecularColor = System.Drawing.Color.CadetBlue;

    var texture = new Texture();
    texture.FileName = "my_image.jpg";
    mat.SetTexture(texture, TextureType.Bitmap);

    var rm = RenderMaterial.CreateBasicMaterial(mat, doc);

    doc.RenderMaterials.Add(rm);

    // set up object attributes to say they use a specific material
    Rhino.Geometry.Sphere sp = new Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 5);

    var id = doc.Objects.AddSphere(sp);

    var rhinoObject = doc.Objects.Find(id);

    rhinoObject.RenderMaterial = rm;
    rhinoObject.CommitChanges();

    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function AddMaterial(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    ' materials are stored in the document's material table
    Dim index As Integer = doc.Materials.Add()
    Dim mat As Rhino.DocObjects.Material = New Rhino.DocObjects.Material
    mat.DiffuseColor = System.Drawing.Color.Chocolate
    mat.SpecularColor = System.Drawing.Color.CadetBlue

    Dim texture As Rhino.DocObjects.Texture = New Rhino.DocObjects.Texture()
    texture.FileName = "my_image.jpg"
    mat.SetTexture(texture, TextureType.Bitmap)

    Dim rm As Rhino.Render.RenderMaterial = Rhino.Render.RenderMaterial.CreateBasicMaterial(mat, doc)

    doc.RenderMaterials.Add(rm)

    ' set up object attributes to say they use a specific material
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
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext
import System.Drawing

def AddMaterial():
    # materials are stored in the document's material table
    mat = Rhino.DocObjects.Material()
    mat.DiffuseColor = System.Drawing.Color.Chocolate
    mat.SpecularColor = System.Drawing.Color.CadetBlue
    
    texture = Rhino.DocObjects.Texture()
    texture.FileName = "my_image.jpg"
    mat.SetTexture(texture, Rhino.DocObjects.TextureType.Bitmap)
    
    rm = Rhino.Render.RenderMaterial.CreateBasicMaterial(mat, scriptcontext.doc)

    scriptcontext.doc.RenderMaterials.Add(rm)

    sp = Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 5)
    scriptcontext.doc.Objects.AddSphere(sp)
    
    id = scriptcontext.doc.Objects.AddSphere(sp)
    
    rhinoObject = scriptcontext.doc.Objects.Find(id)

    rhinoObject.RenderMaterial = rm
    rhinoObject.CommitChanges()

    scriptcontext.doc.Views.Redraw();

if __name__=="__main__":
    AddMaterial()
```
{: #py .tab-pane .fade .in}

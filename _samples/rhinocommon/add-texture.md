---
title: Add Texture
description: Demonstrates how to add a texture to an object from a user-specified bitmap file.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/addtexture
order: 1
keywords: ['add', 'texture']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddTexture(Rhino.RhinoDoc doc)
  {
    // Select object to add texture
    const ObjectType filter = Rhino.DocObjects.ObjectType.Surface |
                              Rhino.DocObjects.ObjectType.PolysrfFilter |
                              Rhino.DocObjects.ObjectType.Mesh;
    Rhino.DocObjects.ObjRef objref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select object to add texture", false, filter, out objref);
    if( rc!= Rhino.Commands.Result.Success )
      return rc;

    Rhino.DocObjects.RhinoObject rhino_object = objref.Object();
    if (rhino_object == null)
      return Rhino.Commands.Result.Failure;

    // Select texture
    Rhino.UI.OpenFileDialog fd = new Rhino.UI.OpenFileDialog();
    fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg";
    if (!fd.ShowDialog())
      return Rhino.Commands.Result.Cancel;

    // Verify texture
    string bitmap_filename = fd.FileName;
    if( string.IsNullOrEmpty(bitmap_filename) || !System.IO.File.Exists(bitmap_filename) )
      return Rhino.Commands.Result.Nothing;

    // Make sure the object has it's material source set to "material_from_object"
    rhino_object.Attributes.MaterialSource = Rhino.DocObjects.ObjectMaterialSource.MaterialFromObject;

    // Make sure the object has a material assigned
    int material_index = rhino_object.Attributes.MaterialIndex;
    if (material_index < 0)
    {
      // Create a new material based on Rhino's default material
      material_index = doc.Materials.Add();
      // Assign the new material (index) to the object.
      rhino_object.Attributes.MaterialIndex = material_index;
    }

    if (material_index >= 0)
    {
      Rhino.DocObjects.Material mat = doc.Materials[material_index];
      mat.SetBumpTexture(bitmap_filename);
      mat.CommitChanges();

      //Don't forget to update the object, if necessary
      rhino_object.CommitChanges();

      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }

    return Rhino.Commands.Result.Failure;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function AddTexture(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	' Select object to add texture
	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Surface Or Rhino.DocObjects.ObjectType.PolysrfFilter Or Rhino.DocObjects.ObjectType.Mesh
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select object to add texture", False, filter, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim rhino_object As Rhino.DocObjects.RhinoObject = objref.Object()
	If rhino_object Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If

	' Select texture
	Dim fd As New Rhino.UI.OpenFileDialog()
	fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"
	If Not fd.ShowDialog() Then
	  Return Rhino.Commands.Result.Cancel
	End If

	' Verify texture
	Dim bitmap_filename As String = fd.FileName
	If String.IsNullOrEmpty(bitmap_filename) OrElse Not System.IO.File.Exists(bitmap_filename) Then
	  Return Rhino.Commands.Result.Nothing
	End If

	' Make sure the object has it's material source set to "material_from_object"
	rhino_object.Attributes.MaterialSource = Rhino.DocObjects.ObjectMaterialSource.MaterialFromObject

	' Make sure the object has a material assigned
	Dim material_index As Integer = rhino_object.Attributes.MaterialIndex
	If material_index < 0 Then
	  ' Create a new material based on Rhino's default material
	  material_index = doc.Materials.Add()
	  ' Assign the new material (index) to the object.
	  rhino_object.Attributes.MaterialIndex = material_index
	End If

	If material_index >= 0 Then
	  Dim mat As Rhino.DocObjects.Material = doc.Materials(material_index)
	  mat.SetBumpTexture(bitmap_filename)
	  mat.CommitChanges()

	  'Don't forget to update the object, if necessary
	  rhino_object.CommitChanges()

	  doc.Views.Redraw()
	  Return Rhino.Commands.Result.Success
	End If

	Return Rhino.Commands.Result.Failure
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext
import System.Guid
import System.Windows.Forms.DialogResult
import System.IO.File

def AddTexture():
    # Select object to add texture
    filter = Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter | Rhino.DocObjects.ObjectType.Mesh
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select object to add texture", False, filter)
    if rc!=Rhino.Commands.Result.Success: return rc

    rhino_object = objref.Object()
    if not rhino_object: return Rhino.Commands.Result.Failure

    # Select texture
    fd = Rhino.UI.OpenFileDialog()
    fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"
    if not fd.ShowDialog():
        return Rhino.Commands.Result.Cancel

    # Verify texture
    bitmap_filename = fd.FileName
    if not System.IO.File.Exists(bitmap_filename):
        return Rhino.Commands.Result.Nothing

    # Make sure the object has it's material source set to "material_from_object"
    rhino_object.Attributes.MaterialSource = Rhino.DocObjects.ObjectMaterialSource.MaterialFromObject

    # Make sure the object has a material assigned
    material_index = rhino_object.Attributes.MaterialIndex
    if material_index<0:
        # Create a new material based on Rhino's default material
        material_index = scriptcontext.doc.Materials.Add()
        # Assign the new material (index) to the object.
        rhino_object.Attributes.MaterialIndex = material_index

    if material_index>=0:
        mat = scriptcontext.doc.Materials[material_index]
        mat.SetBumpTexture(bitmap_filename)
        mat.CommitChanges()

        #Don't forget to update the object, if necessary
        rhino_object.CommitChanges()

        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success

    return Rhino.Commands.Result.Failure

if __name__=="__main__":
    AddTexture()
```
{: #py .tab-pane .fade .in}

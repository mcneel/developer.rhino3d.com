+++
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to extract the render mesh from a surface or polysurface."
keywords = [ "extract", "render", "mesh" ]
languages = [ "C#", "VB" ]
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


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function ExtractRenderMesh(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim objRef As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", False, Rhino.DocObjects.ObjectType.Brep, objRef)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim obj As Rhino.DocObjects.RhinoObject = objRef.Object()
	If Nothing Is obj Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim objList As New System.Collections.Generic.List(Of Rhino.DocObjects.RhinoObject)(1)
	objList.Add(obj)

	Dim meshObjRefs() As Rhino.DocObjects.ObjRef = Rhino.DocObjects.RhinoObject.GetRenderMeshes(objList, True, False)
	If Nothing IsNot meshObjRefs Then
	  For i As Integer = 0 To meshObjRefs.Length - 1
		Dim meshObjRef As Rhino.DocObjects.ObjRef = meshObjRefs(i)
		If Nothing IsNot meshObjRef Then
		  Dim mesh As Rhino.Geometry.Mesh = meshObjRef.Mesh()
		  If Nothing IsNot mesh Then
			doc.Objects.AddMesh(mesh)
		  End If
		End If
	  Next i
	  doc.Views.Redraw()
	End If

	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>

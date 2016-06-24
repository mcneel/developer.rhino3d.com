---
title: Edit Text
description: Demonstrates how to edit selected text, replacing it with new text.
author: steve@mcneel.com
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/edittext
order: 1
keywords: ['edit', 'text']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result EditText(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select text", false, Rhino.DocObjects.ObjectType.Annotation, out objref);
    if (rc != Rhino.Commands.Result.Success || objref == null)
      return rc;

    Rhino.DocObjects.TextObject textobj = objref.Object() as Rhino.DocObjects.TextObject;
    if (textobj == null)
      return Rhino.Commands.Result.Failure;

    Rhino.Geometry.TextEntity textentity = textobj.Geometry as Rhino.Geometry.TextEntity;
    if (textentity == null)
      return Rhino.Commands.Result.Failure;
    string str = textentity.Text;
    rc = Rhino.Input.RhinoGet.GetString("New text", false, ref str);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    textentity.Text = str;
    textobj.CommitChanges();
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function EditText(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select text", False, Rhino.DocObjects.ObjectType.Annotation, objref)
	If rc IsNot Rhino.Commands.Result.Success OrElse objref Is Nothing Then
	  Return rc
	End If

	Dim textobj As Rhino.DocObjects.TextObject = TryCast(objref.Object(), Rhino.DocObjects.TextObject)
	If textobj Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim textentity As Rhino.Geometry.TextEntity = TryCast(textobj.Geometry, Rhino.Geometry.TextEntity)
	If textentity Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If
	Dim str As String = textentity.Text
	rc = Rhino.Input.RhinoGet.GetString("New text", False, str)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	textentity.Text = str
	textobj.CommitChanges()
	doc.Views.Redraw()
	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext

def EditText():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select text", False, Rhino.DocObjects.ObjectType.Annotation)
    if rc!=Rhino.Commands.Result.Success: return

    textobj = objref.Object()
    if not textobj: return

    str = textobj.Geometry.Text
    rc, str = Rhino.Input.RhinoGet.GetString("New text", False, str)
    if rc!=Rhino.Commands.Result.Success: return

    textobj.Geometry.Text = str;
    textobj.CommitChanges();
    scriptcontext.doc.Views.Redraw();

if __name__=="__main__":
    EditText()
```
{: #py .tab-pane .fade .in}

---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: RhinoCommon object plug-in user data
keywords: ['info', 'rhinocommon', 'object', 'plug-in', 'user', 'data']
categories: ['Adding Objects']
description:
order: 1
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result Userdata(RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select Face", false, Rhino.DocObjects.ObjectType.Surface, out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    var face = objref.Face();

    // See if user data of my custom type is attached to the geomtry
    // We need to use the underlying surface in order to get the user data
    // to serialize with the file.
    var ud = face.UnderlyingSurface().UserData.Find(typeof(MyCustomData)) as MyCustomData;
    if (ud == null)
    {
      // No user data found; create one and add it
      int i = 0;
      rc = Rhino.Input.RhinoGet.GetInteger("Integer Value", false, ref i);
      if (rc != Rhino.Commands.Result.Success)
        return rc;

      ud = new MyCustomData(i, "This is some text");
      face.UnderlyingSurface().UserData.Add(ud);
    }
    else
    {
      RhinoApp.WriteLine("{0} = {1}", ud.Description, ud);
    }
    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function Userdata(ByVal doc As RhinoDoc) As Rhino.Commands.Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select Face", False, Rhino.DocObjects.ObjectType.Surface, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim face = objref.Face()

	' See if user data of my custom type is attached to the geomtry
	' We need to use the underlying surface in order to get the user data
	' to serialize with the file.
	Dim ud = TryCast(face.UnderlyingSurface().UserData.Find(GetType(MyCustomData)), MyCustomData)
	If ud Is Nothing Then
	  ' No user data found; create one and add it
	  Dim i As Integer = 0
	  rc = Rhino.Input.RhinoGet.GetInteger("Integer Value", False, i)
	  If rc IsNot Rhino.Commands.Result.Success Then
		Return rc
	  End If

	  ud = New MyCustomData(i, "This is some text")
	  face.UnderlyingSurface().UserData.Add(ud)
	Else
	  RhinoApp.WriteLine("{0} = {1}", ud.Description, ud)
	End If
	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}


---
title: Add Cone
description:
author:
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
platforms: ['Cross-Platform']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/addcone
order: 1
keywords: ['add', 'cone']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddCone(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Plane plane = Rhino.Geometry.Plane.WorldXY;
    const double height = 10;
    const double radius = 5;
    Rhino.Geometry.Cone cone = new Rhino.Geometry.Cone(plane, height, radius);
    if (cone.IsValid)
    {
      const bool cap_bottom = true;
      Rhino.Geometry.Brep cone_brep = cone.ToBrep(cap_bottom);
      if (cone_brep!=null)
      {
        doc.Objects.AddBrep(cone_brep);
        doc.Views.Redraw();
      }
    }
    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function AddCone(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim plane As Rhino.Geometry.Plane = Rhino.Geometry.Plane.WorldXY
	Const height As Double = 10
	Const radius As Double = 5
	Dim cone As New Rhino.Geometry.Cone(plane, height, radius)
	If cone.IsValid Then
	  Const cap_bottom As Boolean = True
	  Dim cone_brep As Rhino.Geometry.Brep = cone.ToBrep(cap_bottom)
	  If cone_brep IsNot Nothing Then
		doc.Objects.AddBrep(cone_brep)
		doc.Views.Redraw()
	  End If
	End If
	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext

def AddCone():
    plane = Rhino.Geometry.Plane.WorldXY
    height = 10
    radius = 5
    cone = Rhino.Geometry.Cone(plane, height, radius)
    if cone.IsValid:
        cap_bottom = True
        cone_brep = cone.ToBrep(cap_bottom)
        if cone_brep:
            scriptcontext.doc.Objects.AddBrep(cone_brep)
            scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    AddCone()
```
{: #py .tab-pane .fade .in}

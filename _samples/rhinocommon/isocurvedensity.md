---
layout: code-sample-rhinocommon
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Adjusting Surface Isocurve Density
keywords: ['adjusting', 'surface', 'isocurve', 'density']
categories: ['Other']
description:
order: 1
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result IsocurveDensity(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select surface", false, Rhino.DocObjects.ObjectType.Surface, out objref);
    if( rc!= Rhino.Commands.Result.Success )
      return rc;

    var brep_obj = objref.Object() as Rhino.DocObjects.BrepObject;
    if( brep_obj!=null )
    {
      brep_obj.Attributes.WireDensity = 3;
      brep_obj.CommitChanges();
      doc.Views.Redraw();
    }
    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function IsocurveDensity(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select surface", False, Rhino.DocObjects.ObjectType.Surface, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim brep_obj = TryCast(objref.Object(), Rhino.DocObjects.BrepObject)
	If brep_obj IsNot Nothing Then
	  brep_obj.Attributes.WireDensity = 3
	  brep_obj.CommitChanges()
	  doc.Views.Redraw()
	End If
	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext

def IsocurveDensity():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select surface", False, Rhino.DocObjects.ObjectType.Surface)
    if rc!= Rhino.Commands.Result.Success: return

    brep_obj = objref.Object()
    if brep_obj:
        brep_obj.Attributes.WireDensity = 3
        brep_obj.CommitChanges()
        scriptcontext.doc.Views.Redraw()

if __name__=="__main__":
    IsocurveDensity()
```
{: #py .tab-pane .fade .in}


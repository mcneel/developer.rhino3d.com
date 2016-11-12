---
title: Reverse Curve
description: Demonstrates how to reverse the direction of user-specified curves.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/curvereverse
order: 1
keywords: ['reverse', 'curve']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result ReverseCurve(RhinoDoc doc)
  {
    ObjRef[] obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select curves to reverse", true, ObjectType.Curve, out obj_refs);
    if (rc != Result.Success)
      return rc;

    foreach (var obj_ref in obj_refs)
    {
      var curve_copy = obj_ref.Curve().DuplicateCurve();
      if (curve_copy != null)
      {
        curve_copy.Reverse();
        doc.Objects.Replace(obj_ref, curve_copy);
      }
    }
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ReverseCurve(ByVal doc As RhinoDoc) As Result
	Dim obj_refs() As ObjRef = Nothing
	Dim rc = RhinoGet.GetMultipleObjects("Select curves to reverse", True, ObjectType.Curve, obj_refs)
	If rc IsNot Result.Success Then
	  Return rc
	End If

	For Each obj_ref In obj_refs
	  Dim curve_copy = obj_ref.Curve().DuplicateCurve()
	  If curve_copy IsNot Nothing Then
		curve_copy.Reverse()
		doc.Objects.Replace(obj_ref, curve_copy)
	  End If
	Next obj_ref
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs
from scriptcontext import *
import Rhino

def ReverseCurves():
    crvs = rs.GetObjects("Select curves to reverse", rs.filter.curve)
    if not crvs: return

    for crvid in crvs:
        crv = rs.coercecurve(crvid)
        if not crv: continue
        dup = crv.DuplicateCurve()
        if dup:
            dup.Reverse()
        doc.Objects.Replace(crvid, dup)

if __name__ == "__main__":
    ReverseCurves()
```
{: #py .tab-pane .fade .in}

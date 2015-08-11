---
layout: code-sample
title: Reversing the Direction of Curves
author: 
categories: ['Curves'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['reversing', 'direction', 'curves']
order: 50
description:  
---



```cs
public class ReverseCurveCommand : Command
{
  public override string EnglishName { get { return "csReverseCurve"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Public Class ReverseCurveCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbReverseCurve"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim objRefs As ObjRef() = Nothing
    Dim rc = RhinoGet.GetMultipleObjects("Select curves to reverse", True, ObjectType.Curve, objRefs)
    If rc <> Result.Success Then
      Return rc
    End If

    For Each objRef As ObjRef In objRefs
      Dim curveCopy = objRef.Curve().DuplicateCurve()
      If curveCopy IsNot Nothing Then
        curveCopy.Reverse()
        doc.Objects.Replace(objRef, curveCopy)
      End If
    Next
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



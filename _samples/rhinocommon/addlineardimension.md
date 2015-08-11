---
layout: code-sample
title: Add Linear Dimension
author: 
categories: ['Drafting'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['linear', 'dimension']
order: 12
description:  
---



```cs
public static Rhino.Commands.Result AddLinearDimension(Rhino.RhinoDoc doc)
{
  Rhino.Geometry.LinearDimension dimension;
  Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetLinearDimension(out dimension);
  if (rc == Rhino.Commands.Result.Success && dimension != null)
  {
    if (doc.Objects.AddLinearDimension(dimension) == Guid.Empty)
      rc = Rhino.Commands.Result.Failure;
    else
      doc.Views.Redraw();
  }
  return rc;
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Shared Function AddLinearDimension(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
  Dim dimension As Rhino.Geometry.LinearDimension = Nothing
  Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetLinearDimension(dimension)
  If rc = Rhino.Commands.Result.Success AndAlso dimension IsNot Nothing Then
    If doc.Objects.AddLinearDimension(dimension) = Guid.Empty Then
      rc = Rhino.Commands.Result.Failure
    Else
      doc.Views.Redraw()
    End If
  End If
  Return rc
End Function
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext
import System.Guid

def AddLinearDimension():
    rc, dimension = Rhino.Input.RhinoGet.GetLinearDimension()
    if rc==Rhino.Commands.Result.Success:
        if scriptcontext.doc.Objects.AddLinearDimension(dimension)==System.Guid.Empty:
            rc = Rhino.Commands.Result.Failure
        else:
            scriptcontext.doc.Views.Redraw()
    return rc


if __name__=="__main__":
    AddLinearDimension()
```
{: #py .tab-pane .fade .in}



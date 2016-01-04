---
title: Add Linear Dimension
description:
author:
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
platforms: ['Cross-Platform']
categories: ['Adding Objects']
origin: unset
order: 1
keywords: ['add', 'linear', 'dimension']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
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
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function AddLinearDimension(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim dimension As Rhino.Geometry.LinearDimension = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetLinearDimension(dimension)
	If rc Is Rhino.Commands.Result.Success AndAlso dimension IsNot Nothing Then
	  If doc.Objects.AddLinearDimension(dimension) = Guid.Empty Then
		rc = Rhino.Commands.Result.Failure
	  Else
		doc.Views.Redraw()
	  End If
	End If
	Return rc
  End Function
End Class
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


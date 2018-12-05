---
title: Increase NURBS Surface Degree
description: Demonstrates how to increase the degree of a NURBS surface.
authors: ['steve_baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/nurbssurfaceincreasedegree
order: 1
keywords: ['increasing', 'degree', 'nurbs', 'surface']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result NurbsSurfaceIncreaseDegree(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject(
      "Select surface", false, ObjectType.Surface, out obj_ref);
    if (rc != Result.Success) return rc;
    if (obj_ref == null) return Result.Failure;
    var surface = obj_ref.Surface();
    if (surface == null) return Result.Failure;
    var nurbs_surface = surface.ToNurbsSurface();

    int new_u_degree = -1;
    rc = RhinoGet.GetInteger(string.Format("New U degree <{0}...11>", nurbs_surface.Degree(0)), true, ref new_u_degree,
      nurbs_surface.Degree(0), 11);
    if (rc != Result.Success) return rc;

    int new_v_degree = -1;
    rc = RhinoGet.GetInteger(string.Format("New V degree <{0}...11>", nurbs_surface.Degree(1)), true, ref new_v_degree,
      nurbs_surface.Degree(1), 11);
    if (rc != Result.Success) return rc;

    rc = Result.Failure;
    if (nurbs_surface.IncreaseDegreeU(new_u_degree))
      if (nurbs_surface.IncreaseDegreeV(new_v_degree))
        if (doc.Objects.Replace(obj_ref.ObjectId, nurbs_surface))
          rc = Result.Success;

    RhinoApp.WriteLine("Result: {0}", rc.ToString());
    doc.Views.Redraw();
    return rc;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function NurbsSurfaceIncreaseDegree(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select surface", False, ObjectType.Surface, obj_ref)
	If rc IsNot Result.Success Then
		Return rc
	End If
	If obj_ref Is Nothing Then
		Return Result.Failure
	End If
	Dim surface = obj_ref.Surface()
	If surface Is Nothing Then
		Return Result.Failure
	End If
	Dim nurbs_surface = surface.ToNurbsSurface()

	Dim new_u_degree As Integer = -1
	rc = RhinoGet.GetInteger(String.Format("New U degree <{0}...11>", nurbs_surface.Degree(0)), True, new_u_degree, nurbs_surface.Degree(0), 11)
	If rc IsNot Result.Success Then
		Return rc
	End If

	Dim new_v_degree As Integer = -1
	rc = RhinoGet.GetInteger(String.Format("New V degree <{0}...11>", nurbs_surface.Degree(1)), True, new_v_degree, nurbs_surface.Degree(1), 11)
	If rc IsNot Result.Success Then
		Return rc
	End If

	rc = Result.Failure
	If nurbs_surface.IncreaseDegreeU(new_u_degree) Then
	  If nurbs_surface.IncreaseDegreeV(new_v_degree) Then
		If doc.Objects.Replace(obj_ref.ObjectId, nurbs_surface) Then
		  rc = Result.Success
		End If
	  End If
	End If

	RhinoApp.WriteLine("Result: {0}", rc.ToString())
	doc.Views.Redraw()
	Return rc
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.Commands import *
from Rhino.Input import *
from Rhino.DocObjects import *
from scriptcontext import doc

def RunCommand():
  rc, obj_ref = RhinoGet.GetOneObject("Select surface", False, ObjectType.Surface)
  if rc != Result.Success: return rc
  if obj_ref == None: return Result.Failure
  surface = obj_ref.Surface()
  if surface == None: return Result.Failure
  nurbs_surface = surface.ToNurbsSurface()

  new_u_degree = -1
  rc, new_u_degree = RhinoGet.GetInteger(
    "New U degree <{0}...11>".format(nurbs_surface.Degree(0)), True, new_u_degree, nurbs_surface.Degree(0), 11)
  if rc != Result.Success: return rc

  new_v_degree = -1
  rc, new_v_degree = RhinoGet.GetInteger(
    "New V degree <{0}...11>".format(nurbs_surface.Degree(1)), True, new_v_degree, nurbs_surface.Degree(1), 11)
  if rc != Result.Success: return rc

  rc = Result.Failure
  if nurbs_surface.IncreaseDegreeU(new_u_degree):
    if nurbs_surface.IncreaseDegreeV(new_v_degree):
      if doc.Objects.Replace(obj_ref.ObjectId, nurbs_surface):
        rc = Result.Success

  print "Result: {0}".format(rc)
  doc.Views.Redraw()
  return rc

if __name__=="__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}

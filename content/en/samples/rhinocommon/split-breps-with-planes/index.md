+++
aliases = ["/en/5/samples/rhinocommon/split-breps-with-planes/", "/en/6/samples/rhinocommon/split-breps-with-planes/", "/en/7/samples/rhinocommon/split-breps-with-planes/", "/en/wip/samples/rhinocommon/split-breps-with-planes/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Split a Set of BReps with a Plane"
keywords = [ "split", "breps", "with", "plane" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Split BReps with Planes"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/splitbrepwithplane"
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
  public static Result SplitBrepsWithPlane(RhinoDoc doc)
  {
    //First, collect all the breps to split
    ObjRef[] obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select breps to split", false, ObjectType.Brep, out obj_refs);
    if (rc != Result.Success || obj_refs == null)
      return rc;

    // Get the final plane
    Plane plane;
    rc = RhinoGet.GetPlane(out plane);
    if (rc != Result.Success)
      return rc;

    //Iterate over all object references
    foreach (var obj_ref in obj_refs)
    {
      var brep = obj_ref.Brep();
      var bbox = brep.GetBoundingBox(false);

      //Grow the boundingbox in all directions
      //If the boundingbox is flat (zero volume or even zero area)
      //then the CreateThroughBox method will fail.
      var min_point = bbox.Min;
      min_point.X -= 1.0;
      min_point.Y -= 1.0;
      min_point.Z -= 1.0;
      bbox.Min = min_point;
      var max_point = bbox.Max;
      max_point.X += 1.0;
      max_point.Y += 1.0;
      max_point.Z += 1.0;
      bbox.Max = max_point;

      var plane_surface = PlaneSurface.CreateThroughBox(plane, bbox);
      if (plane_surface == null)
      {
        //This is rare, it will most likely not happen unless either the plane or the boundingbox are invalid
        RhinoApp.WriteLine("Cutting plane could not be constructed.");
      }
      else
      {
        var breps = brep.Split(plane_surface.ToBrep(), doc.ModelAbsoluteTolerance);
        if (breps == null || breps.Length == 0)
        {
          RhinoApp.Write("Plane does not intersect brep (id:{0})", obj_ref.ObjectId);
          continue;
        }
        foreach (var brep_piece in breps)
        {
          doc.Objects.AddBrep(brep_piece);
        }
        doc.Objects.AddSurface(plane_surface);
        doc.Objects.Delete(obj_ref, false);
      }
    }

    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function SplitBrepsWithPlane(ByVal doc As RhinoDoc) As Result
	'First, collect all the breps to split
	Dim obj_refs() As ObjRef = Nothing
	Dim rc = RhinoGet.GetMultipleObjects("Select breps to split", False, ObjectType.Brep, obj_refs)
	If rc IsNot Result.Success OrElse obj_refs Is Nothing Then
	  Return rc
	End If

	' Get the final plane
	Dim plane As Plane = Nothing
	rc = RhinoGet.GetPlane(plane)
	If rc IsNot Result.Success Then
	  Return rc
	End If

	'Iterate over all object references
	For Each obj_ref In obj_refs
	  Dim brep = obj_ref.Brep()
	  Dim bbox = brep.GetBoundingBox(False)

	  'Grow the boundingbox in all directions
	  'If the boundingbox is flat (zero volume or even zero area)
	  'then the CreateThroughBox method will fail.
	  Dim min_point = bbox.Min
	  min_point.X -= 1.0
	  min_point.Y -= 1.0
	  min_point.Z -= 1.0
	  bbox.Min = min_point
	  Dim max_point = bbox.Max
	  max_point.X += 1.0
	  max_point.Y += 1.0
	  max_point.Z += 1.0
	  bbox.Max = max_point

	  Dim plane_surface = PlaneSurface.CreateThroughBox(plane, bbox)
	  If plane_surface Is Nothing Then
		'This is rare, it will most likely not happen unless either the plane or the boundingbox are invalid
		RhinoApp.WriteLine("Cutting plane could not be constructed.")
	  Else
		Dim breps = brep.Split(plane_surface.ToBrep(), doc.ModelAbsoluteTolerance)
		If breps Is Nothing OrElse breps.Length = 0 Then
		  RhinoApp.Write("Plane does not intersect brep (id:{0})", obj_ref.ObjectId)
		  Continue For
		End If
		For Each brep_piece In breps
		  doc.Objects.AddBrep(brep_piece)
		Next brep_piece
		doc.Objects.AddSurface(plane_surface)
		doc.Objects.Delete(obj_ref, False)
	  End If
	Next obj_ref

	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from Rhino.Input import *
from Rhino.Geometry import *
from scriptcontext import doc

def RunCommand():
    #First, collect all the breps to split
    rc, obj_refs = RhinoGet.GetMultipleObjects("Select breps to split", False, ObjectType.Brep)
    if rc != Result.Success or obj_refs == None:
        return rc

    # Get the final plane
    rc, plane = RhinoGet.GetPlane()
    if rc != Result.Success:
        return rc

    #Iterate over all object references
    for obj_ref in obj_refs:
        brep = obj_ref.Brep()
        bbox = brep.GetBoundingBox(False)

        #Grow the boundingbox in all directions
        #If the boundingbox is flat (zero volume or even zero area)
        #then the CreateThroughBox method will fail.
        min_point = bbox.Min
        min_point.X -= 1.0
        min_point.Y -= 1.0
        min_point.Z -= 1.0
        bbox.Min = min_point
        max_point = bbox.Max
        max_point.X += 1.0
        max_point.Y += 1.0
        max_point.Z += 1.0
        bbox.Max = max_point

        plane_surface = PlaneSurface.CreateThroughBox(plane, bbox)
        if plane_surface == None:
            #This is rare, it will most likely not happen unless either the plane or the boundingbox are invalid
            RhinoApp.WriteLine("Cutting plane could not be constructed.")
        else:
            breps = brep.Split(plane_surface.ToBrep(), doc.ModelAbsoluteTolerance)
            if breps == None or breps.Length == 0:
                RhinoApp.Write("Plane does not intersect brep (id:{0})", obj_ref.ObjectId)
                continue
            for brep_piece in breps:
                doc.Objects.AddBrep(brep_piece)
            doc.Objects.AddSurface(plane_surface)
            doc.Objects.Delete(obj_ref, False)

    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>

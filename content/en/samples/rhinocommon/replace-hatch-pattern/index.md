+++
aliases = ["/en/5/samples/rhinocommon/replace-hatch-pattern/", "/en/6/samples/rhinocommon/replace-hatch-pattern/", "/en/7/samples/rhinocommon/replace-hatch-pattern/", "/wip/samples/rhinocommon/replace-hatch-pattern/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to replace an object's hatch pattern."
keywords = [ "replacing", "hatch", "objects", "pattern" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Replace Hatch Pattern"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/replacehatchpattern"
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
  public static Result ReplaceHatchPattern(RhinoDoc doc)
  {
    ObjRef[] obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select hatches to replace", false, ObjectType.Hatch, out obj_refs);
    if (rc != Result.Success || obj_refs == null)
      return rc;

    var gs = new GetString();
    gs.SetCommandPrompt("Name of replacement hatch pattern");
    gs.AcceptNothing(false);
    gs.Get();
    if (gs.CommandResult() != Result.Success)
      return gs.CommandResult();
    var hatch_name = gs.StringResult();

    var pattern_index = doc.HatchPatterns.Find(hatch_name, true);

    if (pattern_index < 0)
    {
      RhinoApp.WriteLine("The hatch pattern \"{0}\" not found  in the document.", hatch_name);
      return Result.Nothing;
    }

    foreach (var obj_ref in obj_refs)
    {
      var hatch_object = obj_ref.Object() as HatchObject;
      if (hatch_object.HatchGeometry.PatternIndex != pattern_index)
      {
        hatch_object.HatchGeometry.PatternIndex = pattern_index;
        hatch_object.CommitChanges();
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
  Public Shared Function ReplaceHatchPattern(ByVal doc As RhinoDoc) As Result
	Dim obj_refs() As ObjRef = Nothing
	Dim rc = RhinoGet.GetMultipleObjects("Select hatches to replace", False, ObjectType.Hatch, obj_refs)
	If rc IsNot Result.Success OrElse obj_refs Is Nothing Then
	  Return rc
	End If

	Dim gs = New GetString()
	gs.SetCommandPrompt("Name of replacement hatch pattern")
	gs.AcceptNothing(False)
	gs.Get()
	If gs.CommandResult() <> Result.Success Then
	  Return gs.CommandResult()
	End If
	Dim hatch_name = gs.StringResult()

	Dim pattern_index = doc.HatchPatterns.Find(hatch_name, True)

	If pattern_index < 0 Then
	  RhinoApp.WriteLine("The hatch pattern ""{0}"" not found  in the document.", hatch_name)
	  Return Result.Nothing
	End If

	For Each obj_ref In obj_refs
	  Dim hatch_object = TryCast(obj_ref.Object(), HatchObject)
	  If hatch_object.HatchGeometry.PatternIndex IsNot pattern_index Then
		hatch_object.HatchGeometry.PatternIndex = pattern_index
		hatch_object.CommitChanges()
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
from Rhino.Input.Custom import *
from scriptcontext import doc

def RunCommand():
    rc, obj_refs = RhinoGet.GetMultipleObjects("Select hatches to replace", False, ObjectType.Hatch)
    if rc != Result.Success or obj_refs == None:
        return rc

    gs = GetString()
    gs.SetCommandPrompt("Name of replacement hatch pattern")
    gs.AcceptNothing(False)
    gs.Get()
    if gs.CommandResult() != Result.Success:
        return gs.CommandResult()
    hatch_name = gs.StringResult()

    pattern_index = doc.HatchPatterns.Find(hatch_name, True)

    if pattern_index < 0:
        RhinoApp.WriteLine("The hatch pattern \"{0}\" not found  in the document.", hatch_name)
        return Result.Nothing

    for obj_ref in obj_refs:
        hatch_object = obj_ref.Object()
        if hatch_object.HatchGeometry.PatternIndex != pattern_index:
            hatch_object.HatchGeometry.PatternIndex = pattern_index
            hatch_object.CommitChanges()

    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>

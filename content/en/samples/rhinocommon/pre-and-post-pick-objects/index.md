+++
aliases = ["/en/5/samples/rhinocommon/pre-and-post-pick-objects/", "/en/6/samples/rhinocommon/pre-and-post-pick-objects/", "/en/7/samples/rhinocommon/pre-and-post-pick-objects/", "/en/wip/samples/rhinocommon/pre-and-post-pick-objects/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to customize Rhino's pre and post picking of objects behavior."
keywords = [ "pre-pick", "post-pick", "objects" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Pre and Post-Pick Objects"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/prepostpick"
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
  public static Result PrePostPick(RhinoDoc doc)
  {
    var go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select objects");
    go.EnablePreSelect(true, true);
    go.EnablePostSelect(true);
    go.GetMultiple(0, 0);
    if (go.CommandResult() != Result.Success)
      return go.CommandResult();

    var selected_objects = go.Objects().ToList();

    if (go.ObjectsWerePreselected)
    {
      go.EnablePreSelect(false, true);
      go.DeselectAllBeforePostSelect = false;
      go.EnableUnselectObjectsOnExit(false);
      go.GetMultiple(0, 0);
      if (go.CommandResult() == Result.Success)
      {
        foreach (var obj in go.Objects())
        {
          selected_objects.Add(obj);
          // The normal behavior of commands is that when they finish,
          // objects that were pre-selected remain selected and objects
          // that were post-selected will not be selected. Because we
          // potentially could have both, we'll try to do something
          // consistent and make sure post-selected objects also stay selected
          obj.Object().Select(true);
        }
      }
    }
    return selected_objects.Count > 0 ? Result.Success : Result.Nothing;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function PrePostPick(ByVal doc As RhinoDoc) As Result
	Dim go = New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select objects")
	go.EnablePreSelect(True, True)
	go.EnablePostSelect(True)
	go.GetMultiple(0, 0)
	If go.CommandResult() <> Result.Success Then
	  Return go.CommandResult()
	End If

	Dim selected_objects = go.Objects().ToList()

	If go.ObjectsWerePreselected Then
	  go.EnablePreSelect(False, True)
	  go.DeselectAllBeforePostSelect = False
	  go.EnableUnselectObjectsOnExit(False)
	  go.GetMultiple(0, 0)
	  If go.CommandResult() = Result.Success Then
		For Each obj In go.Objects()
		  selected_objects.Add(obj)
		  ' The normal behavior of commands is that when they finish,
		  ' objects that were pre-selected remain selected and objects
		  ' that were post-selected will not be selected. Because we
		  ' potentially could have both, we'll try to do something
		  ' consistent and make sure post-selected objects also stay selected
		  obj.Object().Select(True)
		Next obj
	  End If
	End If
	Return If(selected_objects.Count > 0, Result.Success, Result.Nothing)
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.Commands import *
from Rhino.Input.Custom import *

def RunCommand():
    go = GetObject()
    go.SetCommandPrompt("Select objects")
    go.EnablePreSelect(True, True)
    go.EnablePostSelect(True)
    go.GetMultiple(0, 0)
    if go.CommandResult() != Result.Success:
        return go.CommandResult()

    selected_objects = []
    for obj in go.Objects():
        selected_objects.Add(obj)

    if go.ObjectsWerePreselected:
        go.EnablePreSelect(False, True)
        go.DeselectAllBeforePostSelect = False
        go.EnableUnselectObjectsOnExit(False)
        go.GetMultiple(0, 0)
        if go.CommandResult() == Result.Success:
            for obj in go.Objects():
                selected_objects.Add(obj)
                # The normal behavior of commands is that when they finish,
                # objects that were pre-selected remain selected and objects
                # that were post-selected will not be selected. Because we
                # potentially could have both, we'll try to do something
                # consistent and make sure post-selected objects also stay selected
                obj.Object().Select(True)
    return Result.Success if selected_objects.Count > 0 else Result.Nothing

if __name__ == "__main__":
    RunCommand()
```

</div>

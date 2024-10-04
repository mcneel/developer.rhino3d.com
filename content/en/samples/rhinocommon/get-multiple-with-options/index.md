+++
aliases = ["/en/5/samples/rhinocommon/get-multiple-with-options/", "/en/6/samples/rhinocommon/get-multiple-with-options/", "/en/7/samples/rhinocommon/get-multiple-with-options/", "/wip/samples/rhinocommon/get-multiple-with-options/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to get multiple objects in Rhino command-line options."
keywords = [ "multiple", "with", "options" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Get Multiple With Options"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
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
  public static Rhino.Commands.Result GetMultipleWithOptions(Rhino.RhinoDoc doc)
  {
    const Rhino.DocObjects.ObjectType geometryFilter = Rhino.DocObjects.ObjectType.Surface | 
                                                       Rhino.DocObjects.ObjectType.PolysrfFilter | 
                                                       Rhino.DocObjects.ObjectType.Mesh;
    int integer1 = 300;
    int integer2 = 300;

    Rhino.Input.Custom.OptionInteger optionInteger1 = new Rhino.Input.Custom.OptionInteger(integer1, 200, 900);
    Rhino.Input.Custom.OptionInteger optionInteger2 = new Rhino.Input.Custom.OptionInteger(integer2, 200, 900);

    Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select surfaces, polysurfaces, or meshes");
    go.GeometryFilter = geometryFilter;
    go.AddOptionInteger("Option1", ref optionInteger1);
    go.AddOptionInteger("Option2", ref optionInteger2);
    go.GroupSelect = true;
    go.SubObjectSelect = false;
    go.EnableClearObjectsOnEntry(false);
    go.EnableUnselectObjectsOnExit(false);
    go.DeselectAllBeforePostSelect = false;

    bool bHavePreselectedObjects = false;

    for (; ; )
    {
      Rhino.Input.GetResult res = go.GetMultiple(1, 0);

      if (res == Rhino.Input.GetResult.Option)
      {
        go.EnablePreSelect(false, true);
        continue;
      }

      else if (res != Rhino.Input.GetResult.Object)
        return Rhino.Commands.Result.Cancel;

      if (go.ObjectsWerePreselected)
      {
        bHavePreselectedObjects = true;
        go.EnablePreSelect(false, true);
        continue;
      }

      break;
    }

    if (bHavePreselectedObjects)
    {
      // Normally when command finishes, pre-selected objects will remain
      // selected, when and post-selected objects will be unselected.
      // With this sample, it is possible to have a combination of 
      // pre-selected and post-selected objects. To make sure everything
      // "looks the same", unselect everything before finishing the command.
      for (int i = 0; i < go.ObjectCount; i++)
      {
        Rhino.DocObjects.RhinoObject rhinoObject = go.Object(i).Object();
        if (null != rhinoObject)
          rhinoObject.Select(false);
      }
      doc.Views.Redraw();
    }

    int objectCount = go.ObjectCount;
    integer1 = optionInteger1.CurrentValue;
    integer2 = optionInteger2.CurrentValue;

    Rhino.RhinoApp.WriteLine("Select object count = {0}", objectCount);
    Rhino.RhinoApp.WriteLine("Value of integer1 = {0}", integer1);
    Rhino.RhinoApp.WriteLine("Value of integer2 = {0}", integer2);

    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function GetMultipleWithOptions(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Const geometryFilter As Rhino.DocObjects.ObjectType = Rhino.DocObjects.ObjectType.Surface Or Rhino.DocObjects.ObjectType.PolysrfFilter Or Rhino.DocObjects.ObjectType.Mesh
	Dim integer1 As Integer = 300
	Dim integer2 As Integer = 300

	Dim optionInteger1 As New Rhino.Input.Custom.OptionInteger(integer1, 200, 900)
	Dim optionInteger2 As New Rhino.Input.Custom.OptionInteger(integer2, 200, 900)

	Dim go As New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select surfaces, polysurfaces, or meshes")
	go.GeometryFilter = geometryFilter
	go.AddOptionInteger("Option1", optionInteger1)
	go.AddOptionInteger("Option2", optionInteger2)
	go.GroupSelect = True
	go.SubObjectSelect = False
	go.EnableClearObjectsOnEntry(False)
	go.EnableUnselectObjectsOnExit(False)
	go.DeselectAllBeforePostSelect = False

	Dim bHavePreselectedObjects As Boolean = False

	Do
	  Dim res As Rhino.Input.GetResult = go.GetMultiple(1, 0)

	  If res Is Rhino.Input.GetResult.Option Then
		go.EnablePreSelect(False, True)
		Continue Do

	  ElseIf res IsNot Rhino.Input.GetResult.Object Then
		Return Rhino.Commands.Result.Cancel
	  End If

	  If go.ObjectsWerePreselected Then
		bHavePreselectedObjects = True
		go.EnablePreSelect(False, True)
		Continue Do
	  End If

	  Exit Do
	Loop

	If bHavePreselectedObjects Then
	  ' Normally when command finishes, pre-selected objects will remain
	  ' selected, when and post-selected objects will be unselected.
	  ' With this sample, it is possible to have a combination of 
	  ' pre-selected and post-selected objects. To make sure everything
	  ' "looks the same", unselect everything before finishing the command.
	  For i As Integer = 0 To go.ObjectCount - 1
		Dim rhinoObject As Rhino.DocObjects.RhinoObject = go.Object(i).Object()
		If Nothing IsNot rhinoObject Then
		  rhinoObject.Select(False)
		End If
	  Next i
	  doc.Views.Redraw()
	End If

	Dim objectCount As Integer = go.ObjectCount
	integer1 = optionInteger1.CurrentValue
	integer2 = optionInteger2.CurrentValue

	Rhino.RhinoApp.WriteLine("Select object count = {0}", objectCount)
	Rhino.RhinoApp.WriteLine("Value of integer1 = {0}", integer1)
	Rhino.RhinoApp.WriteLine("Value of integer2 = {0}", integer2)

	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def GetMultipleWithOptions():
    geometryFilter = Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter | Rhino.DocObjects.ObjectType.Mesh
    integer1 = 300
    integer2 = 300

    optionInteger1 = Rhino.Input.Custom.OptionInteger(integer1, 200, 900)
    optionInteger2 = Rhino.Input.Custom.OptionInteger(integer2, 200, 900)

    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select surfaces, polysurfaces, or meshes")
    go.GeometryFilter = geometryFilter
    go.AddOptionInteger("Option1", optionInteger1)
    go.AddOptionInteger("Option2", optionInteger2)
    go.GroupSelect = True
    go.SubObjectSelect = False
    go.EnableClearObjectsOnEntry(False)
    go.EnableUnselectObjectsOnExit(False)
    go.DeselectAllBeforePostSelect = False

    bHavePreselectedObjects = False

    while True:
        res = go.GetMultiple(1, 0)

        if res == Rhino.Input.GetResult.Option:
            go.EnablePreSelect(False, True)
            continue

        elif res != Rhino.Input.GetResult.Object:
            return Rhino.Commands.Result.Cancel

        if go.ObjectsWerePreselected:
            bHavePreselectedObjects = True
            go.EnablePreSelect(False, True)
            continue

        break

    if bHavePreselectedObjects:
        # Normally, pre-selected objects will remain selected, when a
        # command finishes, and post-selected objects will be unselected.
        # This this way of picking, it is possible to have a combination
        # of pre-selected and post-selected. So, to make sure everything
        # "looks the same", lets unselect everything before finishing
        # the command.
        for i in range(0, go.ObjectCount):
            rhinoObject = go.Object(i).Object()
            if not rhinoObject is None:
                rhinoObject.Select(False)
        scriptcontext.doc.Views.Redraw()

    objectCount = go.ObjectCount
    integer1 = optionInteger1.CurrentValue
    integer2 = optionInteger2.CurrentValue

    Rhino.RhinoApp.WriteLine("Select object count = {0}", objectCount)
    Rhino.RhinoApp.WriteLine("Value of integer1 = {0}", integer1)
    Rhino.RhinoApp.WriteLine("Value of integer2 = {0}", integer2)

    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    GetMultipleWithOptions()
```

</div>


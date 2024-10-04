+++
aliases = ["/en/en/5/guides/rhinocommon/object-selection-options/", "/en/6/guides/rhinocommon/object-selection-options/", "/en/7/guides/rhinocommon/object-selection-options/", "/wip/guides/rhinocommon/object-selection-options/"]
authors = [ "steve" ]
categories = [ "Fundamentals" ]
description = "This guide covers how to pick some objects, select command options, return to picking more objects, all while keeping your current selection set."
keywords = [ "RhinoCommon", "Object", "Selection", "Options" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Object Selection with Options"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/developer/rhinocommonsamples/getobjectoption"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## GetObject

RhinoCommon's [GetObject class](/api/RhinoCommon/html/T_Rhino_Input_Custom_GetObject.htm) has a few properties and methods that you need to use, including:

- [GetObject.EnableClearObjectsOnEntry](/api/RhinoCommon/html/M_Rhino_Input_Custom_GetObject_EnableClearObjectsOnEntry.htm)
- [GetObject.EnableUnselectObjectsOnExit](/api/RhinoCommon/html/M_Rhino_Input_Custom_GetObject_EnableUnselectObjectsOnExit.htm)
- [GetObject.DeselectAllBeforePostSelect](/api/RhinoCommon/html/P_Rhino_Input_Custom_GetObject_DeselectAllBeforePostSelect.htm)

Also, after clicking a command line option, turn off pre-selection, using `GetObject.EnablePreSelect`.  Otherwise, `GetObject.GetMultiple` will return with a `GetResult.Object` return code.

For example:

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'vb')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content" id="cs">

```cs
using System;
using Rhino;
using Rhino.Commands;
using Rhino.DocObjects;
using Rhino.Input;
using Rhino.Input.Custom;

...

protected override Result RunCommand(RhinoDoc doc, RunMode mode)
{
  const ObjectType geometryFilter = ObjectType.Surface | ObjectType.PolysrfFilter | ObjectType.Mesh;
  int integer1 = 300;
  int integer2 = 300;

  OptionInteger optionInteger1 = new OptionInteger(integer1, 200, 900);
  OptionInteger optionInteger2 = new OptionInteger(integer2, 200, 900);

  GetObject go = new GetObject();
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

  for (;;)
  {
    GetResult res = go.GetMultiple(1, 0);

    if (res == GetResult.Option)
    {
      go.EnablePreSelect(false, true);
      continue;
    }

    else if (res != GetResult.Object)
      return Result.Cancel;

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
    // Normally, pre-selected objects will remain selected, when a
    // command finishes, and post-selected objects will be unselected.
    // This this way of picking, it is possible to have a combination
    // of pre-selected and post-selected. So, to make sure everything
    // "looks the same", lets unselect everything before finishing
    // the command.
    for (int i = 0; i < go.ObjectCount; i++)
    {
      RhinoObject rhinoObject = go.Object(i).Object();
      if (null != rhinoObject)
        rhinoObject.Select(false);
    }
    doc.Views.Redraw();
  }

  int objectCount = go.ObjectCount;
  integer1 = optionInteger1.CurrentValue;
  integer2 = optionInteger2.CurrentValue;

  RhinoApp.WriteLine(string.Format("Select object count = {0}", objectCount));
  RhinoApp.WriteLine(string.Format("Value of integer1 = {0}", integer1));
  RhinoApp.WriteLine(string.Format("Value of integer2 = {0}", integer2));

  return Result.Success;
}

```

</div>

<div class="codetab-content" id="vb">

```vbnet
Imports Rhino
Imports Rhino.Commands
Imports Rhino.DocObjects
Imports Rhino.Input
Imports Rhino.Input.Custom

...

Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
  Const geometryFilter As ObjectType = ObjectType.Surface Or ObjectType.PolysrfFilter Or ObjectType.Mesh
  Dim integer1 As Integer = 300
  Dim integer2 As Integer = 300

  Dim optionInteger1 As New OptionInteger(integer1, 200, 900)
  Dim optionInteger2 As New OptionInteger(integer2, 200, 900)

  Dim go As New GetObject()
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

  While True
    Dim res As GetResult = go.GetMultiple(1, 0)

    If res = GetResult.[Option] Then
      go.EnablePreSelect(False, True)
      Continue While

    ElseIf res <> GetResult.[Object] Then
      Return Result.Cancel
    End If

    If go.ObjectsWerePreselected Then
      bHavePreselectedObjects = True
      go.EnablePreSelect(False, True)
      Continue While
    End If

    Exit While
  End While

  If bHavePreselectedObjects Then
    ' Normally, pre-selected objects will remain selected, when a
    ' command finishes, and post-selected objects will be unselected.
    ' This this way of picking, it is possible to have a combination
    ' of pre-selected and post-selected. So, to make sure everything
    ' "looks the same", lets unselect everything before finishing
    ' the command.
    For i As Integer = 0 To go.ObjectCount - 1
      Dim rhinoObject As RhinoObject = go.[Object](i).[Object]()
      If rhinoObject IsNot Nothing Then
        rhinoObject.[Select](False)
      End If
    Next
    doc.Views.Redraw()
  End If

  Dim objectCount As Integer = go.ObjectCount
  integer1 = optionInteger1.CurrentValue
  integer2 = optionInteger2.CurrentValue

  RhinoApp.WriteLine(String.Format("Select object count = {0}", objectCount))
  RhinoApp.WriteLine(String.Format("Value of integer1 = {0}", integer1))
  RhinoApp.WriteLine(String.Format("Value of integer2 = {0}", integer2))

  Return Result.Success
End Function
```

</div>
</div>

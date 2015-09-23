---
layout: toc-guide-page
title: Object Selection with Options
author: steve@mcneel.com
categories: ['Fundamentals']
platforms: ['Windows', 'Mac']
apis: ['RhinoCommon']
languages: ['C#']
keywords: ['RhinoCommon', 'Object', 'Selection', 'Options']
TODO: 0
origin: https://wiki.mcneel.com/developer/rhinocommonsamples/getobjectoption
order: 1
---

# Object Selection with Options

This guide covers how to pick some objects, select command options, return to picking more objects, all while keeping your current selection set.

## GetObject

RhinoCommon's [GetObject class]({{ site.baseurl }}/api/RhinoCommon/html/T_Rhino_Input_Custom_GetObject.htm) has a few properties and methods that you need to use, including:

- [GetObject.EnableClearObjectsOnEntry]({{ site.baseurl }}/api/RhinoCommon/html/M_Rhino_Input_Custom_GetObject_EnableClearObjectsOnEntry.htm)
- [GetObject.EnableUnselectObjectsOnExit]({{ site.baseurl }}/api/RhinoCommon/html/M_Rhino_Input_Custom_GetObject_EnableUnselectObjectsOnExit.htm)
- [GetObject.DeselectAllBeforePostSelect]({{ site.baseurl }}/api/RhinoCommon/html/P_Rhino_Input_Custom_GetObject_DeselectAllBeforePostSelect.htm)

Also, after clicking a command line option, turn off pre-selection, using `GetObject.EnablePreSelect`.  Otherwise, `GetObject.GetMultiple` will return with a `GetResult.Object` return code.

For example:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs" data-toggle="pill">C#</a></li>
  <li><a href="#vb" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

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
{: #cs .tab-pane .fade .in .active}

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
{: #vb .tab-pane .fade .in}

</div>

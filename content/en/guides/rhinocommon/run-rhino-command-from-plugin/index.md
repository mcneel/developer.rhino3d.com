+++
aliases = ["/en/en/5/guides/rhinocommon/run-rhino-command-from-plugin/", "/en/6/guides/rhinocommon/run-rhino-command-from-plugin/", "/en/7/guides/rhinocommon/run-rhino-command-from-plugin/", "/wip/guides/rhinocommon/run-rhino-command-from-plugin/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide covers the proper techniques when running a Rhino command from within the context of a plugin command."
keywords = [ "RhinoCommon", "Rhino", "Command", "Plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Run a Rhino command from a Plugin"
type = "guides"
weight = 1
override_last_modified = "2021-08-02T16:02:39Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/runrhinocommandfromplugincommand"
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

 
## The Problem

One of the most common questions asked by new plugin developers is how to run, or script, existing Rhino commands from a plugin command.  Rhino doesn't allow plugin commands to run other commands except under very special circumstances.

Here's the problem: If you have a command that is modifying the Rhino document, and you run another command, problems can happen.

To work around this, the RhinoCommon provides a special kind of command called a script command.  You can create a script command as follows...

## The Solution

When defining your command class, make sure to add the `ScriptRunner` command style attribute.  In other words, instead of defining your command classes like this:

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'vb1')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content1" id="cs1">

```cs
public class TestCommand : Rhino.Commands.Command

```

</div>

<div class="codetab-content1" id="vb1">

```vbnet
Public Class TestCommand
  Inherits Rhino.Commands.Command
```

</div>
</div>

Define your command classes like this:

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'vb2')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content2" id="cs2">

```cs
[Rhino.Commands.CommandStyle(Rhino.Commands.Style.ScriptRunner)]
public class TestCommand : Rhino.Commands.Command

```

</div>

<div class="codetab-content2" id="vb2">

```vbnet
<Rhino.Commands.CommandStyle(Rhino.Commands.Style.ScriptRunner)>
Public Class TestCommand
  Inherits Rhino.Commands.Command
```

</div>
</div>

Then, from within your command class's `RunCommand()` method, you can call `RhinoApp.RunScript()` to script the running of a Rhino command.  For example...

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'vb3')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content3" id="cs3">

```cs
protected override Rhino.Commands.Result RunCommand(Rhino.RhinoDoc doc, Rhino.Commands.RunMode mode)
{
  Rhino.RhinoApp.RunScript("_-Line 0,0,0 10,10,10", false);
  return Rhino.Commands.Result.Success;
}

```

</div>

<div class="codetab-content3" id="vb3">

```vbnet
Protected Overrides Function RunCommand(ByVal doc As Rhino.RhinoDoc, ByVal mode As Rhino.Commands.RunMode) As Rhino.Commands.Result
  Rhino.RhinoApp.RunScript("_-Line 0,0,0 10,10,10", False)
  Return Rhino.Commands.Result.Success
End Function
```

</div>
</div>

## Warnings

This kind of command can be very dangerous. Please be sure you understand the following:

1. If you are not very familiar with how references work, you should only call `Rhino.RhinoApp.RunScript()` from within a `RhinoScriptCommand` derived command.
1. If you are very familiar with references, then please observe the following rules:
   1. If you get a reference or pointer to any part of the Rhino run-time database, this reference or pointer will not be valid after you call `Rhino.RhinoApp.RunScript()`.
   1. If you get a reference or a pointer, then call `Rhino.RhinoApp.RunScript()`, and then use the reference, Rhino will probably crash.
   1. All pointers and references used by the command should be scoped such that they are only valid for the time between calls to `Rhino.RhinoApp.RunScript()`.

This is because `Rhino.RhinoApp.RunScript()` can change the dynamic arrays in the run-time database. The result is that all pointers and references become invalid. Be sure to scope your variables between `Rhino.RhinoApp.RunScript()` calls.

Never allow references and pointers from one section to be used in another section.

In a normal command, when the user enters a command beginning with a !, the command exits. There is no documented way to get this behavior from within a script command.

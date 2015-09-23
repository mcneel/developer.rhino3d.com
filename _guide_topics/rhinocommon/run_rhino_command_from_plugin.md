---
layout: toc-guide-page
title: Run a Rhino command from a Plugin
author: dale@mcneel.com
categories: ['Advanced']
platforms: ['Windows', 'Mac']
apis: ['RhinoCommon']
languages: ['C#']
keywords: ['RhinoCommon', 'Rhino', 'Command', 'Plugin']
TODO: 0
origin: http://wiki.mcneel.com/developer/runrhinocommandfromplugincommand
order: 1
---

# Rhino commands from a Plugin

This guide covers the proper techniques when running a Rhino command from within the context of a plugin command.

## The Problem

One of the most common questions asked by new plugin developers is how to run, or script, existing Rhino commands from a plugin command.  Rhino doesn't allow plugin commands to run other commands except under very special circumstances.

Here's the problem: If you have a command that is modifying the run-time database, and you run another command, problems can happen.

To work around this, the RhinoCommon provides a special kind of command called a script command.  You can create a script command as follows...

## The Solution

When defining your command class, make sure to add the `ScriptRunner` command style attribute.  In other words, instead of defining your command classes like this:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs1" data-toggle="pill">C#</a></li>
  <li><a href="#vb1" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">
```cs
[System.Runtime.InteropServices.Guid(<<test_command_guid>>)]
public class TestCommand : Rhino.Commands.Command
```
{: #cs1 .tab-pane .fade .in .active}

```vbnet
<System.Runtime.InteropServices.Guid(<<test_command_guid>>)> _
Public Class TestCommand
  Inherits Rhino.Commands.Command
```
{: #vb1 .tab-pane .fade .in}

</div>

Define your command classes like this:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs2" data-toggle="pill">C#</a></li>
  <li><a href="#vb2" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">
```cs
[
 System.Runtime.InteropServices.Guid(<<test_command_guid>>),
 Rhino.Commands.CommandStyle(Rhino.Commands.Style.ScriptRunner)
]
public class TestCommand : Rhino.Commands.Command
```
{: #cs2 .tab-pane .fade .in .active}

```vbnet
< _
  System.Runtime.InteropServices.Guid(<<test_command_guid>>), _
  Rhino.Commands.CommandStyle(Rhino.Commands.Style.ScriptRunner) _
> _
Public Class TestCommand
  Inherits Rhino.Commands.Command
```
{: #vb2 .tab-pane .fade .in}

</div>

Then, from within your command class's `RunCommand()` method, you can call `RhinoApp.RunScript()` to script the running of a Rhino command.  For example...

<ul class="nav nav-pills">
  <li class="active"><a href="#cs3" data-toggle="pill">C#</a></li>
  <li><a href="#vb3" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">
```cs
protected override Rhino.Commands.Result RunCommand(Rhino.RhinoDoc doc, Rhino.Commands.RunMode mode)
{
  Rhino.RhinoApp.RunScript("_-Line 0,0,0 10,10,10", false);
  return Rhino.Commands.Result.Success;
}
```
{: #cs3 .tab-pane .fade .in .active}

```vbnet
Protected Overrides Function RunCommand(ByVal doc As Rhino.RhinoDoc, ByVal mode As Rhino.Commands.RunMode) As Rhino.Commands.Result
  Rhino.RhinoApp.RunScript("_-Line 0,0,0 10,10,10", False)
  Return Rhino.Commands.Result.Success
End Function
```
{: #vb3 .tab-pane .fade .in}

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

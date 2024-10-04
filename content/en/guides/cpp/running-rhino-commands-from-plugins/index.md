+++
aliases = ["/en/5/guides/cpp/running-rhino-commands-from-plugins/", "/en/6/guides/cpp/running-rhino-commands-from-plugins/", "/en/7/guides/cpp/running-rhino-commands-from-plugins/", "/wip/guides/cpp/running-rhino-commands-from-plugins/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses the proper techniques to use when running a Rhino command from within the context of a C/C++ plugin command."
keywords = [ "rhino", "commands" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Running Rhino Commands from Plugins"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/runrhinocommandfromplugincommand"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Overview

One of the most common questions asked by new plugin developers is how to run, or script, existing Rhino commands from a plugin command.  Rhino doesn't allow plugin commands to run other commands except under very special circumstances.

Here's the issue: If you have a command that is modifying the run-time database, and you run another command, problems can happen.

To work around this, the Rhino C/C++ SDK provides a special kind of command called a script command.  You can create a script command as follows...

## How To

Derive your command class from CRhinoScriptCommand instead of CRhinoCommand. In other words, instead of defining your command class like this:

```cpp
class CCommandTest : public CRhinoCommand
```

Define your command class like this:

```cpp
class CCommandTest : public CRhinoScriptCommand
```

Then, from within your command class's `RunCommand()` member, you can call `CRhinoApp::RunScript()` to script the running of a Rhino command.  For example:

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  RhinoApp().RunScript( L"_-Line 0,0,0 10,10,10", 0 );
  return CRhinoCommand::success;
}
```

## Warning

This kind of command can be very dangerous.  Please be sure you understand the following:

1. If you are not very familiar with how C++ references work, you should only call `CRhinoApp::RunScript()` from within a `CRhinoScriptCommand` derived command.
1. If you are very familiar with C++ references, then please observe the following rules:
    1. If you get a reference or pointer to any part of the Rhino run-time database, this reference or pointer will not be valid after you call `CRhinoApp::RunScript()`.
    1. If you get a reference or a pointer, then call `CRhinoApp::RunScript()`, and then use the reference, Rhino will probably crash.
    1. All pointers and references used by the command should be scoped such that they are only valid for the time between calls to `CRhinoApp::RunScript()`.

This is because `CRhinoApp::RunScript()` can change the dynamic arrays in the run-time database.  The result is that all pointers and references become invalid. Be sure to scope your variables between `CRhinoApp::RunScript()` calls.

**NOTE**: In a normal command, when the user enters a command beginning with a !, the command exits. There is no documented way to get this behavior from within a script command.

## Sample

Here's good scoping practice when your command is a script command.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  {
    section A
    ... do some stuff ...
  }
  RhinoApp().RunScript(...);
  {
    section B
    ... do some stuff ...
  }
  RhinoApp().RunScript(...);
  {
    section C
    ... do some stuff ...
  }
  RhinoApp().RunScript(...);
  {
    section D
    ... do some stuff ...
  }
  RhinoApp().RunScript(...);
  {
    section E
    ... do some stuff ...
  }
  return CRhinoCommand::success;
}
```

Never allow references and pointers from one section to be used in another section.

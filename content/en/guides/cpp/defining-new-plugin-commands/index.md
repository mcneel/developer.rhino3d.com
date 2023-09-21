+++
aliases = ["/5/guides/cpp/defining-new-plugin-commands/", "/6/guides/cpp/defining-new-plugin-commands/", "/7/guides/cpp/defining-new-plugin-commands/", "/wip/guides/cpp/defining-new-plugin-commands/"]
authors = [ "dale" ]
categories = [ "Getting Started" ]
description = "This guide discusses Rhino commands and how define new commands using C/C++."
keywords = [ "rhino", "commands" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Defining New Plugin Commands"
type = "guides"
weight = 3

[admin]
TODO = "needs to be reviewed for accuracy and considered for consolidation with other plugin topics"
origin = "http://wiki.mcneel.com/developer/sdksamples/addcommand"
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

Rhino plugins can contain any number of commands. Commands are created by deriving a new class from `CRhinoCommand`.  See *rhinoSdkCommand.h* for details on the `CRhinoCommand` class.

Command classes must return a unique *GUID*. If you try to use a *GUID* that is already in use, then your command will not work.  Use the *GUIDGEN.EXE* utility, that comes with Visual Studio, to create unique *GUIDs*.

Command classes must return a unique command name. If you try to use a command name that is already in use, then your command will not work.

Only ONE instance of a command class can be created. This is why you should put the definition of your command classes in *.cpp* files.

## Rhino 8

The **[Rhino Visual Studio Extension](https://github.com/mcneel/RhinoVisualStudioExtensions/releases)**, for the Rhino 8 C/C++ SDK, includes a template that lets you quickly add new commands to your plugin project.

To add a new Rhino command to your plugin project, right-click on the *Source Files* folder, in *Visual Studio’s Solution Explorer*, and click *Add > New Item...*. From the *Add New Item* dialog, select *Empty Command for Rhino 3D (C++)*, specify the name of the command, and click *Add*.

![Add New Item](/images/defining-new-plugin-commands-cpp.png)

## Rhino 7

The *Rhino Command Generator* wizard, included with the Rhino 7 C/C++ SDK, is a standalone application that will generate new skeleton `CRhinoCommand`-derived class. The generated source code is copied to the Windows clipboard so you can easily paste it into your source files.

To use this tool in Visual Studio:

1. Launch Visual Studio.
2. Navigate to *Tools* > *External Tools...*.
3. Use the *Add* button to add the *RhinoCommandGenerator.exe* file to the list.  The file can be found in the following location: *C:\\Program Files\\Rhino 7.0 SDK\\Wizards\\Command*

![Rhino Command Generator](/images/your-first-plugin-windows-cpp-08.png)

Once the tool is installed, you can create a new command by selecting *Tools* > *Rhino Command*. If you add the command declaration to a new *.cpp* file, be sure to `#include "stdafx.h"` at the top.

## Sample

The following sample code demonstrates a simple command class that essentially does nothing:

```cpp
// Do NOT put the definition of class CCommandTest in a header
// file. There is only ONE instance of a CCommandTest class
// and that instance is the static theTestCommand that appears
// immediately below the class definition.

class CCommandTest : public CRhinoCommand
{
public:
  // The one and only instance of CCommandTest is created below.
  // No copy constructor or operator= is required.
  // Values of member variables persist for the duration of the application.

  // CCommandTest::CCommandTest()
  // is called exactly once when static theTestCommand is created.
  CCommandTest() = default;

  // CCommandTest::~CCommandTest()
  // is called exactly once when static theTestCommand is destroyed.
  // The destructor should not make any calls to the Rhino SDK. 
  // If your command has persistent settings, then override 
  // CRhinoCommand::SaveProfile and CRhinoCommand::LoadProfile.
  ~CCommandTest() = default;

  // Returns a unique UUID for this command.
  // If you try to use an id that is already being used, then
  // your command will not work. Use GUIDGEN.EXE to make unique UUID.
  UUID CommandUUID() override
  {
    // {F502C783-C0CE-4118-8869-EFB0CB34CCCB}
    static const GUID TestCommand_UUID =
    { 0xF502C783, 0xC0CE, 0x4118, { 0x88, 0x69, 0xEF, 0xB0, 0xCB, 0x34, 0xCC, 0xCB } };
    return TestCommand_UUID;
  }

  // Returns the English command name.
  // If you want to provide a localized command name, then override 
  // CRhinoCommand::LocalCommandName.
  const wchar_t* EnglishCommandName() override { return L"Test"; }

  // Rhino calls RunCommand to run the command.
  CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
};

// The one and only CCommandTest object
// Do NOT create any other instance of a CCommandTest class.
static class CCommandTest theTestCommand;

CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  // CCommandTest::RunCommand() is called when the user
  // runs the "Test".

  // TODO: Add command code here.

  // Rhino command that display a dialog box interface should also support
  // a command-line, or scriptable interface.

  ON_wString str;
  str.Format(L"The \"%s\" command is under construction.\n", EnglishCommandName());
  if (context.IsInteractive())
    RhinoMessageBox(str, TestPlugIn().PlugInName(), MB_OK);
  else
    RhinoApp().Print(str);

  // TODO: Return one of the following values:
  //   CRhinoCommand::success:  The command worked.
  //   CRhinoCommand::failure:  The command failed because of invalid input, inability
  //                            to compute the desired result, or some other reason.
  //   CRhinoCommand::cancel:   The user interactively canceled the command 
  //                            (by pressing ESCAPE, clicking a CANCEL button, etc.)
  //                            in a Get operation, dialog, time consuming computation, etc.

  return CRhinoCommand::success;
}
```

---
title: Defining New Plugin Commands
description: This guide discusses Rhino commands and how define new commands using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/sdksamples/addcommand
order: 5
keywords: ['rhino', 'commands']
layout: toc-guide-page
TODO: 'needs to be reviewed for accuracy and considered for consolidation with other plugin topics'
---

 
## Overview

Rhino plugins can contain any number of commands.  Commands are created by deriving a new class from `CRhinoCommand`.  See *rhinoSdkCommand.h* for details on the `CRhinoCommand` class.

Command classes must return a unique *UUID*.  If you try to use a *UUID* that is already in use, then your command will not work.  Use the *GUIDGEN.EXE* that comes with Visual Studio to create unique *UUIDs*.

Command classes must return a unique command name.  If you try to use a command name that is already in use, then your command will not work.

Only ONE instance of a command class can be created.  This is why you should put the definition of your command classes in *.cpp* files.

## Rhino Command Generator

The *Rhino Command Generator* wizard is a standalone application that will generate new skeleton `CRhinoCommand`-derived class.  The generated source code is copied to the Windows clipboard so you can easily paste it into your source files.

To use this tool in Visual Studio 2010:

1. Launch Visual Studio.
1. Navigate to *Tools* > *External Tools...*
1. Use the Add button to add the *RhinoCommandGenerator.exe* file to the list.  This file can be found in the following folder: *C:\\Program Files\\Rhino 5.0 x64 SDK\\Wizards\\Command*.

Once the tool is installed, you can create a new command by selecting *Tools* > *Rhino Command*. If you add the command declaration to a new header file, be sure to `#include "stdafx.h"` at the top.

## Sample

The following sample code demonstrates a simple command class that essentially does nothing...

```cpp
// Do NOT put the definition of class CCommandTest in a header
// file.  There is only ONE instance of a CCommandTest class
// and that instance is the static theTestCommand that appears
// immediately below the class definition.

class CCommandTest : public CRhinoCommand
{
public:
  // The one and only instance of CCommandTest is created below.
  // No copy constructor or operator= is required.  Values of
  // member variables persist for the duration of the application.

  // CCommandTest::CCommandTest()
  // is called exactly once when static theTestCommand is created.
  CCommandTest() {}

  // CCommandTest::~CCommandTest()
  // is called exactly once when static theTestCommand is
  // destroyed.  The destructor should not make any calls to
  // the Rhino SDK.  If your command has persistent settings,
  // then override CRhinoCommand::SaveProfile and CRhinoCommand::LoadProfile.
  ~CCommandTest() {}

  // Returns a unique UUID for this command.
  // If you try to use an id that is already being used, then
  // your command will not work.  Use GUIDGEN.EXE to make unique UUID.
  UUID CommandUUID()
  {
    // {5333C9DE-5F01-45B8-9154-28B765E453E0}
    static const GUID TestCommand_UUID =
    { 0x5333C9DE, 0x5F01, 0x45B8, { 0x91, 0x54, 0x28, 0xB7, 0x65, 0xE4, 0x53, 0xE0 } };
    return TestCommand_UUID;
  }

  // Returns the English command name.
  const wchar_t* EnglishCommandName() { return L"Test"; }

  // Returns the localized command name.
  const wchar_t* LocalCommandName() { return L"Test"; }

  // Rhino calls RunCommand to run the command.
  CRhinoCommand::result RunCommand( const CRhinoCommandContext& );
};

// The one and only CCommandTest object.  
// Do NOT create any other instance of a CCommandTest class.
static class CCommandTest theTestCommand;

CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // CCommandTest::RunCommand() is called when the user runs the "Test"
  // command or the "Test" command is run by a history operation.

  // TODO: Add command code here.

  // Rhino command that display a dialog box interface should also support
  // a command-line, or scriptable interface.

  ON_wString wStr;
  wStr.Format( L"The \"%s\" command is under construction.\n", EnglishCommandName() );
  if( context.IsInteractive() )
    RhinoMessageBox( wStr, PlugIn()->PlugInName(), MB_OK );
  else
    RhinoApp().Print( wStr );

  // TODO: Return one of the following values:
  //   CRhinoCommand::success:  The command worked.
  //   CRhinoCommand::failure:  The command failed because of invalid input, inability
  //                            to compute the desired result, or some other reason
  //                            computation reason.
  //   CRhinoCommand::cancel:   The user interactively canceled the command
  //                            (by pressing ESCAPE, clicking a CANCEL button, etc.)
  //                            in a Get operation, dialog, time consuming computation, etc.
  //   CRhinoCommand::nothing:  The command did nothing but CANCEL was not pressed.

  return CRhinoCommand::success;
}
```

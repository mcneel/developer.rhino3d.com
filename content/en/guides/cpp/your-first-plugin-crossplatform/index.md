+++
aliases = []
authors = [ "callum" ]
categories = [ "Getting Started" ]
description = "This guide walks you through your first plugin for Rhino for Windows using C/C++ and Visual Studio."
keywords = [ "c", "C/C++", "plugin" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Creating your first C/C++ plugin (Cross Platform)"
type = "guides"
weight = 2

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

It is presumed you already have the necessary tools installed and are ready to go. If you are not there yet, see:
- [Installing Tools (Windows)](/guides/cpp/installing-tools-windows).
- [Installing Tools (Mac)](/guides/cpp/installing-tools-mac).

## Bare bones plugin

1. Use git to clone the starter repo
`git clone https://github.com/mcneel/CrossPlatformCppPlugin`
1. Download the SDK
`git submodule update --init`
1. Run the rename`./rename.sh` or `powershell -ExecutionPolicy Bypass -File ./rename.ps1` script to fill out the plugin, command, properties and GUIDs correctly. For this tutorial, it is suggested to use all of the default values.

### Plugin Anatomy

The following files are of interest:

| File             | Platform | Description                                                                       |
| :--------------- | :------- | :-------------------------------------------------------------------------------- |
| Sample.vcxproj   | Windows  | Project file that allows Visual C++ to build your plugin.                         |
| stdafx.h         | Windows  | Main project header.                                                              |
| stdafx.cpp       | Windows  | Used to generate the precompiled header.                                          |
| SampleApp.h      | Both     | Application class header that contains the `CSampleApp` class declaration.        |
| SampleApp.cpp    | Both     | Application class implementation that contains the `CSampleApp` member functions. |
| SamplePlugIn.h   | Both     | Plugin class header that contains the `CSamplePlugIn` class declaration.          |
| SamplePlugIn.cpp | Both     | Plugin class implementation that contains the `CSamplePlugIn` member functions.   |
| cmdSample.cpp    | Both     | Initial Rhino command.                                                            |
| Resource.h       | Windows  | #define constant definitions for resources.                                       |
| Sample.rc        | Windows  | Resource script.                                                                  |
| Sample.rc2       | Windows  | Resource script.                                                                  |
| Sample.def       | Windows  | Module definition.                                                                |
| Sample.ico       | Windows  | Plugin icon.                                                                      |
| targetver.h      | Windows  | Defines the supported Windows platform.                                           |

### Getting up and Running

#### Windows

1. Run the rename script `powershell -ExecutionPolicy Bypass -File ./rename.ps1` to fill out the plugin, command, properties and GUIDs correctly. For this tutorial, it is suggested to use all of the default values.
1. Double click the `MySamplePlugIn.sln` file in the `win` directory
1. In *Visual Studio* click *Local Windows Debugger* next to the green arrow. This will load Rhino and the plug-in

![Rhino Options](/images/your-first-plugin-windows-cpp-10.png)

1. For this guide, build the *Debug* configuration.
1. From within Rhino, navigate to *Tools* > *Options*. Navigate to the *Plugins* page under *Rhino Options* and install your plugin (it will be in the win/x64/Debug folder)

    ![Rhino Options](/images/your-first-plugin-windows-cpp-07.png)
1. Run MySampleCommand, a message box should appear

![Rhino Options](/images/your-first-plugin-windows-cpp-09.png)

1. You have finished creating your first plugin!

#### Mac

1. Run the rename script `./rename.sh` to fill out the plugin, command, properties and GUIDs correctly. For this tutorial, it is suggested to use all of the default values.
1. Open `osx/MySamplePlugIn.xcodeproj` in XCode.
1. Click the Run button, *project* > *run*. This will load Rhino and the plugin.
![Rhino Options](/images/your-first-plugin-mac-cpp-01.png)

1. Run MySampleCommand, a message box should appear
![Rhino Options](/images/your-first-plugin-mac-cpp-02.png)

1. You have finished creating your first plugin!

## Adding Additional Commands

Rhino plugins can contain any number of commands. Commands are created by deriving a new class from `CRhinoCommand`. See *rhinoSdkCommand.h* for details on the `CRhinoCommand` class.

### Example

The following example code demonstrates a simple command class that essentially does nothing:

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
  //                            to compute the desired result, or some other reason
  //   CRhinoCommand::cancel:   The user interactively canceled the command
  //                            (by pressing ESCAPE, clicking a CANCEL button, etc.)
  //                            in a Get operation, dialog, time consuming computation, etc.

  return CRhinoCommand::success;
}
```

### Notes

A couple things to consider:

1. Command classes must return a unique UUID.  If you try to use a UUID that is already in use, then your command will not work.  To create a unique UUID, use *GUIDGEN.EXE* (which ships with *Visual Studio*) on Windows, or run `uuidgen` from the *Terminal* on macOS.
2. Command classes must return a unique command name.  If you try to use a command name that is already in use, then your command will not work.
3. Only ONE instance of a command class can be created.  This is why you should put the definition of your command classes in *.cpp* files.

## Related Topics

- [What is a Rhino Plugin?](/guides/general/what-is-a-rhino-plugin)

---
title: Migrate your plugin project to Rhino 6
description: This guide walks you through migrating your plugin project to Rhino 6.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
order: 6
keywords: ['c', 'C/C++', 'plugin']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Windows)]({{ site.baseurl }}/guides/cpp/installing_tools_windows).

## Migrate the project

1. Launch *Visual Studio 2015* and navigate to *File* > *Open* > *Project/Solution...*.
1. Navigate to your project's folder and open either your plugin project *(.vcxproj)* or solution *(.sln)*
1. When your plugin project opens, navigate to the project's setting by clicking *Project* > *[ProjectName] Properties...*.
1. In the project's settings, select *All Configurations* and set the platform to *x64*. Then, set the *Platform Toolset* to *Visual Studio 2015 (v140)* and the click *Apply*.
![Plugin Settings]({{ site.baseurl }}/images/migrate_plugin_windows_cpp.png)

### Plugin Anatomy

The following files are of interest:

1. *Test.vcxproj* is the project file that allows Visual C++ to build your plugin.
1. *stdafx.h* is the main project header.
1. *stdafx.cpp* is used to generate precompiled header.
1. *TestApp.h* is the application class header that contains the `CTestApp` class declaration.
1. *TestApp.cpp* is the application class implementation that contains the `CTestApp` member functions.
1. *TestPlugIn.h* is the plugin class header that contains the `CTestPlugIn` class declaration.
1. *TestPlugIn.cpp* is the plugin class implementation that contains the `CTestPlugIn` member functions.
1. *cmdTest.cpp* is the sample `Test` Rhino command.
1. *Resource.h* is the `#define` constant definitions for resources.
1. *Test.rc* is the resource script.
1. *Test.def* is the module definition.
1. *targetver.h* is used to define the support Windows platform.

### Project Settings

With *Visual Studio 2015*, you can view a project's setting by clicking *Project* > *[ProjectName] Properties...*.

![Test Property Pages]({{ site.baseurl }}/images/your_first_plugin_windows_cpp_04.png)

Reviewing the above settings, you can see that, unlike Rhino 5 plugin projects, there is no 32-bit platform.  This is because Rhino 6 is only available as a 64-bit application.

### Property Sheets
Visual Studio projects have hundreds of compiler switches and options to choose from. Using custom [Project Property Sheets](https://msdn.microsoft.com/en-us/library/669zx6zc.aspx) is a convenient way to synchronize or share these common settings among other projects. 

The Plugin Wizard, used to generate the plugin project, adds Rhino plugin-specific property sheets to the project.  To view these propety sheets, click *View* > *Property Manager*.

![Test Property Manager]({{ site.baseurl }}/images/your_first_plugin_windows_cpp_06.png)

### Boilerplate Build

The *Rhino Plugin Wizard*, in addition to generating code, creates a custom project file for your plugin.  This file, *Test.vcxproj*, specifies all of the file dependencies together with the compile and link option flags.

Before we can build our project, we need to fill in the Rhino plugin developer declarations.  These declarations will let the user of our plugin know who produced the plugin and where they can support information if needed.  

1. Open *TestPlugIn.cpp* and modify the following lines of code, providing your company name and other support information:

        RHINO_PLUG_IN_DEVELOPER_ORGANIZATION(L"My Company Name");
        RHINO_PLUG_IN_DEVELOPER_ADDRESS(L"123 Developer Street\r\nCity State 12345-6789");
        RHINO_PLUG_IN_DEVELOPER_COUNTRY(L"My Country");
        RHINO_PLUG_IN_DEVELOPER_PHONE(L"123.456.7890");
        RHINO_PLUG_IN_DEVELOPER_FAX(L"123.456.7891");
        RHINO_PLUG_IN_DEVELOPER_EMAIL(L"support@mycompany.com");
        RHINO_PLUG_IN_DEVELOPER_WEBSITE(L"http://www.mycompany.com");
        RHINO_PLUG_IN_UPDATE_URL(L"http://www.mycompany.com/support");
1. When finished, delete the following line of source code as the `#error` directive will prevent the project from building:

        #error Developer declarations block is incomplete!
1. *NOTE*: If you do not delete this line, the plugin will build.  You are now ready to build the project by picking *Build Test* from the *Build* menu. If the build was successful, a plugin file named *Test.rhp* is created in the project’s *Debug* folder.

### Testing

1. From *Visual Studio*, navigate to *Debug* > *Start Debugging*.  This will load Rhino.  The version of Rhino that is launched depends on the configuration that you build.  The wizard adds the following configurations to your project:
     - *Debug*: The *Debug* project is a *Release* project that disables optimizations and generates debugging information using the compiler’s *Program Database* (`/Zi`) option and the linker’s *Generate Debug Information* (`/DEBUG`) option.  These option settings let you use the debugger while you are developing your custom plugin. The *PseudoDebug* configuration also links with release runtime libraries.  Plugins built with the *PseudoDebug* configuration will only load in the release version of Rhino that was installed with Rhino.
     - *Release*: The *Release* configuration of your program contains no symbolic debug information and is fully optimized.  *Debug* information can be generated in PDB Files (C++) depending on the compiler options used.  Creating PDB files can be very useful if you later need to debug your release version.  The *Release* configuration also links with release runtime libraries.  Plugins built with the *Release* configuration will only load in the release version of Rhino that was installed with Rhino.
     - *DebugRhino*: The DebugRhino configuration of your program is compiled with full symbolic debug information and no optimization.  Optimization complicates debugging, because the relationship between source code and generated instructions is more complex.  The *DebugRhino* configuration also links with debug runtime libraries.  Plugins built with the *DebugRhino* configuration will only load in the debug version of Rhino included with the Rhino C/C++ SDK.
1. For this guide, build the *Debug* configuration.
1. From within Rhino, navigate to *Tools* > *Options*.  Navigate to the *Plugins* page under *Rhino Options* and install your plugin. 
![Rhino Options]({{ site.baseurl }}/images/your_first_plugin_windows_cpp_05.png)
1. Once your plugin is loaded, close the options dialog and run your `Test` command.  You have finished creating your first plugin!

## Adding Additional Commands

Rhino plugins can contain any number of commands.  Commands are created by deriving a new class from `CRhinoCommand`.  See *rhinoSdkCommand.h* for details on the `CRhinoCommand` class.

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

1. Command classes must return a unique UUID.  If you try to use a UUID that is already in use, then your command will not work.  Use the *GUIDGEN.EXE* that comes with *Visual Studio* to create unique UUIDs.
1. Command classes must return a unique command name.  If you try to use a command name that is already in use, then your command will not work.
1. Only ONE instance of a command class can be created.  This is why you should put the definition of your command classes in *.cpp* files.

### Rhino Command Generator

The *Rhino Command Generator* wizard is a standalone application that will generate new skeleton `CRhinoCommand`-derived class.  The generated source code is copied to the Windows clipboard so you can easily paste it into your source files.

To use this tool in Visual Studio 2015:

1. Launch Visual Studio 2015.
1. Navigate to *Tools* > *External Tools...*.
1. Use the *Add* button to add the *RhinoCommandGenerator.exe* file to the list.  The file can be found in the following location: *C:\\Program Files\\Rhino 6.0 SDK\\Wizards\\Command*
![Rhino Command Generator]({{ site.baseurl }}/images/your_first_plugin_windows_cpp_07.png)
---

## Related Topics

- [What is a Rhino Plugin?]({{ site.baseurl }}/guides/general/what_is_a_rhino_plugin)
- [Installing Tools (Windows)]({{ site.baseurl }}/guides/cpp/installing_tools_windows)

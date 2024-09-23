+++
aliases = ["/5/guides/rhinocommon/your-first-plugin-windows/", "/6/guides/rhinocommon/your-first-plugin-windows/", "/7/guides/rhinocommon/your-first-plugin-windows/", "/wip/guides/rhinocommon/your-first-plugin-windows/"]
authors = [ "dan", "callum" ]
categories = [ "Getting Started" ]
description = "This guide walks you through your first plugin for Rhino for Windows using RhinoCommon and Visual Studio."
keywords = [ "first", "RhinoCommon", "Plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Your First Plugin (Windows)"
type = "guides"
weight = 3
thumbnail = "/images/dev-logo-grasshopper-small.png"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addcommand"
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

It is presumed you already have the necessary tools installed and are ready to go. If you are not there yet, see [Installing Tools (Windows)](/guides/rhinocommon/installing-tools-windows).

## Barebones plugin

We will use the _RhinoCommon Plugin for Rhino 3D (C#)_ project template to create a new general purpose plugin. The project template generates the code for a functioning plugin. Follow these steps to build the plugin.

### Plugin Template

1. Launch _Visual Studio_ and navigate to _File_ > _New_ > _Project..._.
2. From the _Create a new project_ dialog, select the _RhinoCommon Plugin for Rhino 3D (C#)_ template from the list of installed templates and click _Next_.

   ![New Project Template](/images/your-first-plugin-windows-01.png)

3. Type the project name as shown below. You can enter a different name if you want. The template uses the project name when it creates files and classes. If you enter a different name, your files and classes will have a name different from that of the files and classes mentioned in this tutorial. Don’t forget to choose a location to store the project. When finished, click _Create_.

   ![New Project Configure](/images/your-first-plugin-windows-02.png)

4. Upon clicking _Create_, the _New Rhino C# Plugin_ dialog will appear. By default, the template will create a _General Utility_ plugin.

   ![Plugin Settings](/images/your-first-plugin-windows-03.png)

5. The _New RhinoCommon .NET Plugin_ dialog allows you to modify a number of settings used by the template when generating the plugin source code:
   1. **Plugin name**: Modify this field if you want to change the name of the plugin's class name.
   1. **Command class name:**: Modify this field if you want to change the name of the plugin's initial command class name.
   1. **Plugin type**: Select the [type of plugin](/guides/general/what-is-a-rhino-plugin) that you want the template to create.
   1. **Minimum Target Version**: Select the lowest Rhino version to target.
   1. **Build Yak Package**: Toggle true to have Rhino build a Yak package automatically from your project
   1. **Include VS Code launch/tasks json files**: Includes `.vscode` folder so the plugin can be debugged in VSCode as well (Very handy for Mac).
   1. **Wndows UI**: If you are planning on using Windows Forms or WPF for user interface, instead of Eto, then check the approprate box.
6. For this tutorial, just accept the default settings. Click the _Finish_ button, and the template begins to generate your plugin project’s folders, files, and classes. When the template is finished, look through the plugin project using _Visual Studio’s Solution Explorer_...

### Plugin Anatomy

Use the _Solution Explorer_ to expand the _Solution_ (_.sln_) so that it looks like this.

![Plugin Anatomy](/images/your-first-plugin-windows-04.png)

1. **HelloRhinoCommon**: The plugin project (_.csproj_), which has the same name as its parent solution. The project that was created for us by the project template we just used.
1. **Dependencies**: Contains references to both the .NET Framework 4.8 and .NET 7.0 assemblies required by the plugin. The project obtains RhinoCommon dependencies via [NuGet](https://www.nuget.org/packages/rhinocommon).
1. **Properties**: Contains the _AssemblyInfo.cs_ source file. This file contains the meta-data, such as author and copyright, that appears in Rhino's [Plugin Manager](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#options/plug-ins.htm).
1. **Embedded Resources**: Contains icons, bitmaps, and other non-code resources you want embedded in your plugin.
1. **HelloRhinoCommonCommand.cs**: The initial plugin command, which inherits from `Rhino.Commands.Command`.
1. **HelloRhinoCommonPlugin.cs**: The plugin class, which inherits from `Rhino.Plugins.Plugin`.

### Testing

1. From _Visual Studio_, navigate to _Debug_ > _Start Debugging_. You can also press _F5_, or click the _Debug_ button on Visual Studio's toolbar. This will load Rhino.
1. From within Rhino, navigate to _Tools_ > _Options_. Navigate to the _Plugins_ page under _Rhino Options_ and install your plugin.

   ![Rhino Options](/images/your-first-plugin-windows-05.png)

1. Once your plugin is loaded, close the options dialog and run your _HelloRhinoCommonCommand_ command.
1. You have finished creating your first plugin!

## Adding Additional Commands

Rhino plugins can contain any number of commands. Commands are created by inheriting a new class from `Rhino.Commands.Command`.

Note, Command classes must return a unique command name. If you try to use a command name that is already in use, then your command will not work.

To add a new Rhino command to your plugin project, right-click on the project, in Visual Studio’s Solution Explorer, and click Add > New Item…. From the Add New Item dialog, select _Empty RhinoCommon Command for Rhino 3D (C++)_, specify the name of the command, and click _Add_.

![Rhino Command](/images/your-first-plugin-windows-06.png)

### Example

The following example code demonstrates a simple command class that essentially does nothing:

```cs
using Rhino;
using Rhino.Commands;
using Rhino.Geometry;
using Rhino.Input;
using Rhino.Input.Custom;

namespace HelloRhinoCommon
{
  public class HelloRhinoCommonCommand : Command
  {
    public HelloRhinoCommonCommand()
    {
      // Rhino only creates one instance of each command class defined in a
      // plug-in, so it is safe to store a refence in a static property.
      Instance = this;
    }

    ///<summary>The only instance of this command.</summary>
    public static HelloRhinoCommonCommand Instance { get; private set; }

    ///<returns>The command name as it appears on the Rhino command line.</returns>
    public override string EnglishName => "HelloRhinoCommonCommand";

    protected override Result RunCommand(RhinoDoc doc, RunMode mode)
    {
      // TODO: start here modifying the behaviour of your command.
      // ---
      RhinoApp.WriteLine("The {0} command will add a line right now.", EnglishName);

      Point3d pt0;
      using (GetPoint getPointAction = new GetPoint())
      {
        getPointAction.SetCommandPrompt("Please select the start point");
        if (getPointAction.Get() != GetResult.Point)
        {
          RhinoApp.WriteLine("No start point was selected.");
          return getPointAction.CommandResult();
        }
        pt0 = getPointAction.Point();
      }

      Point3d pt1;
      using (GetPoint getPointAction = new GetPoint())
      {
        getPointAction.SetCommandPrompt("Please select the end point");
        getPointAction.SetBasePoint(pt0, true);
        getPointAction.DynamicDraw +=
          (sender, e) => e.Display.DrawLine(pt0, e.CurrentPoint, System.Drawing.Color.DarkRed);
        if (getPointAction.Get() != GetResult.Point)
        {
          RhinoApp.WriteLine("No end point was selected.");
          return getPointAction.CommandResult();
        }
        pt1 = getPointAction.Point();
      }

      doc.Objects.AddLine(pt0, pt1);
      doc.Views.Redraw();
      RhinoApp.WriteLine("The {0} command added one line to the document.", EnglishName);

      // ---
      return Result.Success;
    }
  }
}
```

## Next Steps

If you want to make your new Plugin Cross Platform, check out the [Your First Plugin (Cross Platform)](/guides/rhinocommon/your-first-plugin-crossplatform) guide.

If you'd like to push your exciting new plugin to Yak so that everyone can use it, check out the [Creating a Yak Package](/guides/yak/creating-a-rhino-plugin-package/) guide.

## Related topics

- [Installing Tools (Windows)](/guides/rhinocommon/installing-tools-windows)
- [Your First Plugin (Cross-Platform)](/guides/rhinocommon/your-first-plugin-crossplatform)

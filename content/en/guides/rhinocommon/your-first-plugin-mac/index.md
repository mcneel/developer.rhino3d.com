+++
aliases = ["/5/guides/rhinocommon/your-first-plugin-mac/", "/6/guides/rhinocommon/your-first-plugin-mac/", "/7/guides/rhinocommon/your-first-plugin-mac/", "/wip/guides/rhinocommon/your-first-plugin-mac/"]
authors = [ "dan", "callum" ]
categories = [ "Getting Started" ]
description = "This guide walks you through your first plugin for Rhino for Mac using RhinoCommon and Visual Studio Code."
keywords = [ "first", "RhinoCommon", "Plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Your First Plugin (Mac)"
type = "guides"
weight = 4

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


It is presumed you already have the necessary tools installed and are ready to go. If you are not there yet, see [Installing Tools (Mac)](/guides/rhinocommon/installing-tools-mac).

## HelloRhinoCommon

We will use Visual Studio Code to create a new, basic, command plugin called HelloRhinoCommon.

We are presuming you are new to Visual Studio Code, so we'll go through this one step at a time.

### Download the required template

1. Launch Visual Studio Code.
1. Open *Visual Studio Code's Terminal* via *Terminal (menu entry)* > *New Terminal*, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Inside Terminal, run:
    ``` pwsh
    dotnet new install Rhino.Templates
    ```

### Starting the Project

1. Create a folder on your mac where you would like your project to live. Name the folder `HelloRhinoCommon`.
1. If you have not done so already, *launch Visual Studio Code*.
1. Now we can open our new folder, navigate to *File* > *Open Folder* and choose the folder we just created.
1. Open Terminal via *Terminal* > *New Terminal*, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Enter the following command into the Terminal:
   ```pwsh
   dotnet new rhino --version 8 -sample
   ```
1. In our Folder explorer, we should see the project appear as Visual Studio Code discovers the files.
1. Expand the Solution Explorer, this is the best way to interact with C# projects on Mac in Visual Studio Code.

### Boilerplate Build
1. Before we do anything, let's *Run and Debug* HelloRhinoCommon to make sure everything is working as expected. We'll just build the boilerplate Plugin template. Click the *Run and Debug* button on the left hand side of Visual Studio Code and then the green play button in the newly opened panel.

    ![New Project](/images/your-first-plugin-mac-03.png)

1. *Rhinoceros* launches. Click *New Model*.
1. Type `Hello` into the Rhino Commandline.  Notice that the command autocompletes.

![Command Autocompletes](/images/your-first-plugin-mac-04.png)

1. The *HelloRhinoCommonCommand* command prints a message:

![Command Prompt](/images/your-first-plugin-mac-05.png)

1. *Quit* Rhinoceros. This stops the session. Go back to *Visual Studio Code*. Let's take a look at the Plugin Anatomy.

### Plugin Anatomy

1. Use the *Solution Explorer* to expand the project so that it looks like below.

![Solution Anatomy](/images/your-first-plugin-mac-06.png)

1. The *HelloRhinoCommon* solution (*.sln*) contians all of our projects. This was created for us by the `dotnet` command we ran earlier.
1. The *HelloRhinoCommon* project (*.csproj*) has the same name as its parent solution. This is the project that was created for us by `dotnet` command we ran earlier.
1. *Dependencies*: Just as with most projects, you will be referencing other libraries. The *RhinoCommon Plugin* template added the necessary references to create a basic RhinoCommon plugin.
1. *EmbeddedResources*: This is where you would place any image assets you want to ship with your plugin. The *RhinoCommon Plugin* template added an icon file with a default boilerplate icon.
1. *Properties* contains the *AssemblyInfo.cs* source file.  This file contains the meta-data (author, version, etc), including the very-important `Guid`, which identifies the plugin.
1. *HelloRhinoCommonCommand.cs* is where the action is.  Let's take a look at this file in the next section below...
1. *HelloRhinoCommonPlugin.cs* is where this template plugin derives from *Rhino.Plugins.Plugin* and returns a static Instance of itself.  

### Make Changes

1. Open *HelloRhinoCommonCommand.cs* in Visual Studio Code's Source Editor (if it isn't already).
2. Notice that `HelloRhinoCommonCommand` inherits from `Rhino.Commands.Command`

``` c#
        public class HelloRhinoCommonCommand : Rhino.Commands.Command
```

3. And that it overrides one inherited property called `EnglishName`

``` c#
        public override string EnglishName  => "HelloRhinoCommonCommand";
```

4. All Rhino commands must have an `EnglishName` property.  This command name will become inaccurate soon, as we're going to spice up our quite pointless command. Let's rename the command to *HelloDrawLine*:

``` c#
        public override string EnglishName  => "HelloDrawLine";
```

5. Further down, notice that `HelloRhinoCommandCommand` overrides the `RunCommand` method:

``` c#
        protected override Result RunCommand (Rhino.RhinoDoc doc, RunMode mode)
```

6. All Rhino commands must have a `RunCommand` method. Copy paste the below code into `RunCommand` between the brackets `{}`

``` c#
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
```

7. And then type in the following by hand to get a feel for the editor.

``` c#
doc.Objects.AddLine(pt0, pt1);
doc.Views.Redraw();

return Result.Success;
```

8. Notice that - as you type - Visual Studio Code uses IntelliSense, just like Visual Studio for Windows (and many other editors).


### Debugging

1. Set a breakpoint on line 52 of *HelloRhinoCommonCommand.cs*.  You set breakpoints in Visual Studio Code by clicking in the gutter to the left of the line numbers.
![Set a breakpoint](/images/your-first-plugin-mac-07.png)
1. *Run and Debug*. our project. The breakpoint will become an empty circle, this is because our code has not been loaded yet. Once we hit the breakpoint once and continue, the code will be loaded until we end our Debug session.
![Set a breakpoint](/images/your-first-plugin-mac-08.png)
1. Click New Model. And then run our *HelloDrawLine* command. Create the two points and as soon as you do, you should hit your breakpoint and rhino will pause
![Hit a breakpoint](/images/your-first-plugin-mac-09.png)
1. With Rhino paused, in *Visual Studio Code* we will see *Locals* under *Variables*.  In the list, find the `pt1` object we authored.  Click the dropdown *arrow* to expand the list of members on `pt1`.  
Our `pt1` is a `Rhino.Geometry.Point3d` this class has an `X`, `Y`, `Z` property just as we'll find documented in the [RhinoCommon API](https://developer.rhino3d.com/api/rhinocommon/rhino.geometry.point3d).
![Locals panel](/images/your-first-plugin-mac-10.png)
4. Let's Continue Execution in Rhino by pressing the Green *Play* button in the Debug Bar
1. Control is passed back to *Rhino* and your command finishes.  *Quit* Rhino or *Stop* the debugging session.

*Congratulations!*  You have just built your first RhinoCommon plugin for Rhino for Mac.  *Now what?*

## Next Steps

The above guide will also work perfectly well on Windows, if you need a more complex cross-platform plugin, check out the [Your First Plugin (Cross Platform)](/guides/rhinocommon/your-first-plugin-crossplatform) guide.

## Related topics

- [Installing Tools (Mac)](/guides/rhinocommon/installing-tools-mac)
- [Your First Plugin (Cross-Platform)](/guides/rhinocommon/your-first-plugin-crossplatform)
- [Plugin Installers (Mac)](/guides/rhinocommon/plugin-installers-mac)

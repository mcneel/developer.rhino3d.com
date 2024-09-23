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
1. Open _Visual Studio Code's Terminal_ via _Terminal (menu entry)_ > _New Terminal_, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Inside Terminal, run:
   ```pwsh
   dotnet new install Rhino.Templates
   ```

### Starting the Project

1. Create a folder on your mac where you would like your project to live. Name the folder `HelloRhinoCommon`.
1. If you have not done so already, _launch Visual Studio Code_.
1. Now we can open our new folder, navigate to _File_ > _Open Folder_ and choose the folder we just created.
1. Open Terminal via _Terminal_ > _New Terminal_, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Enter the following command into the Terminal:
   ```pwsh
   dotnet new rhino --version 8 -sample
   ```
1. In our Folder explorer, we should see the project appear as Visual Studio Code discovers the files.
1. Expand the Solution Explorer, this is the best way to interact with C# projects on Mac in Visual Studio Code.

### Boilerplate Build

1. Before we do anything, let's _Run and Debug_ HelloRhinoCommon to make sure everything is working as expected. We'll just build the boilerplate Plugin template. Click the _Run and Debug_ button on the left hand side of Visual Studio Code and then the green play button in the newly opened panel.

   ![New Project](/images/your-first-plugin-mac-03.png)

1. _Rhinoceros_ launches. Click _New Model_.
1. Type `Hello` into the Rhino Commandline. Notice that the command autocompletes.

![Command Autocompletes](/images/your-first-plugin-mac-04.png)

4. The _HelloRhinoCommonCommand_ command lets us draw a line, and then prints out a message
1. Press Stop Debugging _(⇧ F5)_, in Visual Studio Code, signified by the Red Square in the debug toolbar. This stops the debugging session. Go back to _Visual Studio Code_. Let's take a look at the Plugin Anatomy.

### Plugin Anatomy

1. Use the _Solution Explorer_ to expand the project so that it looks like below.

![Solution Anatomy](/images/your-first-plugin-mac-06.png)

1. The _HelloRhinoCommon_ solution (_.sln_) contians all of our projects. This was created for us by the `dotnet` command we ran earlier.
1. The _HelloRhinoCommon_ project (_.csproj_) has the same name as its parent solution. This is the project that was created for us by `dotnet` command we ran earlier.
1. _Dependencies_: Just as with most projects, you will be referencing other libraries. The _RhinoCommon Plugin_ template added the necessary references to create a basic RhinoCommon plugin.
1. _EmbeddedResources_: This is where you would place any image assets you want to ship with your plugin. The _RhinoCommon Plugin_ template added an icon file with a default boilerplate icon.
1. _Properties_ contains the _AssemblyInfo.cs_ source file. This file contains the meta-data (author, version, etc), including the very-important `Guid`, which identifies the plugin.
1. _HelloRhinoCommonCommand.cs_ is where the action is. Let's take a look at this file in the next section below...
1. _HelloRhinoCommonPlugin.cs_ is where this template plugin derives from _Rhino.Plugins.Plugin_ and returns a static Instance of itself.

### Make Changes

1. Open _HelloRhinoCommonCommand.cs_ in Visual Studio Code's Source Editor (if it isn't already).
2. Notice that `HelloRhinoCommonCommand` inherits from `Rhino.Commands.Command`

```c#
        public class HelloRhinoCommonCommand : Rhino.Commands.Command
```

3. And that it overrides one inherited property called `EnglishName`

```c#
        public override string EnglishName  => "HelloRhinoCommonCommand";
```

4. All Rhino commands must have an `EnglishName` property. This command name will become inaccurate soon, as we're going to spice up our quite pointless command. Let's rename the command to _HelloDrawLine_:

```c#
        public override string EnglishName  => "HelloDrawLine";
```

5. Further down, notice that `HelloRhinoCommandCommand` overrides the `RunCommand` method:

```c#
        protected override Result RunCommand (Rhino.RhinoDoc doc, RunMode mode)
```

6. And then type in the following by hand on line 62 to get a feel for the editor.

```c#
RhinoApp.WriteLine("I'm writing my first Rhino Plugin!");
```

7. Notice that - as you type - Visual Studio Code uses IntelliSense, just like Visual Studio for Windows (and many other editors).

### Debugging

1. Set a breakpoint on line 59 of _HelloRhinoCommonCommand.cs_. You set breakpoints in Visual Studio Code by clicking in the gutter to the left of the line numbers.
   ![Set a breakpoint](/images/your-first-plugin-mac-07.png)
1. _Run and Debug_. our project. The breakpoint will become an empty circle, this is because our code has not been loaded yet. Once we hit the breakpoint once and continue, the code will be loaded until we end our Debug session.
   ![Set a breakpoint](/images/your-first-plugin-mac-08.png)
1. Click New Model. And then run our _HelloDrawLine_ command. Create the two points and as soon as you do, you should hit your breakpoint and rhino will pause
   ![Hit a breakpoint](/images/your-first-plugin-mac-09.png)
1. With Rhino paused, in _Visual Studio Code_ we will see _Locals_ under _Variables_. In the list, find the `pt1` object we authored. Click the dropdown _arrow_ to expand the list of members on `pt1`.  
   Our `pt1` is a `Rhino.Geometry.Point3d` this class has an `X`, `Y`, `Z` property just as we'll find documented in the [RhinoCommon API](https://developer.rhino3d.com/api/rhinocommon/rhino.geometry.point3d).
   ![Locals panel](/images/your-first-plugin-mac-10.png)
1. Let's Continue Execution in Rhino by pressing the Green _Play_ button in the Debug Bar
1. Control is passed back to _Rhino_ and your command finishes. _Quit_ Rhino or _Stop_ the debugging session.

_Congratulations!_ You have just built your first RhinoCommon plugin for Rhino for Mac. _Now what?_

## Next Steps

The above guide will also work perfectly well on Windows, if you need a more complex cross-platform plugin, check out the [Your First Plugin (Cross Platform)](/guides/rhinocommon/your-first-plugin-crossplatform) guide.

If you'd like to push your exciting new plugin to Yak so that everyone can use it, check out the [Creating a Yak Package](/guides/yak/creating-a-rhino-plugin-package/) guide.

## Related topics

- [Installing Tools (Mac)](/guides/rhinocommon/installing-tools-mac)
- [Your First Plugin (Cross-Platform)](/guides/rhinocommon/your-first-plugin-crossplatform)
- [Plugin Installers (Mac)](/guides/rhinocommon/plugin-installers-mac)

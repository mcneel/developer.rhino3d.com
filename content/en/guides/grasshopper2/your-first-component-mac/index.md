+++
aliases = ["/en/wip/guides/grasshopper2/your-first-component-mac/"]
authors = [ "callum" ]
categories = [ "Getting Started" ]
description = "This guide walks you through your first Grasshopper 2 component for Rhino for Mac using RhinoCommon and Visual Studio Code."
keywords = [ "developer", "grasshopper2", "grasshopper", "gh2", "components" ]
languages = [ "C#" ]
sdk = [ "Grasshopper 2" ]
title = "Your First Component (Mac)"
type = "guides"
weight = 3

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
block_webcrawlers = true

+++

## Prerequisites

It is presumed you already have the necessary tools installed and are ready to go. If you are not there yet, see [Installing Tools (Mac)](/guides/rhinocommon/installing-tools-mac).

## HelloGrasshopper 2

We will use Visual Studio Code and the dotnet Rhino Grasshopper template to create a new, basic, Grasshopper 2 component called _HelloGrasshopper 2_.

If you are familiar with Visual Studio Code, these step-by-step instructions may be overly detailed for you. The executive summary: create a new Solution using the Grasshopper 2 Component dotnet template, build and run, and then make a change.

We are presuming you have never used Visual Studio Code before, so we'll go through this one step at a time.

### Download the required template

1. Launch Visual Studio Code.
1. Open _Visual Studio Code's Terminal_ via _Terminal (menu entry)_ > _New Terminal_, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Inside Terminal, run:
   ```pwsh
   dotnet new install Rhino.Templates
   ```

### Starting the Project

1. Create a folder on your mac where you would like your project to live. Name the folder `HelloGrasshopper2`.
1. If you have not done so already, _launch Visual Studio Code_.
1. Now we can open our new folder, navigate to _File_ > _Open Folder_ and choose the folder we just created.
1. Open Terminal via _Terminal_ > _New Terminal_, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Enter the following command into the Terminal:
   ```pwsh
   dotnet new gh2 --version 8 -sample
   ```
1. In our Folder explorer, we should see the project appear as Visual Studio Code discovers the files.
1. Expand the Solution Explorer, this is the best way to interact with C# projects on Mac in Visual Studio Code.

### Boilerplate Build

1. Before we do anything, let's _Run and Debug_ HelloGrasshopper 2 to make sure everything is working as expected. We'll just build the boilerplate Plugin template. Click the _Run and Debug_ button on the left hand side of Visual Studio Code and then the green play button in the newly opened panel.

   ![New Project](/images/gh2/your-first-component-mac-01.png)

1. _Rhinoceros and Grasshopper 2_ launch.
1. We will find the HelloGrasshopper 2 Component under **Chapter / Section**

![Solution Anatomy](/images/gh2/your-first-component-mac-02.png)

4. Adding the component to the canvas will run the component and output some interesting geometry in the Rhino Viewport

![Solution Anatomy](/images/gh2/your-first-component-mac-03.png)

5. Press Stop Debugging _(⇧ F5)_, in Visual Studio Code, signified by the Red Square in the debug toolbar. This stops the debugging session. Now let's n take a look at the Plugin Anatomy.

### Component Anatomy

Use the **Solution Explorer** to expand the **Solution** (_.sln_) so that it looks like this...

![Solution Anatomy](/images/gh2/your-first-component-mac-04.png)

1. The **HelloGrasshopper2** solution (_.sln_)
1. The **HelloGrasshopper2** project (_.csproj_) has the same name as its parent solution...this is the project that was created for us by the template earlier.
1. **References**: Just as with most projects, you will be referencing other libraries. The template added the necessary references to create a basic Grasshopper 2 component.
1. **Grasshopper2** is the Rhino for Mac main grasshopper DLL. Classes in this DLL are subclassed and used by your custom component.
1. **Icons** All Icons should be placed in Icons to load automatically.
1. **HelloGrasshopper2Component.cs** is where a custom `Grasshopper.Components.Component` subclass is defined. Your project may contain multiple subclasses of Component if you want to ship multiple components in a single gh2 plugin*.
1. **HelloGrasshopper2Plugin.cs** is where the Grasshopper Plugin is defined.
1. **HelloGrasshopper2Info.cs** defines general information about this gh2 plugin.

### Debugging

1. Add a breakpoint to line 52 of _HelloGrasshopper 2Component.cs_. You set breakpoints in Visual Studio Code by clicking in the gutter to the left of the line numbers.
   ![Set a breakpoint](/images/gh2/your-first-component-mac-05.png)
1. _Run and Debug_. our project. The breakpoint will become an empty circle, this is because our code has not been loaded yet. Once we hit the breakpoint once and continue, the code will be loaded until we end our Debug session.
   ![Set a breakpoint](/images/gh2/your-first-component-mac-06.png)
1. Rhino and Grasshopper 2 should open, if Grasshopper 2 does not open, click "New Model" and run the _G2_ command.
1. Place our sample component _HelloGrasshopper2Component_ and as soon as you do, you should hit your breakpoint and rhino/Grasshopper 2 will pause (You may need to drag the Grasshopper 2 window out of the way to see Visual Studio Code)
   ![Hit a breakpoint](/images/gh2/your-first-component-mac-07.png)
1. With Rhino/Grasshopper 2 paused, in _Visual Studio Code_ we will see _Locals_ under _Variables_. You can inspect all of the values for the variables in your component.
   ![Locals panel](/images/gh2/your-first-component-mac-08.png)
1. Let's Continue Execution in Rhino and Grasshopper 2 by pressing the Green _Play_ button in the Debug Bar
1. Control is passed back to _Rhino / Grasshopper 2_ and your command finishes. Now _Stop_ _(⇧ F5)_ the debugging session as before.
1. **Remove** the breakpoint you created above by clicking on it in the gutter.

**Congratulations!** You have just built your first Grasshopper 2 component for Rhino for Mac.

<!--
### Adding components

A single gh2 plugin can contain more than one [GH_Component](https://mcneel.github.io/grasshopper-api-docs/api/grasshopper/html/T_Grasshopper 2_Kernel_GH_Component.htm) derived class (and commonly does). Dotnet has support for adding more custom components to your project.

1. Open _Visual Studio Code's Terminal_ via _Terminal (menu entry)_ > _New Terminal_, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Inside Terminal, run:

```pwsh
dotnet new ghcomponent -n "NewComponent"
```

1. A new component will appear called _NewComponent_
-->

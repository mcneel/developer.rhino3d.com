+++
aliases = ["/en/5/guides/grasshopper/your-first-component-mac/", "/en/6/guides/grasshopper/your-first-component-mac/", "/en/7/guides/grasshopper/your-first-component-mac/", "/wip/guides/grasshopper/your-first-component-mac/"]
authors = [ "steve", "callum" ]
categories = [ "Getting Started" ]
description = "This guide walks you through your first Grasshopper component for Rhino for Mac using RhinoCommon and Visual Studio Code."
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#" ]
sdk = [ "Grasshopper" ]
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

+++

## Prerequisites

It is presumed you already have the necessary tools installed and are ready to go. If you are not there yet, see [Installing Tools (Mac)](/guides/rhinocommon/installing-tools-mac).

## HelloGrasshopper

We will use Visual Studio Code and the dotnet Rhino Grasshopper template to create a new, basic, Grasshopper component called _HelloGrasshopper_.

If you are familiar with Visual Studio Code, these step-by-step instructions may be overly detailed for you. The executive summary: create a new Solution using the Grasshopper Component dotnet template, build and run, and then make a change.

We are presuming you have never used Visual Studio Code before, so we'll go through this one step at a time.

### Download the required template

1. Launch Visual Studio Code.
1. Open _Visual Studio Code's Terminal_ via _Terminal (menu entry)_ > _New Terminal_, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Inside Terminal, run:
   ```pwsh
   dotnet new install Rhino.Templates
   ```

### Starting the Project

1. Create a folder on your mac where you would like your project to live. Name the folder `HelloGrasshopper`.
1. If you have not done so already, _launch Visual Studio Code_.
1. Now we can open our new folder, navigate to _File_ > _Open Folder_ and choose the folder we just created.
1. Open Terminal via _Terminal_ > _New Terminal_, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Enter the following command into the Terminal:
   ```pwsh
   dotnet new grasshopper --version 8 -sample
   ```
1. In our Folder explorer, we should see the project appear as Visual Studio Code discovers the files.
1. Expand the Solution Explorer, this is the best way to interact with C# projects on Mac in Visual Studio Code.

### Boilerplate Build

{{< call-out hint "Build Issue?" >}}
Older Rhino Templates do not have System.Drawing.Common referenced.
To add them to your project run the command **dotnet add package System.Drawing.Common -v 7.0.0** in the terminal.
{{< /call-out >}}

1. Before we do anything, let's _Run and Debug_ HelloGrasshopper to make sure everything is working as expected. We'll just build the boilerplate Plugin template. Click the _Run and Debug_ button on the left hand side of Visual Studio Code and then the green play button in the newly opened panel.

   ![New Project](/images/your-first-component-mac-01.png)

1. _Rhinoceros and Grasshopper_ launch.
1. We will find the HelloGrasshopper Component under **Category / SubCategory**

![Solution Anatomy](/images/your-first-component-mac-02.png)

4. Adding the component to the canvas will run the component and output some interesting geometry in the Rhino Viewport

![Solution Anatomy](/images/your-first-component-mac-03.png)

5. Press Stop Debugging _(⇧ F5)_, in Visual Studio Code, signified by the Red Square in the debug toolbar. This stops the debugging session. Now let's n take a look at the Plugin Anatomy.

### Component Anatomy

Use the **Solution Explorer** to expand the **Solution** (_.sln_) so that it looks like this...

![Solution Anatomy](/images/your-first-component-mac-04.png)

1. The **HelloGrasshopper** solution (_.sln_)
1. The **HelloGrasshopper** project (_.csproj_) has the same name as its parent solution...this is the project that was created for us by the template earlier.
1. **References**: Just as with most projects, you will be referencing other libraries. The template added the necessary references to create a basic Grasshopper component.
1. **Grasshopper** is the Rhino for Mac main grasshopper DLL. Classes in this DLL are subclassed and used by your custom component.
1. **HelloGrasshopperComponent.cs** is where a custom `Grasshopper.Kernal.GH_Component` subclass is defined. Your project may contain multiple subclasses of GH*Component if you want to ship multiple components in a single \_gha*.
1. **HelloGrasshopperInfo.cs** defines general information about this _gha_.

### Debugging

1. Add a breakpoint to line 75 of _HelloGrasshopperComponent.cs_. You set breakpoints in Visual Studio Code by clicking in the gutter to the left of the line numbers.
   ![Set a breakpoint](/images/your-first-component-mac-05.png)
1. _Run and Debug_. our project. The breakpoint will become an empty circle, this is because our code has not been loaded yet. Once we hit the breakpoint once and continue, the code will be loaded until we end our Debug session.
   ![Set a breakpoint](/images/your-first-component-mac-06.png)
1. Rhino and Grasshopper should open, if Grasshopper does not open, click "New Model" and run the _Grasshopper_ command.
1. Place our sample component _HelloGrasshopperComponent_ and as soon as you do, you should hit your breakpoint and rhino/Grasshopper will pause (You may need to drag the Grasshopper window out of the way to see Visual Studio Code)
   ![Hit a breakpoint](/images/your-first-component-mac-07.png)
1. With Rhino/Grasshopper paused, in _Visual Studio Code_ we will see _Locals_ under _Variables_. You can inspect all of the values for the variables in your component.
   ![Locals panel](/images/your-first-component-mac-08.png)
1. Let's Continue Execution in Rhino and Grasshopper by pressing the Green _Play_ button in the Debug Bar
1. Control is passed back to _Rhino / Grasshopper_ and your command finishes. Now _Stop_ _(⇧ F5)_ the debugging session as before.
1. **Remove** the breakpoint you created above by clicking on it in the gutter.

**Congratulations!** You have just built your first Grasshopper component for Rhino for Mac. **Now what?**

## Next Steps

You've built a component library from boilerplate code, but what about putting together a new simple component "from scratch" and adding it to your project? (Component libraries are made up of multiple components after all). Next, check out the [Simple Component](/guides/grasshopper/simple-component) guide.

Try debugging your new grasshopper plugin on [Windows](/guides/grasshopper/your-first-component-windows/), all plugins using the new templates are now cross-platform by default.

### Adding components

A single gha can contain more than one [GH_Component](https://mcneel.github.io/grasshopper-api-docs/api/grasshopper/html/T_Grasshopper_Kernel_GH_Component.htm) derived class (and commonly does). Dotnet has support for adding more custom components to your project.

1. Open _Visual Studio Code's Terminal_ via _Terminal (menu entry)_ > _New Terminal_, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Inside Terminal, run:

```pwsh
dotnet new ghcomponent -n "NewComponent"
```

1. A new component will appear called _NewComponent_

## Related topics

This article is focused on initial setup and debugging a Grasshopper component in Rhino for Mac. For further reading on customizing your component please see:

- [Grasshopper](/guides/grasshopper/csharp-essentials/)
- [Distributing your Plugin](/guides/yak/creating-a-rhino-plugin-package/)

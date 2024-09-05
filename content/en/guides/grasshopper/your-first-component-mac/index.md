+++
aliases = ["/5/guides/grasshopper/your-first-component-mac/", "/6/guides/grasshopper/your-first-component-mac/", "/7/guides/grasshopper/your-first-component-mac/", "/wip/guides/grasshopper/your-first-component-mac/"]
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

We will use Visual Studio Code and the dotnet Rhino Grasshopper template to create a new, basic, Grasshopper component called *HelloGrasshopper*.

If you are familiar with Visual Studio Code, these step-by-step instructions may be overly detailed for you.  The executive summary: create a new Solution using the Grasshopper Component dotnet template, build and run, and then make a change.

We are presuming you have never used Xamarin Studio before, so we'll go through this one step at a time.



### Download the required template

1. Launch Visual Studio Code.
1. Open *Visual Studio Code's Terminal* via *Terminal (menu entry)* > *New Terminal*, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Inside Terminal, run:
    ``` pwsh
    dotnet new install Rhino.Templates
    ```


### Starting the Project

1. Create a folder on your mac where you would like your project to live. Name the folder `HelloGrasshopper`.
1. If you have not done so already, *launch Visual Studio Code*.
1. Now we can open our new folder, navigate to *File* > *Open Folder* and choose the folder we just created.
1. Open Terminal via *Terminal* > *New Terminal*, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
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

1. Before we do anything, let's *Run and Debug* HelloGrasshopper to make sure everything is working as expected. We'll just build the boilerplate Plugin template. Click the *Run and Debug* button on the left hand side of Visual Studio Code and then the green play button in the newly opened panel.

    ![New Project](/images/your-first-component-mac-01.png)

1. *Rhinoceros and Grasshopper* launch.
1. We will find the HelloGrasshopper Component under **Category / SubCategory**

  ![Solution Anatomy](/images/your-first-component-mac-02.png)

4. Adding the component to the canvas will perform no action

  ![Solution Anatomy](/images/your-first-component-mac-03.png)

5. *Quit* Rhinoceros. This stops the session. Go back to *Visual Studio Code*. Let's take a look at the Plugin Anatomy.



### Component Anatomy
Use the **Solution Explorer** to expand the **Solution** (*.sln*) so that it looks like this...

  ![Solution Anatomy](/images/your-first-component-mac-04.png)

1. The **HelloGrasshopper** solution (*.sln*)
1. The **HelloGrasshopper** project (*.csproj*) has the same name as its parent solution...this is the project that was created for us by the template earlier.
1. **References**: Just as with most projects, you will be referencing other libraries.  The template added the necessary references to create a basic Grasshopper component.
1. **Grasshopper** is the Rhino for Mac main grasshopper DLL. Classes in this DLL are subclassed and used by your custom component.
1. **HelloGrasshopperComponent.cs** is where a custom `Grasshopper.Kernal.GH_Component` subclass is defined. Your project may contain multiple subclasses of GH_Component if you want to ship multiple components in a single *gha*.  
1. **HelloGrasshopperInfo.cs** defines general information about this *gha*.



### Debugging

1. Add a semicolon to line 47 of *HelloGrasshopperComponent.cs*, and set a breakpoint on it. You set breakpoints in Visual Studio Code by clicking in the gutter to the left of the line numbers.
![Set a breakpoint](/images/your-first-component-mac-05.png)
1. *Run and Debug*. our project. The breakpoint will become an empty circle, this is because our code has not been loaded yet. Once we hit the breakpoint once and continue, the code will be loaded until we end our Debug session.
![Set a breakpoint](/images/your-first-component-mac-06.png)
1. Click New Model. And then run our *HelloDrawLine* command. Create the two points and as soon as you do, you should hit your breakpoint and rhino will pause
![Hit a breakpoint](/images/your-first-component-mac-07.png)
1. With Rhino paused, in *Visual Studio Code* we will see *Locals* under *Variables*.  You can inspect all of the values for the variables in your component.
![Locals panel](/images/your-first-component-mac-08.png)
4. Let's Continue Execution in Rhino by pressing the Green *Play* button in the Debug Bar
1. Control is passed back to *Rhino* and your command finishes.  *Quit* Rhino or *Stop* the debugging session.
1. **Remove** the breakpoint you created above by clicking on it in the gutter.

**Congratulations!**  You have just built your first Grasshopper component for Rhino for Mac.  **Now what?**



## Next Steps

### Adding components

A single gha can contain more than one [GH_Component](https://mcneel.github.io/grasshopper-api-docs/api/grasshopper/html/T_Grasshopper_Kernel_GH_Component.htm) derived class (and commonly does). Dotnet has support for adding more custom components to your project.

1. Open *Visual Studio Code's Terminal* via *Terminal (menu entry)* > *New Terminal*, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Inside Terminal, run:

  ``` pwsh
  dotnet new ghcomponent -n "NewComponent"
  ```

1. A new component will appear called *NewComponent*

## Related topics

This article is focused on initial setup and debugging a Grasshopper component in Rhino for Mac.  For further reading on customizing your component please see:

- [Grasshopper](/guides/grasshopper/csharp-essentials/)
- [Distributing your Plugin](/guides/yak/creating-a-rhino-plugin-package/)

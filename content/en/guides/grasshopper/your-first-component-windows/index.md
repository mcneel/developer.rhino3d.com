+++
aliases = ["/5/guides/grasshopper/your-first-component-windows/", "/6/guides/grasshopper/your-first-component-windows/", "/7/guides/grasshopper/your-first-component-windows/", "/wip/guides/grasshopper/your-first-component-windows/"]
authors = [ "dan", "callum" ]
categories = [ "Getting Started" ]
description = "This guide walks you through your first custom Grasshopper component library using Visual Studio."
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#", "VB" ]
sdk = [ "Grasshopper" ]
title = "Your First Component (Windows)"
type = "guides"
weight = 2
thumbnail = "/images/dev-logo-grasshopper-small.png"

[admin]
TODO = ""
origin = ""
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

It is presumed you already have the necessary tools installed and are ready to go. If you are not there yet, see [Installing Tools (Windows)](/guides/grasshopper/installing-tools-windows).

## HelloGrasshopper

We will use the Grasshopper Assembly templates to create a new, basic, component library called HelloGrasshopper.

If you are familiar with Visual Studio, these step-by-step instructions may be overly detailed for you. The executive summary: create a new project using the Grasshopper Assembly template, build and run, and then make a change.

We are presuming you have never used Visual Studio before, so we'll go through this one step at a time.

### File New

1. If you have not done so already, **launch Visual Studio** (for the purposes of this guide, we are using Visual Studio Community Edition and C#).
1. Navigate to **File** > **New** > **Project**...
   ![File New Project](/images/your-first-plugin-windows-01.png)
1. A **Create a new project** wizard should appear. In the **Search for templates** area, search for `Grasshopper` to filter the results. Find and select the **Grasshopper Assembly for Rhino (C\#)** entry and click **Next**.
1. For the purposes of this Guide, we will name our demo plugin _HelloGrasshopper_. In the **Configure your new project** dialog, fill in the **Project name** field. **Browse** and select a location for this project on your disk, then click **Next**
1. The _New Grasshopper Add-On dialog_ appears. Check the _Provide sample code_ checkbox.
   ![New Grasshopper Assembly](/images/your-first-component-windows-03.png)
1. This is where you fill out information about your first component:
   1. Add-on display name: the name of component library itself.
   1. Name: the name of the component as displayed in the ribbon bar and search menus.
   1. Nickname: the default name of the component when inserted into the canvas.
   1. Category: name of tab where component icon will be shown.
   1. Subcategory: name of group inside tab where icon will be shown.
   1. Description: description shown in tooltip when mouse is over the component icon in the menu.
1. For the purposes of this guide, let's chek the "Provide Sample Code", and then click **Finish**...
1. A **new solution** called **HelloGrasshopper** should open...
   ![HelloGrasshopper Solution](/images/your-first-component-windows-04.png)

### Boilerplate Build

1. Before we do anything, let's **build** and **run** HelloGrasshopper to make sure everything is working as expected. We'll just build the boilerplate Plugin template. Click **Start** (play) button in toolbar corner of Visual Studio (or press **F5**) to **Start Debugging**...
   ![Start Button](/images/your-first-compo-windows-06.png)
1. **Rhinoceros** launches and a moment later, so will **Grasshopper**.

{{< call-out hint "First Debug" >}}
_The first debug may take a while depending on your settings, as Visual Studio downloads debugging files, this is normal._
{{< /call-out >}}

1. Navigate to **Curve** > **Primitive** in the components menus. You should see HelloGrasshopper in the list with a blank icon. Drag this onto the canvas. The component will run and some interesting Geometry will appear in the Rhino Viewport.
1. **Exit** Rhinoceros. This stops the session. Go back to **Visual Studio**. Let's take a look at the...

### Component Anatomy

1. Use the **Solution Explorer** to expand the **Solution** (_.sln_) so that it looks like this...
   ![Grasshopper Component Anatomy](/images/your-first-component-windows-06.png)

   _NOTE_: Depending on your edition of Visual Studio, it may look slightly different.

1. The **HelloGrasshopper** project (_.csproj_) has the same name as its parent solution...this is the project that was created for us by the **Grasshopper Assembly** template wizard earlier.
1. **Dependencies**: Just as with most projects, you will be referencing other libraries. The **Grasshopper Assembly** template added the necessary dependencies to create a custom Grasshopper component.
1. **Framework Targets** - The **Grasshopper Assembly** template is multi-targeted so that the correct assemblies are loaded for the correct platforms.
1. **Grasshopper** - The referenced Grasshopper Nuget.
1. **Properties** contains the **launchSettings.json** file. This file contains all of the debug.
1. **HelloGrasshopperInfo.cs** contains the component library information, such as the name, icon, etc.
1. **HelloGrasshopperComponent.cs** is where the action is. Let's take a look at this file...

### Make Changes

1.  Open **HelloGrasshopperComponent.cs** in Visual Studio's Source Editor (if it isn't already).
1.  Notice that `HelloGrasshopperComponent` inherits from `GH_Component` ...

        public class HelloGrasshopperComponent : GH_Component

1.  If you hover over `GH_Component` you will notice this is actually `Grasshopper.Kernel.GH_Component`.
1.  `HelloGrasshopperComponent` also overrides two methods for determining the input and output parameters ...

```cs
protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
...
protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
```

1. The actual work done by the component is to be found in the `SolveInstance` method...

```cs
protected override void SolveInstance(IGH_DataAccess DA)
```

1. As you can see, this is where the action happens. This boilerplate component creates a spiral on a plane. Just to make sure everything is working, let's change the default plane on which the spiral is constructed. On line[^1] 67, in `SolveInstance`, notice that an XY plane is constructed...

```cs
Plane plane = Plane.WorldXY;
```

1. Further down in the `SolveInstance` method, you will notice that the input data is being fed into this plane...

```cs
if (!DA.GetData(0, ref plane)) return;
```

1. Go back to the `RegisterInputParams`, and find the line where the _Plane_ input is registered. The last argument being fed to the method - `Plane.WorldXY` - is the default value of the input...

```cs
pManager.AddPlaneParameter("Plane", "P", "Base plane for spiral", GH_ParamAccess.item, Plane.WorldXY);
```

1. Change the default value of the _Plane_ input to be `Plane.WorldYZ` ...

```cs
pManager.AddPlaneParameter("Plane", "P", "Base plane for spiral", GH_ParamAccess.item, Plane.WorldYZ);
```

1. Now let's examine what happens when inputs are given to this component...

### Debugging

1. Set a breakpoint on line[^1] 99 of _HelloGrasshopperComponent.cs_. You set breakpoints in Visual Studio by clicking in the gutter...
   ![Set a breakpoint](/images/your-first-component-windows-07.png)
1. **Build** and **Run**.
1. In Grasshopper, place a _HelloGrasshopper_ component on the canvas...as soon as you do, you should hit your breakpoint and pause...
   ![Hit a breakpoint](/images/your-first-component-windows-08.png)
1. The reason you hit the breakpoint is because the `SolveInstance` method was called once initially when the component was placed on the canvas. With Rhino and Grasshopper paused, in **Visual Studio** switch to the **Autos** tab (if it not already there). In the list, find the `plane` object. Our `plane` is a `Rhino.Geometry.Plane` with a value of `{Origin=0,0,0 XAxis=0,1,0, YAxis=0,0,1, ZAxis=1,0,0}` ...an YZ plane, the default, as expected.
1. **Continue** in Grasshopper by pressing the **Continue** button in the upper menu of **Visual Studio** (or press **F5**)...
   ![Continue Executing](/images/your-first-plugin-windows-11.png)
1. Control is passed back to **Grasshopper** and the spiral draws in the Rhino viewport. Now, place an _XY Plane_ component on the canvas and feed it as an input into _HelloGrasshopper_'s _Plane_ input. Notice you hit your breakpoint again, because the `SolveInstance` is being called now that the input values have changed.
1. **Exit** Grasshopper and Rhino or **Stop** the debugging session.
1. **Remove** the breakpoint you created above by clicking on it in the gutter.

**DONE!**

**Congratulations!** You have just built your first Grasshopper component for Rhino for Windows. **Now what?**

## Next Steps

You've built a component library from boilerplate code, but what about putting together a new simple component "from scratch" and adding it to your project? (Component libraries are made up of multiple components after all). Next, check out the [Simple Component](/guides/grasshopper/simple-component) guide.

## Related topics

- [Installing Tools (Windows)](/guides/grasshopper/installing-tools-windows)
- [Simple Component](/guides/grasshopper/simple-component)

**Footnotes**

[^1]: **Line numbers** in Visual Studio can be enabled and disabled in **Tools** > **Options...** > **Text Editor** section > **All Languages** entry > **General** sub-entry > **Settings** subsection > check **Line numbers**. Click **OK** to close the **Options** dialog.

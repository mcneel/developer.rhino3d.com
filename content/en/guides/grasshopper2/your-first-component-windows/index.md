+++
aliases = ["/en/wip/guides/grasshopper2/your-first-component-windows/"]
authors = [ "callum" ]
categories = [ "Getting Started" ]
description = "This guide walks you through your first custom Grasshopper 2 component library using Visual Studio."
keywords = [ "developer", "grasshopper2", "grasshopper", "gh2", "components" ]
languages = [ "C#" ]
sdk = [ "Grasshopper 2" ]
title = "Your First Component (Windows)"
type = "guides"
weight = 2
thumbnail = "/images/gh2/dev-logo-grasshopper-small.png"

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
block_webcrawlers = true

+++

It is presumed you already have the necessary tools installed and are ready to go. If you are not there yet, see [Installing Tools (Windows)](/guides/grasshopper/installing-tools-windows).

## HelloGrasshopper 2

We will use the Grasshopper 2 Assembly templates to create a new, basic, component library called HelloGrasshopper2.

If you are familiar with Visual Studio, these step-by-step instructions may be overly detailed for you. The executive summary: create a new project using the Grasshopper 2 Assembly template, build and run, and then make a change.

We are presuming you have never used Visual Studio before, so we'll go through this one step at a time.

### File New

1. If you have not done so already, **launch Visual Studio** (for the purposes of this guide, we are using Visual Studio Community Edition and C#). Click **Create New Project**.
   
![Create New Project](/images/gh2/your-first-component-windows-00.png)

2. A **Create a new project** wizard should appear. In the **Search for templates** area, search for `Grasshopper2` to filter the results. Find and select the **Grasshopper 2 Plug-In for Rhino (C\#)** entry and click **Next**.

![Choose a Template](/images/gh2/your-first-component-windows-01.png)

3. For the purposes of this Guide, we will name our demo plugin _HelloGrasshopper 2_. In the **Configure your new project** dialog, fill in the **Project name** field. **Browse** and select a location for this project on your disk, then click **Create**

![Configure Your New Project](/images/gh2/your-first-component-windows-02.png)

4. For the purposes of this guide, let's check the _Provide Sample Code_

![New Plugin Wizard](/images/gh2/your-first-component-windows-03.png)

5. This is where you fill out information about your first component:
   1. **Plug-In display name:** the name of the plugin itself.
   1. **Component class name:** the name of the component class.
   1. **Name:** the name of the component as displayed in the ribbon bar and search menus.
   1. **Chapter:** name of tab where component icon will be shown.
   1. **Section:** name of group inside tab where icon will be shown.
   1. **Description:** description shown in tooltip when mouse is over the component icon in the menu.

1. Click **Finish**

1. A **new solution** called **HelloGrasshopper 2** should open...
   ![HelloGrasshopper 2 Solution](/images/gh2/your-first-component-windows-04.png)

### Boilerplate Build

1. Before we do anything, let's **build** and **run** HelloGrasshopper 2 to make sure everything is working as expected. We'll just build the boilerplate Plugin template. Click **Start** (play) button in toolbar corner of Visual Studio (or press **F5**) to **Start Debugging**...
   ![Start Button](/images/gh2/your-first-component-windows-05.png)
1. **Rhinoceros** launches and a moment later, so will **Grasshopper 2**.

{{< call-out hint "First Debug" >}}
_The first debug may take a while depending on your settings, as Visual Studio downloads debugging files, this is normal._
{{< /call-out >}}

1. Navigate to **Curve** > **Primitive** in the components menus. You should see HelloGrasshopper 2 in the list with a blank icon. Drag this onto the canvas. The component will run and some interesting Geometry will appear in the Rhino Viewport.
1. **Exit** Rhinoceros. This stops the session. Go back to **Visual Studio**. Let's take a look at the...

### Component Anatomy

1. Use the **Solution Explorer** to expand the **Solution** (_.sln_) so that it looks like this...
   ![Grasshopper 2 Component Anatomy](/images/gh2/your-first-component-windows-06.png)

{{< call-out hint "Varying Editions" >}}
Depending on your edition of Visual Studio, it may look slightly different.
{{< /call-out >}}

1. The **HelloGrasshopper 2** project (_.csproj_) has the same name as its parent solution...this is the project that was created for us by the **Grasshopper 2 Assembly** template wizard earlier.
1. **Dependencies**: Just as with most projects, you will be referencing other libraries. The **Grasshopper 2 Assembly** template added the necessary dependencies to create a custom Grasshopper 2 component.
1. **Framework Targets** - The **Grasshopper 2 Assembly** template is multi-targeted so that the correct assemblies are loaded for the correct platforms.
1. **Grasshopper2** - The referenced Grasshopper 2 Nuget.
1. **Properties** contains the **launchSettings.json** file. This file contains all of the debug.
1. **HelloGrasshopper2Plugin.cs** the Rhino Plugin required for Grasshopper 2.
1. **HelloGrasshopper2PlpuginInfo.cs** contains the component library information, such as the name, icon, etc.
1. **HelloGrasshopper2Component.cs** is where the action is. Let's take a look at this file...

### Make Changes

1.  Open **HelloGrasshopper 2Component.cs** in Visual Studio's Source Editor (if it isn't already).
1.  Notice that `HelloGrasshopper 2Component` inherits from `GH_Component` ...

        public class HelloGrasshopper2Component : Component

1.  If you hover over `Component` you will notice this is actually `Grasshopper.Components.Component`.
1.  `HelloGrasshopper2Component` also overrides two methods for determining the input and output parameters ...

```cs
protected override void AddInputs(InputAdder inputs)
...
protected override void AddOutputs(OutputAdder outputs)
```

5. The actual work done by the component is to be found in the `Process` method...

```cs
protected override void Process(IDataAccess access)
```

6. As you can see, this is where the action happens. This boilerplate component creates a spiral on a plane. Just to make sure everything is working, let's change the default plane on which the spiral is constructed. On line[^1] 51, in `protected override void Process(IDataAccess access)`, notice that an XY plane is retrieved from the inputs...

```cs
if (!access.GetItem(0, out Plane plane)) return;
```

7. Go back to the `AddInputs`, and find the line where the _Plane_ input is registered. The chained method sets the default value of the input...

```cs
inputs.AddPlane("Plane", "P", "Base plane for spiral").Set(Plane.WorldXY);
```

8. Change the default value of the _Plane_ input to be `Plane.WorldYZ` ...

```cs
inputs.AddPlane("Plane", "P", "Base plane for spiral").Set(Plane.WorldYZ);
```

10. Now let's examine what happens when inputs are given to this component...

### Debugging

1. Set a breakpoint on line[^1] 75 of _HelloGrasshopper 2Component.cs_. You set breakpoints in Visual Studio by clicking in the gutter...
   ![Set a breakpoint](/images/gh2/your-first-component-windows-07.png)
1. **Build** and **Run**.
1. Note that at first the breakpoint is not loaded, and won't be until Grasshopper 2 loads.
   ![Inactive breakpoint](/images/gh2/your-first-component-windows-08.png)
1. In Grasshopper 2, place a _HelloGrasshopper2_ component on the canvas...as soon as you do, you should hit your breakpoint and pause...
   ![Hit a breakpoint](/images/gh2/your-first-component-windows-09.png)
1. The reason you hit the breakpoint is because the `Process` method was called when the component was placed on the canvas. With Rhino and Grasshopper 2 paused.
1. In **Visual Studio** let's open the autos panel, use **Ctrl + Q** and search Autos, double click the first result, make sure to _pin_ the panel on the right hand side or else it may auto close.
   ![Open Autos](/images/gh2/your-first-component-windows-10.png)
1. In the list, find the `plane` object. Our `plane` is a `Rhino.Geometry.Plane` with a value of `{Origin=0,0,0 XAxis=0,1,0, YAxis=0,0,1, ZAxis=1,0,0}` ...an YZ plane, the default, as expected.
   ![Continue Executing](/images/gh2/your-first-component-windows-11.png)
1. **Continue** in Grasshopper 2 by pressing the **Continue** button in the upper menu of **Visual Studio** (or press **F5**)...
1. Control is passed back to **Grasshopper 2** and the spiral draws in the Rhino viewport. Now, place a _World XY_ component on the canvas and feed it as an input into _HelloGrasshopper 2_'s _Plane_ input. Notice you hit your breakpoint again, because the `SolveInstance` is being called now that the input values have changed.
1. **Exit** Grasshopper 2 and Rhino or **Stop** the debugging session.
1. **Remove** the breakpoint you created above by clicking on it in the gutter.

**Congratulations!** You have just built your first Grasshopper 2 component for Rhino for Windows.


[^1]: **Line numbers** in Visual Studio can be enabled and disabled in **Tools** > **Options...** > **Text Editor** section > **All Languages** entry > **General** sub-entry > **Settings** subsection > check **Line numbers**. Click **OK** to close the **Options** dialog.

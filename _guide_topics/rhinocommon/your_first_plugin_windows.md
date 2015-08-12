---
layout: toc-guide-page
title: Your First Plugin (Windows)
author: giulio@mcneel.com
categories: ['GettingStarted']
platforms: ['Windows']
apis: ['RhinoCommon']
languages: ['C#']
keywords: ['first', 'RhinoCommon', 'Plugin']
TODO: 0
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/addcommand
order: 3
---

# Your First Plugin (Windows)
{: .toc-title }

This guide walks you through your first plugin for Rhino for Windows using RhinoCommon and Visual Studio. It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Windows)]({{ site.baseurl }}/guides/rhinocommon/installing_tools_windows).

## HelloRhinoCommon
{: .toc-header }

We will use the RhinoCommon Templates to create a new, basic, command plugin called HelloRhinoCommon.

#### Step-by-Step

If you are familiar with Visual Studio, these step-by-step instructions may be overly detailed for you.  The executive summary: create a new Solution using the RhinoCommon template, build and run, and then make a change.

We are presuming you have never used Visual Studio before, so we'll go through this one step at a time.

#### File New
{: .toc-subheader }

1. If you have not done so already, **launch Visual Studio** (for the purposes of this guide, we are using Visual Studio 2015 Community Edition and C#).
1. Navigate to **File** > **New** > **Project**...
![File New Project]({{ site.baseurl }}/images/your_first_plugin_windows_01.png)
1. A **New Project** wizard should appear.  In the left column, find the **Installed** > **Templates** > **Visual C#** > **Rhinoceros** section.  In the central list, select the RhinoCommon Plug-In template...
![New Project]({{ site.baseurl }}/images/your_first_plugin_windows_02.png)
1. For the purposes of this Guide, we will name our demo plugin *HelloRhinoCommon*.  At the bottom of the window, fill in the **Name** field.  **Browse** and select a location for this plugin on your disk...
![Project Configuration]({{ site.baseurl }}/images/your_first_plugin_windows_03.png)
1. Check **Create directory for solution**.  *NOTE*: This is optional depending on how you want to structure your projects.
1. Click the **OK** button.  *NOTE*: You don't have to add the project to source control for this demo.
1. The **New RhinoCommon Plug-In** dialog appears.  This dialog allows you to **Configure your new plugin project**, as well as select which RhinoCommon references to use and which debug version of Rhino you would like to launch...  
![HelloRhinoCommon Solution]({{ site.baseurl }}/images/your_first_plugin_windows_04.png)
1. For the purposes of this guide, we will **accept the defaults** and click **Finish**...
1. A **new solution** called **HelloRhinoCommon** should open...
![HelloRhinoCommon Solution]({{ site.baseurl }}/images/your_first_plugin_windows_05.png)


#### Boilerplate Build
{: .toc-subheader }

1. Before we do anything, let's **build** and **run** HelloRhinoCommon to make sure everything is working as expected.  We'll just build the boilerplate Plugin template.  Click **Start** (play) button in toolbar corner of Visual Studio (or press **F5**) to **Start Debugging**...
![Start Button]({{ site.baseurl }}/images/your_first_plugin_windows_06.png)
1. **Rhinoceros** launches.  Create a new, empty model.
1. Since this is the first time you are running the plugin, you need to **"install"** it.  (The RhinoCommon template has set things up so when you compile the solution an *.rhp* file is compiled in the *bin* subdirectory of the project directory.) In the Rhino command prompt type the **PlugInManager** command.  Click the **Install…** button.
1.  **Browse** to the *HelloRhinoCommon.rhp* file (in our case, this is in *C:\\dev\\repositories\\HelloRhinoCommon\\HelloRhinoCommon\\bin\\*) and click **Open**.  
1. The HelloRhinoCommon plugin is now installed.  Click **OK** to close the Rhino Options dialog.
1. Enter the **HelloRhinoCommonCommand** command.  Notice that the command autocompletes...
1. The **HelloRhinoCommonCommand** command begins and prompts you to ***Please select the start point:***.
1. Notice there is **also a command status** in Rhino's command prompt when the command begins: ***The HelloRhinoCommonCommand command will add a line right now.***
1. **Finish** the command by selecting a start point and and end point.
1. Also note there is **a command status** in Rhino's command prompt when the command ends: ***The HelloRhinoCommonCommand command added one line to the document.***
1. **Exit** Rhinoceros.  This stops the session.  Go back to **Visual Studio**.  Let's take a look at the...


#### Plugin Anatomy
{: .toc-subheader }

1. Use the **Solution Explorer** to expand the **Solution** (*.sln*) so that it looks like this...
![Solution Anatomy]({{ site.baseurl }}/images/your_first_plugin_windows_07.png)
*NOTE*: Depending on your edition of Visual Studio, it may look slightly different.
1. The **HelloRhinoCommon** project (*.csproj*) has the same name as its parent solution...this is the project that was created for us by the **RhinoCommon Plugin** template wizard earlier.
1. **Properties** contains the **AssemblyInfo.cs** source file.  This file contains the meta-data (author, version, etc) about the plugin.
1. **References**: Just as with most projects, you will be referencing other libraries.  The **RhinoCommon Plugin** template added the necessary references to create a basic RhinoCommon plugin.
1. **Microsoft.CSharp** contains classes required for C# code compilation.
1. **RhinoCommon** is *the* critical reference for our purposes here.
1. **System**, **System.Core**, **System.Drawing**, **System.Windows.Forms** are .NET foundational libraries.
1. **HelloRhinoCommonPlugin.cs** is where this template plugin derives from *Rhino.Plugins.Plugin* and returns a static Instance of itself.  
1. **HelloRhinoCommonCommand.cs** is where the action is.  Let's take a look at this file...


#### Make Changes
{: .toc-subheader }

1. Open **HelloRhinoCommonCommand.cs** in Visual Studio's Source Editor (if it isn't already).
1. Notice that `HelloRhinoCommonCommand` inherits from `Command` ...

        public class HelloRhinoCommonCommand : Command
1. If you hover over `Command` you will notice this is actually `Rhino.Commands.Command`.
1. `HelloRhinoCommonCommand` also overrides one inherited property called `EnglishName` ...

        public override string EnglishName {
          get { return "HelloRhinoCommonCommand"; }
        }
1. All Rhino commands must have a `EnglishName` property.  This command name is not very accurate.  We know from running the boilerplate code that this command prompts the user to draw a line.  Let's rename the command to *HelloDrawLine*:

        public override string EnglishName {
          get { return "HelloDrawLine"; }
        }
1. Further down, notice that `HelloRhinoCommandCommand` overrides the `RunCommand` method:

        protected override Result RunCommand (Rhino.RhinoDoc doc, RunMode mode)
1. All Rhino commands must have a `RunCommand` method.  As you can see, this is where the action happens.  Let's create an intermediary line object that we can feed to the `AddLine` method.  Find the spot in `RunCommand` after the user has been prompted to select two points.  Type in...

        Rhino.Geometry.Line line1 = new Line (pt0, pt1);
1. Notice that - as you type - Visual Studio uses IntelliSense to create an auto-complete list of members to call.  Now, feed `line1` as an argument to the `doc.Objects.AddLine` method...

        doc.Objects.AddLine (line1);
1. Now that we have a line of our own, let's examine it...


#### Debugging
{: .toc-subheader }

1. Set a breakpoint on line[^1] 67 of *HelloRhinoCommonCommand.cs*.  You set breakpoints in Visual Studio by clicking in the gutter...
![Set a breakpoint]({{ site.baseurl }}/images/your_first_plugin_windows_08.png)
1. **Build** and **Run**.  Because you have changed the name of the command, you will need to **"install"** the plugin again.  Follow the steps 3-5 in the [Boilerplate Build](#boilerplate-build) section above.
1. Run **HelloDrawLine** in Rhino.  Create the two points...as soon as you do, you should hit your breakpoint and pause...
![Hit a breakpoint]({{ site.baseurl }}/images/your_first_plugin_windows_09.png)
1. With Rhino paused, in **Visual Studio** switch to the **Autos** tab (if it not already there).  In the list, find the `line1` object we authored.  Click the dropdown **arrow** to expand the list of members on `line1`.  Our `line1` is a `Rhino.Geometry.Line` this class has a `Length` property...  
![Autos panel]({{ site.baseurl }}/images/your_first_plugin_windows_10.png)
1. **Continue** in Rhino by pressing the **Continue** button in the upper menu of **Visual Studio** (or press **F5**)...
![Continue Executing]({{ site.baseurl }}/images/your_first_plugin_windows_11.png)
1. Control is passed back to **Rhino** and your command finishes.  **Exit** Rhino or **Stop** the debugging session.
1. **Remove** the breakpoint you created above by clicking on it in the gutter.
1. Now, let's use the `Length` value to report something to the user.  Near the very end of `RunCommand`, add the following line...

        RhinoApp.WriteLine ("The distance between the two points is {0}.", line1.Length);
1. **Save**, **Build**, and **Run**.  Run `HelloDrawLine` in Rhino yet again (create the two points...).  Rhino now reports the length of the line you created.  However, this is not very clean.
1. **Exit** Rhino to **Stop** the debugging session once more.
1. Let's add a unit system and be explicit about what we're reporting...

        RhinoApp.WriteLine ("The distance between the two points is {0} {1}.", line1.Length, doc.ModelUnitSystem.ToString().ToLower());
1. **Save**, **Build**, and **Run** again.  Now we're reporting the length of the line we created with the document's unit system (`doc.ModelUnitSystem`) with the proper case (`ToLower()`).  Much better.

**DONE!**

Well, we could go on and on - `line1` was never necessary, we could have just used `pt0.DistanceTo(pt1).ToString()`, etc. - but that is beside the point:

**Congratulations!**  You have just built your first RhinoCommon plugin for Rhino for Windows.  **Now what?**

---

## Next Steps
{: .toc-header }

You're using RhinoCommon, so this plugin will actually run on both platforms.  Check out the [Your First Plugin (Cross Platform)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_crossplatform) guide.

---

## Related topics
{: .toc-header }

- [Installing Tools (Windows)]({{ site.baseurl }}/guides/rhinocommon/installing_tools_windows)
- [Your First Plugin (Cross-Platform)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_crossplatform)

---

## Footnotes
{: .toc-header }

[^1]: **Line numbers** in Visual Studio can be enabled and disabled in **Tools** > **Options...** > **Text Editor** section > **All Languages** entry > **General** sub-entry > **Settings** subsection > check **Line numbers**.  Click **OK** to close the **Options** dialog.

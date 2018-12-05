---
title: Your First Plugin (Mac)
description: This guide walks you through your first plugin for Rhino for Mac using RhinoCommon and Visual Studio for Mac.
authors: ['dan_belcher']
author_contacts: ['dan']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Mac']
categories: ['Getting Started']
origin: unset
order: 4
keywords: ['first', 'RhinoCommon', 'Plugin']
layout: toc-guide-page
---


It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Mac)]({{ site.baseurl }}/guides/rhinocommon/installing-tools-mac).

## HelloRhinoCommon

We will use the Rhino Xamarin Addin/Extension to create a new, basic, command plugin called HelloRhinoCommon.

If you are familiar with Visual Studio for Windows or Visual Studio for Mac, these step-by-step instructions may be overly detailed for you.  The executive summary: create a new Solution using the RhinoCommon Plugin template, build and run, and then make a change.

We are presuming you have never used Visual Studio for Mac before, so we'll go through this one step at a time.

### File New

1. If you have not done so already, *launch Visual Studio for Mac*.
1. Navigate to *File* > *New* > *Solution*...
![File New Solution]({{ site.baseurl }}/images/your-first-plugin-mac-01.png)
1. A *New Project* wizard should appear.  In the left column, find the *Other* > *Miscellaneous* section.  Under General, select the RhinoCommon Plug-In template...
![New Project]({{ site.baseurl }}/images/your-first-plugin-mac-02.png)
1. Click the *Next* button.
1. You will now *Configure your new project*.  For the purposes of this Guide, we will name our demo plugin *HelloRhinoCommon*.  Fill in the *Project Name* field.  *Browse* and select a location for this plugin on your Mac...
![Project Configuration]({{ site.baseurl }}/images/your-first-plugin-mac-03.png)
1. Check *Create a project within the solution directory*.  *Note*: This is optional depending on how you want to structure your projects.
1. Click the *Create* button.  *Note*: You don't have to create a .git repository for this demo.
1. A *new solution* called *HelloRhinoCommon* should open...
![HelloRhinoCommon Solution]({{ site.baseurl }}/images/your-first-plugin-mac-04.png)
1. Right-click on the *HelloRhinoCommon* project and select *Set As Startup Project* from the menu.

### Boilerplate Build

1. Before we do anything, let's *build* and *run* HelloRhinoCommon to make sure everything is working as expected.  We'll just build the boilerplate Plugin template.  Click the large *Build* > *Run* (play) button in the upper-left corner of Visual Studio for Mac...
![Play Button]({{ site.baseurl }}/images/your-first-plugin-mac-05.png)
1. *Rhinoceros* launches.  Create a *New Model*...
![New Model Button]({{ site.baseurl }}/images/your-first-plugin-mac-06.png)
1. Enter the *HelloRhinoCommonCommand* command.  Notice that the command autocompletes...
![Command Autocompletes]({{ site.baseurl }}/images/your-first-plugin-mac-07.png)
1. The *HelloRhinoCommonCommand* command begins and prompts you...
![Command Prompt]({{ site.baseurl }}/images/your-first-plugin-mac-08.png)
1. Notice there is *also a command status* in Rhino's command history area when the command begins...
![Command Starts]({{ site.baseurl }}/images/your-first-plugin-mac-09.png)
1. Also note there is *a command status* in Rhino's command history area when the command ends...
![Command Ends]({{ site.baseurl }}/images/your-first-plugin-mac-10.png)
1. *Quit* Rhinoceros.  This stops the session.  Go back to *Visual Studio for Mac*.  Let's take a look at the...


### Plugin Anatomy

1. Use the *Solution Explorer* to expand the *Solution* (*.sln*) so that it looks like this...
![Solution Anatomy]({{ site.baseurl }}/images/your-first-plugin-mac-11.png)
1. The *HelloRhinoCommon* project (*.csproj*) has the same name as its parent solution...this is the project that was created for us by the *RhinoCommon Plugin* template wizard earlier.
1. *References*: Just as with most projects, you will be referencing other libraries.  The *RhinoCommon Plugin* template added the necessary references to create a basic RhinoCommon plugin.
1. *Eto* is the cross-platform User Interface (UI) library Rhino uses.  If you examine its properties, you will notice it comes bundled as part of Rhino for Mac.
1. *Rhino.UI* is the Rhino-specific User Interface (UI) library associated with...
1. *RhinoCommon* is *the* critical reference for our purposes here.
1. *System*, *System.Core*, and *System.Drawing* are .NET foundational libraries...in this case, we are referencing the Mono versions of these libraries (on Windows, these references will point to the canonical, Microsoft-provided, versions).
1. *Packages* is used the the [NuGet](https://www.nuget.org/) package-manager.  There are no referenced packages in this boilerplate project, but note that Visual Studio for Mac supports NuGet, just like Visual Studio for Windows does.
1. *Properties* contains the *AssemblyInfo.cs* source file.  This file contains the meta-data (author, version, etc), including the very-important `Guid`, which identifies the plugin.
1. *HelloRhinoCommonPlugin.cs* is where this template plugin derives from *Rhino.Plugins.Plugin* and returns a static Instance of itself.  
1. *HelloRhinoCommonCommand.cs* is where the action is.  Let's take a look at this file...


### Make Changes

1. Open *HelloRhinoCommonCommand.cs* in Visual Studio for Mac's Source Editor (if it isn't already).
1. Notice that `HelloRhinoCommonCommand` inherits from `Rhino.Commands.Command` ...

        public class HelloRhinoCommonCommand : Rhino.Commands.Command
1. ...and overrides one inherited property called `EnglishName` ...

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
1. Notice that - as you type - Visual Studio for Mac uses IntelliSense, just like Visual Studio for Windows (and many other editors).  Now, feed `line1` as an argument to the `doc.Objects.AddLine` method...

        doc.Objects.AddLine (line1);
1. Now that we have a line of our own, let's examine it...


### Debugging

1. Set a breakpoint on line[^1] 55 of *HelloRhinoCommonCommand.cs*.  You set breakpoints in Visual Studio for Mac by clicking in the gutter...
![Set a breakpoint]({{ site.baseurl }}/images/your-first-plugin-mac-12.png)
1. *Build* and *Run*.  Run *HelloDrawLine* in Rhino.  Create the two points...as soon as you do, you should hit your breakpoint and pause...
![Hit a breakpoint]({{ site.baseurl }}/images/your-first-plugin-mac-13.png)
1. With Rhino paused, in *Visual Studio for Mac* switch to the *Locals* tab.  In the list, find the `line1` object we authored.  Click the dropdown *arrow* to expand the list of members on `line1`.  Our `line1` is a `Rhino.Geometry.Line` this class has a `Length` property...  
![Locals panel]({{ site.baseurl }}/images/your-first-plugin-mac-14.png)
1. *Continue Executing* in Rhino by pressing the *Play* button in the upper navigation menu of *Visual Studio for Mac*...
![Continue Executing]({{ site.baseurl }}/images/your-first-plugin-mac-15.png)
1. Control is passed back to *Rhino* and your command finishes.  *Quit* Rhino or *Stop* the debugging session.
1. *Remove* the breakpoint you created above by clicking on it in the gutter.
1. Now, let's use the `Length` value to report something to the user.  Near the very end of `RunCommand`, add the following line...

        RhinoApp.WriteLine ("The distance between the two points is {0}.", line1.Length);
1. *Build* and *Run*.  Run `HelloDrawLine` in Rhino yet again (create the two points...).  Rhino now reports the length of the line you created.  However, this is not very clean.
1. *Quit* Rhino to *Stop* the debugging session once more.
1. Let's add a unit system and be explicit about what we're reporting...

        RhinoApp.WriteLine ("The distance between the two points is {0} {1}.", line1.Length, doc.ModelUnitSystem.ToString().ToLower());
1. *Build* and *Run* again.  Now we're reporting the length of the line we created with the document's unit system (`doc.ModelUnitSystem`) with the proper case (`ToLower()`).  Much better.

**DONE!**

Well, we could go on and on - `line1` was never necessary, we could have just used `pt0.DistanceTo(pt1).ToString()`, etc. - but that is beside the point:

*Congratulations!*  You have just built your first RhinoCommon plugin for Rhino for Mac.  *Now what?*

---

## Next Steps

You're using RhinoCommon, so this plugin will actually run on both platforms.  Check out the [Your First Plugin (Cross Platform)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-crossplatform) guide.

---

## Related topics

- [Installing Tools (Mac)]({{ site.baseurl }}/guides/rhinocommon/installing-tools-mac)
- [Your First Plugin (Cross-Platform)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-crossplatform)
- [Plugin Installers (Mac)]({{ site.baseurl }}/guides/rhinocommon/plugin-installers-mac)


---

## Footnotes

[^1]: *Line numbers* in Visual Studio for Mac can be enabled and disabled in *Visual Studio* > *Preferences...* > *Text Editor* section > *Markers and Rulers* entry > check *Show line numbers*.

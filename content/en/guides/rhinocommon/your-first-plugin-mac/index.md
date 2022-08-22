+++
aliases = ["/5/guides/rhinocommon/your-first-plugin-mac/", "/6/guides/rhinocommon/your-first-plugin-mac/", "/7/guides/rhinocommon/your-first-plugin-mac/", "/wip/guides/rhinocommon/your-first-plugin-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "This guide walks you through your first plugin for Rhino for Mac using RhinoCommon and Visual Studio for Mac."
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

We will use the Rhino Visual Studio Extension to create a new, basic, command plugin called HelloRhinoCommon.

{{< call-out tip "Experienced with Visual Studio?" >}}
If you are familiar with Visual Studio for Windows or Visual Studio for Mac, these step-by-step instructions may be overly detailed for you. The executive summary: create a new Solution using the RhinoCommon Plugin template, build and run, and then make a change.
{{< /call-out >}}

We are presuming you have never used Visual Studio for Mac before, so we'll go through this one step at a time.

### File New

1. If you have not done so already, *launch Visual Studio for Mac*.
1. Navigate to *File* > *New Project*...
![File New Project](/images/your-first-plugin-mac-01.png)
1. A *New Project* wizard should appear. In the left column, find the *Other* > *Miscellaneous* section. Under General, select the RhinoCommon Plug-In template...
![New Project](/images/your-first-plugin-mac-02.png)
1. Click the *Continue* button.
1. You will now *Configure your new project*. For the purposes of this Guide, we will name our demo plugin *HelloRhinoCommon*. Fill in the *Project Name* field. Leave the other defaults alone.
![Project Configuration](/images/your-first-plugin-mac-03.png)
1. Click the *Continue* button.
1. *Browse* and select a location for this plugin on your Mac.
1. Click the *Create* button. *Note*: You don't have to create a .git repository for this demo.
1. A *new project* called *HelloRhinoCommon* should open...
![HelloRhinoCommon Solution](/images/your-first-plugin-mac-04.png)

### Boilerplate Build

{{< image url="/images/your-first-plugin-mac-05.png" alt="Play Button" class="float_right" >}}
1. Before we do anything, let's *build* and *run* HelloRhinoCommon to make sure everything is working as expected. We'll just build the boilerplate Plugin template. Click the large *Build* > *Run* (play) button in the upper-left corner of Visual Studio for Mac...
{{< image url="/images/your-first-plugin-mac-06.png" alt="New Model Button" class="float_right" >}}
1. *Rhinoceros* launches.  Create a *New Model*...
1. Enter the *HelloRhinoCommonCommand* command.  Notice that the command autocompletes...
![Command Autocompletes](/images/your-first-plugin-mac-07.png)
1. The *HelloRhinoCommonCommand* command begins and prompts you...
![Command Prompt](/images/your-first-plugin-mac-08.png)
1. Notice there is *also a command status* in Rhino's command history area when the command begins...
![Command Starts](/images/your-first-plugin-mac-09.png)
1. Also note there is *a command status* in Rhino's command history area when the command ends.
1. *Quit* Rhinoceros. This stops the session. Go back to *Visual Studio for Mac*.  Let's take a look at the...


### Plugin Anatomy

1. Use the *Solution Explorer* to expand the *Solution* (*.sln*) so that it looks like this...
![Solution Anatomy](/images/your-first-plugin-mac-11.png)
1. The *HelloRhinoCommon* project (*.csproj*) has the same name as its parent solution...this is the project that was created for us by the *RhinoCommon Plugin* template wizard earlier.
1. *Dependencies*: Just as with most projects, you will be referencing other libraries. The *RhinoCommon Plugin* template added the necessary references to create a basic RhinoCommon plugin.
1. *EmbeddedResources*: This is where you would place any image assets you want to ship with your plugin. The *RhinoCommon Plugin* template added an icon file with a default boilerplate icon.
1. *Properties* contains the *AssemblyInfo.cs* source file.  This file contains the meta-data (author, version, etc), including the very-important `Guid`, which identifies the plugin.
1. *.gitignore* is a file added by the git version control system. Feel free to ignore this for now.
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

1. Set a breakpoint on line[^1] 59 of *HelloRhinoCommonCommand.cs*.  You set breakpoints in Visual Studio for Mac by clicking in the gutter...
![Set a breakpoint](/images/your-first-plugin-mac-12.png)
1. *Build* and *Run*.  Run *HelloDrawLine* in Rhino.  Create the two points...as soon as you do, you should hit your breakpoint and pause...
![Hit a breakpoint](/images/your-first-plugin-mac-13.png)
1. With Rhino paused, in *Visual Studio for Mac* switch to the *Locals* tab.  In the list, find the `line1` object we authored.  Click the dropdown *arrow* to expand the list of members on `line1`.  Our `line1` is a `Rhino.Geometry.Line` this class has a `Length` property...  
![Locals panel](/images/your-first-plugin-mac-14.png)
{{< image url="/images/your-first-plugin-mac-15.png" alt="Continue Executing" class="float_right" >}}
4. *Continue Executing* in Rhino by pressing the *Play* button in the upper navigation menu of *Visual Studio for Mac*...
1. Control is passed back to *Rhino* and your command finishes.  *Quit* Rhino or *Stop* the debugging session.
1. *Remove* the breakpoint you created above by clicking on it in the gutter.
1. Now, let's use the `Length` value to report something to the user.  Near the very end of `RunCommand`, add the following line...

```cs
RhinoApp.WriteLine ("The distance between the two points is {0}.", line1.Length);
```

8. *Build* and *Run*.  Run `HelloDrawLine` in Rhino yet again (create the two points...).  Rhino now reports the length of the line you created.  However, this is not very clean.
1. *Quit* Rhino to *Stop* the debugging session once more.
1. Let's add a unit system and be explicit about what we're reporting...

```cs
RhinoApp.WriteLine ("The distance between the two points is {0} {1}.", line1.Length, doc.ModelUnitSystem.ToString().ToLower());
```

11. *Build* and *Run* again.  Now we're reporting the length of the line we created with the document's unit system (`doc.ModelUnitSystem`) with the proper case (`ToLower()`).  Much better.

**DONE!**

Well, we could go on and on - `line1` was never necessary, we could have just used `pt0.DistanceTo(pt1).ToString()`, etc. - but that is beside the point:

*Congratulations!*  You have just built your first RhinoCommon plugin for Rhino for Mac.  *Now what?*

## Next Steps

You're using RhinoCommon, so this plugin will actually run on both platforms.  Check out the [Your First Plugin (Cross Platform)](/guides/rhinocommon/your-first-plugin-crossplatform) guide.

## Related topics

- [Installing Tools (Mac)](/guides/rhinocommon/installing-tools-mac)
- [Your First Plugin (Cross-Platform)](/guides/rhinocommon/your-first-plugin-crossplatform)
- [Plugin Installers (Mac)](/guides/rhinocommon/plugin-installers-mac)


**Footnotes**

[^1]: *Line numbers* in Visual Studio for Mac can be enabled and disabled in *Visual Studio* > *Preferences...* > *Text Editor* section > *Markers and Rulers* entry > check *Show line numbers*.

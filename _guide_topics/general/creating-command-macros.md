---
title: Creating Macros
description: A basic tutorial on creating macros (scripting together Rhino commands)
authors: ['Scott Davidson']
author_contacts: ['scottd']
sdk: ['Macro']
languages: ['Macro']
platforms: ['Windows', 'Mac']
categories: ['Overview']
origin: https://wiki.mcneel.com/rhino/basicmacros
order: 1
keywords: ['macro', 'overview', 'rhinoceros', 'command']
layout: toc-guide-page
---

You can create macros in Rhino to automate many tasks, customize your commands, and improve your workflow.

There may be some confusion about the use of the term “scripting” here.  Classically, it describes both the process of writing macros (what this section is about), as well as writing more sophisticated scripts in either [RhinoScript]({{ site.baseurl }}/guides/rhinoscript/), [Rhino.Python]({{ site.baseurl }}/guides/rhinopython/) or other programming languages.  

The two things are actually very different. Writing functions in RhinoScript or other programming languages is a lot more complex than creating macros, and requires some programming knowledge and skills.  We don't cover that here.

I use the term “Macro” here exclusively to describe the putting together of strings of ordinary Rhino commands and their options to create an automated function.  This is scripting on its simplest of levels, and is easily accessible to any ordinary Rhino user, even if they have no knowledge of programming.  All You need is a reasonable understanding of Rhino commands and their structure, as well as a logical mind and a taste for a little experimentation and debugging.

####The tools you need
1. Your brain.

2. The Rhino Help file -  lists all Rhino commands and their sub-options. This is your most important reference.

3. The Rhino **MacroEditor**, to easily run and debug your macros.


##You've already used a macro or two...
First, if you are a user of Rhino, you are already a macro user even though you may not know it.  Many of the commands in Rhino are already “macroed” for you. When you click a toolbar button or call a command from the menu, it is often a preset macro.  To see, Shift+right-click on the button **Extrude Straight**:

{{:legacy:en:ExtrudeCrvButtonEditor.gif}}

This is an example of the simplest macro, which sets a series of options within a single command so that you don’t have to specify each one every time you use it.  **ExtrudeCrv** has several buttons with preset options, **Tapered, AlongCurve, ToPoint, Cap=Yes** (solid) etc.  Check out the macros under all the **ExtrudeCrv** buttons to see how they are laid out.

In a sense, you’re doing the same thing as if you clicked or typed the options one at a time at the command line.  In fact, that’s all macros really are -- just a set of instructions to repeat a sequence of commands that you would otherwise input manually one at a time.

This scripting of options for a single command can also be combined with data entry (i.e. coordinates or other numerical data). It is also possible to string together several commands in a row, for an automated sequence of events to manipulate or create objects.

**Note:** Why the _Underscores ?  These tell Rhino that the command which follows is in English (no matter what the language you are running Rhino in), which will make your macro universal.  If you are running in English and don’t care, you can eliminate the underscores in your macros if you wish. It will not affect anything else.  Also, why the exclamation point (!)?  This cancels any previous command that might be running, for safety's sake.

##Getting started

Say you have to place a series of 10x10x10 boxes with the center of the bottom face landing at the desired point, with that point to be specified by either by a mouse click at the desired location or by entering the coordinates by the keyboard.

You could use the standard Box (**Corner to Corner + Height**) command, but by default this will place the insertion point at the first corner of the box.  To have the insertion point where we want, it is easier to use the Box, Center command.   This is in reality just the Box command with the center option, so you will have to activate it in your macro.

Open the **MacroEditor** and  type this in:

```
! _Box _Center
```

(This is actually the macro under the Box, Center button if you check.) 
All entries (command words and numerical inputs) need to be separated by a single space.

Now, we need to specify the center point.  To do this, you need to tell Rhino to stop processing the command temporarily and wait for an input in the form of a click or a keyboard entry.  Do this by inserting the command Pause.

```
! _Box _Center _Pause
```

Once the data has been entered, you can specify the box size directly in the command.  Since the Center option in Box wants a corner of the box as a second input, you can specify its X,Y coordinates:

```
! _Box _Center _Pause r5,5
```

(Why the `r`?  We want this coordinate to be relative to the last picked point, that is to say, the box bottom center.  Otherwise the corner will always land at X5, Y5.)

At this point you can put in the height, which in this case is relative to the original starting point.

```
! _Box _Center _Pause r5,5 10
```

Since there is no further input necessary nor options possible, the macro completes and our box is there.  Note that since we wanted a height equal to the width, another possibility  would just to have been to use Enter instead of 10 for the last entry.

```
! _Box _Center _Pause r5,5 _Enter
```

Now that the macro is running, [[rhino:macroscriptsetup|make a new toolbar button]] and paste the macro in. Give it a recognizable name, like “10x10x10 bottom centered box”.  Note, once the macro is executed, right-clicking repeats the whole sequence of this macro, so you can use it many times in a row without clicking the button every time.

##OK, let’s get a bit more complicated…

Some commands invoke dialog boxes with many options.  Normally, this stops your macro and waits for you to click the desired options, then continue.  Since you want to automate, you can bypass the dialog by putting a –hyphen (also known as a dash) before the command.  Then you can script in all your options and the macro will run to completion without needing your intervention.  Some commands have several levels of sub-options.  If you want to see what’s available, type the command at the command line with the hyphen and look at what’s proposed for options.  Click on the options and see if they have sub-options.

####Loft two open curves

Let’s say you would like to repetitively `Loft` two *OPEN* curves together to form a surface.  If you use the standard `Loft` command, you always have to go through the dialog.  If you use the `–Loft` version, you can avoid this and things go much faster.  Look at the following:

```
_-Loft
_Pause
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Note that when you invoke the command, immediately a pause lets you pick your curves.  If you remove the pause, the macro won’t work if you have not selected your curves before calling it.  If you have already preselected your curves the pause is intelligently ignored.  The command then sets all your specified options. Once that is done, it creates the surface and finishes. Try it with two open curves, either pre or post selecting them.  Try modifying one or more of the options, like substituting Closed=Yes or Simplify=Rebuild. (For this you also have to add a line with Rebuild=20 or some other value.)

#### Modifying it to use with closed curves

Now, try it with two closed curves.  You have a problem.  Why? For closed curves, Loft needs another input from you -– the seam location.  This is something that needs to be in the macro in the right sequence.  So, you can either choose from various automatic seam options (which are on a sub-option level) or you can adjust it on screen.  Either way, you need to modify the macro.

Adding a pause in the right place lets you check and adjust the seam on screen:

```
_-Loft
_Pause
_Pause  <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Adding an `Enter` instead of the `Pause` tells Rhino you don’t care. Just leave the seam the way it is by default.

```
_-Loft
_Pause
_Enter  <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Or, you can specify another Loft seam option by stepping down into the seam sub-option level:

```
_-Loft
_Pause
_Natural  <--
_Enter    <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

(The `Enter` after Natural is necessary to exit the “seam” option level and get back up to the Loft options level.)

Unfortunately, the same macro will not work correctly for both open and closed curves because of the extra seam option required.  This is one of the limitations of the macro system and the way some Rhino commands have been written.


##Using macros to set your interface options quickly

Macros can also be used to set various GUI and Document Properties options automatically without having to go wading into the Options dialog.  I use the following to set the render mesh the way I want it. (Note the dash before -_DocumentProperties.)

```
-_DocumentProperties
_Mesh _Custom
_MaxAngle=0 _AspectRatio=0
_MinEdgeLength=0 _MaxEdgeLength=0
_MaxEdgeSrf=0.01 _GridQuads=16
_Refine=Yes _JaggedSeams=No
_SimplePlanes=No
_Enter
_Enter
```

Why are there two Enters at the end?

You went down two levels in -_DocumentProperties, first to the Mesh level, then to the Custom sublevel inside Mesh.  You need one Enter to exit the sublevel and go back to the main level, and one more to exit the command.  Some scripts might even need three enters.  

The following is from Jeff LaSor, for turning on or off the crosshair cursor:

To script Crosshairs  ON or OFF put the following on a button:

```
  -_Options _Appearance _Visibility
  _Crosshairs _Enter _Enter _Enter
```
Notice the reference to each individual command option name.  Specifying them inside the script is like clicking on them with the mouse.  Also note the three Enter entries.  Since each command option takes you down into a new set of sub-level command options, an Enter is required to take you back up.  Since this script went down three levels, it needs to specify three Enters to get all the way out of the command.

Or, if you just use an exclamation point `!` at the end (which in a script means “end now!”), it takes you all the way out regardless of how many sub-levels you're in. Note, if you want to continue your macro with something else, do not use `!`, use the Enters instead, otherwise your macro will always stop at the `!` and terminate.

The script simply toggles the crosshairs ON and OFF. But if you wanted a script that always turned them ON and another that always turned them OFF, here's what they would look like:

Always ON version:

```
  -_Options _Appearance _Visibility
  _Crosshairs=_Show !
</code>
Always OFF version:
<code>
  -_Options _Appearance _Visibility
  _Crosshairs=_Hide !
```

Note the use of the`!` here. Also, note you can assign directly the values options can take on to that option using the '=' operator.  The Crosshairs option has two possible values, "Show" and "Hide", and thus, that's what is used in the assignment.

(Thanks, Jeff)

##Other useful macro writing tools and commands

There are some handy tricks for doing more complex macros.  One is the discriminating use of various selection filters, particularly `SelLast`, which selects the last object created/transformed, `SelPrev`,  which selects the previous input object, and `SelNone`, which deselects everything.  There are also possibilities to name objects, group them (and name the group) and then recall them later by that object name or group name.

```
Select
SelLast
SelPrev
SelNone
SetObjectName
SetGroupName
SelGroup
SelName
Group
Ungroup
```

To set a single object name (this in itself is a macro!):

```
  _Properties _Pause _Object _Name
  [put your object name here] _Enter _Enter
```

To cancel a single object name (without deleting the object)

```
  _Properties _Pause _Object _Name
  “ “ _Enter _Enter (quote space quote for the name)
```

##Examples using the above tools

Look at the following macro:

```
_Select _Pause _Setredrawoff
_BoundingBox _World _Enter
_Selnone _Sellast
_OffsetSrf _Solid _Pause
_Delete _Sellast
_BoundingBox _World _Enter
_Delete _Setredrawon
```

It creates an offset bounding box around an object. The offset is input by the user.  See if you can follow the logical sequence.  The Setredrawoff/on stop/restart the screen refresh, eliminates the display flickering as all is executed and speeds up the process.  Beware, if you terminate the command before Setredrawon, you will think Rhino is dead, as the screen no longer updates.  If this happens, don’t panic, typing the command `Setredrawon` will restore the display refresh.

**As a final example,** the following macro creates a point centered on a 2D planar or text object and grouped with it. It assumes that you're in the same view the text was created in, and that the object is really 2D and planar. (Otherwise it will likely fail.)

Note the use of a named group and various selection commands.  The `NoEcho` command temporarily stops the reporting of information to the command line, which, combined with Setredrawoff/on makes the macro run without flashing and without too much info reported to command history.  It will run without those as well, though.

```
_Select _Pause _Noecho _Setredrawoff
_Group _Enter _SetGroupName TexTemp
_BoundingBox _CPlane _Enter
_SelNone _SelLast _PlanarSrf
_SelPrev _Delete _SelLast
_AreaCentroid _Delete
_Sellast _SelGroup TexTemp
_Ungroup _Group _Setredrawon
```

**Please feel free to add to or edit this tutorial!**
This is a work in progress...

---

## Related Topics

- [Python Basic Syntax]({{ site.baseurl }}/guides/rhinopython/)
- [Rhinoscript]({{ site.baseurl }}/guides/rhinoscript/)
- [Macro Syntax Help Topic](http://docs.mcneel.com/rhino/5/help/en-us/information/rhinoscripting.htm)
- [Running a Macro]({{ site.baseurl }}/guides/rhinoscript/running-scripts-from-macros/)

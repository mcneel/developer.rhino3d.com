---
title: Running Scripts from Macros
description: This guide explains how to set up and run macros and RhinoScripts.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Scripts', 'Macros', 'How To']
origin: http://wiki.mcneel.com/developer/macroscriptsetup
order: 1
keywords: ['script', 'Rhino', 'vbscript', 'macros']
layout: toc-guide-page
TODO: 'needs review and updated screencaptures'
---

 
## How To

### Creating button or alias for your macro or script

The simplest way to save and run your macro is from a toolbar button or alias.  If you don’t know how to make a new toolbar button or alias, look in the Help file.  There’s a good explanation.  Once you have your new button (or have chosen to edit an existing one), open the editor by <kbd>shift</kbd>+right-clicking on the button.  For an alias, you will do the same thing, but instead of creating a new button, go into *Options* > *Aliases* and use the *New* button to create a new alias.

### Use the macro editor to work out new macros

The *MacroEditor* command opens a text editing window in which you can type macros and try them out without the need to edit a button every time.  The run button on the lower edge of the editor runs the macro.  If there is selected text, it runs the selected text.  When it all runs to your satisfaction, copy and paste the macro to a toolbar button.

![Macro Editor]({{ site.baseurl }}/images/running-scripts-from-macros-01.png)

### Paste your macro or script into the button or alias

Now, there are two ways to approach associating the macro or script to your button or alias.  First and simplest is to just copy/paste the whole thing into the left or right button box (or in the alias box).  The advantage of the button method is that it is portable.  That is, if you copy or export the button to another installation the macro goes with it.  Once the test is pasted in, click *OK* to exit the button editor, and you’re ready to go!

The paste-in-button (or alias) method is fine for macros of Rhino commands and shorter, smaller scripts, but it gets a bit unwieldy to edit if there is a great deal of text.  For larger scripts, some people like to place them externally in a folder with a link so that Rhino can find them.  Both toolbar buttons and aliases can link to external scripts.  One advantage of this system is that all scripts are located in one spot so you can easily find and update them.  The problem here is that if you copy your button or workspace for use somewhere else, you have to remember to bring the script with it.

### Linking to external scripts

To set up an external scripts folder: Find a logical place to create your folder.  *Take care in choosing this folder. Make sure that the user has permissions to access it.*  Open the *Options* dialog, and navigate to the *Files* tab.  In the file search paths box, click the new button and then the little *...* button and browse to the location of the scripts folder.  Then click *OK*.  Exit the options dialog. Rhino will now go looking for scripts in this folder.

Currently Python does not read this section, so if you use Python scripts you will also need to do a similar operation inside the Python script editor: Open the editor with *EditPythonScript* and go to *Tools* > *Options* and enter the path to your folder in *Module Search Paths*.

To link your button or alias to an external script: The syntax used will depend on the type of script.  If it is a simple text file with normal Rhino commands (like a long macro), you will need to use the command *ReadCommandFile Filename.txt*  Substitute the name of your text file for *Filename.txt*.  Paste that string into the left or right button box and you’re good to go.  To run a *RhinoScript .rvb* file use the command *LoadScript Filename.rvb* instead.  In general, that’s all you need to do, but some scripts are written to run immediately on load.  Others are not, so some script tweaking may be necessary.

![Edit Toolbar Button Dialog]({{ site.baseurl }}/images/running-scripts-from-macros-02.png)

You can also paste an entire RhinoScript into a button. For that, start with the command *-_RunScript* (not *-_LoadScript*) followed by a space and an open parentheses.  At the end of the script you need a close parentheses.  For python scripts, you want to use *-_RunPythonScript* instead of just *-_RunScript*.

Don't forget the dash in front of the command, otherwise it will stop and prompt you for what script you want to run.  The underbar insures that the *_-Runscript* command will run in languages other than English, but it will not insure the actual script will do the same.  It has to be written correctly as well.

```
! _NoEcho -_Runscript (

Paste in
your entire
script here

)
```

The button editor showing pasted in complete RhinoScript should look something like this...

![Edit Toolbar Button Done]({{ site.baseurl }}/images/running-scripts-from-macros-03.png)

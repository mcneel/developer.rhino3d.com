---
title: Crash Dump Analysis
description: This guide discusses how to analyze crash dump files in Visual Studio.
author: ['Dale Fugier', '@dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/crashdumpanalysis
order: 1
keywords: ['rhino']
layout: toc-guide-page
TODO: 'needs screen-capture update and overall review.'
---

# {{ page.title }}

{{ page.description }}

## Overview

If Rhino crashes, two files are created on the user's desktop: *RhinoCrashDump.dmp* and *RhinoCrashDump.3dm*. The *.3DM* file is Rhino's last ditch effort to save the model.  The *.DMP* file can be used in Visual Studio to find the place in the source code where a Rhino plugin crashed.

## Analysis

Analyzing crash dumps is not a quick and easy way to diagnose crash bugs.  If a crash is repeatable, do not use crash dumps. Simply debug the crash by running the command in the debugger.  In a crash dump, no heap is available and only a limited amount of stack is available.  But with a little effort and thought, you can find the line where the crash occurred and see what arguments were passed to the functions.

Keep in mind you are debugging optimized code.  Some values of local variables (like loop counters and frequently used doubles) are kept in CPU registers and cannot be viewed in a watch window.

If you read a RhinoCrashDump.dmp file in Notepad.exe and search for “RHINOCRASHINFO” you will find a block of text like the following:

```
<RHINOCRASHINFO>
  <BUILD VERSION="YYYY-MM-DD" DATE="mmm dd yyyy" TIME="hh:mm"ss" />
  <COMMAND NAME="..." UUID="..." />
  <EXECUTABLE FILENAME="..." UUID="..." />
</RHINOCRASHINFO>
```

If the crash happens in a command that is in a plugin, the name of the plugin's *.RHP* file is in *<EXECUTABLE FILENAME>* and the id is in *<EXECUTABLE UUID>*.

*<BUILD DATE>* and *<BUILD TIME>* are the date and time the *.cpp* file that contains the crash dump exception handing code was compiled.

### Step-by-Step

1. **Determine which build of Rhino crashed**: Open the *RhinoCrashDump.dmp* file in Notepad.exe (or your favorite text editor) and search for `RHINOCRASHINFO`.  Then look for `B u i l d V e r s i o n = " YYYY - MM - DD "`... `YYYYMMDD` is the build that crashed.  If you are lucky, the other `RHINOCRASHINFO` values will give you a hint about what crashed.
1. **Get the build of Rhino that crashed**: To analyze the crash dump file, you need the same build of Rhino on your system that produced the crash dump.  If you do not have the same build, download it from the [Rhino download page](http://www.rhino3d.com/download).
1. **Copy files**: After you have determined the version of the crashed Rhino, copy the *RhinoCrashDump.dmp* into the same directory as the *Rhino.exe* file.  In most cases, this will be the following folder: *C:\\Program Files\\Rhinoceros\\System*.  Over your plugin's life you are likely to see many crashes.  So do yourself a big favor and rename the *RhinoCrashDump.dmp* file something descriptive. Also, copy your plugin's release *.RHP* and *.PDB* files into the same folder.
     <div class="bs-callout bs-callout-danger">
       <h4>WARNING</h4>
       <p>To be successful in performing crash dump analysis, save your release build .PDB files to use later.  Without your plugin's .PDB file, crash dump analysis is useless.</p>
     </div>
1. **Locate the crash**: Start a new instance of Developer Studio and from the menu use *File* > *Open Solution...* to bring up the *Open Solution* dialog box.  In the *Files of type: droplist box* select *Dump files (.dmp; .mdmp)*.  Then navigate to the Rhino System folder and double-click on *RhinoCrashDump.dmp*.  It may also be possible to double-click on the *dmp* file from Explorer and have Visual Studio open it.
     1. Once the dump is loaded (it doesn't take long), press the <kbd>F10</kbd> key.  When you are prompted to save *RhinoCrashDump.sln*, click the *Save* button.  The *Output window* will pop up and you can watch as the debugger attempts to reconstruct the state of the executable when the crash occurred.  This can take a while, especially if the debugger has to go to an external symbol server to download symbols.
     1. Eventually an error message box will pop up with *Break/Continue/Ignore/Help* buttons.  Click *Break* and examine the call stack for hints about what when wrong.

## Microsoft Symbol Server

You must have symbol information when you debug applications with various Microsoft tools.  Symbol files provide a footprint of the functions contained in executable files and dynamic-link libraries (*DLLs*). Also, symbol files can present a roadmap of the function calls that lead to the point of failure.  For example, you must have the symbols when you dump call stacks inside a debugger.

The Microsoft Symbol Server is built by using the SymSrv technology (*SymSrv.dll*) that is provided with the Debugging Tools for Windows package.  SymSrv builds a local symbol cache for fast, automatic symbol resolution.

You can use the symbol server to allow Visual Studio to automatically download the proper Microsoft symbols for debugging your Visual Studio project.  To allow Visual Studio to use the Microsoft Symbol Server, select *Tools* > *Options* and fill in the information listed below.

![Microsoft Symbol Server Options]({{ site.baseurl }}/images/crash_dump_analysis_01.png)

## Try this yourself

Below is a sample C++ plugin that will crash Rhino.  To test out crash dump analysis, download and build the plugin.  Then, launch Rhino and load the plugin using the `PlugInManager` command.  Then run the `TestSdkCrash` command.  While the *McNeel Error Reporting* dialog is displayed, copy the *RhinoCrashDump.dmp* from the desktop to some other location, and then click *Don't Send*.  Then follow the steps above to analyze the crash dump.

<a href="{{ site.baseurl }}/files/testsdkcrash.zip"><span class="glyphicon glyphicon-download">&nbsp;testsdkcrash.zip</span></a>

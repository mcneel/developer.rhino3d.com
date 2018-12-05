---
title: Crash Dump Analysis
description: This guide discusses how to analyze crash dump files in Visual Studio.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/crashdumpanalysis
order: 1
keywords: ['rhino']
layout: toc-guide-page
TODO: 'needs screen-capture update and overall review.'
---


## Overview

If Rhino crashes, two files are created on the user's desktop: *RhinoCrashDump.dmp* and *RhinoCrashDump.3dm*. The *.3DM* file is Rhino's last ditch effort to save the model.  The *.DMP* file can be used in Visual Studio to find the place in the source code where a Rhino plugin crashed.

### Configuration
Before you can analyze crashes, you'll need to set up visual studio to help you get symbols.

1. **Enable Symbol Servers**
    1. Open Visual Studio
    1. From the **Tools** menu, click **Options**
    1. Select the **Debugging** > **Symbols** tab
    1. In the *Symbol file (.pdb) locations* box, add:
        * http://s3.symbols.rhino3d.com/symbols/dujour
    1. Optionally add these symbol servers if you need symbols for OpenGL driver related crashes:
        * https://download.amd.com/dir/bin_2018
        * https://download.amd.com/dir/bin
        * https://driver-symbols.nvidia.com
    1. In the *Cache symbols in this directory* folder enter a folder where Visual Studio will cache symbols. Depending on the number of crashes you debug, this folder can get quite large.
    1. Under *Automatically load symbols for:* select **Load all modules, unless excluded**
    (Note that this will make debugging your project slow. To speed this up, select *Load only specified modules*)



### Debugging Crashes

  1. Download and extract the Zip archive containing the crash dump.
  1. Start Visual Studio 2017
  1. From the **File** menu, click **Open**
  1. Browse to the RhinoCrashDump.dmp file in the extracted folder
  1. Click **Debug using mixed**
  1. For details we've extracted about the crash, view the **RhinoCrashDump.dmp.xml** file.

### Try it!

Below is a sample C++ plugin that will crash Rhino.  To test out crash dump analysis:
  1. Download and build the <a href="{{ site.baseurl }}/files/testsdkcrash.zip">TestSdkCrash</a> plugin.
  1. Launch Rhino and load the plugin using the `PlugInManager` command.
  1. Run the `TestSdkCrash` command.  
  1. While the *McNeel Error Reporting* dialog is displayed, copy the *RhinoCrashDump.dmp* from the desktop to some other location, and then click *Don't Send*.
  1. Follow the steps above to analyze the crash dump.

### Storing symbols

In order to get the most out of your crashes, you need to save the symbols and source code from each of the builds. You'll also need to add source information into your PDB files before you store them in the symbol server.

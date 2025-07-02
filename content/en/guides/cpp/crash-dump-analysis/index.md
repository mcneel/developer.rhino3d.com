+++
aliases = ["/en/5/guides/cpp/crash-dump-analysis/", "/en/6/guides/cpp/crash-dump-analysis/", "/en/7/guides/cpp/crash-dump-analysis/", "/en/wip/guides/cpp/crash-dump-analysis/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide discusses how to analyze crash dump files in Visual Studio."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Crash Dump Analysis"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = "needs screen-capture update and overall review."
origin = "http://wiki.mcneel.com/developer/sdksamples/crashdumpanalysis"
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


## Overview

If Rhino crashes, two files are created on the user's desktop: *RhinoCrashDump.dmp* and *RhinoCrashDump.3dm*. The *.3dm* file is Rhino's last ditch effort to save the model.  The *.dmp* file can be used in Visual Studio to find the place in the source code where a Rhino plugin crashed.

### Configuration
Before you can analyze crashes, you'll need to set up Visual Studio to help you get symbols.

1. **Enable Symbol Servers**
    1. Open Visual Studio
    1. From the **Tools** menu, click **Options**
    1. Select **Debugging** > **General** and enable the following options:
        * *Enable source server support*
        * *Print source server diagnostic messages to the Output window*
        * *Allow source server for partial trust assemblies (Managed only)*
        * *Always run untrusted source server commands without prompting*
    1. Select **Debugging** > **Symbols**
    1. In the *Symbol file (.pdb) locations* box, add:
        * http://s3.symbols.rhino3d.com/symbols/dujour
        * https://msdl.microsoft.com/download/symbols
    1. Optionally add these symbol servers if you need symbols for video driver related crashes:
        * https://driver-symbols.nvidia.com
        * https://download.amd.com/dir/bin_2018
        * https://download.amd.com/dir/bin
        * https://software.intel.com/sites/downloads/symbols
    1. In the *Cache symbols in this directory* folder, enter a folder where Visual Studio will cache symbols. Depending on the number of crashes you debug, this folder can get quite large.
    1. Under *Symbol search preferences:* select **Search for all modules unless excluded**
    (Note that this will make debugging your project slow. To speed this up, select *Automatically choose what module symbols to search for*)


### Debugging Crashes

  1. Start Visual Studio
  1. From the **File** menu, click **Open**
  1. Browse to the **RhinoCrashDump.dmp** file in the extracted folder
  1. Click **Debug with Mixed**

### Try it!

Below is a sample C++ plugin that will crash Rhino.  To test out crash dump analysis:
  1. Download and build the <a href="/files/testsdkcrash.zip">TestSdkCrash</a> plugin.
  1. Launch Rhino and load the plugin using the `PlugInManager` command.
  1. Run the `TestSdkCrash` command.  
  1. While the *McNeel Error Reporting* dialog is displayed, copy the *RhinoCrashDump.dmp* from the desktop to some other location, and then click *Don't Send*.
  1. Follow the steps above to analyze the crash dump.

### Storing symbols

In order to get the most out of your crashes, you need to save the symbols (.pdb) and source code from each of the builds. You'll also need to add source information into your .pdb files before you store them in the symbol server.

### More

[Working with Debug Symbols and Source](https://learn.microsoft.com/en-us/shows/visual-studio-2022-launch-event/tips-and-tricks-tips-for-working-with-debug-symbols-and-source)

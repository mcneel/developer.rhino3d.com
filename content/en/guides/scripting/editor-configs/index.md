+++
title = "Script Editor Options"
description = "Provides information on editing and language support options in Script Editor"
type = "guides"
categories = ["Scripting"]
keywords = [ "", "" ]
languages = [ "C#", "Python", "CPython", "IronPython", "VB" ]
authors = ["ehsan"]
sdk = [ "RhinoCommon" ]
weight = 4

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

<style>
    .main-content img { zoom: 50%; }
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
    }
</style>

**Editor Options** dialog (*Tools > Options* menu) provides access to editor and language settings that are persistent.

Hovering over help icons provides more information about each option:

![](editor-options-tipdot.png)

## General Options

General options are under **General** tab of *Editor Options* dialog and are self explanatory:

![](editor-options-general.png)

Grasshopper Script Editor has a few layout options under *General* tab. *Window* menu also shows toggles for these options:

![](editor-options-general-embedded.png)

*Window > Toggle \** menu items provide toggles for Editor UI elements. Editor remembers the last UI layout before it is closed. See [Layout Options: Python](/guides/scripting/scripting-gh-python/#layout-options) or [C#](/guides/scripting/scripting-gh-csharp/#layout-options) for more information on these options.

## Editing Options

Editing options are language-specific. Each language tab has its own editing options:

![](editor-options-editing.png)

*Edit > Toggle \** menu items provide toggles for some of the options. These changes are in-session only and do not get saved to settings file. See [Editing Features](/guides/scripting/editor-editing/) for more information on these options.

## Language Support Options

Language Support options are language-specific. Each language tab has its own language options:

![](editor-options-langserver.png)

*Edit > Toggle \** menu items provide toggles for some of the options. These changes are in-session only and do not get saved to settings file. See [Editing Features](/guides/scripting/editor-editing/) for more information on these options.

## Python Paths

### Scripts Path

By default, Rhino adds these paths to Python 2 and 3 search paths (`sys.path`):

On Windows:

- **Shared** `%PROGRAMDATA%\McNeel\Rhinoceros\<version>.0\scripts` (if exists)
- **User** `%APPDATA%\McNeel\Rhinoceros\<version>.0\scripts`

On macOS:

- **Shared** `/Users/Shared/McNeel/Rhinoceros/<version>.0/scripts` (if exists)
- **User** `~/Library/Application Support/McNeel/Rhinoceros/<version>.0/scripts`

Note that the first path on either platform, is the shared path and takes precedence over the user path. So if python module `test` is available in both paths, the one under shared path will be imported. Shared `scripts` path are not created by default so there is not a conflict unless you, your system admin, or other third-party plugin intentionally places python modules or scripts in this path.

### Editor Paths

You can add a list of other search paths for each Python version in Editor options:

![](editor-options-python-paths.png)

Note that the order of these paths is important. First path on the list would be the first path to be search for a module.

Editor stores these paths in two `.rhinocode/python-3.pth` and `.rhinocode/python-2.pth` files. See [Path Files]({{< relref "/guides/scripting/advanced-pthfiles" >}}) for more information.
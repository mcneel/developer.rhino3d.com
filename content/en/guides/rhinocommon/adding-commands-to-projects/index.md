+++
aliases = ["/en/5/guides/rhinocommon/adding-commands-to-projects/", "/en/6/guides/rhinocommon/adding-commands-to-projects/", "/en/7/guides/rhinocommon/adding-commands-to-projects/", "/en/wip/guides/rhinocommon/adding-commands-to-projects/"]
authors = [ "dan", "callum" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates how to add additional commands to a RhinoCommon plugin project."
keywords = [ "adding", "RhinoCommon", "commands", "projects" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Adding Commands to Projects"
type = "guides"
weight = 6

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addcommand"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++


## Problem

A fresh project ([Windows](/guides/rhinocommon/installing-tools-windows/#rhinocommon-templates) or [Mac](/guides/rhinocommon/installing-tools-mac/#install-the-rhino-add-in)) is only a skeleton plugin project with a single command.  However, plugins can contain more than one command.  How does one add additional commands to plugin projects?

## Solution

To add a new command to your RhinoCommon plugin project, you simply need to define a new class that inherits from `Rhino.Commands.Command`.

An easy way to do this is to just use the *Empty RhinoCommmon Command* template. Here is how you do that:

### Windows

1. Make sure you have the [RhinoCommon Project Wizard](/guides/rhinocommon/installing-tools-windows/#rhinocommon-templates) installed.
1. Launch *Visual Studio* and open your plugin project.
1. From *Visual Studio*, navigate to *Project* > *Add New Item* menu item.
1. Select the *Empty RhinoCommmon Command* template from the list of installed templates.
1. Provide a unique file name that relates to the command you are adding.
1. Click the *Add* button.

### Mac

1. Make sure you have [Rhino.Templates](/guides/rhinocommon/installing-tools-mac/#install-the-rhino-add-in) installed.
1. Launch *Visual Studio Code* and open your plugin project folder.
1. Open _Visual Studio Code's Terminal_ via _Terminal (menu entry)_ > _New Terminal_, or using the command palette _(⌘ ⇧ P)_ and search for "Terminal".
1. Inside Terminal, run:
   ```pwsh
   dotnet new rhinocommand -n MyCommandName
   ```

## Related Topics

- [Installing Tools (Windows)](/guides/rhinocommon/installing-tools-windows)
- [Installing Tools (Mac)](/guides/rhinocommon/installing-tools-mac)

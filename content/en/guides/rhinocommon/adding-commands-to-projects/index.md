+++
aliases = ["/en/5/guides/rhinocommon/adding-commands-to-projects/", "/en/6/guides/rhinocommon/adding-commands-to-projects/", "/en/7/guides/rhinocommon/adding-commands-to-projects/", "/en/wip/guides/rhinocommon/adding-commands-to-projects/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates how to add additional commands to a RhinoCommon plugin project."
keywords = [ "adding", "RhinoCommon", "commands", "projects" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Adding Commands to Projects"
type = "guides"
weight = 6
override_last_modified = "2021-09-03T08:29:10Z"

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

The RhinoCommon Project Wizard ([Windows](/guides/rhinocommon/installing-tools-windows/#rhinocommon-templates) or [Mac](/guides/rhinocommon/installing-tools-mac/#install-the-rhino-add-in)) creates a skeleton plugin project with a single command.  However, plugins can contain more than one command.  How does one add additional commands to plugin projects?

## Solution

To add a new command to your RhinoCommon plugin project, you simply need to define a new class that inherits from `Rhino.Commands.Command`.

An easy way to do this is to just use the *Empty RhinoCommmon Command* template. Here is how you do that:

1. Make sure you have the RhinoCommon Project Wizard ([Windows](/guides/rhinocommon/installing-tools-windows/#rhinocommon-templates) or [Mac](/guides/rhinocommon/installing-tools-mac/#install-the-rhino-add-in)) installed.
1. Launch *Visual Studio* and open your plugin project.
1. From *Visual Studio*, navigate to *Project* > *Add New Item* menu item.  From *Visual Studio for Mac*, right-click on the project name in the *Solution Explorer* and navigate to *Add* > *New File...*.
1. Select the *Empty RhinoCommmon Command* template from the list of installed templates.
1. Provide a unique file name that relates to the command you are adding.
1. In *Visual Studio for Windows*, click the *Add* button.  In *Visual Studio for Mac*, click the *New* button.

## Related Topics

- [Installing Tools (Windows)](/guides/rhinocommon/installing-tools-windows)
- [Installing Tools (Mac)](/guides/rhinocommon/installing-tools-mac)

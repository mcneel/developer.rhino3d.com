+++
aliases = ["/en/5/guides/cpp/adding-online-help-to-your-plugin/", "/en/6/guides/cpp/adding-online-help-to-your-plugin/", "/en/7/guides/cpp/adding-online-help-to-your-plugin/", "/wip/guides/cpp/adding-online-help-to-your-plugin/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "Discusses how to add online help support to your Rhino plugin using C/C++."
keywords = [ "rhino", "help" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Adding Online Help to Your Plugin"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/pluginhelp"
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

Once you have your Rhino plugin completed, you may want to add online help support to help your customers use your plugin efficiently and properly.  Most Windows applications provide online help in the form of an HTML help file.

## Authoring Tools

HTML help files are made with help authoring tools.

Microsoft provides a free utility called the [HTML Help Workshop](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=00535334-c8a6-452f-9aa0-d597d16580cc) that can compile existing HTML files into an HTML help file (.chm). This is a fairly low-level utility in that it will only build HTML help files - it will not create or edit content. Thus, most who are looking to produce online help are looking for something a bit more full featured.

MadCap make a popular help authoring tool called [MadCap Flare](http://www.madcapsoftware.com/products/flare/) that will help you create, edit, and publish professional quality topic based technical content.  This is the tool used to create the help files for Rhino.

There are several other tools available on the market.  Google "Create HTML Help File" to see the list.

## Plugin Support

You can add your plugin to Rhino's *Help* > *Plug-ins* menu by overriding the following two virtual functions:

1. `CRhinoPlugIn::AddToPlugInHelpMenu`: Called by Rhino to determine if the plugin name should be added to the Rhino *Help* > *Plug-ins* menu.
1. `CRhinoPlugIn::OnDisplayPlugInHelp`: Called by Rhino if `CRhinoPlugIn::AddToPlugInHelpMenu` returns true and the menu item associated with this plugin is selected.

Details on both of these virtual function can be found in *rhinoSdkPlugIn.h*.

## Command Support

While running a Rhino command, you can press <kbd>F1</kbd> to bring up online help for that command.  Your plugin commands can do the same.  Simply override the `CRhinoCommand::DoHelp` virtual function.  If your command is running when the user presses <kbd>F1</kbd>, this member will be called.

Also, if your want your command's help to appear in Rhino's command help dockable window (*Help* > *Command Help*), then override the `CRhinoCommand::ContextHelpURL` virtual function.

Details on both of these virtual function can be found in *rhinoSdkCommand.h*.

## Dialog Support

There are a couple of ways you can add help support to dialog boxes.  The first is to simply place a "Help" button somewhere on the form.

Also, if your dialog box has focus and the user presses <kbd>F1</kbd>, Windows will send a WM_HELPINFO message to it.  So, by adding a message handler to your dialog box, you can capture these notifications and display the requested information.

And, if you add the "Context Help" style to your dialog box resource, a ? icon will appear in the upper right corner of the window.  Now, if the user clicks the ? icon and then clicks a control, your dialog's `OnHelpInfo` implementation will and passed information about the control that was clicked.

MSDN had lots of information on how to add context help to dialog boxes.

## Related Topics

- [HTML Help Workshop (on Microsoft.com)](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=00535334-c8a6-452f-9aa0-d597d16580cc)
- [MadCap Flare](http://www.madcapsoftware.com/products/flare/)

+++
aliases = ["/en/en/5/guides/rhinocommon/create-deploy-plugin-toolbar/", "/en/6/guides/rhinocommon/create-deploy-plugin-toolbar/", "/en/7/guides/rhinocommon/create-deploy-plugin-toolbar/", "/wip/guides/rhinocommon/create-deploy-plugin-toolbar/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide covers the creation and deployment of plugin toolbars."
keywords = [ "RhinoCommon", "C/C++", "Rhino", "Toolbar", "Plugin" ]
languages = [ "C#", "C/C++" ]
sdk = [ "RhinoCommon", "C/C++" ]
title = "Creating and Deploying Plugin Toolbars"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = ""
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


## Question

How can I create one or more toolbars for my plugin, and how can I deploy these toolbars with my plugin?

## Answer

If you want to create Rhino-style toolbars, then use Rhino's `Toolbar` command. You can save your custom toolbars in your own Rhino User Interface (RUI) file. For details on creating toolbars, see the Rhino help file.

If you give your custom RUI file the exact same name as the plugin RHP file and install it in the folder containing the RHP file, then Rhino will automatically open it the first time your plugin loads.

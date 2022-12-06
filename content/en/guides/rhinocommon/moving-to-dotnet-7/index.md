+++
authors = []
categories = []
description = "This guide walks you through making the transition to .NET 7"
keywords = [ ".NET", "RhinoCommon", "Plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Moving to .NET 7"
type = "guides"
weight = 4

[admin]
TODO = "Author this page"
origin = ""
picky_sisters = ""
state = "In Progress"

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true
+++

Things plugin authors should be aware of when running in .NET 7:

- Target .NET 4.8 for your plugin so it runs on either runtime.
- How to enable debugging from Visual Studio when running in .NET Core/7.
- Link to: how yak packages specify if they are built for .NET 7, .NET 6, .NET 4.8, or even possibly have many versions.

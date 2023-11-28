+++
title = ""
description = ""
type = "guides"
categories = ["Scripting"]
keywords = [ "", "" ]
languages = [ "C#", "Python", "CPython", "IronPython", "VB" ]
authors = ["eirannejad"]
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


## Script Component

## First Script

## Script Inputs and Outputs

### Type Hinting

## Edit Script

## Run Scripts

## Debugging Scripts

### Debugging Multiple Scripts

## Using Packages

### Python Packages

### Python Libraries (Modules)

### NuGet Packages

## Editor Features

Script editor has other noteworthy features. Here we highlight a few that are used more often:

### Search

Click on the **Search** tab to open the Search panel. Searching for a keyword will show all the matches for all the open scripts in the panel. You can click on any matched item to navigate to the script and line:

![](30.png)

### Help

Click on the **Help** tab to open the Help panel. This panel provides a simple method to get help on Rhino and Grasshopper APIs and provided python modules:

![](31.png)

Use the search field to search for class or method names. The info panel at the bottom provides some info about the method and its parameters:

![](32.png)

<!-- If the selected member has an online documentation, a preview tab opens in the editor showing the contents:

![](33.png) -->

- open Grasshopper
- drop a Maths > Script component on canvas
- wait for langs to initialize
- no script - note the language menu
- choose language
- add a few inputs
- add a few outputs
- modify the hinting - convertors not casting!
- hit run
- put a breakpoint
- hit debug
- see values in variables
- save - run unsaved script
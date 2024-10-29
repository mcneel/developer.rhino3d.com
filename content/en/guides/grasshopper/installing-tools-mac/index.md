+++
aliases = ["/en/5/guides/grasshopper/installing-tools-mac/", "/en/6/guides/grasshopper/installing-tools-mac/", "/en/7/guides/grasshopper/installing-tools-mac/", "/en/wip/guides/grasshopper/installing-tools-mac/"]
authors = [ "dan", "callum" ]
categories = [ "Getting Started" ]
description = "This guide covers all the necessary tools required to author Grasshopper components on Mac."
keywords = [ "first", "grasshopper", "components" ]
languages = [ "C#" ]
sdk = [ "Grasshopper" ]
title = "Installing Tools (Mac)"
type = "guides"
weight = 2

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++


By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging Grasshopper components using RhinoCommon in Rhino for Mac.

## Prerequisites

This guide presumes you have an:

- [Apple Mac](http://store.apple.com/) running [macOS](https://www.apple.com/osx/) Monterey (12) or later.
- [Rhino for Mac](https://www.rhino3d.com/download/)

## Install Visual Studio Code

{{< call-out info "What happened to Visual Studio for Mac?" >}}
Visual Studio for Mac has been [retired by Microsoft](https://learn.microsoft.com/en-us/visualstudio/mac/what-happened-to-vs-for-mac?view=vsmac-2022).
{{< /call-out >}}

#### Step-by-Step

1. *[Download Visual Studio Code](https://code.visualstudio.com/)*.
1. Once you have downloaded the *VSCode-darwin-universal.zip*, double-click it to unzip.
1. Drag Visual Studio Code to the */Applications* folder.
1. Open Visual Studio Code, you will need to click "Open" the first time you open it.
1. You will need to install some packages before starting, luckily all the required pacakges are bundled together. These can be found by clicking "Extensions" on the left side bar:
   - [Intellicode for C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscodeintellicode-csharp)
   - [NuGet Gallery Plugin](https://marketplace.visualstudio.com/items?itemName=patcx.vscode-nuget-gallery) (*Recommended*)
1. Restart Visual Studio Code.
1. Visual Studio Code is installed in your */Applications* folder. You will want to *drag its icon to your Dock* for future use or - if it's running - right/option-click the icon in the Dock and select *Keep in Dock*.

## Next Steps

*Congratulations!*  You have all the tools necessary to build a Grasshopper component on macOS.  *Now what?*

Check out the [Your First Component (Mac)](/guides/grasshopper/your-first-component-mac) guide for instructions building - your guessed it - your first component.

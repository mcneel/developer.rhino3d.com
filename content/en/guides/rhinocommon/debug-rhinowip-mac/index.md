+++
aliases = ["/en/5/guides/rhinocommon/debug-rhinowip-mac/", "/en/6/guides/rhinocommon/debug-rhinowip-mac/", "/en/7/guides/rhinocommon/debug-rhinowip-mac/", "/en/wip/guides/rhinocommon/debug-rhinowip-mac/"]
authors = [ "dan" ]
categories = [ "Deprecated" ]
description = "This guide explains how to debug using the RhinoWIP for Mac."
keywords = [ "first", "RhinoCommon", "Plugin", "RhinoWIP" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Debug in RhinoWIP (Mac)"
type = "guides"
weight = 1
override_last_modified = "2021-09-03T08:29:10Z"

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

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>This guide is deprecated.  You can debug in the RhinoWIP using the RhinoCommon Visual Studio for Mac extension.  See the <a href="/guides/rhinocommon/installing-tools-mac">Installing Tools (Mac)</a> guide for more information.</p>
</div>

By the end of this guide, you should understand how to modify your plugin's C# project file in order to target and debug using RhinoWIP.

## Prerequisites

This guide presumes you have [installed all the necessary tools](/guides/rhinocommon/installing-tools-mac) and know how to [build and debug a plugin using RhinoCommon with Rhinoceros](/guides/rhinocommon/your-first-plugin-mac).  

It also presumes you have downloaded and installed [the latest RhinoWIP](http://www.rhino3d.com/go/download/rhino-for-mac/wip/latest).

## Edit References

Your plugin requires references to RhinoCommon dlls that are contained within the Rhino application bundle.  The default RhinoCommon Plugin template that comes with the Rhino Xamarin Studio AddIn references *Eto*, *Rhino.UI*, and *RhinoCommon*:

![Bundle References](/images/debug-rhinowip-mac-01.png)

...which are all contained within the *Rhinoceros.app* bundle.

We want to target those found in the *RhinoWIP.app* bundle.  Unfortunately, Visual Studio for Mac does not allow you to browse to references that are contained within an application bundle.  We will have to "manually" change these references so that they target the appropriate versions contained in RhinoWIP.

#### Step-by-Step

1. In Visual Studio for Mac, *right/option-click* on the project name and select *Tools* > *Edit File*...  
![Visual Studio for Mac Edit File](/images/debug-rhinowip-mac-02.png)
1. Use Visual Studio for Mac's *Search* > *Replace* function to find *\Applications\Rhinoceros.app* and replace it with *\Applications\RhinoWIP.app*...
![Search and Replace](/images/debug-rhinowip-mac-03.png)
1. Verify that these changes are only happening with the `<ItemGroup>` that contains `<Reference>` entries.  Accept your *\Applications\RhinoWIP.app* replacements to make the change.  If you are not using Nuget packages, you will also need to add some changes to the default hint paths so they search the proper location within the app bundle:

        <ItemGroup>
          <Reference Include="System" />
          <Reference Include="System.Core" />
          <Reference Include="System.Drawing" />
          <Reference Include="RhinoCommon">
            <HintPath>..\..\Applications\RhinoWIP.app\Contents\Frameworks\RhCore.framework\Resources\RhinoCommon.dll</HintPath>
            <Private>False</Private>
          </Reference>
          <Reference Include="Rhino.UI">
            <HintPath>..\..\Applications\RhinoWIP.app\Contents\Frameworks\RhCore.framework\Resources\Rhino.UI.dll</HintPath>
            <Private>False</Private>
          </Reference>
          <Reference Include="Eto">
            <HintPath>..\..\Applications\RhinoWIP.app\Contents\Frameworks\RhCore.framework\Resources\Eto.dll</HintPath>
            <Private>False</Private>
          </Reference>
        </ItemGroup>
1. *Save* and *Close* your project's *.csproj*.
1. The project will reload automatically.  In the *Solution Explorer*, select any of the three references you just changed above.  If you examine their properties (*right/option-click* > *Properties*), you will notice they are now referencing the *RhinoWIP.app* versions.
1. *Build* and *Run*.  Your plugin's *debugging session* should now *launch with RhinoWIP*.

---
title: Creating a Skin (Windows)
description: This guide outlines the tools for RhinoCommon developers to wrap their application around Rhino by creating custom Skin.  Custom skins are supported on Windows only.
authors: ['dale_fugier']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/rhinocommon/skin
order: 2
keywords: ['skin', 'RAP', 'rhino', 'RhinoCommon']
layout: toc-guide-page
---


## Overview

Rhino allows developers to customize most of Rhino's interface so that the application appears to be their own.  We call this a custom *Skin*.  With a custom Skin, you can change the application icon, splash screen, the application name etc.

Creating a custom Skin for Rhino involves creating a custom skin assembly:

*skin name.rhs* This is a regular .NET Assembly (*.DLL*) that implements the skin's icon, splash screen, application name, etc.  In this guide, we will refer this to the Skin DLL. See a full list of methods and properties on the [Skin class documentation]({{ site.baseurl }}/api/RhinoCommon/html/T_Rhino_Runtime_Skin.htm).

## Create the Skin DLL

To create the Skin DLL:

1. Launch *Visual Studio* and add a new Class Library project to your solution.
1. In the new Class Library project, add a reference to *RhinoCommon.dll*, which is found in Rhino's *System* folder. Note: make sure, after adding the reference, to set the properties of the reference to *Copy Local = False*.
1. Create a new class that inherits from `Rhino.Runtime.Skin`.
1. Add a post build event to the project to rename the assembly from *.dll* to *.rhs*:
```
Copy "$(TargetPath)" "$(TargetDir)$(ProjectName).rhs"
Erase "$(TargetPath)"
```

## Skin Class

The skin class can override basic properties, like the `ApplicationName`:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs" data-toggle="pill">C#</a></li>
  <li><a href="#vb" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">
```cs
namespace MySkin
{
  public class MyHippoSkin : Rhino.Runtime.Skin
  {
    protected override string ApplicationName
    {
      get
      {
        return "Hippopotamus";
      }
    }
  }
  // You can override more methods and properties here
}
```
{: #cs .tab-pane .fade .in .active}

```vbnet
Namespace MySkin
    Public Class MyHippoSkin
        Inherits Rhino.Runtime.Skin
        Protected Overrides ReadOnly Property ApplicationName() As String
            Get
                Return "Hippopotamus"
            End Get
        End Property
    End Class
    ' You can override more methods and properties here
End Namespace
```
{: #vb .tab-pane .fade .in}

</div>

## Installation

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>Modifying the registry incorrectly can have negative consequences on your system's stability and even damage the system.</p>
</div>

To install your custom Skin, use *REGEDIT.EXE* to add a scheme key to your registry with a path to your Skin DLL. For example:

| **Item** |    |    | **Value** |
|:--------|:----:|:----:|:--------|
| Subkey   |    |    | HKEY_LOCAL_MACHINE\SOFTWARE\McNeel\Rhinoceros\6.0\Scheme: MySkin   |
| Entry name   |    |    | SkinDLLPath   |
| Type   |    |    | REG_SZ   |
| Data value   |    |    | C:\Src\MySkin\Bin\Release\MySkin.rhs   |

## Testing

You can now test your custom Skin by creating shortcut to your Rhino executable with `/scheme="<scheme name from the previous step>"` as command line argument.  For example:

*C:\Program Files\Rhino WIP\System\Rhino.exe" /scheme=MySkin*

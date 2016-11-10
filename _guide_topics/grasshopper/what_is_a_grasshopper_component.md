---
title: What is a Grasshopper Component?
description: This guide gives an overview of custom Grasshopper components.
authors: ['David Rutten']
author_contacts: ['DavidRutten']
apis: ['Grasshopper']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Overview']
origin: http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm
order: 1
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
TODO: 'needs to be reviewed for accuracy.  Also, needs a little more high-level info'
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

This guide also explains the hierarchy of all assemblies involved with the Grasshopper plugin.  This is important for component developers so they know which Assembly References they need to have in order to compile a Grasshopper Component Library.  It also provides some background information which is useful when communicating with other developers.

## Rhino Plugin Architecture

Grasshopper is a .NET ([RhinoCommon]({{ site.baseurl }}/guides/rhinocommon/what_is_rhinocommon/)) plugin for Rhino 5 for Windows and later ([a version for Rhino 5 for Mac is currently in beta](http://www.grasshopper3d.com/page/grasshopper-for-mac)).  It was written using Microsoft Visual Studio Professional using both VB.NET and C# source compiled against the .NET Framework.  It is recommended, though not required, that you target the same framework when developing Grasshopper Component Libraries.

Our aim is to keep Grasshopper dependencies as conservative as possible.  However, it is possible that we will switch to a higher version number of Rhino or .NET if this new version fixes crucial bugs or exposes useful functions.

## .NET Component Library

The Grasshopper project type is *Class Library*, meaning it cannot be run as a stand-alone application.  *Grasshopper.dll* is loaded by a [Rhino plugin]({{ site.baseurl}}/guides/general/what_is_a_rhino_plugin/) called *GrasshopperPlugin.rhp*.

## Assembly References

As a Class Library, Grasshopper references namespaces in addition to *RhinoCommon.dll*, some of these are standard namespaces provided by the .NET Framework, others are 3rd-party assemblies and others still are written by McNeel developers but are shipped separately for technical reasons. Some of these assemblies need to be referenced by Component developers, while others can be safely ignored.  The following table lists all assemblies referenced by *Grasshopper.dll*:

<div class="table-responsive" align="center">
<table class="table">
  <thead>
    <tr style="border-bottom:1pt solid black;">
      <th>Assembly</th>
      <th>Author</th>
      <th>Purpose</th>
      <th>Required</th>
    </tr>
  </thead>
  <tbody class="table-striped index_table">
  <tr>
    <td><i><a href="{{ site.baseurl }}/guides/rhinocommon/what_is_rhinocommon/">RhinoCommon.dll</a></i></td>
	  <td><a href="http://www.mcneel.com">McNeel</a></td>
	  <td>Rhinoceros .NET SDK</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td><i>GH_IO.dll</i></td>
    <td><a href="http://www.mcneel.com">McNeel</a></td>
    <td>Grasshopper Input/Output library required to read and write Grasshopper files.</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td><i>GH_Util.dll</i></td>
    <td><a href="http://www.mcneel.com">McNeel</a></td>
    <td>Grasshopper utility library containing some peripheral algorithms.</td>
    <td>Optional</td>
  </tr>
  <tr>
    <td><i>QWhale.*.dll</i></td>
    <td><a href="http://www.qwhale.net/">Quantum Whale</a></td>
    <td>Syntax highlighter functionality.  Contains a total of 5 dlls.</td>
    <td>Optional</td>
  </tr>
  <tr>
    <td><i><a href="https://msdn.microsoft.com/en-us/library/system(v=vs.110).aspx">System</a></i></td>
    <td><a href="https://www.microsoft.com/net">Microsoft</a></td>
    <td>Base .NET Namespace.</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td><i><a href="https://msdn.microsoft.com/en-us/library/system.drawing(v=vs.110).aspx">System.Drawing</a></i></td>
    <td><a href="https://www.microsoft.com/net">Microsoft</a></td>
    <td>.NET namespace involved with drawing shapes and text.</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td><i><a href="https://msdn.microsoft.com/en-us/library/system.windows.forms(v=vs.110).aspx">System.Windows.Forms</a></i></td>
    <td><a href="https://www.microsoft.com/net">Microsoft</a></td>
    <td>.NET namespace involved with dialogs and controls.</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td><i><a href="https://msdn.microsoft.com/en-us/library/system.collections.generic(v=vs.110).aspx">System.Collections.Generic</a></i></td>
    <td><a href="https://www.microsoft.com/net">Microsoft</a></td>
    <td>.NET namespace containing useful list classes.</td>
    <td>Yes</td>
  </tr>
 </tbody>
 </table>
 </div>

---

## Related topics

- [Developer Prerequities]({{ site.baseurl }}/guides/general/rhino_developer_prerequisites/)
- [What is a Rhino Plugin?]({{ site.baseurl}}/guides/general/what_is_a_rhino_plugin/)
- [What is RhinoCommon?]({{ site.baseurl }}/guides/rhinocommon/what_is_rhinocommon/)
- [Your First Component]({{ site.baseurl }}/guides/grasshopper/your_first_component_windows)

+++
aliases = ["/en/5/", "/en/6/", "/en/7/", "/en/wip/"]
description = "Official developer resources for Rhino and Grasshopper.  Rhino developer tools are royalty free and include support."
title = "Rhino and Grasshopper Developer Documentation"
type = "home"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = []
since = 0

[cascade]
list_group = "uncategorized"
+++

## New in Rhino 9

{{< card-gallery columns="4" >}}
{{< feature-card page="/guides/cpp" url="/guides/cpp/your-first-plugin-crossplatform/" image="/images/new-in-v9/cpp-mac.png" title="C++ SDK on Mac" description="Build C++ plugins for Windows and Mac." >}}
{{< feature-card page="/guides/compute/compute-linux-getting-started" image="/images/new-in-v9/compute-linux.png" title="Rhino.Compute on Linux" description="Run Rhino and Grasshopper on a Linux server." >}}
{{< feature-card page="/guides/grasshopper2" image="/images/new-in-v9/gh2-component.png" title="Grasshopper 2 components" description="Make your first Grasshopper 2 component on Windows or Mac." >}}
{{< feature-card page="/guides/rhinopython/python-3-in-rhino" image="/images/new-in-v9/python3.png" title="Python 3 and the Script Editor" description="Write Python 3 and C# scripts in Rhino and Grasshopper." >}}
{{< /card-gallery >}}

[See all that is new for developers in Rhino 9](/guides/general/new-in-v9/).

## Development Platform Overview

<br>

<div class="table-responsive" align="center">
<table class="table" style="width:940px;">
  <thead>
    <tr style="border-bottom:1pt solid black;">
      <th style="text-align: left;">What</th>
      <th style="text-align: left;">Where</th>
      <th style="text-align: left;">How</th>
      <th style="text-align: left;">Why</th>
    </tr>
  </thead>
  <tbody class="table-striped index_table">
  <tr>
    <td><a href="/guides/rhinocommon" title="RhinoCommon: The cross-platform toolkit for Rhino and Grasshopper"> RhinoCommon</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/vb-logo-small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Write Rhino plugins & Grasshopper components</td>
  </tr>
  <tr>
    <td><a href="/guides/rhinopython" title="Rhino.Python: Pythonic in three dimensions!"> Rhino.Python</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Cross-platform scripting</td>
  </tr>
  <tr>
    <td><a href="/guides/opennurbs" title="openNURBS is free and open source"> openNURBS</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">3dm file reading and writing</td>
  </tr>
  <tr>
    <td><a href="/guides/rhinoscript" title="RhinoScript is based on Microsoft's VBScript language"> RhinoScript</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/vbscript-logo-small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Rhino for Windows scripting</td>
  </tr>
  <tr>
    <td><a href="/guides/cpp" title="C/C++ SDK for Rhino"> C/C++</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Write Rhino plugins</td>
  </tr>
   <tr>
    <td><a href="/guides/grasshopper" title="Grasshopper Component Development"> Grasshopper</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="OS X" class="index_table_icon" title="Mac OS X"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/vb-logo-small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Grasshopper components</td>
  </tr>
  <!--
  <tr>
    <td><a href="/guides/#rdk" title="Renderer Development Kit"> RDK</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"><img src="/images/vbscript-logo-small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Renderer plugin development on Windows.</td>
  </tr>
  -->
  <!-- RAP is really just a feature of the C/C++ SDK and the RhinoCommon SDK
  <tr>
    <td><a href="/guides/#rap" title="Rhino Application Platform"> RAP</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">"Skinning" Rhino for Windows.</td>
  </tr>
  -->
  <!--
  <tr>
    <td><a href="/guides/#zoo" title="Zoo License Manager Plugins"> Zoo</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Zoo license manager plugins on Windows</td>
  </tr>
  -->
 </tbody>
 </table>
 </div>



<div align="center">


<p>Still unclear?  Browse the <a href="/guides/">Guides</a>.  Ask a question in <a href="/guides/general/contributing/#discourse">the Forum</a>.  Check out the <a href="/guides/general/frequently-asked-questions/">FAQ</a>. Ask <a href="/guides/general/contributing/#contacts">a developer</a>.</p>

<p><a href="/license">{{< awesome "fas fa-balance-scale" >}} MIT License</a>. Rhino developer tools are royalty free and include support. </p>
</div>


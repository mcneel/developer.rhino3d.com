---
title: Rhino and Grasshopper Developer Documentation
description: Official developer resources for Rhino and Grasshopper.  Rhino developer tools are royalty free and include support.
layout: fullwidth-page
---
<!--
<div align="center"><h1 id="getting-started-with-rhino-development">Getting Started with Rhino Development</h1></div>
-->
<!--
<div>
  <table style="width:100%; border: 1px; margin: 0 auto; padding:0; border-spacing: 0px; border-collapse: separate;">
    <tbody>
      <tr>
        <td style="padding: 20px; text-align: center;">
          <a href="{{ site.baseurl }}/guides/#grasshopper" title="Grasshopper Components">
            <img src="{{ site.baseurl }}/images/ghcomponent_logo_intro.png" class="index_use_images">
          </a>
        </td>
        <td style="padding: 20px; text-align: center;">
          <a href="{{ site.baseurl }}/guides/#rhinocommon" title="RhinoCommon: The cross-platform .NET API for Rhino and Grasshopper">
            <img src="{{ site.baseurl }}/images/rhinocommon_logo_intro.png" class="index_use_images">
          </a>
        </td>
        <td style="padding: 20px; text-align: center;">
          <a href="{{ site.baseurl }}/guides/#rhinopython" title="Rhino.Python: Pythonic in three dimensions!">
            <img src="{{ site.baseurl }}/images/rhino_python_logo_intro.png" class="index_use_images">
          </a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
-->
<div class="embed-responsive embed-responsive-16by9">
  <iframe class="embed-responsive-item" src="https://player.vimeo.com/video/188730450"></iframe>
</div>

<br>

<div class="table-responsive" align="center">
<table class="table" style="width:940px;">
  <thead>
    <tr style="border-bottom:1pt solid black;">
      <th>What</th>
      <th>Where</th>
      <th>How</th>
      <th>Why</th>
    </tr>
  </thead>
  <tbody class="table-striped index_table">
  <tr>
    <td><a href="{{ site.baseurl }}/guides/rhinocommon" title="RhinoCommon: The cross-platform toolkit for Rhino and Grasshopper"> RhinoCommon</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/vb_logo_small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="{{ site.baseurl }}/images/python_logo_small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Write Rhino plugins & Grasshopper components</td>  
  </tr>
  <tr>
    <td><a href="{{ site.baseurl }}/guides/rhinopython" title="Rhino.Python: Pythonic in three dimensions!"> Rhino.Python</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="{{ site.baseurl }}/images/python_logo_small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Cross-platform scripting</td>  
  </tr>
  <tr>
    <td><a href="{{ site.baseurl }}/guides/opennurbs" title="openNURBS is free and open source"> openNURBS</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/cpp_logo_small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">3dm file reading and writing</td>  
  </tr>
  <tr>
    <td><a href="{{ site.baseurl }}/guides/rhinoscript" title="RhinoScript is based on Microsoft's VBScript language"> RhinoScript</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/vbscript_logo_small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Rhino for Windows scripting</td>  
  </tr>
  <tr>
    <td><a href="{{ site.baseurl }}/guides/cpp" title="C/C++ SDK for Rhino for Windows"> C/C++</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/cpp_logo_small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Rhino for Windows plugins</td>  
  </tr>
   <tr>
    <td><a href="{{ site.baseurl }}/guides/#grasshopper" title="Grasshopper Component Development"> Grasshopper</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="index_table_icon" title="Mac OS X"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/vb_logo_small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="{{ site.baseurl }}/images/python_logo_small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Grasshopper components</td>  
  </tr>
  <!--
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#rdk" title="Renderer Development Kit"> RDK</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/cpp_logo_small.png" alt="C/C++" class="index_table_icon" title="C/C++"><img src="{{ site.baseurl }}/images/vbscript_logo_small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Renderer plugin development on Windows.</td>  
  </tr>
  -->
  <!-- RAP is really just a feature of the C/C++ SDK and the RhinoCommon SDK
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#rap" title="Rhino Application Platform"> RAP</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/cpp_logo_small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">"Skinning" Rhino for Windows.</td>  
  </tr>
  -->
  <!--
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#zoo" title="Zoo License Manager Plugins"> Zoo</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/cpp_logo_small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Zoo license manager plugins on Windows</td>  
  </tr>
  -->
  <tr>
    <td><a href="{{ site.baseurl }}/guides/rhinomobile" title="Tools for using 3dm files in mobile applications"> RhinoMobile</a></td>
	<td><img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="index_table_icon" title="Android"><img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="index_table_icon" title="Apple iOS"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"></td>
    <td class="index_table_primary_use">3D mobile application development</td>  
  </tr>
 </tbody>
 </table>
 </div>

{: rules="groups"}

<div align="center">
<p><i>WARNING</i>: This is the Work-In-Progress version of this site & should not be considered stable. <a href="{{site.baseurl_orig}}{{ page.url }}">View the current stable version instead.</a></p>

<p>Still unclear?  Browse the <a href="{{ site.baseurl }}/guides/">Guides</a>.  Ask a question in <a href="{{ site.baseurl }}/guides/general/contributing/#discourse">the Forum</a>.  Check out the <a href="{{ site.baseurl }}/guides/general/frequently_asked_questions/">FAQ</a>. Ask <a href="{{ site.baseurl }}/guides/general/contributing/#contacts">a developer</a>.</p>

<p>Rhino developer tools are royalty free and include support.</p>

</div>

+++
aliases = ["/en/5/", "/en/6/", "/en/7/", "/en/wip/"]
description = "Offizielle Entwickler-Ressourcen für Rhino und Grasshopper.  Rhino Entwickler-Tools sind gebührenfrei und enthalten Support."
title = "Entwickler-Dokumentation für Rhino und Grasshopper"
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

{{< call-out note "Brauchen Sie Hilfe beim Migrieren von C# nach Rhino 8?" >}}
Werfen Sie einen Blick in den [Leitfaden zum Umzug auf .NET 7](/guides/rhinocommon/moving-to-dotnet-7/).
{{< /call-out >}}

{{< vimeo 188730450 >}}

<br>

<div class="table-responsive" align="center">
<table class="table" style="width:940px;">
  <thead>
    <tr style="border-bottom:1pt solid black;">
      <th style="text-align: left;">Was</th>
      <th style="text-align: left;">Wo</th>
      <th style="text-align: left;">Wie</th>
      <th style="text-align: left;">Warum</th>
    </tr>
  </thead>
  <tbody class="table-striped index_table">
  <tr>
    <td><a href="/guides/rhinocommon" title="RhinoCommon: The cross-platform toolkit for Rhino and Grasshopper"> RhinoCommon</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/vb-logo-small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Rhino-Plug-ins und Grasshopper-Komponenten schreiben</td>
  </tr>
  <tr>
    <td><a href="/guides/rhinopython" title="Rhino.Python: Pythonic in three dimensions!"> Rhino.Python</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Plattformübergreifendes Skripting</td>
  </tr>
  <tr>
    <td><a href="/guides/opennurbs" title="openNURBS is free and open source"> openNURBS</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Lesen und Schreiben von 3dm-Dateien</td>
  </tr>
  <tr>
    <td><a href="/guides/rhinoscript" title="RhinoScript is based on Microsoft's VBScript language"> RhinoScript</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/vbscript-logo-small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Skripting für Rhino für Windows</td>
  </tr>
  <tr>
    <td><a href="/guides/cpp" title="C/C++ SDK for Rhino for Windows"> C/C++</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Plug-ins für Rhino für Windows</td>
  </tr>
   <tr>
    <td><a href="/guides/grasshopper" title="Grasshopper Component Development"> Grasshopper</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="OS X" class="index_table_icon" title="Mac OS X"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/vb-logo-small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Grasshopper-Komponenten</td>
  </tr>
  <!--
  <tr>
    <td><a href="/guides/#rdk" title="Renderer Development Kit"> RDK</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"><img src="/images/vbscript-logo-small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Entwicklung von Render-Plug-ins auf Windows.</td>
  </tr>
  -->
  <!-- RAP ist tatsächlich nur eine Funktion von C/C++ SDK und RhinoCommon SDK
  <tr>
    <td><a href="/guides/#rap" title="Rhino Application Platform"> RAP</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">"Skinning" in Rhino für Windows.</td>
  </tr>
  -->
  <!--
  <tr>
    <td><a href="/guides/#zoo" title="Zoo License Manager Plugins"> Zoo</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Zoo-Lizenzmanager-Plug-ins auf Windows</td>
  </tr>
  -->
  <!--
  <tr>
    <td><a href="/guides/rhinomobile" title="Tools for using 3dm files in mobile applications"> RhinoMobile</a></td>
	<td><img src="/images/android-logo-small.png" alt="Android" class="index_table_icon" title="Android"><img src="/images/ios-logo-small.png" alt="iOS" class="index_table_icon" title="Apple iOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"></td>
    <td class="index_table_primary_use">Entwicklung von 3D-Mobilanwendungen</td>
  </tr>
  -->
 </tbody>
 </table>
 </div>



<div align="center">


<p>Gibt es noch Unklarheiten?  Suchen Sie in den <a href="/guides/">Leitfäden</a>.  Fragen Sie im <a href="/guides/general/contributing/#discourse">Forum</a>.  Stöbern Sie in den <a href="/guides/general/frequently-asked-questions/">FAQ</a>. Fragen Sie einen <a href="/guides/general/contributing/#contacts">Entwickler</a>.</p>

<p><a href="/license">{{< awesome "fas fa-balance-scale" >}} MIT-Lizenz</a>. Rhino Entwickler-Tools sind gebührenfrei und enthalten Support. </p>
</div>


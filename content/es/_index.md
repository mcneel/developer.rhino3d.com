+++
aliases = ["/en/5/", "/en/6/", "/en/7/", "/en/wip/"]
description = "Recursos oficiales para desarrolladores de Rhino y Grasshopper.  Las herramientas para desarrolladores de Rhino están libres de derechos e incluyen soporte técnico."
title = "Documentación para desarrolladores de Rhino y Grasshopper"
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

{{< call-out note "¿Necesita ayuda para migrar C# a Rhino 8?" >}}
Consulte la [Guía de migración a .NET 7](/guides/rhinocommon/moving-to-dotnet-7/).
{{< /call-out >}}

{{< vimeo 188730450 >}}

<br>

<div class="table-responsive" align="center">
<table class="table" style="width:940px;">
  <thead>
    <tr style="border-bottom:1pt solid black;">
      <th style="text-align: left;">Info</th>
      <th style="text-align: left;">Qué</th>
      <th style="text-align: left;">Cómo</th>
      <th style="text-align: left;">Por qué</th>
    </tr>
  </thead>
  <tbody class="table-striped index_table">
  <tr>
    <td><a href="/guides/rhinocommon" title="RhinoCommon: The cross-platform toolkit for Rhino and Grasshopper"> RhinoCommon</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/vb-logo-small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Escribir plugins de Rhino y componentes de Grasshopper</td>
  </tr>
  <tr>
    <td><a href="/guides/rhinopython" title="Rhino.Python: Pythonic in three dimensions!"> Rhino.Python</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Programación multiplataforma</td>
  </tr>
  <tr>
    <td><a href="/guides/opennurbs" title="openNURBS is free and open source"> openNURBS</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Lectura y escritura de archivos 3dm</td>
  </tr>
  <tr>
    <td><a href="/guides/rhinoscript" title="RhinoScript is based on Microsoft's VBScript language"> RhinoScript</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/vbscript-logo-small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Scripting de Rhino para Windows</td>
  </tr>
  <tr>
    <td><a href="/guides/cpp" title="C/C++ SDK for Rhino for Windows"> C/C++</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Plugins de Rhino para Windows</td>
  </tr>
   <tr>
    <td><a href="/guides/grasshopper" title="Grasshopper Component Development"> Grasshopper</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="OS X" class="index_table_icon" title="Mac OS X"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/vb-logo-small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Componentes de Grasshopper</td>
  </tr>
  <!--
  <tr>
    <td><a href="/guides/#rdk" title="Renderer Development Kit"> RDK</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"><img src="/images/vbscript-logo-small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Desarrollo de plugins de renderizado en Windows.</td>
  </tr>
  -->
  <!-- RAP es en realidad una característica del SDK de C/C++ y del SDK de RhinoCommon.
  <tr>
    <td><a href="/guides/#rap" title="Rhino Application Platform"> RAP</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">"Skinning" de Rhino para Windows.</td>
  </tr>
  -->
  <!--
  <tr>
    <td><a href="/guides/#zoo" title="Zoo License Manager Plugins"> Zoo</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Plugins del administrador de licencias Zoo en Windows</td>
  </tr>
  -->
  <!--
  <tr>
    <td><a href="/guides/rhinomobile" title="Tools for using 3dm files in mobile applications"> RhinoMobile</a></td>
	<td><img src="/images/android-logo-small.png" alt="Android" class="index_table_icon" title="Android"><img src="/images/ios-logo-small.png" alt="iOS" class="index_table_icon" title="Apple iOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"></td>
    <td class="index_table_primary_use">Desarrollo de aplicaciones móviles 3D</td>
  </tr>
  -->
 </tbody>
 </table>
 </div>



<div align="center">


<p>¿Necesita más información?  Navegue por las <a href="/guides/">Guías</a>.  Haga preguntas en el <a href="/guides/general/contributing/#discourse">Foro</a>.  Consulte las <a href="/guides/general/frequently-asked-questions/">FAQ</a>. Pregunte a un <a href="/guides/general/contributing/#contacts">desarrollador</a>.</p>

<p><a href="/license">{{< awesome "fas fa-balance-scale" >}} MIT License</a>. Las herramientas para desarrolladores de Rhino son gratuitas e incluyen soporte técnico. </p>
</div>


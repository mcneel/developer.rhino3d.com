+++
aliases = ["/es/5/", "/es/6/", "/es/7/", "/es/wip/"]
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
<!--
<div align="center"><h1 id="getting-started-with-rhino-development">Empezar con el desarrollo de Rhino</h1></div>
-->
<!--
<div>
  <table style="width:100%; border: 1px; margin: 0 auto; padding:0; border-spacing: 0px; border-collapse: separate;">
    <tbody>
      <tr>
        <td style="padding: 20px; text-align: center;">
          <a href="/guides/grasshopper" title="Grasshopper Components">
            <img src="/images/ghcomponent-logo-intro.png" class="index_use_images">
          </a>
        </td>
        <td style="padding: 20px; text-align: center;">
          <a href="/guides/#rhinocommon" title="RhinoCommon: The cross-platform .NET SDK for Rhino and Grasshopper">
            <img src="/images/rhinocommon-logo-intro.png" class="index_use_images">
          </a>
        </td>
        <td style="padding: 20px; text-align: center;">
          <a href="/guides/#rhinopython" title="Rhino.Python: Pythonic in three dimensions!">
            <img src="/images/rhino-python-logo-intro.png" class="index_use_images">
          </a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
-->

{{< alt-version "https://developer.rhino3d.com/guides/rhinocommon/moving-to-dotnet-7/" "¿Necesita ayuda para migrar C# a Rhino 8? ¡Haa clic aquí!">}}

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


</div>

<h3>Licencia MIT</h3>
Las herramientas para desarrolladores de Rhino son gratuitas e incluyen soporte técnico.

Copyright (c) 1993-2024 Robert McNeel & Associates. Todos los derechos reservados.

Se concede por la presente, de forma gratuita, permiso a cualquier persona para obtener una copia
de los SDK y API de Rhino, incluidos openNURBS, rhino3dm, RhinoCommon, la API de Grasshopper y los archivos de documentación asociados (el "Software"), para tratar
el Software sin restricciones, incluyendo, entre otros, los derechos
de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de
así como el derecho a permitir que las personas a quienes
se proporcione el Software lo hagan bajo las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso deberán incluirse en todas 
las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍAS DE NINGÚN TIPO, EXPRESAS O
IMPLÍCITAS, INCLUIDAS, ENTRE OTRAS, LAS GARANTÍAS DE COMERCIABILIDAD,
IDONEIDAD PARA UN FIN DETERMINADO Y NO INFRACCIÓN. EN NINGÚN CASO LOS
AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U
OTRA RESPONSABILIDAD, YA SEA POR CONTRATO, AGRAVIO O CUALQUIER OTRA FIGURA LEGAL, DERIVADA DE,
RELACIONADA CON O CONECTADA AL SOFTWARE O AL USO O A OTRAS INTERACCIONES CON EL
SOFTWARE.
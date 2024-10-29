+++
aliases = ["/en/5/", "/en/6/", "/en/7/", "/en/wip/"]
description = "RhinoやGrasshopperの開発者向けの公式のリソースを掲載しています。Rhinoの開発ツールは、ロイヤリティフリーで、サポートを含みます。"
title = "RhinoとGrasshopperの開発時に参照できるドキュメンテーション"
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

{{< call-out note "C# をRhino 8に移行する際に支援が必要ですか?" >}}
[Moving to .NET 7ガイド](/guides/rhinocommon/moving-to-dotnet-7/) をご覧ください。
{{< /call-out >}}

{{< vimeo 188730450 >}}

<br>

<div class="table-responsive" align="center">
<table class="table" style="width:940px;">
  <thead>
    <tr style="border-bottom:1pt solid black;">
      <th style="text-align: left;">種類</th>
      <th style="text-align: left;">プラットフォーム</th>
      <th style="text-align: left;">方法</th>
      <th style="text-align: left;">目的</th>
    </tr>
  </thead>
  <tbody class="table-striped index_table">
  <tr>
    <td><a href="/guides/rhinocommon" title="RhinoCommon: RhinoとGrasshopperのクロスプラットフォーム ツールキット"> RhinoCommon</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/vb-logo-small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="IronPythonを介したPython"></td>
    <td class="index_table_primary_use">Rhinoのプラグイン & Grasshopperのコンポーネントを作成</td>
  </tr>
  <tr>
    <td><a href="/guides/rhinopython" title="Rhino.Python: 3DでPythonic!"> Rhino.Python</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="IronPythonを介したPython"></td>
    <td class="index_table_primary_use">クロスプラットフォームのスクリプト作成</td>
  </tr>
  <tr>
    <td><a href="/guides/opennurbs" title="openNURBS - 無償でオープンソース"> openNURBS</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">3dmファイルの読み書き</td>
  </tr>
  <tr>
    <td><a href="/guides/rhinoscript" title="RhinoScript - MicrosoftのVBScript言語がベース"> RhinoScript</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/vbscript-logo-small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Windows版Rhino用のスクリプト作成</td>
  </tr>
  <tr>
    <td><a href="/guides/cpp" title="Windows版RhinoのC/C++ SDK"> C/C++</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Windows版Rhino用のプラグイン</td>
  </tr>
   <tr>
    <td><a href="/guides/grasshopper" title="Grasshopperのコンポーネントの開発"> Grasshopper</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="OS X" class="index_table_icon" title="Mac OS X"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/vb-logo-small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="IronPythonを介したPython"></td>
    <td class="index_table_primary_use">Grasshopperのコンポーネント</td>
  </tr>
  <!--
  <tr>
    <td><a href="/guides/#rdk" title="レンダラの開発キット"> RDK</a></td>
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
  <!--
  <tr>
    <td><a href="/guides/rhinomobile" title="Tools for using 3dm files in mobile applications"> RhinoMobile</a></td>
	<td><img src="/images/android-logo-small.png" alt="Android" class="index_table_icon" title="Android"><img src="/images/ios-logo-small.png" alt="iOS" class="index_table_icon" title="Apple iOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"></td>
    <td class="index_table_primary_use">3D mobile application development</td>
  </tr>
  -->
 </tbody>
 </table>
 </div>



<div align="center">


<p>ご不明な点があれば、 <a href="/guides/">ガイド</a> をご覧ください。ご質問は、 <a href="/guides/general/contributing/#discourse">フォーラム</a> をご利用ください。 <a href="/guides/general/contributing/#contacts">開発者</a> に連絡を取っていただくこともできます。<a href="/guides/general/frequently-asked-questions/">FAQ</a> もご覧ください。</p>

<p><a href="/license">{{< awesome "fas fa-balance-scale" >}} MIT License</a>. Rhino developer tools are royalty free and include support. </p>
</div>


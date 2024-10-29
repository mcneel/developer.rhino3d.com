+++
aliases = ["/kr/5/", "/kr/6/", "/kr/7/", "/kr/wip/"]
description = "Rhino와 Grasshopper 개발자를 위한 공식 리소스입니다.   Rhino 개발자 도구는 로열티가 없으며, 지원이 포함되어 있습니다."
title = "Rhino와 Grasshopper 개발자를 위한 문서"
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

{{< call-out note "C#를 Rhino 8로 마이그레이션하는 데 도움이 필요하세요?" >}}
[Moving to .NET 7 가이드](/guides/rhinocommon/moving-to-dotnet-7/)를 참조하세요.
{{< /call-out >}}

{{< vimeo 188730450 >}}

<br>

<div class="table-responsive" align="center">
<table class="table" style="width:940px;">
  <thead>
    <tr style="border-bottom:1pt solid black;">
      <th style="text-align: left;">종류</th>
      <th style="text-align: left;">플랫폼</th>
      <th style="text-align: left;">방법</th>
      <th style="text-align: left;">용도</th>
    </tr>
  </thead>
  <tbody class="table-striped index_table">
  <tr>
    <td><a href="/guides/rhinocommon" title="RhinoCommon: The cross-platform toolkit for Rhino and Grasshopper"> RhinoCommon</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/vb-logo-small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Rhino 플러그인과 Grasshopper 컴포넌트 작성</td>
  </tr>
  <tr>
    <td><a href="/guides/rhinopython" title="Rhino.Python: Pythonic in three dimensions!"> Rhino.Python</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">크로스 플랫폼 스크립팅</td>
  </tr>
  <tr>
    <td><a href="/guides/opennurbs" title="openNURBS is free and open source"> openNURBS</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="macOS" class="index_table_icon" title="Apple macOS"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">3dm 파일 읽고 쓰기</td>
  </tr>
  <tr>
    <td><a href="/guides/rhinoscript" title="RhinoScript is based on Microsoft's VBScript language"> RhinoScript</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/vbscript-logo-small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Windows용 Rhino 스크립팅</td>
  </tr>
  <tr>
    <td><a href="/guides/cpp" title="C/C++ SDK for Rhino for Windows"> C/C++</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="/images/cpp-logo-small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Windows용 Rhino 플러그인</td>
  </tr>
   <tr>
    <td><a href="/guides/grasshopper" title="Grasshopper Component Development"> Grasshopper</a></td>
	<td><img src="/images/win-logo-small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="/images/mac-logo-small.png" alt="OS X" class="index_table_icon" title="Mac OS X"></td>
	<td><img src="/images/cs-logo-small.png" alt="C#" class="index_table_icon" title="C#"><img src="/images/vb-logo-small.png" alt="Visual Basic" class="index_table_icon" title="Visual Basic"><img src="/images/python-logo-small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Grasshopper 컴포넌트</td>
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


<p>더 자세한 사항은 <a href="/guides/">가이드</a>를 참조하시고, 질문이 있으시면 <a href="/guides/general/contributing/#discourse">사용자 게시판</a>을 이용하시기 바랍니다. <a href="/guides/general/frequently-asked-questions/">질문과 대답</a> 페이지도 둘러보세요. <a href="/guides/general/contributing/#contacts">개발자</a>에게 직접 문의하실 수 있습니다.</p>

<p><a href="/license">{{< awesome "fas fa-balance-scale" >}} MIT License</a>. Rhino 개발자 도구는 로열티가 없으며, 지원이 포함되어 있습니다. </p>
</div>


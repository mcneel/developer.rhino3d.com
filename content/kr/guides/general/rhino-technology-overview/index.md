+++
aliases = ["/kr/5/guides/general/rhino-technology-overview/", "/kr/6/guides/general/rhino-technology-overview/", "/kr/7/guides/general/rhino-technology-overview/", "/kr/wip/guides/general/rhino-technology-overview/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "Rhino 테크놀로지 아키텍처 소개."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Rhino 테크놀로지 개요"
type = "guides"
weight = 0
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++


## 개요

Rhinoceros는 많은 언어로 쓰여져 서로 계층을 이루며 쌓여 있는 구성입니다.  가장 기본적인 토대는 바닥에 위치하지만, 최상단 계층을 결코 표면적인 것으로 생각하면 안 됩니다.

![The Rhino Stack](/images/rhino-technology-overview-01.png)

이러한 각각의 계층을 바닥부터 순서대로 설명해보고자 합니다.

## 파운데이션

### C++ Rhino Core

Rhino의 C++ Core는 가장 오래되고 광범위한 코드 세트입니다.  Microsoft의 MFC는 SDK를 비롯하여 여러 곳에 사용되고 있습니다.  여기가 런타임 문서가 관리되고, 모든 OpenGL 뷰포트 도면 코드가 존재하고, 우리 수학자들이 작성한 계산 기하학 코드가 위치하는 곳입니다.  많은 Rhino 명령이 여기에 있습니다.

다양한 사용자 인터페이스 - 명령행, 애플리케이션 메인프레임, 상태 표시줄, Rhino Core의 많은 명령의 대화상자.

### openNURBS

openNURBS는 Rhino *3dm* 파일을 읽고 쓸 수 있는 무료 C++ 소스 코드이며, Rhino 1버전 파일부터 사용할 수 있습니다.  openNURBS는 저희의 제일 첫 번째 오픈 소스 프로젝트였습니다.

이 코드는 Windows, macOS, Linux, iOS, Android에서 컴파일됩니다.  ArchiCAD, SolidWorks, Inventor, SketchUp, 그리고 *3dm* 파일을 직접 읽거나 쓰는 기타 제품들과 같은 다양한 타사 애플리케이션에서 사용됩니다.

Rhino는 *3dm* 파일을 읽기/쓰기에 기본적으로 openNURBS를 사용합니다.  이 툴킷은 Rhino보다 먼저 릴리스되므로, 경쟁사를 포함한 모든 제품이 최신 *3dm* 파일과 호환될 수 있습니다.  Rhino가 작성하는 *3dm* 파일과 openNURBS를 사용하여 다른 애플리케이션이 읽고 쓰는 *3dm* 파일 사이에는 차이가 없습니다.

openNURBS에 대한 자세한 정보는 [openNURBS 가이드](/guides/opennurbs/)를 참조하세요.

### C++ SDK

모든 것의 최상단에는 C++ SDK 가 있으며, 이는 Windows에서만 사용할 수 있습니다.

C++ SDK에 대해 컴파일하려면 Microsoft Visual Studio의 특정한 버전과 Microsoft C-Runtime이 필요합니다.  Rhino의 모든 주요 버전용으로 다시 컴파일해야 합니다.

Rhino가 실행할 수 있는 거의 대부분의 기능은 C++ SDK를 통해 공개됩니다. 일부 명령과 기능은 아직 공개되지 않았으나, 이 SDK는 매우 광범위하고 다채롭습니다.

안타깝게도 이 SDK는 Rhino Core와 밀접하게 결합되어 있어, Rhino가 릴리스될 때마다 플러그인 개발자는 해당 플러그인을 다시 컴파일해야 합니다.

C++ SDK에 대한 자세한 정보는 [C/C++ 가이드](/guides/cpp/)를 참조하세요.

## C++ 스택

위의 스택 다이어그램에서 오른쪽이 Rhino의 C++ 부분입니다.  C++ 스택을 사용하면, 당사와 타사 플러그인 개발자가 Rhino 개발에 사용하는 것과 동일한 C++ SDK를 사용하여 Rhino 플러그인을 작성할 수 있습니다.  C++를 사용하여 Grasshopper 컴포넌트를 작성할 수 없음을 주의하시기 바랍니다.

### C++ 플러그인

C++ SDK 위에는 C++ 플러그인이 있습니다.  명령, 파일 가져오기/내보내기, 렌더러를 비롯하여 Rhino에서 기본 제공하는 많은 기능은 실제로는 C++ 플러그인입니다.  [Asuni의 VisualARQ,](http://www.visualarq.com/) [MecSoft의 RhinoCAM](https://mecsoft.com/rhinocam-software/), [Chaos Software의 V-Ray](https://www.chaosgroup.com/vray/rhino) 등 수십 개의 타사 C++ 플러그인도 있습니다.

C++ SDK에 대한 자세한 정보는 [C/C++ 가이드](/guides/cpp/)를 참조하세요.

### RhinoScript

Rhino와 함께 기본 제공되는 C++ 플러그인 중 하나는 [RhinoScript](/guides/rhinoscript/what-are-vbscript-rhinoscript/) 입니다.  RhinoScript는 널리 사용되고 인기 있는 스크립팅 언어인 VBScript를 통해 Rhino SDK의 유용한 하위 세트를 공개합니다.  RhinoScript를 사용하면 Rhino뿐만 아니라 Windows의 다른 COM 개체에도 액세스할 수 있습니다.

더 자세한 정보를 보시려면 [RhinoScript 가이드](/guides/rhinoscript/), 특히 [What are VBScript and RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript/) 가이드를 참조하시기 바랍니다.

## .NET 스택

.NET SDK는 3개의 계층으로 나타납니다:

- C API
- .NET Framework
- RhinoCommon
- Eto

### C API

직접적인 C API가 C++ SDK를 래핑하여 C++ SDK로 플랫폼 호출(P/Invoke)이 가능하며, 기본적인 C++ 코드와 관리되는 .NET 계층 사이에 브리지를 형성합니다.

### .NET Framework

Microsoft에서 [.NET Framework](https://www.microsoft.com/net/framework)를 개발합니다.  .NET을 사용하여 C#, F#, VB.NET 그리고 Microsoft IL로 컴파일되는 다른 언어로 플러그인을 작성할 수 있습니다.

Microsoft .NET Framework는 Windows와 함께 기본 제공됩니다.

Mac용 Rhino 제품에서는 .NET 런타임의 부분적 크로스 플랫폼 구현인 [Mono Runtime](https://www.mono-project.com)이 포함되어 있습니다.

.NET 관련 정보와 Rhino 개발과 .NET의 관계에 대한 자세한 정보를 보시려면 [What are Mono & Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/) 를 참조하시기 바랍니다.

### RhinoCommon

RhinoCommon은 당사의 Rhino용 .NET SDK이며, Windows와 macOS(Mono를 통해)에서 모두 *공통적인(common)* .NET Framework의 부분을 기반으로 빌드되었습니다.  개발자는 RhinoCommon을 사용하여 Windows용 Rhino와 Mac용 Rhino에서 모두 .NET 코드를 실행할 수 있습니다.

RhinoCommon에 대한 자세한 정보는 [RhinoCommon 가이드](/guides/rhinocommon/), 특히 [What is RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon) 가이드를 참조하시기 바랍니다.

### Eto

RhinoCommon을 사용하여 사용자 인터페이스를 제외하고 Windows와 Mac에서 작동하는 .NET 플러그인을 작성할 수 있습니다.  Mono 팀에서 WinForms나 WPF를 클론하지 않았기 때문에, 두 기술 모두 Mac에서 작동하지 않습니다.  이 문제를 대처하기 위해, 이제 Rhino에서 Eto.Forms를 기본 제공합니다.  Eto를 사용하면 C#, XAML 또는 JSON으로 사용자 인터페이스를 한 번만 작성하고 Windows와 macOS에서 이를 사용할 수 있습니다.  실제로, Eto로 작성된 UI는 iOS, Android, Linux 에서도 실행될 수 있습니다.

Eto에 대한 더 자세한 정보는 [Eto.Forms on GitHub](https://github.com/picoe/Eto) 페이지를 참조하시기 바랍니다.

### .NET 플러그인

당사 플러그인과 타사에서 개발한 플러그인을 비롯한 많은 플러그인이 RhinoCommon 상에 빌드되었습니다.  예를 들어, [Grasshopper](http://www.grasshopper3d.com/)는 RhinoCommon 플러그인입니다.  Rhino의 일부 명령, 렌더러 및 파일 가져오기/내보내기 플러그인은 실제로 RhinoCommon 플러그인으로 작성되었습니다.  시간이 지나면서, 플랫폼 간에 더 많은 코드를 공유할 수 있도록 점점 더 편리한 기능을 RhinoCommon/.NET 플러그인으로 옮기고 있습니다.  [RhinoGold](http://www.tdmsolutions.com/)와 [GEMVision의 Matrix](http://www.stuller.com/matrix), [Orca3D](http://orca3d.com/)를 비롯한 많은 성공적인 타사 플러그인 개발에 RhinoCommon과 .NET이 사용되었습니다.

RhinoCommon에 대한 자세한 정보를 보시려면 [RhinoCommon 가이드](/guides/rhinocommon/)를 참조하세요.

### Grasshopper 컴포넌트

이제 Rhino에서 알고리즘 및 파라메트릭 디자인을 위한 시각적 프로그래밍 언어인 Grasshopper가 기본 제공됩니다.  Grasshopper는 그 자체로 독립적인 개발 플랫폼이며, [물리 시뮬레이션](http://www.food4rhino.com/project/kangaroo), [사용자 인터페이스 생성](http://www.food4rhino.com/project/human-ui), [산업 로봇 프로그래밍 및 제어](http://www.food4rhino.com/project/hal)를 비롯한 수많은 작업을 수행할 수 있는 [수백 개의 타사 Grasshopper 컴포넌트](http://www.food4rhino.com/grasshopper-addons)가 있습니다.

Grasshopper에 대한 자세한 정보, 특히 Grasshopper 컴포넌트 개발에 대한 정보를 보시려면 [Grasshopper 가이드](/guides/grasshopper/)를 참조하시기 바랍니다.

### Python 스크립트

Rhino에 기본 탑재된 .NET 플러그인 중 하나는 RhinoPython 입니다.  RhinoPython은 [Python](https://www.python.org/) 런타임의 .NET 구현인 [IronPython](http://ironpython.net/)을 사용하여 작성되었으며, 전체 RhinoCommon SDK를 Python 스크립팅 언어에 노출합니다.  이것은 RhinoCommon에 기능이 추가되면 그 때마다 RhinoPython에 자동으로 기능이 나타남을 뜻합니다.

RhinoPython에 대한 자세한 정보는 [RhinoPython 가이드](/guides/rhinopython/)를 참조하시기 바랍니다.

## 관련 주제

- [C/C++ 가이드](/guides/cpp/)
- [openNURBS 가이드](/guides/opennurbs/)
- [RhinoScript 가이드](/guides/rhinoscript/)
- [Microsoft .NET Framework (microsoft.com)](https://www.microsoft.com/net/framework)
- [RhinoCommon이란 무엇인가?](/guides/rhinocommon/what-is-rhinocommon)
- [RhinoCommon 가이드](/guides/rhinocommon/)
- [Mono와 Xamarin이란 무엇인가?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Mono 프로젝트](https://www.mono-project.com)
- [GitHub의 Eto.Forms](https://github.com/picoe/Eto)
- [Grasshopper 가이드](/guides/grasshopper/)
- [RhinoPython 가이드](/guides/rhinopython/)

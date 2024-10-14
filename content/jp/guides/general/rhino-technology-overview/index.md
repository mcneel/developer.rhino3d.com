+++
aliases = ["/5/guides/general/rhino-technology-overview/", "/6/guides/general/rhino-technology-overview/", "/7/guides/general/rhino-technology-overview/", "/wip/guides/general/rhino-technology-overview/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "Rhinoのテクノロジ・アーキテクチャの概要"
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Rhinoの技術的概要"
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


## 概要

Rhinocerosは、さまざまな言語で記述された多数の階層で構成されており、すべてが互いに積み重ねられています。最も基礎となるものは最下層にありますが、最上層は決して表面的なものと見なすべきではありません。

![The Rhino Stack](/images/rhino-technology-overview-01.png)

一番下の層から順に、各層について説明しましょう。

## 基礎

### C++ Rhino Core (C++ Rhinoコア)

RhinoのC++コアは、最も古く、最も幅広いコードセットです。私達は、SDKを含むいくつかの場所でMicrosoftのMFCを使用しています。ここはランタイムドキュメントが管理されるところです。すべてのOpenGLビューポートの描画コードが存在し、当社の数学者によって記述された計算幾何学のコードが存在します。Rhinoのコマンドの多くはここにあります。

Rhinoコアには、コマンドライン、アプリケーションのメインフレーム、ステータスバー、そして多くのコマンドのダイアログボックスを含む多数のユーザーインターフェイスが存在します。

### openNURBS

openNURBSは、バージョン1まで遡ってRhinoの*3dm*ファイルを読み書きできるようにする無償のC++ソースコードです。openNURBSは、私達の最初のオープンソースのプロジェクトでした。

このコードは、Windows、macOS、Linux、iOS、Androidでコンパイルできます。ArchiCAD、SolidWorks、Inventor、SketchUpなどの様々なサードパーティアプリケーションや、その他多くの製品で*3dm*を直接読み書きするのに使用されています。

openNURBSは、Rhinoが*3dm*ファイルの読み取り/書き込みにネイティブで使用するものです。このツールキットはRhinoより前にリリースされたため、私達の競合会社のものを含むどのような製品でも最新の*3dm*ファイルと互換性があります。Rhinoが書き込む*3dm*ファイルと、openNURBSを使用して*3dm*の読み書きを行う他のアプリケーションの3dmファイルの間に違いはありません。

openNURBSの詳細については [openNURBSのガイド](/guides/opennurbs/) を参照してください。

### C++ SDK

基礎の階層の上にあるのは、Windowsのみで使用可能な当社のC++ SDKです。

C++ SDKに対してコンパイルするには、特定のバージョンのMicrosoft Visual StudioとMicrosoft C-Runtimeが必要です。Rhinoのメジャーバージョン毎に再コンパイルが必要です。

Rhinoで実行できるほぼすべての機能は、C++ SDKを通じて公開しています。コマンドと機能によってはまだ公開していないものもあります。しかし、このSDKは非常に広範で豊かです。

残念ながら、Rhino Coreと非常に密接に結合されているため、プラグインの開発者はRhinoのリリース毎にプラグインを再コンパイルする必要があります。

C++ SDKの詳細については [C/C++のガイド](/guides/cpp/) を参照してください。

## C++のスタック

上の階層の図の右側の列は、RhinoのC++の部分です。C++のスタックで私達やサードパーティのプラグイン開発者は、私達がRhino自体の開発に使用しているのと同じC++ SDKを使用してRhinoのプラグインを作成できます。C++を使用してGrasshopperのコンポーネントを作成することはできないことに注意してください。

### C++ Plugins (C++のプラグイン)

C++ SDKの上にはC++のプラグインが位置します。一部のコマンド、ファイルI/O、レンダラなど、Rhinoに搭載されている多くの機能は、実際はC++のプラグインです。また、 [AsuniのVisualARQ](http://www.visualarq.com/) 、 [MecSoftのRhinoCAM](https://mecsoft.com/rhinocam-software/) 、 [Chaos SoftwareのV-Ray](https://www.chaosgroup.com/vray/rhino) など、サードパーティのC++プラグインも多数あります。

C++ SDKの詳細については [C/C++のガイド](/guides/cpp/) を参照してください。

### RhinoScript

Rhinoに含まれているC++プラグインの1つに [RhinoScript](/guides/rhinoscript/what-are-vbscript-rhinoscript/) があります。RhinoScriptは、広く使用されている人気のスクリプト言語であるVBScriptを介して、RhinoのSDKの便利なサブセットを公開しています。RhinoScriptを使用すると、Rhinoだけでなく、Windows上の他のCOMオブジェクトにもアクセスできます。

詳細については、 [RhinoScriptのガイド](/guides/rhinoscript/) を、特に [What are VBScript and RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript/) のガイドを参照してください。

## .NETのスタック

ここでは、.NET SDKは下記のものを3つの階層で表します。

- C API
- .NET Framework
- RhinoCommon
- Eto

### C API

C APIがC++ SDKをラップしているので、プラットフォーム呼び出し (P/Invoke) によりC++ SDKにアクセスすることができ、ネイティブのC++コードと管理された.NET層の間に橋渡しが形成されます。　

### .NET Framework

[.NET Framework](https://www.microsoft.com/net/framework) は、Microsoftが開発しています。.NETを使用すると、C#、F#、VB.NET、そしてMicrosoftのILにコンパイルされるその他の言語でプラグインを記述できます。

Microsoft .NET FrameworkはWindowsに含まれています。

Mac版Rhinoには、.NETランタイムの部分的なクロスプラットフォーム実装である [Monoランタイム](https://www.mono-project.com) を組み込んでいます。

.NETとそれがRhinoの開発にどのように関連しているかの詳細については [What are Mono & Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/) を参照してください。

### RhinoCommon

RhinoCommonは、WindowsとmacOS(Monoを介して)の両方で *共通* する、.NET Framework部分に基づいて構築された、私達のRhino用の.NET SDKです。RhinoCommonを使用すると、開発者はWindows版RhinoとMac版Rhinoの両方で.NETコードを実行できます。

RhinoCommonの詳細については、 [RhinoCommonのガイド](/guides/rhinocommon/) を、特に [What is RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon) のガイドを参照してください。

### Eto

RhinoCommonを使用すると、WindowsとMacで動作する.NETプラグインを作成できます。ただし、ユーザーインターフェイスは除きます。MonoのチームはWinFormsやWPFをクローンしなかったため、これらのテクノロジはどちらもMacでは動作しません。この問題に対処するため、Rhinoには現在Eto.Formsが含まれています。Etoを使用すると、C#、XAML、またはJSONでユーザーインターフェイスを一度記述すれば、WindowsとmacOSで使用できます。実際には、Etoで記述したUIは、iOS、Android、Linuxでも実行できます。

Etoについての詳細は、 [GitHub上のEto.Forms](https://github.com/picoe/Eto) を参照してください。

### .NETのプラグイン

RhinoCommon上には、多数のプラグインが構築されています。これには内部で開発されたプラグイン、そして、サードパーティで開発されたプラグインの両方が含まれます。例えば [Grasshopper](http://www.grasshopper3d.com/) はRhinoCommonのプラグインです。Rhinoの一部のコマンド、レンダラ、及びファイルIOプラグインは、実際にはRhinoCommonのプラグインとして作成されています。そのうちに、プラットフォーム間でより多くのコードを共有できるように、より便利な機能性をRhinoCommon/.NETプラグインに移行する予定です。 [RhinoGold](http://www.tdmsolutions.com/) 、 [GEMVisionのMatrix](http://www.stuller.com/matrix) 、そして [Orca3D](http://orca3d.com/) のような多くのメジャーなサードパーティのプラグインもRhinoCommon/.NETを使用して書かれています。

RhinoCommonについての詳細は、 [RhinoCommonのガイド](/guides/rhinocommon/) を参照してください。

### Grasshopperのコンポーネント

Rhinoには現在、当社のアルゴリズム/パラメトリックデザイン用のビジュアルプログラミング言語であるGrasshopperが搭載されています。Grasshopperはそれ自体が、 [サードパーティによって作成された数多くのGrasshopperのコンポーネント](http://www.food4rhino.com/grasshopper-addons) を含んだ開発プラットフォームです。 [物理のシミュレーション](http://www.food4rhino.com/project/kangaroo) 、 [カスタム・ユーザーインターフェイスの作成](http://www.food4rhino.com/project/human-ui) 、 [産業用ロボットのプログラミングと制御](http://www.food4rhino.com/project/hal) など様々なことを行えるようになっています。

Grasshopperについての詳細、特にGrasshopperのコンポーネントの開発についての詳細は、 [Grasshopperのガイド](/guides/grasshopper/) を参照してください。

### Pythonスクリプト

Rhinoに含まれている.NETプラグインの1つにRhinoPythonがあります。 [Python](https://www.python.org/) ランタイムの.NET実装である [IronPython](http://ironpython.net/) を使用して書かれたRhinoPythonは、RhinoCommon SDK全体をPythonスクリプト言語に公開します。つまり、RhinoCommonに機能を追加すると、その機能がRhinoPythonに自動的に表示されます。

RhinoPythonの詳細については、 [RhinoPythonのガイド](/guides/rhinopython/) を参照してください。

## 関連トピック

- [C/C++のガイド](/guides/cpp/)
- [openNURBSのガイド](/guides/opennurbs/)
- [RhinoScriptのガイド](/guides/rhinoscript/)
- [Microsoft .NET Framework (microsoft.com)](https://www.microsoft.com/net/framework)
- [What is RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon)
- [RhinoCommonのガイド](/guides/rhinocommon/)
- [What are Mono & Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Mono Project](https://www.mono-project.com)
- [GitHub上のEto.Forms](https://github.com/picoe/Eto)
- [Grasshopperのガイド](/guides/grasshopper/)
- [RhinoPythonのガイド](/guides/rhinopython/)

+++
aliases = ["/en/5/guides/", "/en/6/guides/", "/en/7/guides/", "/en/wip/guides/"]
description = "RhinoまたはGrasshopperのための開発に利用できるすべてのガイドです。"
title = "ガイド"
type = "guides"
weight = 2

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = []
since = 0

[page_options]
byline = false
toc = true
toc_type = "single"
+++

## [一般](/guides/general)

*SDK、そして複数のプラットフォームに共通のガイドです。*

### 概要

- [公開のソフトウェア開発](/guides/general/developing-software-in-public)
- [Rhinoの技術的概要](/guides/general/rhino-technology-overview)
- [Frequently Asked Questions (FAQ)](/guides/general/frequently-asked-questions)

### はじめに

- [Developer Prerequisites](/guides/general/rhino-developer-prerequisites)
- [Contributing](/guides/general/contributing)

### 基礎

- [What is a Rhino Plugin?](/guides/general/what-is-a-rhino-plugin)
- [Rhino Package Manager](/guides/yak/)
- [Rhino UI System](/guides/general/rhino-ui-system/)
- [Simple Command Macros](/guides/general/creating-command-macros/)

### [Essential Mathematics](/guides/general/essential-mathematics)

- [Introduction](/guides/general/essential-mathematics)  
- [Vector Mathematics](/guides/general/essential-mathematics/vector-mathematics)  
- [Matrices and Transformations](/guides/general/essential-mathematics/matrices-transformations)  
- [Parametric Curves and Surfaces](/guides/general/essential-mathematics/parametric-curves-surfaces)  
- [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6/essentialmathematics/) [Download Essential Mathematics for Computational Design as a single PDF ](https://www.rhino3d.com/download/rhino/6/essentialmathematics/)

### このサイト

- [How This Site Works](/guides/general/how-this-site-works)
- [Getting Started with Developer Docs](https://github.com/mcneel/developer-rhino3d-com/blob/main/README.md)
- [Developer Docs Style Guide](/guides/general/developer-docs-style-guide)

## [スクリプト作成](/guides/scripting)

*Rhino 8以降のスクリプト作成機能の使用に関するガイド。すべてのプログラミング言語に適用されます。*

### はじめに

#### ScriptEditorコマンド
  - [Opening Script Editor](/guides/scripting/scripting-command/#opening-script-editor)
  - [First Script](/guides/scripting/scripting-command/#first-script)
  - [Edit Script](/guides/scripting/scripting-command/#edit-script)
  - [Running Scripts](/guides/scripting/scripting-command/#running-scripts)
  - [Debugging Scripts](/guides/scripting/scripting-command/#debugging-scripts)
  - [Using Packages](/guides/scripting/scripting-command/#using-packages)
  - [Editor Features](/guides/scripting/scripting-command/#editor-features)

#### Scriptコンポーネント
  - [Create Script Component](/guides/scripting/scripting-component/#script-component)
  - [First Script](/guides/scripting/scripting-component/#first-script)
  - [Script Inputs and Outputs](/guides/scripting/scripting-component/#script-inputs-and-outputs)
  - [Edit Script](/guides/scripting/scripting-component/#edit-script)
  - [Run Scripts](/guides/scripting/scripting-component/#debugging-scripts)
  - [Debugging Scripts](/guides/scripting/scripting-component/#debugging-scripts)
  - [Using Packages](/guides/scripting/scripting-component/#using-packages)
  - [Editor Features](/guides/scripting/scripting-component/#editor-features)

### Pythonでのスクリプト作成
- <!-- [Python Scripting](/guides/scripting/scripting-python) --> Scripting: Python {{% comingsoon-label %}}
- {{< dev-topic "Grasshopper Scripting: Python" "/guides/scripting/scripting-gh-python" >}}

### C#でのスクリプト作成
- <!-- [C# Scripting](/guides/scripting/scripting-csharp) --> Scripting: C# {{% comingsoon-label %}}
- {{< dev-topic "Grasshopper Scripting: C#" "/guides/scripting/scripting-gh-csharp" >}}

### エディタの機能
- {{< dev-topic "Editing Features" "/guides/scripting/editor-editing" >}}
- <!-- [Explorer](/guides/scripting/editor-explorer) --> Explorer {{% comingsoon-label %}}
- <!-- [Search & Replace](/guides/scripting/editor-search) --> Search & Replace {{% comingsoon-label %}}
- {{< dev-topic "Terminal" "/guides/scripting/editor-terminal" >}}
- <!-- [Problems Tray](/guides/scripting/editor-problems) --> Problems Tray {{% comingsoon-label %}}
- <!-- [Debugging Your Scripts](/guides/scripting/editor-debug) --> Debugger {{% comingsoon-label %}}
- <!-- [Templates](/guides/scripting/editor-templates) --> Templates {{% comingsoon-label %}}
- <!-- [Examples](/guides/scripting/editor-examples) --> Examples {{% comingsoon-label %}}
- <!-- [Help](/guides/scripting/editor-help) --> Help {{% comingsoon-label %}}
- {{< dev-topic "Options" "/guides/scripting/editor-configs" >}}
- {{< dev-topic "Logs" "/guides/scripting/editor-logs" >}}

### スクリプトプラグインの公開

- {{< dev-topic "Creating Rhino Projects" "/guides/scripting/projects-create" >}}
- {{< dev-topic "Creating Rhino and Grasshopper Plugins" "/guides/scripting/projects-publish" >}}

### 上級

- {{< dev-topic "ScriptEditor Macros" "/guides/scripting/advanced-scripteditor-macros" >}}
- {{< dev-topic "Language Initialization" "/guides/scripting/advanced-langinit" >}}
- <!-- [CPython Runtime and Language Server](/guides/scripting/advanced-pyruntime) --> CPython Runtime and Language Server {{% comingsoon-label %}}
- {{< dev-topic "Python Path Files" "/guides/scripting/advanced-pthfiles" >}}
- {{< dev-topic "Python Package Environments" "/guides/scripting/advanced-pyvenvs" >}}
- <!-- [Language Libraries](/guides/scripting/advanced-libraries) --> Language Libraries {{% comingsoon-label %}}
- {{< dev-topic "Asynchronous Execution" "/guides/scripting/advanced-async" >}}
- <!-- [VisualStudioCode Extension](/guides/scripting/advanced-vscode) --> VisualStudioCode Extension {{% comingsoon-label %}}
- {{< dev-topic "RhinoCode Command Line Interface" "/guides/scripting/advanced-cli" >}}
<!-- [RhinoCode API](/guides/scripting/advanced-core-api) -->
<!-- [RhinoCodeEditor API](/guides/scripting/advanced-editor-api) -->

## [RhinoCommon](/guides/rhinocommon)

*Rhino用のクロスプラットフォーム.NETプラグインのSDKです。*

### 概要

- [What is RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon/)
- [What's New?](/guides/rhinocommon/whats-new/)

### はじめに

- Installing Tools ([Windows](/guides/rhinocommon/installing-tools-windows/), [Mac](/guides/rhinocommon/installing-tools-mac/))
- Your First Plugin ([Windows](/guides/rhinocommon/your-first-plugin-windows/), [Mac](/guides/rhinocommon/your-first-plugin-mac/)
- Plugin Installers ([Windows](/guides/rhinocommon/plugin-installers-windows/), [Mac](/guides/rhinocommon/plugin-installers-mac/))
- [Distributing a Rhino Plug-In with the Package Manager](/guides/yak/creating-a-rhino-plugin-package/)

### 基礎

{{< dev-topic-list "guides" "RhinoCommon" "Fundamentals" "weight" >}}

### RhinoCommonのジオメトリ

- [Overview](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#31-overview)  
- [Geometry structures](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#32-geometry-structures)  
    - [The Point3d structure](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#321-the-point3d-structure)  
    - [Points and vectors](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#322-points--vectors)  
    - [Lightweight curves](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#323-lightweight-curves)  
    - [Lightweight surfaces](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#324-lightweight-surfaces)  
    - [Lightweight surfaces](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#325-other-geometry-structures)  
- [Geometry classes](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#33-geometry-classes)  
    -  [Curves](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#331-curves)  
    - [Surfaces](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#332-surfaces)  
    - [Boundary representation (Brep)](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#334-boundary-representation-brep)  
    - [Other geometry classes](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#335-other-geometry-classes)  
- [Geometry transformations](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#34-geometry-transformations)  

### レンダリング

{{< dev-topic-list "guides" "RhinoCommon" "Rendering" "weight" >}}

### 上級

{{< dev-topic-list "guides" "RhinoCommon" "Advanced" "weight" >}}

### Zoo

{{< dev-topic-list "guides" "RhinoCommon" "Zoo" "weight" >}}

### Cloud Zoo

{{< dev-topic-list "guides" "RhinoCommon" "CloudZoo" "weight" >}}

## [Rhino.Python](/guides/rhinopython)


*Rhinoに機能を素早く追加したり、反復的なタスクを自動化したりします。*

### 概要

{{< dev-topic-list "guides" "RhinoPython" "Overview" "weight" "8" >}}

### はじめに

- Your First Python Script in Rhino ([Windows](/guides/rhinopython/your-first-python-script-in-rhino-windows), [Mac](/guides/rhinopython/your-first-python-script-in-rhino-mac), [Grasshopper](/guides/rhinopython/your-first-python-script-in-grasshopper))
- [Where to get help...](/guides/rhinopython/python-where-to-find-help)
- [Troubleshooting Installation](/guides/rhinopython/python-troubleshooting-install)

### Windows用Pythonエディタ

{{< dev-topic-list "guides" "RhinoPython" "Python Windows" "weight" "8" >}}

### GrasshopperでのPython

{{< dev-topic-list "guides" "RhinoPython" "GhPython" "weight" "8" >}}

### 基礎

{{< dev-topic-list "guides" "RhinoPython" "Fundamentals" "weight" "8" >}}

### RhinoでのPython

{{< dev-topic-list "guides" "RhinoPython" "Python in Rhino" "weight" "8" >}}

### [Rhino.Python 101](/guides/rhinopython/primer-101)

&nbsp;&nbsp; [Introduction](/guides/rhinopython/primer-101)  
&nbsp;&nbsp; [Where to find help](/guides/rhinopython/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [What's it all about?](/guides/rhinopython/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [Python Essentials](/guides/rhinopython/primer-101/2-python-essentials/)  
&nbsp;&nbsp; 3. [Script Anatomy](/guides/rhinopython/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operators and Functions](/guides/rhinopython/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Conditional Execution](/guides/rhinopython/primer-101/5-conditional-execution/)  
&nbsp;&nbsp; 6. [Tuples, Lists, and Dictionaries](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/)  
&nbsp;&nbsp; 7. [Classes](/guides/rhinopython/primer-101/7-classes/)  
&nbsp;&nbsp; 8. [Geometry](/guides/rhinopython/primer-101/8-geometry/)  

&nbsp;&nbsp; [{{< awesome "fas fa-download">}} ](https://download.rhino3d.com/IronPython/5.0/RhinoPython101/) [Download the Rhino.Python 101 Primer as a single PDF ](https://download.rhino3d.com/IronPython/5.0/RhinoPython101/)  


### 中級

{{< dev-topic-list "guides" "RhinoPython" "Intermediate" "weight" "8" >}}

### Etoでのカスタムダイアログ

{{< dev-topic-list "guides" "RhinoPython" "Eto" "weight" "8" >}}


### その他のリソース

- [Rhino Scripting Forum (Discourse)](https://discourse.mcneel.com/c/scripting)  
- [Rhino.Python Samples](/samples/#rhinopython)  
- [Rhino.Python Developer Samples GitHub](https://github.com/mcneel/rhino-developer-samples/tree/master/rhinopython)  
- [Designalyze Python Tutorials](https://designalyze.com/)
- [Plethora Project](https://www.plethora-project.com/education/2017/5/31/rhino-python-programming)
- [Steve Baer's Blog](https://stevebaer.wordpress.com/category/python/)
- [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide/Programmers)
- [Tutorials Point Python Series](https://www.tutorialspoint.com/python/index.htm)
- [Rhino.Python Dash Docset](https://discourse.mcneel.com/t/rhino-python-dash-docset/6399)
- [Nature of Code Video Tutorials](https://www.youtube.com/watch?v=Kyi_K85Gsm4&list=PL5Up_u-XkWgP7nB7XIevMTyBCZ7pvLBGP)

## [openNURBS](/guides/opennurbs)

*ご自身のアプリケーションでRhinoの3dmファイルを読み書きできます。*

### 概要

{{< dev-topic-list "guides" "openNURBS" "Overview" "weight" >}}

### はじめに

{{< dev-topic-list "guides" "openNURBS" "Getting Started" "weight" >}}

### 基礎

{{< dev-topic-list "guides" "openNURBS" "Fundamentals" "weight" >}}

### 上級

{{< dev-topic-list "guides" "openNURBS" "Advanced" "weight" >}}

## [C/C++](/guides/cpp)

*Windows版Rhinoのプラグイン用のネイティブSDKです。*

### 概要

{{< dev-topic-list "guides" "C/C++" "Overview" "weight" >}}

### はじめに

{{< dev-topic-list "guides" "C/C++" "Getting Started" "weight" >}}

### 基礎

{{< dev-topic-list "guides" "C/C++" "Fundamentals" "weight" >}}

### 上級

{{< dev-topic-list "guides" "C/C++" "Advanced" "weight" >}}

### レンダリング (RDK)

{{< dev-topic-list "guides" "C/C++" "RDK" "weight" >}}

### Zoo

{{< dev-topic-list "guides" "C/C++" "Zoo" "weight" >}}

### トラブルシューティング

{{< dev-topic-list "guides" "C/C++" "Troubleshooting" "weight" >}}

## [Grasshopper](/guides/grasshopper)


*カスタムのGrasshopperコンポーネントやプラグインを作成します。*

### [Essential Algorithms and Data Structures for Grasshopper](/guides/grasshopper/gh-algorithms-and-data-structures/)

- [Introduction](/guides/grasshopper/gh-algorithms-and-data-structures/)
- [Algorithms and Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/)
  - [1.1 Algorithmic design](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#11-algorithmic-design)
  - [1.2 Algorithms parts](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#12-algorithms-parts)
  - [1.3 Designing algorithms: the 4-step process](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#13-designing-algorithms-the-4-step-process)
  - [1.4 Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#14-data)
  - [1.5 Data sources](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#15-data-sources)
  - [1.6 Data types](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#16-data-types)
  - [1.7 Processing Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#17-processing-data)
  - [1.8 Pitfalls of algorithmic design](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#18-pitfalls-of-algorithmic-design)
  - [1.9 Tutorials: algorithms and data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#19-tutorials-algorithms-and-data)
- [Introduction to Data Structures](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/)
  - [2.1 Overview](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#21-overview)
  - [2.2 Generating lists](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#22-generating-lists)
  - [2.3 List operations](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#23-list-operations)
  - [2.4 List matching](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#24-list-matching)
  - [2.5 Tutorials: data structures](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#25-tutorials-data-structures)
- [Advanced Data Structures](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/)
  - [3.1 The Grasshopper data structure](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#31-the-grasshopper-data-structure)
  - [3.2 Generating trees](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#32-generating-trees)
  - [3.3 Tree matching](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#33-tree-matching)
  - [3.4 Traversing trees](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#34-traversing-trees)
  - [3.5 Basic tree operations](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#35-basic-tree-operations)
  - [3.6 Advanced tree operations](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#36-advanced-tree-operations)
  - [3.7 Tutorials: advanced data ](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#37-tutorials-advanced-data-structures)
- [{{< awesome "fas fa-download">}}](https://www.rhino3d.com/download/rhino/6.0/essential-algorithms/) [Download full PDF and GH examples](https://www.rhino3d.com/download/rhino/6.0/essential-algorithms/)

### GrasshopperでのPythonスクリプトの作成

- [Create Script Component](/guides/scripting/scripting-component/#script-component)
- [First Script](/guides/scripting/scripting-component/#first-script)
- [Script Inputs and Outputs](/guides/scripting/scripting-component/#script-inputs-and-outputs)
- [Edit Script](/guides/scripting/scripting-component/#edit-script)
- [Run Scripts](/guides/scripting/scripting-component/#debugging-scripts)
- [Debugging Scripts](/guides/scripting/scripting-component/#debugging-scripts)
- [Using Packages](/guides/scripting/scripting-component/#using-packages)
- [エディタの機能](/guides/scripting/scripting-component/#editor-features)
- [Grasshopper Scripting: Python](/guides/scripting/scripting-gh-python)
- [Creating Global Sticky Variables](/guides/rhinopython/ghpython-global-sticky/)
- [Node in Code from Python](/guides/rhinopython/ghpython-call-components/)
- [Custom GhPython Baking Component](/guides/rhinopython/ghpython-bake/)
- [Grasshopper data trees and Python](/guides/rhinopython/grasshopper-datatrees-and-python/)
- [GhPython Common Questions and Answers](/guides/rhinopython/ghpython-question-answer/)

### [GrasshopperでのC#スクリプトの作成](/guides/grasshopper/csharp-essentials/)

- [C# Component in Grasshopper](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#21-introduction)
- [C# Programming Basics](/guides/grasshopper/csharp-essentials/2-csharp-basics/)
- [RhinoCommon Geometry](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/)
- [Design Algorithms](/guides/grasshopper/csharp-essentials/4-design-algorithms/)

### Grasshopperのプラグイン

- [What is a Grasshopper Component?](/guides/grasshopper/what-is-a-grasshopper-component/)
- Installing Tools ([Windows](/guides/grasshopper/installing-tools-windows/), [Mac](/guides/grasshopper/installing-tools-mac/))
- Your First Component ([Windows](/guides/grasshopper/your-first-component-windows/), [Mac](/guides/grasshopper/your-first-component-mac/))
- [Developer samples on GitHub](https://github.com/mcneel/rhino-developer-samples)
- [Developer discussions on Discourse](https://discourse.mcneel.com/c/grasshopper-developer)
- [Distributing a Grasshopper Plug-In with the Package Manager](/guides/yak/creating-a-grasshopper-plugin-package/)

#### プラグインの基礎
{{< dev-topic-list "guides" "Grasshopper" "Fundamentals" "weight" >}}

#### 詳細
{{< dev-topic-list "guides" "Grasshopper" "In Depth" "weight" >}}

#### 上級
{{< dev-topic-list "guides" "Grasshopper" "Advanced" "weight" >}}


## [RhinoScript](/guides/rhinoscript)


*RhinoScriptはMicrosoftのVBScript言語を元にしたスクリプトツールです。RhinoScriptを使うと、Windows版Rhinoに機能を追加したり、繰り返し行う作業を自動化したりすることができます。*

### 概要

- [What are VBScript and RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript)

### [RhinoScript 101](/guides/rhinoscript/primer-101)

&nbsp;&nbsp; [Introduction](/guides/rhinoscript/primer-101)  
&nbsp;&nbsp; [Where to find help](/guides/rhinoscript/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [What's it all about?](/guides/rhinoscript/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [RhinoScript Essentials](/guides/rhinoscript/primer-101/2-vbscript-essentials/)  
&nbsp;&nbsp; 3. [Script Anatomy](/guides/rhinoscript/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operators and Functions](/guides/rhinoscript/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Conditional Execution](/guides/rhinoscript/primer-101/5-conditional-execution/)  
&nbsp;&nbsp; 6. [Arrays](/guides/rhinoscript/primer-101/6-arrays/)  
&nbsp;&nbsp; 7. [Geometry](/guides/rhinoscript/primer-101/7-geometry/)  
&nbsp;&nbsp; [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/5.0/rhinoscript101) [Download the RhinoScript 101 Primer as a single PDF ](https://www.rhino3d.com/download/rhino/5.0/rhinoscript101)

### 基礎

{{< dev-topic-list "guides" "RhinoScript" "Fundamentals" "weight" >}}


### 中級

{{< dev-topic-list "guides" "RhinoScript" "Intermediate" "weight" >}}

### 上級

{{< dev-topic-list "guides" "RhinoScript" "Advanced" "weight" >}}

### トラブルシューティング

{{< dev-topic-list "guides" "RhinoScript" "Troubleshooting" "weight" >}}

### その他のリソース

- [Pascal Golay's scripted utilities for Rhino](https://wiki.mcneel.com/people/pascalgolay)
- [RhinoScript Samples on GitHub](https://github.com/mcneel/rhinoscript)
- [RhinoScript Dash Docset](https://discourse.mcneel.com/t/rhinoscript-dash-docset/6382)
- [RhinoScript Help File On-Line](https://www.rhino3d.com/5/rhinoscript/index.html)

<!-- ## [Compute](/guides/compute) -->
<h2 id="compute"><a href="/guides/compute">Compute</a></h2>


### はじめに

{{< dev-topic-list "guides" "Compute" "Getting Started" "weight" >}}

### 実稼働環境への導入

{{< dev-topic-list "guides" "Compute" "Deployment" "weight" >}}

### Hops

{{< dev-topic-list "guides" "Compute" "Hops" "weight" >}}

## 開発者向けサービス

### [ローカライゼーション](https://www.rhino3d.com/localization)

弊社のヨーロッパ支店では、サードパーティ、またはその他の製品のフランス語、ドイツ語、イタリア語、スペイン語などへの翻訳、ローカライズサービスを行っています。 [詳細…](https://www.rhino3d.com/localization)

### マーケティングサポート

RhinoやのGrasshopperのアドオンを開発し、Rhinoのユーザーの方達にそれをお知らせされたい場合は、 [food4Rhino](https://www.food4rhino.com/) に詳細を掲載していただけます。 Food4Rhinoは、McNeelが無料で運用しているプラグインのコミュニティサービスです。このウェブサイトでは、最新のRhinoのプラグイン、Grasshopperのアドオン、マテリアル、テクスチャ、背景、スクリプトなどを見つけていただけます。 [FAQをご覧ください...](https://www.food4rhino.com/faq)

+++
aliases = ["/5/guides/general/rhino-technology-overview/", "/6/guides/general/rhino-technology-overview/", "/7/guides/general/rhino-technology-overview/", "/wip/guides/general/rhino-technology-overview/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "Rhino 技術架構摘要。"
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Rhino 技術概述"
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


## 概述

Rhinoceros 由許多層組成 - 用多種語言編寫 - 一層一層堆疊上去。最基礎的是底層，但頂層絕不應該被認為是膚淺的...

![The Rhino Stack](/images/rhino-technology-overview-01.png)

讓我們依序討論每一層，從基礎底層開始...

## 底層

### C++ Rhino Core

Rhino 的 C++ Core 是最古老、最廣泛的程式碼集。我們在很多地方使用微軟的 MFC，包括 SDK。這是管理 runtime 文件的地方，是所有 OpenGL 視窗建立程式碼所在的地方，也是我們數學家編寫的計算幾何程式碼所在的地方。Rhino 的許多指令都在這裡。

許多的使用者界面 - 指令行、應用程式主機、狀態列以及 Rhino core 許多指令的對話框。

### openNURBS

openNURBS 是免費的 C++ 原始程式碼，可讓您讀取和寫入 Rhino *3dm* 檔案 - 追溯到版本 1，openNURBS 是我們的第一個開放源碼項目。

該程式碼在 Windows、macOS、Linux、iOS 和 Android 編譯，可用於各種第三方應用程式，如 ArchiCAD、SolidWorks、Inventor、SketchUp 和其他許多可讀取或寫入 *3dm* 檔案的產品。

openNURBS 是 Rhino 本身用來讀取/寫入 *3dm* 檔案的工具。該工具包在 Rhino 之前就已發布，因此任何產品，包括我們的競爭對手，都可以和最新的 *3dm* 檔案相容。Rhino 寫的 *3dm* 檔案與其他使用 openNURBS 讀寫 *3dm* 的應用程式的檔案沒有區別。

有關 openNURBS 的更多訊息，請參閱 [openNURBS 指南](/guides/opennurbs/)。

### C++ SDK

最重要的是我們的 C++ SDK，僅在 Windows 上提供。

針對 C++ SDK 進行編譯需要特定版本的 Microsoft Visual Studio 和 Microsoft C-Runtime。您必須為 Rhino 的每個主要版本重新編譯。

事實上，Rhino 可以做的所有事情都是透過 C++ SDK 公開的。有些指令和功能還沒有公開，但這個 SDK 非常廣泛和豐富。

不幸的是，由於它與 Rhino Core 緊密結合，外掛程式開發人員需要為每個 Rhino 版本重新編譯他們的外掛程式。

有關 C++ SDK 的更多訊息，請參閱[ C/C++ 指南](/guides/cpp/)。

## C++ Stack

上面堆疊圖的右邊欄位是 Rhino 的 C++ 部分。C++ stack 允許我們以及第三方外掛程式開發人員使用與我們開發 Rhino 本身相同的 C++ SDK 編寫 Rhino 外掛程式。請注意，您無法使用 C++ 創作 Grasshopper 元件。

### C++ 外掛程式

C++ SDK 之上是 C++ 外掛程式。Rhino 附帶的許多功能，包括一些指令、檔案 I/O、彩現器實際上都是 C++ 外掛程式，另外還有數十個第三方 C++ 外掛程式，例如 [Asuni 的 VisualARQ](http://www.visualarq.com/)、[MecSoft 的 RhinoCAM](https://mecsoft.com/rhinocam-software/) 和 [Chaos Software 的 V-Ray](https://www.chaosgroup.com/vray/rhino)。

有關 C++ SDK 的更多訊息，請參閱[ C/C++ 指南](/guides/cpp/)。

### RhinoScript

[RhinoScript](/guides/rhinoscript/what-are-vbscript-rhinoscript/) 是我們隨 Rhino 提供的 C++ 外掛程式之一。RhinoScript 透過 VBScript (廣泛使用且流行的腳本語言) 公開 Rhino SDK 的一個有用子集。RhinoScript 不僅可以讓您存取 Rhino，還可以存取 Windows 上的任何其他 COM 物件。

相關的更多訊息，請參閱 [RhinoScript 指南](/guides/rhinoscript/)，若要更具體的話，可以參考[什麼是 VBScript 和 RhinoScript？](/guides/rhinoscript/what-are-vbscript-rhinoscript/)。

## .NET Stack

.NET SDK 在這裡分為三層：

- C API
- .NET Framework
- RhinoCommon
- Eto

### C API

直接的 C API 包裝 C++ SDK，讓我們可以將平台呼叫 (P/Invoke) 到 C++ SDK 中，從而在本機 C++ 程式碼和託管 .NET 層之間形成橋樑。

### .NET Framework

[.NET Framework](https://www.microsoft.com/net/framework) 是 Microsoft 開發。.NET 可以用 C#、F#、VB.NET 和任何其他可編譯為 Microsoft IL 的語言編寫外掛程式。

Microsoft .NET framework 隨 Windows 一起提供。

在 Rhino for Mac 產品，我們嵌入 [Mono Runtime](https://www.mono-project.com)，這是 .NET Runtime 的部分跨平台實現。

有關 .NET 及其與 Rhino 開發的關係，請參閱[什麼是 Mono 和 Xamarin？](/guides/rhinocommon/what-are-mono-and-xamarin/)

### RhinoCommon

RhinoCommon 是我們針對 Rhino 的 .NET SDK，建構在 Windows 和 macOS (透過 Mono) 上*通用*的 .NET framework 部分之上。RhinoCommon 允許開發人員在 Windows 版 Rhino 和 Mac 版 Rhino 上執行 .NET 程式碼。

有關 RhinoCommon 的更多訊息，請參閱 [RhinoCommon 指南](/guides/rhinocommon/)，更具體地，請參閱[什麼是 RhinoCommon？](/guides/rhinocommon/what-is-rhinocommon)。

### Eto

使用 RhinoCommon，您可以編寫可在 Windows 和 Mac 上執行的 .NET 外掛程式…使用者界面除外。Mono 團隊沒有複製 WinForms 或 WPF，因此這些技術都無法在 Mac 上運作。為了解決這個問題，Rhino 現在附帶 Eto.Forms。Eto 允許您使用 C#、XAML 或 JSON 編寫一次使用者界面，然後在 Windows 和 macOS 上使用它。實際上，用 Eto 編寫的 UI 也可以在 iOS、Android 和 Linux 上運作。

有關 Eto 的更多訊息，請參閱 [GitHub 上的 Eto.Forms](https://github.com/picoe/Eto)。

### .NET 外掛程式

建構在 RhinoCommon 之上的是許多外掛程式，包括內部外掛程式和第三方開發的外掛程式。例如，[Grasshopper](http://www.grasshopper3d.com/) 是一個 RhinoCommon 外掛程式。Rhino 中的一些指令、彩現器和檔案 IO 外掛程式實際上是作為 RhinoCommon 外掛程式編寫的。隨著時間的推移，我們正在將越來越多方便的功能轉移到 RhinoCommon/.NET 外掛程式中，以便在平台之間共享更多程式碼。 許多成功的第三方外掛程式也是使用 RhinoCommon 和 .NET 編寫的，例如 [RhinoGold](http://www.tdmsolutions.com/) 和 [GEMVision 的 Matrix](http://www.stuller.com/matrix)，以及 [Orca3D](http://orca3d.com/)。

有關 RhinoCommon 的更多訊息，參閱 [RhinoCommon 指南](/guides/rhinocommon/)。

### Grasshopper 元件

Rhino 現在附帶的 Grasshopper，這是我們用於演算法和參數化設計的視覺化程式語言。Grasshopper 本身就是一個開發平台，擁有[數百個第三方編寫的 Grasshopper 元件](http://www.food4rhino.com/grasshopper-addons)，用於執行各種操作，從[物理模擬](http://www.food4rhino.com/project/kangaroo)到[創建自訂使用者界面](http://www.food4rhino.com/project/human-ui)，再到[工業機器人程式設計和控制](http://www.food4rhino.com/project/hal)。

有關 Grasshopper 的更多訊息，如何更具體地開發 Grasshopper 元件，請參閱 [Grasshopper 指南](/guides/grasshopper/)。

### Python 指令碼

RhinoPython 是 Rhino 隨附的 .NET 外掛程式之一。RhinoPython 使用 [IronPython](http://ironpython.net/) ([Python](https://www.python.org/) runtime的 .NET 實現) 編寫，將整個 RhinoCommon SDK 公開給 Python 腳本語言。這意味著每當我們為 RhinoCommon 增加功能時，它都會自動顯示在 RhinoPython 中。

有關 RhinoPython 的更多訊息，參閱 [RhinoPython 指南](/guides/rhinopython/)。

## 相關主題

- [C/C++ 指南](/guides/cpp/)
- [openNURBS 指南](/guides/opennurbs/)
- [RhinoScript 指南](/guides/rhinoscript/)
- [Microsoft .NET Framework (位於 microsoft.com)](https://www.microsoft.com/net/framework)
- [什麼是 RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon)
- [RhinoCommon 指南](/guides/rhinocommon/)
- [什麼是 Mono & Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Mono 介紹](https://www.mono-project.com)
- [GitHub 上的 Eto.Forms](https://github.com/picoe/Eto)
- [Grasshopper 指南](/guides/grasshopper/)
- [RhinoPython 指南](/guides/rhinopython/)

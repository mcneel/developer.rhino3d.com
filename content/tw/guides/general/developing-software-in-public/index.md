+++
aliases = ["/5/guides/general/developing-software-in-public/", "/6/guides/general/developing-software-in-public/", "/7/guides/general/developing-software-in-public/", "/wip/guides/general/developing-software-in-public/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "McNeel 開發流程概述。"
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "公開開發軟體"
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

在過去的二十年裡，我們整合了一套流程來幫助我們贏得客戶的滿意度。這個流程有八個部分，它們都同樣重要。多年來，我們建立自己的專有工具支援此流程的大部分。但現在，有一些很棒的商用工具 - 我們也鼓勵您使用這些工具。

我們的軟體開發流程，就像其他流程一樣，是一個循環，所以我們可以從任何地方開始。

![Rhino Development Cycle](/images/developing-software-in-public-01.png)

## 循環流程

由於這是開發人員指南，所以我們從編寫程式碼開始。

### 程式碼

這就是我們作為軟體開發人員花費大量時間做的事情。我們打開最喜歡的 IDE，編寫程式碼、偵錯、解決問題。相信每個軟體開發人員都很習慣解決問題。

當我們得到一些東西時，就會將其*提交*到我們的版本控制系統...

### 提交

我們將程式碼提交到[版本控制系統](https://en.wikipedia.org/wiki/Version_control)。我們的作法是將 [git](https://git-scm.com/) 與 [GitHub](https://github.com/) 結合使用。此外還有許多其他版本控制系統。我們以前用 [Subversion](https://subversion.apache.org/)，但現在我們用 [GitHub](https://github.com/)。[GitHub](https://github.com/) 與許多其他工具配合得很好，並且擁有非常豐富的 API。不過也還有其他值得考慮的：如 [BitBucket](https://bitbucket.org)、[Mercurial](https://www.mercurial-scm.org/) 等。

如果您沒有使用任何版本控制系統，我們懇切希望您可以從現在開始。其實很容易，而且它可以讓您在出現問題之前返回軟體的其他版本，就像一個團隊進行合作一樣。任何類型的建置自動化都需要它。

作為開發人員，我們使用 [GitHub Flow](https://guides.github.com/introduction/flow/) 的修改版本建立並合併 pull requests 到我們的主分支 (master branch)。

提交程式碼後，我們進行...

### 編譯

我們除了在辦公桌上進行編譯之外，我們還有專用的 [TeamCity](https://www.jetbrains.com/teamcity/) 伺服器不斷建立我們的程式碼，並驗證它是否與我們在 [GitHub](https://github.com/) 上的主分支一起工作。這可以確保我們不會破壞彼此獲取最新程式碼和編譯的能力。

這些 [TeamCity](https://www.jetbrains.com/teamcity/) 伺服器會驗證每次提交，並建立我們的每日版本 (其中有許多版本)，大約每四小時一次，另外還會建立我們的公用 WIP 和修正版本。

對於每個新版本，我們都會進行測試...

### 測試

當開發人員修復錯誤並解決問題時，我們的內部測試人員會確保公用建置正常運作，也會依據客戶測試 WIP 和修正版候選版。

下一步是發布 (發布前和發布後都會進行測試)...

### 發布

每當我們有一個版本可供客戶使用時，我們就會部署 (或發布) 它。

包括以下...

- [可下載的安裝程式](http://www.rhino3d.com/download)
- [SDKs](http://developer.mcneel.com)
- 文件 (例如這個頁面)

...並透過電子郵件、部落格和社交媒體發布公告。

### 傾聽

我們盡可能以多種方式進行傾聽:

- [交談](http://www.rhino3d.com/support#)
- [電子郵件](mailto:tech@mcneel.com)
- 技術支援 (206) 545-6877
- [論壇](https://discourse.mcneel.com/)

通常，當我們傾聽時，我們會發現需要解決的問題。有時是很小的問題…有時是很大的問題。無論如何，我們都會將問題記錄下來...

### 追蹤

我們在 [YouTrack](https://mcneel.myjetbrains.com) 記錄問題。

[YouTrack](https://mcneel.myjetbrains.com) 對我們來說效果很好，因為它可以幫助我們確保每個問題都得到正確的測試和記錄。

### 確定優先順序

要弄清楚下一個最重要的事情是什麼是很困難的。我們與客戶互相交談，使用 Gmail、Google 雲端硬碟和 Google 文件進行交流。在 [Slack](https://slack.com/) 可以 24 小時的交談。

我們每週二開會。在我們開會之前，我們會先在 Google 文件分享我們所做的事情，也會分享接下來要發布的每個產品的目標、正在開發的每個功能群組，包括我們隨著時間的推移如何進展的圖表，還有連結回到我們的 [YouTrack](https://mcneel.myjetbrains.com) 問題，並且得到每個負責該功能的人員的報告。

此外，每個開發人員都會寫下他們一直在做什麼、下一步計劃做什麼以及完成工作時遇到的障礙。

### 自動化

最後但同樣重要的一點是，我們做了很多自動化的工作。

以下是我們進行自動化所做的一些事情：

- 在進入我們的主開發分支之前，建立每個開發人員的每個提交。
- 當 [TeamCity](https://www.jetbrains.com/teamcity/) 伺服器將修復合併到我們的主開發分支時，將關閉 [YouTrack](https://mcneel.myjetbrains.com) 中的問題。
- 在我們的 [TeamCity](https://www.jetbrains.com/teamcity/) 伺服器建立內部和公用版本。
- 透過在 [Slack](https://slack.com/) 輸入指令發布新的 WIP 版本。
- 將公用版本上傳到我們的下載伺服器。

## 公開

直到最近，我們已公開流程的以下部分：

- 測試
- 發布 (如同您看到我們發布的內容)
- 傾聽

在過去幾年中，我們透過切換到 YouTrack 公開我們的問題追蹤器。而某些問題需要隱藏，是因為出於安全或用戶隱私原因。

我們近期想做的就是將更多資訊公開：

- 在 GitHub 將我們的一些程式碼作為公共儲存庫共享，以便您可以使用一些真實的、經過生產驗證的程式碼範例。
- 讓您分享我們程式碼的修復和改進。
- 透過將 RhinoCommon 發布為 NuGet 套件，可以更輕鬆地建立外掛程式專案。
- 必要時幫助建立自動化。

## 相關主題

- [Rhino 技術概述](/guides/general/rhino-technology-overview)
- [貢獻](/guides/general/contributing)
- [開發人員的必要條件](/guides/general/rhino-developer-prerequisites)

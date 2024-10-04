+++
aliases = ["/en/5/guides/general/developing-software-in-public/", "/en/6/guides/general/developing-software-in-public/", "/en/7/guides/general/developing-software-in-public/", "/wip/guides/general/developing-software-in-public/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "McNeelの開発プロセスについての概要"
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "公開のソフトウェア開発"
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

当社は過去20年の間、お客様に満足していただけるようなソフトウェア開発プロセスを構築してきました。このプロセスには8つの部分があり、どれもが同じように重要です。長年に渡り、当社はこのプロセスのほとんどの部分をサポートするために独自のツールを構築してきましたが、今では優れた市販ツールがあります。(これらは皆さまにもぜひ使用していただきたいツールです。)

当社のソフトウェアの開発プロセスは、他のプロセスと同様にサイクルとなっており、どこからでも開始可能です。

![Rhino Development Cycle](/images/developing-software-in-public-01.png)

## サイクル

これは開発者向けのガイドなので、まずは「Code (コード)」から説明を始めましょう。

### Code (コード)

この部分は、私達ソフトウェア開発者が多くの時間を費やしている部分です。お気に入りのIDE(統合開発環境)を開いて、コードを書き、デバッグし、問題を解決します。

何かが出来上がると、私達はそれをバージョン管理システムに *コミット* します。

### Commit (コミット)

コードは [バージョン管理システム](https://en.wikipedia.org/wiki/Version_control) にコミットします。私達の場合、 [GitHub](https://github.com/) で [git](https://git-scm.com/) を使用しています。バージョン管理システムは他にもいろいろあり、以前は [Subversion](https://subversion.apache.org/) を使用していましたが、現在は [GitHub](https://github.com/) を使用しています。 [GitHub](https://github.com/) は他の多くのツールとうまく連携し、豊富なAPIを備えています。(しかし、 [BitBucket](https://bitbucket.org) や [Mercurial](https://www.mercurial-scm.org/) など、検討する価値のある他のツールもあります。)

バージョン管理をまったく使用していない場合は、ぜひ使用してください。現在では非常に簡単です。バージョン管理を使用すると、ソフトウェアを問題が発生する前のバージョンを選んで戻すことができます。チームとして共同作業するのに役に立ちます。バージョン管理はどのような種類のビルド自動化にも必要なものです。

私達は開発者として、 [GitHub Flow](https://guides.github.com/introduction/flow/) の変更バージョンを使用してプルリクエストを作成し、マスターブランチにマージします

コードをコミットしたら、それをビルドします。

### Compile (コンパイル)

私達は自分達のデスクでコンパイルするだけでなく、コードを継続的にビルドする専用の複数の [TeamCity](https://www.jetbrains.com/teamcity/) サーバーを使用し、[GitHub](https://github.com/) のマスターブランチと適合するかどうかを確認しています。これにより、お互いが最新のコードを取得してコンパイルが正常に行えます。

これらの [TeamCity](https://www.jetbrains.com/teamcity/) サーバーは、すべてのコミットを検証し、毎日のリリースをビルドします(多くの場合、約4時間毎)。また、公開用のWIPビルドやサービスリリースのビルドもビルドします。

ビルドはそれぞれテストを行います。

### Test (テスト)

開発者がバグを修正し、イシューをクローズすると、社内のテストスタッフが公開予定のビルドが正しく動作することを確認します。また、WIPビルドとリリース候補ビルドはお客さまにも試していただいています。

テストは次のステップである公開の前と後に行っています。

### Publish (公開)

お客様に提供する準備が整ったビルドができたら、それをデプロイ(または公開)します。

これには、下記のリリースが含まれます。

- [ダウンロード可能なインストーラ](http://www.rhino3d.com/download)
- [SDK](http://developer.mcneel.com)
- ドキュメンテーション

また、メール、ブログ、そしてソーシャルメディアを通じて公に発表します。

### Listen (お客様のフィードバックに耳を傾ける)

私達はできる限り多くの方法でフィードバックに耳を傾けます:

- [チャット](http://www.rhino3d.com/support#)
- [メール](mailto:tech@mcneel.com)
- 電話によるサポート (206) 545-6877
- [フォーラム (Discourse)](https://discourse.mcneel.com/)

フィードバックに耳を傾けると、解決すべき問題が見つかることがよくあります。小さな問題もあれば、非常に大きな問題もあります。私たちは常に問題を記録しています。

### Track (追跡)

課題(問題)は [YouTrack](https://mcneel.myjetbrains.com) に記録します。

[YouTrack](https://mcneel.myjetbrains.com) は、各課題が適切に検証され、文書化されることを確実にできるため、当社にとって非常に便利です。

### Prioritize (優先順位付け)

開発にとって次に何が最も重要なことかを見極めるのは困難なため、私達はお客様と連絡を取り合います。コミュニケーションにはGmail、Googleドライブ、Googleドキュメントを使用します。私達は [Slack](https://slack.com/) を用い24時間チャットしています。

私達は毎週火曜日にミーティングを行います。ミーティングの前、そしてミーティング中には、Googleドキュメントで次にリリースするバージョン、製品、機能の目標を共有します。ドキュメントは、時間の経過に伴う進捗状況のグラフや [YouTrack](https://mcneel.myjetbrains.com) の課題へのリンクなども含んでいます。

また、各開発者は、これまで何に取り組んできたか、次に何を計画しているか、そして仕事の完了を妨げているものは何かなどをドキュメントに記入します。ミーティングでは、機能に取り組んでいる各メンバーから口頭で報告も受けています。

### 自動化

私達の行っていることで忘れてはいけないのは、多くの自動化です。

これらは私達が自動化していることのいくつかです:

- すべての開発者からのすべてのコミットを、マスター開発ブランチに移動する前にビルドする
- [TeamCity](https://www.jetbrains.com/teamcity/) サーバーによって修正がマスター開発ブランチにマージされたら、 [YouTrack](https://mcneel.myjetbrains.com) の課題を閉じる
- [TeamCity](https://www.jetbrains.com/teamcity/) サーバー上で社内リリースと公開リリースをビルドする
- [Slack](https://slack.com/) にコマンドを入力して、新しいWIPリリースを公開する
- 公開リリースをダウンロードサーバーにアップロードする

## 公開範囲

最近まで、私達が公開していたプロセスの一部は次のとおりです。

- Test (テスト)
- Publish (公開)
- Listen (お客様のフィードバックに耳を傾ける)

上記の内容に加えて、私達は数年前にYouTrackに切り替えて課題の追跡を公開しました。(セキュリティやユーザーのプライバシー上の理由から、一部の課題は一般公開されません。)

私達が近々したいことは、公開内容を増やすことです:

- 実際の問題なく運用できるコード例を参考にできるように、私達のコードの一部をGitHubのパブリックリポジトリとして共有する
- 私達のコードに加えた修正や改良を共有する
- RhinoCommonをNuGetパッケージとして公開することで、プラグインのプロジェクトのビルドを容易にする
- 必要に応じてビルドの自動化を支援する

## 関連トピック

- [Rhinoの技術的概要](/guides/general/rhino-technology-overview)
- [Contributing](/guides/general/contributing)
- [Developer Prerequisites](/guides/general/rhino-developer-prerequisites)

+++
aliases = ["/en/5/guides/yak/what-is-yak/", "/en/6/guides/yak/what-is-yak/", "/en/7/guides/yak/what-is-yak/", "/en/wip/guides/yak/what-is-yak/"]
authors = [ "will" ]
categories = [ "Overview" ]
description = "In dieser Anleitung wir der Rhino-Paketmanager (alias Yak) vorgestellt."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Was ist der Paketmanager?"
type = "guides"
weight = 1
override_last_modified = "2020-11-12T12:17:36Z"

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

## Übersicht

Der Paketmanager dient als Hilfe bei der Entdeckung, Installierung und Verwaltung von Ressourcen rund um Rhino (einschließlich Grasshopper). Derzeit werden Rhino- und Grasshopper-Plug-ins unterstützt, aber das Ziel ist es, in Zukunft auch Dinge wie Skripte, Materialien, Ansichtsfenster usw. einzubeziehen!

{{< call-out "note" "Hinweis" >}}
Der Rhino-Paketmanager war ursprünglich unter dem Codenamen "Yak" bekannt. Der Name Yak wird immer noch für das Kommandozeilenwerkzeug verwendet, das Pakete erstellt und veröffentlicht.
{{< /call-out >}}

Der Paketmanager verfolgt mehrere Ziele.

- Den Anwendern das Entdecken und Verwalten von Plug-ins und mehr zu erleichtern.
- Entwickler und Autoren wiederverwendbarer Inhalte bei der gemeinsamen Nutzung ihrer Arbeit zu unterstützen.
- Einfache Werkzeuge zur Systemverwaltung bereitzustellen.

Da wir nicht das Rad neu erfinden wollten, haben wir uns von Linux und der
Softwareentwicklung im Allgemeinen inspirieren lassen. Das Paketverwaltungssystem kann in drei Hauptbereiche
unterteilt werden.

1. [Server](#server)
2. [Integrationen](#integrations)
3. [Befehlszeilenwerkzeuge](#command-line-tool)

## Server

Der Paketserver ist das Herzstück des Systems. Einmal erstellte Pakete werden auf den Server
übertragen, um sie mit anderen zu teilen. Er hält die Pakete für seine Clients
organisiert - das Kommandozeilenwerkzeug und Rhino (über Integrationen).

{{< call-out "note" "Hinweis" >}}
Zusätzlich zum öffentlichen Paketserver (https://yak.rhino3d.com) unterstützt der Paketmanager auch Datei- bzw. Ordner-basierte [Benutzerdefinierte Paket-Repositories](../package-sources).
{{< /call-out >}}

## Integrationen

Integrationen bieten einen direkten Zugriff auf das Paket-Ökosystem innerhalb von Rhino. Gegenwärtig geschieht dies auf zwei Arten: "Paketwiederherstellung" für Grasshopper und die Paketmanager-UI.

### Paketwiederherstellung in Grasshopper

Der Rhino-Paketmanager wurde in den Grasshopper-Dialog "Unerkannte Objekte" integriert und bietet [Paketwiederherstellung](../package-restore-in-grasshopper)-Funktionalität. Beim Öffnen einer neuen Datei, die Komponenten eines nicht auf dem Rechner installierten Plug-ins enthält, hat der Benutzer die Möglichkeit, auf dem Paketserver nach den fehlenden Plug-ins zu suchen und sie direkt zu installieren.

![Package restore for Grasshopper](/images/yak-gh-restore-guid.gif)

### Paketmanager-UI

Die Benutzeroberfläche des Paketmanagers ist über den Befehl `PaketManager` verfügbar. Es bietet eine NuGet-ähnliche Schnittstelle, die es den Benutzern ermöglicht, nach Paketen zu suchen, sie zu installieren und zu sehen, ob Aktualisierungen für aktuell installierte Pakete verfügbar sind.

![The package manager UI](/images/testpackagemanager-wip.jpg)

## Befehlszeilenwerkzeug

Das Kommandozeilen-Tool bietet eine einfache, aber mit voller Funktionalität ausgestattete Schnittstelle. Es orientiert sich an bekannten domänenspezifischen Paketmanagern wie Ruby's `gem` und Python's `pip`. Es kommuniziert mit dem Server und verbindet sich zur Authentifizierung mit Rhino Accounts.

Auf Windows finden Sie das Tool unter `"C:\Programme\Rhino {{< latest-rhino-version >}}\System\yak.exe"`.
Auf dem Mac gibt es das Skript `"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"`.

Geben Sie `<path_to_yak> help` ein, um zu beginnen.



## Verwandte Themen

- [Anatomie eines Pakets](/guides/yak/the-anatomy-of-a-package/)
- [Das Paketmanifest](/guides/yak/the-package-manifest/)
- [Yak CLI-Referenz](/guides/yak/yak-cli-reference)

+++
aliases = ["/en/5/guides/general/rhino-installer-engine/", "/en/6/guides/general/rhino-installer-engine/", "/en/7/guides/general/rhino-installer-engine/", "/en/wip/guides/general/rhino-installer-engine/"]
authors = [ "brian", "will" ]
categories = [ "Fundamentals" ]
description = "Diese Anleitung ist eine kurze Einführung in die Rhino-Installer-Engine."
keywords = [ "developer", "rhino", "installer" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Rhino-Installer-Engine"
type = "guides"
weight = 6
override_last_modified = "2021-07-27T08:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinoinstallerengine/overview"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

{{< call-out "warning" "Wichtig" >}}
⚠️ Diese Technologie ist ab Rhino 7 veraltet und wurde durch das <a href="/guides/yak/">yak-Format zusammen mit dem Paketmanager</a> ersetzt.
{{< /call-out >}}

## Überblick (Windows)

Die Rhino-Installer-Engine vereinfacht die Verteilung, Installation und Aktualisierung von Plug-ins für Rhino für Windows.

## Wie funktioniert das?

### Datei- und Ordnerstruktur

Ein Rhino-Installer-Paket ist eine Zip-Datei mit der Erweiterung *.rhi* . Das Paket kann mehr als eine Version eines Plug-ins enthalten, jedoch müssen alle Versionen die gleiche GUID haben (d.h. sie sind verschiedene Versionen des _gleichen_ Plug-ins).

Es gibt keine Anforderungen an die Dateistruktur oder die Namensgebung. Zum Beispiel sind die beiden folgenden Pakete funktionell gleichwertig. Beide enthalten Versionen von "Marmoset" - ein fiktives C++ Plug-in, das für Rhino 5 (32-bit und 64-bit) und Rhino 6[^1]kompiliert wurde.

```
Marmoset_tree.rhi/
├── Rhino 6/
│   ├── Marmoset.rhp
│   ├── Marmoset.dll
│   └── Marmoset.rui
└── Rhino 5.0/
    ├── x86/
    │   ├── Marmoset.rhp
    │   └── ...
    └── x64/
        ├── Marmoset.rhp
        └── ...
```

```
Marmoset_flat.rhi/
├── Marmoset_rhino6.rhp
├── Marmoset_rhino5_x86.rhp
├── Marmoset_rhino5_x64.rhp
├── Marmoset_rhino6.dll
├── ...
└── Marmoset.rui
```

Sie können alles, was Sie wollen, in das *.rhi* -Paket aufnehmen - unterstützende DLLs, Hilfedateien, Dokumentation, [Toolbar- (*.rui-*) Dateien](/guides/rhinocommon/create-deploy-plugin-toolbar.md) usw. Der gesamte Inhalt wird in ein Verzeichnis auf dem Rechner des Benutzers entpackt.

### Installation und Kompatibilität

Die Rhino Installer Engine prüft jede *.rhp*-Datei und extrahiert die Plug-in-GUID, den Titel, die Version, das verwendete SDK (z.B. RhinoCommon, C++) und die SDK-Version. Diese Information wird verwendet, um festzustellen, welche Version des Plug-ins für welche installierte Version von Rhino für Windows installiert wird; das neueste kompatible Plug-in wird mit der entsprechenden Version von Rhino registriert. RhinoCommon-Plug-ins, die als `AnyCPU` kompiliert wurden, werden sowohl für 32- als auch 64-Bit-Rhino 5[^1] installiert.

{{< call-out "note" "Hinweis" >}}
<strong>Seit Rhino 6:</strong> Wenn ein RhinoCommon-Plug-in gefunden wird, das für eine frühere _Hauptversion_ von Rhino kompiliert wurde als die installierte, wird eine eingehende Kompatibilitätsprüfung durchgeführt, um festzustellen, ob das SDK des installierten Rhino die vom Plug-in verwendete Funktionalität noch unterstützt. Wenn die Prüfung erfolgreich ist, wird das veraltete Plug-in installiert.
{{< /call-out >}}

## Einschränkungen

- Die Rhino-Installer-Engine kopiert Dateien aus dem *.rhi*-Archiv und registriert die gefundenen Plug-ins. Es wird keine weitere Ausführung vorgenommen.
- Derzeit ist es nicht möglich, *.rhi*-Dateien digital zu signieren, um die Quelle von *.rhi*-Dateien zu überprüfen.
- Die Rhino-Installer-Engine ist mit Rhino 5 und neuer verfügbar.

## Verwandte Themen

- [Plug-in-Installer (Windows)](/guides/rhinocommon/plugin-installers-windows)
- [Plug-in-Installer (Mac)](/guides/rhinocommon/plugin-installers-mac)

**Fußnoten**

[^1]: Since version 6 Rhino for Windows has been 64-bit only.

+++
aliases = ["/en/5/guides/yak/the-anatomy-of-a-package/", "/en/6/guides/yak/the-anatomy-of-a-package/", "/en/7/guides/yak/the-anatomy-of-a-package/", "/en/wip/guides/yak/the-anatomy-of-a-package/"]
authors = [ "will", "callum" ]
categories = [ "Fundamentals" ]
description = "Dieser Leitfaden erläutert die Struktur eines Yak-Pakets."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Die Anatomie eines Pakets"
type = "guides"
weight = 1

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

## Struktur des Pakets

Pakete sind einfach ZIP-Archive mit der Erweiterung .yak. Nehmen Sie dieses einfache Beispiel...

```
howler-0.4.0-any-any.yak
├── manifest.yml
├── Howler.rhp
├── Howler.rui
├── HowlerCommon.dll
├── HowlerGrasshopper.gha
└── misc/
    ├── README.md
    └── LICENSE.txt
```

### Eine Anmerkung zu .NET Multi-Targeting

Ab Rhino 8 unterstützt Yak auch Mehrfach-Anwendungen, so dass Ihr Rhino-Plug-in entweder in dotnet core oder dotnet framework ausgeführt werden kann.
Beachten Sie, dass die Datei `manifest.yml` nun außerhalb des Framework-Verzeichnisses liegen muss, anstatt innerhalb des Verzeichnisses.

```
howler-0.4.0-rh8-any.yak
├── manifest.yml
├── net48/
│  ├── Howler.rhp
│  ├── Howler.rui
│  ├── HowlerCommon.dll
│  ├── HowlerGrasshopper.gha
│  └── misc/
│     ├── README.md
│     └── LICENSE.txt
└── net7.0/
   ├── Howler.rhp
   ├── Howler.rui
   ├── HowlerCommon.dll
   ├── HowlerGrasshopper.gha
   └── misc/
      ├── README.md
      └── LICENSE.txt
```

## Bedingungen

1. Pakete **müssen** eine `manifest.yml` Datei im obersten Verzeichnis haben. Details über das Manifest können im [Manifest Reference Guide](../the-package-manifest) gefunden werden.
1. Alle Plug-ins (`.rhp`-, `.gha`-, `.ghpy`-Dateien) **müssen** sich im obersten Verzeichnis, oder in einem [Multi-Targeting-Verzeichnis](#a-note-on-net-multi-targeting) befinden, damit Rhino und Grasshopper sie finden und laden können.
1. Paketversionsnummern **müssen** entweder [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) (z.B. `1.1.0-beta`) oder `System.Version`, auch bekannt als Microsofts vierstelliger Standard (z.B. `1.2.3.4`), folgen. Es wird empfohlen, Semantic Versioning zu verwenden, da es Paketautoren erlaubt, Vorabversionen anzugeben. Diese sind praktisch für begrenzte Tests, da standardmäßig die neueste _stable_ Version installiert ist.

## Distributionen

Für eine einzelne Paketversion ist es möglich, mehrere "Distributionen" hochzuladen, um auf verschiedene Rhino-Versionen und -Plattformen abzuzielen. Diese Informationen werden in einem "Distributions-Tag" kodiert, das an den Dateinamen des Pakets angehängt wird, z.B. _example-1.0.0-rh7-win.yak_.

Das Distributions-Tag besteht aus einem "App"-Kennzeichen und einer Version sowie einer Plattform. Derzeit werden nur die Anwendungen `rh` und `any` unterstützt - Grasshopper wird mit Rhino ausgeliefert und benötigt daher keinen eigenen Bezeichner. Sofern es sich nicht um die Anwendung `any` handelt, muss eine Anwendungsversion in der Form `<major>_<minor>` aufgenommen werden. Die Minor-Version ist optional und nützlich, wenn ein Plug-in auf einer SDK-Änderung beruht, die in einem Service-Release vorgenommen wurde. Die Plattform kann `win`, `mac` oder `any` (d.h. plattformübergreifend) sein.

Ein paar Beispiele...

* `rh7-win` - Rhino 7 für Windows >= 7.0
* `rh6_14-mac` - Rhino 6 für Mac >= 6.14
* `rh6_9-any` - Rhino 6 (beide Plattformen) >= 6.9
* `any-any` - alles geht! (bestehendes Verhalten)

Bei der Installation von Paketen prüft der Paketmanager, ob eine kompatible Distribution für die gewünschte Version existiert. Nur Paketversionen, die mindestens eine kompatible Distribution haben, werden angezeigt, wenn der Befehl `_PackageManager` in Rhino 7+ ausgeführt wird.

Der aktualisierte Server funktioniert reibungslos mit bestehenden Paketen und alten Versionen von Rhino. Bereits auf dem Server vorhandene Versionen (ohne Distributionen) werden bei der Installation als `any-any` behandelt. Neue Paketversionen, die kein Distributions-Tag enthalten, z.B. solche, die von früheren Versionen des CLI erstellt wurden, werden bei der Veröffentlichung ebenfalls als "any-any" behandelt.

## Weitere Schritte:

Nachdem Sie nun gesehen haben, was in einem Paket enthalten ist, sollten Sie ein Paket erstellen:

* [Erstellen Sie ein Grasshopper-Paket](../pushing-a-package-to-the-server) für Ihr Plug-in.
* [Erstellen Sie ein Rhino-Paket](../pushing-a-package-to-the-server) für alle.
* [Erstellen Sie ein Paket mit mehreren Zielgruppen](../creating-a-multi-targeted-rhino-plugin-package) für Rhino 8.

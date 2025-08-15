+++
aliases = ["/en/5/guides/yak/package-restore-in-grasshopper/", "/en/6/guides/yak/package-restore-in-grasshopper/", "/en/7/guides/yak/package-restore-in-grasshopper/", "/en/wip/guides/yak/package-restore-in-grasshopper/"]
authors = [ "will" ]
categories = [ "Features" ]
description = "Wie kann Grasshopper Yak nutzen, um die Dinge zu vereinfachen?"
keywords = [ "yak", "grasshopper" ]
sdk = [ "Yak" ]
title = "Paketwiederherstellung in Grasshopper"
type = "guides"
weight = 1
override_last_modified = "2020-10-21T15:58:32Z"

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

Zunächst ist dies weniger eine Anleitung für Entwickler als vielmehr eine Beschreibung der Funktionsweise, damit Sie als Entwickler besser verstehen können, wie Ihr Paket und Ihr Plug-in eingerichtet werden müssen, um diese Funktion zu nutzen.

Es kann frustrierend sein, eine Grasshopper-Definition zu öffnen und dann festzustellen, dass die erforderlichen Plug-ins nicht auf dem System installiert sind. Der Paketmanager kann helfen, indem er den Prozess der Erfüllung dieser Abhängigkeiten rationalisiert.

Seit Rhino 6 bietet das Dialogfeld "Nicht erkannte Objekte" dem Benutzer die Möglichkeit, fehlende Plug-ins _herunterzuladen und zu installieren_. Diese Funktion wird als Paketwiederherstellung bezeichnet.

![Grasshopper package restore](/images/yak-gh-restore.gif)

Die Paketwiederherstellung verwendet den Namen, die ID und die Version der fehlenden Plug-ins, um den Paketserver zu durchsuchen. Wenn Pakete der Suchanfrage entsprechen, werden sie installiert und, wenn möglich, vor dem Öffnen der Definition geladen[^3].

<iframe width="560" height="315" src="https://www.youtube.com/embed/MsjRdRtHW08" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Anpassung

### Benennung

Im Idealfall stimmen der Name des Grasshopper-Plug-ins und der des Pakets überein. Falls dies nicht möglich ist - entweder aufgrund der Beschränkungen des Paketnamen-Schemas[^1] oder aufgrund der Tatsache, dass es mehrere Plug-ins in einem Paket gibt, die jeweils einen anderen Namen haben - kann das richtige Paket auch anhand der Plug-in-ID identifiziert werden.

Für jede .gha-Datei wird die Plugin-ID extrahiert und der `manifest.yml` hinzugefügt, wenn Sie `yak build` ausführen.

### Versionsnummern

Paketversionsnummern können entweder der Spezifikation [Semantic Versioning 2.0.0](https://semver.org) (SemVer) folgen oder sie können vierstellig sein[^2], wie in `System.Version`. Siehe den [Paketserver](../the-package-server)-Leitfaden für weitere Details zu den erlaubten Versionsnummernformaten.

Der Server erlaubt sowohl SemVer als auch vierstellige Zahlen, da einige Grasshopper-Plug-ins ihre Versionsnummer als `String` in einer von `GH_AssemblyInfo` abgeleiteten Klasse angeben, während andere auf das `AssemblyVersionAttribute` zurückgreifen.

Wenn beim Wiederherstellen von Paketen ein Paket auf dem Server existiert, das entweder mit dem Namen oder der ID des fehlenden Plug-ins übereinstimmt, aber die genaue Version nicht existiert, wird die neueste stabile Version installiert.

[^1]: Paketnamen sind ziemlich strikt. Nur Buchstaben und Zahlen sowie Binde- und Unterstriche sind erlaubt.
[^2]: Unterstützung für vierstellige (`System.Version`) Versionsnummern wurde in Yak 0.8 hinzugefügt.
[^3]: Hinzugefügt in Grasshopper im Dezember 2019. Dynamisches Laden ist nur möglich, wenn noch keine andere Version der Grasshopper-Bibliothek installiert und geladen ist. Andernfalls muss Rhino neu gestartet werden, um die neue Version der Bibliothek zu laden.

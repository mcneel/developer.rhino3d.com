+++
aliases = ["/en/5/guides/yak/package-sources/", "/en/6/guides/yak/package-sources/", "/en/7/guides/yak/package-sources/", "/en/wip/guides/yak/package-sources/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Dies ist eine Kurzanleitung zur Konfiguration benutzerdefinierter Paket-Repositories in Rhino."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Benutzerdefinierte Paket-Repositorien"
type = "guides"
weight = 20
override_last_modified = "2021-02-12T11:31:53Z"

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

<!-- {{< call-out "note" "Hinweis" >}}
Diese Funktion erfordert die Änderung der erweiterten Einstellungen in Rhino!
{{< /call-out >}} -->

Rhino verwendet standardmäßig den offiziellen McNeel-Paketserver - https://yak.rhino3d.com. Zusätzlich (oder stattdessen!) ist es möglich, Rhino so zu konfigurieren, dass es Ihre eigenen Paket-Repositories verwendet.

Ein benutzerdefiniertes Paket-Repository ist einfach ein Ordner, der .yak-Paketdateien enthält. Der Ordner kann sich auf dem lokalen Rechner oder auf einem gemeinsamen Dateiserver befinden. Sie können Rhino so konfigurieren, dass Pakete aus diesem Repository in den Paketmanager aufgenommen werden, indem Sie die folgenden Schritte ausführen.


1. Gehen Sie zu _Optionen > Erweitert_ und suchen Sie nach der Einstellung `Rhino.Options.PackageManager.Sources`.
1. Fügen Sie den vollständigen Pfad zu Ihrem Paket-Repository-Ordner hinzu und trennen Sie ihn durch ein Semikolon vom Standard-Paket-Server, z. B. `https://yak.rhino3d.com;C:\rhino_packages`.
1. Führen Sie den Befehl `_PackageManager` aus und suchen Sie nach einem der Pakete, die Sie dem neuen Paket-Repository hinzugefügt haben.

Im Moment unterstützt es nur, was Directory.EnumerateFiles() unterstützt, was, soweit ich sagen kann, reguläre Pfade, zugeordnete Laufwerke (Windows), UNC-Pfade (Windows) und eingebundene Freigaben (macOS) sind.

### Tipps für gemeinsame Ordner

Unter Windows verwenden Sie den UNC-Pfad, d. h. `\\server\share\packages`. Wenn für die Freigabe Anmeldedaten erforderlich sind, navigieren Sie zunächst im Explorer zu `\\server` in Explorer, melden Sie sich an und aktivieren Sie das Kontrollkästchen "Anmeldedaten speichern".

Unter macOS muss die Dateifreigabe zunächst im Finder über _Gehen zu > Mit Server verbinden..._ (<kbd>⌘</kbd> + <kbd>K</kbd>) eingehängt werden. Geben Sie die Adresse ein (`smb://server/share`) und geben Sie bei Aufforderung Anmeldedaten an. Jetzt kann der gemountete Pfad als Paketquelle verwendet werden, d.h. `/Volumes/share/packages`. Das Mount ist nicht dauerhaft, so dass es in Zukunft wieder eingehängt werden muss.

### Vom Administrator erzwungene Einstellungen

Unter [Vom Administrator erzwungene Einstellungen](https://docs.mcneel.com/rhino/8/help/de-de/index.htm#information/admin-enforced_settings.htm) finden Sie Tipps, wie Sie diese Einstellung für Windows-Benutzer in Ihrer Organisation bereitstellen und erzwingen können.

### Leistung

Seit Rhino 8.15 sind einige Leistungsverbesserungen für private Paket-Repositorien enthalten.

Das Werkzeug yak.exe verfügt über einen neuen "Cache"-Befehl, der, wenn er innerhalb des privaten Paketordners ausgeführt wird, einen Index der verfügbaren Pakete erstellt. Wenn der Paketmanager diese Indexdatei sieht, verwendet er sie, _anstatt_ das Verzeichnis zu durchsuchen. Dadurch wird die Ladezeit des Paketmanagers bei privaten Repositorien mit vielen Paketen, großen Paketen oder langsamen Netzwerkverbindungen erheblich verkürzt.

```
$ cd X:\private\repo\directory
$ "C:\Program Files\Rhino 8\System\yak.exe" cache

Building cache for local package repository in X:\private\repo\directory

[...]
```

Stellen Sie sicher, dass der Cache neu erstellt wird, wenn Paketdateien hinzugefügt oder aus dem Verzeichnis entfernt werden. Entfernen Sie die _.cache*_-Dateien aus dem Verzeichnis, um das alte Verhalten wiederherzustellen.

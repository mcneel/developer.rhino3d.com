+++
aliases = ["/en/5/guides/yak/installing-and-managing-packages/", "/en/6/guides/yak/installing-and-managing-packages/", "/en/7/guides/yak/installing-and-managing-packages/", "/en/wip/guides/yak/installing-and-managing-packages/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "Dies ist eine Schritt-für-Schritt-Anleitung zur Installation und Deinstallation eines Yak-Pakets mit Hilfe der CLI."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Installieren und Verwalten von Paketen"
type = "guides"
weight = 30
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

{{< call-out "note" "Anmerkung" >}}
Yak ist plattformübergreifend. Die folgenden Beispiele sind für Windows. Für Mac ersetzen Sie den Pfad zum Yak CLI-Tool durch <code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.
{{< /call-out >}}



## Installation

Die Installation eines yak-Pakets mit dem CLI-Tool ist einfach.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" install marmoset

Downloading marmoset (1.0.0)...
Downloaded marmoset (1.0.0)
Installing marmoset (1.0.0)...
Successfully installed marmoset (1.0.0)
```

{{< call-out "note" "Anmerkung" >}}
Rhino wird beim nächsten Start die neuen Pakete laden.
{{< /call-out >}}

Sie können Yak auch bitten, eine bestimmte Version zu installieren.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" install marmoset 1.0.0

...
```

Das Paket wird in einem speziellen Ordner installiert, ähnlich dem Ordner Grasshopper Libraries, aber mit einer von einer Yak kontrollierten Ordner- bzw. Dateistruktur.


## Deinstallieren

Pakete können auch einfach mit dem Yak CLI Tool deinstalliert werden.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" uninstall marmoset

marmoset successfully uninstalled
```

{{< call-out "note" "Anmerkung" >}}
Rhino wird registrieren, dass das Paket deinstalliert wurde,
wenn es das nächste Mal startet.
{{< /call-out >}}


## Liste

Sie können jederzeit überprüfen, welche Pakete gerade installiert sind.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" list

marmoset (1.0.0)
```

## Verwandte Themen

- [Yak-Anleitungen und Tutorials](/guides/yak/)
- [Erstellen eines Grasshopper-Plug-in-Pakets](/guides/yak/creating-a-grasshopper-plugin-package/)
- [Erstellen eines Rhino-Plug-in-Pakets](/guides/yak/creating-a-rhino-plugin-package/)

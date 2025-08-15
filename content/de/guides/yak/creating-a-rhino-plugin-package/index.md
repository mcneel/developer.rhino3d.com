+++
aliases = ["/en/5/guides/yak/creating-a-rhino-plugin-package/", "/en/6/guides/yak/creating-a-rhino-plugin-package/", "/en/7/guides/yak/creating-a-rhino-plugin-package/", "/en/wip/guides/yak/creating-a-rhino-plugin-package/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "Dies ist eine Schritt-für-Schritt-Anleitung zur Erstellung eines Pakets für ein Grasshopper-Plug-in (.rhp)."
keywords = [ "developer", "yak", "c", "C/C++", "plugin", "installer" ]
sdk = [ "Yak", "C/C++"]
title = "Erstellen eines Rhino-Plug-in-Pakets"
type = "guides"
weight = 10
override_last_modified = "2021-02-04T18:27:17Z"

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

Der [Paketmanager](/guides/yak/) wurde in Rhino 7 eingeführt. Er erleichtert das Entdecken, Installieren und Verwalten von Rhino-Plug-ins aus Rhino heraus. Diese Anleitung beschreibt, wie man ein Paket aus einem Rhino-Plug-in erstellt, das auf dem Paketserver veröffentlicht werden kann.

{{< call-out "note" "Anmerkung" >}}
Der Paketmanager ist plattformübergreifend. Die folgenden Beispiele sind für Windows.
Für Mac ersetzen Sie den Pfad zum Yak CLI-Tool durch
<code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.
{{< /call-out >}}



Nehmen wir zunächst an, dass Sie einen Ordner auf Ihrem Computer haben, in dem alle
Dateien enthalten sind, die Sie in Ihrem Paket verteilen möchten. Etwa so...

```commandline
C:\Benutzer\Bozo\dist
├── Tamarin.rhp
├── icon.png
└── misc\
    ├── README.md
    └── LICENSE.txt
```

{{< call-out "note" "Anmerkung" >}}
Dies ist nur ein Beispiel. Die einzigen Dateien, die von Bedeutung sind, sind Tamarin.rhp und icon.png (auf das Symbol werden wir später in der Datei manifest.yml verweisen).
{{< /call-out >}}

Wir werden das Yak CLI Tool verwenden, um das Paket zu erstellen, öffnen Sie also eine
Befehls-Eingabeaufforderung und navigieren Sie zu dem oben genannten Verzeichnis.

```commandline
> cd C:\Benutzer\Bozo\dist
```

Jetzt brauchen wir eine Datei `manifest.yml`! Sie können leicht Ihre eigene erstellen, indem Sie
den [Leitfaden der Manifest-Referenzen](../the-package-manifest) studieren. Alternativ können Sie den Befehl `spec` verwenden
um eine Skelettdatei zu erzeugen. Wir werden hier Letzteres tun.

```commandline
> "C:\Programne\Rhino {{< latest-rhino-version >}}\System\Yak.exe" spec

Inspecting content: Tamarin.rhp

---
name: tamarin
version: 1.0.0
authors:
- Park Ranger
description: An example RhinoCommon plug-in
url: https://example.com


Saved to C:\Benutzer\Bozo\dist\manifest.yml
```

Der Befehl `spec` sieht sich das aktuelle Verzeichnis an und wird, falls vorhanden, nützliche Informationen aus der Baugruppe `.rhp` zu gewinnen versuchen und daraus eine mit Name, Version, Beschreibung usw. vorausgefüllte `manifest.yml` erstellen. Wenn Sie diese Informationen noch nicht hinzugefügt haben, werden Platzhalter verwendet.

Der RhinoCommon-Plug-in-Inspektor extrahiert die Baugruppenattribute, die Sie bei der Erstellung Ihres Plug-ins festgelegt haben. Das Attribut `AssemblyInformationalVersion` wird verwendet, um das Versionsfeld zu füllen, da dieses Attribut nicht an die vierstellige Versionsspezifikation von Microsoft gebunden ist und eine SemVer-kompatible Versionszeichenkette enthalten kann. Attribut `AssemblyVersion` wird als Ersatz verwendet.

{{< call-out "note" "Anmerkung" >}}
Der Befehl `spec` ist nützlich, um zu Beginn die Datei manifest.yml zu erstellen. Wenn Sie eine haben, bewahren Sie sie zusammen mit Ihrem Projekt auf und aktualisieren Sie sie für jede Veröffentlichung.
{{< /call-out >}}

Als nächstes öffnen Sie die Manifestdatei mit Ihrem [bevorzugten Editor](https://code.visualstudio.com) und füllen Sie die Lücken aus.

Danach sollten Sie etwas haben, das in etwa so aussieht...

```yaml
---
name: tamarin
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
icon: icon.png
keywords:
- something
```

Jetzt, da wir eine Manifestdatei haben, können wir das Paket erstellen!

```commandline
> "C:\Programme\Rhino {{< latest-rhino-version >}}\System\Yak.exe" build

Building package from contents of C:\Benutzer\Bozo\dist

Found manifest.yml for package: tamarin (1.0.0)
Inspecting content: Tamarin.rhp
Creating tamarin-1.0.0-rh6_18-any.yak

---
name: tamarin
version: 1.0.0
authors:
- Will Pearson
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
keywords:
- something
- guid:c9beedb9-07ec-4974-a0a2-44670ddb17e4

C:\Benutzer\Bozo\dist\tamarin-1.0.0-rh6_18-any.yak
├── Tamarin.dll
├── Tamarin.rhp
├── manifest.yml
└── misc/
    ├── LICENSE.txt
    └── README.md
```

{{< call-out "note" "Anmerkung" >}}
Der Dateiname enthält ein <a href="../the-anatomy-of-a-package#distributions" class="alert-link">"Distribution Tag"</a> (in diesem Fall<code>rh6_18-any</code>). Der erste Teil, <code>rh6_18</code>, wird von der Version von Rhinocommon.dll oder Rhino C++ SDK abgeleitet, die im Plug-in-Projekt referenziert wird. Der zweite Teil, <code>any</code>, bezieht sich auf die Plattform, für die das Plug-in bestimmt ist. Um ein plattformspezifisches Paket zu erstellen, führen Sie den Befehl build erneut mit dem Argument <code>&#45;&#45;platform &lt;platform&gt;</code> aus, wobei <code>&lt;platform&gt;</code> entweder <code>win</code> oder <code>mac</code> sein kann.
{{< /call-out >}}

{{< call-out "warning" "Wichtig" >}}
Wenn Sie derzeit ein Paket mit einem <code>rh6*</code> Distribution Tag veröffentlichen, ist es nicht für Rhino 7 installierbar. Wenn Ihr Plug-in auch in Rhino 7 funktioniert, markieren Sie es bitte als kompatibel, indem Sie die .yak-Datei kopieren, den Teil des Dateinamens im Distribution Tag aktualisieren (also <code>rh6_18</code> ➡ <code>rh7_0</code>) und <a href="../pushing-a-package-to-the-server" class="alert-link">beides auf den Paketserver pushen</a>.
{{< /call-out >}}

{{< call-out "note" "Anmerkung" >}}
Vielleicht bemerken Sie, dass sich der GUID Ihres Plug-ins in den Schlüsselwörtern versteckt hält. Weitere Informationen darüber, wie dies verwendet wird, finden Sie im Leitfaden <a href="../package-restore-in-grasshopper" class="alert-link">"Paketwiederherstellung in Grasshopper"</a>.
{{< /call-out >}}

Herzlichen Glückwunsch! 🙌 Sie haben gerade ein Paket für Ihr Grasshopper-Plug-in erstellt.

## Weitere Schritte:

Nachdem Sie nun ein Paket erstellt haben, [pushen Sie es auf den Paketserver](../pushing-a-package-to-the-server), damit es im Paketmanager verfügbar ist!

## Verwandte Themen

- [Erstellen eines Grasshopper-Plug-in-Pakets](/guides/yak/creating-a-grasshopper-plugin-package/)
- [RhinoCommon: Ihr erstes Plug-in (Windows)](/guides/rhinocommon/your-first-plugin-windows)
- [RhinoCommon: Ihr erstes Plug-in (Mac)](/guides/rhinocommon/your-first-plugin-mac)
- [Ihr erstes C/C++-Plug-in für Rhino erstellen](/guides/cpp/your-first-plugin-windows/)

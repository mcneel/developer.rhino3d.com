+++
aliases = ["/en/5/guides/rhinomobile/what-is-rhinomobile/", "/en/6/guides/rhinomobile/what-is-rhinomobile/", "/en/7/guides/rhinomobile/what-is-rhinomobile/", "/en/wip/guides/rhinomobile/what-is-rhinomobile/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "Diese Anleitung verschafft einen Überblick über RhinoMobile."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Was ist RhinoMobile?"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac" ]
since = 5
until = 7

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true

[_build]
list = "never"
+++

{{< call-out "warning" "RhinoMobile: Veraltet" >}}
RhinoMobile wird nicht mehr unterstützt. Rhino 3dm File I/O ist weiterhin auf iOS und Android über die [rhino3dm-Bibliothek](https://github.com/mcneel/rhino3dm) verfügbar.
{{< /call-out >}}
 
{{< image url="/images/rhinomobile-overview-01.png" alt="/images/rhinomobile-overview-01.png" class="float_right" width="325" >}}

RhinoMobile ist eine C#-.NET-Bibliothek zur Entwicklung von mobilen, plattformunabhängigen 3D-Anwendungen. RhinoMobile basiert - wie RhinoCommon - auf dem Xamarin Mono-Framework, einer voll funktionsfähigen .NET-Laufzeitumgebung, die auf Android, iOS und macOS funktioniert. RhinoMobile verwendet openNURBS (die 3dm-NURBS-Bibliothek) und RhinoCommon (das .NET SDK für Rhinoceros und Grasshopper) und funktioniert mit Datei-IO, Gestenerkennung und 3D-Anzeige (OpenGL ES 2.0). Es handelt sich nicht um die Gesamtheit von RhinoCommon, sondern um eine Untergruppe.

## Wer sollte es nutzen?

Alle, die sich für die Entwicklung allgemein bzw. die von Prototypen interessieren oder einfach nur mit der mobilen 3D-Entwicklung experimentieren möchten. Es gibt zwar viele gute 3D-Bibliotheken für Handyspiele, aber keine ist auf 3D-Modellierung und -Design ausgerichtet. RhinoMobile versucht, diese Lücke zu schließen. Wenn Sie in C# entwickeln und so viele Geräte wie möglich adressieren möchten, ist dies die richtige Bibliothek für Sie. Sie müssen keine Erfahrung mit mobiler Entwicklung vorweisen...nur mit C# und .NET vertraut sein.

## Wo erhalte ich Hilfe?
{{< div class="clear_both" />}}
Besuchen Sie das [Rhino-Forum](http://discourse.mcneel.com/), stellen Sie Ihre Frage in der [Kategorie Rhino-Entwickler](http://discourse.mcneel.com/c/rhino-developer) und erwähnen Sie den Entwickler @dan.

## Downloads und Links

### Entwickler-Tools

- [Xamarin-Plattform](http://xamarin.com/download). Die Verwendung von RhinoMobile erfordert eine 30-tägige kostenlose Testversion der Business Edition. - Xamarin hat reduzierte Preise für Akademiker.
- [Xcode](http://developer.apple.com/xcode/) auf einem Mac mit OS X 10.8 (Mountain Lion) oder neuer zum Erstellen von iOS-Apps.
- [Visual Studio 2012](http://https//www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx), oder noch besser: nur Nicht-Express-Editionen (für die Erweiterungen von Xamarin sind kostenpflichtige Versionen erforderlich).
- [Intel Hardware Accelerated Execution Manager](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/) bietet Hardware-Beschleunigung für Android-Emulatoren.

### Bibliotheken und Beispiele

- [RhinoCommon (rhino3dmio-Zweig)](https://github.com/mcneel/rhinocommon/tree/rhino3dmio): Das .NET-Plug-in-SDK für Rhino und Grasshopper.
- [openNURBS](http://www.rhino3d.com/opennurbs)-Download: C++ openNURBS SDK
- [RhinoMobile](http://github.com/mcneel/RhinoMobile) Laden Sie die RhinoMobile-Bibliothek herunter oder klonen Sie sie.
- [RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples) Laden Sie einige Beispielprojekte, die RhinoMobile verwenden, herunter, oder klonen Sie sie.

## FAQ

**Ist RhinoMobile kostenlos?**

Ja.

**Kann ich die von mir mit RhinoMobile entwickelten Anwendungen verkaufen?**

Ja.

**Werden mit RhinoMobile erstellte Anwendungen sowohl auf Mac- und Windows-Computern als auch auf mobilen Geräten funktionieren?**

Nein, mit einem Vorbehalt: Obwohl wir es noch nicht in die Bibliothek aufgenommen haben, planen wir, Windows Phone zu unterstützen, das DirectX als Anzeigepipeline verwendet und (mit einigen Einschränkungen) als "Windows Store App" (alias: Metro UI-App) ausgeführt werden kann.

**Verwendet McNeel RhinoMobile zur Entwicklung von iRhino 3D?**

Selbstverständlich.

**Und ist das alles von RhinoCommon?**

Nein. RhinoMobile verwendet eine Untergruppe von RhinoCommon (rhino3dmio), deren Grenzen durch folgendes Symbol definiert sind: MOBILE_BUILD. Dort gibt es eine ganze Menge: Rhino.DocObjects, Rhino.Geometry, Rhino.FileIO...so ziemlich alles, was Sie zum Lesen, Schreiben und Zeichnen von Rhino 3dm benötigen.

**Ich kann also wahrscheinlich keine Polygonnetze erzeugen bzw. nicht den Befehl 2DZeichnung ausführen?**

Derzeit leider noch nicht. In Anbetracht der CPU-Beschränkungen mobiler Plattformen würden Sie damit wahrscheinlich ohnehin Ihre gesamte Akkulaufzeit aufbrauchen.

## Weitere Schritte:

Wenn Sie bereit sind, mit RhinoMobile zu beginnen, vergewissern Sie sich zunächst, dass Sie alle Werkzeuge installiert haben.  Lesen Sie:

- [Installation von Werkzeugen (Mac)](/guides/rhinomobile/installing-tools-mac/); oder
- [Installation von Werkzeugen (Windows)](/guides/rhinomobile/installing-tools-windows/)

## Verwandte Themen

- [Was ist RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon/)
- [Installation von Werkzeugen (Mac)](/guides/rhinomobile/installing-tools-mac/)
- [Installation von Werkzeugen (Windows)](/guides/rhinomobile/installing-tools-windows/)

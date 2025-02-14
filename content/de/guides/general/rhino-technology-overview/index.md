+++
aliases = ["/en/5/guides/general/rhino-technology-overview/", "/en/6/guides/general/rhino-technology-overview/", "/en/7/guides/general/rhino-technology-overview/", "/en/wip/guides/general/rhino-technology-overview/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "Eine Zusammenfassung der Rhino-Technologiearchitektur."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Rhino-Technologie in der Übersicht"
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


## Übersicht

Rhinoceros besteht aus einer Vielzahl von - in vielen Sprachen geschriebenen - Ebenen, die alle übereinander gestapelt sind.  Die grundlegendsten befinden sich zuunterst, aber die Top-Ebenen sollten keinesfalls als oberflächlich gelten...

![The Rhino Stack](/images/rhino-technology-overview-01.png)

Sprechen wir stattdessen über jede einzelne Ebene, angefangen bei der untersten, nämlich...

## Foundation

### C++ Rhino Core

Der C++-Kern von Rhino ist der älteste und umfangreichste Codesatz.  Wir verwenden teilweise Microsofts MFC, auch im SDK.  Hier wird das Laufzeitdokument verwaltet, hier befindet sich der gesamte OpenGL-Zeichencode für das Ansichtsfenster, und hier befindet sich der von unseren Mathematikern geschriebene Code für die Berechnungsgeometrie.  Viele der Rhino-Befehle sind hier zu finden.

Ein Großteil der Bedienoberfläche - die Befehlszeile, das Anwendungs-Grundgerüst, die Statusleiste und die Dialogfenster für viele Befehle im Rhino-Kern.

### openNURBS

openNURBS ist ein kostenloser C++-Quellcode, mit dem Sie Rhino *3dm* -Dateien lesen und schreiben können - bis zurück zur Version 1.  openNURBS war unser erstes Open-Source-Projekt.

Der Code lässt sich auf Windows, macOS, Linux, iOS und Android kompilieren.  Er wird in verschiedenen Anwendungen von Drittanbietern wie ArchiCAD, SolidWorks, Inventor, SketchUp und vielen anderen Produkten verwendet, um *3dm* -Dateien direkt zu lesen oder zu schreiben.

openNURBS ist das, was Rhino nativ zum Lesen/Schreiben von *3dm* -Dateien verwendet.  Dieses Toolkit wird vor Rhino veröffentlicht, so dass alle Produkte, einschließlich der unserer Konkurrenten, mit den neuesten *3dm* -Dateien kompatibel sein können.  Es gibt keinen Unterschied zwischen den *3dm* -Dateien, die Rhino schreibt, und denen anderer Anwendungen, die openNURBS zum Lesen und Schreiben von *3dm* verwenden.

Weitere Informationen über openNURBS finden Sie in den [openNURBS-Anleitungen](/guides/opennurbs/).

### C++ SDK

Hinzu kommt unser C++-SDK, das nur in Windows verfügbar ist.

Die Kompilierung mit dem C++ SDK erfordert eine bestimmte Version von Microsoft Visual Studio und Microsoft C-Runtime.  Sie müssen für jede Hauptversion von Rhino neu kompilieren.

Praktisch alles, was Rhino tun kann, wird durch das C++ SDK dargestellt. Einige Befehle und Funktionen wurden noch nicht dargestellt, aber dieses SDK ist sehr umfangreich und reichhaltig.

Da es so eng an den Rhino-Kern gekoppelt ist, müssen Plug-in-Entwickler ihre Plug-ins leider für jede Rhino-Version neu kompilieren.

Weitere Informationen über das C++ SDK finden Sie in den [C/C++ Anleitungen](/guides/cpp/).

## C++ Stapel

In der rechten Spalte des obigen Stapeldiagramms befindet sich der C++ Anteil von Rhino.  Der C++ Stapel ermöglicht es uns - und auch unabhängigen Plug-in-Entwicklern - Rhino-Plug-ins mit demselben C++ SDK zu schreiben, das wir auch für die Entwicklung von Rhino selbst verwenden.  Beachten Sie, dass Sie Grasshopper-Komponenten nicht mit C++ erstellen können.

### #### C++ Plug-ins

Zusätzlich zum C++ SDK gibt es C++ Plug-ins.  Viele in Rhino enthaltene Funktionen, einschließlich einiger Befehle, Datei-E/A und Renderer, sind eigentlich C++-Plug-ins.  Außerdem gibt es Dutzende von C++ Plug-ins von Drittanbietern, wie [VisualARQ von Asuni](http://www.visualarq.com/), [RhinoCAM von MecSoft](https://mecsoft.com/rhinocam-software/) und [V-Ray von Chaos Software](https://www.chaosgroup.com/vray/rhino).

Weitere Informationen über das C++ SDK finden Sie in den [C/C++ Anleitungen](/guides/cpp/).

### RhinoScript

Eines der C++-Plugins, die wir mit Rhino liefern, ist [RhinoScript](/guides/rhinoscript/what-are-vbscript-rhinoscript/).  RhinoScript stellt eine nützliche Teilmenge des Rhino-SDKs über VBScript zur Verfügung - eine weit verbreitete und beliebte Skriptsprache.  RhinoScript ermöglicht Ihnen nicht nur den Zugriff auf Rhino, sondern auch auf jedes andere COM-Objekt in Windows.

Weitere Informationen finden Sie in den [RhinoScript-Anleitungen](/guides/rhinoscript/), insbesondere in [Was sind VBScript und RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript/).

## .NET-Stapel

Das .NET SDK wird hier in drei Schichten dargestellt:

- C API
- .NET-Rahmenwerk
- RhinoCommon
- Eto

### C API

Eine reine C API wrappt das C++ SDK und ermöglicht es uns, Platform Invoke (P/Invoke) in das C++-SDK einzubinden und so eine Brücke zwischen dem nativen C++-Code und den verwalteten .NET-Ebenen zu bilden.

### .NET Framework

Microsoft entwickelt das [.NET Framework](https://www.microsoft.com/net/framework).  NET ermöglicht es, Plugins in C#, F#, VB.NET und jeder anderen Sprache zu schreiben, die sich mit Microsofts IL kompilieren lässt.

Das Microsoft .NET-Framework ist im Lieferumfang von Windows enthalten.

In Rhino für Mac betten wir die [Mono Runtime](https://www.mono-project.com) ein, eine teilweise plattformübergreifende Implementierung der .NET Runtime.

Für weitere Informationen über .NET und wie es sich auf die Rhino-Entwicklung bezieht, siehe [Was sind Mono und Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/).

### RhinoCommon

RhinoCommon ist unser .NET-SDK für Rhino, das auf den Teilen des .NET-Frameworks aufbaut, die sowohl auf Windows als auch macOS (über Mono) *gebräuchlich* sind.  RhinoCommon ermöglicht es Entwicklern, .NET-Code sowohl auf Rhino für Windows als auch auf Rhino für Mac auszuführen.

Weitere Informationen über RhinoCommon finden Sie in den [RhinoCommon-Anleitungen](/guides/rhinocommon/), oder genauer gesagt in [Was ist RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon).

### Eto

Mit RhinoCommon können Sie .NET-Plug-ins schreiben, die auf Windows und Mac funktionieren... mit Ausnahme der Benutzeroberfläche.  Das Mono-Team hat weder WinForms noch WPF geklont, so dass keine dieser Technologien auf dem Mac funktioniert.  Um dieses Problem zu lösen, wird Rhino jetzt mit Eto.Forms geliefert.  Mit Eto können Sie die Benutzeroberfläche einmal in C#, XAML oder JSON schreiben und auf Windows und macOS verwenden.  Tatsächlich kann Ihre in Eto geschriebene Benutzeroberfläche auch auf iOS, Android und Linux laufen.

Weitere Informationen über Eto finden Sie unter [Eto.Forms auf GitHub](https://github.com/picoe/Eto).

### .NET-Plug-ins

Auf RhinoCommon bauen zahlreiche Plug-ins auf, sowohl interne als auch von Dritten entwickelte Plug-ins.  [Grasshopper](http://www.grasshopper3d.com/), zum Beispiel, ist ein RhinoCommon-Plug-in.  Einige Befehle, Renderer und Datei-IO-Plug-ins in Rhino sind eigentlich als RhinoCommon-Plug-ins geschrieben.  Im Laufe der Zeit verschieben wir mehr und mehr praktische Funktionen in RhinoCommon/.NET-Plug-ins, um mehr Code über die Plattformen hinweg zu teilen.  Viele erfolgreiche Plug-ins von Drittanbietern wurden ebenfalls mit RhinoCommon und .NET geschrieben, wie [RhinoGold](http://www.tdmsolutions.com/) und [Matrix von GEMVision](http://www.stuller.com/matrix) und [Orca3D](http://orca3d.com/).

Weitere Informationen über RhinoCommon finden Sie in den [RhinoCommon-Anleitungen](/guides/rhinocommon/).

### Grasshopper Components

Rhino wird jetzt mit Grasshopper geliefert, unserer visuellen Programmiersprache für algorithmisches und parametrisches Design.  Grasshopper ist eine eigenständige Entwicklungsplattform mit [Hunderten von Grasshopper-Komponenten von Drittanbietern](http://www.food4rhino.com/grasshopper-addons), mit denen sich alle möglichen Dinge tun lassen, von [Physiksimulationen](http://www.food4rhino.com/project/kangaroo) über [Benutzeroberflächen](http://www.food4rhino.com/project/human-ui) bis hin zur [Industrieroboterprogrammierung und -steuerung](http://www.food4rhino.com/project/hal).

Weitere Informationen über Grasshopper, insbesondere über die Entwicklung von Grasshopper-Komponenten, finden Sie in den [Grasshopper-Anleitungen](/guides/grasshopper/).

### Python-Scripting

Eines der .NET-Plugins, die wir mit Rhino liefern, ist RhinoPython.  Geschrieben mit [IronPython](http://ironpython.net/), einer .NET-Implementierung der [Python](https://www.python.org/) -Laufzeitumgebung, stellt RhinoPython das gesamte RhinoCommon-SDK der Python-Skriptsprache zur Verfügung.  Das bedeutet, dass jedes Mal, wenn wir eine Funktion zu RhinoCommon hinzufügen, diese automatisch in RhinoPython auftaucht.

Weitere Informationen über RhinoPython finden Sie in den [RhinoPython-Anleitungen](/guides/rhinopython/).

## Verwandte Themen

- [C/C++ Anleitungen](/guides/cpp/)
- [openNURBS-Führer](/guides/opennurbs/)
- [RhinoScript-Anleitungen](/guides/rhinoscript/)
- [Microsoft .NET Framework (auf microsoft.com)](https://www.microsoft.com/net/framework)
- [Was ist RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon)
- [RhinoCommon-Anleitungen](/guides/rhinocommon/)
- [Was sind Mono und Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Mono-Projekt](https://www.mono-project.com)
- [Eto.Forms auf GitHub](https://github.com/picoe/Eto)
- [Grasshopper-Anleitungen](/guides/grasshopper/)
- [RhinoPython-Anleitungen](/guides/rhinopython/)

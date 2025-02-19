+++
aliases = ["/en/5/guides/general/frequently-asked-questions/", "/en/6/guides/general/frequently-asked-questions/", "/en/7/guides/general/frequently-asked-questions/", "/en/wip/guides/general/frequently-asked-questions/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "Dieser Leitfaden ist eine Liste häufig gestellter Fragen (FAQ)."
keywords = [ "developer", "rhino", "faq" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Häufig gestellte Fragen"
type = "guides"
weight = 4
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptspage"
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


**Welches SDK ist das richtige für mich?**

Das hängt ganz davon ab, was Sie tun wollen.  Wenn es Ihre Absicht ist, repetitive Aufgaben in Rhino zu automatisieren, ist das Schreiben eines [Python](/guides/#rhinopython)-Skripts der richtige Weg.  Wenn Sie beabsichtigen, ein vollwertiges Plug-in oder Grasshopper-Komponente zu schreiben, empfehlen wir Ihnen dringend [RhinoCommon SDK](/guides/rhinocommon/what-is-rhinocommon/).  Wenn Sie sehr kompetent in C/C++ sind, sollten Sie die native C/C++ SDK in Betracht ziehen (wird nur in Rhino für Windows unterstützt).

**Kann ich Plug-ins schreiben, die sowohl auf Windows als auch Mac ausführbar sind?**

Ja ...sogar unter Verwendung [des gleichen Codes](/guides/rhinocommon/what-is-rhinocommon/).

**Was ist Mono/Xamarin?**

Mono ist eine Open-Source-Version von Microsofts .NET-Laufzeit, die auf Linux, macOS, iOS und Android ausgeführt wird.  Werfen Sie einen Blick in den Leitfaden [Was sind Mono und Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/) um mehr zu erfahren.

**Was sind Makros?**
Makros sind Zeichenketten von Rhino-Befehlen und Befehlsoptionen, die Ihnen die Erzeugung einer automatisierten Sequenz von Vorgängen ermöglichen.  Dieses Makro (Sequenz) kann dann durch Betätigung einer Werkzeugleistenschaltfläche oder durch Eingabe eines Verweises wiederholt werden.

**Was sind Skripts?**
Für komplexere Aufgaben sind Makros ungenügend.  Sie sind weder zur Ausführung komplexer Berechnungen imstande noch zum Speichern und Erhalten von Daten, dem Analysieren der Daten und Treffen von Bedingungsentscheidungen, oder um tief in die inneren Funktionsweisen von Rhino vorzudringen.  Hierfür benötigt man ein wirkliches Programmierungswerkzeug.  Das einfachste und am leichtesten zugängliche ist Python, das ebenso seine Version der RhinoScript-Syntax enthält.  Wenn von Skripten die Rede ist, nehmen wir normalerweise auf Funktionen Bezug, die mit RhinoScript oder Python geschrieben wurden.

**Was sind Plug-ins?**
Plug-ins sind noch durchdachtere Werkzeuge: hierbei handelt es sich um kompilierte Computerprogramme, die in Rhino integriert werden können.  Sie können von einfachen, skriptähnlichen Funktionen bis zu komplexen, voll ausgearbeitten Programmen für Rendering, Animation, Bearbeitung usw. reichen.

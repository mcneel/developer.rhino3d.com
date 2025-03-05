+++
aliases = ["/en/5/guides/general/rhino-developer-prerequisites/", "/en/6/guides/general/rhino-developer-prerequisites/", "/en/7/guides/general/rhino-developer-prerequisites/", "/en/wip/guides/general/rhino-developer-prerequisites/"]
authors = [ "dan", "callum" ]
categories = [ "Getting Started" ]
description = "Dieser Leitfaden beschreibt die wichtigsten Anforderungen, um für Rhino zu entwickeln."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Voraussetzungen für Entwickler"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/learningresources"
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


Es gibt eine Reihe von Voraussetzungen, um an der Entwicklung von Rhino mitarbeiten zu können.  Diese lassen sich grob in drei Kategorien einteilen, die aufsteigend nach Schwierigkeitsgrad geordnet sind:

1. [Hardware-Voraussetzungen](#hardware)
1. [Software-Voraussetzungen](#software)
1. [Programmierkenntnisse](#programming-knowledge)

## Hardware

Wenn Sie diese Anleitung lesen, haben Sie wahrscheinlich bereits einen Computer, auf dem Rhino läuft. (Falls nicht, hat Rhino einige minimale [Systemanforderungen](http://www.rhino3d.com/system_requirements/), die Sie überprüfen sollten, bevor Sie eine Hardware erwerben).  Im Allgemeinen ist bei einem zur Ausführung von Rhino geeigneten Computer *davon auszugehen*, dass er auch für die im Abschnitt [Software](#software) umrissenen Entwickler-Tools tauglich ist.

Wenn Sie ein Windows-Benutzer sind und Plug-ins für Rhino für Mac entwickeln möchten, benötigen Sie einen Apple Mac Computer.  Wenn Sie hingegen ein macOS-Benutzer sind und für Rhino für Windows entwickeln möchten, benötigen Sie einen Computer, auf dem Rhino für Windows ausgeführt werden kann (virtuelle Maschinen, auf denen Windows unter macOS ausgeführt wird, können jedoch sehr gut funktionieren).


## Software

Je nachdem, was Sie tun möchten, sind die Softwarevoraussetzungen unterschiedlich.  Im Allgemeinen benötigen Sie jedoch Folgendes:

- [Rhinoceros](http://www.rhino3d.com/download)
- Einen Code-Editor.  Es gibt viele Möglichkeiten... hier sind einige:
   - [Visual Studio für Windows](https://www.visualstudio.com): Microsofts repräsentative Integrierte Entwicklungsumgebung IDE (Integrated Developer Environment) für Windows.
   - [Visual Studio Code](https://code.visualstudio.com/): Der beste kostenlose plattformübergreifende Editor

Siehe den [SDK-spezifischen Leitfaden](/guides/) für die Software-Voraussetzungen... normalerweise in den *"Installing Tools"* Anleitungen zu finden.

## Programmierkenntnisse

Der Erwerb von Programmierkenntnissen ist die arbeitsintensivste Voraussetzung.  Programmieren zu lernen - oder auch eine neue Sprache auszuprobieren - macht in jedem Fall Spaß und ist eine Bereicherung.  Unter Verwendung von Rhino programmieren zu lernen ist ein sehr guter Anfang...

### C# .NET lernen

Wenn Sie Plug-ins mit RhinoCommon schreiben möchten, müssen Sie eine .NET-kompatible Programmiersprache wie C# (oder VB) verstehen.  Wir empfehlen [C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)) (C Sharp), weil es modern, sicher und leicht zu erlernen ist - und Sie können in C# sowohl auf Windows als auch auf macOS entwickeln.

*Ansehen*...

- [Beginning C# Programming](http://shop.oreilly.com/product/0636920036036.do) Von Eric Lippert - Veröffentlicht von O'Reilly Media
- [C# Fundamentals for Absolute Beginners](https://www.microsoftvirtualacademy.com/en-US/training-courses/c-fundamentals-for-absolute-beginners-16169) auf Microsofts Virtual Academy
- [C# Essential Training](http://www.lynda.com/C-tutorials/C-Essential-Training/188207-2.html) mit David Gassner auf Lynda.com

*Lesen*...

- [Programming C# 5.0](http://shop.oreilly.com/product/0636920024064.do) Von Ian Griffiths - Veröffentlicht von O'Reilly Media
- [C# 5.0 in a Nutshell](http://shop.oreilly.com/product/0636920023951.do) Von Joseph Albahari, Ben Albahari - Veröffentlicht von O'Reilly Media

*Außerdem*...

- [Stöbern Sie in den Beispielen](/samples/#rhinocommon) auf dieser Site
- [Bitten Sie auf Discourse um Hilfe](http://discourse.mcneel.com/c/rhino-developer)

### C/C++ lernen

Um Plug-ins für Rhino mit C/C++ SDK zu schreiben, müssen Sie zunächst die [C++-Programmiersprache](https://en.wikipedia.org/wiki/C%2B%2B) selbst erlernen.  C/C++ wird manchmal als "fortgeschrittene" Programmiersprache angesehen.

*Ansehen*...

- [C++: A General Purpose Language](https://www.microsoftvirtualacademy.com/en-us/training-courses/c-a-general-purpose-language-and-library-jump-start-8251) auf Microsofts Virtual Academy
- [C++ Essential Training](http://www.lynda.com/C-tutorials/C-Essential-Training/182674-2.html) mit Bill Weinmann auf Lynda.com

*Lesen*...

- [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language) von Ian Kernighan und Dennis Ritchie
- [Practical C++ Programming](http://shop.oreilly.com/product/9780596004194.do) von Steve Oualline - Published von O'Reilly Media
- [C++ Primer Plus](http://www.amazon.com/Primer-Plus-Edition-Developers-Library/dp/0321776402) von Stephen Prata

*Außerdem*...

- [Stöbern Sie in den Beispielen](/samples/#cc) auf dieser Site
- [Bitten Sie auf Discourse um Hilfe](http://discourse.mcneel.com/c/rhino-developer)

### Python lernen

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) ist eine fantastische erste Sprache und eine erstaunlich flexible zusätzliche Sprache, um sie in Ihr Toolkit zu integrieren.

*Ansehen*...

- [Google's Python Class](https://developers.google.com/edu/python/) von Google for Education
- [Up and Running with Python](http://www.lynda.com/Python-tutorials/Up-Running-Python/122467-2.html) mit Joe Marini auf Lynda.com


*Lesen*...

- [The Python Tutorial](https://docs.python.org/2/tutorial/index.html)
- [RhinoPython Primer](http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101) von Skylar Tibbits, Arthur van der Harten, Steve Baer und David Rutten
- [The Python Tutorial](https://docs.python.org/2/tutorial/index.html) von der Python Software Foundation
- [Learn Python the Hard Way](http://learnpythonthehardway.org/book/) von Zed A. Shaw - trotz des Titels ist dies ein Buch für Anfänger
- [Automate The Boring Stuff With Python](https://automatetheboringstuff.com/) von Al Sweigart

*Außerdem*...

- [Stöbern Sie in den Beispielen](/samples/#rhinopython) auf dieser Site
- [Bitten Sie auf Discourse um Hilfe](http://discourse.mcneel.com/c/scripting)

### RhinoScript lernen

RhinoScript ist ein Scripting-Werkzeug, das auf Microsofts VBScript basiert.  RhinoScript läuft in Rhino für Windows.

*Lesen*...

- [RhinoScript Primer](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101) von David Rutten
- [Microsoft VBScript User's Guide and Language Reference](https://msdn.microsoft.com/en-us/library/t0aew7h6(VS.85).aspx)

*Außerdem*...

- [Stöbern Sie in den Beispielen](/samples/#rhinoscript) auf dieser Site
- [Bitten Sie auf Discourse um Hilfe](http://discourse.mcneel.com/c/scripting)

### Weiterführendes Lernmaterial

- [Crafting Interpreters](https://craftinginterpreters.com/) von Robert Nystrom
- [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) von Robert C. Martin


## Verwandte Themen

- [Was ist ein Rhino-Plug-in?](/guides/general/what-is-a-rhino-plugin/)
- <a href="https://en.wikipedia.org/wiki/C_Sharp_(programming_language">C Sharp auf Wikipedia</a>
- [C++ auf Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B)
- [Python auf Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))

+++
aliases = ["/en/5/guides/general/what-is-a-rhino-plugin/", "/en/6/guides/general/what-is-a-rhino-plugin/", "/en/7/guides/general/what-is-a-rhino-plugin/", "/en/wip/guides/general/what-is-a-rhino-plugin/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "Dieser Leitfaden beschreibt, was ein Rhino-Plugin ist und welche Formen es davon gibt."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Was ist ein Rhino-Plug-in?"
type = "guides"
weight = 3
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/developer/whatisarhinoplugin"
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


Ein Rhino-Plug-in ist ein Softwaremodul, das die Funktionalität von Rhino oder Grasshopper durch Hinzufügen von Befehlen, Funktionen oder Fähigkeiten erweitert.  Ein Rhino-Plug-in ist eine Dynamic Link Library, oder DLL.

Unter Windows ist ein Rhino-Plugin, das mit dem [C/C++ SDK](/guides/cpp/what-is-the-cpp-sdk/) erstellt wurde, eine reguläre DLL, die die gemeinsame MFC-DLL verwendet.

Unter Windows und Mac ist ein Rhino-Plugin, das mit dem [RhinoCommon SDK](/guides/rhinocommon/what-is-rhinocommon/) erstellt wurde, eine .NET-Assembly.

Beispiele für Rhino-Plug-ins sind [Grasshopper](http://www.grasshopper3d.com), [Brazil](http://brazil.rhino3d.com/), [Flamingo](http://nxt.flamingo3d.com/) und [Bongo](http://bongo.rhino3d.com/).  Siehe [food4rhino.com](http://www.food4rhino.com/) für weitere Informationen.


## Arten von Plug-ins

Rhino unterstützt fünf verschiedene Arten von Plugins:

1. *Allgemeines Dienstprogramm*: Ein Allzweckprogramm, das einen oder mehrere Befehle enthalten kann.
1. *Datei-Import*: Importiert Daten aus anderen Dateiformaten in Rhino; kann mehr als ein Format unterstützen.
1. *Datei-Export*: Exportiert Daten aus Rhino in andere Dateiformate; kann mehr als ein Format unterstützen.
1. *Benutzerdefiniertes Rendering*: Wendet Materialien, Texturen und Lichter auf eine Szene an, um gerenderte Bilder zu erzeugen.
1. *3D-Digitalisierung*: Schnittstellen zu 3D-Digitalisierungsgeräten, wie z. B. die von MicroScribe, Faro und Romer.

***Hinweis***: Die Plug-ins für Datei-Import, Datei-Export, Benutzerdefiniertes Rendering und 3D-Digitalisierung sind allesamt spezielle Erweiterungen des als Allgemeines Dienstprogramm verwendeten Plug-ins.  Somit können alle Plug-in-Arten einen oder mehrere Befehle enthalten.


## Plug-in-Kompatibilität

Damit Rhino Ihr Plug-in erfolgreich laden und ausführen kann, müssen mehrere Bedingungen erfüllt sein:

1. Die "RhinoSdkVersion"-Nummer Ihres Plug-ins muss mit der "RhinoSdkVersion" von Rhino übereinstimmen.
1. Die "RhinoSdkServiceRelease" Nummer von Rhino muss größer oder gleich der "RhinoSdkServiceRelease" Ihres Plug-ins sein.

Wir nehmen gelegentlich Änderungen an unseren SDKs vor.  Wenn wir das tun, ändern wir die "RhinoSdkServiceRelease"-Nummer.  

Als Plug-in-Entwickler ist es unwahrscheinlich, dass Sie mit der ersten Bedingung ein Problem haben werden.  Dies würde z.B. passieren, wenn ein Benutzer versucht, ein für Rhino 6 erstelltes Plug-in in Rhino 4 zu laden.

Gelegentlich kann es jedoch zu Problemen mit der zweiten Bedingung kommen.  Wenn Sie Ihr Plug-in mit dem SDK 6.2 (RhinoSdkVersion.RhinoSdkServiceRelease) kompiliert haben und ein Benutzer mit Rhino 6.1 versucht, es auszuführen, erhält er eine Fehlermeldung und das Plug-in wird nicht geladen.  Wenn Ihr Kunde diese Meldung erhält, muss er die neueste Rhino-Version erhalten (in diesem Beispiel 6.2 oder neuer), und damit sollte das Problem gelöst sein.

## Verwandte Themen

- [Voraussetzungen für Entwickler](/guides/general/rhino-developer-prerequisites)

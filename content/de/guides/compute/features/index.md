+++
aliases = ["/en/5/guides/compute/features/", "/en/6/guides/compute/features/", "/en/7/guides/compute/features/", "/en/wip/guides/compute/features/"]
authors = [ "brian" ]
categories = [ "Getting Started" ]
description = "Rhino SDK-Funktionen über REST API"
keywords = [ "developer", "compute" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Compute: Funktionen"
type = "guides"
weight = 1
override_last_modified = "2020-11-12T13:14:51Z"

[admin]
TODO = "needs editing"
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++


## Compute kann:
  * Grasshopper-Definitionen online in seriellen oder parallelen Lösungen berechnen.
  * Rhino- (3dm-) und andere Dateitypen überall im Netz manipulieren.
  * Mehr als 2400 geometrische Operationen an benutzerdefinierten Objekten aus bestehenden Prozessen online aufrufen. Dazu gehören Punkte, Kurven, Flächen, Netze und Volumenkörper.

## Funktionen von Compute
  * Geometrieberechnungen über eine cloudbasierte zustandslose REST-API durchführen.
  * Zugriff auf [mehr als 2400 RhinoCommon-API-Aufrufe](https://compute.rhino3d.com/sdk) von außerhalb von Rhino.
  * Zugriff auf zusätzliche RhinoCommon-Funktionen, die in [openNURBS](https://www.rhino3d.com/opennurbs) nicht verfügbar sind, einschließlich:
  * Berechnung des nächstliegenden Punkts
  * Berechnungen von Überschneidungen
  * Oberflächentesselierung (Vermaschung)
  * Interpolierung
  * Boolesche Operationen
  * Berechnungen von Flächen- und Masseeigenschaften
  * Sonstige verschiedene Geometrieberechnungen
  * Erweiterbare REST-Methodenaufrufe durch eine gemeinsame Deklaration.
  * Zugriff auf vorhandene Rhino/Grasshopper-Plug-ins über die Online-Schnittstelle.
  * Serialisierung von Operationen in einer Anfrage durch Grasshopper oder Python-Skripte.
  * Client-seitige Bibliotheken zur Verwendung mit eigenständigem C#(.NET), Python und JavaScript.

## Open Source:
Basierend auf der [Rhino Inside™-Technologie](https://www.rhino3d.com/inside), ist compute ein [Open Source Projekt](https://github.com/mcneel/compute.rhino3d).
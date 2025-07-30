+++
aliases = ["/en/5/guides/compute/compute-python-getting-started/", "/en/6/guides/compute/compute-python-getting-started/", "/en/7/guides/compute/compute-python-getting-started/", "/en/wip/guides/compute/compute-python-getting-started/"]
authors = [ "scottd" ]
categories = [ "Getting Started", "Client" ]
description = "Diese Anleitung behandelt alle notwendigen Werkzeuge, die für den Einstieg in den Rhino Compute Service mittels Python erforderlich sind."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "Python" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Aufrufen von Compute mit Python"
type = "guides"
weight = 3
override_last_modified = "2020-11-12T13:14:51Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac", "Unix" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++


Am Ende dieses Leitfadens sollten Sie alle Werkzeuge installiert haben, die für die Verwendung von [Rhino Compute](https://www.rhino3d.com/compute) durch Python notwendig sind.

Hier geht es zu einem [Video-Tutorial von Junichiro Horikawa über die ersten Schritte mit Python](https://youtu.be/XCkRXAEJMhg).


Diese Anleitung setzt voraus, dass Sie Python auf der Plattform installiert haben:

- Python 2.7 - Windows (32 und 64 Bit)
- Python 3.7 - Windows (32 und 64 Bit)
- Python 2.7 - OSX (installiert durch Homebrew)
- Python 3.7 - OSX (installiert durch Homebrew)
- Linux und andere Python-Versionen werden durch Quelldistributionen auf PyPi unterstützt.

## Einrichten eines Compute-Projekts in Python

Es gibt einige clientseitige Tools, die für die Kommunikation mit dem Compute-Server in Python installiert werden müssen. Dazu gehören:

- **rhino3dm.py** -  Dies ist Teil der [Rhino3dm Bibliotheken](https://github.com/mcneel/rhino3dm).  Es ist ein Python-Wrapper für [openNURBS](https://developer.rhino3d.com/guides/opennurbs/), der die Funktionen zum Lesen und Schreiben von Rhino-Geometrieobjekten enthält. Dies ist als Pip-Paket erhältlich.

  `pip install rhino3dm`

- **compute-rhino3d.py** - Hier handelt es sich um ein in Arbeit befindliches Paket, das zum Hinzufügen von Klassen gedacht ist, die in [RhinoCommon](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/), aber nicht über rhino3dm.py verfügbar sind. Compute-rhino3d ruft für diese Funktionen den McNeel Cloud Compute Server auf. Es übernimmt alle Transaktionsautorisierungen und die JSON-Datenkonvertierung.

  `pip install compute-rhino3d`

## Die erste Verwendung von Compute

Ein Beispiel für die Verwendung von Python für den Zugriff auf Compute finden Sie im [makemesh.py-Beispiel](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/py/SampleTkinter)

Bitte beachten Sie, dass die Compute-Python-Aufrufe über das Paket `compute_rhino3d.py` mit einem `_` (Unterstrich) und nicht mit einem `-` (Bindestrich) erfolgen.

# Weitere Schritte:

*Herzlichen Glückwunsch!*  Sie haben die Werkzeuge, um [Rhino Compute Server](https://www.rhino3d.com/compute) zu verwenden.  *Was nun?*

1. Um die transaktionale Natur von Compute zu sehen, lesen Sie **compute.rhino3d.py**.
1. Siehe eine Liste der [2400+ API-Aufrufe](https://compute.rhino3d.com/sdk), die für compute.rhino3d.com verfügbar sind.
1. Laden Sie das [Compute Samples Repo von GitHub](https://github.com/mcneel/compute.rhino3d.samples) herunter.
1. Die Bibliotheken sind noch sehr neu und verändern sich schnell. Probieren Sie sie aus oder beteiligen Sie sich. Stellen Sie Fragen oder teilen Sie Ihre Arbeit im [Compute-Diskussionsforum](https://discourse.mcneel.com/c/serengeti/compute-rhino3d) mit.

---

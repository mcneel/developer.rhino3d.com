+++
aliases = ["/en/5/guides/compute/compute-javascript-getting-started/", "/en/6/guides/compute/compute-javascript-getting-started/", "/en/7/guides/compute/compute-javascript-getting-started/", "/en/wip/guides/compute/compute-javascript-getting-started/"]
authors = [ "scottd" ]
categories = [ "Getting Started", "Client" ]
description = "Diese Anleitung behandelt alle notwendigen Werkzeuge, die für den Einstieg in den Rhino Compute Service über JavaScript erforderlich sind."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "JavaScript" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Aufrufen von Compute mit JavaScript"
type = "guides"
weight = 4
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


Am Ende dieses Leitfadens sollten Sie alle Werkzeuge installiert haben, die für die Verwendung von [Rhino Compute](https://www.rhino3d.com/compute) durch JavaScript notwendig sind.

Die Bibliotheken laufen auf allen gängigen Browsern sowie auf node.js.

## Einrichten eines Compute-Projekts mit JavaScript

Es gibt einige clientseitige Tools, die für die Kommunikation mit dem Compute-Server erforderlich sind und auf die verwiesen werden muss. Dazu gehören:

- **rhino3dm.js** -  Ist Teil des Rhino3dm-Projekts.  Es ist ein Javascript-Wrapper und eine Web-Assembly (WASM) für [openNURBS](https://developer.rhino3d.com/guides/opennurbs/) , die die Funktionen zum Lesen und Schreiben von Rhino-Geometrieobjekten enthält. 

- **compute-rhino3d.js** - Hier handelt es sich um ein in Arbeit befindliches Paket, das zum Hinzufügen von Klassen gedacht ist, die in RhinoCommon, aber nicht über rhino3dm.js verfügbar sind. Compute-rhino3d ruft für diese Funktionen den McNeel Cloud Compute Server auf. Es übernimmt alle Transaktionsautorisierungen und die JSON-Datenkonvertierung.

In einer browserbasierten Anwendung würde "index.html" wie folgt aussehen:

  ```
  <html>
    <head>
    <!-- stuff -->
    </head>
    <body>
        <!-- Import maps polyfill -->
        <!-- Remove this when import maps will be widely supported -->
        <script async src="https://unpkg.com/es-module-shims@1.10.0/dist/es-module-shims.js"></script>

        <script type="importmap">
            {
                "imports": {
                    "rhino3dm":"https://unpkg.com/rhino3dm@8.4.0/rhino3dm.module.min.js",
                    "rhinocompute": "https://www.unpkg.com/compute-rhino3d@0.13.0-beta/compute.rhino3d.module.js"
                }
            }
        </script>

        <script type="module" src="./script.js"></script>
	</body>
</html>
  ```

  Importieren Sie in der Datei script.js die Bibliotheken:
  ```
  // Import libraries

import rhino3dm from 'rhino3dm'
import { RhinoCompute } from 'rhinocompute'

// Load rhino3dm
const rhino = await rhino3dm()
console.log('Loaded rhino3dm.')

// Your code ...

  ```

  Für eine node.js-Anwendung installieren Sie zunächst die Bibliotheken mit npm:

  `npm i rhino3dm compute-rhino3d`

  Verweisen Sie dann in Ihrem Skript auf sie:

  ```
  // Import libraries

  import rhino3dm from 'rhino3dm'
  import RhinoCompute from 'compute-rhino3d'

  // Load rhino3dm
  const rhino = await rhino3dm()
  console.log('Loaded rhino3dm.')

```

## Die erste Verwendung von Compute

Beispiele für die Verwendung von JavaScript für den Zugriff auf Compute finden Sie in der [Javascript Sample repo](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/js) 

# Weitere Schritte:

*Herzlichen Glückwunsch!*  Sie haben die Werkzeuge, um [Rhino Compute Server](https://www.rhino3d.com/compute) zu verwenden.  *Was nun?*

1. Um die transaktionale Natur von Compute zu sehen, lesen Sie [compute.rhino3d.js](https://files.mcneel.com/rhino3dm/js/latest/compute.rhino3d.js).
1. Siehe eine Liste der [2400+ API-Aufrufe](https://compute.rhino3d.com/sdk), die für compute.rhino3d.com verfügbar sind.
1. Laden Sie das [Compute Samples Repo von GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute) herunter.
1. Die Bibliotheken sind noch sehr neu und verändern sich schnell. Probieren Sie sie aus oder beteiligen Sie sich. Stellen Sie Fragen oder teilen Sie Ihre Arbeit im [Compute Discussion Forum](https://discourse.mcneel.com/c/serengeti/compute-rhino3d) mit.


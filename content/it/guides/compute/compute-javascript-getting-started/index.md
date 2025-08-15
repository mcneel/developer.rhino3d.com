+++
aliases = ["/en/5/guides/compute/compute-javascript-getting-started/", "/en/6/guides/compute/compute-javascript-getting-started/", "/en/7/guides/compute/compute-javascript-getting-started/", "/en/wip/guides/compute/compute-javascript-getting-started/"]
authors = [ "scottd" ]
categories = [ "Getting Started", "Client" ]
description = "Questa guida illustra tutti gli strumenti necessari per iniziare a lavorare con Rhino Compute Service attraverso JavaScrip."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "JavaScript" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Chiamare Compute con Javascript"
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


Alla fine di questa guida, dovreste avere installato tutti gli strumenti necessari per utilizzare [Rhino Compute](https://www.rhino3d.com/compute) attraverso JavaScript.

Le librerie funzionano su tutti i principali browser e su node.js.

## Impostazione di un progetto di calcolo con JavaScript

È necessario fare riferimento ad alcuni strumenti del lato client che sono essenziali per comunicare con il server di calcolo. Si includono:

- **rhino3dm.js** -  Fa parte del progetto Rhino3dm.  È un wrapper Javascript e un assembly web (WASM) per [openNURBS](https://developer.rhino3d.com/guides/opennurbs/) che contiene le funzioni per leggere e scrivere gli oggetti geometrici di Rhino. 

- **compute-rhino3d.js** - Questo è un pacchetto in divenire che ha lo scopo di aggiungere classi disponibili in RhinoCommon, ma non disponibili tramite rhino3dm.js. Compute-rhino3d effettua chiamate al server McNeel Cloud Compute per queste funzioni. Gestisce tutte le autorizzazioni alle transazioni e la conversione dei dati JSON.

In un'applicazione basata su browser, `index.html` avrebbe questo aspetto:

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

  In script.js, importare le librerie:
  ```
  // Import libraries

import rhino3dm from 'rhino3dm'
import { RhinoCompute } from 'rhinocompute'

// Load rhino3dm
const rhino = await rhino3dm()
console.log('Loaded rhino3dm.')

// Your code ...

  ```

  Per un'applicazione node.js, installare prima le librerie con npm:

  `npm i rhino3dm compute-rhino3d`

  Quindi fare riferimento ad essi nello script:

  ```
  // Import libraries

  import rhino3dm from 'rhino3dm'
  import RhinoCompute from 'compute-rhino3d'

  // Load rhino3dm
  const rhino = await rhino3dm()
  console.log('Loaded rhino3dm.')

```

## Il primo utilizzo di Compute

Esempi di utilizzo di JavaScript per accedere al calcolo si trovano nel [repository Javascript Sample](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/js). 

# Passi successivi

*Ottimo lavoro!*  Disponi degli strumenti per utilizzare [Rhino Compute server](https://www.rhino3d.com/compute).  *E adesso?*

1. Per vedere la natura transazionale di Compute, consulta [compute.rhino3d.js](https://files.mcneel.com/rhino3dm/js/latest/compute.rhino3d.js).
1. Consulta un elenco di [oltre 2400 chiamate API](https://compute.rhino3d.com/sdk) disponibili per compute.rhino3d.com.
1. Scarica il [repository con esempi di Compute da GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute).
1. Le librerie sono ancora molto nuove e cambiano velocemente. Provale o partecipa! Porgi domande o condividi i tuoi progetti sul [Forum di discussione su Compute](https://discourse.mcneel.com/c/serengeti/compute-rhino3d).


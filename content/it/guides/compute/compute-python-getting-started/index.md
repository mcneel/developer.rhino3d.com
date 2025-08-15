+++
aliases = ["/en/5/guides/compute/compute-python-getting-started/", "/en/6/guides/compute/compute-python-getting-started/", "/en/7/guides/compute/compute-python-getting-started/", "/en/wip/guides/compute/compute-python-getting-started/"]
authors = [ "scottd" ]
categories = [ "Getting Started", "Client" ]
description = "Questa guida illustra tutti gli strumenti necessari per iniziare a lavorare con il servizio Rhino Compute in Python."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "Python" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Chiamare Compute con Python"
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


Alla fine di questa guida, dovresti avere installato tutti gli strumenti necessari per utilizzare [Rhino Compute](https://www.rhino3d.com/compute) attraverso Python.

[Video tutorial introduttivo su Python di Junichiro Horikawa](https://youtu.be/XCkRXAEJMhg)


Questa guida presuppone che sulla piattaforma sia installato Python:

- Python 2.7 - Windows (32 e 64 bit).
- Python 3.7 - Windows (32 e 64 bit).
- Python 2.7 - OSX (installato tramite Homebrew).
- Python 3.7 - OSX (installato tramite Homebrew).
- Linux e altre versioni di Python sono supportate attraverso le distribuzioni sorgenti su PyPi.

## Impostazione di un progetto Compute in Python

È necessario fare riferimento ad alcuni strumenti del lato client che sono essenziali per comunicare con il server Compute. Questi includono:

- **rhino3dm.py** -  Questa è la parte delle [librerie Rhino3dm](https://github.com/mcneel/rhino3dm).  Si tratta di un wrapper di Python per [openNURBS](https://developer.rhino3d.com/guides/opennurbs/) che contiene le funzioni per leggere e scrivere gli oggetti geometrici di Rhino. È disponibile come pacchetto Pip.

  `pip install rhino3dm`

- **compute-rhino3d.py** - Questo è un pacchetto in divenire che ha lo scopo di aggiungere classi disponibili in [RhinoCommon](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/), ma non sono disponibili tramite rhino3dm.py. Compute-rhino3d effettua chiamate al server McNeel Cloud Compute per queste funzioni. Gestisce tutte le autorizzazioni alle transazioni e la conversione dei dati JSON.

  `pip install compute-rhino3d`

## Il primo utilizzo di Compute

Esempi di utilizzo di Python per accedere a Compute si trovano nell’[esempio makemesh.py](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/py/SampleTkinter).

Si noti che le chiamate a compute Python sono effettuate attraverso il pacchetto `compute_rhino3d.py` usando `_`  (trattino basso) e non `-` (trattino).

# Passi successivi

*Ottimo lavoro!*  Disponi degli strumenti per utilizzare [Rhino Compute server](https://www.rhino3d.com/compute).  *E adesso?*

1. Per vedere la natura transazionale di Compute, consulta **compute.rhino3d.py**.
1. Consulta un elenco di [oltre 2400 chiamate API](https://compute.rhino3d.com/sdk) disponibili per compute.rhino3d.com.
1. Scarica il [repository con esempi di Compute da GitHub](https://github.com/mcneel/compute.rhino3d.samples).
1. Le librerie sono ancora molto nuove e cambiano velocemente. Provale o partecipa! Porgi domande o condividi i tuoi progetti sul [Forum di discussione su Compute](https://discourse.mcneel.com/c/serengeti/compute-rhino3d).

---

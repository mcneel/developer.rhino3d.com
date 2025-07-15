+++
aliases = ["/en/5/guides/compute/compute-python-getting-started/", "/en/6/guides/compute/compute-python-getting-started/", "/en/7/guides/compute/compute-python-getting-started/", "/en/wip/guides/compute/compute-python-getting-started/"]
authors = [ "scottd" ]
categories = [ "Getting Started", "Client" ]
description = "Ce guide couvre tous les outils nécessaires pour démarrer avec le service Rhino Compute en utilisant Python."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "Python" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Appeler Compute avec Python"
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


À la fin de ce guide, vous devriez avoir installé tous les outils nécessaires pour utiliser [Rhino Compute](https://www.rhino3d.com/compute) via Python.

Découvrez un [tutoriel vidéo de démarrage de Junichiro Horikawa avec Python](https://youtu.be/XCkRXAEJMhg).


Ce guide suppose que Python est installé sur la plateforme :

- Python 2.7 - Windows (32 et 64 bits)
- Python 3.7 - Windows (32 et 64 bits)
- Python 2.7 - OSX (installé via Homebrew)
- Python 3.7 - OSX (installé via Homebrew)
- Linux et d’autres versions de Python sont prises en charge par les distributions de sources sur PyPi.

## Mise en place d’un projet Compute dans Python

Il est important de citer quelques outils côté client qui sont essentiels pour communiquer avec le serveur Compute. C’est le cas de :

- **rhino3dm.py** -  C’est la partie des bibliothèques [Rhino3dm](https://github.com/mcneel/rhino3dm).  Il s’agit d’un « wrapper » Python pour [OpenNURBS](https://developer.rhino3d.com/guides/opennurbs/) qui contient les fonctions nécessaires à la lecture et à l’écriture des objets de géométrie de Rhino. Il est disponible sous la forme d'un package Pip.

  `pip install rhino3dm`

- **compute-rhino3d.py** - Il s’agit d'un package en cours de développement destiné à ajouter des classes disponibles dans [RhinoCommon](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/), mais pas via rhino3dm.py. Compute-rhino3d appelle ces fonctions dans le serveur McNeel Cloud Compute. Il gère toutes les autorisations de transaction et la conversion des données JSON.

  `pip install compute-rhino3d`

## Première utilisation de Compute

Un exemple illustrant comment utiliser Python pour accéder à Compute est disponible dans [makemesh.py](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/py/SampleTkinter).

Veuillez noter que les appels de Compute via Python sont faits à travers le package `compute_rhino3d.py` en utilisant un `_` (tiret bas) et non un `-` (tiret haut).

# Étapes suivantes

*Félicitations !*  Vous disposez à présent des outils nécessaires pour utiliser le serveur [Rhino Compute](https://www.rhino3d.com/compute).  *Et maintenant ?*

1. Pour voir la nature transactionnelle de Compute, lisez **compute.rhino3d.py**
1. Découvrez une liste de [plus de 2 400 appels API](https://compute.rhino3d.com/sdk) disponibles pour compute.rhino3d.com.
1. Téléchargez le [répertoire d’exemples de Compute sur GitHub](https://github.com/mcneel/compute.rhino3d.samples).
1. Les bibliothèques sont encore très récentes et changent rapidement. Essayez-les ou impliquez-vous. Posez vos questions ou partagez vos travaux sur le [Forum de discussion Compute](https://discourse.mcneel.com/c/serengeti/compute-rhino3d).

---

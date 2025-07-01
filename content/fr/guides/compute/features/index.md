+++
aliases = ["/en/5/guides/compute/features/", "/en/6/guides/compute/features/", "/en/7/guides/compute/features/", "/en/wip/guides/compute/features/"]
authors = [ "brian" ]
categories = [ "Getting Started" ]
description = "Fonctions du SDK Rhino via l’API REST"
keywords = [ "developer", "compute" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Les fonctions de Compute"
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


## Compute peut :
  * Calculer des définitions de Grasshopper en ligne sur des solutions en série ou en parallèle.
  * Manipuler des fichiers de Rhino (3DM) et d’autres formats n’importe où sur Internet.
  * Appeler plus de 2 400 opérations géométriques sur des objets personnalisés à partir de processus en ligne existants. Les objets peuvent être des points, des courbes, des surfaces, des maillages ou des solides.

## Fonctions de Compute
  * Exécution de calculs de géométrie à travers une API REST sans état basée sur le cloud.
  * Accès à [plus de 2 400 appels API RhinoCommon ](https://compute.rhino3d.com/sdk) hors de Rhino.
  * Accès à des fonctions RhinoCommon supplémentaires non disponibles dans [openNURBS](https://www.rhino3d.com/opennurbs), telles que :
  * Calculs par la méthode des points les plus proches
  * Calculs d’intersection
  * Tessellation de surfaces (maillage)
  * Interpolation
  * Opérations booléennes
  * Calculs d’aires et de propriétés de masse
  * Autres calculs de géométrie divers
  * Appels de méthode REST extensibles à travers une déclaration commune.
  * Accès à des modules existants de Rhino/Grasshopper à travers l’interface en ligne.
  * Sérialisation d’opérations en une seule requête à travers des scripts de Grasshopper ou de Python.
  * Bibliothèques axées sur le client à utiliser avec C#(.NET), Python et JavaScript en autonome.

## Open Source
Basé sur la technologie [Rhino Inside™](https://www.rhino3d.com/inside), Compute est un [projet open source](https://github.com/mcneel/compute.rhino3d).
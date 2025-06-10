+++
aliases = ["/en/5/guides/compute/compute-javascript-getting-started/", "/en/6/guides/compute/compute-javascript-getting-started/", "/en/7/guides/compute/compute-javascript-getting-started/", "/en/wip/guides/compute/compute-javascript-getting-started/"]
authors = [ "scottd" ]
categories = [ "Getting Started", "Client" ]
description = "Ce guide couvre tous les outils nécessaires pour démarrer avec le service Rhino Compute sous JavaScript."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "JavaScript" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Appeler Compute avec Javascript"
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


À la fin de ce guide, vous devriez avoir installé tous les outils nécessaires pour utiliser [Rhino Compute](https://www.rhino3d.com/compute) sous JavaScript.

Les bibliothèques fonctionneront sur les principaux navigateurs ainsi que sur node.js.

## Mise en place d’un projet Compute avec JavaScript

Il est important de citer quelques outils côté client qui sont essentiels pour communiquer avec le serveur Compute. C’est le cas de :

- **rhino3dm.js** -  Il fait partie du projet Rhino3dm.  C’est un « wrapper » Javascript et WebAssembly (WASM) pour [openNURBS](https://developer.rhino3d.com/guides/opennurbs/) qui contient les fonctions nécessaires à la lecture et à l’écriture des objets de géométrie de Rhino. 

- **compute-rhino3d.js** - Il s’agit d’un paquet en cours de développement destiné à ajouter des classes disponibles dans RhinoCommon, mais pas accessibles via rhino3dm.js. Compute-rhino3d appelle ces fonctions dans le serveur McNeel Cloud Compute. Il gère toutes les autorisations de transaction et la conversion des données JSON.

Dans une application exécutée dans un navigateur, `index.html` ressemblerait à ceci :

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

  Dans le fichier script.js, importez les bibliothèques :
  ```
  // Import libraries

import rhino3dm from 'rhino3dm'
import { RhinoCompute } from 'rhinocompute'

// Load rhino3dm
const rhino = await rhino3dm()
console.log('Loaded rhino3dm.')

// Votre code...

  ```

  Pour une application node.js, installez d’abord les bibliothèques avec npm :

  `npm i rhino3dm compute-rhino3d`

  Référencez-les ensuite dans votre script :

  ```
  // Import libraries

  import rhino3dm from 'rhino3dm'
  import RhinoCompute from 'compute-rhino3d'

  // Load rhino3dm
  const rhino = await rhino3dm()
  console.log('Loaded rhino3dm.')

```

## Première utilisation de Compute

Des exemples illustrant comment utiliser JavaScript pour accéder à Compute sont disponibles dans le [répertoire d’exemples Javascript](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/js).

# Étapes suivantes

*Félicitations !*  Vous disposez à présent des outils nécessaires pour utiliser le serveur [Rhino Compute](https://www.rhino3d.com/compute).  *Et maintenant ?*

1. Pour voir la nature transactionnelle de Compute, lisez [compute.rhino3d.js](https://files.mcneel.com/rhino3dm/js/latest/compute.rhino3d.js).
1. Découvrez une liste de [plus de 2 400 appels d’API](https://compute.rhino3d.com/sdk) disponibles pour compute.rhino3d.com.
1. Téléchargez le [répertoire d’exemples de Compute sur GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute).
1. Les bibliothèques sont encore très récentes et changent rapidement. Essayez-les ou impliquez-vous. Posez vos questions ou partagez vos travaux sur le [Forum de discussion Compute](https://discourse.mcneel.com/c/serengeti/compute-rhino3d).


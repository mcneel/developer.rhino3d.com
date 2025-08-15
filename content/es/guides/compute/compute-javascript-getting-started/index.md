+++
aliases = ["/en/5/guides/compute/compute-javascript-getting-started/", "/en/6/guides/compute/compute-javascript-getting-started/", "/en/7/guides/compute/compute-javascript-getting-started/", "/en/wip/guides/compute/compute-javascript-getting-started/"]
authors = [ "scottd" ]
categories = [ "Getting Started", "Client" ]
description = "Esta guía muestra todas las herramientas necesarias para empezar a utilizar Rhino Compute Service a través de JavaScript."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "JavaScript" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Llamar a Compute con JavaScript"
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


Al final de esta guía, tendrá todas las herramientas instaladas necesarias para utilizar [Rhino Compute](https://www.rhino3d.com/compute) a través de JavaScript.

Las bibliotecas funcionarán en los principales navegadores, así como en node.js.

## Crear un proyecto de Compute con JavaScript

Hay algunas herramientas del lado del cliente que necesitan ser referenciadas y que son esenciales para comunicarse con el servidor Compute. Entre ellas figuran:

- **rhino3dm.js** -  Forma parte del proyecto Rhino3dm.  Es una wrapper Javascript y un ensamblado web (WASM) para [openNURBS](https://developer.rhino3d.com/guides/opennurbs/) que contiene las funciones para leer y escribir objetos de geometría de Rhino. 

- **compute-rhino3d.js** - Es un paquete en desarrollo para añadir clases disponibles en RhinoCommon, pero no disponibles a través de rhino3dm.js. Compute-rhino3d realiza llamadas al servidor McNeel Cloud Compute para estas funciones. Gestiona todas las autorizaciones de transacciones y la conversión de datos JSON.

En una aplicación basada en navegador `index.html` quedaría así:

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

  En el script.js, importe las bibliotecas:
  ```
  // Importar bibliotecas

import rhino3dm from 'rhino3dm'
import { RhinoCompute } from 'rhinocompute'

// Cargar rhino3dm
const rhino = await rhino3dm()
console.log('Loaded rhino3dm.')

// El código ...

  ```

  Para una aplicación node.js, primero instala las bibliotecas con npm:

  `npm i rhino3dm compute-rhino3d`

  Luego referéncielos en el script:

  ```
  // Importar bibliotecas

  import rhino3dm from 'rhino3dm'
  import RhinoCompute from 'compute-rhino3d'

  // Cargar rhino3dm
  const rhino = await rhino3dm()
  console.log('Loaded rhino3dm.')

```

## El primer uso de Compute

En el repositorio [Javascript Sample](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/js) puede encontrar ejemplos de JavaScript para acceder a Compute. 

# Próximos pasos

*¡Felicidades!*  Dispone de las herramientas para utilizar el [servidor de Rhino Compute](https://www.rhino3d.com/compute).  *¿Y ahora qué?*

1. Para ver la naturaleza transaccional de Compute, lea [compute.rhino3d.js](https://files.mcneel.com/rhino3dm/js/latest/compute.rhino3d.js).
1. Consulte una lista de las [más de 2400 llamadas a la API](https://compute.rhino3d.com/sdk) disponibles para compute.rhino3d.com.
1. Descargue el repositorio [Compute Samples de GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute).
1. Las bibliotecas son aún muy nuevas y cambian rápidamente. Pruébelos o participe. Haga cualquier pregunta o comparta su trabajo en el [Foro sobre Compute](https://discourse.mcneel.com/c/serengeti/compute-rhino3d).


+++
aliases = ["/en/5/guides/compute/features/", "/en/6/guides/compute/features/", "/en/7/guides/compute/features/", "/en/wip/guides/compute/features/"]
authors = [ "brian" ]
categories = [ "Getting Started" ]
description = "Funciones del SDK de Rhino a través de la API REST"
keywords = [ "developer", "compute" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Compute: Funciones"
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


## Compute puede:
  * Calcular las definiciones de Grasshopper en línea con soluciones en serie o en paralelo.
  * Manipular Rhino (3DM) y otros tipos de archivos en cualquier lugar de la red.
  * Llamar a más de 2400 operaciones geométricas en objetos personalizados desde los procesos existentes en línea. Incluye puntos, curvas, superficies, mallas y sólidos.

## Funciones de Compute
  * Realice cálculos geométricos a través de una API REST sin estado basada en la nube.
  * Acceda a [más de 2400 llamadas a la API de RhinoCommon](https://compute.rhino3d.com/sdk) desde fuera de Rhino.
  * Acceda a funciones adicionales de RhinoCommon no disponibles en [openNURBS](https://www.rhino3d.com/opennurbs), tales como:
  * Cálculos de punto más cercano
  * Cálculos de intersección
  * Triangulación de superficies (mallado)
  * Interpolación
  * Booleanas
  * Cálculos de propiedades de área y masa
  * Otros cálculos geométricos
  * Llamadas a métodos REST ampliables mediante una declaración común.
  * Acceda a los plugins existentes de Rhino/Grasshopper a través de la interfaz en línea.
  * Serialice operaciones en una sola petición a través de scripts de Grasshopper o Python.
  * Bibliotecas del lado del cliente disponibles para usar con C#(.NET), Python y JavaScript.

## Código abierto:
Basado en la tecnología [Rhino Inside™](https://www.rhino3d.com/inside), Compute es un [proyecto de código abierto](https://github.com/mcneel/compute.rhino3d).
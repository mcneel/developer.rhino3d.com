+++
aliases = ["/en/5/guides/compute/compute-python-getting-started/", "/en/6/guides/compute/compute-python-getting-started/", "/en/7/guides/compute/compute-python-getting-started/", "/en/wip/guides/compute/compute-python-getting-started/"]
authors = [ "scottd" ]
categories = [ "Getting Started", "Client" ]
description = "Esta guía muestra todas las herramientas necesarias para empezar a utilizar Rhino Compute Service con Python."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "Python" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Llamar a Compute con Python"
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


Al final de esta guía, deberías tener instaladas todas las herramientas necesarias para utilizar [Rhino Compute](https://www.rhino3d.com/compute) a con Python.

Consulte este [videotutorial de iniciación de Junichiro Horikawa con Python](https://youtu.be/XCkRXAEJMhg).


Esta guía asume que tiene Python instalado en la plataforma:

- Python 2.7 - Windows (32 y 64 bits)
- Python 3.7 - Windows (32 y 64 bits)
- Python 2.7 - OSX (instalado a través de homebrew)
- Python 3.7 - OSX (instalado a través de homebrew)
- Linux y otras versiones de python son compatibles a través de distribuciones de código fuente en PyPi

## Crear un proyecto de Compute en Python

Hay algunas herramientas del lado del cliente que necesitan ser instaladas en Python y que son esenciales para comunicarse con el servidor de Compute. Entre ellas figuran:

- **rhino3dm.py** -  Esta es la parte de las [librerías de Rhino3dm](https://github.com/mcneel/rhino3dm).  Es un wrapper de Python para [OpenNurbs](https://developer.rhino3d.com/guides/opennurbs/) que contiene las funciones para leer y escribir objetos de geometría de Rhino. Está disponible como paquete Pip.

  `pip install rhino3dm`

- **compute-rhino3d.py** - Es un paquete en desarrollo para añadir clases disponibles en [RhinoCommon](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/), pero no disponibles a través de rhino3dm.py. Compute-rhino3d realiza llamadas al servidor McNeel Cloud Compute para estas funciones. Gestiona todas las autorizaciones de transacciones y la conversión de datos JSON.

  `pip install compute-rhino3d`

## El primer uso de Compute

Un ejemplo de uso de Python para acceder a Compute se puede encontrar en el ejemplo [makemesh.py](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/py/SampleTkinter).

Tenga en cuenta que las llamadas a compute Python se realizan a través del paquete `compute_rhino3d.py` utilizando un `_` (guión bajo) y no un `-` (guión).

# Próximos pasos

*¡Felicidades!*  Dispone de las herramientas para utilizar el [servidor de Rhino Compute](https://www.rhino3d.com/compute).  *¿Y ahora qué?*

1. Para ver la naturaleza transaccional de Compute, lea **compute.rhino3d.py**.
1. Consulte una lista de las [más de 2400 llamadas API](https://compute.rhino3d.com/sdk) disponibles para compute.rhino3d.com.
1. Descargue el repositorio [Compute Samples de GitHub](https://github.com/mcneel/compute.rhino3d.samples).
1. Las bibliotecas son todavía muy nuevas y cambian rápidamente. Pruébelas o participe. Haga preguntas o comparta su trabajo en el [Foro de Compute](https://discourse.mcneel.com/c/serengeti/compute-rhino3d).

---

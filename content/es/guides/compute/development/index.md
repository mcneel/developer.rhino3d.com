+++
aliases = ["/en/5/guides/compute/development/", "/en/6/guides/compute/development/", "/en/7/guides/compute/development/", "/en/wip/guides/compute/development/"]
authors = [ "pedro" ]
categories = [ "Getting Started", "Development" ]
description = "Implementar Compute para producción"
keywords = [ "developer", "compute", "production" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Ejecutar y depurar Compute localmente"
type = "guides"
weight = 2
override_last_modified = "2024-05-13T15:49:48Z"

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

Rhino.Compute permite usar el cálculo geométrico de Rhino en la nube. Antes de implementar su aplicación en un entorno de producción, debe asegurarse de que todo funciona perfectamente en un entorno controlado.

Esta guía está dirigida a desarrolladores familiarizados con Windows y con conocimientos básicos de [Visual Studio](https://visualstudio.microsoft.com/downloads/) y [Git](https://git-scm.com/downloads). Tanto si es un usuario experimentado de Rhino como si es nuevo en Rhino.Compute, esta documentación le proporcionará los pasos necesarios para configurar su entorno de desarrollo y empezar a depurar con eficacia.

## Requisitos previos

Antes de empezar a configurar Rhino.Compute en su equipo local, debe asegurarse de que dispone de las herramientas adecuadas. Esto es lo que necesitará:

- Sistema operativo Windows. Rhino.Compute solo funciona en Windows.
- Entorno de desarrollo. Necesitará [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) para compilar el código.
- Control de versiones. [Git](https://git-scm.com/downloads) es necesario para clonar el repositorio compute.rhino3d y gestionar las ramas según su versión de Rhino.
- Rhino. Visite nuestra página de descargas para obtener las últimas versiones de [Rhino 8](https://www.rhino3d.com/download/rhino-for-windows/8/latest) o [Rhino 7](https://www.rhino3d.com/download/rhino-for-windows/7/latest). Después de descargarla e instalarla, inicie Rhino y siga las instrucciones de inicio para validar la licencia en su máquina o a través de Cloud Zoo.

{{< call-out "note" "Nota" >}}
Deberá ejecutar la versión específica de Rhino.Compute según la versión de Rhino que haya instalado. En la siguiente sección, clonará el código fuente del repositorio compute.rhino3d. Si ha instalado Rhino 8 en su máquina, tendrá que asegurarse de clonar la rama 8.x. Alternativamente, si ha instalado Rhino 7, asegúrese de clonar la rama 7.x.
{{< /call-out >}}

## Clonar el repositorio

Para obtener la última versión de Rhino.Compute deberá clonar su [repositorio](https://github.com/mcneel/compute.rhino3d) desde nuestra cuenta oficial en Github.

1. Vaya a [https://github.com/mcneel/compute.rhino3d](https://github.com/mcneel/compute.rhino3d)

1. En el menú desplegable de la rama, asegúrese de seleccionar la rama 8.x o 7.x para clonar.

1. Una vez allí, haga clic en el botón verde "<> Code" y copie la URL del repositorio.
![compute_geometry_clone](/images/compute_geometry_clone.png)

1. En su equipo local, cree una carpeta en la que quiera clonar el repositorio.

1. Navegue a ese directorio a través del símbolo del sistema y escriba `git clone` y pegue la URL copiada.
    ```python
    git clone https://github.com/mcneel/compute.rhino3d.git
    ```
1. Una vez finalizada la operación de clonación, verá los archivos y directorios que se han descargado del repositorio compute.rhino3d en la carpeta que ha creado.

## Anatomía de la solución

El repositorio Rhino.Compute se compone de dos proyectos principales, cada uno de los cuales cumple distintas funciones dentro del marco. Comprenderlos puede ayudar a aclarar cómo funciona Rhino.Compute, especialmente si desea trabajar o contribuir a su desarrollo. He aquí un desglose de los dos proyectos:

- **compute.geometry**. Este proyecto se centra principalmente en los aspectos de cálculo geométrico. Esencialmente, compute.geometry proporciona una API REST que expone el motor de geometría de Rhino para su uso a través de la web. Esto significa que las operaciones geométricas se pueden realizar en un servidor y los resultados se pueden recuperar de forma remota, lo que lo hace muy útil para aplicaciones basadas en web o servicios que requieren un procesamiento geométrico complejo.

- **rhino.compute**. Este proyecto puede considerarse como una capa de servicio de alto nivel que gestiona y orquesta las llamadas a la API de compute.geometry, gestionando tareas como la autenticación, la generación de procesos secundarios y el establecimiento de límites de tiempo para el proceso de cierre.

## Compilar la solución

Ahora que ya tiene el código, es hora de abrir el proyecto en Visual Studio 2022 y prepararlo para la depuración.

1. Navegue hasta el directorio donde clonó el repositorio y busque el archivo **compute.sln**. Haga doble clic en el archivo para abrir el proyecto en Visual Studio 2022.

1. Establezca la configuración de la solución en modo **Debug**. Esto permite ejecutar el código con todas las funciones de depuración, lo que facilita el seguimiento del código y la detección de errores.
![compute_geometry_vs_debug](/images/compute_geometry_vs_debug.png)

1. En el menú File, haga clic en Build -> Build Solution (Ctrl + Mayús + B). Esto compilará todos los archivos del proyecto.
![compute_geometry_vs_build](/images/compute_geometry_vs_build.png)

1. En el panel Solution Explorer, haga clic con el botón derecho del ratón en el proyecto **rhino.compute** y seleccione **Set as Startup Project**. Esto asegura que cuando ejecute el depurador, Visual Studio iniciará este proyecto en particular.
![compute_geometry_vs_startup](/images/compute_geometry_vs_startup.png)

1. Haga clic en **rhino.compute** para iniciar la aplicación en el depurador. Aparecerá una aplicación de consola en la barra de tareas mostrando el estado del proceso de carga de Rhino.Compute.
![compute_geometry_vs_run](/images/compute_geometry_vs_run.png)

1. Ahora solo tiene que esperar unos segundos a que Rhino.Compute se cargue. Tenga en cuenta que la información registrada depende de la versión de Rhino que haya elegido previamente.
![compute.geometry.exe](/images/compute_geometry_screenshot.png)

## Probar un punto de conexión

Con la aplicación Rhino.Compute en la consola, vaya a cualquiera de estos puntos de conexión para comprobar que todo funciona.
- [http://localhost:6500/version](http://localhost:6500/version)
- [http://localhost:6500/healthcheck](http://localhost:6500/healthcheck)
- [http://localhost:6500/activechildren](http://localhost:6500/activechildren)
- [http://localhost:6500/sdk](http://localhost:6500/sdk)
+++
aliases = ["/5/guides/", "/6/guides/", "/7/guides/", "/wip/guides/"]
description = "Todas las guías disponibles para desarrollar Rhino o Grasshopper."
title = "Guías"
type = "guides"
weight = 2

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = []
since = 0

[page_options]
byline = false
toc = true
toc_type = "single"
+++

## [General](/guides/general)

*Guías aplicables a todas las plataformas y SDK*

### Información general

- [Desarrollo de software público](/guides/general/developing-software-in-public)
- [Información general de la tecnología de Rhino](/guides/general/rhino-technology-overview)
- [Preguntas más frecuentes (FAQ)](/guides/general/frequently-asked-questions)

### Introducción

- [Requisitos previos para desarrolladores](/guides/general/rhino-developer-prerequisites)
- [Contribuir](/guides/general/contributing)

### Fundamentos

- [¿Qué es un plugin de Rhino?](/guides/general/what-is-a-rhino-plugin)
- [Administrador de paquetes de Rhino](/guides/yak/)
- [Sistema de la IU de Rhino](/guides/general/rhino-ui-system/)
- [Macros de comandos simples](/guides/general/creating-command-macros/)

### [Matemáticas esenciales](/guides/general/essential-mathematics)

- [Introducción](/guides/general/essential-mathematics)  
- [Matemáticas vectoriales](/guides/general/essential-mathematics/vector-mathematics)  
- [Matrices y transformaciones](/guides/general/essential-mathematics/matrices-transformations)  
- [Curvas paramétricas y superficies](/guides/general/essential-mathematics/parametric-curves-surfaces)  
- [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6/essentialmathematics/) [Descargar Matemáticas Esenciales para Diseño Computacional como PDF](https://www.rhino3d.com/download/rhino/6/essentialmathematics/)

### Este sitio web

- [Cómo funciona este sitio](/guides/general/how-this-site-works)
- [Introducción a los documentos para desarrolladores](https://github.com/mcneel/developer-rhino3d-com/blob/main/README.md)
- [Guía de estilo de los documentos para desarrolladores](/guides/general/developer-docs-style-guide)

## [Scripting](/guides/scripting)

*Guías sobre el uso de las funciones de scripting en Rhino 8 y versiones posteriores, que se aplican a todos los lenguajes de programación*

### Introducción

#### Editor de scripts
  - [Abrir el editor de scripts](/guides/scripting/scripting-command/#opening-script-editor)
  - [Primer script](/guides/scripting/scripting-command/#first-script)
  - [Editar un script](/guides/scripting/scripting-command/#edit-script)
  - [Ejecutar scripts](/guides/scripting/scripting-command/#running-scripts)
  - [Depurar scripts](/guides/scripting/scripting-command/#debugging-scripts)
  - [Usar paquetes](/guides/scripting/scripting-command/#using-packages)
  - [Funciones del editor](/guides/scripting/scripting-command/#editor-features)

#### Componente de script
  - [Crear un componente de script](/guides/scripting/scripting-component/#script-component)
  - [Primer script](/guides/scripting/scripting-component/#first-script)
  - [Entradas y salidas de scripts](/guides/scripting/scripting-component/#script-inputs-and-outputs)
  - [Editar script](/guides/scripting/scripting-component/#edit-script)
  - [Ejecutar scripts](/guides/scripting/scripting-component/#debugging-scripts)
  - [Depurar scripts](/guides/scripting/scripting-component/#debugging-scripts)
  - [Usar paquetes](/guides/scripting/scripting-component/#using-packages)
  - [Funciones del editor](/guides/scripting/scripting-component/#editor-features)

### Scripts de Python
- <!-- [Scripts de Python](/guides/scripting/scripting-python) --> Scripting: Python {{% comingsoon-label %}}
- [Scripts de Grasshopper: Python](/guides/scripting/scripting-gh-python)

### Scripts C#
- <!-- [Scripts C#](/guides/scripting/scripting-csharp) --> Scripting: C# {{% comingsoon-label %}}
- [Scripts de Grasshopper: C#](/guides/scripting/scripting-gh-csharp)

### Funciones del editor
- <!-- [Funciones de edición](/guides/scripting/editor-editing) --> Funciones de edición {{% comingsoon-label %}}
- <!-- [Explorador](/guides/scripting/editor-explorer) --> Explorador {{% comingsoon-label %}}
- <!-- [Buscar y reemplazar](/guides/scripting/editor-search) --> Buscar y reemplazar {{% comingsoon-label %}}
- <!-- [Terminal](/guides/scripting/editor-terminal) --> Terminal {{% comingsoon-label %}}
- <!-- [Bandeja de problemas](/guides/scripting/editor-problems) --> Bandeja de problemas {{% comingsoon-label %}}
- <!-- [Depurar scripts](/guides/scripting/editor-debug) --> Depurador {{% comingsoon-label %}}
- <!-- [Plantillas](/guides/scripting/editor-templates) --> Plantillas {{% comingsoon-label %}}
- <!-- [Ejemplos](/guides/scripting/editor-examples) --> Ejemplos {{% comingsoon-label %}}
- <!-- [Ayuda](/guides/scripting/editor-help) --> Ayuda {{% comingsoon-label %}}
- [Configuraciones](/guides/scripting/editor-configs)
- <!-- [Registros](/guides/scripting/editor-logs) --> Registros {{% comingsoon-label %}}

### Publicación 

- <!-- [Crear de proyectos de Rhino](/guides/scripting/projects-create) --> Crear proyectos de Rhino {{% comingsoon-label %}}
- <!-- [Crear plugins de Rhino y Grasshopper](/guides/scripting/projects-publish) --> Crear plugins de Rhino y Grasshopper {{% comingsoon-label %}}

### Avanzado

- [Inicialización de lenguaje](/guides/scripting/advanced-langinit)
- <!-- [CPython Runtime y servidor de lenguaje](/guides/scripting/advanced-pyruntime) --> CPython Runtime y servidor de lenguaje {{% comingsoon-label %}}
- [Archivos de ruta de Python](/guides/scripting/advanced-pthfiles)
- <!-- [Librerías de lenguajes](/guides/scripting/advanced-libraries) --> Librerías de lenguajes {{% comingsoon-label %}}
- <!-- [Ejecución asíncrona](/guides/scripting/advanced-async) --> Ejecución asíncrona {{% comingsoon-label %}}
- <!-- [Extensión de VisualStudioCode](/guides/scripting/advanced-vscode) --> Extensión de VisualStudioCode {{% comingsoon-label %}}
- <!-- [Interfaz de línea de comandos de RhinoCode](/guides/scripting/advanced-cli) --> Interfaz de línea de comandos de RhinoCode {{% comingsoon-label %}}
<!-- [API de RhinoCode](/guides/scripting/advanced-core-api) -->
<!-- [API de RhinoCodeEditor](/guides/scripting/advanced-editor-api) -->

## [RhinoCommon](/guides/rhinocommon)

*El SDK de plug-ins .NET multiplataforma para Rhino.*

### Información general

- [¿Qué es RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon/)
- [Novedades](/guides/rhinocommon/whats-new/)

### Introducción

- Instalar herramientas ([Windows](/guides/rhinocommon/installing-tools-windows/), [Mac](/guides/rhinocommon/installing-tools-mac/))
- Su primer plugin ([Windows](/guides/rhinocommon/your-first-plugin-windows/), [Mac](/guides/rhinocommon/your-first-plugin-mac/), [Multiplataforma](/guides/rhinocommon/your-first-plugin-crossplatform/))
- Instaladores de plugins ([Windows](/guides/rhinocommon/plugin-installers-windows/), [Mac](/guides/rhinocommon/plugin-installers-mac/))
- [Distribuir un plug-in de Rhino con el administrador de paquetes](/guides/yak/creating-a-rhino-plugin-package/)

### Fundamentos

{{< dev-topic-list "guides" "RhinoCommon" "Fundamentals" "weight" >}}

### Geometría de RhinoCommon 

- [Introducción](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#31-overview)  
- [Estructuras geométricas](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#32-geometry-structures)  
    - [La estructura Point3d](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#321-the-point3d-structure)  
    - [Puntos y vectores](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#322-points--vectors)  
    - [Curvas ligeras](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#323-lightweight-curves)  
    - [Superficies ligeras](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#324-lightweight-surfaces)  
    - [Superficies ligeras](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#325-other-geometry-structures)  
- [Clases de geometría](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#33-geometry-classes)  
    -  [Curvas](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#331-curves)  
    - [Superficies](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#332-surfaces)  
    - [Representación de contornos (Brep)](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#334-boundary-representation-brep)  
    - [Otras clases de geometría](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#335-other-geometry-classes)  
- [Transformaciones geométricas](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#34-geometry-transformations)  

### Renderizado

{{< dev-topic-list "guides" "RhinoCommon" "Rendering" "weight" >}}

### Avanzado

{{< dev-topic-list "guides" "RhinoCommon" "Advanced" "weight" >}}

### Zoo

{{< dev-topic-list "guides" "RhinoCommon" "Zoo" "weight" >}}

### Cloud Zoo

{{< dev-topic-list "guides" "RhinoCommon" "CloudZoo" "weight" >}}

## [Rhino.Python](/guides/rhinopython)


*Añada rápidamente funcionalidades a Rhino o automatizar tareas repetitivas.*

### Información general

{{< dev-topic-list "guides" "RhinoPython" "Overview" "weight" "8" >}}

### Introducción

- Su primer script Python en Rhino ([Windows](/guides/rhinopython/your-first-python-script-in-rhino-windows), [Mac](/guides/rhinopython/your-first-python-script-in-rhino-mac), [Grasshopper](/guides/rhinopython/your-first-python-script-in-grasshopper))
- [Dónde encontrar ayuda...](/guides/rhinopython/python-where-to-find-help)
- [Solución de problemas de instalación](/guides/rhinopython/python-troubleshooting-install)

### Editor de Python para Windows

{{< dev-topic-list "guides" "RhinoPython" "Python Windows" "weight" "8" >}}

### Python en Grasshopper

{{< dev-topic-list "guides" "RhinoPython" "GhPython" "weight" "8" >}}

### Fundamentos

{{< dev-topic-list "guides" "RhinoPython" "Fundamentals" "weight" "8" >}}

### Python en Rhino

{{< dev-topic-list "guides" "RhinoPython" "Python in Rhino" "weight" "8" >}}

### [Rhino.Python 101](/guides/rhinopython/primer-101)

&nbsp;&nbsp; [Introducción](/guides/rhinopython/primer-101)  
&nbsp;&nbsp; [Dónde encontrar ayuda](/guides/rhinopython/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [¿Qué es?](/guides/rhinopython/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [Fundamentos de Python](/guides/rhinopython/primer-101/2-python-essentials/)  
&nbsp;&nbsp; 3. [Anatomía de los scripts](/guides/rhinopython/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operadores y funciones](/guides/rhinopython/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Ejecución condicional](/guides/rhinopython/primer-101/5-conditional-execution/)  
&nbsp;&nbsp; 6. [Tuplas, listas y diccionarios](/guides/rhinopython/primer-101/6-tuplas-listas-diccionarios/)  
&nbsp;&nbsp; 7. [Clases](/guides/rhinopython/primer-101/7-classes/)  
&nbsp;&nbsp; 8. [Geometría](/guides/rhinopython/primer-101/8-geometry/)  

&nbsp;&nbsp; [{{< awesome "fas fa-download">}} ](https://download.rhino3d.com/IronPython/5.0/RhinoPython101/) [Descargue el Manual de Rhino.Python 101 como PDF ](https://download.rhino3d.com/IronPython/5.0/RhinoPython101/)  


### Intermedio

{{< dev-topic-list "guides" "RhinoPython" "Intermediate" "weight" "8" >}}

### Diálogos personalizados en Eto

{{< dev-topic-list "guides" "RhinoPython" "Eto" "weight" "8" >}}


### Otros recursos

- [Foro sobre scripts de Rhino (Discourse)](https://discourse.mcneel.com/c/scripting)  
- [Muestras de Rhino.Python](/samples/#rhinopython)  
- [Muestras de Rhino.Python para desarrolladores en GitHub](https://github.com/mcneel/rhino-developer-samples/tree/master/rhinopython)  
- [Tutoriales de Python de Designalyze](https://designalyze.com/)
- [Proyecto Pletora](https://www.plethora-project.com/education/2017/5/31/rhino-python-programming)
- [Blog de Steve Baer](https://stevebaer.wordpress.com/category/python/)
- [Guía de Python para principiantes](https://wiki.python.org/moin/BeginnersGuide/Programmers)
- [Serie de Python en Tutorials Point](https://www.tutorialspoint.com/python/index.htm)
- [Rhino.Python Dash Docset](https://discourse.mcneel.com/t/rhino-python-dash-docset/6399)
- [Tutoriales en vídeo sobre la naturaleza del código](https://www.youtube.com/watch?v=Kyi_K85Gsm4&list=PL5Up_u-XkWgP7nB7XIevMTyBCZ7pvLBGP)

## [openNURBS](/guides/opennurbs)

*Lea y escriba archivos 3dm de Rhino en su aplicación.*

### Información general

{{< dev-topic-list "guides" "openNURBS" "Overview" "weight" >}}

### Introducción

{{< dev-topic-list "guides" "openNURBS" "Getting Started" "weight" >}}

### Fundamentos

{{< dev-topic-list "guides" "openNURBS" "Fundamentals" "weight" >}}

### Avanzado

{{< dev-topic-list "guides" "openNURBS" "Advanced" "weight" >}}

## [C/C++](/guides/cpp)

*SDK nativo de Rhino para plugins de Windows.*

### Información general

{{< dev-topic-list "guides" "C/C++" "Overview" "weight" >}}

### Introducción

{{< dev-topic-list "guides" "C/C++" "Getting Started" "weight" >}}

### Fundamentos

{{< dev-topic-list "guides" "C/C++" "Fundamentals" "weight" >}}

### Avanzado

{{< dev-topic-list "guides" "C/C++" "Advanced" "weight" >}}

### Renderizado (RDK)

{{< dev-topic-list "guides" "C/C++" "RDK" "weight" >}}

### Zoo

{{< dev-topic-list "guides" "C/C++" "Zoo" "weight" >}}

### Solución de problemas

{{< dev-topic-list "guides" "C/C++" "Troubleshooting" "weight" >}}

## [Grasshopper](/guides/grasshopper)


*Crear componentes y plugins de Grasshopper personalizados.*

### Información general

- [¿Qué es un componente de Grasshopper?](/guides/grasshopper/what-is-a-grasshopper-component/)

### Introducción

- Herramientas de instalación ([Windows](/guides/grasshopper/installing-tools-windows/), [Mac](/guides/grasshopper/installing-tools-mac/))
- Su primer componente ([Windows](/guides/grasshopper/your-first-component-windows/), [Mac](/guides/grasshopper/your-first-component-mac/))
- [Distribuir un complemento de Grasshopper con el administrador de paquetes](/guides/yak/creating-a-rhino-plugin-package/)

### Fundamentos

{{< dev-topic-list "guides" "Grasshopper" "Fundamentals" "weight" >}}

### Avanzado

{{< dev-topic-list "guides" "Grasshopper" "Advanced" "weight" >}}

### En profundidad

{{< dev-topic-list "guides" "Grasshopper" "In Depth" "weight" >}}

### [Algoritmos y estructuras de datos esenciales para Grasshopper](/guides/grasshopper/gh-algorithms-and-data-structures/)

- [Introducción](/guides/grasshopper/gh-algorithms-and-data-structures/)
- [Algoritmos y datos](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/)
- [Introducción a las estructuras de datos](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/)
- [Estructuras de datos avanzadas](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/)
- [{{< awesome "fas fa-download">}}](https://www.rhino3d.com/download/rhino/6.0/essential-algorithms/) [Descargar el PDF completo y ejemplos de GH](https://www.rhino3d.com/download/rhino/6.0/essential-algorithms/)

### Python en Grasshopper

{{< dev-topic-list "guides" "RhinoPython" "GhPython" "weight" "8" >}}

### [C# en Grasshopper](/guides/grasshopper/csharp-essentials/)

- [Componente C# en Grasshopper](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#21-introduction)
- [Conceptos básicos de programación en C#](/guides/grasshopper/csharp-essentials/2-csharp-basics/)
- [Geometría de RhinoCommon](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/)
- [Algoritmos de diseño](/guides/grasshopper/csharp-essentials/4-design-algorithms/)


## [RhinoScript](/guides/rhinoscript)


*RhinoScript, herramienta de scripting basada en el lenguaje VBScript de Microsoft. Con RhinoScript, puede agregar rápidamente funcionalidades a Rhino para Windows o automatizar tareas repetitivas.*

### Información general

- [¿Qué son VBScript y RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript)

### [RhinoScript 101](/guides/rhinoscript/primer-101)

&nbsp;&nbsp; [Introducción](/guides/rhinoscript/primer-101)  
&nbsp;&nbsp; [Dónde encontrar ayuda](/guides/rhinoscript/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [¿Qué es?](/guides/rhinoscript/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [RhinoScript Essentials](/guides/rhinoscript/primer-101/2-vbscript-essentials/)  
&nbsp;&nbsp; 3. [Anatomía de los scripts](/guides/rhinoscript/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operadores y funciones](/guides/rhinoscript/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Ejecución condicional](/guides/rhinoscript/primer-101/5-conditional-execution/)  
&nbsp;&nbsp; 6. [Matrices](/guides/rhinoscript/primer-101/6-arrays/)  
&nbsp;&nbsp; 7. [Geometría](/guides/rhinoscript/primer-101/7-geometry/)  
&nbsp;&nbsp; [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/5.0/rhinoscript101) [Descargar el Manual de RhinoScript 101 como PDF](https://www.rhino3d.com/download/rhino/5.0/rhinoscript101)

### Fundamentos

{{< dev-topic-list "guides" "RhinoScript" "Fundamentals" "weight" >}}


### Intermedio

{{< dev-topic-list "guides" "RhinoScript" "Intermediate" "weight" >}}

### Avanzado

{{< dev-topic-list "guides" "RhinoScript" "Advanced" "weight" >}}

### Solución de problemas

{{< dev-topic-list "guides" "RhinoScript" "Troubleshooting" "weight" >}}

### Otros recursos

- [Utilidades de scripts de Pascal Golay para Rhino](https://wiki.mcneel.com/people/pascalgolay)
- [Muestras de RhinoScript en GitHub](https://github.com/mcneel/rhinoscript)
- [RhinoScript Dash Docset](https://discourse.mcneel.com/t/rhinoscript-dash-docset/6382)
- [Ayuda online de RhinoScript](https://www.rhino3d.com/5/rhinoscript/index.html)

<!-- ## [Compute](/guides/compute) -->
<h2 id="compute"><a href="/guides/compute">Compute</a></h2>


### Introducción

{{< dev-topic-list "guides" "Compute" "Getting Started" "weight" >}}

### Implementación de producción

{{< dev-topic-list "guides" "Compute" "Deployment" "weight" >}}

### Hops

{{< dev-topic-list "guides" "Compute" "Hops" "weight" >}}

## Servicios para desarrolladores

### [Localización](https://www.rhino3d.com/localization)

Nuestra oficina regional en Europa proporciona un servicio de traducción y localización para desarrolladores externos y cualquier persona interesada en traducir su productos al alemán, español, francés, italiano, inglés, etc. [Más información...](https://www.rhino3d.com/localization)

### Soporte de marketing

Si ha desarrollado un complemento de Rhino que le gustaría poner a disposición de otros usuarios, [food4Rhino](https://www.food4rhino.com/) es el lugar donde puede publicar toda la información sobre sus plug‑ins para Rhino y Grasshopper. Food4Rhino es el servicio de comunidad de plug-ins de McNeel. Los usuarios pueden encontrar los últimos plug-ins de Rhino, complementos de Grasshopper, materiales, texturas y fondos, scripts y mucho más. Es gratuito. [Preguntas más frecuentes](https://www.food4rhino.com/es/faq)
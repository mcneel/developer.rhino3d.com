+++
aliases = ["/5/guides/general/rhino-technology-overview/", "/6/guides/general/rhino-technology-overview/", "/7/guides/general/rhino-technology-overview/", "/wip/guides/general/rhino-technology-overview/"]
authors = ["brian" ]
categories = [ "Overview" ]
description = "Resumen de la tecnología de Rhino".
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Información general sobre la tecnología de Rhino"
type = "guides"
weight = 0
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = ["Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Información general

Rhinoceros se compone de muchas capas, escritas en muchos lenguajes y apiladas unas sobre otras.  Las más fundacionales están en la parte inferior, pero las capas superiores tampoco deben considerarse superficiales...

![Pilas de Rhino](/images/rhino-technology-overview-01.png)

Analicemos cada una de las capas por separado, empezando por la...

## Capa fundacional

### Núcleo C++ de Rhino

El núcleo C++ de Rhino es el volumen de código más amplio antiguo.  Utilizamos MFC de Microsoft en algunas partes, incluido el SDK.  Aquí es donde se gestiona el documento en tiempo de ejecución, donde se encuentra todo el código de dibujo de vista OpenGL y donde reside el código de geometría computacional escrito por nuestros matemáticos. Muchos de los comandos de Rhino están aquí.

Gran parte de la interfaz de usuario: la línea de comandos, el marco principal de la aplicación, la barra de estado y los cuadros de diálogo de muchos comandos del núcleo de Rhino.

### openNURBS

openNURBS es un código fuente C++ gratuito que permite leer y escribir archivos *3dm* de Rhino, desde la versión 1.  openNURBS fue nuestro primer proyecto de código abierto.

El código compila en Windows, macOS, Linux, iOS y Android.  Se utiliza en varias aplicaciones de terceros como ArchiCAD, SolidWorks, Inventor, SketchUp y muchos otros productos para leer o escribir archivos *3dm* directamente.

openNURBS es lo que Rhino utiliza de forma nativa para leer/escribir archivos *3dm*.  Este kit de herramientas se publica antes que Rhino, por lo que cualquier producto, incluidos nuestros competidores, puede ser compatible con los archivos *3dm* más recientes.  No hay diferencia entre los archivos *3dm* que escribe Rhino y los de otras aplicaciones que utilizan openNURBS para leer y escribir *3dm*.

Para obtener más información sobre openNURBS, consulte las [guías de openNURBS](/guides/opennurbs/).

### SDK de C++

Además de todo esto está nuestro SDK de C++, disponible solo en Windows.

La compilación con el SDK de C++ requiere una versión específica de Microsoft Visual Studio y Microsoft C-Runtime.  Hay que recompilar para cada versión principal de Rhino.

Prácticamente todo lo que Rhino puede hacer se expone a través del SDK de C++. Algunos comandos y funciones aún no se han expuesto, pero este SDK es muy amplio y rico.

Por desgracia, al estar tan estrechamente vinculado al núcleo de Rhino, los desarrolladores de plugins tienen que recompilar sus plugins para cada versión de Rhino.

Para obtener más información sobre el SDK de C++, consulte las [guías de C/C++](/guides/cpp/).

## Pila de C++

En la columna derecha del diagrama de pila anterior está la parte C++ de Rhino.  La pila C++ nos permite a nosotros y a los desarrolladores de plugins de terceros escribir plugins de Rhino utilizando el mismo SDK de C++ que utilizamos para desarrollar el propio Rhino.  Tenga en cuenta que no puede crear componentes de Grasshopper utilizando C++.

### Plugins de C++

Además del SDK de C++, existen plugins de C++.  Muchas de las funciones que vienen con Rhino, incluidos algunos comandos, E/S de archivos y renderizadores, son en realidad plugins de C++.  También hay decenas de plugins de C++ de terceros, como [VisualARQ de Asuni](http://www.visualarq.com/), [RhinoCAM de MecSoft](https://mecsoft.com/rhinocam-software/) y [V-Ray de Chaos Software](https://www.chaosgroup.com/vray/rhino).

Para obtener más información sobre el SDK de C++, consulte las [guías de C/C++](/guides/cpp/).

### RhinoScript

Uno de los plugins de C++ que incluimos con Rhino es [RhinoScript](/guides/rhinoscript/what-are-vbscript-rhinoscript/).  RhinoScript expone un útil subconjunto del SDK de Rhino a través de VBScript, un lenguaje de scripting muy utilizado y popular.  RhinoScript permite acceder no solo a Rhino, sino a cualquier otro objeto COM de Windows.

Para obtener más información, consulte las [guías de RhinoScript](/guides/rhinoscript/), y más concretamente la guía [¿Qué son VBScript y RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript/).

## .Pila .NET

El SDK .NET se representa aquí en tres capas:

- API C
- .NET Framework
- RhinoCommon
- Eto

### API C

Una API C directa encapsula el SDK de C++ y nos permite invocar a la plataforma (P/Invoke) en el SDK de C++, formando un puente entre el código nativo C++ y las capas gestionadas de .NET.

### .NET Framework

Microsoft desarrolla [.NET Framework](https://www.microsoft.com/net/framework). .NET permite escribir plugins en C#, F#, VB.NET y cualquier otro lenguaje que se compile según el lenguaje IL de Microsoft.

Microsoft .NET Framework se suministra con Windows.

En el producto Rhino para Mac, incrustamos [Mono Runtime](https://www.mono-project.com), una implementación parcial multiplataforma de .NET Runtime.

Para obtener más información sobre .NET y su relación con el desarrollo de Rhino, consulte [¿Qué son Mono y Xamarin?] (/guides/rhinocommon/what-are-mono-and-xamarin/).

### RhinoCommon

RhinoCommon es nuestro SDK .NET para Rhino, creado sobre las partes de .NET Framework que son *comunes* tanto en Windows como en macOS (a través de Mono).  RhinoCommon permite a los desarrolladores ejecutar código .NET tanto en Rhino para Windows como en Rhino para Mac.

Para obtener más información sobre RhinoCommon, consulte las [guías de RhinoCommon](/guides/rhinocommon/), o más concretamente, la guía [¿Qué es RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon).

### Eto

Con RhinoCommon, puede escribir plugins .NET que funcionen en Windows y Mac... excepto la interfaz de usuario. El equipo de Mono no clonó WinForms ni WPF, por lo que ninguna de esas tecnologías funciona en Mac.  Para solucionar este problema, Rhino incluye ahora Eto.Forms.  Eto permite escribir la interfaz de usuario una vez en C#, XAML o JSON y utilizarla en Windows y macOS.  En realidad, la IU escrita en Eto puede funcionar también en iOS, Android y Linux.

Para obtener más información sobre Eto, consulte [Eto.Forms en GitHub](https://github.com/picoe/Eto).

### .Plugins .NET

Sobre RhinoCommon se han desarrollado numerosos plugins, tanto internos como de terceros.  [Grasshopper](http://www.grasshopper3d.com/), por ejemplo, es un plugin de RhinoCommon. Algunos comandos, renderizadores y plugins de archivos IO de Rhino están escritos como plugins de RhinoCommon.  A medida que pasa el tiempo, estamos trasladando cada vez más funciones a los plugins de RhinoCommon/.NET para poder compartir más código entre plataformas.  Muchos plugins de terceros también se han escrito utilizando RhinoCommon y .NET, como [RhinoGold](http://www.tdmsolutions.com/) y [Matrix de GEMVision](http://www.stuller.com/matrix), y [Orca3D](http://orca3d.com/).

Para obtener más información sobre RhinoCommon, consulte las [guías de RhinoCommon](/guides/rhinocommon/).

### Componentes de Grasshopper

Rhino ahora incluye Grasshopper, nuestro lenguaje de programación visual para diseño algorítmico y paramétrico.  Grasshopper es una plataforma de desarrollo en sí misma, con [cientos de componentes de Grasshopper de terceros](http://www.food4rhino.com/grasshopper-addons), para hacer todo tipo de cosas, desde [simulación física](http://www.food4rhino.com/project/kangaroo), hasta [creación de interfaces de usuario personalizadas](http://www.food4rhino.com/project/human-ui), pasando por [programación y control de robótica industrial](http://www.food4rhino.com/project/hal).

Para obtener más información sobre Grasshopper, y más concretamente sobre el desarrollo de componentes de Grasshopper, consulte las [guías de Grasshopper](/guides/grasshopper/).

### Scripts de Python

Uno de los plugins .NET que se incluye con Rhino es RhinoPython.  Escrito con [IronPython](http://ironpython.net/), una implementación .NET del runtime de [Python](https://www.python.org/), RhinoPython expone todo el SDK de RhinoCommon al lenguaje de programación de Python.  Esto significa que cada vez que añadimos una función a RhinoCommon, aparece automáticamente en RhinoPython.

Para obtener más información sobre RhinoPython, consulte las [guías de RhinoPython](/guides/rhinopython/).

## Temas relacionados

- [Guías de C/C++](/guides/cpp/)
- [Guías de openNURBS](/guides/opennurbs/)
- [Guías de RhinoScript](/guides/rhinoscript/)
- [Microsoft .NET Framework (en microsoft.com)](https://dotnet.microsoft.com/es-es/apps/desktop)
- [¿Qué es RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon)
- [Guías de RhinoCommon](/guides/rhinocommon/)
- [Qué son Mono y Xamarin](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Proyecto Mono](https://www.mono-project.com)
- [Eto.Forms en GitHub](https://github.com/picoe/Eto)
- [Guías de Grasshopper](/guides/grasshopper/)
- [Guías de RhinoPython](/guides/rhinopython/)

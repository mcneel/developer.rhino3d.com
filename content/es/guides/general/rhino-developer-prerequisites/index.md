+++
aliases = ["/en/5/guides/general/rhino-developer-prerequisites/", "/en/6/guides/general/rhino-developer-prerequisites/", "/en/7/guides/general/rhino-developer-prerequisites/", "/en/wip/guides/general/rhino-developer-prerequisites/"]
authors = [ "dan", "callum" ]
categories = [ "Getting Started" ]
description = "Esta guía describe los principales requisitos para desarrollar en Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Requisitos previos para desarrolladores"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/learningresources"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++


Hay una serie de requisitos previos necesarios para desarrollar en Rhino.  A grandes rasgos, pueden dividirse en tres categorías, clasificadas en orden ascendente de dificultad:

1. [Requisitos de hardware](#hardware)
1. [Requisitos previos de software](#software)
1. [Conocimientos de programación](#programming-knowledge)

## Hardware

Si está leyendo esta guía, es probable que ya tenga un equipo en el que puede ejecutar Rhino. (Si no es así, Rhino tiene unos [requisitos mínimos del sistema](http://www.rhino3d.com/system_requirements/) que debería revisar antes de adquirir cualquier hardware).  En general, cualquier equipo que pueda ejecutar Rhino *debe* poder ejecutar las herramientas de desarrollo descritas en la sección [Software](#software) .

Si es usuario de Windows y desea desarrollar plugins para Rhino para Mac, necesitará un Mac de Apple.  Por el contrario, si es usuario de macOS y desea desarrollar para Rhino para Windows, necesitará un equipo que pueda ejecutar Rhino para Windows (las máquinas virtuales que ejecutan Windows en macOS pueden funcionar perfectamente).


## Software

Según lo que quiera hacer, los requisitos previos del software varían.  En general, necesitará:

- [Rhinoceros](http://www.rhino3d.com/download)
- Un editor de código.  Hay muchas opciones... aquí tiene algunas:
   - [Visual Studio para Windows](https://www.visualstudio.com): El principal entorno de desarrollo integrado (IDE) de Microsoft para Windows.
   - [Visual Studio Code](https://code.visualstudio.com/): El mejor editor multiplataforma gratuito

Consulte las [guías específicas de SDK](/guides/) para conocer los requisitos previos de software, que normalmente se encuentran en las guías *"Instalación de herramientas"* .

## Conocimientos de programación

Adquirir conocimientos de programación es el requisito previo más exigente.  Sin embargo, aprender a programar, incluso probar un nuevo lenguaje, es divertido y enriquecedor.  Aprender a programar con Rhino es una buena manera de empezar...

### Aprender C# .NET

Si desea escribir plugins con RhinoCommon, tendrá que entender un lenguaje de programación compatible con .NET como C# (o VB).  Recomendamos [C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)) (C Sharp) porque es moderno, seguro y fácil de aprender (y puede desarrollar en C# tanto en Windows como en macOS).

*Vea*...

- [Beginning C# Programming](http://shop.oreilly.com/product/0636920036036.do) por Eric Lippert, publicado por O'Reilly Media
- [C# Fundamentals for Absolute Beginners](https://learn.microsoft.com/en-us/shows/csharp-fundamentals-for-absolute-beginners/) en la Academia Virtual de Microsoft.
- [C# and .NET Essential Training](https://www.linkedin.com/learning/c-sharp-and-dot-net-essential-training) en LinkedIn Learning

*Lea*...

- [Programming C# 5.0](http://shop.oreilly.com/product/0636920024064.do) por Ian Griffiths, publicado por O'Reilly Media
- [C# 5.0 in a Nutshell](http://shop.oreilly.com/product/0636920023951.do) por Joseph Albahari, Ben Albahari, publicado por O'Reilly Media

*Haga*...

- [Vea muestras](/samples/#rhinocommon) en este sitio web
- [Pida ayuda en Discourse](http://discourse.mcneel.com/c/rhino-developer)

### Aprender C/C++

Para escribir plugins para Rhino con el SDK de C/C++, primero tiene que aprender el lenguaje de programación [C++](https://en.wikipedia.org/wiki/C%2B%2B) .  C/C++ a veces se considera un lenguaje de programación "avanzado".

*Vea*...

- [C++: A General Purpose Language](https://learn.microsoft.com/en-us/shows/cplusplus-language-library/) en Microsoft Virtual Academy
- [C++ Essential Training](https://www.linkedin.com/learning/c-plus-plus-essential-training-15106801) con Bill Weinmann en LinkedIn Learning

*Lea*...

- [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language) por Ian Kernighan y Dennis Ritchie
- [Practical C++ Programming](http://shop.oreilly.com/product/9780596004194.do) por Steve Oualline, publicado por O'Reilly Media
- [C++ Primer Plus](http://www.amazon.com/Primer-Plus-Edition-Developers-Library/dp/0321776402) por Stephen Prata

*Haga*...

- [Vea muestras](/samples/#cc) en este sitio web
- [Pida ayuda en Discourse](http://discourse.mcneel.com/c/rhino-developer)

### Aprenda Python

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) es un primer lenguaje fantástico y un lenguaje adicional muy flexible para añadir a su conjunto de herramientas.

*Vea*...

- [Google's Python Class](https://developers.google.com/edu/python/) por Google for Education
- [Up and Running with Python](http://www.lynda.com/Python-tutorials/Up-Running-Python/122467-2.html) con Joe Marini en Lynda.com


*Lea*...

- [The Python Tutorial](https://docs.python.org/2/tutorial/index.html)
- [RhinoPython Primer](http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101) por Skylar Tibbits, Arthur van der Harten, Steve Baer y David Rutten.
- [The Python Tutorial](https://docs.python.org/2/tutorial/index.html) por Python Software Foundation
- [Learn Python the Hard Way](http://learnpythonthehardway.org/book/) por Zed A. Shaw (a pesar del título, se trata de un libro para principiantes).
- [Automate The Boring Stuff With Python](https://automatetheboringstuff.com/) por Al Sweigart

*Haga*...

- [Vea muestras](/samples/#rhinopython) en este sitio web
- [Pida ayuda en Discourse](http://discourse.mcneel.com/c/scripting)

### Aprenda RhinoScript

RhinoScript es una herramienta de programación basada en el lenguaje VBScript de Microsoft.  RhinoScript se ejecuta en Rhino para Windows.

*Lea*...

- [RhinoScript Primer](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101) por David Rutten
- [Microsoft VBScript User's Guide and Language Reference](https://msdn.microsoft.com/en-us/library/t0aew7h6(VS.85).aspx)

*Haga*...

- [Vea muestras](/samples/#rhinoscript) en este sitio web
- [Pida ayuda en Discourse](http://discourse.mcneel.com/c/scripting)

### Más información

- [Crafting Interpreters](https://craftinginterpreters.com/) por Robert Nystrom
- [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) por Robert C. Martin


## Temas relacionados

- [¿Qué es un plugin de Rhino?](/guides/general/what-is-a-rhino-plugin/)
- <a href="https://en.wikipedia.org/wiki/C_Sharp_(programming_language">C Sharp en Wikipedia</a>
- [C++ en Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B)
- [Python en Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))

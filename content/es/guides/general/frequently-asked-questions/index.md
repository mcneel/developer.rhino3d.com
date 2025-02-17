+++
aliases = ["/en/5/guides/general/frequently-asked-questions/", "/en/6/guides/general/frequently-asked-questions/", "/en/7/guides/general/frequently-asked-questions/", "/en/wip/guides/general/frequently-asked-questions/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "Esta guía contiene una lista de preguntas frecuentes (FAQ)."
keywords = [ "developer", "rhino", "faq" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Preguntas frecuentes"
type = "guides"
weight = 4
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptspage"
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


**¿Qué SDK me conviene más?**

Todo depende de lo que quiera hacer.  Si desea automatizar tareas repetitivas en Rhino, lo mejor es escribir un script de [Python](/guides/#rhinopython) .  Si desea escribir un plugin o componente de Grasshopper completo, le recomendamos el [SDK de RhinoCommon](/guides/rhinocommon/what-is-rhinocommon/).  Si domina C/C++, debería considerar el SDK nativo de C/C++ (solo compatible con Rhino para Windows).

**¿Puedo escribir plugins que funcionen tanto en Windows como en Mac?**

Sí... incluso utilizando [el mismo código](/guides/rhinocommon/what-is-rhinocommon/).

**¿Qué son Mono y Xamarin?**

Mono es una versión de código abierto del tiempo de ejecución .NET de Microsoft que funciona en Linux, macOS, iOS y Android.  Consulte la guía [¿Qué son Mono y Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/) para obtener más información.

**¿Qué son las macros?**
Las macros son cadenas de comandos y opciones de comandos de Rhino que permiten crear una secuencia automatizada de operaciones.  Esta macro (secuencia) puede repetirse pulsando un botón de la barra de herramientas o escribiendo un alias.

**¿Qué son los scripts?**
Para tareas más complejas, las macros son insuficientes.  Carecen de la capacidad de realizar cálculos complejos, almacenar y recuperar datos, analizar esos datos y tomar decisiones condicionales, o profundizar en el funcionamiento interno de Rhino.  Para ello, se necesita una verdadera herramienta de programación.  La más sencilla y accesible es Python, que también incluye su versión de la sintaxis de RhinoScript.  Cuando hablamos de scripts solemos referirnos a funciones escritas con RhinoScript o Python.

**¿Qué son los plugins?**
Los plugins son herramientas aún más sofisticadas: son programas informáticos compilados que pueden integrarse en Rhino.  Pueden ser desde simples funciones de scripts hasta complejos programas completos para renderizado, animación, mecanizado, etc.

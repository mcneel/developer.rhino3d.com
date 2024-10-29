+++
aliases = ["/es/5/guides/general/developing-software-in-public/", "/es/6/guides/general/developing-software-in-public/", "/es/7/guides/general/developing-software-in-public/", "/es/wip/guides/general/developing-software-in-public/"]
authors = ["brian" ]
categories = [ "Overview" ]
description = "Información general del proceso de desarrollo de Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Desarrollo de software público"
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

En los últimos 20 años hemos desarrollado un proceso que nos ayuda a satisfacer a nuestros clientes.  Este proceso consta de ocho partes, todas ellas igualmente importantes.  Durante años, hemos creado nuestras propias herramientas para facilitar la mayor parte de este proceso.  Pero ahora existen excelentes herramientas comerciales que os animamos a utilizar.

Nuestro proceso de desarrollo de software, al igual que los demás procesos, es un ciclo.  Así que podemos empezar en cualquier fase.

![Ciclo de desarrollo de Rhino](/images/developing-software-in-public-01.png)

## El ciclo

Como esta guía es para desarrolladores, empecemos por escribir código.

### Escribir código

Escribir código es lo que nosotros, como desarrolladores de software, pasamos mucho tiempo haciendo. Tenemos nuestro IDE favorito abierto, escribimos código, depuramos, resolvemos problemas. No conocemos a ningún desarrollador de software al que no le guste resolver problemas.

Cuando tenemos algo, lo enviamos (*commit*) a nuestro sistema de control de versiones...

### Enviar

Enviamos código a un [Sistema de control de versiones](https://es.wikipedia.org/wiki/Control_de_versiones). En nuestro caso, utilizamos [git](https://git-scm.com/) con [GitHub](https://github.com/).  Existen muchos otros sistemas de control de versiones.  Antes usábamos [Subversion](https://subversion.apache.org/), pero ahora usamos [GitHub](https://github.com/).  [GitHub](https://github.com/) es compatible con muchas otras herramientas y tiene una API muy completa.  Pero hay otros que se pueden tener en cuenta: [BitBucket](https://bitbucket.org), [Mercurial](https://www.mercurial-scm.org/), etc.

Si no utiliza ningún control de versiones, por favor, empiece ya.  Ahora es muy fácil.  Permite volver a otras versiones del software antes de introducir un problema.  Ayuda a colaborar en equipo.  Es necesario para cualquier tipo de automatización de la compilación.  ¿Hemos mencionado que es fácil?

Como desarrolladores, utilizamos una versión modificada de [GitHub Flow](https://guides.github.com/introduction/flow/) para crear y fusionar solicitudes de extracción (*pull requests*) en nuestra rama principal (*master branch*).

Después de enviar el código, lo compilamos...

### Compilar

Además de compilar en nuestros escritorios, tenemos servidores dedicados de [TeamCity](https://www.jetbrains.com/teamcity/) que compilan constantemente el código y verifican que funciona en la rama *master* en [GitHub](https://github.com/).  Así nos aseguramos de que no haya errores y todos los demás puedan obtener el código más reciente y compilar.

Estos servidores [TeamCity](https://www.jetbrains.com/teamcity/) verifican cada envío (*commit*) y también crean nuestras versiones diarias cada cuatro horas aproximadamente. También crean nuestras versiones públicas WIP y Service Release.

Con cada nueva compilación, realizamos pruebas (*test*)...

### Probar

Cuando los desarrolladores corrigen errores y solucionan problemas, nuestro personal interno de pruebas se asegura de que la versión pública funcione correctamente.  También confiamos en nuestros clientes para probar las versiones WIP y Release Candidate.

Las pruebas se realizan antes y después del siguiente paso: publicar (*publish*)...

### Publicar

Cuando tenemos una compilación lista para enviar a los clientes, la implementamos (o publicamos).

Esto incluye la publicación de...

- [Instaladores descargables](http://www.rhino3d.com/download)
- [SDK](http://developer.mcneel.com)
- Documentación (este sitio web)

...y el envío de anuncios públicos por correo electrónico, blogs y redes sociales.

### Escuchar

Escuchamos de todas las formas posibles:

- [Chat](http://www.rhino3d.com/support#)
- [Correo electrónico](mailto:tech@mcneel.com)
- Soporte telefónico +34 933 199 002
- [Foro (Discourse)](https://discourse.mcneel.com/)

Y a menudo, cuando escuchamos, encontramos problemas que hay que solucionar.  A veces son pequeños... a veces son ENORMES.  Siempre registramos un problema...

### Registrar

Registramos los problemas en [YouTrack](https://mcneel.myjetbrains.com) y hacemos seguimiento.

[YouTrack](https://mcneel.myjetbrains.com) nos funciona bien porque nos ayuda a garantizar que cada problema se prueba y documenta adecuadamente.

### Priorizar

Averiguar cuáles son las prioridades es DIFÍCIL.  Hablamos con nuestros clientes.  Hablamos entre nosotros.  Utilizamos Gmail, Google Drive y Google Docs para comunicarnos.  Chateamos 24 horas al día en [Slack](https://slack.com/).

Nos reunimos los martes de cada semana.  Antes de reunirnos, compartimos lo que hemos hecho en un Google Doc. En ese documento, compartimos los objetivos de cada producto que vamos a lanzar y cada grupo de funciones en las que estamos trabajando, incluimos gráficos de nuestro progreso y enlaces a nuestros problemas [YouTrack](https://mcneel.myjetbrains.com), y recibimos informes verbales de persona que trabaja en las funciones.

Además, cada desarrollador escribe en qué ha estado trabajando, qué tiene previsto hacer a continuación y qué le impide completar su trabajo.

### Automatizar

Y por último, pero no por ello menos importante, hacemos MUCHA automatización.

Algunas de las cosas que automatizamos:

- Compilar cada envío o *commit* de cada desarrollador antes de que pase a la rama *master* de desarrollo.
- Cerrar incidencias en [YouTrack](https://mcneel.myjetbrains.com) cuando los servidores de [TeamCity](https://www.jetbrains.com/teamcity) fusionan las correcciones en nuestra rama *master* de desarrollo.
- Compilar versiones internas y públicas en nuestros servidores de [TeamCity](https://www.jetbrains.com/teamcity).
- Publicar nuevas versiones WIP escribiendo un comando en [Slack](https://slack.com/).
- Subir versiones públicas a nuestros servidores de descarga.

## En público

Hasta hace poco, estas son las partes de nuestros procesos que hemos hecho públicas:

- Probar
- Publicar (al menos se ve lo que publicamos)
- Escuchar

Y en los últimos dos años, hemos hecho público nuestro gestor de incidencias al cambiar a YouTrack. Algunas cuestiones las ocultamos al público por motivos de seguridad o privacidad de los usuarios.

Lo que nos gustaría hacer pronto es hacer aún más pública esta información:

- Compartir parte de nuestro código como repositorios públicos en GitHub para que los desarrolladores tengan ejemplos de código reales con los que trabajar.
- Permitir a los desarrolladores compartir correcciones y mejoras de nuestro código.
- Facilitar la creación de proyectos de plug-ins publicando RhinoCommon como paquete NuGet.
- Ayudar en la automatización de compilaciones cuando sea necesario.

## Temas relacionados

- [Información general de la tecnología de Rhino](/guides/general/rhino-technology-overview)
- [Contribuir](/guides/general/contributing)
- [Requisitos previos para desarrolladores](/guides/general/rhino-developer-prerequisites)
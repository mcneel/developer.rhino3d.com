+++
aliases = ["/en/5/guides/general/what-is-a-rhino-plugin/", "/en/6/guides/general/what-is-a-rhino-plugin/", "/en/7/guides/general/what-is-a-rhino-plugin/", "/en/wip/guides/general/what-is-a-rhino-plugin/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "Esta guía describe qué es un plugin de Rhino y de qué tipo son."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "¿Qué es un plugin de Rhino?"
type = "guides"
weight = 3
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/developer/whatisarhinoplugin"
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


Un plugin de Rhino es un módulo de software que amplía la funcionalidad de Rhino o Grasshopper añadiendo comandos, características o capacidades.  Un plugin de Rhino es una biblioteca de vínculos dinámicos, o DLL.

En Windows, un plugin de Rhino creado con el [SDK C/C++](/guides/cpp/what-is-the-cpp-sdk/) es una DLL normal que utiliza la DLL de MFC compartida.

En Windows y Mac, un plugin de Rhino creado con el [SDK de RhinoCommon](/guides/rhinocommon/what-is-rhinocommon/) es un ensamblaje .NET.

Algunos ejemplos de plugins de Rhino son [Grasshopper](http://www.grasshopper3d.com), [Brazil](http://brazil.rhino3d.com/), [Flamingo](http://nxt.flamingo3d.com/) y [Bongo](http://bongo.rhino3d.com/).  Consulte [food4rhino.com](http://www.food4rhino.com/) para obtener más información.


## Tipos de plugins

Rhino admite cinco tipos diferentes de plugins:

1. *Utilidad general*: Utilidad de propósito general que puede contener uno o más comandos.
1. *Importación de archivos*: Importa datos de otros formatos de archivo en Rhino; puede admitir más de un formato.
1. *Exportación de archivos*: Exporta datos de Rhino a otros formatos de archivo; puede admitir más de un formato.
1. *Renderizado personalizado*: Aplica materiales, texturas y luces a una escena para producir imágenes renderizadas.
1. *Digitalización 3D*: Interfaces con dispositivos de digitalización 3D, como los fabricados por MicroScribe, Faro y Romer.

***Nota***: Los plugins de Importación de archivos, Exportación de archivos, Renderizado personalizado y Digitalización 3D son mejoras especializadas del plugin de Utilidad general.  Así, todos los tipos de plugin pueden contener uno o más comandos.


## Compatibilidad de plugins

Para que Rhino cargue y ejecute correctamente su plugin, deben cumplirse varias condiciones:

1. El número "RhinoSdkVersion" de su plugin debe coincidir con el número "RhinoSdkVersion" de Rhino.
1. El número "RhinoSdkServiceRelease" de Rhino debe ser mayor o igual que el número "RhinoSdkServiceRelease" de su plugin.

Ocasionalmente realizamos cambios en nuestros SDK.  Cuando lo hacemos, cambiamos el número de "RhinoSdkServiceRelease".  

Como desarrollador de plugins, es poco probable que encuentre un problema con la primera condición.  Esto ocurriría, por ejemplo, si un usuario intentara cargar un plugin creado para Rhino 6 en Rhino 4.

Sin embargo, en ocasiones puede tener problemas con la segunda condición.  Si ha compilado su plugin utilizando el SDK 6.2 (RhinoSdkVersion.RhinoSdkServiceRelease) y un usuario con Rhino 6.1 intenta ejecutarlo, recibirá un mensaje de error y el plugin no se cargará.  Si su cliente recibe este mensaje, necesita obtener la última versión de Rhino (podría ser la 6.2 o una superior en este ejemplo) y así se resuelve el problema.

## Temas relacionados

- [Requisitos previos para desarrolladores](/guides/general/rhino-developer-prerequisites)

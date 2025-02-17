+++
aliases = ["/en/5/guides/general/rhino-installer-engine/", "/en/6/guides/general/rhino-installer-engine/", "/en/7/guides/general/rhino-installer-engine/", "/en/wip/guides/general/rhino-installer-engine/"]
authors = [ "brian", "will" ]
categories = [ "Fundamentals" ]
description = "Esta guía es una breve introducción al motor de instalación de Rhino."
keywords = [ "developer", "rhino", "installer" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Motor de instalación de Rhino"
type = "guides"
weight = 6
override_last_modified = "2021-07-27T08:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinoinstallerengine/overview"
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

{{< call-out "warning" "Warning" >}}
⚠️ Esta tecnología está obsoleta a partir de Rhino 7 y ha sido sustituida por el formato <a href="/guides/yak/">yak junto con el administrador de paquetes.</a>
{{< /call-out >}}

## Información general (Windows)

El motor de instalación de Rhino simplifica la distribución, instalación y actualización de plugins de Rhino para Windows.

## Cómo funciona

### Estructura de archivos y carpetas

Un paquete del instalador de Rhino es un archivo zip con extensión *.rhi* . El paquete puede incluir más de una versión de un plugin, pero todas las versiones deben compartir el mismo GUID (es decir, son versiones diferentes del _mismo_ plugin).

No hay requisitos de estructura de archivos ni de nomenclatura. Por ejemplo, los dos paquetes siguientes son funcionalmente equivalentes. Ambos contienen versiones de "Marmoset", un plugin C++ ficticio compilado para Rhino 5 (32 y 64 bits) y Rhino 6[^1].

```
Marmoset_tree.rhi/
├── Rhino 6/
│├── Marmoset.rhp
│├── Marmoset.dll
│└── Marmoset.rui
└── Rhino 5.0/
    ├── x86/
    │   ├── Marmoset.rhp
    │   └── ...
    └── x64/
        ├── Marmoset.rhp
        └── ...
```

```
Marmoset_flat.rhi/
├── Marmoset_rhino6.rhp
├── Marmoset_rhino5_x86.rhp
├── Marmoset_rhino5_x64.rhp
├── Marmoset_rhino6.dll
├── ...
└── Marmoset.rui
```

Puede incluir todo lo que desee en el paquete *.rhi*: DLL de soporte, archivos de ayuda, documentación, archivos de [barras de herramientas (*.rui*)](/guides/rhinocommon/create-deploy-plugin-toolbar.md), etc. Todo el contenido se descomprime en un directorio de la máquina del usuario.

### Instalación y compatibilidad

El motor del instalador de Rhino examina cada archivo *.rhp* y extrae el GUID del plugin, el título, la versión, el SDK utilizado (por ejemplo, RhinoCommon, C++) y la versión del SDK. Esta información se utiliza para determinar qué versión del plugin se instalará para qué versión instalada de Rhino para Windows; el plugin compatible más reciente se registra con la versión correspondiente de Rhino. Los plugins de RhinoCommon compilados como `AnyCPU` se instalarán para Rhino 5 de 32 y 64 bits[^1].

{{< call-out "note" "Note" >}}
<strong>Desde Rhino 6:</strong> si se encuentra un plug-in de RhinoCommon que se ha compilado con una versión _principal_ de Rhino anterior a la instalada, se realizará una comprobación exhaustiva de compatibilidad para determinar si el SDK del Rhino instalado aún admite la funcionalidad utilizada por el plugin. Si la comprobación es correcta, se instalará el plugin obsoleto.
{{< /call-out >}}

## Limitaciones

- El motor de instalación de Rhino copiará los archivos del archivo *.rhi* y registrará los plugins que encuentre. No se realiza ninguna otra ejecución.
- Actualmente, no es posible firmar digitalmente los archivos *.rhi* para verificar la fuente de los archivos *.rhi* .
- El motor de instalación de Rhino está disponible con Rhino 5 y versiones posteriores.

## Temas relacionados

- [Instaladores de plugins (Windows)](/guides/rhinocommon/plugin-installers-windows)
- [Instaladores de plugins (Mac)](/guides/rhinocommon/plugin-installers-mac)

**Notas a pie de página**

[^1]: Since version 6 Rhino for Windows has been 64-bit only.

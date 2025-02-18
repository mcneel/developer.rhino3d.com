+++
aliases = ["/en/8/guides/general/rhino-ui-system/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "Esta guía describe el sistema de interfaz de usuario de Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "El sistema de interfaz de usuario de Rhino"
type = "guides"
weight = 3
override_last_modified = "2023-11-20T08:29:10Z"

[admin]
TODO = ""
origin = ""
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

Esta guía muestra una visión general del sistema de interfaz de usuario (UI) de Rhino y compara el nuevo sistema de Rhino 8 con el sistema anterior de Rhino 7 y versiones anteriores.

## Sistema de interfaz de usuario Rhino 8

Los objetivos del nuevo sistema de interfaz de usuario de Rhino 8 eran:

- Mostrar paneles y barras de herramientas en el mismo contenedor.
- Barras de herramientas y macros de referencia desde múltiples fuentes sin tener que copiar definiciones de un archivo RUI a otro.
- Realizar cambios en la interfaz de usuario de Rhino (RUI) sin sobrescribir ni reemplazar los archivos existentes en las service releases de Rhino o de plug-ins. (En versiones anteriores de Rhino, el reemplazo del archivo RUI para obtener barras de herramientas y macros actualizadas provocaba que los cambios de usuario en los archivos RUI se sobrescribieran.)
- Cambiar rápidamente la interfaz de usuario de Rhino para mostrar herramientas orientadas a tareas.
- Compartir diseños de interfaz de usuario entre los usuarios.
- Permitir a los usuarios modificar arbitrariamente la interfaz de usuario sin tener conocer la ubicación o el origen de un componente de interfaz de usuario y realizar un seguimiento automático de los cambios.
- Proporcionar una interfaz de usuario unificada de Windows y Mac.

Los principales cambios en el nuevo sistema de interfaz de usuario de Rhino 8 son:

- Los grupos de barras de herramientas han sido reemplazados por contenedores. Los contenedores pueden mostrar tanto paneles como barras de herramientas.
- Los archivos RUI se utilizan para proporcionar librerías de barras de herramientas y macros, y ya no se modifican directamente. Rhino rastrea los cambios de RUI y los aplica al cargar. Al hacerlo, Rhino muestra los archivos RUI actualizados sin perder cambios de usuario en una barra de herramientas o macro.
- Se han agregado diseños de ventana y se pueden usar para cambiar rápidamente entre diferentes configuraciones de interfaz de usuario. Se pueden exportar como archivos e incluirán modificaciones en barras de herramientas y macros y archivos RUI del usuario.
- La importación de un diseño de ventana extraerá los archivos RUI del usuario según sea necesario y aplicará modificaciones de RUI.

El nuevo sistema de interfaz de usuario de Rhino 8 está diseñado para permitir la referencia de componentes de interfaz de usuario de muchas fuentes: paneles, barras de herramientas y macros, definidos por cualquier archivo o plug-in RUI.  Cuando Rhino se cierra, los cambios en la interfaz de usuario se guardan y los archivos RUI originales nunca se modifican a menos que se solicite específicamente. Las configuraciones de los diseños de interfaz de usuario se pueden guardar, restaurar, exportar e importar como diseños de ventana y compartir entre Windows y Mac.

### Contenedores

Los contenedores pueden mostrar referencias tanto a paneles como a barras de herramientas. Las barras de herramientas pueden ser referenciadas desde cualquier fuente válida de RUI. Los elementos se muestran como una pestaña en un contenedor. Los contenedores pueden estar visibles u ocultos.

Los contenedores se pueden modificar arrastrando las pestañas de un contenedor a otro, o haciendo clic en el menú de "Engranaje" del contenedor para agregar o eliminar referencias a paneles o barras de herramientas. El mismo panel puede ser referenciado por múltiples contenedores, lo que significa que es posible tener la pestaña "Capas", por ejemplo, mostrada en múltiples contenedores.

Las definiciones de contenedor, visibilidad, ubicación y tamaño se guardan cuando Rhino se cierra y se restauran al reiniciar Rhino. Esta información también puede almacenarse y compartirse a través de los diseños de ventana.

Los contenedores se pueden gestionar con el comando **[Contenedores](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/containers.htm#(null))** de Rhino.

### Diseños de ventanas

Los diseños de ventanas son una instantánea de las definiciones de los contenedores, los estados de visibilidad, las ubicaciones y el tamaño. Al restaurar un diseño de ventana se reconfigurará la interfaz de usuario actual para que aparezca como cuando se creó el diseño. Los contenedores restaurados mostrarán las pestañas en el orden en que estaban cuando se creó el diseño de la ventana y aparecerán en la misma ubicación y tamaño. Las pestañas de la barra de herramientas harán referencia a la definición actual de una barra de herramientas; si la barra de herramientas ya no existe, la pestaña no se mostrará.

Los diseños de ventana se pueden gestionar con el comando **[DiseñoDeVentanas](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/windowlayout.htm#(null))** de Rhino.

#### Exportación e importación de diseños de ventanas

Los diseños de ventana se pueden exportar a un archivo de diseño de ventana de Rhino (RHW). Los archivos RHW exportados incluyen los archivos RUI personalizados referenciados y los cambios asociados a todos los archivos RUI en el momento de la creación del archivo RHW.

Al importar un archivo RHW se comprobará si hay abierto un archivo RUI personalizado incrustado. Si el archivo no está abierto, se extrae el archivo personalizado y se abre. Una vez extraída o verificada la lista personalizada, los cambios de RUI guardados en el archivo RHW se aplicarán a los archivos RUI actuales. Se ignorará la información de cambios asociada a barras de herramientas definidas por archivos de plugins que no existan. Una vez restaurados los datos RUI, los contenedores se crearán o modificarán para que coincidan con la definición almacenada en el archivo RHW. Se ignorarán los contenedores que solo hagan referencia a barras de herramientas de plugins que no estén instalados. Una vez importado, el diseño aparecerá en la lista de diseños de ventanas y podrá restaurarse.

Los diseños de ventana se pueden exportar e importar con el comando **[DiseñoDeVentanas](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/windowlayout.htm#(null))** de Rhino.

### Archivos RUI

En Rhino 8, los archivos RUI ahora simplemente son una colección de barras de herramientas, macros e imágenes. Estos archivos están pensados para proporcionar librerías de barras de herramientas que puedan ser referenciadas por los contenedores. Los cambios en las barras de herramientas y las macros ahora se pueden entregar con las actualizaciones de Rhino y de los plugins. Las nuevas barras de herramientas definidas en la librería RUI actualizada aparecerán automáticamente en la lista de comandos de la barra de herramientas. Los botones añadidos o eliminados de una barra de herramientas se añadirán o eliminarán en la referencia de la barra de herramientas.

Los grupos de barras de herramientas definidos en archivos RUI se convierten en contenedores cuando se cargan para admitir archivos RUI heredados y de plugins y proporcionar a un archivo RUI de plugin una forma de crear contenedores asociados con el plugin.

Los archivos RUI vinculados se pueden gestionar mediante la opción **[Opciones > Apariencia > Barras de herramientas](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#options/appearance_toolbars.htm#(null))** de Rhino.

### Barras de herramientas

Las barras de herramientas son conjuntos de botones. Los botones de las barra de herramientas hacen referencia a macros que pueden proceder de cualquier fuente RUI válida. Las barras de herramientas se muestran como pestañas en un contenedor.

#### Grupos de barras de herramientas

Los grupos de barras de herramientas se convierten ahora en contenedores cuando se cargan por primera vez. Existen como forma de dar soporte a los archivos RUI heredados. Los grupos también pueden ser utilizados por los desarrolladores de plugins para proporcionar definiciones de contenedores asociados a un plugin.

#### Barra de herramientas

Las barras de herramientas son conjuntos de botones de barras de herramientas y pueden ser referenciadas por múltiples contenedores. Pueden modificarse arrastrando y soltando botones de otras barras de herramientas o utilizando el asistente para nuevos botones.

Las barras de herramientas se pueden gestionar con el comando **[BarraDeHerramientas](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/toolbar.htm#(null))** de Rhino.

#### Botón de barra de herramientas

Los botones de las barra de herramientas pueden contener acciones de clic con el botón izquierdo y/o derecho del ratón. Las acciones de clic con el botón izquierdo y derecho del ratón se asignan a macros que contienen un script que se ejecuta al hacer clic. Los botones de las barras de herramientas muestran la imagen asociada a la macro asignada a la acción del botón izquierdo del ratón si está presente, si no se utiliza la imagen de la macro del botón derecho.

#### Menús

El sistema de menús de Rhino puede ampliarse utilizando objetos de menú definidos en un archivo RUI. El archivo RUI contiene información de ubicación que describe dónde insertar un elemento en el sistema de menús. Los nuevos elementos de menú se definen haciendo referencia a una macro que contiene:

- Texto del menú.
- Imagen del menú.
- Texto de ayuda que se muestra en la barra de estado cuando el ratón está sobre un elemento del menú.
- Script de comando que se ejecuta cuando se hace clic en el elemento del menú.

Los menús se pueden gestionar con el comando **[Menús](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#toolbarsandmenus/workspace_editor.htm#(null))** de Rhino.

#### Macro

Las macros contienen la información necesaria para describir el script de comandos que se ejecuta cuando se ejecuta la macro. Entre las definiciones macro se incluyen las siguientes:

- Nombre
- Imagen, versiones en modo claro y oscuro
- Script de comando
- Texto del botón
- Información sobre el botón
- Texto del menú
- Texto de ayuda

Las macros se pueden gestionar con el comando **[Macros](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/macros.htm#(null))** de Rhino.

### Paneles

Los paneles son formas de interfaz de usuario no modales creados por Rhino o por plugins. Pueden aparecer en cualquier contenedor como una pestaña, y pueden moverse entre contenedores arrastrándolos y soltándolos.

Los paneles pueden ser referenciados por varios contenedores, pero no pueden aparecer en el mismo contenedor más de una vez.

## Sistema de interfaz de Rhino anterior

El sistema de interfaz de usuario de Rhino, que se encuentra en Rhino para Windows versión 7 y anteriores, consta de lo siguiente:

### Barras de herramientas

Las barras de herramientas de Rhino son conjuntos de botones de barras de herramientas. Los botones de barras de herramientas hacen referencia a macros que deben definirse en el mismo archivo RUI que la barra de herramientas. Los botones contienen: imagen, tooltip, texto de menú, texto de ayuda y script. Las barras de herramientas se muestran en grupos de barras de herramientas.

### Grupo de barras de herramientas

Los grupos de barras de herramientas son conjuntos de referencias a barras de herramientas del mismo archivo RUI. Al arrastrar una barra de herramientas de un archivo a un grupo de otro archivo, la barra de herramientas y sus macros referenciadas se copian del archivo de origen al de destino. Los grupos de barras de herramientas no pueden hacer referencia a paneles de Rhino.

### Barra de herramientas

Las barras de herramientas son conjuntos de botones de barras de herramientas y solo se referencian y muestran por grupos de barras de herramientas.

### Botón de barra de herramientas

Los botones de las barra de herramientas pueden contener acciones de clic con el botón izquierdo y/o derecho del ratón. Las acciones de clic del ratón se asignan a macros que contienen un script que se ejecuta al hacer clic. Los botones de las barras de herramientas muestran la imagen asociada a la macro asignada a la acción del botón izquierdo del ratón si está presente, si no se utiliza la imagen de la macro del botón derecho.

Si se desea, los botones de las barras de herramientas pueden configurarse para que salgan temporalmente de otras barras de herramientas.

Los botones de las barras de herramientas solo pueden hacer referencia a macros del mismo archivo RUI que la barra de herramientas a la que pertenecen.

### Menú

El sistema de menús de Rhino puede ampliarse utilizando objetos de menú definidos en un archivo RUI. El archivo RUI contiene información de ubicación que describe dónde insertar un elemento en el sistema de menús. Los nuevos elementos de menú se definen haciendo referencia a una macro que contiene:

- Texto del menú.
- Imagen del menú.
- Texto de ayuda que se muestra en la barra de estado cuando el ratón está sobre un elemento del menú.
- Script de comando que se ejecuta cuando se hace clic en el elemento del menú.

### Macro

Las macros contienen la información necesaria para mostrar o describir el script de comandos que se ejecuta cuando se ejecuta la macro. Entre las definiciones macro se incluyen las siguientes:
Imagen que se muestra en un botón de la barra de herramientas referenciado o en un elemento del menú.

- Información sobre el botón.
- Texto del botón.
- Texto del menú
- Texto de ayuda que se muestra en la barra de estado cuando el ratón está sobre un elemento del menú.
- Script de comando a ejecutar.

### Archivo RUI

Los archivos RUI son conjuntos de los elementos anteriores y se almacenan en un directorio en el que se puede escribir. Los elementos almacenados en un archivo RUI solo pueden hacer referencia a elementos definidos en el mismo archivo. Los cambios en los elementos del archivo se guardan automáticamente cuando se cierra Rhino. Puede abrir o cerrar archivos RUI o elegir manualmente guardar un archivo en cualquier momento. Se realiza una copia de seguridad de la versión actual de un archivo y los cambios se guardan en el nombre del archivo. Si un archivo se daña, puede borrarlo y cambiarle el nombre al archivo de copia de seguridad para intentar restaurar la versión anterior. Si el archivo de copia de seguridad está dañado, no se puede recuperar nada.

Los plugins de Rhino pueden instalar un archivo RUI con el mismo nombre que el plugin y se copiará en una ubicación con permisos de escritura y se abrirá automáticamente cuando se inicie Rhino. Esto permite que un plugin amplíe la interfaz de Rhino y que no se cargue hasta que se haga referencia a él.

Tenga en cuenta que todo lo anterior se puede gestionar con el comando **[BarrasDeHerramientas](https://docs.mcneel.com/rhino/7/help/en-us/index.htm#options/toolbars.htm#(null))** de Rhino 7.

### Paneles de Rhino

Los paneles de Rhino son definiciones de interfaz de usuario sin modelo creadas por el núcleo de Rhino o un plugin.

Los paneles se muestran en un conjunto de pestañas. Los conjuntos de fichas solo pueden contener referencias a paneles y un panel solo puede ser referenciado por un único conjunto. Mostrar un panel en un conjunto eliminará las referencias a ese panel desde cualquier otro conjunto.

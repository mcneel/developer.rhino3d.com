+++
aliases = ["/en/5/guides/compute/hops-component/", "/en/6/guides/compute/hops-component/", "/en/7/guides/compute/hops-component/", "/en/wip/guides/compute/hops-component/"]
authors = [ "steve", "scottd", "andy.payne" ]
categories = [ "Hops" ]
description = "Hops añade funciones a Grasshopper."
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "El componente Hops"
type = "guides"
weight = 3
override_last_modified = "2024-10-28T11:35:10Z"

[admin]
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

## Información general 


{{< image url="/images/hops-overview.png" alt="/images/hops-overview.png" class="image_center" width="100%" >}}

Hops es un componente para Grasshopper en Rhino 7 y Rhino 8 para Windows. Hops añade **funciones externas** a Grasshopper. Al igual que otros lenguajes de programación, las funciones permiten:

* Simplificar algoritmos complejos utilizando varias veces la misma función.
* Eliminar combinaciones de componentes duplicados colocando las combinaciones comunes en una función.
* Compartir documentos de Grasshopper con otros miembros del equipo.
* Hacer referencia a documentos de Grasshopper en varios proyectos.
* Resolver documentos externos en paralelo, acelerando potencialmente los grandes proyectos.
* Ejecutar de forma asíncrona cálculos de larga duración sin bloquear las interacciones entre Rhino y Grasshopper.

Las funciones de Hops se almacenan como documentos separados de Grasshopper. El componente Hops adaptará sus entradas y salidas a la función especificada. Durante el cálculo, Hops resuelve la definición en un proceso independiente y, a continuación, devuelve los resultados al documento actual.

## Cómo utilizar Hops <img src="/images/hops.svg" alt="Windows" class="guide_icon">

{{< vimeo 713836707 >}}

### Instalación de Hops:

Hay varias maneras de instalar Hops en su máquina.
  1. [Instale Hops](rhino://package/search?name=hops) (se iniciará Rhino)
  1. O escriba `AdministradorDePaquetes` en la línea de comandos de Rhino.
      1. A continuación, busque "Hops".
      1. Seleccione Hops y, a continuación, Instalar.

{{< image url="/images/hops-package-manager.png" alt="/images/hops-package-manager.png" class="image_center" width="100%" >}}

### Crear una función de Hops

Las funciones de Hops son documentos de Grasshopper con entradas y salidas especiales.

{{< image url="/images/hops_simple_function.png" alt="/images/hops_simple_function.png" class="image_center" width="100%" >}}

#### Definir entradas

Las entradas de Hops se crean mediante **Get Components**. Los componentes Get disponibles en Grasshopper se encuentran en *pestaña Params > grupo Util*:

{{< image url="/images/hops_context_getters1.png" alt="/images/hops_context_getters1.png" class="image_center" width="65%" >}}

El nombre del componente se utiliza para el nombre del parámetro de entrada de Hops. Así, en el ejemplo anterior, tenemos tres componentes Get Number con los nombres A, B y C. Cada uno de estos componentes Get se convierten en parámetros de entrada cuando Hops compila la definición.

{{< image url="/images/hops_getter_inputs.png" alt="/images/hops_getter_inputs.png" class="image_center" width="80%" >}}

Cada componente Get tiene un menú contextual (botón derecho del ratón) con varios ajustes.

{{< image url="/images/hops-get-component-menu.png" alt="/images/hops-get-component-menu.png" class="image_center" width="50%" >}}

* **Component Name** - Este es el nombre que se asignará a la entrada del componente Hops.
* **Prompt** - Esta entrada será la información sobre herramientas que se mostrará al pasar el ratón por encima de este parámetro en el componente Hops.
* **Enable/Disable** - Activa o desactiva este componente.
* **At Least** - Solo se utiliza para Grasshopper Player y define el número mínimo de valores a aceptar para esta entrada.
* **At Most** - Define el número máximo de valores a aceptar para esta entrada (por defecto = 1). Si este valor se establece en 1, el componente Hops tratará esta entrada como *Item Access*. Sin embargo, si este valor es más de uno (o no se establece) Hops tratará esta entrada como *List Access*.
* **Tree Access** - Define si se espera pasar un Data Tree a esta entrada. Esta entrada solo se utiliza en Hops y si se establece en True, entonces este valor sustituirá al valor *At Most* establecido anteriormente.
* **Minimum & Maximum** - Estas entradas opcionales solo se utilizan para Grasshopper Player y conectarán las entradas numéricas a estos límites.
* **Presets** - Esta entrada opcional solo se utiliza para Grasshopper Player y solo se encuentra en los componentes Get *String*, *Integer*y *Number*. Este cuadro de diálogo permite establecer una lista de opciones predefinidas que se mostrarán al usuario a través de la línea de comandos.

#### Definir las salidas

Las salidas de Hops pueden definirse mediante los componentes **Context Bake** o **Context Print**. El nombre del parámetro de entrada en cualquiera de los componentes Context se utilizará como nombre del parámetro de salida cuando se calcule Hops.

{{< image url="/images/hops_getter_outputs.png" alt="/images/hops_getter_outputs.png" class="image_center" width="67%" >}}

### Utilizar el componente Hops

1. Coloque el componente *Params Tab > Util Group > Hops component* de Grasshopper en el lienzo.
1. Haga clic con el botón derecho del ratón en el componente Hops y, a continuación, en Path.
1. Seleccione una función de Hops. Nota: puede tratarse de una definición de Grasshopper en su ordenador, en un ordenador remoto o en un punto de conexión REST.
1. El componente mostrará las entradas y salidas.
1. Utilice el nuevo componente como cualquier otro componente de Grasshopper.

{{< image url="/images/hops_multiplyadd.png" alt="/images/hops_multiplyadd.png" class="image_center" width="80%" >}}

### Nota sobre Hops para usuarios de macOS

El componente Hops funciona en tándem con una instancia local de un servidor [Rhino.compute](https://developer.rhino3d.com/guides/compute/) que, normalmente, se pone en marcha cada vez que se inicia Grasshopper. Sin embargo, este servidor no funcionará en macOS, lo que significa que hay otras dos opciones a considerar. Puede:

1. realizar una llamada REST API a un servidor remoto que se ejecuta en Windows.
1. realizar una llamada REST API a un ghhops_server python que se ejecute localmente.

La primera opción (realizar una llamada a un servidor Windows remoto) requerirá algunas modificaciones de configuración en la máquina remota. Para obtener más información sobre cómo configurar un servidor remoto, consulte la sección [Configuración de máquinas remotas](../hops-component/#remote-machine-configuration).

La segunda opción (hacer una llamada a un servidor python local) se trata con más detalle en la sección [Llamar a un servidor CPython](../hops-component/#calling-a-cpython-server).

## Configuración de Hops

### Configuración de la aplicación

La configuración de Hops controla cómo se ejecuta Hops a nivel de aplicación.  Está disponible a través del desplegable File > Preferences > Solver de Grasshopper.

{{< image url="/images/hops-preferences.png" alt="/images/hops-preferences.png" class="image_center" width="60%" >}}

* **Hops-Compute server URL** - Lista la dirección IP o URL de cualquier máquina remota o servidor de Compute.
* **API Key** - La clave API es una cadena de texto secreta para el servidor de computación y las aplicaciones que utilizan la API de computación, por ejemplo `b8f91f04-3782-4f1c-87ac-8682f865bf1b`. Es opcional si está realizando pruebas localmente, pero debería utilizarse en un entorno de producción. Es básicamente la forma en que el servidor de computación se asegura de que las llamadas a la API proceden únicamente de sus aplicaciones. Puede introducir cualquier cadena que sea única y secreta. Asegúrate de guardarla en un lugar seguro.
* **Max Concurrent requests** - Se utiliza para limitar el número de solicitudes activas en situaciones asíncronas. De este modo, Hops no realiza miles de peticiones mientras se procesa la petición original.
* **Clear Hops Memory cache** - Borra de la memoria todas las soluciones almacenadas anteriormente.
* **Hide Rhino.Compute Console Window** - Hops resolverá en segundo plano, pero mostrar la ventana puede ser útil para solucionar problemas.
* **Launch Local Rhino.Compute at Start** - Utilícelo para equipos remotos cuando sea necesario iniciar Compute antes de enviar cualquier solicitud.
* **Child Process Count** - Se utiliza para limitar el número de solicitudes de procesos paralelos adicionales. Puede que quiera definir esta opción en el número de núcleos disponibles.
* **Function Sources** - Esta sección permite añadir una ruta (ya sea a un directorio local o a una URL) a las funciones Hops de uso frecuente (por ejemplo, definiciones de Grasshopper).

{{< call-out "note" "Nota" >}}
A partir de la versión 7.13 de Rhino, las tolerancias del modelo activo (es decir, las tolerancias absolutas de distancia y ángulo) se pasan desde Hops a la instancia en ejecución de Rhino.compute como parte de la solicitud JSON.
{{< /call-out >}}

### Configuración de componentes

Haga clic con el botón derecho del ratón en el componente Hops para seleccionar las opciones que controlan su funcionamiento.

{{< image url="/images/gh-hops-component-settings.png" alt="/images/gh-hops-component-settings.png" class="image_center" width="60%" >}}

* **Parallel Computing** - Pasa cada elemento a un nuevo nodo paralelo si está disponible.
* **Path...** - Añade la ubicación de la función GH a resolver. Puede ser un nombre de archivo, una dirección IP o una URL.
* **Mostrar entrada: Path** - Convierte la ruta en una entrada del componente, de modo que la ruta puede establecerse a través del lienzo de Grasshopper.
* **Mostrar entrada: Enabled** - Muestra una entrada Enabled que ejecuta el componente basándose en un valor booleano `True` o `False`.
* **Asynchronous** - La interfaz de usuario no se bloqueará mientras se espera que se resuelva un proceso remoto y la definición se actualizará cuando se complete la resolución.
* **Cache In Memory** - Las soluciones anteriores se almacenan en la memoria de la máquina local para mejorar el rendimiento si se calcularon previamente las mismas entradas.
* **Cache On Server** - Las soluciones anteriores se almacenan en el servidor remoto para mejorar el rendimiento. Actualmente disponible solo en los servicios de Remote Hops.

## Configuración de máquinas remotas

Por defecto, Hops utilizará su equipo local para resolver las funciones de Grasshopper. Sin embargo, es posible configurar equipos remotos (es decir, servidores) o máquinas virtuales para que Hops llame.

Para realizar llamadas API a una máquina remota, siga esta [guía para configurar un entorno de producción](../deploy-to-iis/).

## Llamar a un servidor CPython

Utilice Hops para llamar a CPython. Algunas ventajas de este componente:

1. Llamar a librerías CPython, como Numpy y SciPy
1. Utilizar algunas de las bibliotecas más recientes disponibles para CPython, como TensorFlow.
1. Crear funciones reutilizables y procesamiento paralelo.
1. Admite modos de depuración reales, incluidos puntos de interrupción.
1. Compatibilidad total con Visual Studio Code.
1. Otras aplicaciones y servicios que admiten una API Python también pueden utilizar las bibliotecas aquí incluidas.
1. El componente Hops intenta detectar cuándo han cambiado las entradas y salidas en un servidor.  

### Introducción a CPython en Grasshopper

Este módulo Python ayuda a crear funciones Python (específicamente CPython) y utilizarlas dentro de sus scripts de Grasshopper utilizando los nuevos componentes de Hops.

**Se necesita:**

1. [Rhino 7.4 o posterior](https://www.rhino3d.com/download/)
1. [CPython 3.8 o superior](https://www.python.org/downloads/)
1. [Componente de Hops para Grasshopper](https://developer.rhino3d.com/guides/grasshopper/hops-component/)
1. [Visual Studio Code](https://code.visualstudio.com/) muy recomendable

**Tutorial en vídeo:**

{{< vimeo 524032610 >}}

Este módulo puede utilizar su servidor HTTP incorporado por defecto para servir las funciones como componentes de Grasshopper, o actuar como middleware de una aplicación [Flask](https://flask.palletsprojects.com/en/1.1.x/). También puede funcionar junto con [Rhino.Inside.CPython](https://discourse.mcneel.com/t/rhino-inside-python/78987) para dar acceso completo a la [API RhinoCommon](https://developer.rhino3d.com/api/).

## Preguntas frecuentes:

#### ¿Se pueden anidar funciones de Hops dentro de otras funciones?

Sí, es posible anidar funciones de Hops dentro de otras funciones. Se denomina _recursión_ y el límite de recursión por defecto está fijado en 10.

#### ¿Hay que pagar para utilizar Hops?

No, Hops es gratuito.

#### ¿Se puede utilizar Hops con Grasshopper Player para crear comandos?

Sí, las funciones Hops pueden utilizar los componentes Context Bake y Context Print para crear comandos de Rhino en Grasshopper Player.

#### ¿Admite Hops el procesamiento en paralelo?

Sí, Hops lanzará por defecto un proceso paralelo para cada rama de un flujo de entrada de árbol de datos.

#### ¿Qué tipos de entrada y salida admite Hops? (Admite todos los tipos habituales, pregunta por otros si los necesitas)

Hops procesa tipos de datos estándar de Grasshopper (cadenas, números, líneas, etc.). Para otros tipos de datos, como imágenes o archivos meteorológicos EPW, utilice una cadena para el nombre del archivo, de modo que la función externa también pueda leer el mismo archivo.

#### ¿Pueden ejecutarse los componentes de plugins en las funciones de Hops?

Sí, todos los plugins Grasshopper instalados pueden ejecutarse dentro de una función de Hops.

#### ¿Puede utilizarse para cálculos extremadamente largos dentro de una función?

Sí, cada componente de Hops tiene una opción para resolver de forma asíncrona. La interfaz de usuario no se bloqueará mientras se espera a que un proceso remoto resuelva y la definición se actualizará cuando finalice la resolución. Hops esperará a que se devuelvan todas las llamadas a funciones antes de procesar las salidas a los componentes posteriores.
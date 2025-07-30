+++
aliases = ["/en/5/guides/compute/what-is-hops/", "/en/6/guides/compute/what-is-hops/", "/en/7/guides/compute/what-is-hops/", "/en/wip/guides/compute/what-is-hops/"]
authors = [ "andy.payne" ]
categories = [ "Hops" ]
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "Qué es Hops"
type = "guides"
weight = 1
override_last_modified = "2022-03-21T17:57:18Z"

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

Hops permite simplificar grandes definiciones complejas. Las definiciones de Grasshopper pueden ser grandes, complicadas y repetitivas. Este estado de desorganización se denomina a veces [código espagueti](https://www.pcmag.com/encyclopedia/term/spaghetti-code). Son muchos los factores que contribuyen a la aparición de código espagueti: limitaciones de tiempo, nivel de conocimientos del programador, complejidad del proyecto y limitaciones del lenguaje de programación. Después de intentar descifrar un código espagueti en Grasshopper, hay una verdad universal: el código espagueti es difícil de leer y entender. **Ahora, puede utilizar Hops para simplificar  código espagueti difícil de leer.**

{{< image url="/images/hops_spaghetti_code_1.png" alt="/images/hops_spaghetti_code_1.png" class="image_center" width="100%" >}}

### Llamar a funciones en Grasshopper

En programación, una **función** es un módulo de código "autónomo" que procesa entradas y devuelve un resultado. Las definiciones de Grasshopper también procesan entradas y devuelven resultados. Sin embargo, Grasshopper no se escribió pensando en las funciones. Los clusters funcionan en cierto modo, pero no facilitan la reutilización de definiciones sencillas en proyectos complejos.

Para solucionarlo, se ha añadido el componente Hops. Hops permite utilizar definiciones de Grasshopper  independientes como funciones. La clave está en aprender a dividir un problema en subdefiniciones más pequeñas que utilizaremos como funciones.

Imagine que necesita realizar un análisis de sombras para una torre paramétrica que está diseñando para la ciudad de Nueva York. Este problema podría dividirse en cuatro tareas más pequeñas:
1. Crear el contorno del solar
1. Crear la envolvente del edificio
1. Crear las placas de suelo
1. Realice el análisis de sombras desde la fachada del edificio y los edificios circundantes.

Una vez definidas claramente las tareas, se puede determinar qué información se necesitará para realizar cada una de ellas (es decir, las entradas) y qué datos se devolverán al final (es decir, las salidas). En el paso 1, las entradas necesarias para generar el esquema del solar incluirían los retranqueos del solar y otros parámetros normativos de los códigos de edificación y zonificación. El resultado de esta función incluiría probablemente una polilínea que indicaría la superficie máxima del edificio en la planta baja. 

Para definir los parámetros que se utilizarán en una función de Grasshopper, utilice los componentes **Context Get** para las entradas y el componente **Context Bake** para las salidas. Cada uno de ellos se encuentra en la *pestaña Params > grupo Util*.

{{< image url="/images/hops_context_getters.png" alt="/images/hops_context_getters.png" class="image_center" width="92%" >}}

Ahora que tenemos definidas las entradas y salidas, solo nos queda rellenar los pasos para convertir esas entradas en salidas. Una vez que una función se ha definido completamente como una definición de Grasshopper, puede ser llamada por Hops. Hops expone las entradas y salidas que ha definido dentro de su función en la definición que la contiene. A diferencia de los clusters, Hops permite hacer referencia a archivos externos que pueden guardarse localmente o en una unidad de red, lo que facilita compartir definiciones entre otros miembros del equipo y colaboradores.

Hops le permite aumentar la legibilidad de su código simplificando las definiciones complejas, reduciendo la duplicación y compartiendo y reutilizando funciones. Hops permite resolver funciones en paralelo, lo que puede acelerar los proyectos de gran envergadura. También permite resolver funciones de forma asíncrona, sin bloquear las interacciones entre Rhino y Grasshopper.

## ¿Cómo funciona?

En segundo plano, el cliente Hops pasa la definición de Grasshopper especificada a una instancia sin interfaz de Rhino y al servidor Grasshopper.  

### El cliente de Hops

Un cliente es un dispositivo de hardware (es decir, un ordenador) o una aplicación de software que solicita un recurso digital a un servidor a través de una conexión de red. 

El componente Hops es el cliente. Se puede encontrar en la *pestaña Params > grupo Util* después de instalar Hops a través del administrador de paquetes. Hops necesita la ruta o URL de la definición que va a resolver.
{{< image url="/images/hops_hello_world4.png" alt="/images/hops_hello_world4.png" class="image_center" width="55%" >}} 

Una vez especificada la definición, el componente se actualiza para mostrar las entradas y salidas definidas en la definición.
{{< image url="/images/hops_io.png" alt="/images/hops_io.png" class="image_center" width="30%" >}} 

### El servidor de Rhino

Un servidor sirve datos a sus clientes a través de una conexión de red. 

En el contexto de Hops, el servidor es una versión sin interfaz de Rhino y Grasshopper. El servidor de Rhino sin interfaz resuelve la definición de Grasshopper enviada desde Hops y, a continuación, devuelve el resultado.
{{< image url="/images/hops_console.png" alt="/images/hops_console.png" class="image_center" width="100%" >}}

Hops opcionalmente permite apuntar a un servidor Rhino.Compute que se ejecuta en otro ordenador para resolver las definiciones de Grasshopper. Esto permite descargar parte o la totalidad de la resolución a un recurso informático externo.

## Primeros pasos

Para crear una función que pueda ser referenciada por Hops, necesitamos dividir nuestra definición en tres secciones distintas; una para definir nuestros parámetros de entrada, otra para especificar las salidas y, finalmente, una sección que realice las *acciones* de la función. Para empezar a utilizar Hops, puede seguir el vídeo o seguir los pasos que se indican a continuación.

{{< vimeo 713836707 >}}

<br><br>
En este ejemplo queremos crear una función sencilla que tome como entrada el nombre de un usuario (por ejemplo, David) y devuelva un mensaje como *"¡Hola David!"*.

### Instalar Hops

Antes de empezar, asegurémonos de que Hops está instalado correctamente. Hay varias maneras de instalar Hops en su máquina.
  1. [Install Hops](rhino://package/search?name=hops) (se iniciará Rhino)
  1. O escriba `AdministradorDePaquetes` en la línea de comandos de Rhino.
      1. A continuación, busque "Hops".
      1. Seleccione Hops y, a continuación, Install.

### Crear una entrada

Ahora que tenemos Hops instalado, vamos a empezar a definir nuestra función mediante la creación de un parámetro de texto de entrada. En la *pestaña Params > grupo Util* verá un conjunto de componentes Context Getter. Coloque un componente **Get String** en el lienzo. Haga clic con el botón derecho del ratón en el centro de este componente y cambie el nombre de `Get String` a `Name`. Este valor es el que Hops utilizará como nombre del parámetro de entrada.
{{< image url="/images/hops_getting_started_01.png" alt="/images/hops_getting_started_01.png" class="image_center" width="100%" >}}

Puede asignar un valor por defecto a este parámetro conectando una cadena a la entrada del componente Get String. Añada un **Text Panel** al lienzo. Se puede encontrar en la *pestaña Params > grupo Input*. Haga doble clic en el Text Panel y escribe su nombre en la entrada.
{{< image url="/images/hops_getting_started_02.png" alt="/images/hops_getting_started_02.png" class="image_center" width="100%" >}}

### Definir la función

Ahora que hemos creado un parámetro de entrada, necesitamos realizar algún tipo de acción utilizando ese valor. Crearemos un mensaje utilizando el nombre que acaba de pasar al componente Get String. Añada un **componente Concatenate** al lienzo. Se encuentra en la *pestaña Sets > grupo Text*. 

El componente Concatenate agregará una serie de fragmentos de texto en un único mensaje. En nuestro caso, queremos crear una cadena que diga "Hola, su nombre". 

El componente Concatenate es un tipo especial de componente en Grasshopper que utiliza una interfaz de usuario ampliable (ZUI, por sus siglas en inglés). Si amplía el componente (utilizando la rueda de desplazamiento central), aparecerá un pequeño botón (+) a la izquierda del componente. Haga clic en el signo (+) situado bajo el segundo parámetro (B) para añadir un tercer parámetro de entrada.

Ahora, reduzca con el zoom y añada otro Text Panel al lienzo. Haga doble clic en él para introducir texto. Escriba `Hola` en el panel (nota: hay un espacio extra añadido después de la palabra). Conecte ese panel a la entrada A del componente Concatenate.

A continuación, conecte la salida del componente Get String a la entrada B del componente Concatenate. Por último, añada otro panel de texto al lienzo y escriba un signo de exclamación `!` en el panel. Conecte la salida de ese panel de texto a la entrada C del componente Concatenate.

Conecte un Text Panel a la salida del componente Concatenate para ver este mensaje. La definición debería quedar así.
{{< image url="/images/hops_getting_started_03.png" alt="/images/hops_getting_started_03.png" class="image_center" width="100%" >}}

### Crear una salida

El último paso en la creación de la función de Hops sería crear un parámetro de salida para devolver la cadena que acabamos de crear. Vaya a la *pestaña Param > grupo Util* y añada el componente **Context Print** al lienzo.

Haga clic con el botón derecho en el parámetro de entrada (etiquetado Tx) y cambie el nombre a `Message`. Puede ponerle el nombre que quiera, pero este valor es el que Hops utilizará para el parámetro de salida.

Ahora guarde el archivo en algún directorio de su equipo. Llame al archivo **Hello_World.gh**.
{{< image url="/images/hops_getting_started_04.png" alt="/images/hops_getting_started_04.png" class="image_center" width="100%" >}}

### Llamar a la función

Ahora hemos creado una función compatible con el Hops. Usaremos Hops para llamar a esa función. Empiece creando una nueva definición de Grasshopper (Ctrl + N).

Vaya a la *pestaña Param > grupo Util* y añada un componente **Hops** al lienzo. Haga clic con el botón derecho en este componente y seleccione la opción de menú **Path**. En el cuadro de diálogo emergente, seleccione el archivo **Hello_World.gh** que acabamos de crear. Seleccione **OK** cuando haya seleccionado la ruta.

En este punto, el componente Hops debería cambiar de apariencia, añadiendo una entrada llamada `Name` y una salida llamada `Message`. Hops esencialmente agrupa el ejemplo Hello_World.gh que hemos creado y lo envía a un servidor local rhino.compute para realizar el cálculo y devolver el resultado.

Pruebe a añadir un nuevo **Text Panel** en el lienzo y conéctelo a la entrada Name del componente Hops. Haga doble clic para cambiar el nombre en el Text Panel. Añada otro Text Panel a la salida del componente Hops para ver el resultado que devuelve el servidor rhino.compute.
{{< image url="/images/hops_getting_started_05.png" alt="/images/hops_getting_started_05.png" class="image_center" width="100%" >}}

Acabamos de ver cómo crear y llamar a su primera función de Hops. Si desea obtener más información sobre cómo se comunica Hops con el servidor rhino.compute o sobre cómo configurar su propio entorno de producción, consulte los siguientes enlaces.

 ---

## Enlaces rápidos

 - [Cómo funciona Hops](../how-hops-works)
 - [El componente Hops](../hops-component)
 - [Configurar un entorno de producción](../deploy-to-iis)

+++
aliases = ["/en/5/guides/compute/compute-faq/", "/en/6/guides/compute/compute-faq/", "/en/7/guides/compute/compute-faq/", "/en/wip/guides/compute/compute-faq/", "/en/guides/compute/faq/"]
authors = [ "andy.payne" ]
categories = [ "Getting Started" ]
description = "Esta guía contiene una lista de preguntas frecuentes (FAQ) para Rhino.Compute."
keywords = [ "developer", "compute", "faq" ]
languages = []
sdk = [ "Compute" ]
title = "Preguntas frecuentes"
type = "guides"
weight = 1
override_last_modified = "2025-05-07T09:45:21Z"

[admin]
TODO = ""
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

## General

### ¿Qué es Rhino.Compute?

En su definición más simple, Rhino.Compute es un servidor web que puede realizar cálculos geométricos utilizando la biblioteca de geometría de Rhino (es decir, [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/)). Funciona recibiendo peticiones a través de la web (mediante [HTTP](https://en.wikipedia.org/wiki/HTTP) o [HTTPS](https://en.wikipedia.org/wiki/HTTPS)), procesándolas con el motor de geometría de Rhino y devolviendo los resultados. Cualquier aplicación que pueda enviar peticiones web puede interactuar con Rhino.Compute, lo que facilita su integración en diferentes flujos de trabajo.

### ¿Por qué utilizarlo?

Rhino.Compute le permite utilizar las potentes herramientas y funciones de Rhino fuera de la interfaz habitual de Rhino o Grasshopper. Es ideal para equipos, ya que puede ejecutar definiciones de Grasshopper o funciones de Rhino desde un lugar central, lo que facilita la colaboración. También puede gestionar varias tareas al mismo tiempo (en paralelo), lo que ayuda a acelerar grandes proyectos. Y para cálculos más largos, se ejecuta en segundo plano (de forma asíncrona), por lo que no se bloquea ni ralentiza la interfaz principal.

### ¿Funcionará en macOS?

No. Rhino.Compute depende de [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/) que permite que Rhino y Grasshopper se ejecuten *dentro* de otras aplicaciones de 64 bits. Actualmente, Rhino.Inside solo es compatible con el sistema operativo Windows.

### ¿Cuesta dinero?

La respuesta corta es: depende de *dónde* ejecute Rhino.Compute. Si lo utiliza en un ordenador Windows normal, como su PC personal, no hay ningún coste adicional. Rhino.Compute comprobará su licencia estándar de Rhino al iniciarse (nota: [las versiones de evaluación de Rhino](https://www.rhino3d.com/download/) funcionarán perfectamente). Pero si lo ejecuta en un servidor Windows (como una máquina virtual en la nube), se le cobrará en función de nuestro modelo de [facturación por hora de núcleo](../core-hour-billing/) .

### ¿En qué se diferencia de Hops?

[Hops](../what-is-hops/) es un complemento de Grasshopper (disponible en el [administrador de paquetes](../../yak/what-is-yak/)) que facilita la resolución de definiciones de Grasshopper mediante Rhino.Compute. Al instalar Hops, se inicia automáticamente una instancia de Rhino.Compute en segundo plano cada vez que se abre Grasshopper. A continuación, puede utilizar el componente Hops para enviar su definición de Grasshopper a Rhino.Compute, que la resuelve y envía los resultados de vuelta. En este contexto, Hops es el "cliente" y Rhino.Compute es el "servidor".

### ¿Puedo crear mi propia interfaz para trabajar con Rhino.Compute?

Sí. Como se ha mencionado anteriormente, cualquier aplicación que pueda enviar peticiones web puede trabajar con Rhino.Compute. Para facilitarle las cosas, le ofrecemos tres bibliotecas que puede utilizar en función del lenguaje que prefiera:
1. [Biblioteca Python Rhino.Compute](https://pypi.org/project/compute-rhino3d/)
1. [Biblioteca Javascript Rhino.Compute](https://www.npmjs.com/package/compute-rhino3d)
1. [Biblioteca .NET (C#) Rhino.Compute](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs)

También tenemos guías paso a paso para ayudarle a empezar con las bibliotecas anteriores:
1. [Llamar a Compute con Python](../compute-python-getting-started/)
1. [Llamar a Compute con Javascript](../compute-javascript-getting-started/)
1. [Llamar a Compute con .NET](../compute-net-getting-started/)

Por último, tenemos un repositorio [GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute) con un montón de proyectos de muestra y ejemplos que muestran cómo utilizar Rhino.Compute para diferentes tareas de geometría.

### ¿Puedo utilizar Rhino.Compute en un entorno de producción?

Sí. Ofrecemos una [guía paso a paso](../deploy-to-iis/) para ayudarle a configurar Rhino.Compute en un entorno de producción, como en una máquina virtual (VM). La configuración es muy sencilla: basta con ejecutar un sencillo script de PowerShell y Rhino.Compute estará listo para gestionar solicitudes.

## Solución de problemas

Hemos trabajado mucho para que Rhino.Compute sea lo más fácil de usar posible. Pero a veces las cosas no salen según lo previsto. Esta sección está aquí para ayudarte a solucionar cualquier problema que pueda encontrar.

### ¿Dónde se encuentran los archivos de registro?

Si está ejecutando Rhino.Compute con Hops, deberá asegurarse de que la aplicación de consola de Rhino.Compute esté visible siempre que se inicie. Para ello, siga los pasos siguientes:
1. Ejecutar Grasshopper
1. Haga clic en **Archivo -> Preferencias** para abrir el cuadro de diálogo Grasshopper Settings.
1. Haga clic en la pestaña **Solver** del menú de la izquierda
1. **Desmarque** la opción de menú Hide Rhino.Compute Console Window.
1. Reinicie Rhino y Grasshopper 

{{< image url="/images/hops-preferences-1.png" alt="/images/hops-preferences-1.png" class="image_center" width="75%" >}}

En este punto, debería ver aparecer una nueva aplicación en su barra de tareas (si utiliza Windows) cuando inicie Grasshopper. Esta es la aplicación de consola de Rhino.Compute. Aquí se mostrará información útil para la resolución de problemas mientras trabaja con Rhino.Compute.

{{< image url="/images/hops-console-2.png" alt="/images/hops-console-2.png" class="image_center" width="100%" >}}

<br>
Si está ejecutando Rhino.Compute en una máquina virtual, los archivos de registro se guardan como archivos de texto. Se crearán nuevos archivos de registro diariamente. Por defecto, los archivos de registro se guardan en la siguiente ubicación: 

```cs
C:\inetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute\logs\
```

### ¿Puedo activar el registro de información detallada?

Por defecto, Rhino.Compute envía un conjunto mínimo de información a los registros. Para habilitar un registro más detallado, deberá crear una variable de entorno en su máquina.

1. Haga clic con el botón derecho en el icono **Este PC** del Explorador de archivos y, a continuación, seleccione **Propiedades** o **Sistema** en el Panel de control.
1. En la ventana Propiedades del sistema, haga clic en **Configuración avanzada del sistema**.
1. En la pestaña **Opciones avanzadas** , haga clic en **Variables de entorno**.
1. Haga clic en el botón **Nueva** para crear una nueva variable de sistema
1. En la entrada **Nombre de variable** , escriba "RHINO_COMPUTE_DEBUG"
1. En la entrada **Valor de la variable** , escriba "true"
1. Haga clic en Aceptar para guardar la variable de entorno del sistema y, a continuación, vuelva a hacer clic en Aceptar para cerrar el cuadro de diálogo Variables de entorno y la ventana Propiedades del sistema.

### ¿Qué hago si obtengo un error HRESULT E_FAIL?

Si Rhino.Compute devuelve el siguiente error:

```cs
Excepción de inicio de aplicación
System.Runtime.InteropServices.COMException (0x80004005): Se ha devuelto el error HRESULT E_FAIL de una llamada a un componente COM.
   en Rhino.Runtime.InProcess.RhinoCore.InternalStartup(Int32 argc, String[] argv, StartupInfo& info, IntPtr hostWnd)
```

La causa más probable es que Rhino.Compute no encuentra una licencia válida al iniciarse. Si está ejecutando una máquina basada en Windows Server (es decir, en una máquina virtual), siga estos pasos:

1. Vaya al [Portal de licencias](https://www.rhino3d.com/licenses?_forceEmpty=true) y seleccione el grupo que configuró con facturación por hora de núcleo.
1. Haga clic en **Gestionar grupo -> Gestionar facturación por hora de núcleo**.
1. Haga clic en **Acción -> Obtener token de autenticación** para obtener un token.
1. Cree una nueva variable de entorno con el nombre `RHINO_TOKEN` y utilice el token como valor. Como el token es demasiado largo para el cuadro de diálogo Variables de entorno de Windows, lo más fácil es hacerlo mediante un comando de PowerShell.

```ps
[System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'your token here', 'Machine')
```

A partir de ahora, cuando inicie Rhino en esta máquina utilizará su equipo de facturación por hora de núcleo.

{{< call-out "warning" "Aviso" >}}
<strong>Aviso:</strong> su token de facturación por hora de núcleo permite a cualquiera cobrar a su grupo. <strong>NO</strong> comparta este token con nadie.
{{< /call-out >}}

### Recibo un mensaje de error 401. ¿Qué significa?

Si Rhino.Compute le da un error 401, significa que la solicitud no estaba autorizada. Esto suele ocurrir cuando a la solicitud le falta una clave API. Rhino.Compute comprueba esta clave, que se guarda como variable de entorno en la máquina en la que se ejecuta, para asegurarse de que solo los clientes autorizados pueden conectarse.

Si utiliza Hops, puede configurar la clave API en la sección de preferencias.

1. Ejecutar Grasshopper
1. Haga clic en **Archivo -> Preferencias** para abrir el cuadro de diálogo Configuración de Grasshopper.
1. Haga clic en la pestaña **Solver** del menú de la izquierda
1. **Introduzca la clave API** en el cuadro de diálogo de entrada.
1. Reinicie Rhino y Grasshopper

{{< image url="/images/hops-api-key.png" alt="/images/hops-api-key.png" class="image_center" width="75%" >}}

<br>
Si envía una solicitud web a Rhino.Compute utilizando un método diferente, asegúrese de incluir un par clave/valor en la cabecera de la solicitud. La clave debe llamarse "RhinoComputeKey", y su valor debe coincidir con la clave API establecida en la máquina que ejecuta Rhino.Compute.

### ¿Qué significa un código de error 500?

Si recibe una respuesta de Rhino.Compute con un código de error 500, significa que el servidor no funciona correctamente y no puede procesar la solicitud. Si esto ocurre, puede que tenga que intentar ejecutar Rhino.Compute en modo depuración para obtener más información sobre por qué falla el servidor. [Siga esta guía](../development/) para aprender a ejecutar Rhino.Compute en modo de depuración.

### ¿Qué hago si recibo una excepción de tiempo de espera?

Si Rhino.Compute devuelve el siguiente error:

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Id de conexión "...", Id de solicitud "...": La aplicación ha lanzado una excepción no controlada.
      System.Threading.Tasks.TaskCanceledException: La solicitud se ha cancelado porque ha transcurrido el tiempo de espera configurado en HttpClient.Timeout de 100 segundos.
```

El tiempo de espera de una solicitud HTTP se produce cuando un cliente (como Hops) no recibe una respuesta de un servidor (como Rhino.Compute) en un tiempo determinado. Por lo tanto, hay dos valores de tiempo de espera que debemos tener en cuenta: 1) el tiempo de espera del cliente y 2) el tiempo de espera del servidor.

La configuración del tiempo de espera que ve en las preferencias de Hops controla el tiempo de espera del lado del cliente. El valor por defecto es de 100 segundos, pero puede ampliarse para paliar este error.

{{< image url="/images/hops-timeout.png" alt="/images/hops-timeout.png" class="image_center" width="75%" >}}

El tiempo de espera del servidor se gestiona por separado: se establece mediante una variable de entorno en la máquina que ejecuta el servidor. Para configurar la variable de entorno, siga estos pasos:

1. Haga clic con el botón derecho del ratón en el icono **Este PC** del Explorador de archivos y, a continuación, seleccione **Propiedades** o **Sistema** en el Panel de control.
1. En la ventana Propiedades del sistema, haga clic en **Configuración avanzada del sistema**.
1. En la pestaña **Avanzado** , haga clic en **Variables de entorno**.
1. Haga clic en el botón **Nuevo** para crear una nueva variable de sistema
1. En la entrada **Nombre de la variable** , escriba "RHINO_COMPUTE_TIMEOUT".
1. En la entrada **Valor de la variable** , escriba el **número de segundos** que desea utilizar como valor de tiempo de espera del lado del servidor
1. Haga clic en Aceptar para guardar la variable de entorno del sistema y, a continuación, vuelva a hacer clic en Aceptar para cerrar el cuadro de diálogo Variables de entorno y la ventana Propiedades del sistema.

### Recibo un error que dice que el cuerpo de la solicitud es demasiado grande. ¿Qué debo hacer?

Si Rhino.Compute devuelve el siguiente error:

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Id de conexión "...", Id de solicitud "...": La aplicación ha lanzado una excepción no controlada.
      Microsoft.AspNetCore.Server.Kestrel.Core.BadHttpRequestException: Cuerpo de la solicitud demasiado grande.
```

Este error puede producirse si está intentando enviar una gran cantidad de datos a Rhino.Compute en el cuerpo de una solicitud. El límite por defecto para el tamaño de una petición es de aproximadamente 50mb. Para aumentar este límite, siga estos pasos:

1. Haga clic con el botón derecho del ratón en el icono **Este PC** del Explorador de archivos y, a continuación, seleccione **Propiedades** o **Sistema** en el Panel de control.
1. En la ventana Propiedades del sistema, haga clic en **Configuración avanzada del sistema**.
1. En la pestaña **Avanzado** , haga clic en **Variables de entorno**.
1. Haga clic en el botón **Nuevo** para crear una nueva variable de sistema
1. En la entrada **Nombre de variable** , escriba "RHINO_COMPUTE_MAX_REQUEST_SIZE".
1. En la entrada **Valor de la variable** , escriba el **número máximo de bytes** permitido en el cuerpo de una petición HTTP. El valor por defecto es de 52.428.800 bytes (aproximadamente 50mb). Aumente este valor para permitir peticiones más grandes.
1. Haga clic en Aceptar para guardar la variable de entorno del sistema y, a continuación, vuelva a hacer clic en Aceptar para cerrar el cuadro de diálogo Variables de entorno y la ventana Propiedades del sistema.

<br><br>
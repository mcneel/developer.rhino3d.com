+++
aliases = ["/en/5/guides/compute/deploy-to-iis/", "/en/6/guides/compute/deploy-to-iis/", "/en/7/guides/compute/deploy-to-iis/", "/en/wip/guides/compute/deploy-to-iis/", "/en/guides/compute/deploy/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
description = "Cómo implementar Rhino.Compute para producción en una máquina que ejecuta Internet Information Services (IIS)."
keywords = [ "developer", "compute", "production", "IIS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Implementación en servidores de producción"
type = "guides"
weight = 4
override_last_modified = "2022-05-18T09:45:21Z"

[admin]
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

## Información general

Esta guía muestra cómo configurar una instancia de Rhino.Compute en una máquina virtual que ejecute Internet Information Services (IIS). [IIS](https://www.iis.net/), es un servidor web flexible y de propósito general desarrollado por Microsoft que puede configurarse para servir páginas o archivos HTML solicitados. Podemos configurar IIS para que procese las peticiones entrantes (ya sean de Hops o de algún otro cliente) y las reenvíe a la instancia de Rhino.Compute. 

Quizá se pregunte: "¿Para qué necesito IIS? ¿Por qué no puedo simplemente lanzar el servidor Rhino.Compute y enviar solicitudes API directamente a esa instancia?". Técnicamente hablando, no necesita IIS. Sin embargo, tendrá que averiguar cómo relanzar el servidor informático en caso de que se bloquee o funcione mal. También deberá configurar Rhino.Compute para que se inicie siempre que se inicie la máquina virtual. 

Una de las principales ventajas de utilizar IIS como middleware es que puede generar automáticamente una instancia del servidor Rhino.Compute cada vez que se recibe una solicitud. Con esta configuración, no es necesario que Compute funcione continuamente. En su lugar, IIS puede lanzar una instancia de Compute cuando sea necesario, que a su vez lanzará uno o más procesos secundarios. Estos procesos secundarios son los que realizan el cálculo real y también los que requieren su autorización de licencia. 

Cuando Rhino.Compute.exe no recibe peticiones para resolver durante un periodo de segundos (esto se denomina idlespans y el valor predeterminado es de 1 hora), los procesos secundarios de compute.geometry.exe se apagarán y dejarán de incurrir en facturación por hora de núcleo. En algún momento en el futuro, cuando se reciba una nueva solicitud, IIS se asegurará de que Rhino.Compute.exe se está ejecutando, lo que relanzará los procesos secundarios. Tenga en cuenta que puede haber un pequeño retraso en la respuesta mientras se inician los procesos secundarios.

{{< image url="/images/IIS_Request.png" alt="/images/IIS_Request.png" class="image_center" width="100%" >}}
<figcaption align = "left"><b>Fig.1 - Diagrama de flujo que muestra cómo IIS recibe una solicitud entrante y ejecuta Rhino.Compute.exe, que a su vez inicia procesos secundarios.</b></figcaption>

## Requisitos previos

Antes de ejecutar el script Bootstrap en su servidor o máquina virtual, necesitará la siguiente información.

* **`EmailAddress`** - El script utilizará este correo electrónico para descargar una copia de Rhino para instalar. Funciona de manera similar a la página de descarga de Rhino.
* **`ApiKey`** - La clave API es una cadena de texto secreta para el servidor de Compute y las aplicaciones que utilizan la API de Compute, por ejemplo `b8f91f04-3782-4f1c-87ac-8682f865bf1b`. Es básicamente la forma en que el servidor de Compute se asegura de que las llamadas a la API proceden únicamente de sus aplicaciones. Puede introducir cualquier cadena que sea única y secreta para usted y sus aplicaciones informáticas. Asegúrese de guardarlo en un lugar seguro.
* **`RhinoToken`** – Se trata de un token largo que identifica su instancia de Rhino Compute ante el sistema de facturación por hora de núcleo. Vaya al [Portal de licencias](https://www.rhino3d.com/licenses?_forceEmpty=true) para generar este identificador único basado en su licencia. Consulte la guía ["Facturación por hora de núcleo"](../core-hour-billing/) para obtener más información.

{{< call-out "note" "Nota" >}}
Ejecutar Rhino Compute localmente utiliza su licencia de Rhino existente y tiene costes adicionales (aparte de la inversión inicial en la licencia de Rhino). Ejecutar Compute localmente es la mejor opción para el desarrollo y las pruebas. Para obtener más información, lea <a href="../development"><u>Ejecutar y depurar Compute localmente</u></a>.<br><br>.

Sin embargo, al configurar un entorno de producción, necesitará un servidor o una máquina virtual preinstalados con Windows Server 2019 o superior. Las licencias funcionan de forma diferente cuando se ejecuta Rhino (es decir, a través de Compute) en un entorno de producción (es decir, en un servidor) y se le cobrará una tarifa de 0,10 dólares por núcleo y hora. <br><br>

Siga la guía <a href="../core-hour-billing"><u>"Facturación por hora de núcleo"</u></a> para configurarlo. Este paso es importante, así que no se lo salte.
{{< /call-out >}}

## Crear la máquina virtual

El primer paso en el proceso de implementación de **Rhino.Compute** para producción es configurar una máquina física para que actúe como servidor o crear una máquina virtual (VM). Para esta guía, utilizaremos una máquina virtual. Existen varios servicios populares que pueden configurarse para crear una amplia gama de máquinas virtuales en función de sus necesidades de recursos. Dos de los proveedores más destacados son [Azure](https://azure.microsoft.com/en-us/free/virtual-machines/) y [AWS](https://aws.amazon.com/ec2/instance-types/).  

Dependiendo de sus preferencias, le recomendamos comenzar con una máquina virtual de Azure o AWS. Utilice las siguientes guías para realizar ese proceso.

* [Crear una máquina virtual en Azure](../creating-an-Azure-VM).

* [Crear una máquina virtual en AWS](../creating-an-aws-vm).

### Conectarse mediante RDP

Ahora que hemos configurado la máquina virtual, necesitamos poder iniciar sesión en ella para poder configurar IIS y la instancia de Rhino.Compute. Para ello, utilizaremos un protocolo de escritorio remoto (RDP) que conecta dos equipos a través de una red.

Para empezar, vamos a descargar el archivo RDP. Usaremos el Azure VM Portal pero un proceso similar se usa para AWS.

1. En primer lugar, asegúrese de que la máquina virtual está en funcionamiento. Haga clic en la pestaña **Overview** en el menú de la izquierda. Si el *Status* dice *Stopped (Deallocated)*, haga clic en el botón **Start** de la parte superior para iniciar la máquina remota. Después de unos segundos, el estado debe indicar *Running*.

1. Haga clic en la opción **Connect** del menú de la izquierda para desplegar la hoja de configuración de la conexión.

1. Haga clic en el botón **Download RDP File** y guarde el archivo en su equipo.
{{< image url="/images/Azure_VM_Connect1.png" alt="/images/Azure_VM_Connect1.png" class="image_center" width="100%" >}}

1. Haga clic en el menú **Inicio** de Windows y escriba *conexión remota a escritorio* en la barra de búsqueda. Haga clic en el enlace para iniciar la aplicación.

1. Haga clic en el botón de la parte inferior de la aplicación para **Mostrar opciones**.

1. En el área *Configuración de la conexión* , seleccione **Abrir** y navegue hasta el directorio donde guardó el archivo RDP. Elija ese archivo y pulse Abrir.

1. Seleccione la casilla de verificación **Permitirme guardar credenciales**.

1. Haga clic en **Conectar**.
{{< image url="/images/Azure_VM_Connect2.png" alt="/images/Azure_VM_Connect2.png" class="image_center" width="60%" >}}

1. Se abrirá una ventana emergente de seguridad. Haga clic en la casilla **No volver a pedirme conexiones con este equipo** y, a continuación, haga clic en **Conectar**.

1. Introduzca las credenciales de administrador que introdujo en el paso 7 para [Crear una máquina virtual](../deploy-to-iis/#setting-up-a-virtual-machine).

1. Es posible que aparezca otra ventana emergente de seguridad. De nuevo, seleccione **No volver a pedirme conexiones con este equipo** y haga clic en **Sí**.

Enhorabuena. Ahora debería tener acceso al escritorio de la máquina remota que ejecuta Windows Server 2019 o superior.

## Ejecutar el script Bootstrap
Suponiendo que ya ha iniciado sesión en la máquina virtual (mediante RDP), siga los siguientes pasos para instalar Rhino.Compute detrás de IIS. Nota: Los siguientes pasos suponen que se trata de una instalación en una nueva máquina o servidor virtual (lo que significa que Rhino.Compute no se ha instalado previamente en esta máquina). Si ya ha configurado Rhino.Compute e IIS en este equipo y solo necesita actualizar Rhino y/o Rhino.Compute en esta máquina virtual, vaya a la sección [Actualizar Rhino Compute](../deploy-to-iis/#updating-the-deployment).

### Paso 1

1. Haga clic en el menú Inicio de Windows y escriba "Powershell". En el menú que aparece, haga clic con el botón derecho en la **aplicación Windows Powershell** y elija **Ejecutar como administrador**.
{{< image url="/images/powershell_1.png" alt="/images/powershell_1.png" class="image_center" width="50%" >}}

1. **Copie y pegue** el siguiente comando en el prompt de Powershell y pulse **Intro**. Este comando descargará el último script Bootstrap del paso 1 e instalará Rhino e IIS en su máquina virtual. Nota: se le pedirá que introduzca su **Dirección de correo electrónico**, **Clave API**y **Token de Rhino**, así que tenga esa información a mano.
    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-1')">Rhino 7: Paso 1</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-1')" id="defaultOpen1">Rhino 8: Paso 1</button>
    </div>

    <div class="tab-content">
    <div class="codetab-content1" id="r7-1">

    ```powershell
    $F="/bootstrap_step-1.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/bootstrap_step-1.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-1\boostrap_step-1.ps1" 
    ```

    </div>

    <div class="codetab-content1" id="r8-1">

    ```powershell
    $F="/bootstrap_step-1.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/bootstrap_step-1.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-1\boostrap_step-1.ps1" 
    ```

    </div>
    </div>

1. Al final del paso 1, su máquina virtual se reiniciará automáticamente (se cerrará su sesión de Escritorio Remoto).

### Paso 2

1. Vuelva a iniciar sesión en su máquina virtual mediante Escritorio remoto.

1. Abra una nueva instancia de **Windows Powershell**. Asegúrese de hacer clic con el botón derecho en la aplicación y seleccione **Ejecutar como administrador**.

1. **Copie y pegue** el siguiente comando en el indicador de Powershell y pulse **Intro**. Este comando descargará el último script Bootstrap del paso 2 y configurará IIS para que funcione con Rhino.Compute.
    <div class="codetab">
      <button class="tablinks2" onclick="openCodeTab(event, 'r7-2')">Rhino 7: Paso 2</button>
      <button class="tablinks2" onclick="openCodeTab(event, 'r8-2')" id="defaultOpen2">Rhino 8: Paso 2</button>
    </div>

    <div class="tab-content">
    <div class="codetab-content2" id="r7-2">

    ```powershell
    $F="/bootstrap_step-2.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/bootstrap_step-2.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-2\boostrap_step-2.ps1"
    ```

    </div>

    <div class="codetab-content2" id="r8-2">

    ```powershell
    $F="/bootstrap_step-2.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/bootstrap_step-2.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-2\boostrap_step-2.ps1"
    ```

    </div>
    </div>

1. Al final del script de instalación del paso 2, debería aparecer el mensaje *¡Felicidades!*.* Ya se han instalado todos los componentes.* A continuación se darán algunas instrucciones sobre cómo instalar plugins de terceros para que funcionen correctamente con Rhino.Compute. Tenga en cuenta el nuevo **Nombre de usuario** y **Contraseña** que serán necesarios cuando vuelva a iniciar sesión para instalar cualquier plugin adicional.

## Probar la aplicación

En este punto, IIS debe estar configurado para lanzar la instancia de Rhino.Compute cuando se realice una solicitud de API. Intentemos que Hops envíe una definición a la URL de nuestra máquina virtual. 

1. Inicie **Rhino** en su máquina local.

1. Si aún no ha instalado Hops en este equipo, hágalo buscándolo en el **Administrador de paquetes** de Rhino.

1. Inicie **Grasshopper** escribiendo la palabra *Grasshopper* en el símbolo del sistema y pulsando intro.

1. Vaya a **Archivo** y luego a **Preferencias** para abrir el cuadro de diálogo de preferencias. 

1. Haga clic en la pestaña **Solver** del menú de la izquierda. 

1. En la sección **Hops - Compute server URLs** , escriba la dirección web de su máquina virtual. Comience escribiendo `http://` seguido de la dirección IP de la máquina virtual seguida de un `:` y el número de puerto `80`. La dirección completa sería algo parecido a esto:
            
        http://52.168.38.105:80/

1. En la sección **API Key** , introduzca la clave de API que guardó en la sección [Requisitos previos](../deploy-to-iis/#prerequisites) .
{{< image url="/images/Hops_To_IIS_4.png" alt="/images/Hops_To_IIS_4.png" class="image_center" width="80%" >}}

1. Añada un componente **Hops** al lienzo de **Grasshopper** (Params/Util)

1. Haga clic con el botón derecho en el componente **Hops** y establezca **Path** en una definición válida de Hops/Grasshopper. Para obtener más información sobre cómo configurar una definición de Grasshopper que funcione correctamente con Hops, [siga esta guía](../hops-component/).
{{< image url="/images/Hops_To_IIS_2.png" alt="/images/Hops_To_IIS_2.png" class="image_center" width="50%" >}}

Una vez establecida la ruta, el componente Hops creará la solicitud de API adecuada y la enviará a la URL que especificamos en el paso 6 (el servidor Rhino.Compute que se ejecuta en IIS). El servidor de cálculo procesa la solicitud y envía una respuesta a Hops, que devuelve el resultado.
{{< image url="/images/Hops_To_IIS_3.png" alt="/images/Hops_To_IIS_3.png" class="image_center" width="70%" >}}

¡Felicidades! Ha configurado correctamente una instancia de Rhino.Compute que se ejecuta detrás de IIS en una máquina virtual. 

## Modificación de los parámetros de Compute después de la implementación

Hay una serie de argumentos de línea de comandos que se pueden utilizar para modificar el comportamiento de Rhino.Compute. En esta sección se explica cómo cambiar estos parámetros después de implementar Rhino.Compute.

1. Inicie sesión en su máquina virtual (mediante RDP). Consulte la sección [Connect via RDP](#connect-via-rdp) para obtener más detalles.

1. En el menú **Inicio**, haga clic en el área de búsqueda y escriba *Administrador de Internet Information Services (IIS)*. Haga clic para iniciar la aplicación.

1. En el Administrador de IIS, **haga clic** en el nodo del servidor web en el panel **Conexiones** de la izquierda. Nota, este nombre de servidor web debe ser el mismo que utilizó al configurar el nombre de su máquina virtual. 

1. En el panel **Acciones** de la derecha, haga clic en **Detener** para detener el servidor web.
{{< image url="/images/iis_manager.png" alt="/images/iis_manager.png" class="image_center" width="100%" >}}

Ahora que el servidor web IIS se ha detenido, tenemos que modificar el archivo **web.config* para Rhino.Compute. El archivo [web.config](https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/web-config?view=aspnetcore-6.0) es un archivo que leen IIS y el módulo ASP.NET Core para configurar una aplicació alojada en IIS. 

1. Abra una ventana del **Explorador de archivos** y navegue hasta *C:\inetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute*. Al final de este directorio, debería ver un archivo llamado **web.config**. Es posible que tenga que hacer clic en la pestaña **Ver** y hacer clic en la casilla de verificación para activar las **extensiones de nombre de archivo**. Abra el archivo web.config con **Notepad** o cualquier otro editor de texto que prefiera.

El archivo web.config completo debería verse así:

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.webServer>
    <handlers>
      <add name="aspNetCore" path="*" verb="*" modules="AspNetCoreModuleV2" resourceType="Unspecified"/>
    </handlers>
    <aspNetCore processPath=".\rhino.compute.exe" arguments="--port 80" stdoutLogEnabled="true" stdoutLogFile="..\..\..\..\..\logs\LogFiles\W3SVC1\" forwardWindowsAuthToken="true" hostingModel="InProcess"/>
  </system.webServer>
</configuration>
```
La línea que más nos interesa modificar es la que empieza con la etiqueta **`<aspNetCore>`**. Puede ver que el segundo parámetro de esta línea se denomina **`arguments`**. Esta es la sección que debe editar para añadir otros argumentos de línea de comandos para modificar Rhino.Compute. 

A continuación se describe cada argumento de la línea de comandos que puede modificarse.

- **port** - Es el número de puerto en el que se ejecutará Rhino.Compute. El puerto número 80 suele reservarse para la comunicación HTTP, mientras que el puerto número 443 se utiliza para el protocolo HTTPS. Hemos configurado Rhino.Compute para que se conecte al puerto 80 en el script Bootstrap, así que no modifique este valor a menos que sepa lo que está haciendo. Ejemplo de uso: `--port 80`.

- **childcount** - Este parámetro controla el número de procesos secundarios de compute.geometry a gestionar. El *valor predeterminado es 4* , lo que significa que Rhino.Compute generará cuatro procesos secundarios, cada uno de los cuales podrá gestionar las solicitudes entrantes. Ejemplo de uso: `--childcount 8` le dice a Rhino.Compute que lance ocho procesos secundarios.

- **childof** - Este es el identificador del proceso principal. Compute revisa la existencia 
de este identificador y se cerrará cuando este proceso haya terminado. Como dependemos de que IIS inicie y detenga Rhino.Compute, no necesita este parámetro cuando se ejecute en un entorno de producción.

- **spawn-on-startup** - Esta opción determina si se inicia un proceso secundario compute.geometry cuando se inicia Rhino.Compute. El *valor predeterminado es false*. Este parámetro es una bandera, lo que significa que si no se incluye en la lista de argumentos, el valor será false. Si incluye este parámetro, su valor será true. Para entornos de producción, este valor debe permanecer como false.

- **idlespan** - Es el número de segundos que un proceso secundario de compute.geometry debe permanecer abierto entre peticiones. El *valor predeterminado es 1 hora*. Cuando Rhino.Compute.exe no recibe peticiones para resolver durante un periodo de `idlespan` segundos, los procesos secundarios de compute.geometry.exe se apagarán y dejarán de incurrir en facturación por horas de núcleo. En algún momento en el futuro, cuando se reciba una nueva solicitud, los procesos secundarios se volverán a lanzar, lo que provocará un pequeño retraso en las solicitudes mientras se lanzan los procesos secundarios. Ejemplo de uso: `--idlespan 1800` le dice a Rhino.Compute que apague los procesos secundarios después de 30 minutos (30 min. x 60 seg. = 1800).

    Si cambia el valor `idelspan` en los argumentos de la línea de comandos para Rhino.Compute, también tendrá que hacer una modificación en la configuración de IIS. Esto se debe a que IIS también contiene una configuración para cerrar Rhino.Compute si no se reciben nuevas solicitudes después de un periodo de tiempo. Cuando Rhino.Compute se cierra, cerrará a su vez cualquier proceso secundario. 

    Por ejemplo, digamos que cambia el valor de `idlespan` a 7.200 (2 horas). El script Bootstrap establece el valor `IdleTimeout` de IIS en 65 minutos (ligeramente superior al valor `idlespan` predeterminado). Después de 65 minutos, IIS cierra Rhino.Compute, que a su vez cierra todos sus procesos secundarios mucho antes del límite de tiempo esperado de 2 horas. Por lo tanto, si cambia el valor de `idlespan`, se recomienda que también cambie el valor de `Tiempo de inactividad` en la configuración de IIS.

    1. Para ello, vuelva al Administrador de IIS y haga clic en el elemento **Grupos de aplicaciones** del panel **Conexiones** de la izquierda. 
    
    1. En la ventana central, haga clic en **RhinoComputeAppPool**.

    1. En el panel **Acciones** de la derecha, haga clic en **Configuración avanzada**.

    1. Busque la fila **Tiempo de inactividad** en la sección **Modelo de proceso** y cambie el valor del tiempo de inactividad para que sea ligeramente superior al valor de `idlespan` que estableció en los argumentos de la línea de comandos. Nota: el valor `idlespan` está en segundos mientras que el valor `Tiempo de inactividad` está en minutos.
    {{< image url="/images/iis_idletimout.png" alt="/images/iis_idletimout.png" class="image_center" width="60%" >}}

Una vez que haya modificado el archivo web.config, **guárdelo** y cierre el archivo. A continuación, puede volver al Administrador de IIS e **Iniciar** el servidor web haciendo clic en el nodo del servidor web en el panel **Conexiones** de la izquierda y haciendo clic en **Iniciar** en el panel **Acciones** de la derecha.

## Actualizar la implementación
Si ya ha configurado Rhino.Compute en este equipo, es posible que tenga que actualizar periódicamente Rhino y los archivos de compilación de Rhino.Compute a la última versión. Siga los pasos que se indican a continuación para actualizar estas aplicaciones.

### Actualizar Rhino

1. Haga clic en el menú Inicio de Windows y escriba "Powershell". En el menú que aparece, haga clic con el botón derecho en la **aplicación Windows Powershell** y elija **Ejecutar como administrador**.

1. **Copie y pegue** el siguiente comando en el indicador de Powershell y pulse **Enter**. Este comando descargará la última versión de Rhino para Windows. Nota: se le pedirá que introduzca su **Dirección de correo electrónico**, así que tenga a mano esa información.

    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-3')">Actualizar a la última versión de Rhino 7</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-3')" id="defaultOpen3">Actualizar a la última versión de Rhino 8</button>
    </div>

    <div class="tab-content">
    <div class="codetab-content1" id="r7-3">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/module_update_rhino.ps1 -outfile update_rhino.ps1; .\update_rhino.ps1 
    ```

    </div>

    <div class="codetab-content1" id="r8-3">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/module_update_rhino.ps1 -outfile update_rhino.ps1; .\update_rhino.ps1 
    ```

    </div>
    </div>

### Actualizar Compute

1. Haga clic en el menú Inicio de Windows y escriba "Powershell". En el menú que aparece, haga clic con el botón derecho en la **aplicación Windows Powershell** y elija **Ejecutar como administrador**.

1. **Copie y pegue** el siguiente comando en el símbolo del sistema de Powershell y pulse **Intro**. Este comando descargará la última versión de Rhino.Compute.

    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-4')">Actualizar Rhino.Compute para Rhino 7</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-4')" id="defaultOpen4">Actualizar Rhino.Compute para Rhino 8</button>
    </div>

    <div class="tab-content">
    <div class="codetab-content1" id="r7-4">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/module_update_compute.ps1 -outfile update_compute.ps1; .\update_compute.ps1 
    ```

    </div>

    <div class="codetab-content1" id="r8-4">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/module_update_compute.ps1 -outfile update_compute.ps1; .\update_compute.ps1 
    ```

    </div>
    </div>

 
## Enlaces rápidos

 - [Qué es Hops](../what-is-hops)
 - [Cómo funciona Hops](../how-hops-works)
 - [El componente Hops](../hops-component)

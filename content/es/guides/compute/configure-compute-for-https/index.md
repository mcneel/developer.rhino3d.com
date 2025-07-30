+++
aliases = ["/en/5/guides/compute/configure-https/", "/en/6/guides/compute/configure-https/", "/en/7/guides/compute/configure-https/", "/en/wip/guides/compute/configure-https/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "AWS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Configurar Compute para utilizar HTTPS"
type = "guides"
weight = 5
override_last_modified = "2025-02-25T08:16:19Z"

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

En esta guía explicaremos el proceso de creación de un certificado SSL válido para que Rhino.Compute pueda comunicarse con los clientes mediante el protocolo HTTPS.

## Requisitos previos

Debe completar lo siguiente:

1. Debe tener una instancia de máquina virtual (VM) activa. Utilice las siguientes guías para configurar una máquina virtual.

    * [Crear una máquina virtual en Azure](../creating-an-Azure-VM).
    * [Crear una máquina virtual en AWS](../creating-an-aws-vm).

1. La máquina virtual debe ser accesible desde la web (puertos 80 y 443 abiertos).

1. Debe asociar una dirección IPv4 pública estática a su máquina virtual. Para obtener más información sobre la configuración de direcciones IP estáticas, utilice los siguientes enlaces:
    * [Configurar direcciones IP para una interfaz de red Azure](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/virtual-network-network-interface-addresses?tabs=nic-address-portal#add-ip-addresses).
    * [Asociar una dirección IP elástica con una instancia EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html).

1. Debe disponer de un dominio y tener acceso a su configuración DNS. Un **registro A** en su configuración DNS debe apuntar a la dirección IPv4 pública de su máquina virtual.

{{< call-out "note" "Nota" >}}
Para esta guía, he asociado una dirección IP elástica con mi instancia de máquina virtual. También he configurado un registro A en mi configuración DNS para apuntar *rhino.compute.rhino3d.com* a la dirección IP de mi máquina virtual.
{{< /call-out >}}

## Modificar el nombre del host

Antes de realizar el proceso de generación de un certificado SSL, debemos realizar una modificación en la configuración del IIS existente para Rhino.Compute.

1. Si aún no lo ha hecho, inicie sesión en su máquina virtual (a través de RDP). Consulte la sección [Conexión mediante RDP](../deploy-to-iis/#connect-via-rdp) para obtener más detalles.

1. En el menú **Inicio**, haga clic en el área de búsqueda y escriba *Administrador de Servicios de Información de Internet (IIS)*. Haga clic para iniciar la aplicación.

1. En el Administrador de IIS, **haga clic** en el nodo del servidor web en el panel **Conexiones** de la izquierda para expandir el árbol de menús. A continuación, **haga clic** en el nodo **Sitios** para desplegar el submenú. Por último, seleccione el nodo **Rhino.Compute** del árbol de menús para ajustar su configuración.

1. En el panel **Acciones** de la derecha, haga clic en **Enlaces**. {{< image url="/images/Site_Binding_2.png" alt="/images/Site_Binding_2.png" class="image_center" width="100%" >}}

1. En el panel **Enlaces del sitio**, seleccione el botón **Añadir** . {{< image url="/images/Site_Binding_3.png" alt="/images/Site_Binding_3.png" class="image_center" width="100%" >}}

1. En el campo de texto **Nombre de host**, escriba el nombre del subdominio que creó al configurar el registro A. Haga clic en **Aceptar** cuando haya terminado.
{{< image url="/images/Site_Binding_1.png" alt="/images/Site_Binding_1.png" class="image_center" width="80%" >}}

1. En este punto, debería tener dos enlaces de sitio en la lista. Haga clic en **Cerrar** cuando haya terminado. {{< image url="/images/Site_Binding_4.png" alt="/images/Site_Binding_4.png" class="image_center" width="100%" >}}

## Generar el certificado

El siguiente paso del proceso es crear e instalar un certificado SSL para el servidor IIS local. Un certificado SSL es un certificado digital que autentica la identidad de un sitio web y permite una conexión cifrada. Es necesario para utilizar el protocolo HTTPS.

Para generar el certificado, recomendamos utilizar [Win-ACME](https://www.win-acme.com/). Win-ACME es un sencillo cliente interactivo que puede crear e instalar el certificado, así como gestionar su renovación cuando sea necesario.

1. [Descargue Win-ACME Client](https://github.com/win-acme/win-acme/releases/download/v2.2.2.1449/win-acme.v2.2.2.1449.x64.pluggable.zip) en la máquina virtual. Nota: Win-ACME se distribuye como archivo .zip.

1. Haga clic con el botón derecho en el archivo .zip de descarga y seleccione **Extraer todo**. En realidad, no importa en qué directorio elija extraer los archivos, ya que los moveremos/renombraremos manualmente en el siguiente paso. Haga clic en **Extraer**.

1. Seleccione el directorio recién extraído y escriba **Ctrl+X** para **Cortar** y, a continuación, **Ctrl+V** para **Pegar** esta carpeta en la unidad raíz <i>C:\</i> . 

1. Ahora, haga clic con el botón derecho en el directorio que acaba de copiar en la unidad <i>C:\</i> y seleccione **Cambiar nombre** en el menú. Acorte el nombre de la carpeta a solo *"win-acme"*. 
{{< image url="/images/win_acme_1.png" alt="/images/win_acme_1.png" class="image_center" width="100%" >}}

1. Haga clic en el menú Inicio de Windows y escriba "Powershell". En el menú que aparece, haga clic con el botón derecho en la **aplicación Windows Powershell** y elija **Ejecutar como administrador**.

1. Escriba el siguiente comando y pulse **Intro** para iniciar la aplicación Win-ACME.
``powershell
    C:\win-acme\wacs.exe
```
1. Debería aparecer un menú interactivo con una serie de instrucciones que pueden ejecutarse tecleando una letra determinada.
{{< image url="/images/win_acme_7.png" alt="/images/win_acme_7.png" class="image_center" width="100%" >}} 

1. Escriba la letra **N** y pulse **Intro** para crear un certificado con la configuración predeterminada. Debería ver una lista de los sitios IIS disponibles. Si no ve una entrada para **Rhino.Compute (1 enlace)** entonces es probable que no haya configurado el nombre de host correctamente en el paso anterior. Consulte la sección sobre cómo [modificar el nombre de host](#modify-the-host-name).
{{< image url="/images/win_acme_8.png" alt="/images/win_acme_8.png" class="image_center" width="100%" >}} 

1. Escriba el número asociado a la fila de **Rhino.Compute (1 enlace)** y pulse **Intro**.
{{< image url="/images/win_acme_9.png" alt="/images/win_acme_9.png" class="image_center" width="100%" >}} 

1. Vuelva a pulsar **Intro** para aceptar la opción predeterminada **Seleccionar todos los enlaces**.

1. Cuando se le solicite *¿Desea continuar con esta selección?* pulse **Intro** o escriba **S** para decir sí.
{{< image url="/images/win_acme_10.png" alt="/images/win_acme_10.png" class="image_center" width="100%" >}} 

1. Debería ver información impresa en la consola mientras se genera el certificado SSL.
{{< image url="/images/win_acme_11.png" alt="/images/win_acme_11.png" class="image_center" width="100%" >}} 

Enhorabuena. Si ha ido todo bien, la aplicación ejecutará una serie de pruebas de autorización y validación para confirmar que el host es seguro. Win-ACME generará el certificado SSL, lo instalará con IIS y añadirá un nuevo enlace **(*:443)** al sitio Rhino.Compute. El certificado SSL tendrá una validez de 90 días. Sin embargo, la aplicación Win-ACME creará un programador de tareas que intentará renovar el certificado transcurridos 60 días. Ahora debería poder enviar una solicitud HTTPS a su servidor Rhino.Compute y obtener una respuesta válida.

<br>

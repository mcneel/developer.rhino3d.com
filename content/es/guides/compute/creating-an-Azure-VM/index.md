+++
aliases = ["/en/5/guides/compute/creating-an-Azure-VM/", "/en/6/guides/compute/creating-an-Azure-VM/", "/en/7/guides/compute/creating-an-Azure-VM/", "/en/wip/guides/compute/creating-an-Azure-VM/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "Azure" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Cómo crear una máquina virtual (VM) en Azure"
type = "guides"
weight = 2
override_last_modified = "2022-02-14T14:13:06Z"

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

## Crear la máquina virtual

En esta guía, mostraremos el proceso de configuración de una máquina virtual utilizando los servicios de Azure. 

Para empezar, confirme que dispone de una suscripción válida a Azure y que ya ha configurado un grupo de recursos para alojar los distintos recursos de esta instancia. Para obtener más información sobre cómo configurar un grupo de recursos en Azure, [visite esta página](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal).

1. Inicie sesión en el [portal](https://portal.azure.com/#home) de Azure.

1. Escriba **máquinas virtuales** en la barra de búsqueda.

1. En **Servicios**, seleccione **Máquinas virtuales**.

1. En la página **Máquinas virtuales**, seleccione **Crear** y, a continuación, **Máquina virtual**.

1. En la pestaña **Básicos**, en **Detalles del proyecto**, asegúrese de que se han seleccionado la Suscripción y el Grupo de recursos correctos.

1. En **Detalles de la instancia**, cree un nombre único para la máquina virtual. Utilizaremos *Rhino-Compute-VM* para el nombre de nuestra VM. Seleccione una región cercana y, a continuación, seleccione *Windows Server 2022 Datacenter - Azure Edition Gen2* para la **Imagen**. No dude en seleccionar cualquier **Tamaño** VM que se ajuste a sus necesidades. Utilizaremos *Standard DS2_v2* para este ejemplo. Deje los demás valores por defecto.
{{< image url="/images/Azure_VM_Create3.png" alt="/images/Azure_VM_Create3.png" class="image_center" width="100%" >}}

1. En **Cuenta de administrador**, indique un nombre de usuario y una contraseña. Tome nota de estas credenciales ya que las utilizaremos cuando iniciemos sesión en la máquina remota.

1. En **Reglas de puertos entrantes**, elija **Permitir puertos seleccionados** y, a continuación, seleccione **RDP (3389)**, **HTTPS (443)** y **HTTP (80)**.
{{< image url="/images/Azure_VM_Create4.png" alt="/images/Azure_VM_Create4.png" class="image_center" width="100%" >}}

1. Seleccione **Siguiente : Disco >**.

1. Seleccione **Siguiente : Red >**.

1. En la sección **Interfaz de red** , haga clic en el botón *Crear nueva* de la subsección **IP pública** .

1. Cuando se abra la hoja emergente, seleccione **Estática** en la pestaña Asignación. Haga clic en **Aceptar** para guardar esta configuración.
{{< image url="/images/Azure_VM_Create5.png" alt="/images/Azure_VM_Create5.png" class="image_center" width="100%" >}}

1. Deje todos los demás valores por defecto. Seleccione **Revisar + crear**.

1. Una vez que su configuración pase la comprobación de validación, seleccione **Crear** para implementar la máquina virtual.

1. Una vez finalizada la implementación, seleccione **Ir al recurso**.

### Añadir una regla de puerto de entrada

Una vez implementada la máquina virtual, debería poder ir a la página de inicio de recursos. Aquí puede cambiar varios ajustes y configuraciones. Vamos a añadir una regla de puerto de entrada para que podamos enviar solicitudes de API en un puerto dedicado.

Por defecto, Azure deniega y bloquea todo el tráfico entrante público, que también incluye el tráfico ICMP. Esto es positivo, ya que mejora la seguridad al reducir la superficie de ataque. El [Protocolo de mensajes de control de Internet (ICMP)](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) se utiliza normalmente para diagnósticos y para solucionar problemas de red. 

Activaremos el tráfico ICMP para nuestra VM para que podamos tratar de hacer ping a la dirección IP y asegurarnos de que obtenemos una respuesta. Lo primero que tenemos que hacer es añadir una regla de puerto de entrada para el tráfico ICMP. 

1. En el menú lateral izquierdo, seleccione la opción **Red** . Esto abrirá la hoja de red.

1. Haga clic en el botón **Añadir regla de puerto de entrada** .
{{< image url="/images/Azure_VM_Create6.png" alt="/images/Azure_VM_Create6.png" class="image_center" width="100%" >}}

1. En el panel **Añadir regla de seguridad de entrada** , establezca el **Rango de puertos de destino** en *, cambie el **Protocolo** a **ICMP**, establezca la **Prioridad** en **100** y escriba **ICMP** en la entrada **Nombre**.
{{< image url="/images/Azure_VM_Create8.png" alt="/images/Azure_VM_Create8.png" class="image_center" width="75%" >}}

1. Haga clic en **Añadir** para crear la nueva regla de puerto entrante.

¡Enhorabuena! En esta guía, ha implementado una máquina virtual sencilla en Azure.
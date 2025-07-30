+++
aliases = ["/en/5/guides/compute/creating-an-aws-vm/", "/en/6/guides/compute/creating-an-aws-vm/", "/en/7/guides/compute/creating-an-aws-vm/", "/en/wip/guides/compute/creating-an-aws-vm/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "AWS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Cómo crear una máquina virtual (VM) en Amazon Web Service"
type = "guides"
weight = 3
override_last_modified = "2021-12-14T13:16:19Z"

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

En esta guía, mostraremos el proceso de configuración de una máquina virtual mediante Amazon Elastic Compute Cloud (Amazon EC2). 

Para empezar, deberá confirmar su suscripción a AWS. Si es nuevo en AWS, puede empezar con Amazon EC2 utilizando [Capa gratuita de AWS](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all). 

{{< call-out "note" "Nota" >}}
Si creó su cuenta de AWS hace menos de 12 meses y aún no ha superado los beneficios de la capa gratuita para Amazon EC2, no le costará nada completar este tutorial. De lo contrario, incurrirá en las tarifas de uso estándar de Amazon EC2 desde el momento en que lance la instancia hasta que la termine, incluso si permanece inactiva.
{{< /call-out >}}

## Requisitos previos

1. [Crear una cuenta para AWS](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#sign-up-for-aws)

1. [Crear un par de claves](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-key-pair). Nota: Recomendamos guardar el archivo de **clave privada** en formato **.pem** con cifrado **RSA** .

1. [Crear un grupo de seguridad](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-base-security-group). Nota: recomendamos añadir una regla para **HTTP**, **HTTPS**, **RDP**y **Todos los ICMP - IPv4**.

## Iniciar la instancia

Para crear una nueva instancia de máquina virtual en AWS, siga estos pasos:

1. Abra la [consola Amazon EC2](https://console.aws.amazon.com/ec2/).

1. En el panel de control de la consola de EC2, seleccione **Lanzar instancia**.

1. Proporcione un nombre para la instancia VM. Para este tutorial, utilizaremos el nombre **"RhinoComputeVM"**.

1. En la sección titulada Imágenes de aplicaciones y SO, haga clic en el botón **Windows** de la pestaña Inicio rápido. En la sección Imagen de máquina de Amazon (AMI) debería haber un menú desplegable con una lista de todas las imágenes de máquina disponibles. Seleccione la AMI para **Microsoft Windows Server 2022 Base**.</p>
{{< image url="/images/AWS_Setup_11.png" alt="/images/AWS_Setup_11.png" class="image_left" width="90%" >}}

1. En la sección **Tipo de instancia**, seleccione el tipo de instancia **t2.micro** (predeterminado) o un tipo de instancia mayor si es necesario. Nota: el tipo de instancia *t2.micro* es elegible para la capa gratuita. En las regiones en las que *t2.micro* no esté disponible, puede utilizar una instancia *t3.micro** de la capa gratuita.</p>
{{< image url="/images/AWS_Setup_12.png" alt="/images/AWS_Setup_12.png" class="image_left" width="90%" >}}

1. En la sección **Par de claves (inicio de sesión)** , seleccione el nombre del par de claves que creó en el paso 2 de la [sección de requisitos previos](../creating-an-aws-vm/#prerequisites) de la lista desplegable.</p>
{{< image url="/images/AWS_Setup_13.png" alt="/images/AWS_Setup_13.png" class="image_left" width="90%" >}}

1. En la sección **Configuración de red**, en **Firewall (grupos de seguridad)** elija el botón de opción **Seleccionar grupo de seguridad existente**. A continuación, en la lista desplegable **Grupos de seguridad comunes**, seleccione el grupo de seguridad que creó en el paso 3 de la sección [Requisitos previos](../creating-an-aws-vm/#prerequisites).{{< call-out "warning" "Importante" >}}Si la opción **Autoasignar IP pública** está configurada como **Desactivada**, haga clic en el botón **Editar** situado en la parte superior derecha del panel de esta sección y cambie esta opción a **Activada**.{{< /call-out >}}
{{< image url="/images/AWS_Setup_14.png" alt="/images/AWS_Setup_14.png" class="image_left" width="90%" >}}

1. En la sección **Configurar almacenamiento**, seleccione la cantidad predeterminada de almacenamiento para esta instancia.

1. Ahora, en el extremo derecho seleccione **Lanzar instancia**.

1. Una página de confirmación le informa de que su instancia se ha lanzado correctamente. En el menú superior, que dice **EC2 > Instancias > Lanzar una instancia**, seleccione el elemento de menú **Instancias** para ver la ventana de la consola de instancias.</p>
{{< image url="/images/AWS_Setup_15.png" alt="/images/AWS_Setup_15.png" class="image_left" width="90%" >}}

1. En la pantalla **Instancias**, puede ver el estado de la instancia lanzada. La instancia debería estar ejecutándose automáticamente después del lanzamiento, pero si no es así, seleccione la casilla de verificación de la fila de instancia y, a continuación, seleccione el elemento de menú **Estado de la instancia** en la parte superior. Seleccione **Iniciar instancia** para iniciar la máquina virtual.

1. Con la fila de instancia seleccionada, haga clic en el botón **Conectar** del menú superior.

1. En la página **Conectarse a la instancia**, seleccione la pestaña **Cliente RDP** .

1. A continuación, seleccione el botón **Obtener contraseña**.

1. Seleccione **Cargar archivo de clave privada** y navegue hasta el archivo de clave privada (.pem) que creó cuando lanzó la instancia.

1. Seleccione **Descifrar contraseña**. La consola muestra la contraseña de administrador por defecto de la instancia en **Contraseña**, sustituyendo al enlace **Obtener contraseña** mostrado anteriormente. **Guarde esta contraseña en un lugar seguro**. Esta contraseña es necesaria para conectarse a la instancia.

1. Seleccione **Descargar archivo de escritorio remoto** para guardar el archivo .rdp en su equipo local. Necesitará este archivo cuando se conecte a su instancia utilizando la aplicación Remote Desktop Connect.

¡Enhorabuena! En este tutorial, ha lanzado con éxito una máquina virtual en AWS y descargado el archivo RDP que se puede utilizar para conectarse a esa instancia.
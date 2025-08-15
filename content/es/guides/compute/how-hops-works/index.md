+++
aliases = ["/en/5/guides/compute/how-hops-works/", "/en/6/guides/compute/how-hops-works/", "/en/7/guides/compute/how-hops-works/", "/en/wip/guides/compute/how-hops-works/"]
authors = [ "andy.payne" ]
categories = [ "Hops" ]
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "Cómo funciona Hops"
type = "guides"
weight = 2
override_last_modified = "2022-02-18T10:08:37Z"

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

El proceso de comunicación entre Hops y un servidor compatible con Hops es un poco más matizado que el simple envío y recepción de una única petición y respuesta http. El primer paso del proceso se produce cuando Hops agrupa la definición de Grasshopper referenciada y envía una solicitud http a un punto final del servidor. 

Un punto de conexión es una dirección URL a la que se puede acceder para realizar una determinada función. En esta petición, el servidor abre la definición de Grasshopper enviada desde Hops y determina qué información será necesaria para rellenar las entradas y salidas del componente Hops. Así, el punto final se llamará `/io` (abreviatura de Input Output).

{{< image url="/images/hops_io_request.png" alt="/images/hops_io_request.png" class="image_center" width="100%" >}}

El componente Hops debería tener ahora suficiente información para crear los nodos de entrada y salida necesarios para sí mismo. 

{{< image url="/images/hops_get_inputs.png" alt="/images/hops_get_inputs.png" class="image_center" width="75%" >}}

Cuando todas las entradas de Hops se hayan conectado a los parámetros de origen, enviará otra petición http al servidor, solo que esta vez la enviará al punto de conexión `/solve`. No es necesario volver a enviar la definición de Grasshopper, ya que se almacenó en el servidor durante el proceso `/io`. En su lugar, los datos enviados en la petición `/solve` solo contienen un ID que indica al servidor dónde encontrar el archivo correcto y todos los datos de entrada. 

La respuesta http del servidor contiene todos los datos que se obtendrían al ejecutar el archivo Grasshopper de la forma tradicional.

{{< image url="/images/hops_return_results.png" alt="/images/hops_return_results.png" class="image_center" width="70%" >}}

Para comprender mejor cómo funciona cada paso anterior, puede exportar la última solicitud y respuesta http para los puntos finales `/io` y `/solve` directamente desde el componente Hops.

{{< image url="/images/hops_export_requests.png" alt="/images/hops_export_requests.png" class="image_center" width="100%" >}}

 ---
 
## Enlaces rápidos

 - [Qué es Hops](../what-is-hops)
 - [El componente Hops](../hops-component)
 - [Configurar un entorno de producción](../deploy-to-iis)
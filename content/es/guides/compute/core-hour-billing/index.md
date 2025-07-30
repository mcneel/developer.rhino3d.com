+++
aliases = ["/en/5/guides/compute/core-hour-billing/", "/en/6/guides/compute/core-hour-billing/", "/en/7/guides/compute/core-hour-billing/", "/en/wip/guides/compute/core-hour-billing/"]
authors = [ "brian" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "core-hour" ]
languages = []
sdk = [ "Compute" ]
title = "Licencias y facturación"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://www.grasshopper3d.com/forum/topics/how-do-i-install-a-custom-ghx"
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


## Sobre la facturación por hora de núcleo

Cuando Rhino está conectado a una cuenta de servicio y se ejecuta en un sistema operativo basado en Windows Server, se le facturarán **0,10 $ por núcleo por hora** que Rhino esté funcionando (prorrateado por minuto).

***Ejemplo 1:** Rhino funcionando en un servidor de 32 núcleos durante una hora:*

  * 1 equipo * 32 núcleos * 1 hora * 0,10 $ por núcleo-hora = 3,20 $

***Ejemplo 2:** Rhino funcionando en 200 servidores de 4 núcleos durante 6 minutos:*

  * 200 equipos * 4 núcleos * 0,1 horas * 0,10 $ por núcleo-hora = 8,00 $

***Ejemplo 3:** 1 instancia de Rhino funcionando en un servidor de 2 núcleos 8 horas al día durante 30 días:*
  * 1 equipo * 2 núcleos * 8 horas/día * 30 días/mes * 0,10 $/hora-núcleo = 48 $/mes

***Ejemplo 4:** 10 instancias de Rhino funcionando en un servidor de 2 núcleos 8 horas al día durante 30 días:*
  * 1 equipo * 2 núcleos * 8 horas/día * 30 días/mes * 0,10 $/hora-núcleo = 48 $/mes
  * (Tenga en cuenta que el número de instancias de Rhino no afecta a la facturación)

**La facturación se basa en el tiempo de actividad**, no en el uso. No hacemos un seguimiento de la actividad de cada núcleo, solo de que tiene uno funcionando con Rhino. Puede escalar sus cargas de trabajo hacia arriba y hacia abajo para optimizar el rendimiento y el coste.

**Se permiten múltiples instancias** - Puede ejecutar tantas instancias de Rhino en el mismo equipo como desee, y el coste será el mismo que el de ejecutar una instancia.

## Configuración de la facturación por horas de núcleo

La facturación por horas de núcleo es necesaria cuando se ejecuta Rhino en un sistema operativo basado en Windows Server.

1. Vaya al [Portal de licencias](https://www.rhino3d.com/licenses?_forceEmpty=true) (inicie sesión en su cuenta de Rhino si se le solicita).
2. Haga clic en _Crear nuevo grupo_ y cree un grupo para su proyecto de Compute. {{< call-out "note" "Nota" >}}
Crear un nuevo grupo no es estrictamente necesario, pero la facturación de hora por núcleo no es *compatible* con las licencias existentes en el grupo. Por lo tanto, si su equipo tiene licencias, no se permitirá la facturación de hora por núcleo.
{{< /call-out >}}

3. Haga clic en _Gestionar grupo_ -> _Gestionar facturación por hora de núcleo_.
4. Marque la casilla situada junto a los productos que desea activar. \
**Tenga en cuenta que si tiene un grupo en funcionamiento desde hace años, puede que necesite activar versiones más recientes de Rhino.**
5. Haga clic en _Guardar_ e introduzca la información de pago cuando se le solicite para su nuevo grupo.

## Usar la facturación por hora de núcleo

1. Vaya al [Portal de licencias](https://www.rhino3d.com/licenses?_forceEmpty=true) y seleccione el grupo que acaba de configurar con facturación por hora de núcleo.
1. Haga clic en _Gestionar grupo_ -> _Gestionar facturación por hora de núcleo_.
2. Haga clic en _Acción_ -> _Obtener token de autenticación_ para obtener un token.
3. Cree una nueva variable de entorno con el nombre `RHINO_TOKEN` y utilice el token como valor. Como el token es demasiado largo para el cuadro de diálogo Variables de entorno de Windows, lo más fácil es hacerlo mediante un comando de PowerShell.

    ```ps
    [System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'token', 'Machine')
    ```

A partir de ahora, cuando inicie Rhino en esta máquina utilizará su equipo de facturación por hora de núcleo.

{{< call-out "warning" "Aviso" >}}
<strong>Aviso:</strong> este token permite a cualquiera cobrar a su grupo. <strong>NO</strong> comparta este token con nadie.
{{< /call-out >}}

## No se admiten licencias para un solo equipo

Cuando se ejecuta en Windows Server, no es posible introducir un código de licencia para que se ejecute como licencia para un solo equipo, ya que Rhino requiere una licencia por núcleo.

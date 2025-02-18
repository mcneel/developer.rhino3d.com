+++
aliases = ["/en/5/guides/general/creating-command-macros/", "/en/6/guides/general/creating-command-macros/", "/en/7/guides/general/creating-command-macros/", "/en/wip/guides/general/creating-command-macros/"]
authors = [ "scottd" ]
categories = [ "Overview" ]
description = "Tutorial básico sobre la creación de macros (scripts de comandos de Rhino)"
keywords = [ "macro", "overview", "rhinoceros", "command" ]
languages = [ "Macro" ]
sdk = [ "Macro" ]
title = "Creación de macros"
type = "guides"
weight = 1
override_last_modified = "2018-12-06T15:12:10Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/rhino/basicmacros"
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

Puede crear macros en Rhino para automatizar muchas tareas, personalizar sus comandos y mejorar su flujo de trabajo.

Puede haber cierta confusión sobre el uso del término "scripting".  Clásicamente, describe tanto el proceso de escritura de macros (de lo que trata esta sección), como la escritura de scripts más sofisticados en [RhinoScript](/guides/rhinoscript/), [Rhino.Python](/guides/rhinopython/) u otros lenguajes de programación.  

En realidad, ambas cosas son muy diferentes. Escribir funciones en RhinoScript u otros lenguajes de programación es mucho más complejo que crear macros, y requiere ciertos conocimientos y habilidades de programación.  No trataremos este tema.

Aqui utilizamos el término "macro" exclusivamente para describir la unión de cadenas de comandos ordinarios de Rhino y sus opciones para crear una función automatizada.  Esto es scripting en su nivel más simple, y es fácilmente accesible para cualquier usuario común de Rhino, aunque no tenga conocimientos de programación.  Lo que necesita es una comprensión razonable de los comandos de Rhino y su estructura, así como una mente lógica y que le guste un poco la experimentación y la depuración.

#### Herramientas necesarias
1. Su cerebro.

2. El archivo de Ayuda de Rhino, que enumera todos los comandos de Rhino y sus subopciones. Esta es su referencia más importante.

3. El **EditorDeMacros** de Rhino, para ejecutar y depurar fácilmente sus macros.


## Ya ha usado una macro o dos...
En primer lugar, si es usuario de Rhino, ya es usuario de macros aunque no lo sepa.  Muchos de los comandos de Rhino ya están "macroprogramados" para usted. Cuando hace clic en un botón de la barra de herramientas o llama un comando del menú, suele tratarse de una macro predefinida.  Para verlo, pulse Mayús+clic derecho en el botón **Extrusión recta**:

![Extrude](/images/extrudecrvbuttoneditor.gif)

Este es un ejemplo de la macro más sencilla, que establece una serie de opciones dentro de un único comando para que no tenga que especificar cada una de ellas cada vez que la utilice.  **ExtrusiónDeCrv** tiene varios botones con opciones predefindas, **Ahusado, PorCurva, HaciaUnPunto, Tapar=Sí** (sólido), etc. Eche un vistazo a las macros de de todos los botones de **ExtrusiónDeCrv** para ver cómo están definidos.

En cierto sentido, está haciendo lo mismo que si pulsara o tecleara las opciones de una en una en la línea de comandos.  De hecho, eso son las macros: un conjunto de instrucciones que repiten una secuencia de comandos que, de otro modo, tendría que introducir manualmente de uno en uno.

Esta programación de opciones para un único comando también puede combinarse con la introducción de datos (es decir, coordenadas u otros datos numéricos). También es posible encadenar varios comandos seguidos, para una secuencia automatizada de eventos de manipulación o creación de objetos.

**Nota:** ¿Por qué los guiones bajos (_)?  Indican a Rhino que el comando que sigue está en inglés (independientemente del idioma en el que esté ejecutando Rhino), lo que hará que su macro sea universal.  Si ejecuta Rhino en inglés y no le importa, puede eliminar los guiones bajos en sus macros si lo desea. No afectará a nada más.  ¿Por qué el signo de exclamación (!)?  Este signo cancela cualquier comando anterior que pudiera estar ejecutándose, por seguridad.

## Para empezar

Digamos que tiene que colocar una serie de cajas de 10x10x10 con el centro de la cara inferior en el punto deseado, y tiene que especificar ese punto mediante un clic del ratón en la ubicación deseada o introduciendo las coordenadas con el teclado.

Podría utilizar el comando estándar Caja (**De esquina a Esquina + Altura**), pero por defecto se colocará el punto de inserción en la primera esquina de la caja.  Para tener el punto de inserción donde queremos, es más fácil utilizar el comando Caja, Centro.   Se trata del comando Caja con la opción Centro, por lo que tendrá que activarlo en su macro.

Abra el **EditorDeMacros** y escriba esto:

```
 ! _Box _Center
```

(Se trata de la macro que se encuentra en el botón Caja, Centro, si se fija). 
Todas las entradas (palabras de comando y entradas numéricas) deben ir separadas por un espacio.

Ahora tenemos que especificar el punto central.  Para ello, debe indicar a Rhino que deje de procesar el comando temporalmente y espere una entrada en forma de clic o entrada de teclado.  Para ello, introduzca el comando Pausa.

```
 ! _Box _Center _Pause
```

Una vez introducidos los datos, puede especificar el tamaño de la caja directamente en el comando.  Como la opción Centro en Caja quiere una esquina de la caja como segunda entrada, puede especificar las coordenadas X,Y:

```
 ! _Box _Center _Pause r5,5
```

(¿Por qué la "r"?  Queremos que esta coordenada sea relativa al último punto elegido, es decir, el centro inferior de la caja.  De lo contrario, la esquina siempre estará en X5, Y5).

En este punto puede introducir la altura, que en este caso es relativa al punto de inicio original.

```
 ! _Box _Center _Pause r5,5 10
```

Como no es necesaria ninguna otra entrada ni hay opciones posibles, la macro se completa y nuestra caja se ha creado.  Tenga en cuenta que como queríamos una altura igual a la anchura, otra posibilidad habría sido utilizar Enter en lugar de 10 para la última entrada.

```
 ! _Box _Center _Pause r5,5 _Enter
```

Ahora que la macro se está ejecutando, [[rhino:macroscriptsetup|cree un nuevo botón de barra de herramientas]] y pegue la macro dentro. Asígnele un nombre reconocible, como "caja centrada inferior 10x10x10".  Tenga en cuenta que, una vez ejecutada la macro, al hacer clic con el botón derecho se repite toda la secuencia de esta macro, por lo que puede utilizarla muchas veces seguidas sin tener que hacer clic en el botón cada vez.

## Bien, vamos a complicarnos un poco más...

Algunos comandos invocan cuadros de diálogo con muchas opciones.  Normalmente, esto detiene la macro y espera a que haga clic en las opciones deseadas, y luego continúa.  Dado que desea automatizar, puede omitir el cuadro de diálogo anteponiendo un –guión (también conocido como raya) al comando.  A continuación, puede escribir todas sus opciones y la macro se ejecutará hasta el final sin necesidad de intervención.  Algunos comandos tienen varios niveles de subopciones.  Si quiere ver lo que hay disponible, escriba el comando en la línea de comandos con el guión y mire las opciones que se proponen.  Haga clic en las opciones y compruebe si tienen subopciones.

#### Transición de dos curvas abiertas

Digamos que desea ejecutar repetidamente el comando `Transición` en dos curvas *ABIERTAS* para formar una superficie.  Si utiliza el comando estándar `Transición`, siempre tendrá que pasar por el cuadro de diálogo.  Si utiliza la versión `-Transición`, podrá evitarlo y todo irá mucho más rápido.  Mire lo siguiente:

```
_-Loft
_Pause
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Tenga en cuenta que cuando invoca el comando, inmediatamente una pausa le permite elegir sus curvas.  Si elimina la pausa, la macro no funcionará si no ha seleccionado sus curvas antes de llamarla.  Si ya ha preseleccionado sus curvas, la pausa se ignora de forma inteligente.  A continuación, el comando establece todas las opciones especificadas. Una vez hecho esto, crea la superficie y termina. Pruébelo con dos curvas abiertas, antes o después de seleccionarlas.  Pruebe a modificar una o varias de las opciones, como sustituir Cerrado=Sí o Simplificar=Reconstruir. (Para esto también hay que añadir una línea con Rebuild=20 o algún otro valor).

#### Modificarlo para utilizarlo con curvas cerradas

Ahora, inténtelo con dos curvas cerradas.  Tiene un problema.  ¿Por qué? Para las curvas cerradas, el comando Transición necesita otra información: la posición de la costura.  Esto tiene que estar en la macro en la secuencia correcta.  Puede elegir entre varias opciones de costura automática (que están en un nivel de subopción) o puede ajustarla en pantalla.  En cualquier caso, tiene que modificar la macro.

Añadir una pausa en el lugar adecuado permite comprobar y ajustar la costura en pantalla:

```
_-Loft
_Pause
_Pause  <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Añadir un `Enter` en lugar de `Pause` indica a Rhino que no importa. Deje la costura como está por defecto.

```
_-Loft
_Pause
_Enter  <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

También puede especificar otra opción de costura de la transición bajando al nivel de subopción de la costura:

```
_-Loft
_Pause
_Natural  <--
_Enter    <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

(El `Enter` después de Natural es necesario para salir del nivel de opciones "costura" y volver al nivel de opciones de Transición).

Lamentablemente, la misma macro no funcionará correctamente para curvas abiertas y cerradas debido a la opción de costura adicional necesaria.  Esta es una de las limitaciones del sistema de macros y de la forma en que se han escrito algunos comandos de Rhino.


## Uso de macros para configurar rápidamente las opciones de la interfaz

Las macros también pueden utilizarse para establecer automáticamente varias opciones de la interfaz gráfica de usuario y de las propiedades del documento sin tener que entrar en el cuadro de diálogo Opciones.  Yo uso lo siguiente para configurar la malla de renderizado de la manera que quiero. (Observe el guión delante de -_DocumentProperties).

```
-_DocumentProperties
_Mesh _Custom
_MaxAngle=0 _AspectRatio=0
_MinEdgeLength=0 _MaxEdgeLength=0
_MaxEdgeSrf=0.01 _GridQuads=16
_Refine=Yes _JaggedSeams=No
_SimplePlanes=No
_Enter
_Enter
```

¿Por qué hay dos Enter al final?

Bajó dos niveles en -_DocumentProperties, primero al nivel Mesh, luego al subnivel Custom dentro de Mesh.  Necesita un Enter para salir del subnivel y volver al nivel principal, y otro más para salir del comando.  Algunos guiones pueden necesitar incluso tres entradas.  

La siguiente macro es de Jeff LaSor, para activar o desactivar el cursor en cruz:

Para activar (ON) o desactivar (OFF) el cursor en cruz, ponga lo siguiente en un botón:

```
  -_Options _Appearance _Visibility
  _Crosshairs _Enter _Enter _Enter
```
Observe la referencia a cada nombre de opción de comando individual.  Especificarlos dentro del script es como hacer clic sobre ellos con el ratón.  Fíjese también en las tres entradas Enter.  Dado que cada opción de comando lleva a un nuevo conjunto de opciones de comando de subnivel, es necesario pulsar Intro para volver a subir.  Como este script bajó tres niveles, necesita especificar tres Enter para salir del todo del comando.

O, si simplemente usa un signo de exclamación `!` al final (que en un script significa "terminar ahora"), le lleva hasta el final sin importar en cuántos subniveles esté. Tenga en cuenta que, si quiere continuar su macro con algo más, no use `!`, use los Enter en su lugar; de lo contrario, la macro siempre se detendrá en el `!` y terminará.

El script simplemente activa y desactiva el cursor en cruz. Pero si quisiera un script que siempre lo activara y otro que siempre lo desactivara, sería así:

Versión activar siempre:

```
  -_Options _Appearance _Visibility
  _Crosshairs=_Show !
</code>
Versión desactivar siempre:
<code>
  -_Options _Appearance _Visibility
  _Crosshairs=_Hide !
```

Fíjese en el uso de `!` aquí. Además, tenga en cuenta que puede asignar directamente los valores que pueden adquirir las opciones en esa opción utilizando el operador '='.  La opción CursorEnCruz tiene dos valores posibles, "Mostrar" y "Ocultar", y por tanto, eso es lo que se utiliza en la asignación.

(Gracias, Jeff)

## Otras herramientas y comandos útiles para escribir macros

Hay algunos trucos útiles para hacer macros más complejas.  Uno de ellos es el uso discriminado de varios filtros de selección, en particular `SelLast`, que selecciona el último objeto creado/transformado, `SelPrev`, que selecciona el objeto de entrada anterior, y `SelNone`, que anula la selección de todo.  También existe la posibilidad de nombrar objetos, agruparlos (y nombrar el grupo) y recuperarlos más tarde con ese nombre de objeto o de grupo.

```
Select
SelLast
SelPrev
SelNone
SetObjectName
SetGroupName
SelGroup
SelName
Group
Ungroup
```

Para definir un único nombre de objeto (esto en sí mismo es una macro!):

```
  _Properties _Pause _Object _Name
  [ponga aquí el nombre de su objeto] _Enter _Enter
```

Para cancelar el nombre de un objeto (sin borrar el objeto)

```
  _Properties _Pause _Object _Name
  “ “ _Enter _Enter (comillas espacio comillas para el nombre)
```

## Ejemplos de uso de las herramientas anteriores

Observe la siguiente macro:

```
_Select _Pause _Setredrawoff
_BoundingBox _World _Enter
_Selnone _Sellast
_OffsetSrf _Solid _Pause
_Delete _Sellast
_BoundingBox _World _Enter
_Delete _Setredrawon
```

Crea un cuadro delimitador con desfase alrededor de un objeto. El desfase lo introduce el usuario.  A ver si puede seguir la secuencia lógica.  Setredrawoff/on detiene/reinicia la actualización de la pantalla, elimina el parpadeo de la pantalla mientras se ejecuta todo y acelera el proceso.  Cuidado, si termina el comando antes del Setredrawon, pensará que Rhino se ha colgado, ya que la pantalla ya no se actualiza.  Si esto ocurre, que no cunda el pánico, escriba el comando `_Setredrawon` y se restablecerá la actualización de la pantalla.

**Como ejemplo final,** la siguiente macro crea un punto centrado en un objeto 2D plano o de texto y agrupado. Asume que está en la misma vista en la que se creó el texto y que el objeto es realmente 2D y plano. (De lo contrario, es probable que no funcione).

Observe que se usa un grupo con nombre y varios comandos de selección.  El comando `NoEcho` detiene temporalmente la información de la línea de comandos, lo cual, combinado con Setredrawoff/on hace que la macro se ejecute sin parpadeos y sin demasiada información en el historial de comandos.  Sin embargo, también funcionará sin ellos.

```
_Select _Pause _Noecho _Setredrawoff
_Group _Enter _SetGroupName TexTemp
_BoundingBox _CPlane _Enter
_SelNone _SelLast _PlanarSrf
_SelPrev _Delete _SelLast
_AreaCentroid _Delete
_Sellast _SelGroup TexTemp
_Ungroup _Group _Setredrawon
```

**Si lo desea, puede ampliar o modificar este tutorial.**
Se trata de un trabajo en progreso...

## Temas relacionados

- [Sintaxis básica de Python](/guides/rhinopython/)
- [RhinoScript](/guides/rhinoscript/)
- [Tema de ayuda sobre sintaxis de macros](http://docs.mcneel.com/rhino/6/help/en-us/information/rhinoscripting.htm)
- [Ejecutar una macro](/guides/rhinoscript/running-scripts-from-macros/)

+++
aliases = ["/en/5/guides/general/essential-mathematics/vector-mathematics/", "/en/6/guides/general/essential-mathematics/vector-mathematics/", "/en/7/guides/general/essential-mathematics/vector-mathematics/", "/en/wip/guides/general/essential-mathematics/vector-mathematics/"]
authors = [ "rajaa" ]
categories = [ "Essential Mathematics" ]
category_page = "guides/general/essential-mathematics/"
description = "Esta guía trata las matemáticas vectoriales, incluida la representación de vectores, las operaciones vectoriales y las ecuaciones de líneas y planos."
keywords = [ "mathematics", "geometry", "grasshopper3d" ]
languages = "unset"
sdk = [ "General" ]
title = "1 Matemáticas vectoriales"
type = "guides"
weight = 1
override_last_modified = "2021-06-03T20:37:31Z"

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
Un vector representa un parámetro, como la velocidad o la fuerza, que tiene dirección y longitud. Los vectores en sistemas de coordenadas 3D se representan con un conjunto ordenado de tres números reales de la forma:

{{< mathjax >}}$$\mathbf{\vec v}  = <a_1, a_2, a_3>$${{< /mathjax >}}

{{< youtube NU34_aCoN3E >}}

## 1.1 Representación vectorial

En este documento, las letras minúsculas en negrita representarán los vectores. Los componentes de un vector también se representarán entre paréntesis angulares. Las letras mayúsculas representarán los puntos. Las coordenadas de los puntos siempre se representarán entre paréntesis.

Utilizando un sistema de coordenadas y cualquier conjunto de puntos de anclaje en ese sistema, podemos representar o visualizar estos vectores  dibujándolos como el segmento de una línea. Dibujamos también la punta de una flecha para representar la dirección de los vectores.

Por ejemplo, si tenemos un vector que tiene una dirección paralela al eje x de un sistema de coordenadas dado y una magnitud de 5 unidades, podemos escribir el vector de la siguiente manera:

{{< mathjax >}}$$\mathbf{\vec v} = <5, 0, 0>$${{< /mathjax >}}  

Para representar ese vector, necesitamos un punto de anclaje en el sistema de coordenadas. Por ejemplo, todas las flechas de la siguiente figura son representaciones iguales del mismo vector a pesar de que están ancladas en diferentes ubicaciones.  

<figure>
   <img src="/images/math-image169.png">
   <figcaption>Figura (1): Representación de vectores en el sistema de coordenadas 3D.</figcaption>
</figure>  

{{< call-out note "Note" >}}

Dado un vector 3D {{< mathjax >}}$$\vec v = <a_1, a_2, a_3>$${{< /mathjax >}} , todos los componentes de los vectores {{< mathjax >}}$$a_1$${{< /mathjax >}}, {{< mathjax >}}$a_2$${{< /mathjax >}}, {{< mathjax >}}$a_3$${{< /mathjax >}} son números reales. Además, todos los segmentos de línea desde un punto {{< mathjax >}}$$A(x,y,z)$${{< /mathjax >}} hasta otro punto {{< mathjax >}}$$B(x+a_1, y+a_2, z+a_3)$${{< /mathjax >}} son representaciones equivalentes del vector {{< mathjax >}}$$\vec v$${{< /mathjax >}}.

{{< /call-out >}}   

Entonces, ¿cómo definimos los puntos finales de un segmento de línea que representa un vector dado?
Definamos un punto de anclaje (A) de modo que:

{{< mathjax >}}$$A = (1, 2, 3)$${{< /mathjax >}}

Y un vector:

{{< mathjax >}}$$\mathbf{\vec v} = <5, 6, 7>$${{< /mathjax >}}

El punto extremo {{< mathjax >}}$$(B)$${{< /mathjax >}} del vector se calcula sumando los componentes correspondientes del punto de anclaje y el vector {{< mathjax >}}$$\vec v$${{< /mathjax >}}:  

{{< mathjax >}}$$B = A + \mathbf{\vec v}$${{< /mathjax >}}  
{{< mathjax >}}$$B = (1+5, 2+6, 3+7) $${{< /mathjax >}}  
{{< mathjax >}}$$B = (6, 8, 10)$${{< /mathjax >}}  


<figure>
   <img src="/images/math-image172.png">
   <figcaption>Figura (2): La relación entre un vector, el punto de anclaje del vector y el punto que coincide con la ubicación del extremo del vector.</figcaption>
</figure>  

{{< youtube ELQ8NgENhJY >}}
{{< youtube INtNgczxyWg >}}

### Vector de posición

Existe una representación especial de vectores que utiliza el {{< mathjax >}}$$\text{punto de origen} (0,0,0)$${{< /mathjax >}} como punto de anclaje del vector.
El vector de posición {{< mathjax >}}$$\mathbf{\vec v} = <a_1,a_2,a_3>$${{< /mathjax >}} se representa con un segmento de línea entre dos puntos, el origen y B, de modo que:  

{{< mathjax >}}$$\text{Punto de origen} = (0,0,0)$${{< /mathjax >}}  
{{< mathjax >}}$$B = (a_1,a_2,a_3)$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image171.png">
   <figcaption>Figura (3): Vector de posición. Las coordenadas del punto extremo son iguales a los componentes del vector correspondiente.</figcaption>
</figure>  

{{< call-out note "Note" >}}

Un *vector de posición* de un vector dado {{< mathjax >}}$$\vec v= < a_1,a_2,a_3 >$${{< /mathjax >}} es una representación especial del segmento de línea desde el punto de origen {{< mathjax >}}$$(0,0,0)$${{< /mathjax >}} al punto {{< mathjax >}}$$(a_1, a_2, a_3)$${{< /mathjax >}}.

{{< /call-out >}}

{{< youtube 8BNyMC4EBcw >}}

{{< youtube Ft2edI4g1qY >}}

### Vectores y puntos  

Es importante no confundir vectores con puntos. Son conceptos muy diferentes. Los vectores, como mencionamos, representan una cantidad que tiene dirección y longitud, mientras que los puntos indican una ubicación. Por ejemplo, la dirección norte es un vector, mientras que el polo norte es una ubicación (punto).
Si tenemos un vector y un punto que tienen los mismos componentes, como por ejemplo:  

{{< mathjax >}}$$\mathbf{\vec v} = <3,1,0>$${{< /mathjax >}}  
{{< mathjax >}}$$P = (3,1,0)$${{< /mathjax >}}  

Podemos dibujar el vector y el punto de la siguiente manera:  

<figure>
   <img src="/images/math-image174.png">
   <figcaption>Figura (4): Un vector define una dirección y una longitud. Un punto define una ubicación.</figcaption>
</figure>  

{{< youtube RRrTz_QO_rA >}}

### Longitud vectorial  

Como se ha mencionado anteriormente, los vectores tienen longitud. Usaremos {{< mathjax >}}$$\vert a \vert$${{< /mathjax >}} para representar la longitud de un vector dado {{< mathjax >}}$$ a $${{< /mathjax >}}. Por ejemplo:  

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = 5$${{< /mathjax >}}  

En general, la longitud de un vector {{< mathjax >}}$$\mathbf{\vec a} <a_1,a_2,a_3>$${{< /mathjax >}} se calcula de la siguiente manera:

{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{(a_1)^2 + (a_2)^2 + (a_3)^2} $${{< /mathjax >}}

<figure>
   <img src="/images/math-image173.png">
   <figcaption>Figura (5): Longitud del vector.</figcaption>
</figure>  

### Vector unitario

Un vector unitario es un vector con una longitud igual a una unidad. Los vectores unitarios se utilizan comúnmente para comparar las direcciones de los vectores.

{{< call-out note "Note" >}}

Un vector unitario es un vector cuya longitud es igual a una unidad.

{{< /call-out >}}

Para calcular un vector unitario, necesitamos encontrar la longitud del vector dado y luego dividir los componentes del vector por la longitud. Por ejemplo:

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec a} \vert  = 5 \text{ unidades de longitud}$${{< /mathjax >}}  

Si {{< mathjax >}}$$\mathbf{\vec b} = \text{vector unitario}$${{< /mathjax >}} de {{< mathjax >}}$$a$${{< /mathjax >}}, entonces:  
&nbsp;&nbsp;     {{< mathjax >}}$$\mathbf{\vec b} = <4/5, 3/5, 0/5>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\mathbf{\vec b} = <0.8, 0.6, 0>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{0.8^2 + 0.6^2 + 0^2}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{0.64 + 0.36 + 0}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{(1)} = 1 \text{ unidad de longitud}$${{< /mathjax >}}  

En general:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  

El vector unitario de {{< mathjax >}}$$\mathbf{\vec a} = <a_1/\vert \mathbf{\vec a} \vert , a_2/\vert \mathbf{\vec a} \vert , a_3/\vert \mathbf{\vec a} \vert >$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image176.png">
   <figcaption>Figura (6): El vector unitario es igual a una unidad de longitud del vector.</figcaption>
</figure>  

{{< youtube yVSigpl3EUo >}}

## 1.2 Operaciones vectoriales

{{< youtube uInxocphhxI >}}

### Operación escalar de vectores

La operación escalar de vectores implica multiplicar un vector por un número. Por ejemplo:  

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$2* \mathbf{\vec a} = <2*4, 2*3, 2*0> $${{< /mathjax >}}  
{{< mathjax >}}$$2*\mathbf{\vec a} = <8, 6, 0>$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image175.png">
   <figcaption>Figura (7): Operación escalar de vectores</figcaption>
</figure>  

En general, dado el vector {{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}} y un número real {{< mathjax >}}$$t$${{< /mathjax >}}   

{{< mathjax >}}$$t*\mathbf{\vec a} = < t* a_1, t* a_2, t* a_3 >$${{< /mathjax >}}  

{{< youtube S59M8BnDYAQ >}}

### Suma de vectores

La suma de vectores toma dos vectores y se obtiene un tercer vector. Sumamos vectores añadiendo sus componentes.

{{< call-out note "Note" >}}

Los vectores se suman añadiendo sus componentes.

{{< /call-out >}}

Por ejemplo, si tenemos dos vectores:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 0> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <4, 1, 3> $${{< /mathjax >}}   
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <1+4, 2+1, 0+3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <5, 3, 3>$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image179.png">
   <figcaption>Figura (8): Adición de vectores.</figcaption>
</figure>  

En general, la suma de vectores de los dos vectores a y b se calcula de la siguiente manera:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <a_1+b_1, a_2+b_2, a_3+b_3>$${{< /mathjax >}}  

La suma de vectores es útil para hallar la dirección media de dos o más vectores. En estos casos, solemos usar vectores de la misma longitud. Este es un ejemplo que muestra la diferencia entre emplear vectores de iguales o de diferentes longitudes en la resultante de la suma de dichos vectores:  

<figure>
   <img src="/images/math-image177.png">
   <figcaption>Figura (9): Suma de varios vectores de longitud (izquierda). Suma de vectores de la misma longitud (derecha) para obtener la dirección media.</figcaption>
</figure>  

Es probable que los vectores de entrada no tengan la misma longitud. Para encontrar la dirección media, tiene que utilizar el vector unitario de los vectores de entrada. Como se ha mencionado anteriormente, el vector unitario es un vector de que tiene una longitud igual a 1.

{{< youtube VTVk3t3WeAY >}}

### Resta de vectores

La resta de vectores toma dos vectores y se obtiene un tercer vector. Restamos dos vectores restando los componentes correspondientes. Por ejemplo, si tenemos dos vectores {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} and {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} y restamos {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} de {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, entonces:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 0> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <4, 1, 4> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <1-4, 2-1, 0-4>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <-3, 1, -4> = \mathbf{\mathbf{\vec b}a}$${{< /mathjax >}}

Si restamos {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} de {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, obtenemos un resultado diferente:  

{{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a} = <4-1, 1-2, 4-0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a} = <3, -1, 4> = \mathbf{\mathbf{\vec a}b}$${{< /mathjax >}}  

Observe que el vector {{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a}$${{< /mathjax >}} tiene la misma longitud que el vector {{< mathjax >}}$$$\mathbf{\vec a} - \mathbf{\vec b}$${{< /mathjax >}}, pero va en sentido contrario.  

<figure>
   <img src="/images/math-image178.png">
   <figcaption>Figura (10): Resta de vectores.</figcaption>
</figure>  

En general, si tenemos dos vectores, {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} y {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}, entonces {{< mathjax >}}$$$\mathbf{\vec a} - \mathbf{\vec b}$${{< /mathjax >}} es un vector que se calcula de la siguiente manera:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <a_1 - b_1, a_2 - b_2, a_3 - b_3> = \mathbf{\mathbf{\vec b}a}$${{< /mathjax >}}  

La resta de vectores se suele usar para hallar vectores entre puntos. Por lo tanto, si necesitamos hallar un vector que vaya desde el punto extremo del vector de posición {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} al punto extremo del vector de posición {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, usamos la resta de vectores {{< mathjax >}}$$(\mathbf{\vec a}-\mathbf{\vec b})$${{< /mathjax >}} como se muestra en la Figura (11).  

<figure>
   <img src="/images/math-image180.png">
   <figcaption>Figura (11): Utilice la resta de vectores para hallar un vector entre dos puntos. </figcaption>
</figure> 

{{< youtube RQK8pCIWKNY >}} 

### Propiedades de los vectores

Los vectores tienen ocho propiedades fundamentales. Si a, b y c son vectores, y s y t son números, entonces:  

{{< mathjax >}}$$\mathbf{\vec a} + \mathbf{\vec b} = \mathbf{\vec b} + \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + 0 = a$${{< /mathjax >}}  
{{< mathjax >}}$$s * (\mathbf{\vec a} + \mathbf{\vec b}) = s * a + s * \mathbf{\vec b}$${{< /mathjax >}}  
{{< mathjax >}}$$s * t * (\mathbf{\vec a}) = s * (t * \mathbf{\vec a})$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + (\mathbf{\vec b} + \mathbf{\vec c}) = (\mathbf{\vec a} + \mathbf{\vec b}) + \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + (-\mathbf{\vec a}) = 0$${{< /mathjax >}}  
{{< mathjax >}}$$(s + t) * \mathbf{\vec a} = s * \mathbf{\vec a} + t * \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$1 * \mathbf{\vec a} = \mathbf{\vec a}$${{< /mathjax >}}  

### Producto escalar de vectores

El producto escalar toma dos vectores y se obtiene un número.
Por ejemplo, si tenemos los dos vectores a y b de modo que:

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 3> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <5, 6, 7>$${{< /mathjax >}}  

Entonces el producto escalar es la suma de multiplicar los componentes de la siguiente manera:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = 1 * 5 + 2 * 6 + 3 * 7$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = 38$${{< /mathjax >}}  

En general, dados los dos vectores a y b:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = a_1 * b_1 + a_2 * b_2 + a_3 * b_3$${{< /mathjax >}}  

Siempre obtenemos un número positivo del producto escalar entre dos vectores cuando van en la misma dirección general. Un producto escalar negativo entre dos vectores significa que los dos vectores van en la dirección general opuesta.

<figure>
   <img src="/images/math-image181.png">
   <figcaption>Figura (12): Cuando los dos vectores van en la misma dirección (izquierda), el resultado es un producto escalar positivo. Cuando los dos vectores van en la dirección opuesta (derecha), el resultado es un producto escalar negativo. </figcaption>
</figure>  

Al calcular el producto escalar de dos vectores unitarios, el resultado siempre está entre 1 y +1. Por ejemplo:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <0,6, 0,8, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = (1 * 0.6, 0 * 0.8, 0 * 0) = 0.6$${{< /mathjax >}}  

Además, el producto escalar de un vector consigo mismo es igual a la longitud de ese vector elevado a dos. Por ejemplo:  

{{< mathjax >}}$$\mathbf{\vec a} = <0, 3, 4>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = 0 * 0 + 3 * 3 + 4 * 4 $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = 25$${{< /mathjax >}}  

Cálculo de la longitud cuadrada del vector {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}:  

{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = 5$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert 2 = 25$${{< /mathjax >}}  

### Producto escalar de vectores, longitudes y ángulos

Existe una relación entre el producto escalar de dos vectores y el ángulo entre ellos.  

{{< call-out note "Note" >}}

El producto escalar de dos vectores unitarios distintos a cero es igual al coseno del ángulo entre ellos.

{{< /call-out >}}

En general:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = \vert \mathbf{\vec a} \vert * \vert \mathbf{\vec b} \vert * cos(ө)$${{< /mathjax >}} , o bien  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} / (\vert \mathbf{\vec a} \vert * \vert \mathbf{\vec b} \vert) = cos(ө)$${{< /mathjax >}}

Donde:  

{{< mathjax >}}$$ө$${{< /mathjax >}} es el ángulo incluido entre los vectores.  

Si los vectores a y b son vectores unitarios, podemos decir que:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = cos(ө)$${{< /mathjax >}}  

Y dado que el coseno de un ángulo de 90 grados es igual a 0, podemos decir que:  

{{< call-out note "Note" >}}

Los vectores {{< mathjax >}}$$\vec a$${{< /mathjax >}} y {{< mathjax >}}$$\vec b$${{< /mathjax >}} son ortogonales si, y solo si, {{< mathjax >}}$$\vec{a} \cdot \vec{b} = 0$${{< /mathjax >}}.

{{< /call-out >}}

Por ejemplo, si calculamos el producto escalar de los dos vectores ortogonales, el eje x y el eje y universales, el resultado será igual a cero.  

{{< mathjax >}}$$\mathbf{\vec x} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec y} = <0, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec x} · \mathbf{\vec y} = (1 * 0) + (0 * 1) + (0 * 0)$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec x} · \mathbf{\vec y} = 0$${{< /mathjax >}}  

También existe una relación entre el producto escalar y la longitud de proyección de un vector sobre otro. Por ejemplo:  

{{< mathjax >}}$$\mathbf{\vec a} = <5, 2, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <9, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$unidad(\mathbf{\vec b}) = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · unidad(\mathbf{\vec b}) = (5 * 1) + (2 * 0) + (0 * 0) $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} - unidad(\mathbf{\vec b}) = 2 (\text{que es igual a la longitud de proyección de mathbf{\vec a} sobre mathbf{\vec b}})$${{< /mathjax >}}

<figure>
   <img src="/images/math-image182.png">
   <figcaption>Figura (13): El producto escalar es igual a la longitud de proyección de un vector sobre un vector unitario distinto a cero. </figcaption>
</figure>  

En general, dado un vector a y un vector distinto a cero b, podemos calcular la longitud de proyección pL del vector a sobre el vector b utilizando el producto escalar.  

{{< mathjax >}}$$pL = \vert \mathbf{\vec a} \vert * cos(ө) $${{< /mathjax >}}  
{{< mathjax >}}$$pL = \mathbf{\vec a} · unidad(\mathbf{\vec b})$${{< /mathjax >}} 

 {{< youtube ZsM2RQbVDf4 >}}

### Propiedades del producto escalar

Si {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} y {{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} son vectores y s es un número, entonces:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = \vert  \mathbf{\vec a} \vert ^2$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b} + \mathbf{\vec c}) = \mathbf{\vec a} · \mathbf{\vec b} + \mathbf{\vec a} · \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$0 · \mathbf{\vec a} = 0$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = \mathbf{\vec b} · \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$(s * \mathbf{\vec a}) · \mathbf{\vec b} = s * (\mathbf{\vec a} · \mathbf{\vec b}) = \mathbf{\vec a} · (s * \mathbf{\vec b})$${{< /mathjax >}}  

### Producto vectorial

El producto vectorial toma dos vectores y se obtiene un tercer vector que es ortogonal a ambos.

<figure>
   <img src="/images/math-image183.png">
   <figcaption>Figura (14): Cálculo del producto vectorial de dos vectores. </figcaption>
</figure>  

Por ejemplo, si tiene dos vectores que se encuentran en el plano xy universal, entonces su producto vectorial es un vector perpendicular al plano xy que va en la dirección del eje z universal positivo o negativo. Por ejemplo:  

{{< mathjax >}}$$\mathbf{\vec a} = <3, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <1, 2, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = < (1 * 0 – 0 * 2), (0 * 1 - 3 * 0), (3 * 2 - 1 * 1) > $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <0, 0, 5>$${{< /mathjax >}}  

{{< call-out note "Note" >}}

El vector {{< mathjax >}}$$\vec a \times \vec b$${{< /mathjax >}} es ortogonal tanto a {{< mathjax >}}$$\vec a$${{< /mathjax >}} como a {{< mathjax >}}$$\vec b$${{< /mathjax >}}.

{{< /call-out >}}

Probablemente nunca tenga que calcular manualmente un producto vectorial de dos vectores, pero si tiene curiosidad sobre cómo se hace, continúe leyendo; si no, puede omitir esta sección. El producto vectorial {{< mathjax >}}$$a × b$${{< /mathjax >}} se resuelve utilizando determinantes. Esta ilustración simple muestra cómo calcular un determinante utilizando los vectores base estándar:  

{{< mathjax >}}$$ \color {red}{i} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$ \color {blue}{j} = <0,1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$ \color {green}{k} = <0, 0, 1>$${{< /mathjax >}}  

<img src="/images/math-image184.png">

El producto vectorial de los dos vectores {{< mathjax >}}$$\mathbf{\vec a} = <a1, a2, a3>$${{< /mathjax >}} y {{< mathjax >}}$$\mathbf{\vec b} = <b1, b2, b3>$${{< /mathjax >}} se calcula de la siguiente manera utilizando el diagrama anterior:  

{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = \color {red}{i (a_2 * b_3)} + \color {blue}{ j (a_3 * b_1)} + \color {green}{k(a_1 * b_2)} - \color {green}{k (a_2 * b_1)} - \color {red}{i (a_3 * b_2)} -\color {blue}{ j (a_1 * b_3)}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = \color {red}{i (a_2 * b_3 - a_3 * b_2)} + \color {blue}{j (a_3 * b_1 - a_1 * b_3)} +\color {green}{k (a_1 * b_2 - a_2 * b_1)}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <\color {red}{a_2 * b_3 – a_3 * b_2},  \color {blue}{a_3 * b_1 - a_1 * b_3},  \color {green}{a_1 * b_2 - a_2 * b_1} >$${{< /mathjax >}}  

{{< youtube I5WkhSo4p6o >}}

### Producto vectorial y ángulo entre vectores

Existe una relación entre el ángulo entre dos vectores y la longitud de su producto vectorial. Cuanto menor sea el ángulo (seno más pequeño), más corto será el producto vectorial. El orden de los operandos es importante en los productos vectoriales. Por ejemplo:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <0, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <0, 0, 1>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} × \mathbf{\vec a} = <0, 0, -1>$${{< /mathjax >}}  


<figure>
   <img src="/images/math-image185.png">
   <figcaption>Figura (15): Existe una relación entre el ángulo entre dos vectores y la longitud de su producto vectorial.</figcaption>
</figure>  

En el sistema diestro de Rhino, la dirección de {{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b}$${{< /mathjax >}} viene dada por la regla de la mano derecha (donde {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} = dedo índice, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} = dedo corazón y {{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b}$${{< /mathjax >}} = pulgar).  

<img src="/images/math-image186.png" width="375px">  

En general, para cualquier par de vectores 3D {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} y {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}:  

{{< mathjax >}}$$\vert \mathbf{\vec a} × \mathbf{\vec b} \vert  = \vert  \mathbf{\vec a} \vert  \vert  \mathbf{\vec b} \vert  sin(ө)$${{< /mathjax >}}  

Donde:   

{{< mathjax >}}$$ө$${{< /mathjax >}} es el ángulo incluido entre los vectores de posición de {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} y {{< mathjax >}}$$\mathbf{\vec b}$$${{< /mathjax >}}  

Si a y b son vectores unitarios, entonces podemos decir que la longitud de su producto vectorial es igual al seno del ángulo entre ellos. En otras palabras:  

{{< mathjax >}}$$\vert \mathbf{\vec a} × \mathbf{\vec b} \vert = sin(ө)$${{< /mathjax >}}  

El producto vectorial entre dos vectores nos ayuda a determinar si dos vectores son paralelos. Esto se debe a que el resultado es siempre un vector cero.  

{{< call-out note "Note" >}}

Los vectores {{< mathjax >}}$$\vec a$${{< /mathjax >}} y {{< mathjax >}}$$\vec b$${{< /mathjax >}} son paralelos si, y solo si, {{< mathjax >}}$$a \times b = 0$${{< /mathjax >}}.

{{< /call-out >}}

### Propiedades del producto vectorial

Si {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} y {{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} son vectores, y {{< mathjax >}}$$s$${{< /mathjax >}} es un número, entonces:  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = -\mathbf{\vec b} × \mathbf{\vec a}$${{< /mathjax >}}   
{{< mathjax >}}$$(s * \mathbf{\vec a}) × \mathbf{\vec b} = s * (\mathbf{\vec a} × \mathbf{\vec b}) = \mathbf{\vec a} × (s * \mathbf{\vec b})$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × (\mathbf{\vec b} + \mathbf{\vec c}) = \mathbf{\vec a} × \mathbf{\vec b} + \mathbf{\vec a} × \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$(\mathbf{\vec a} + \mathbf{\vec b}) × \mathbf{\vec c} = \mathbf{\vec a} × \mathbf{\vec c} + \mathbf{\vec b} × \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b} × \mathbf{\vec c}) = (\mathbf{\vec a} × \mathbf{\vec b}) · \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × (\mathbf{\vec b} × \mathbf{\vec c}) = (\mathbf{\vec a} · \mathbf{\vec c}) * \mathbf{\vec b} – (\mathbf{\vec a} · \mathbf{\vec b}) * \mathbf{\vec c}$${{< /mathjax >}}  

## 1.3 Ecuación vectorial de una línea

La ecuación vectorial de una línea se utiliza en aplicaciones de modelado 3D y diseño gráfico por ordenador.

<figure>
   <img src="/images/math-image187.png">
   <figcaption>Figura (16): Ecuación vectorial de una línea.</figcaption>
</figure>  

Por ejemplo, si sabemos la dirección de una línea y un punto en esa línea, podemos hallar cualquier otro punto en la línea utilizando vectores, como se muestra a continuación:

{{< mathjax >}}$$\overline{L} = line$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec v} = <a, b, c>$${{< /mathjax >}} vector unitario de dirección de la línea  
{{< mathjax >}}$$Q = (x_0, y_0, z_0)$${{< /mathjax >}} punto de posición de la línea  
{{< mathjax >}}$$P = (x, y, z)$${{< /mathjax >}} cualquier punto en la línea  

Sabemos que:  

{{< mathjax >}}$$\mathbf{\vec a} = t *\mathbf{\vec v}$${{< /mathjax >}}   (2)  
{{< mathjax >}}$$\mathbf{\vec p} = \mathbf{\vec q} + \mathbf{\vec a}$${{< /mathjax >}}   (1)  

A partir de 1 y 2:  

{{< mathjax >}}$$\mathbf{\vec p} = \mathbf{\vec q} + t * \mathbf{\vec v}$${{< /mathjax >}}  (3)   

Sin embargo, también podemos expresar (3) de la siguiente manera:  

{{< mathjax >}}$$<x, y, z> = <x_0, y_0, z_0> + <t * a, t * b, t * c>$${{< /mathjax >}}  
{{< mathjax >}}$$<x, y, z> = <x_0 + t * a, y_0 + t * b, z_0 + t * c>$${{< /mathjax >}}  

Por tanto:  

{{< mathjax >}}$$x = x_0 + t * a$${{< /mathjax >}}  
{{< mathjax >}}$$y = y_0 + t * b$${{< /mathjax >}}  
{{< mathjax >}}$$z = z_0 + t * c$${{< /mathjax >}}  

Que es lo mismo que:  

{{< mathjax >}}$$P = Q + t * \mathbf{\vec v}$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Dado un punto {{< mathjax >}}$$Q$${{< /mathjax >}} y una dirección {{< mathjax >}}$$\vec v$${{< /mathjax >}} en una línea, cualquier punto {{< mathjax >}}$$P$${{< /mathjax >}} de esa línea se puede calcular utilizando la ecuación vectorial de una línea {{< mathjax >}}$$P = Q + t * \vec v$${{< /mathjax >}} donde {{< mathjax >}}$$t$${{< /mathjax >}} es un número.  

{{< /call-out >}}

Otro ejemplo común es hallar el punto medio entre dos puntos. A continuación, se muestra cómo encontrar el punto medio utilizando la ecuación vectorial de una línea:  

{{< mathjax >}}$$\mathbf{\vec q}$${{< /mathjax >}} es el vector de posición del punto {{< mathjax >}}$Q$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec p}$${{< /mathjax >}} es el vector de posición del punto {{< mathjax >}}$$P$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} es el vector que va desde {{< mathjax >}}$$Q \rightarrow P$${{< /mathjax >}}  

De la resta de vectores se obtiene que:  

{{< mathjax >}}$$\mathbf{\vec a} = \mathbf{\vec p} - \mathbf{\vec q}$${{< /mathjax >}}  

De la ecuación lineal se obtiene que:  

{{< mathjax >}}$$M = Q + t * \mathbf{\vec a}$${{< /mathjax >}}  

Y como necesitamos hallar el punto medio, entonces:  

{{< mathjax >}}$$t = 0.5$${{< /mathjax >}}  

Por tanto, podemos decir que:  

{{< mathjax >}}$$M = Q + 0.5 * \mathbf{\vec a}$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image159.png">
   <figcaption>Figura (17): Búsqueda del punto medio entre dos puntos de entrada.</figcaption>
</figure>  

En general, puede hallar cualquier punto entre {{< mathjax >}}$$Q$${{< /mathjax >}} y {{< mathjax >}}$$P$${{< /mathjax >}} cambiando el valor {{< mathjax >}}$$t$${{< /mathjax >}} entre 0 y 1 utilizando la ecuación general:  

{{< mathjax >}}$$M = Q + t * (P - Q)$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Dados dos puntos {{< mathjax >}}$$Q$${{< /mathjax >}} y {{< mathjax >}}$$P$${{< /mathjax >}}, cualquier punto {{< mathjax >}}$$M$${{< /mathjax >}} entre los dos puntos se calcula utilizando la ecuación {{< mathjax >}}$$M = Q + t * (P - Q)$${{< /mathjax >}} donde t es un número entre 0 y 1.

{{< /call-out >}}

## 1.4 Ecuación vectorial de un plano

Una forma de definir un plano es cuando hay un punto y un vector que es perpendicular al plano. Ese vector generalmente se conoce como normal al plano. La normal apunta en la dirección por encima del plano.  

Un ejemplo de cómo calcular la normal de un plano es cuando hay tres puntos no lineales en el plano.   

En la Figura (16), dados:  

{{< mathjax >}}$$A$${{< /mathjax >}} = el primer punto del plano  
{{< mathjax >}}$$B$${{< /mathjax >}} = el segundo punto del plano  
{{< mathjax >}}$$C$${{< /mathjax >}} = el tercer punto del plano  

Y:  

{{< mathjax >}}$$\mathbf{\vec a} $${{< /mathjax >}} = un vector de posición del punto {{< mathjax >}}$$A$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} = un vector de posición del punto {{< mathjax >}}$$B$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} = un vector de posición del punto {{< mathjax >}}$$C$${{< /mathjax >}}  

Podemos encontrar el vector de la normal {{< mathjax >}}$$\mathbf{\vec n}$${{< /mathjax >}} de la siguiente manera:  

{{< mathjax >}}$$\mathbf{\vec n} = (\mathbf{\vec b} - \mathbf{\vec a}) × (\mathbf{\vec c} - \mathbf{\vec a})$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image160.png">
   <figcaption>Figura (18): Vectores y planos</figcaption>
</figure>  

También podemos derivar la ecuación escalar del plano utilizando el producto escalar del vector:  

{{< mathjax >}}$$\mathbf{\vec n} · (\mathbf{\vec b} - \mathbf{\vec a}) = 0$${{< /mathjax >}}  

Si:  

{{< mathjax >}}$$\mathbf{\vec n} = <a, b, c>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <x, y, z>$${{< /mathjax >}}  
{{< mathjax >}}$$ \mathbf{\vec a} = <x_0, y_0, z_0>$${{< /mathjax >}}  

Entonces podemos ampliar lo anterior:  

{{< mathjax >}}$$<a, b, c> · <x-x_0, y-y_0, z-z_0 > = 0$${{< /mathjax >}}  

Resolver el producto escalar da la ecuación escalar general de un plano:  

{{< mathjax >}}$$a * (x - x_0) + b * (y - y_0) + c * (z - z_0) = 0$${{< /mathjax >}}  

## 1.5 Tutoriales

Todos los conceptos tratados en este capítulo tienen una aplicación directa para resolver problemas geométricos comunes que se encuentran durante el modelado. Los siguientes tutoriales paso a paso emplean los conceptos aprendidos en este capítulo utilizando Rhinoceros y Grasshopper (GH).

### 1.5.1 Dirección de cara
Dados un punto y una superficie, ¿cómo podemos determinar si el punto está orientado hacia la parte frontal o posterior de esa superficie?  

**Entrada:**  

1. Una superficie  
2. Un punto  

<img src="/images/math-image161.png">  

**Parámetros:**  

La dirección de la cara está definida por la dirección normal de la superficie. Necesitaremos la siguiente información:  

* La dirección normal de la superficie en una ubicación de superficie más cercana al punto de entrada.  
* Una dirección de vector desde el punto más cercano al punto de entrada.  

Compare las dos direcciones anteriores. Si van en la misma dirección, el punto está orientado hacia la parte frontal; de lo contrario, está orientado hacia la parte posterior.  

**Solución:**  

1\. Encuentre la ubicación del punto más cercano en la superficie en relación con el punto de entrada utilizando el componente Pull. Esto nos dará la ubicación uv del punto más cercano, que luego podemos usar para evaluar la superficie y hallar su dirección normal.  

<img src="/images/math-image162.png">  

2\. Ahora podemos usar el punto más cercano para dibujar un vector orientado hacia el punto de entrada. También podemos dibujar:  

<img src="/images/math-image163.png">  

3\. Podemos comparar los dos vectores utilizando el producto escalar. Si el resultado es positivo, el punto está delante de la superficie. Si el resultado es negativo, el punto está detrás de la superficie.  

<img src="/images/math-image164.png">  

Los pasos anteriores también se pueden resolver utilizando otros lenguajes de scripting. Uso del componente VB de Grasshopper:  

<img src="/images/math-image165.png">  

```vb
Private Sub RunScript(ByVal pt As Point3d, ByVal srf As Surface, ByRef A As Object)

  'Declare variables
  Dim u, v As Double
  Dim closest_pt As Point3d

  'get closest point u, v
  srf.ClosestPoint(pt, u, v)

  'get closest point
  closest_pt = srf.PointAt(u, v)

  'calculate direction from closest point to test point
  Dim dir As New Vector3d(pt - closest_pt)

  'calculate surface normal
  Dim normal = srf.NormalAt(u, v)

  'compare the two directions using the dot product
  A = dir * normal
End Sub
```

Uso del componente Python de Grasshopper con RhinoScriptSyntax:

<img src="/images/math-image14.png">  

```python
import rhinoscriptsyntax as rs #import RhinoScript library

#find the closest point
u, v = rs.SurfaceClosestPoint(srf, pt)

#get closest point
closest_pt = rs.EvaluateSurface(srf, u, v)

#calculate direction from closest point to test point
dir = rs.PointCoordinates(pt) - closest_pt

#calculate surface normal
normal = rs.SurfaceNormal(srf, [u, v])

#compare the two directions using the dot product
A = dir * normal
```



Uso del componente Python de Grasshopper solo con RhinoCommon:

<img src="/images/math-image13.png">  

```python
#find the closest point
found, u, v = srf.ClosestPoint(pt)

if found:

    #get closest point
    closest_pt = srf.PointAt(u, v)

    #calculate direction from closest point to test point
    dir = pt - closest_pt

    #calculate surface normal
    normal = srf.NormalAt(u, v)

    #compare the two directions using the dot product
    A = dir * normal
```



Uso del componente C# de Grasshopper:  

<img src="/images/math-image165.png">  

```cs
private void RunScript(Point3d pt, Surface srf, ref object A)
{
  //Declare variables
  double u, v;
  Point3d closest_pt;

  //get closest point u, v
  srf.ClosestPoint(pt, out u, out v);

  //get closest point
  closest_pt = srf.PointAt(u, v);

  //calculate direction from closest point to test point
  Vector3d dir = pt - closest_pt;

  //calculate surface normal
  Vector3d normal = srf.NormalAt(u, v);

  //compare the two directions using the dot product
  A = dir * normal;
}
```

### 1.5.2 Caja descompuesta  

El siguiente tutorial muestra cómo descomponer una polisuperficie. Así es como queda la caja descompuesta al final:   

<img src="/images/math-image15.jpg">  

**Entrada:**  

Identifique la entrada, que es una caja. 

<img src="/images/math-image17.jpg">  

**Parámetros:**  

* Piense en todos los parámetros que tenemos que conocer para este tutorial.  
* El centro de la descomposición.  
* Las caras de la caja que estamos descomponiendo.  
* La dirección hacia la que se mueve cada cara.   


<img src="/images/math-image19.jpg">  

Una vez identificados los parámetros, es cuestión de juntarlos en una solución uniendo los pasos lógicos para lograr una respuesta.

**Solución:**

1\. Encuentre el centro de la caja utilizando el componente **Box Properties** en GH:

<img src="/images/math-image21.png">  

2\. Extraiga las caras de la caja con el componente **Deconstruct Brep**:

<img src="/images/math-image23.png">

3\. La dirección hacia la que movemos las caras es la parte complicada. Primero debemos encontrar el centro de cada cara y luego definir la dirección desde el centro de la caja hacia el centro de cada cara de la siguiente manera:

<img src="/images/math-image25.png">

4\. Una vez tengamos todos los parámetros listos, podemos usar el componente **Move** para mover las caras en la dirección adecuada. Asegúrese de configurar la amplitud deseada de los vectores y ya podrá empezar.

<img src="/images/math-image27.png">

Los pasos anteriores también se pueden resolver mediante VB script, C# o Python. A continuación se muestra la solución con estos lenguajes de scripting.

Uso del componente VB de Grasshopper:

<img src="/images/math-image29.png">

```vb
Private Sub RunScript(ByVal box As Brep, ByVal dis As Double, ByRef A As Object)

    'get the brep center
    Dim area As Rhino.Geometry.AreaMassProperties
    area = Rhino.Geometry.AreaMassProperties.Compute(box)

    Dim box_center As Point3d
    box_center = area.Centroid

    'get a list of faces
    Dim faces As Rhino.Geometry.Collections.BrepFaceList = box.Faces

    'decalre variables
    Dim center As Point3d
    Dim dir As Vector3d
    Dim exploded_faces As New List( Of Rhino.Geometry.Brep )
    Dim i As Int32
    'loop through all faces

    For i = 0 To faces.Count() - 1
      'extract each of the face
      Dim extracted_face As Rhino.Geometry.Brep = box.Faces.ExtractFace(i)

      'get the center of each face
      area = Rhino.Geometry.AreaMassProperties.Compute(extracted_face)
      center = area.Centroid

      'calculate move direction (from box centroid to face center)
      dir = center - box_center
      dir.Unitize()
      dir *= dis

      'move the extracted face
      extracted_face.Transform(Transform.Translation(dir))

      'add to exploded_faces list
      exploded_faces.Add(extracted_face)
    Next

    'assign exploded list of faces to output
    A = exploded_faces
  End Sub
```
Uso del componente Python de Grasshopper con RhinoCommon:

<img src="/images/math-image4.png">

```python
import Rhino

#get the brep center
area = Rhino.Geometry.AreaMassProperties.Compute(box)
box_center = area.Centroid

#get a list of faces
faces = box.Faces

#decalre variables
exploded_faces = []

#loop through all faces
for i, face in enumerate(faces):

	#get a duplicate of the face
	extracted_face = faces.ExtractFace(i)
	
	#get the center of each face
	area = Rhino.Geometry.AreaMassProperties.Compute(extracted_face)
	center = area.Centroid
	
	#calculate move direction (from box centroid to face center)
	dir = center - box_center
	dir.Unitize()
	dir *= dis
	
	#move the extracted face
	move = Rhino.Geometry.Transform.Translation(dir)
	extracted_face.Transform(move)
	
	#add to exploded_faces list
	exploded_faces.append(extracted_face)

#assign exploded list of faces to output
A = exploded_faces
```

Uso del componente C# de Grasshopper:

<img src="/images/math-image2.png">

```cs
private void RunScript(Brep box, double dis, ref object A)
{

    //get the brep center
  Rhino.Geometry.AreaMassProperties area =        Rhino.Geometry.AreaMassProperties.Compute(box);
  Point3d box_center = area.Centroid;

  //get a list of faces
  Rhino.Geometry.Collections.BrepFaceList faces = box.Faces;

  //decalre variables
  Point3d center;   Vector3d dir;
  List<Rhino.Geometry.Brep> exploded_faces = new List<Rhino.Geometry.Brep>();

  //loop through all faces   for( int i = 0; i < faces.Count(); i++ )
  {
    //extract each of the face
    Rhino.Geometry.Brep extracted_face = box.Faces.ExtractFace(i);

    //get the center of each face
    area = Rhino.Geometry.AreaMassProperties.Compute(extracted_face);
    center = area.Centroid;

    //calculate move direction (from box centroid to face center)
    dir = center - box_center;
    dir.Unitize();
    dir *= dis;

    //move the extracted face
    extracted_face.Transform(Transform.Translation(dir));

    //add to exploded_faces list
    exploded_faces.Add(extracted_face);
  }

  //assign exploded list of faces to output
  A = exploded_faces;
}
```

### 1.5.3 Esferas tangentes

Este tutorial muestra cómo crear dos esferas tangentes entre dos puntos de entrada.
El resultado será el siguiente:

<img src="/images/math-image5.png">

**Entrada:**  
Dos puntos ({{< mathjax >}}$$A$${{< /mathjax >}} y {{< mathjax >}}$$B$${{< /mathjax >}}) en el sistema de coordenadas 3D.

<img src="/images/math-image6.png">

Parámetros:
A continuación, se muestra un diagrama de los parámetros que necesitaremos para resolver el problema:
{{< mathjax >}}$$A$${{< /mathjax >}} punto tangente {{< mathjax >}}$$D$${{< /mathjax >}} entre las dos esferas, en algún parámetro {{< mathjax >}}$$t$${{< /mathjax >}} (0-1) entre los puntos {{< mathjax >}}$$A$${{< /mathjax >}} y {{< mathjax >}}$$B$${{< /mathjax >}}.

* El centro de la primera esfera o el punto medio {{< mathjax >}}$$C1$${{< /mathjax >}} entre {{< mathjax >}}$$A$${{< /mathjax >}} y {{< mathjax >}}$$D$${{< /mathjax >}}.  
* El centro de la segunda esfera o el punto medio {{< mathjax >}}$$C2$${{< /mathjax >}} entre {{< mathjax >}}$$D$${{< /mathjax >}} y {{< mathjax >}}$$B$${{< /mathjax >}}.  
* El radio de la primera esfera {{< mathjax >}}$$(r1)$${{< /mathjax >}} o la distancia entre {{< mathjax >}}$$A$${{< /mathjax >}} y {{< mathjax >}}$$C1$${{< /mathjax >}}.  
* El radio de la segunda esfera {{< mathjax >}}$$(r2)$${{< /mathjax >}} o la distancia entre {{< mathjax >}}$$D$${{< /mathjax >}} y {{< mathjax >}}$$C2$${{< /mathjax >}}.  

**Solución:**

1\. Utilice el componente **Expression** para definir el punto {{< mathjax >}}$$D$${{< /mathjax >}} entre {{< mathjax >}}$$A$${{< /mathjax >}} y {{< mathjax >}}$$B$${{< /mathjax >}} como parámetro {{< mathjax >}}$$t$${{< /mathjax >}}. La expresión que usaremos se basa en la ecuación vectorial de una línea:  

{{< mathjax >}}$$D = A + t*(B-A)$${{< /mathjax >}}  

{{< mathjax >}}$$B-A$${{< /mathjax >}} : es el vector que va de {{< mathjax >}}$$B$${{< /mathjax >}} a {{< mathjax >}}$$A  (\vec{BA}) mediante la operación de resta de vectores.  

$${{< /mathjax >}}t*(B-A){{< mathjax >}}$$: donde $${{< /mathjax >}}t{{< mathjax >}}$$ está entre 0 y 1 para obtener una ubicación en el vector.  

$${{< /mathjax >}}A+t*(B-A){{< mathjax >}}$$ : obtiene un punto en el vector entre A y B.  

<img src="/images/math-image8.png">

2\. Utilice el componente Expression para definir también los puntos medios $${{< /mathjax >}}C1{{< mathjax >}}$$ y $${{< /mathjax >}}C2{{< mathjax >}}$$.  

<img src="/images/math-image9.png">  

3\. El radio de la primera esfera $${{< /mathjax >}}(r1){{< mathjax >}}$$ y el radio de la segunda esfera $${{< /mathjax >}}(r2){{< mathjax >}}$$ se pueden calcular utilizando el componente **Distance**.  

<img src="/images/math-image10.png">  

4\. El último paso consiste en crear la esfera a partir de un plano base y un radio. Debemos asegurarnos de que los orígenes estén conectados a $${{< /mathjax >}}C1{{< mathjax >}}$$ y $${{< /mathjax >}}C2{{< mathjax >}}$$ y al radio de $${{< /mathjax >}}r1{{< mathjax >}}$$ y $${{< /mathjax >}}r2$$.  

<img src="/images/math-image54.png">  

**Uso del componente VB de Grasshopper:**  

<img src="/images/math-image56.png">  

```vb
Private Sub RunScript(ByVal A As Point3d, ByVal B As Point3d, ByVal t As Double, ByRef S1 As Object, ByRef S2 As Object)

  'declare variables
  Dim D, C1, C2 As Rhino.Geometry.Point3d
  Dim r1, r2 As Double

  'find a point between A and B
  D = A + t * (B - A)

  'find mid point between A and D
  C1 = A + 0.5 * (D - A)

  'find mid point between D and B
  C2 = D + 0.5 * (B - D)
  'find spheres radius
  r1 = A.DistanceTo(C1)
  r2 = B.DistanceTo(C2)

  'create spheres and assign to output
  S1 = New Rhino.Geometry.Sphere(C1, r1)
  S2 = New Rhino.Geometry.Sphere(C2, r2)

End Sub
```

Uso del componente Python:

<img src="/images/math-image62.png">

```python
import Rhino

#find a point between A and B
D = A + t * (B - A)

#find mid point between A and D
C1 = A + 0.5 * (D - A)

#find mid point between D and B
C2 = D + 0.5 * (B - D)

#find spheres radius
r1 = A.DistanceTo(C1)
r2 = B.DistanceTo(C2)

#create spheres and assign to output
S1 = Rhino.Geometry.Sphere(C1, r1)
S2 = Rhino.Geometry.Sphere(C2, r2)
```

Uso del componente C# de Grasshopper:

<img src="/images/math-image58.png">

```cs
private void RunScript(Point3d A, Point3d B, double t, ref object S1, ref object S2)
{
  //declare variables
  Rhino.Geometry.Point3d D, C1, C2;
  double r1, r2;

  //find a point between A and B
  D = A + t * (B - A);

  //find mid point between A and D
  C1 = A + 0.5 * (D - A);

  //find mid point between D and B
  C2 = D + 0.5 * (B - D);

  //find spheres radius
  r1 = A.DistanceTo(C1);
  r2 = B.DistanceTo(C2);

  //create spheres and assign to output
  S1 = new Rhino.Geometry.Sphere(C1, r1);
  S2 = new Rhino.Geometry.Sphere(C2, r2);
}
```

## Descargar archivos de muestra

Descargue el archivo [{{< awesome "fas fa-download">}} ](/files/math-samplesandtutorials.zip.zip) [math-samplesandtutorials.zip](/files/math-samplesandtutorials.zip) , que contiene todos los archivos de ejemplo de Grasshopper y de código de esta guía.

## Próximos pasos

Ahora que ya conoce las matemáticas vectoriales, consulte la guía [Matrices y transformaciones](/guides/general/essential-mathematics/matrices-transformations/) para aprender más sobre mover, rotar y  escalar objetos....

+++
aliases = ["/en/5/guides/general/essential-mathematics/", "/en/6/guides/general/essential-mathematics/", "/en/7/guides/general/essential-mathematics/", "/en/wip/guides/general/essential-mathematics/"]
authors = [ "rajaa" ]
categories = [ "General" ]
description = "Presenta a los profesionales del diseño los conceptos matemáticos básicos para el desarrollo eficaz de modelos 3D computacionales."
keywords = [ "rhino", "developer" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "General" ]
title = "Matemáticas Esenciales para Diseño Computacional"
type = "guides"
weight = 1
override_last_modified = "2022-05-12T15:41:51Z"

[admin]
TODO = "This needs to be shimmed for Mac Platform."
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0
+++

<div class="row">
<div class="col-12" markdown="1">   


</div>
{{< column >}}  

{{< image url="/images/math-logo.svg" alt="/images/math-logo.svg" class="float_right" >}}

*Matemáticas Esenciales para Diseño Computacional* presenta a los profesionales del diseño los conceptos matemáticos básicos que son necesarios para el desarrollo de métodos computacionales para el modelado en 3D y el diseño gráfico por ordenador. Este documento no es una fuente completa y exhaustiva de información, sino más bien una introducción a los conceptos básicos más usados. El material está enfocado a diseñadores que tienen poca o ninguna experiencia en matemáticas más allá de la escuela secundaria. Todos los conceptos se explican visualmente usando [Grasshopper® (GH)](https://www.grasshopper3d.com), el entorno de modelado generativo para [Rhinoceros® (Rhino)](https://www.rhino3d.com).  

El contenido se divide en tres capítulos. En el [capítulo 1](/guides/general/essential-mathematics/vector-mathematics/) se tratan las matemáticas vectoriales, incluida la representación de vectores, las operaciones vectoriales y las ecuaciones de líneas y planos. En el [capítulo 2](/guides/general/essential-mathematics/matrices-transformations/) se estudian las operaciones y transformaciones matriciales. En el [capítulo 3](/guides/general/essential-mathematics/parametric-curves-surfaces/) se realiza una revisión en profundidad de las curvas paramétricas, con especial énfasis en las curvas NURBS y los conceptos de continuidad y curvatura.  También se hace un repaso general de las superficies y polisuperficies NURBS.

*Me gustaría agradecer la excelente y completa revisión técnica del [Dr. Dale Lear](https://discourse.mcneel.com/u/dalelear/activity) de Robert McNeel & Associates. Sus valiosos comentarios fueron fundamentales para producir esta edición. También quiero agradecer a la Sra. [Margaret Becker](https://discourse.mcneel.com/u/margaret/activity), de Robert McNeel & Associates, por revisar la redacción técnica y el formato del documento.*

{{< /column >}}  
</div>  

<div class="row">  
<div class="col-md-12" markdown="1">  

***[Rajaa Issa](https://discourse.mcneel.com/u/rajaa/activity)***

Robert McNeel & Associates

#### Descargas:
* [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6/essentialmathematics) [Descargue el PDF de la guía y todos los ejemplos de Grasshopper (4ª edición)](https://www.rhino3d.com/download/rhino/6/essentialmathematics/) en inglés, francés, alemán, español, italiano o chino simplificado.
* <a href="https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK"><span class="glyphicon glyphicon-play"></span></a> [Vea los vídeos de Matemáticas Esenciales... ](https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK)

### Contenido  

</div>  
</div>  

{{< row >}}  
{{< column >}}  

### 1. [Matemáticas vectoriales](/guides/general/essential-mathematics/vector-mathematics/)

   1.1 [Representación vectorial](/guides/general/essential-mathematics/vector-mathematics/#11-vector-representation)  
&nbsp;&nbsp; Vector de posición   
&nbsp;&nbsp; Vectores y puntos   
&nbsp;&nbsp; Longitud del vector   
&nbsp;&nbsp; Vector unitario    

   1.2 [Operaciones vectoriales](/guides/general/essential-mathematics/vector-mathematics/#12-vector-operations)  
&nbsp;&nbsp; Operación escalar de vectores   
&nbsp;&nbsp; Suma de vectores    
&nbsp;&nbsp; Resta de vectores   
&nbsp;&nbsp; Propiedades de los vectores  
&nbsp;&nbsp; Producto escalar de vectores   
&nbsp;&nbsp; Producto escalar de vectores, longitudes y ángulos    
&nbsp;&nbsp; Propiedades del producto escalar    
&nbsp;&nbsp; Producto vectorial   
&nbsp;&nbsp; Producto vectorial y ángulo entre vectores    
&nbsp;&nbsp; Propiedades del producto vectorial   

   1.3 [Ecuación vectorial de una línea](/guides/general/essential-mathematics/vector-mathematics/#13-vector-equation-of-line)  

   1.4 [Ecuación vectorial de un plano](/guides/general/essential-mathematics/vector-mathematics/#14-vector-equation-of-a-plane)  

   1.5 [Tutoriales](/guides/general/essential-mathematics/vector-mathematics/#15-tutorials)   
&nbsp;&nbsp; Dirección de cara  
&nbsp;&nbsp; Caja descompuesta  
&nbsp;&nbsp; Esferas tangentes  

{{< /column >}}
{{< column >}} 

### 2. [Matrices y transformaciones](/guides/general/essential-mathematics/matrices-transformations/)
   2.1 [Operaciones con matrices](/guides/general/essential-mathematics/matrices-transformations/#21-matrix-operations)  
Multiplicación de matrices  
Matriz de identidad  

   2.2 [Operaciones de transformación](/guides/general/essential-mathematics/matrices-transformations/#22-transformation-operations)  
&nbsp;&nbsp; Transformación de traslación (mover)   
&nbsp;&nbsp; Transformación de rotación  
&nbsp;&nbsp; Transformación de escala  
&nbsp;&nbsp; Transformación de inclinación  
&nbsp;&nbsp; Transformación de espejo o reflejo  
&nbsp;&nbsp; Transformación de proyección plana  

{{< /column >}}
{{< column >}} 


### 3. [Curvas y superficies paramétricas](/guides/general/essential-mathematics/parametric-curves-surfaces/)

   3.1 [Curva paramétrica](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
&nbsp;&nbsp; Parámetro de curva  
&nbsp;&nbsp; Dominio o intervalo de curva  
&nbsp;&nbsp; Evaluación de curvas  
&nbsp;&nbsp; Vector tangente a una curva  
&nbsp;&nbsp; Curvas polinómicas cúbicas  
&nbsp;&nbsp; Evaluación de curvas cúbicas de Bézier  

   3.2 [Curvas NURBS](/guides/general/essential-mathematics/parametric-curves-surfaces/#32-nurbs-curves)  
&nbsp;&nbsp; Grado  
&nbsp;&nbsp; Puntos de control  
&nbsp;&nbsp; Pesos de puntos de control  
&nbsp;&nbsp; Nodos  
&nbsp;&nbsp; Los nodos son valores de parámetros  
&nbsp;&nbsp; Regla de evaluación  
&nbsp;&nbsp; Características de las curvas NURBS  
&nbsp;&nbsp; Evaluación de curvas NURBS  

   3.3 [Continuidad geométrica de curva](/guides/general/essential-mathematics/parametric-curves-surfaces/#33-curve-geometric-continuity)   

   3.4 [Curvatura de curva](/guides/general/essential-mathematics/parametric-curves-surfaces/#34-curve-curvature)   

   3.5 [Superficies paramétricas](/guides/general/essential-mathematics/parametric-curves-surfaces/#35-parametric-surfaces)   
&nbsp;&nbsp; Parámetros de superficie  
&nbsp;&nbsp; Dominio de superficie  
&nbsp;&nbsp; Evaluación de superficies  
&nbsp;&nbsp; Plano tangente a una superficie  

   3.6 [Continuidad geométrica de superficie](/guides/general/essential-mathematics/parametric-curves-surfaces/#36-surface-geometric-continuity)     

   3.7 [Curvatura de superficie](/guides/general/essential-mathematics/parametric-curves-surfaces/#37-surface-curvature)     
&nbsp;&nbsp; Curvaturas principales  
&nbsp;&nbsp; Curvatura gaussiana  
&nbsp;&nbsp; Curvatura media  

   3.8 [Superficies NURBS](/guides/general/essential-mathematics/parametric-curves-surfaces/#38-nurbs-surfaces)     
&nbsp;&nbsp; Características de las superficies NURBS  
&nbsp;&nbsp; Singularidad en superficies NURBS  
&nbsp;&nbsp; Superficies NURBS recortadas  

   3.9 [Polisuperficies](/guides/general/essential-mathematics/parametric-curves-surfaces/#39-polysurfaces)     

   3.10 [Tutoriales](/guides/general/essential-mathematics/parametric-curves-surfaces/#310-tutorials)     
&nbsp;&nbsp; Continuidad entre curvas  
&nbsp;&nbsp; Superficies con singularidad  

{{< /column >}}
{{< /row >}}

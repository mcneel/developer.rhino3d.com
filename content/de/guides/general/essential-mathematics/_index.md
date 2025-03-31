+++
aliases = ["/en/5/guides/general/essential-mathematics/", "/en/6/guides/general/essential-mathematics/", "/en/7/guides/general/essential-mathematics/", "/en/wip/guides/general/essential-mathematics/"]
authors = [ "rajaa" ]
categories = [ "General" ]
description = "Führt Designfachleute in die grundlegenden mathematischen Konzepte für die effektive Entwicklung von rechnergestützten 3D-Modellen ein."
keywords = [ "rhino", "developer" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "General" ]
title = "Essential Mathematics for Computational Design"
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

*Essential Mathematics for Computational Design* präsentiert Designfachleuten die grundlegenden mathematischen Konzepte, die für eine erfolgreiche Entwicklung computergestützter Methoden zur 3D-Modellierung und für Computergrafiken notwendig sind. Dies ist nicht als komplette und umfassende Ressource gedacht, sondern eher als Übersicht der grundlegenden und meistverwendeten Konzepte. Das Material richtet sich an Designer mit wenig oder gar keiner mathematischen Erfahrung seit dem Schulabgang. Alle Konzepte werden visuell unter Verwendung von [Grasshopper® (GH)](https://www.grasshopper3d.com) erklärt, der generativen Modellierungsumgebung für [Rhinoceros® (Rhino)](https://www.rhino3d.com).  

Der Inhalt ist in drei Kapitel gegliedert. In [Kapitel 1](/guides/general/essential-mathematics/vector-mathematics/) geht es um Vektor-Mathematik einschließlich Vektordarstellung, Vektoroperation und Linien- und Ebenengleichungen. In [Kapitel 2](/guides/general/essential-mathematics/matrices-transformations/) werden Matrix-Operationen und -Transformationen erklärt. [Kapitel 3](/guides/general/essential-mathematics/parametric-curves-surfaces/) widmet sich eingehend den parametrischen Kurven mit besonderem Schwerpunkt auf NURBS-Kurven sowie den Konzepten Stetigkeit und Krümmung.  NURBS-Flächen und -Flächenverbände kommen ebenso zur Sprache.

*Mein Dank geht an [Dr. Dale Lear](https://discourse.mcneel.com/u/dalelear/activity) von Robert McNeel & Associates für seine sorgfältige und fachmännische technische Nachprüfung. Seine Anmerkungen waren für die vorliegende Ausgabe von unschätzbarem Wert. Ich möchte auch Frau [Margaret Becker](https://discourse.mcneel.com/u/margaret/activity) von Robert McNeel & Associates für die Überprüfung der Technischen Redaktion und der Formatierung*.

{{< /column >}}  
</div>  

<div class="row">  
<div class="col-md-12" markdown="1">  

***[Rajaa Issa](https://discourse.mcneel.com/u/rajaa/activity)***

Robert McNeel & Associates

#### Downloads:
* [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6/essentialmathematics) [Laden Sie das PDF-Handbuch und alle Grasshopper-Beispiele (4. Auflage)](https://www.rhino3d.com/download/rhino/6/essentialmathematics/) auf Englisch, Französisch, Deutsch, Spanisch, Italienisch oder vereinfachtes Chinesisch herunter.
* <a href="https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK"><span class="glyphicon glyphicon-play"></span></a> [Sehen Sie sich die Videos zu Essential Mathematics an... ](https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK)

### Inhaltsverzeichnis  

</div>  
</div>  

{{< row >}}  
{{< column >}}  

### 1. [Vektor-Mathematik](/guides/general/essential-mathematics/vector-mathematics/)

   1.1 [Vektor-Darstellung](/guides/general/essential-mathematics/vector-mathematics/#11-vector-representation)  
&nbsp;&nbsp; Positionsvektor   
&nbsp;&nbsp; Vektoren im Vergleich zu Punkten   
&nbsp;&nbsp; Vektorlänge   
&nbsp;&nbsp; Einheitsvektor    

   1.2 [Vektoroperationen](/guides/general/essential-mathematics/vector-mathematics/#12-vector-operations)  
&nbsp;&nbsp; Skalare Vektoroperation   
&nbsp;&nbsp; Vektoraddition    
&nbsp;&nbsp; Vektorsubtraktion   
&nbsp;&nbsp; Vektoreigenschaften  
&nbsp;&nbsp; Vektorpunktprodukt   
&nbsp;&nbsp; Vektorpunktprodukt, Längen und Winkel    
&nbsp;&nbsp; Eigenschaften des Punktprodukts    
&nbsp;&nbsp; Vektor-Kreuzprodukt   
&nbsp;&nbsp; Kreuzprodukte und Winkel zwischen Vektoren    
&nbsp;&nbsp; Eigenschaften des Kreuzprodukts   

   1.3 [Lineare Vektorgleichungen](/guides/general/essential-mathematics/vector-mathematics/#13-vector-equation-of-line)  

   1.4 [Vektorgleichung einer Ebene](/guides/general/essential-mathematics/vector-mathematics/#14-vector-equation-of-a-plane)  

   1.5 [Tutorials](/guides/general/essential-mathematics/vector-mathematics/#15-tutorials)   
&nbsp;&nbsp; Seitenrichtung  
&nbsp;&nbsp; Zerlegter Quader  
&nbsp;&nbsp; Tangentiale Kugeln  

{{< /column >}}
{{< column >}} 

### 2. [Matrices und Transformationen](/guides/general/essential-mathematics/matrices-transformations/)
   2.1 [Matrixoperationen](/guides/general/essential-mathematics/matrices-transformations/#21-matrix-operations)  
&nbsp;&nbsp; Matrixmultiplikation  
&nbsp;&nbsp; Einheitsmatrix  

   2.2 [Transformationsvorgänge](/guides/general/essential-mathematics/matrices-transformations/#22-transformation-operations)  
&nbsp;&nbsp; Transformation durch Transponieren (Verschieben)   
&nbsp;&nbsp; Drehtransformation  
&nbsp;&nbsp; Skalierungs-Transformation  
&nbsp;&nbsp; Scherungs-Transformation  
&nbsp;&nbsp; Spiegel- oder Reflektionstransformation  
&nbsp;&nbsp; Planare Projektionstransformation  

{{< /column >}}
{{< column >}} 


### 3. [Parametrische Kurven und Flächen](/guides/general/essential-mathematics/parametric-curves-surfaces/)

   3.1 [Parametrische Kurve](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
&nbsp;&nbsp; Kurvenparameter  
&nbsp;&nbsp; Kurvendomäne oder Intervall  
&nbsp;&nbsp; Kurvenauswertung  
&nbsp;&nbsp; Tangentialvektor zu einer Kurve  
&nbsp;&nbsp; Kubische Polynomkurven  
&nbsp;&nbsp; Auswertung kubischer Bézier-Kurven  

   3.2 [NURBS-Kurven](/guides/general/essential-mathematics/parametric-curves-surfaces/#32-nurbs-curves)  
&nbsp;&nbsp; Grad  
&nbsp;&nbsp; Kontrollpunkte  
&nbsp;&nbsp; Wichtungen von Kontrollpunkten  
&nbsp;&nbsp; Knoten  
&nbsp;&nbsp; Knoten als Parameterwerte  
&nbsp;&nbsp; Auswertungsregel  
&nbsp;&nbsp; Eigenschaften von NURBS-Kurven  
&nbsp;&nbsp; Auswertung von NURBS-Kurven  

   3.3 [Geometrische Kurvenstetigkeit](/guides/general/essential-mathematics/parametric-curves-surfaces/#33-curve-geometric-continuity)   

   3.4 [Kurvenkrümmung](/guides/general/essential-mathematics/parametric-curves-surfaces/#34-curve-curvature)   

   3.5 [Parametrische Flächen](/guides/general/essential-mathematics/parametric-curves-surfaces/#35-parametric-surfaces)   
&nbsp;&nbsp; Flächenparameter  
&nbsp;&nbsp; Flächendomäne   
&nbsp;&nbsp; Flächenauswertung  
&nbsp;&nbsp; Tangentiale Ebene einer Fläche  

   3.6 [Geometrische Flächenstetigkeit](/guides/general/essential-mathematics/parametric-curves-surfaces/#36-surface-geometric-continuity)     

   3.7 [Flächenkrümmung](/guides/general/essential-mathematics/parametric-curves-surfaces/#37-surface-curvature)     
&nbsp;&nbsp; Hauptkrümmungen  
&nbsp;&nbsp; Gaußsche Krümmung  
&nbsp;&nbsp; Mittlere Krümmung  

   3.8 [NURBS-Flächen](/guides/general/essential-mathematics/parametric-curves-surfaces/#38-nurbs-surfaces)     
&nbsp;&nbsp; Eigenschaften von NURBS-Flächen  
&nbsp;&nbsp; Singularität in NURBS-Flächen  
&nbsp;&nbsp; Getrimmte NURBS-Flächen  

   3.9 [Flächenverbände](/guides/general/essential-mathematics/parametric-curves-surfaces/#39-polysurfaces)     

   3.10 [Tutorials](/guides/general/essential-mathematics/parametric-curves-surfaces/#310-tutorials)     
&nbsp;&nbsp; Stetigkeit zwischen Kurven  
&nbsp;&nbsp; Flächen mit Singularität  

{{< /column >}}
{{< /row >}}

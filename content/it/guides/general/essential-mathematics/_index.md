+++
aliases = ["/en/5/guides/general/essential-mathematics/", "/en/6/guides/general/essential-mathematics/", "/en/7/guides/general/essential-mathematics/", "/en/wip/guides/general/essential-mathematics/"]
authors = [ "rajaa" ]
categories = [ "General" ]
description = "Introduce ai professionisti della progettazione i concetti matematici di base per lo sviluppo efficace di modelli 3D digitali."
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

*Essential Mathematics for Computational Design* introduce i concetti matematici di base necessari per lo sviluppo efficace di metodi digitali per la modellazione 3D e la grafica computer. Ciò non vuol dire che si tratta di una risorsa completa ed esauriente, ma piuttosto di una panoramica dei concetti di base usati più di frequente. Il materiale è rivolto a progettisti con poche conoscenze sui concetti matematici, al di là di quelli appresi alle scuole superiori. Tutti i concetti vengono spiegati con supporto visivo usando [Grasshopper® (GH)](https://www.grasshopper3d.com), l'ambiente di modellazione generativa per [Rhinoceros® (Rhino)](https://www.rhino3d.com).  

Il presente testo è diviso in tre capitoli. Il [capitolo 1](/guides/general/essential-mathematics/vector-mathematics/) riguarda la matematica dei vettori, tra cui rappresentazioni e operazioni vettoriali, equazioni di primo grado ed equazioni di piani. Il [capitolo 2](/guides/general/essential-mathematics/matrices-transformations/) analizza le operazioni con matrici e trasformazioni. Il [capitolo 3](/guides/general/essential-mathematics/parametric-curves-surfaces/) include un approfondimento sulle curve parametriche, con particolare attenzione alle curve NURBS e ai concetti di continuità e curvatura.  Questo capitolo tratta anche le superfici e polisuperfici NURBS.

*Un riconoscimento particolare merita l'eccellente analisi di [Dale Lear](https://discourse.mcneel.com/u/dalelear/activity) di Robert McNeel & Associates. I suoi preziosi commenti sono stati determinanti per la realizzazione di questa edizione. Un altro riconoscimento speciale va a [Margaret Becker](https://discourse.mcneel.com/u/margaret/activity) di Robert McNeel & Associates per la stesura della documentazione tecnica.*

{{< /column >}}  
</div>  

<div class="row">  
<div class="col-md-12" markdown="1">  

***[Rajaa Issa](https://discourse.mcneel.com/u/rajaa/activity)***

Robert McNeel & Associates

#### Download:
* [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6/essentialmathematics) [Scarica il PDF della guida e tutti gli esempi di Grasshopper (4a edizione)](https://www.rhino3d.com/download/rhino/6/essentialmathematics/) in inglese, francese, tedesco, spagnolo, italiano o cinese semplificato.
* <a href="https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK"><span class="glyphicon glyphicon-play"></span></a> [Guarda i video di Essential Mathematics... ](https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK)

### Sommario  

</div>  
</div>  

{{< row >}}  
{{< column >}}  

### 1. [Matematica vettoriale](/guides/general/essential-mathematics/vector-mathematics/)

   1.1 [Rappresentazione vettoriale](/guides/general/essential-mathematics/vector-mathematics/#11-vector-representation)  
&nbsp;&nbsp; Vettore di posizione   
&nbsp;&nbsp; Vettori e punti   
&nbsp;&nbsp; Lunghezza del vettore   
&nbsp;&nbsp; Unità vettoriale    

   1.2 [Operazioni vettoriali](/guides/general/essential-mathematics/vector-mathematics/#12-vector-operations)  
&nbsp;&nbsp; Operazioni scalari vettoriali   
&nbsp;&nbsp; Addizione vettoriale    
&nbsp;&nbsp; Sottrazione vettoriale   
&nbsp;&nbsp; Proprietà del vettore  
&nbsp;&nbsp; Prodotto vettoriale del punto   
&nbsp;&nbsp; Prodotto scalare del vettore, lunghezze e angoli    
&nbsp;&nbsp; Proprietà del prodotto di punto    
&nbsp;&nbsp; Prodotto incrociato vettoriale   
&nbsp;&nbsp; Prodotto vettoriale e angolo fra vettori    
&nbsp;&nbsp; Proprietà trasversali del prodotto   

   1.3 [Equazione vettoriale di una retta](/guides/general/essential-mathematics/vector-mathematics/#13-vector-equation-of-line)  

   1.4 [Equazione vettoriale di un piano](/guides/general/essential-mathematics/vector-mathematics/#14-vector-equation-of-a-plane)  

   1.5 [Tutorial](/guides/general/essential-mathematics/vector-mathematics/#15-tutorials)   
&nbsp;&nbsp; Direzione delle facce  
&nbsp;&nbsp; Parallelepipedo esploso  
&nbsp;&nbsp; Sfere tangenti  

{{< /column >}}
{{< column >}} 

### 2. [Matrici e trasformazioni](/guides/general/essential-mathematics/matrices-transformations/)
   2.1 [Operazioni con le matrici](/guides/general/essential-mathematics/matrices-transformations/#21-matrix-operations)  
&nbsp;&nbsp; Moltiplicazione con le matrici  
&nbsp;&nbsp; Matrice di identità  

   2.2 [Operazioni di trasformazione](/guides/general/essential-mathematics/matrices-transformations/#22-transformation-operations)  
&nbsp;&nbsp; Trasformazione (spostamento) traduzione   
&nbsp;&nbsp; Trasformazione rotazione  
&nbsp;&nbsp; Trasformazione della scala  
&nbsp;&nbsp; Trasformazione al taglio  
&nbsp;&nbsp; Trasformazione speculare o riflessione  
&nbsp;&nbsp; Trasformazione proiezione planare  

{{< /column >}}
{{< column >}} 


### 3. [Curve e superfici parametriche](/guides/general/essential-mathematics/parametric-curves-surfaces/)

   3.1 [Curve parametriche](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
&nbsp;&nbsp; Parametro della curva  
&nbsp;&nbsp; Dominio o intervallo della curva  
&nbsp;&nbsp; Valutazione della curva  
&nbsp;&nbsp; Vettore tangente su una curva  
&nbsp;&nbsp; Curve polinomiali cubiche  
&nbsp;&nbsp; Valutazione delle curve cubiche di Bézier  

   3.2 [Curve NURBS](/guides/general/essential-mathematics/parametric-curves-surfaces/#32-nurbs-curves)  
&nbsp;&nbsp; Grado  
&nbsp;&nbsp; Punti di controllo  
&nbsp;&nbsp; Pesi dei punti di controllo  
&nbsp;&nbsp; Nodi  
&nbsp;&nbsp; I nodi sono valori parametrici  
&nbsp;&nbsp; Regola di valutazione  
&nbsp;&nbsp; Caratteristiche delle curve NURBS  
&nbsp;&nbsp; Valutazione delle curve NURBS  

   3.3 [Continuità geometrica delle curve](/guides/general/essential-mathematics/parametric-curves-surfaces/#33-curve-geometric-continuity)   

   3.4 [Curvatura](/guides/general/essential-mathematics/parametric-curves-surfaces/#34-curve-curvature)   

   3.5 [Superfici parametriche](/guides/general/essential-mathematics/parametric-curves-surfaces/#35-parametric-surfaces)   
&nbsp;&nbsp; Parametri di superficie  
&nbsp;&nbsp; Dominio della superficie  
&nbsp;&nbsp; Valutazione delle superfici  
&nbsp;&nbsp; Piano tangente di una superficie  

   3.6 [Continuità geometrica delle superfici](/guides/general/essential-mathematics/parametric-curves-surfaces/#36-surface-geometric-continuity)     

   3.7 [Curvatura di una superficie](/guides/general/essential-mathematics/parametric-curves-surfaces/#37-surface-curvature)     
&nbsp;&nbsp; Curvature principali  
&nbsp;&nbsp; Curvatura gaussiana  
&nbsp;&nbsp; Curvatura media  

   3.8 [Superfici NURBS](/guides/general/essential-mathematics/parametric-curves-surfaces/#38-nurbs-surfaces)     
&nbsp;&nbsp; Caratteristiche delle superfici NURBS  
&nbsp;&nbsp; Singolarità nelle superfici NURBS  
&nbsp;&nbsp; Superfici NURBS ritagliate  

   3.9 [Polisuperfici](/guides/general/essential-mathematics/parametric-curves-surfaces/#39-polysurfaces)     

   3.10 [Tutorial](/guides/general/essential-mathematics/parametric-curves-surfaces/#310-tutorials)     
&nbsp;&nbsp; Continuità tra le curve  
&nbsp;&nbsp; Superfici con singolarità  

{{< /column >}}
{{< /row >}}

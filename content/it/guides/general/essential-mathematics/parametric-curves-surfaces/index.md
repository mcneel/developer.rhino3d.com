+++
aliases = ["/en/5/guides/general/essential-mathematics/parametric-curves-surfaces/", "/en/6/guides/general/essential-mathematics/parametric-curves-surfaces/", "/en/7/guides/general/essential-mathematics/parametric-curves-surfaces/", "/en/wip/guides/general/essential-mathematics/parametric-curves-surfaces/"]
authors = [ "rajaa" ]
categories = [ "Essential Mathematics" ]
category_page = "guides/general/essential-mathematics/"
description = "Il capitolo 3 include un approfondimento sulle curve parametriche, con particolare attenzione alle curve NURBS e ai concetti di continuità e curvatura."
keywords = [ "mathematics", "geometry", "grasshopper3d" ]
languages = "unset"
sdk = [ "General" ]
title = "3 Curve e superfici parametriche"
type = "guides"
weight = 1
override_last_modified = "2019-08-14T13:31:55Z"

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

Supponiamo che ti sposti ogni giorno da casa al lavoro. Esci di casa alle ore 8:00 e arrivi al lavoro alle ore 9:00. Nell'intervallo dalle 8:00 alle 9:00, ti trovi in un punto del percorso. Se tracci la tua posizione ogni minuto durante il tragitto, puoi definire il percorso da casa al lavoro collegando i 60 punti tracciati. Presupponendo che ogni giorno ti sposti esattamente alla stessa velocità, alle 8:00 sei a casa (posizione iniziale), alle 9:00 arrivi al lavoro (posizione finale) e alle 8:40 ti trovi nella stessa posizione del percorso che corrisponde al quarantesimo punto tracciato. A questo punto, hai definito la tua prima curva parametrica. Hai usato il *tempo* come *parametro* per definire il percorso, quindi puoi definire la tua curva di percorso *curva parametrica*. L'intervallo di tempo impiegato dall'inizio alla fine (dalle 8:00 alle 9:00) viene chiamato *dominio* o *intervallo* della curva.

{{< image url="/images/math-image106.png" alt="/images/math-image106.png" class="float_right" width="275" >}}   

In generale, possiamo descrivere le posizioni  {{< mathjax >}}$$x$${{< /mathjax >}}, {{< mathjax >}}$$y$${{< /mathjax >}} e {{< mathjax >}}$$z$${{< /mathjax >}} di una curva parametrica in termini di parametro {{< mathjax >}}$$t$${{< /mathjax >}} come segue:  
&nbsp; {{< mathjax >}}$$x = x(t)$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$y = y(t)$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$z = z(t)$${{< /mathjax >}}  
Dove:  
&nbsp; {{< mathjax >}}$$t$${{< /mathjax >}} è un intervallo di numeri reali.  

{{< div class="clear_both" />}}  

Osserviamo che l'equazione parametrica di una retta in termini del parametro {{< mathjax >}}$$t$${{< /mathjax >}} è definita come segue:

&nbsp; {{< mathjax >}}$$x = x’ + t * a$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$y = y’ + t * b$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$z = z’ + t * c$${{< /mathjax >}}  

Dove:

&nbsp; {{< mathjax >}}$$x$${{< /mathjax >}}, {{< mathjax >}}$$y$${{< /mathjax >}} e {{< mathjax >}}$$z$${{< /mathjax >}} sono funzioni di t dove t rappresenta un intervallo di numeri reali.
&nbsp; {{< mathjax >}}$$x’$${{< /mathjax >}}, {{< mathjax >}}$$y’$${{< /mathjax >}} e {{< mathjax >}}$$z’$${{< /mathjax >}} sono le coordinate di un punto sul segmento di retta.
&nbsp; {{< mathjax >}}$$a$${{< /mathjax >}}, {{< mathjax >}}$$b$${{< /mathjax >}} e {{< mathjax >}}$$c$${{< /mathjax >}} definiscono la pendenza della retta, in modo tale che il vettore {{< mathjax >}}$$\mathbf{\vec v} <a, b, c>$${{< /mathjax >}} sia parallelo alla retta.

{{< image url="/images/math-image108.png" alt="/images/math-image108.png" class="float_right" width="275" >}}   

Possiamo quindi scrivere l'equazione parametrica del segmento di una retta usando un parametro {{< mathjax >}}$$t$${{< /mathjax >}} compreso fra due valori numerici reali {{< mathjax >}}$$t0$${{< /mathjax >}}, {{< mathjax >}}$$t1$${{< /mathjax >}} e un vettore di unità {{< mathjax >}}$$\mathbf{\vec v}$${{< /mathjax >}} nella direzione della retta, come segue:

{{< mathjax >}}$$P = P’ + t * \mathbf{\vec v}​$${{< /mathjax >}}

{{< div class="clear_both" />}}

Un altro esempio è un cerchio. L'equazione parametrica del cerchio sul piano xy, con un centro all'origine (0,0) e un parametro angolare {{< mathjax >}}$$t$${{< /mathjax >}} compreso fra {{< mathjax >}}$$0$${{< /mathjax >}} e {{< mathjax >}}$$2π$${{< /mathjax >}} il radiante è:  

{{< image url="/images/math-image110.png" alt="/images/math-image110.png" class="float_right" width="241" >}}  

&nbsp; {{< mathjax >}}$$x = r \dot cos(t)$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$y = r \dot sin(t)$${{< /mathjax >}}  

Possiamo derivare l'equazione generale di un cerchio per uno parametrico come segue:  

&nbsp; {{< mathjax >}}$$ x/r = cos(t)$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$y/r = sin(t)$${{< /mathjax >}}  

E poiché:  

&nbsp; {{< mathjax >}}$$cos(t)^2 + sin(t)^2 = 1$${{< /mathjax >}} (identità pitagorica)  

Allora:  

&nbsp; {{< mathjax >}}$$(x/r)^2 + (y/r)^2 = 1$${{< /mathjax >}} o   
&nbsp; {{< mathjax >}}$$x^2 + y^2 = r^2$${{< /mathjax >}}  


## 3.1 Curve parametriche

### Parametro di una curva

Un parametro su una curva rappresenta la direzione di un punto su tale curva. Come menzionato in precedenza, possiamo considerare una curva parametrica come un percorso fra due punti in un determinato intervallo di tempo, a velocità fissa o variabile. Se il tragitto impiega un determinato tempo {{< mathjax >}}$$T$${{< /mathjax >}}, allora il parametro rappresenta un tempo in {{< mathjax >}}$$T$${{< /mathjax >}} che si traduce in una posizione (punto) sulla curva.  

Se si ha un percorso rettilineo (segmento di linea) tra i due punti {{< mathjax >}}$$A$${{< /mathjax >}} e {{< mathjax >}}$$B$${{< /mathjax >}} e {{< mathjax >}}$$\mathbf{\vec v}$${{< /mathjax >}} fosse un vettore da {{< mathjax >}}$$A$${{< /mathjax >}} a {{< mathjax >}}$$B$${{< /mathjax >}} ({{< mathjax >}}$$\mathbf{\vec v} = B - A$${{< /mathjax >}}), è possibile utilizzare l'equazione parametrica della retta per trovare tutti i punti {{< mathjax >}}$$M$${{< /mathjax >}} fra {{< mathjax >}}$$A$${{< /mathjax >}} e {{< mathjax >}}$$B$${{< /mathjax >}} come segue:  

&nbsp; {{< mathjax >}}$$M = A + t*(B-A)$${{< /mathjax >}}  

Dove:  

&nbsp; {{< mathjax >}}$$t$${{< /mathjax >}} è un valore compreso fra 0 e 1.

L'intervallo dei valori di t, da 0 a 1 in questo caso, si riferisce al dominio della curva o all'intervallo. Se t è un valore fuori dal dominio (inferiore a 0 o superiore a 1), allora il punto  {{< mathjax >}}$$M$${{< /mathjax >}} che ne risulta si troverà fuori dalla curva lineare {{< mathjax >}}$$\overline{AB}$${{< /mathjax >}}.


<figure>
   <img src="/images/math-image112.png">
   <figcaption>Figura (25): Curva lineare parametrica nello spazio 3-D e intervallo di parametri.</figcaption>
</figure>  

Lo stesso principio si applica a qualsiasi curva parametrica. Qualsiasi punto sulla curva può essere calcolato usando il parametro t nell'intervallo o nel dominio di valori che definiscono i limiti della curva. Il parametro iniziale del dominio viene solitamente definito come {{< mathjax >}}$$t0$${{< /mathjax >}} e la fine del dominio come {{< mathjax >}}$$t1$${{< /mathjax >}}.  

<figure>
   <img src="/images/math-image94.png" width="500px">
   <figcaption>Figura (26): Curva nello spazio 3D (1). Dominio della curva (2).</figcaption>
</figure>  

### Dominio o intervallo della curva

Un *dominio* o *intervallo* della curva è definito come un intervallo di parametri considerati in un punto nella curva. Il dominio viene descritto di solito con due numeri reali, definendo i limiti del dominio espressi nella forma (da min a max) o (min, max). I limiti del dominio possono corrispondere a uno qualsiasi dei due valori correlati o non correlati alla lunghezza reale della curva. In un dominio crescente, il parametro min viene considerato il punto iniziale della curva mentre il parametro max il punto finale della curva.  

<figure>
   <img src="/images/math-image95.png" width="540px">
   <figcaption>Figura (27): Il dominio o l'intervallo della curva può essere compreso tra due numeri qualsiasi.</figcaption>
</figure>  

La modifica del dominio di una curva si riferisce al processo di riparametrizzazione della curva. Ad esempio, è molto comune modificare il dominio in modo che sia (da 0 a 1). La riparametrizzazione di una curva non ha effetto sulla forma della curva 3D. È come modificare il tempo di percorrenza correndo anziché camminare; anche qui la forma del percorso non cambia.  

<figure>
   <img src="/images/math-image96.png" width="500px">
   <figcaption>Figura (28): Dominio della curva normalizzato da 0 a 1.</figcaption>
</figure>  

Un dominio crescente implica che il valore minimo del dominio punta verso l'inizio della curva. Di solito i domini sono crescenti, ma non sempre.  

### Valutazione delle curve

Abbiamo imparato che l'intervallo di una curva corrisponde all'intervallo di tutti i parametri che vengono considerati punti in una curva 3D. Tuttavia, non è possibile garantire che la valutazione al centro del dominio, ad esempio, creerà un punto che si trova al centro della curva, come mostrato nella figura (29).  

Possiamo pensare alla parametrizzazione uniforme di una curva come percorso a velocità costante. Una retta di grado 1 fra due punti è un esempio in cui gli intervalli di parametri uguali si traducono in intervalli uguali della lunghezza di un arco sulla retta. Nelle curve parametriche, è raro che gli intervalli di parametri vengano considerati intervalli uguali sulla curva 3D.  

<figure>
   <img src="/images/math-image79.png" width="500px">
   <figcaption>Figura (29): Intervalli di parametri uguali in una retta di grado 1 si valutano come lunghezze di curva uguali.</figcaption>
</figure>  

È probabile che la velocità diminuisce o aumenta lungo il percorso. Ad esempio, se per percorrere una strada impieghi 30 minuti, è improbabile che dopo 15 minuti ti trovi esattamente a metà strada. La figura (30) mostra un caso tipico in cui gli intervalli di parametri uguali vengono considerati come lunghezza variabile sulla curva 3D.  

<figure>
   <img src="/images/math-image81.png" width="500px">
   <figcaption>Figura (30): Gli intervalli di parametri uguali non sempre vengono tradotti in distanze uguali su una curva.</figcaption>
</figure>  

Potresti dover considerare i punti su una curva 3D impostata su una percentuale definita della lunghezza della curva. Ad esempio, potresti dover dividere la curva in lunghezze uguali. Di solito, i modellatori 3D forniscono strumenti per valutare le curve relative alla lunghezza dell'arco.

### Vettore tangente a una curva

Una tangente a una curva in qualsiasi parametro (o un punto su una curva) è un vettore che tocca la curva su quel punto, ma non cambia. L'inclinazione del vettore tangente è uguale all'inclinazione della curva sullo stesso punto. Il seguente esempio valuta la tangente a una curva in due parametri diversi.

<figure>
   <img src="/images/math-image83.png" width="500px">
   <figcaption>Figura (31): Tangenti a una curva.</figcaption>
</figure>  

### Curve polinomiali cubiche

Le curve Hermite e Bézier sono due esempi di curve polinomiali cubiche determinate da quattro parametri. Un curva di Hermite è determinata da due punti di fine e due vettori tangenti a tali punti, mentre una curva di Bézier è definita da quattro punti. Sebbene i due tipi di curve siano diversi dal punto di vista matematico, condividono caratteristiche e limiti simili.  

<figure>
   <img src="/images/math-image85.png" width="500px">
   <figcaption>Figura (32): Curve polinomiali cubiche. La curva di Bézier (a sinistra) è definita da quattro punti. La curva di Hermite (a destra) è definita da due punti e due tangenti.</figcaption>
</figure>  

Nella maggior parte dei casi, le curve sono rappresentate da vari segmenti. Ciò richiede la creazione della cosiddetta curva cubica *con funzione definita a tratti*. Ecco un'illustrazione con una curva di Bézier che utilizza 7 punti di archiviazione per creare una curva cubica a due segmenti. Nota: nonostante la curva finale sia unita, non appare uniforme e continua.

<figure>
   <img src="/images/math-image87.png" width="500px">
   <figcaption>Figura (33): Due suddivisioni di Bézier condividono un punto.</figcaption>
</figure>  

Sebbene le curve di Hermite utilizzano lo stesso numero di parametri come curve di Bézier (quattro parametri per definire una curva), offrono le informazioni aggiuntive della curva tangente, che possono anche essere condivise con il tratto successivo per creare una curva dall'aspetto uniforme con meno spazio di archiviazione totale, come mostrato di seguito.  

<figure>
   <img src="/images/math-image88.png" width="500px">
   <figcaption>Figura (34): Due suddivisioni di Hermite condividono un punto e una tangente.</figcaption>
</figure>  

Una NURBS (Non-uniform rational B-spline) è una potente rappresentazione di curve, che mantiene curve ancora più uniformi e continue. I segmenti condividono più punti di controllo per creare curve ancora più uniformi con meno spazio di archiviazione.  

<figure>
   <img src="/images/math-image90.png" width="500px">
   <figcaption>Figura (35): Due suddivisioni con NURBS di grado 3 condividono tre punti di controllo.</figcaption>
</figure>  

Le curve e le superfici NURBS corrispondono alla principale rappresentazione matematica usata da Rhino per rappresentare la geometria. Le caratteristiche e i componenti delle curve NURBS verranno trattati nel dettaglio più avanti in questo capitolo.  

### Valutazione delle curve di Bézier cubiche

Dal nome del proprio inventore, Paul de Casteljau, l'algoritmo di Casteljau valuta le curve di Bézier usando un metodo ricorsivo. I passi relativi all'algoritmo possono essere riepilogati come segue:  

**Input:**  

&nbsp; Quattro punti {{< mathjax >}}$$A$${{< /mathjax >}}, {{< mathjax >}}$$B$${{< /mathjax >}}, {{< mathjax >}}$$C$${{< /mathjax >}}, {{< mathjax >}}$$D$${{< /mathjax >}} definiscono una curva {{< mathjax >}}$$t$$${{< /mathjax >}}, è un qualsiasi parametro nel dominio della curva  

**Output:**  

{{< image url="/images/math-image72.png" alt="/images/math-image72.png" class="float_right" width="325" >}}   

Il punto {{< mathjax >}}$$R$${{< /mathjax >}} sulla curva che si trova sul parametro {{< mathjax >}}$$t$${{< /mathjax >}}.  

**Soluzione:**  

1.	Trova il punto {{< mathjax >}}$$M$${{< /mathjax >}} in corrispondenza del parametro {{< mathjax >}}$$t$${{< /mathjax >}} sulla riga  {{< mathjax >}}$$\overline{AB}$${{< /mathjax >}}.    
  2.Trovare il punto {{< mathjax >}}$$N$${{< /mathjax >}} in corrispondenza del parametro {{< mathjax >}}$$t$$${{< /mathjax >}} sulla linea  {{< mathjax >}}$$\overline{BC}$${{< /mathjax >}}.   
  3.Trovare il punto {{< mathjax >}}$$O$${{< /mathjax >}} in corrispondenza del parametro {{< mathjax >}}$$t$$${{< /mathjax >}} sulla retta {{< mathjax >}}$$\overline{CD}$${{< /mathjax >}}.   
  4.Trovare il punto {{< mathjax >}}$$P$${{< /mathjax >}} in corrispondenza del parametro {{< mathjax >}}$$t$${{< /mathjax >}} sulla riga {{< mathjax >}}$$\overline{MN}$${{< /mathjax >}}.   
  5.Trovare il punto {{< mathjax >}}$$Q$${{< /mathjax >}} in corrispondenza del parametro {{< mathjax >}}$$t$${{< /mathjax >}} sulla riga {{< mathjax >}}$$\overline{NO}$${{< /mathjax >}}.   
  6.Trovare il punto {{< mathjax >}}$$R$${{< /mathjax >}} in corrispondenza del parametro {{< mathjax >}}$$t$${{< /mathjax >}} sulla riga {{< mathjax >}}$$\overline{PQ}$${{< /mathjax >}}.   

## 3.2 Curve NURBS

La geometria NURBS è una rappresentazione matematica precisa di curve molto intuitiva e facile da modificare. È facile rappresentare curve free-form usando NURBS e la struttura di controllo semplifica e rende intuitivo il processo di modifica.  

<figure>
   <img src="/images/math-image74.png">
   <figcaption>Figura (36): NURBS (Non-uniform rational B-splines) e la struttura di controllo.</figcaption>
</figure>

Esistono numerosi libri e bibliografia di riferimento per gli utenti interessati ad approfondire l'argomento sulla geometria NURBS. Tuttavia, è necessario conoscere i concetti di base relativi alle NURBS per poter usare i modellatori NURBS in modo più efficace. Ecco quattro attributi principali che definiscono la curva NURBS: grado, punti di controllo, nodi e regole di valutazione.

1. [Wikipedia: Algoritmo di De Boor.](http://en.wikipedia.org/wiki/De_Boor's_algorithm)
2. [Michigan Tech, Department of Computer Science, De Boor's algorithm.](http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/de-Boor.html)

### Grado

Il grado della curva è un numero intero positivo. Rhino consente di lavorare con curve di qualsiasi grado iniziando da 1. I gradi 1, 2, 3 e 5 sono i più utili mentre il grado 4 e i gradi superiori a 5 non sono molto usati nel mondo reale. Di seguito, alcuni esempi di curve e il grado corrispondente:  

<table width="100%">  
<tr style="border-bottom: 1px solid #ccc;border-top: 1px solid #ccc;">  
<td><b>Linee</b> e <b>polilinee</b> presentano curve NURBS di grado 1.</td>  
<td width="50%"><img src="/images/math-image75.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td><b>Cerchi</b> ed <b>ellissi</b> presentano curve NURBS di grado 2. </td>  
<td><img src="/images/math-image77.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Le <b>curve</b>free-form sono di solito rappresentate come <br> curve NURBS di grado 3 o 5. </td>  
<td> <img src="/images/math-image128.png"></td>  
</tr>  
</table>  

### Punti di controllo

I punti di controllo di una curva NURBS includono almeno punti di grado+1. Il modo più intuitivo di modificare la forma di una curva NURBS è spostarne i punti di controllo.  

Il numero di punti di controllo che coinvolgono ciascuna suddivisione in una curva NURBS viene definito dal grado della curva. Ad esempio, ciascuna suddivisione in una curva di grado -1 è modificata solo da due punti di controllo finali. In una curva di grado -2, tre punti di controllo modificano ciascuna suddivisione e così via.  


<table width="100%">  
<tr style="border-bottom: 1px solid #ccc;border-top: 1px solid #ccc;">  
<td>Le curve con punti di controllo di grado 1 attraversano tutti i punti di controllo della curva. In una curva NURBS di grado 1, due punti di controllo (di grado+1) definiscono ciascuna suddivisione. Usando cinque punti di controllo, la curva presenta quattro suddivisioni. </td>  
<td width="50%"><img src="/images/math-image130.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>I cerchi e le ellissi sono esempi di curve di grado due. In una curva NURBS di grado 2, tre punti di controllo (di grado+1) definiscono ciascuna suddivisione. Usando cinque punti di controllo, la curva presenta tre suddivisioni.</td>  
<td><img src="/images/math-image132.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Le curve con punti di controllo di grado 3 non toccano di solito la curva, ad eccezione dei punti finali in curve aperte. In una curva NURBS di grado 3, quattro punti di controllo (di grado+1) definiscono ciascuna suddivisione. Usando cinque punti di controllo, la curva presenta due suddivisioni. </td>  
<td> <img src="/images/math-image134.png"></td>  
</tr>  
</table>  

### Pesi dei punti di controllo

Ciascun punto di controllo ha associato un numero chiamato *peso*. Tranne che per alcune eccezioni, i pesi sono numeri positivi. Quando tutti i punti di controllo hanno lo stesso peso, di solito 1, la curva viene definita non razionale. Intuitivamente, possiamo considerare i pesi come la quantità di gravità di ciascun punto di controllo. Se il peso relativo di un punto di controllo è elevato, la curva viene avvicinata di più a tale punto di controllo.

Si consiglia di evitare di cambiare i pesi delle curve. Cambiando i pesi, raramente si ottiene il risultato desiderato e implica calcoli difficili in operazioni come intersezioni. L'unico motivo valido per usare curve razionali è la rappresentazione di curve che altrimenti non possono essere tracciate, come ad esempio cerchi ed ellissi.  

<figure>
   <img src="/images/math-image135.png" width="500px">
   <figcaption>Figura (37): L'effetto della variazione di peso dei punti di controllo sulla curva risultante. 
La curva a sinistra è una curva non razionale con pesi di punti di controllo uniformi. 
Il cerchio a destra è una curva razionale con punti di controllo angolari che presentano un peso inferiore a 1.</figcaption>
</figure>  

### Nodi

Ciascuna curva NURBS presenta un elenco di numeri associati chiamati *nodi* (a volte definiti *vettori nodi*). I nodi non sono molto facili da capire e impostare. Utilizzando un modellatore 3D, non occorre impostare manualmente i nodi per ciascuna curva creata. Di seguito, vengono spiegate alcune nozioni utili sui nodi.

### I nodi come valori parametrici

I nodi rappresentano un elenco di valori parametrici nel dominio di una curva. In Rhino, esistono più nodi di grado meno 1 che punti di controllo. Cioè il numero di nodi è uguale al
numero di punti di controllo più il grado della curva meno 1:

|nodi| = |punti di controllo| + grado -1

Di solito, per le curve non periodiche, i nodi del primo grado sono uguali al minimo del dominio e i nodi dell'ultimo grado sono uguali al massimo del dominio.

Ad esempio, i nodi di una curva NURBS di grado 3 aperta con 7 punti di controllo e un dominio compreso fra 0 e 4 potrebbe apparire come <0, 0, 0, 1, 2, 3, 4, 4, 4>.


<figure>
   <img src="/images/figure-38a.png" width="500px">
   <figcaption>Figura (38): In Rhino, esistono più nodi di grado -1 (meno 1) che punti di controllo. Se il numero di punti di  controllo è uguale a 7 e il grado della curva è uguale a 3, il numero di nodi è 9.
   I valori dei nodi sono parametri che valutano i punti sulla curva 3D.</figcaption>
</figure>

Scalare l'elenco dei nodi non influisce sulla curva 3D. Se cambi il dominio della curva nell'esempio precedente impostando “da 0 a 4” anziché “da 0 a 1”, l'elenco dei nodi viene scalato, ma la curva 3D non cambia.


<figure>
   <img src="/images/math-image-figure38A.png" width="500px">
   <figcaption>Figura (39): Scalare l'elenco dei nodi non cambia la curva 3D.</figcaption>
</figure>

Definiamo nodo semplice un nodo con un valore che appare solo una volta. I nodi interni sono di solito nodi semplici come nei due esempi precedenti.

### Molteplicità di nodi

La molteplicità di un nodo è il numero di volte in cui il nodo appare nell'elenco dei nodi. La molteplicità di un nodo non può essere superiore al grado della curva. La molteplicità di nodi viene usata per controllare la continuità nel punto della curva corrispondente.  

### Nodi a molteplicità piena

Un nodo a molteplicità piena presenta una molteplicità uguale al grado della curva. Un nodo a molteplicità piena presenta il punto di controllo corrispondente e la curva passa attraverso questo punto.  

Ad esempio, le curve fisse o aperte presentano nodi a molteplicità piena sugli estremi della curva. Ciò è dovuto al fatto che i punti di controllo finali coincidono con la curva e i punti. I nodi a molteplicità piena consentono un punto di discontinuità nella curva sul punto corrispondente. 

Ad esempio, le due curve seguenti sono entrambe di grado 3 e presentano lo stesso numero di punti di controllo nella stessa posizione. Tuttavia, presentano diversi nodi e anche la loro forma è diversa. La molteplicità piena forza la curva attraverso il punto di controllo associato.

Ecco due curve che hanno lo stesso grado, lo stesso numero e la stessa posizione dei punti di controllo, ma che hanno un vettore di nodi diverso che determina una forma diversa della curva:  

<table width="100%">  
<tr style="border-bottom: 1px solid #ccc;border-top: 1px solid #ccc;">  
<td>Degree = 3<br>
Numero di punti di controllo = 7<br>
knots = <0,0,0,1,2,3,4,4,4> = 9 knots<br>
Dominio (da 0 a 4)</td>  
<td width="50%"><img src="/images/math-image151.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Degree = 3<br>
Numero di punti di controllo = 7<br>
knots = <0,0,0,1,1,1,4,4,4> = 9 knots<br>
Dominio (da 0 a 4) <br>
<b>Nota:</b> un nodo a molteplicità piena al centro crea un punto di discontinuità e la curva viene forzata a passare per il punto di controllo associato.</td>  
<td><img src="/images/math-image154.png"></td>  
</tr>  
</table> 

### Nodi uniformi

Un elenco uniforme di nodi in curve aperte soddisfa la seguente condizione:

I nodi che iniziano con un nodo a molteplicità piena sono seguiti da nodi semplici e terminano con un nodo a molteplicità piena. I valori aumentano a intervalli uguali. Questa è una caratteristica tipica delle curve fisse o aperte. Le curve chiuse periodiche funzionano in modo diverso come vedremo in seguito.  

<figure>
   <img src="/images/math-image-figure41.png" width="500px">
   <figcaption>Figura (40): L'elenco di nodi uniformi indica che lo spazio fra i nodi è costante, ad eccezione delle curve fisse in cui queste possono essere nodi a molteplicità piena all'inizio e alla fine e che sono considerate comunque uniformi. La curva a sinistra è periodica (chiusa senza punti di discontinuità) e quella a destra è fissa (aperta).</figcaption>
</figure> 

### Nodi non uniformi

Le curve NURBS vengono usate per ottenere spazi non uniformi fra i nodi. Ciò può aiutare a controllare la curvatura lungo la curva per creare curve più uniformi. Il seguente esempio mostra l'interpolazione attraverso punti usando l'elenco di nodi non uniformi a sinistra e nodi uniformi a destra. In generale, se lo spazio fra nodi di una curva NURBS è proporzionale allo spazio fra i punti di controllo, la curva è più uniforme. 

<figure>
   <img src="/images/figure-38b.png" width="500px">
   <figcaption>Figura (41): L'elenco di nodi non uniformi può aiutare a creare curve più uniformi. La curva sull'interpolazione sinistra attraverso punti con nodi non uniformi crea una curvatura più uniforme. La curva sull'interpolazione destra attraverso gli stessi punti, ma forzando uno spazio uniforme di nodi, crea una curva non uniforme.</figcaption>
</figure> 

Un esempio di curva non uniforme e razionale è rappresentato da un cerchio NURBS. L'esempio seguente è una curva di grado 2 con 9 punti di controllo e 10 nodi. Il dominio è compreso fra 0 e  4 e lo spazio alternato è compreso fra 0 e 1.
knots = <0,0,1,1,2,2,3,3,4,4> --- (full multiplicity in the interior knots)
spazio fra nodi = [0,1,0,1,0,1,0,1,0] --- (non-uniform)

<figure>
   <img src="/images/math-image-figure43.png" width="500px">
   <figcaption>Figura (42): Un'approssimazione NURBS di un cerchio rappresenta una NURBS razionale non uniforme.</figcaption>
</figure> 

### Regola di stima

La regola di stima utilizza una formula matematica che assegna un punto a un numero nel dominio di una curva. La formula prende in considerazione il grado, i punti di controllo e i nodi.  

Usando questa formula, le funzioni di curva specializzate usano il parametro di una curva e creano il punto corrispondente su tale curva. Un parametro è un numero sul dominio di una curva. Di solito, i domini aumentano e sono formati da due numeri: il parametro di dominio minimo {{< mathjax >}}$$t(0)$${{< /mathjax >}} viene considerato punto iniziale della curva e il parametro massimo {{< mathjax >}}$$t(1)$${{< /mathjax >}} viene considerato il punto finale della curva.   

<figure>
   <img src="/images/math-image153.png" width="500px">
   <figcaption>Figura (43): Valutare i parametri in base ai punti della curva.</figcaption>
</figure>  

### Caratteristiche delle curve NURBS

Per creare una curva NURBS, occorre fornire le informazioni seguenti:

- Dimensione, di solito 3.
- Grado, (a volte usa l'*ordine* che è uguale al grado+1).
- Punti di controllo (elenco di punti).
- Peso del punto di controllo (elenco di numeri).
- Nodi (elenco di numeri).

Quando viene creata una curva, occorre definire almeno il grado e le posizioni dei punti di controllo. Il resto delle informazioni necessarie per costruire le curve NURBS possono essere ricavate automaticamente. Selezionare il punto di fine, per farlo coincidere con il punto di inizio, crea di solito una curva chiusa periodica. La seguente tabella mostra esempi di curve aperte e chiuse:  


<table width="100%">  
<tr style="border-bottom: 1px solid #ccc;border-top: 1px solid #ccc;">  
<td>Curva aperta di grado 1.<br>
La curva attraversa tutti i punti di controllo.</td>  
<td width="50%"><img src="/images/math-image148.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Curva aperta di grado 3.<br>
Entrambi gli estremi della curva coincidono con i punti di controllo.</td>  
<td><img src="/images/math-image147.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Curva periodica chiusa di grado 3.<br>
Il punto di giunzione della curva non attraversa un punto di controllo.</td>  
<td><img src="/images/math-image150.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Lo spostamento dei punti di controllo di una curva periodica non influisce sull'uniformità della curva.</td>  
<td><img src="/images/math-image149.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>I punti di discontinuità vengono creati quando si forza la curva a passare per alcuni punti di controllo.</td>  
<td><img src="/images/math-image146.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Spostare i punti di controllo di una curva non periodica non garantisce la continuità uniforme di una curva, ma consente un maggiore controllo sul risultato.</td>  
<td><img src="/images/math-image145.png"></td>  
</tr>  
</table>  

### Curve fisse e curve NURBS periodiche

I punti di fine di curve fisse chiuse coincidono con i punti di controllo di fine. Le curve periodiche sono curve chiuse uniformi. Il modo migliore per capire le differenze fra i due tipi di curva è confrontarne i punti di controllo e i nodi.  

L'esempio seguente mostra una curva NURBS non razionale, fissa e aperta. Questa curva presenta quattro punti di controllo, nodi uniformi a molteplicità piena in corrispondenza dei nodi di inizio e di fine e i pesi di tutti i punti di controllo sono uguali a 1.  

<figure>
   <img src="/images/math-image118.png" width="500px">
   <figcaption>Figura (44): Analisi di curve NURBS non razionali aperte di grado 3.</figcaption>
</figure>  

La seguente curva circolare è un esempio di curva NURBS periodica chiusa di grado 3. È anche non razionale poiché tutti i pesi sono uguali. Nota: le curve periodiche richiedono più punti di controllo con alcune sovrapposizioni. Inoltre, i nodi sono nodi semplici.  

<figure>
   <img src="/images/math-image119.png" width="500px">
   <figcaption>Figura (45): Analisi di una curva NURBS periodica chiusa di grado 3.</figcaption>
</figure>  

Nota: la curva periodica converte i quattro punti di input in sette punti di controllo (di grado+4) mentre la curva fissa usa solo i quattro punti di controllo. La curva periodica utilizza solo nodi semplici mentre i nodi di inizio e di fine di una curva fissa presentano molteplicità piena, forzando la curva ad attraversare i punti di controllo di inizio e di fine.  

Se impostiamo il grado degli esempi precedenti su 2 anziché su 3, i nodi diventano più piccoli e il numero di punti di controllo di curve periodiche cambia.  

<figure>
   <img src="/images/math-image120.png" width="500px">
   <figcaption>Figura (46): Analisi di una curva NURBS aperta di grado 2.</figcaption>
</figure>  

<figure>
   <img src="/images/math-image121.png" width="500px">
   <figcaption>Figura (47): Analisi di una curva NURBS periodica chiusa di grado 2.</figcaption>
</figure>  

### Pesi

I pesi dei punti di controllo in una curva NURBS uniforme sono impostati su 1, ma questo numero può cambiare in curve NURBS razionali. L'esempio seguente mostra l'effetto della variazione dei pesi dei punti di controllo.

<figure>
   <img src="/images/math-image122.png" width="500px">
   <figcaption>Figura (48): Analisi dei pesi in una curva NURBS aperta.</figcaption>
</figure>  

<figure>
   <img src="/images/math-image115.png" width="500px">
   <figcaption>Figura (49): Analisi dei pesi in una curva NURBS chiusa.</figcaption>
</figure>  

### Valutazione delle curve NURBS

{{< image url="/images/math-image114.png" alt="/images/math-image114.png" class="float_right" width="350" >}}  

Dal nome del proprio inventore, Carl de Boor, l'algoritmo di De Boorè una generalizzazione dell'algoritmo di Casteljau per le curve di Bézier. Si tratta di un algoritmo numericamente stabile, ampiamente usato per valutare punti sulle curve NURBS in applicazioni 3D. Il seguente esempio si riferisce alla valutazione di un punto su una curva NURBS di grado 3 usando l'algoritmo di De Boor.  

**Input:**  
Sette punti di controllo da {{< mathjax >}}$$P0$${{< /mathjax >}} a {{< mathjax >}}$$P6$${{< /mathjax >}}  
Nodi:  
&nbsp; {{< mathjax >}}$$u_0 = 0.0$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$u_1 = 0.0$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$u_2 = 0.0$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$u_3= 0.25$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$u_4 = 0.5$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$u_5 = 0.75$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$u_6 = 1.0$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$u_7 = 1.0$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$u_8 = 1.0$${{< /mathjax >}}  

**Output:**  

Punto su curva, ovvero in {{< mathjax >}}$$u=0.4$${{< /mathjax >}}  

**Soluzione:**  

1\. Calcolo dei coefficienti per la prima iterazione:  
&nbsp; {{< mathjax >}}$$A_c = ((u – u_1)/(u_{1+3} – u_1) = 0.8$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$B_c = (u – u_2)/(u_{2+3} – u_2) = 0.53$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$C_c = (u – u_3)/(u_{3+3} – u_3) = 0.2$${{< /mathjax >}}  

2\. Calcolo dei punti usando i dati di coefficiente:  
&nbsp; {{< mathjax >}}$$A = 0.2P_1 + 0.8P_2$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$B = 0.47 P_2 + 0.53 P_3$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$C = 0.8 P_3 + 0.2 P_4$${{< /mathjax >}}  

3\.	Calcolo dei coefficienti per la seconda iterazione:  
&nbsp; {{< mathjax >}}$$D_c = (u – u_2) / (u_{2+3-1} – u_2) = 0.8$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$E_c = (u – u_3) / (u_{3+3-1} – u_3) = 0.3$${{< /mathjax >}}  

4\.	Calcolo dei punti usando i dati di coefficiente:  
&nbsp; {{< mathjax >}}$$D = 0.2A+ 0.8B$${{< /mathjax >}}   
&nbsp; {{< mathjax >}}$$E = 0.7B + 0.3C$${{< /mathjax >}}   

5\.	Calcolo dell'ultimo coefficiente:  
&nbsp; {{< mathjax >}}$$Fc = (u – u_3)/ (u_{3+3-2} – u_3) = 0.6$${{< /mathjax >}}  

Trova il punto sulla curva nel parametro {{< mathjax >}}$$u=0.4$${{< /mathjax >}}:  

&nbsp; {{< mathjax >}}$$F= 0.4D + 0.6E$${{< /mathjax >}}  

{{< div class="clear_both" />}}  

## 3.3 Continuità geometrica delle curve

La continuità è un concetto importante nella modellazione 3‑D. La continuità è importante per ottenere uniformità visiva, illuminazione tenue e flusso dell'aria.
La seguente tabella mostra varie continuità e le definizioni corrispondenti:  

| **G0**| (posizione continua) | Due segmenti di curva uniti insieme |  
| **G1**| (tangente continua) | La direzione di una tangente nel punto di unione è la stessa per entrambi i segmenti di curva. |  
 **G2**| (curvatura continua) | Le curvature così come le tangenti concordano con entrambi i segmenti di curva nel punto finale comune. |  
| **GN**|....... | Le curve concordano con un ordine più alto |  

<figure>
   <img src="/images/math-image138.png" >
   <figcaption>Figura (50): Esaminare la continuità di curve con analisi del grafico di curvatura.</figcaption>
</figure>  

## 3.4 Curvatura

La curvatura è un concetto ampiamente usato nella modellazione 3‑D di curve e superfici. La curvatura è definita come la variazione di inclinazione di una tangente su una curva, sulla lunghezza di unità di un arco. Per un cerchio o una sfera, la curvatura è il reciproco del raggio ed è costante sull'intero dominio.   

In qualsiasi punto di una curva sul piano, la linea che si avvicina di più alla curva che attraversa questo punto è la linea tangente. Possiamo anche trovare il cerchio che si avvicina di più, che attraversa questo punto e che è tangente alla curva. Il reciproco del raggio di questo cerchio è la curvatura della curva in questo punto.  

<figure>
   <img src="/images/math-image188.png" >
   <figcaption>Figura (51): Esaminare la curvatura di una curva in diversi punti.</figcaption>
</figure>  

Il cerchio che si avvicina di più può trovarsi a destra o a sinistra. In questo senso, possiamo per esempio assegnare un segno positivo alla curvatura se il cerchio si trova a sinistra della curva e un segno negativo se si trova a destra della curva. Questo concetto viene denominato curvatura con segno. I valori di curvatura di curve unite indicano la continuità fra le curve.  

## 3.5 Superfici parametriche

### Parametri di superficie

Una superficie parametrica è una funzione di due parametri indipendenti (indicati normalmente come {{< mathjax >}}$$u$${{< /mathjax >}}, {{< mathjax >}}$$v$${{< /mathjax >}}) su domini bidimensionali. Prendiamo come esempio un piano. Se abbiamo un punto {{< mathjax >}}$$P$${{< /mathjax >}} sul piano e due vettori non paralleli sul piano, {{< mathjax >}}$$\vec a$${{< /mathjax >}} e {{< mathjax >}}$$\vec b$${{< /mathjax >}} allora possiamo definire un'equazione del piano parametrica in termini di due parametri {{< mathjax >}}$$u$${{< /mathjax >}} e {{< mathjax >}}$$v$${{< /mathjax >}} come segue:  

{{< mathjax >}}$$P = P’ + u * \mathbf{\vec a} + v * \mathbf{\vec b}$${{< /mathjax >}}  

Dove:  

&nbsp; {{< mathjax >}}$$P’$${{< /mathjax >}}: è un punto noto sul piano.  
&nbsp; {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}: è il primo vettore sul piano.  
&nbsp; {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}: è il primo vettore sul piano.  
&nbsp; {{< mathjax >}}$$u$${{< /mathjax >}}: è il primo parametro.  
&nbsp; {{< mathjax >}}$$v$${{< /mathjax >}}: è il primo parametro.  

<figure>
   <img src="/images/math-image189.png" width="500px" >
   <figcaption>Figura (52): Il rettangolo parametrico di un piano.</figcaption>
</figure>  

Un altro esempio è la sfera. L'equazione cartesiana di una sfera centrata nell'origine con il raggio {{< mathjax >}}$$R$${{< /mathjax >}} è  

{{< mathjax >}}$$x^2 + y^2 + z^2 = R^2$${{< /mathjax >}}

Ciò vuol dire che per ciascun punto esistono tre variabili ({{< mathjax >}}$$x$${{< /mathjax >}}, {{< mathjax >}}$$y$${{< /mathjax >}}, {{< mathjax >}}$$z$${{< /mathjax >}}), questo scenario non è utile per una rappresentazione parametrica che richiede due variabili. Tuttavia, nel sistema di coordinate sferiche, ciascun punto viene trovato usando i tre valori:

{{< mathjax >}}$$r$${{< /mathjax >}}: distanza radiale tra il punto e l'origine.  
{{< mathjax >}}$$θ$${{< /mathjax >}}: l'angolo dall'asse x sul piano xy.  
{{< mathjax >}}$$ø$${{< /mathjax >}}: l'angolo tra l'asse z e il punto.  

<figure>
   <img src="/images/math-image127.png" >
   <figcaption>Figura (53): Sistema di coordinate sferiche.</figcaption>
</figure>  

È possibile ottenere una conversione di punti da coordinate sferiche a coordinate cartesiane come segue:  

&nbsp; {{< mathjax >}}$$x = r * sin(ø) * cos(θ)$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$y = r * sin(ø) * sin(θ)$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$z = r * cos (ø)$${{< /mathjax >}}  

Dove:  

&nbsp; {{< mathjax >}}$$r$${{< /mathjax >}} è la distanza dall'origine {{< mathjax >}}$$≥ 0$${{< /mathjax >}}   
&nbsp; {{< mathjax >}}$$θ$${{< /mathjax >}} è in esecuzione da {{< mathjax >}}$$0$${{< /mathjax >}} a {{< mathjax >}}$$2π$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$ø$${{< /mathjax >}} è in esecuzione da {{< mathjax >}}$$0$${{< /mathjax >}} a {{< mathjax >}}$$π$${{< /mathjax >}}  

Poiché {{< mathjax >}}$$r$${{< /mathjax >}} è costante in una superficie sferica, abbiamo lasciato solo due variabili, quindi possiamo usare l'esempio precedente per creare una rappresentazione parametrica di una superficie sferica:  

&nbsp; {{< mathjax >}}$$u = θ$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$v = ø$${{< /mathjax >}}  

Quindi abbiamo:  

&nbsp; {{< mathjax >}}$$x = r * sin(v) * cos(u)$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$y = r * sin(v) * sin(u)$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$z = r * cos(v)$${{< /mathjax >}}  

Where ({{< mathjax >}}$$u$${{< /mathjax >}}, {{< mathjax >}}$$v$${{< /mathjax >}}) è all'interno del dominio ({{< mathjax >}}$$2 π$${{< /mathjax >}}, {{< mathjax >}}$$π$${{< /mathjax >}})

<figure>
   <img src="/images/math-image191.png" >
   <figcaption>Figura (54): Il rettangolo parametrico di una sfera.</figcaption>
</figure>  

La superficie parametrica segue la forma generale:  
&nbsp; {{< mathjax >}}$$x = x(u,v)$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$y = y(u,v)$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$z = z(u,v)$${{< /mathjax >}}  

Dove:  

&nbsp; {{< mathjax >}}$$u$${{< /mathjax >}} e {{< mathjax >}}$$v$${{< /mathjax >}} sono due parametri nel dominio o regione della superficie.  

### Dominio di superficie

Un dominio di superficie è definito come intervallo di ({{< mathjax >}}$$u,v$${{< /mathjax >}}) parametri valutati in un punto 3D sulla superficie. Il dominio in ciascuna dimensione ({{< mathjax >}}$$u$${{< /mathjax >}} o {{< mathjax >}}$$v$${{< /mathjax >}}) è di solito descritto come due numeri reali ({{< mathjax >}}$$u_{min}$${{< /mathjax >}} a {{< mathjax >}}$$u_{max}$${{< /mathjax >}}) e ({{< mathjax >}}$$v_{min}$${{< /mathjax >}} a {{< mathjax >}}$$v_{max}$${{< /mathjax >}})

Cambiare un dominio di superficie significa *riparametrizzare* la superficie. Un dominio crescente indica che il valore minimo del dominio punta verso il punto minimo della superficie. Di solito i domini sono crescenti, ma non sempre.

<figure>
   <img src="/images/math-image192.png" >
   <figcaption>Figura (55): superficie NURBS nello spazio di modellazione 3D (a sinistra). Il rettangolo parametrico di superficie con il dominio che va da u0 a u1 nella prima direzione e da v0 a v1 nella seconda direzione (a destra).</figcaption>
</figure>  

### Valutazione di una superficie

Valutare una superficie in un parametro nel dominio di una superficie crea un punto che si trova sulla superficie. Occorre tenere in considerazione che il centro del dominio ({{< mathjax >}}$$u_{mid}$${{< /mathjax >}}, {{< mathjax >}}$$v_{mid}$${{< /mathjax >}}) potrebbe non necessariamente essere considerato il punto centrale della superficie 3D. Inoltre, considerare i valori {{< mathjax >}}$$u-$${{< /mathjax >}} e {{< mathjax >}}$$v-$${{< /mathjax >}}  che si trovano al di fuori del dominio della superficie non fornirà un risultato utile.  

<figure>
   <img src="/images/math-image193.png" >
   <figcaption>Figura (56): Valutazione della superficie.</figcaption>
</figure>  

### Piano tangente di una superficie

Il piano tangente di una superficie in un determinato punto è rappresentato dal piano che tocca la superficie in quel punto. La direzione z del piano tangente rappresenta la direzione alla normale della superficie in quel punto.  

<figure>
   <img src="/images/math-image194.png" >
   <figcaption>Figura (57): Tangente e vettori alla normale di una superficie.</figcaption>
</figure>  

## 3.6 Continuità geometrica delle superfici
Numerosi modelli non possono essere costruiti da patch di superfici. La continuità fra patch di superfici unite è importante per ottenere uniformità visiva, riflessione della luce e flusso dell'aria.
La seguente tabella mostra varie continuità e le definizioni corrispondenti:


| **G0**| (Posizione continua) | Due superfici unite. |  
| **G1**| (Tangenti continue) | Le tangenti corrispondenti delle due superfici lungo il bordo di unione sono parallele sia nella direzione u che v. |  
| **G2**| (Curvatura continua) | Le curvature così come le tangenti concordano con entrambe le superfici sul bordo comune. |  
| **GN**|....... Le superfici concordano con un ordine più alto. |  


<figure>
   <img src="/images/math-image126.png" >
   <figcaption>Figura (58): Esaminare la continuità di superficie con l'analisi zebra.</figcaption>
</figure>  

## 3.7 Curvatura di una superficie

Per le superfici, la curvatura della normale è una generalizzazione della curvatura sulle superfici. Dato un punto sulla superficie ed una direzione situata sul piano tangente della superficie in quel punto, la curvatura della sezione della normale viene calcolata intersecando la superficie con il piano suddiviso dal punto, la normale alla superficie in quel punto e la direzione. La curvatura della sezione della normale è la curvatura con segno di questa curva nel punto preso in considerazione.   

Se guardiamo in tutte le direzioni sul piano tangente alla superficie nel punto analizzato e calcoliamo la curvatura della sezione della normale in tutte le direzioni, otterremo un valore massimo e un valore minimo.

<figure>
   <img src="/images/math-image125.png" >
   <figcaption>Figura (59): Curvature normali.</figcaption>
</figure>  

### Curvature principali

Le curvature principali di una superficie in un punto rappresentano il minimo ed il massimo delle curvature normali in quel punto. Misurano la quantità di piegatura massima e minima della superficie in quel punto. Le curvature principali si usano per calcolare la curvatura Gaussiana e le curvature medie di una superficie.  

Ad esempio, in una superficie cilindrica, non esiste una piegatura nella direzione lineare (curvatura uguale a zero) mentre la piegatura massima si verifica durante l'intersezione con un piano parallelo alle facce di fine (curvatura uguale a 1/raggio). Quelle con due estremi creano le curvature principali di tale superficie.  

<figure>
   <img src="/images/math-image86.png" >
   <figcaption>Figura (60): Le curvature principali in un punto della superficie rappresentano le curvature minime e massime in quel punto.</figcaption>
</figure>  

### Curvatura gaussiana

La curvatura gaussiana di una superficie in un punto è il prodotto delle curvature principali in quel punto. Il piano tangente di qualsiasi punto con curvatura gaussiana positiva tocca la superficie in un solo punto, mentre il piano tangente di qualsiasi punto con curvatura gaussiana negativa taglia la superficie.  

![/images/math-image91.png](/images/math-image91.png)

A: Curvatura positiva quando la superficie è concava.  
B: Curvatura negativa quando la superficie è convessa.  
C: Curvatura pari a zero quando la superficie è piana almeno in una direzione (piano, cilindro).  

<figure>
   <img src="/images/math-image89.png" width="500px" >
   <figcaption>Figura (61): Analisi della curvatura gaussiana della superficie.</figcaption>
</figure>  

### Curvatura media

La curvatura media di una superficie in un punto è la metà della somma delle curvature principali in quel punto. Qualsiasi punto con curvatura media pari a zero presenta una curvatura gaussiana negativa o pari a zero.  

Le superfici con curvatura media in qualsiasi punto pari a zero vengono denominate superfici minime. I processi fisici che possono essere modellati con superfici minime comprendono la formazione di pellicole di sapone che si estendono su oggetti fissi, come per esempio un cappio a filo metallico. Una pellicola di sapone non viene deformata dalla pressione dell'aria (che è uguale da entrambi i lati) ed è libera di minimizzare la propria area. Una bolla di sapone, invece, racchiude una quantità fissa di aria ed ha pressioni diverse al suo interno ed al suo esterno. La curvatura media è utile per trovare zone di variazioni brusche sulla superficie della curvatura.  

Le superfici con curvatura media costante in qualsiasi punto vengono definite superfici CMC (a curvatura media costante). Le superfici a curvatura media costante includono la formazione di bolle di sapone, sia libere che attaccate agli oggetti. Una bolla di sapone, diversamente da una semplice pellicola, racchiude un volume ed esiste in uno stato di equilibrio, dove la pressione leggermente maggiore all'interno della bolla viene equilibrata dalle forze della superficie minima della bolla stessa.  

## 3.8 Superfici NURBS tagliate

È possibile paragonare le superfici NURBS a una griglia con curve NURBS che vanno in due direzioni. La forma di una superficie NURBS viene definita da un numero di punti di controllo e dal grado della superficie in ciascuna delle due direzioni (direzioni u e v). Le superfici NURBS sono efficienti per archiviare e rappresentare superfici free-form con un alto livello di precisione. Le equazioni matematiche e le informazioni sulle superfici NURBS vanno oltre le finalità di questo testo. Ci soffermeremo quindi solo sulle caratteristiche più utili ai progettisti.  

<figure>
   <img src="/images/math-image80.png" width="500px">
   <figcaption>Figura (62): La superficie NURBS con isocurve rosse nella direzione u e le isocurve verdi nella direzione v.</figcaption>
</figure>  

<figure>
   <img src="/images/math-image78.png" width="500px">
   <figcaption>Figura (63): La struttura di controllo di una superficie NURBS.</figcaption>
</figure>  

<figure>
   <img src="/images/math-image84.png" width="500px">
   <figcaption>Figura (64): Il rettangolo parametrico di una superficie NURBS.</figcaption>
</figure>  

Nella nella maggior parte dei casi, valutare i parametri a intervalli uguali nel rettangolo parametrico 2D non si traduce in intervalli uguali in uno spazio 3D.  

<figure>
   <img src="/images/math-image82.png">
   <figcaption>Figura (65): Valutazione delle superfici.</figcaption>
</figure>  

### Caratteristiche delle superfici NURBS

Le caratteristiche delle superfici NURBS sono molto simili a quelle delle curve NURBS e si distinguono solo per la presenza di un parametro aggiuntivo. Le superfici NURBS implicano i seguenti dettagli:  

- Dimensione, di solito 3.  
- Il grado nelle direzioni U e V. (a volte si usa l'ordine di grado + 1).  
- Punti di controllo (punti).  
- Pesi dei punti di controllo (numeri).  
- Nodi (numeri).  

Come nelle curve NURBS, probabilmente non occorre sapere come creare una superficie NURBS, poiché i modellatori 3D forniscono di solito strumenti utili per farlo. È comunque possibile ricostruire superfici e curve per un nuovo grado e un nuovo numero di punti di controllo. Le superfici possono essere aperte, chiuse o periodiche. Ecco alcuni esempi di superfici:  

<table width="100%">  
<tr style="border-bottom: 1px solid #ccc;border-top: 1px solid #ccc;">  
<td>Superficie di grado 1 in entrambe le direzioni u e v.
Tutti i punti di controllo giacciono sulla superficie.</td>  
<td width="50%"><img src="/images/math-image73.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Superficie aperta di grado 3 nella direzione u e di grado 1 nella direzione v.
I vertici della superficie coincidono con i punti di controllo dei vertici.</td>  
<td><img src="/images/math-image71.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Superficie non periodica chiusa di grado 3 nella direzione u e di grado 1 nella direzione v.
Alcuni punti di controllo coincidono con la giunzione della superficie.</td>  
<td><img src="/images/math-image76.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Spostare i punti di controllo di una superficie non periodica chiusa crea un punto di discontinuità e quindi la superficie non appare uniforme.</td>  
<td><img src="/images/math-image107.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Superficie periodica di grado 3 nella direzione u e di grado 1 nella direzione v.
I punti di controllo non coincidono con la giunzione della superficie.</td>  
<td><img src="/images/math-image105.png"></td>  
</tr>  
<tr style="border-bottom: 1px solid #ccc;">  
<td>Spostare i punti di controllo di una superficie periodica non influisce sull'uniformità della superficie o sulla creazione di punti di discontinuità.</td>  
<td><img src="/images/math-image111.png"></td>  
</tr>  
</table>  

### Singolarità delle superfici NURBS

Ad esempio, se in un bordo lineare di un piano semplice trascini due punti di controllo finali di un angolo, questi si sovrappongono (collassano) al centro in modo da ottenere un bordo singolo. Nota: le isocurve di superficie convergono nel punto singolo.  

<figure>
   <img src="/images/math-image109.png" width="500px">
   <figcaption>Figura (66): Contrarre due punti di una superficie NURBS rettangolare per creare una superficie triangolare con singolarità. Il rettangolo parametrico rimane rettangolare.</figcaption>
</figure>  

La forma triangolare precedente può essere creata senza singolarità. È possibile tagliare una superficie con una polilinea del triangolo. Quando esamini la struttura NURBS sottostante, questa rimane di forma rettangolare.  

<figure>
   <img src="/images/math-image99.png" width="500px">
   <figcaption>Figura (67): Tagliare una superficie NURBS rettangolare per creare a una superficie rettangolare tagliata.</figcaption>
</figure>  

Altri comuni esempi di superfici difficili da creare senza singolarità sono rappresentati dal cono o dalla sfera. La parte superiore di un cono e i bordi inferiori di una sfera vengono collassati in un punto. Indipendentemente dal fatto che esista la singolarità, il rettangolo parametrico mantiene più o meno la regione rettangolare.  

### Superfici NURBS tagliate

Le superfici NURBS possono essere tagliate o non tagliate. Le superfici tagliate usano la superficie NURBS sottostante e curve chiuse per tagliare parte della superficie. Ciascuna superficie presenta una curva chiusa che definisce il bordo più esterno (*ciclo esterno*) e può presentare curve interne chiuse non intersecanti per definire fori (*cicli interni*). Una superficie con un ciclo più esterno uguale a quello della superficie NURBS sottostante e che non presenta fori viene definita superficie *non tagliata*.

<figure>
   <img src="/images/math-image97.png" width="500px">
   <figcaption>Figura (68): Superficie tagliata nello spazio di modellazione (a sinistra) e nel rettangolo parametrico (a destra).</figcaption>
</figure>  

## 3.9 Polisuperfici

Una polisuperficie è formata da due o più superfici NURBS (possibilmente tagliate) unite tra di loro. Ciascuna superficie presenta la propria struttura, parametrizzazione e direzioni di isocurve che non devono coincidere. Le polisuperfici vengono rappresentate usando la rappresentazione del contorno (*BRep*). La struttura BRep descrive superfici, bordi e vertici con dati di taglio e connettività fra le varie parti. La superficie tagliata è rappresentata anche dalla struttura dati BRep.

<figure>
   <img src="/images/math-image103.png" width="500px">
   <figcaption>Figura (69): Le polisuperfici sono costruite da superfici unite con bordi comuni allineati perfettamente entro la tolleranza.</figcaption>
</figure>  

BRep è una struttura dati che descrive ciascuna faccia in termini di superficie sottostante, bordi 3D circostanti, vertici, tagli 2D dello spazio parametrico e rapporto tra le facce vicine. Gli oggetti BRep vengono chiamati anche solidi quando sono chiusi (perfettamente chiuse).  

Un esempio di polisuperficie è un parallelepipedo semplice composto da sei superfici non tagliate unite insieme.

<figure>
   <img src="/images/math-image101.png" width="500px">
   <figcaption>Figura (70): Parallelepipedo composto da sei superfici non tagliate unite in una polisuperficie.</figcaption>
</figure>  

Lo stesso parallelepipedo può essere creato usando le superfici tagliate, così come quello superiore mostrato nell'esempio seguente.

<figure>
   <img src="/images/math-image93.png" width="500px">
   <figcaption>Figura (71): Le facce delle scatole possono essere rifilate.</figcaption>
</figure>  

La faccia superiore e la faccia inferiore del cilindro nell'esempio seguente sono tagliate dalle superfici planari.  

<figure>
   <img src="/images/math-image92.png" width="500px">
   La figura (72) mostra i punti di controllo delle superfici sottostanti.</figcaption>
</figure>  

Abbiamo visto che la modifica di curve NURBS e di superfici non tagliate è un processo intuitivo che può essere eseguito in modo interattivo spostando i punti di controllo. Tuttavia, la modifica di superfici e polisuperfici tagliate può rappresentare una vera e propria impresa. La sfida principale è mantenere uniti i bordi uniti di varie facce entro la tolleranza desiderata. Le facce vicine che condividono facce comuni possono essere tagliate e di solito non devono coincidere con la struttura NURBS; quindi, modificare l'oggetto in modo da deformare il bordo comune, potrebbe creare un intervallo.  

<figure>
   <img src="/images/math-image51.png" width="500px">
   <figcaption>Figura (73): Due facce triangolari unite in una polisuperficie, ma che non devono coincidere con il bordo unito. Lo spostamento di un vertice crea un foro.</figcaption>
</figure>  

Un'altra sfida è rappresentata da un controllo minore sul risultato, specialmente durante la modifica della geometria tagliata.   

<figure>
   <img src="/images/math-image44.png" width="500px">
   <figcaption>Figura (74): Una volta creata la superficie tagliata, esiste un controllo limitato per modificare il risultato.</figcaption>
</figure>  

<figure>
   <img src="/images/math-image42.png" width="500px">
   <figcaption>Figura (75): Usare la tecnica di modifica tramite gabbia in Rhino per modificare polisuperfici.</figcaption>
</figure>  

Le superfici tagliate vengono descritte nello spazio parametrico usando la superficie sottostante non tagliata combinata con le curve tagliate 2D che corrispondono ai bordi 3D nella superficie 3D.  

## 3.10 Tutorial

I seguenti tutorial utilizzano i concetti appresi in questo capitolo. Utilizzano Rhinoceros 5 e Grasshopper 0.9.  

### 3.10.1 Continuità tra le curve

Esaminare la continuità fra due curve di input. La continuità implica che le curve si incontrino in corrispondenza della fine della prima curva e l'inizio della seconda curva.  

![/images/math-image48.png](/images/math-image48.png)

##### Input:

Due curve di input.

##### Parametri:

Calcolare quanto segue per poter stabilire la continuità fra due curve:

![/images/math-image46.png](/images/math-image46.png)

- Il punto di fine della prima curva	({{< mathjax >}}$$P1$${{< /mathjax >}})
- Il punto di inizio della seconda curva ({{< mathjax >}}$$P2$${{< /mathjax >}})
- La tangente in corrispondenza della fine della prima curva e all'inizio della seconda curva ({{< mathjax >}}$$T1$${{< /mathjax >}} e {{< mathjax >}}$$T2$${{< /mathjax >}}).
- La curvatura in corrispondenza della fine della prima curva e all'inizio della seconda curva ({{< mathjax >}}$$C1$${{< /mathjax >}} e {{< mathjax >}}$$C2$${{< /mathjax >}}).

##### Soluzione:

1\. Riparametrizzare le Curve in input. Eseguiamo questa operazione in modo da sapere che l'inizio della curva coincide con {{< mathjax >}}$$t=0$${{< /mathjax >}} e la fine con {{< mathjax >}}$$t=1$${{< /mathjax >}}.  
2\. Estrarre i punti di inizio e di fine di due curve e controllare se coincidono. Se è così, le due curve presentano almeno una continuità {{< mathjax >}}$$G0$${{< /mathjax >}}.  

![/images/math-image36.png](/images/math-image36.png)  

3\. Calcolare le tangenti.  
4\. Confrontare le tangenti usando il prodotto scalare. Assicurarsi di unificare i vettori. Se le curve sono parallele, la continuità sarà almeno {{< mathjax >}}$$G1$${{< /mathjax >}}.  

![/images/math-image34.png](/images/math-image34.png)  

5\. Calcolare i vettori di curvatura.  
6\. Confrontare i vettori di curvatura e, se concordano, le due curve presentano continuità {{< mathjax >}}$$G2$${{< /mathjax >}}.  

![/images/math-image40.png](/images/math-image40.png)  

7\. Creare una logica che filtra i tre risultati (G1, G2 e G3) e selezionare la continuità più alta.

![/images/math-image38.png](/images/math-image38.png)  

Usare il componente VBScript di Grasshopper:

![/images/math-image31.png](/images/math-image31.png)  

```vb
Private Sub RunScript(ByVal c1 As Curve, ByVal c2 As Curve, ByRef A As Object)

  'declare variables
  Dim continuity As New String("")
  Dim t1, t2 As Double
  Dim v_c1, v_c2, c_c1, c_c2 As Vector3d

  'extract start and end points
  Dim end_c1 = c1.PointAtEnd
  Dim start_c2 = c2.PointAtStart

  'check G0 continuity
  If end_c1.DistanceTo(start_c2) = 0 Then
    continuity = "G0"
  End If

  'check G1 continuity
  If continuity = "G0" Then
    'calculate tangents
    v_c1 = c1.TangentAtEnd
    v_c2 = c2.TangentAtStart
    'unitize tangent vectors
    v_c1.Unitize
    v_c2.Unitize
    'compare tangents
    If v_c1 * v_c2 = 1.0 Then
      continuity = "G1"
    End If
  End If

  'check G2 continuity
  If continuity = "G1" Then
    'extract the parameter at start and end of the curves domain
    t1 = c1.Domain.Max
    t2 = c2.Domain.Min
    'calculate curvature
    c_c1 = c1.CurvatureAt(t1)
    c_c2 = c2.CurvatureAt(t2)
    'unitize curvature vectors
    c_c1.Unitize
    c_c2.Unitize
    'compare vectors
    If c_c1 * c_c2 = 1.0 Then
      continuity = "G2"
    End If
  End If

  'Assign output
  A = continuity

End Sub
```
Usare il componente Python per Grasshopper:

![/images/math-image69.png](/images/math-image69.png)  

```python
#decclare variables
continuity = ""

#extract start and end points
end_c1 = c1.PointAtEnd
start_c2 = c2.PointAtStart

#check G0 continuity
if end_c1.DistanceTo(start_c2) == 0:
    continuity = "G0"

#check G1 continuity
if continuity == "G0":
    #calculate tangents
    v_c1 = c1.TangentAtEnd
    v_c2 = c2.TangentAtStart
    #unitize tangent vectors
    v_c1.Unitize()
    v_c2.Unitize()
    #compare tangents
    dot = v_c1 * v_c2
    if dot == 1.0:
        continuity = "G1"
    else:
        print("Failed G1")
        print(dot)

#check G2 continuity
if continuity == "G1":

    #extract the parameter at start and end of the curves domain
    t1 = c1.Domain.Max
    t2 = c2.Domain.Min
    #calculate curvature
    c_c1 = c1.CurvatureAt(t1)
    c_c2 = c2.CurvatureAt(t2)
    #unitize curvature vectors
    c_c1.Unitize()
    c_c2.Unitize()
    #compare vectors
    dot = c_c1 * c_c2
    if dot == 1.0:
        continuity = "G2"
    else:
        print("Failed G2")
        print(dot)

#assign output
A = continuity
```


Usare il componente C# per Grasshopper:

![/images/math-image70.png](/images/math-image70.png)  

```cs
Private Sub RunScript(ByVal c1 As Curve, ByVal c2 As Curve, ByRef A As Object)

    //decalre variables
    string continuity = ("");
    double t1, t2;
    Vector3d v_c1, v_c2, c_c1, c_c2;

    //extract start and end points
    Point3d end_c1 = c1.PointAtEnd;
    Point3d start_c2 = c2.PointAtStart;

    //check G0 continuity
    if( end_c1.DistanceTo(start_c2) == 0){
      continuity = "G0";
    }

    //check G1 continuity
    if( continuity == "G0")
    {
      //calculate tangents
      v_c1 = c1.TangentAtEnd;
      v_c2 = c2.TangentAtStart;
      //unitize tangent vectors
      v_c1.Unitize();
      v_c2.Unitize();
      //compare tangents
      if( v_c1 * v_c2 == 1.0 ){
        continuity = "G1";
      }
    }

    //check G2 continuity
    if( continuity == "G1" )
    {
      //extract the parameter at start and end of the curves domain
      t1 = c1.Domain.Max;
      t2 = c2.Domain.Min;
      //calculate curvature
      c_c1 = c1.CurvatureAt(t1);
      c_c2 = c2.CurvatureAt(t2);
      //unitize curvature vectors
      c_c1.Unitize();
      c_c2.Unitize();
      //compare vectors
      if( c_c1 * c_c2 == 1.0 ){
        continuity = "G2";
      }
    }

    //assign output
    A = continuity;

End Sub
```

### 3.10.2 Surfaces with singularity

Estrarre i punti singolari in una sfera e un cono.  

**Input:**  

Una sfera e un cono.  

![/images/math-image61.png](/images/math-image61.png)  

**Parametri:**  

La singolarità può essere rilevata attraverso i tagli dell'analisi dello spazio parametrico 2D che presentano bordi non validi o corrispondenti a lunghezza zero. Tali tagli devono essere singolari.  

**Soluzione:**  

1. La traversa attraverso tutti i tagli nell'input.  
2. Controllare se i tagli presentano un bordo non valido e contrassegnarlo come taglio singolare.  
3. Estrarre posizioni di punti nello spazio 3D.  

Usare il componente VB per Grasshopper:

![/images/math-image59.png](/images/math-image59.png)  

```vb
Private Sub RunScript(ByVal srf As Brep, ByRef A As Object)

  'Decalre a new list of points
  Dim singular_points As New List( Of Point3d)

  'Examine all trims in the input
  For Each trim As BrepTrim In srf.Trims

    'Null edge of a trim indicates a singularity
    If trim.Edge Is Nothing Then

      'Find the 2D parameter space point of the start or end of the trim
      Dim pt2d = New Point2d(trim.PointAtStart)

      'Evaluate trim end point on the object surface
      Dim pt3d = trim.Face.PointAt(pt2d.x, pt2d.y)

      'Add 3D point to the list of singular points
      singular_points.Add(pt3d)
    End If

  Next

  'Asign output
  A = singular_points

End Sub
```

Usare il componente Python per Grasshopper:

![/images/math-image53.png](/images/math-image53.png)  

```python
#Decalre a new list of points
singular_points = []

#Examine all trims in the input brep
for trim in srf.Trims:

	#Null edge of a trim indicates a singularity
	if trim.Edge == None:
		#Find the 2D parameter space point at trim start or end
		pt2d = trim.PointAtStart

		#Evaluate trim end point on the object surface
		pt3d = trim.Face.PointAt(pt2d.X, pt2d.Y)

		#Add 3D point to the list of singular points
		singular_points.append(pt3d)

#Asign output
A = singular_points
```


Usare il componente C# per Grasshopper:

![/images/math-image63.png](/images/math-image63.png)  

```cs
private void RunScript(Brep srf, ref object A)
{
  //Decalre a new list of points
  List < Point3d > singular_points = new List<Point3d>();

  //Examine all trims in the input
  foreach( BrepTrim trim in srf.Trims)
  {
    //Null edge of a trim indicates a singularity
    if( trim.Edge == null)
    {
      //Find the 2D parameter space point of the start or end of the trim
      Point2d pt2d = new Point2d(trim.PointAtStart);

      //Evaluate trim end point on the object surface
      Point3d pt3d = trim.Face.PointAt(pt2d.X, pt2d.Y);

      //Add 3D point to the list of singular points
      singular_points.Add(pt3d);
    }
  }

  //Asign output   
  A = singular_points
}
```

## Download dei file di esempio

Download del file [{{< awesome "fas fa-download">}} ](/files/math-samplesandtutorials.zip.zip) [math-samplesandtutorials.zip](/files/math-samplesandtutorials.zip) contenente tutti gli esempi di Grasshopper e i file del codice menzionati in questa guida.

## Passi successivi

Per ulteriori informazioni, consulta la guida [Riferimenti](/guides/general/essential-mathematics/references/) per conoscere la struttura dettagliata delle curve e delle superfici NURBS.  

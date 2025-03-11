+++
aliases = ["/en/5/guides/general/essential-mathematics/vector-mathematics/", "/en/6/guides/general/essential-mathematics/vector-mathematics/", "/en/7/guides/general/essential-mathematics/vector-mathematics/", "/en/wip/guides/general/essential-mathematics/vector-mathematics/"]
authors = [ "rajaa" ]
categories = [ "Essential Mathematics" ]
category_page = "guides/general/essential-mathematics/"
description = "Il capitolo 1 riguarda la matematica dei vettori, tra cui rappresentazioni e operazioni vettoriali, equazioni di primo grado ed equazioni di piani."
keywords = [ "mathematics", "geometry", "grasshopper3d" ]
languages = "unset"
sdk = [ "General" ]
title = "1 Matematica vettoriale"
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
Un vettore indica una quantità, come la velocità o la forza, con direzione e lunghezza. Nei sistemi di coordinate 3D, i vettori sono rappresentati da un gruppo ordinato di tre numeri reali del tipo:

{{< mathjax >}}$$\mathbf{\vec v}  = <a_1, a_2, a_3>$${{< /mathjax >}}

{{< youtube NU34_aCoN3E >}}

## 1.1 Rappresentazione vettoriale

In questo documento, le lettere minuscole in grassetto con la freccia in alto indicano i vettori. I componenti vettoriali vengono anche indicati fra parentesi angolari. Le lettere maiuscole indicano i punti. Le coordinate di punti vengono sempre indicate fra parentesi.

Utilizzando un sistema di coordinate e un qualsiasi insieme di punti di ancoraggio, possiamo rappresentare e visualizzare i vettori usando una rappresentazione con segmenti di linee, dove una freccia mostra la direzione del vettore. Una freccia mostra la direzione del vettore.

Ad esempio, se abbiamo un vettore con una direzione parallela all'asse X di un determinato sistema di coordinate 3D e una lunghezza di 5 unità, possiamo scrivere il vettore come segue:

{{< mathjax >}}$$\mathbf{\vec v} = <5, 0, 0>$${{< /mathjax >}}  

Per rappresentare tale vettore, occorre un punto di ancoraggio nel sistema di coordinate. Ad esempio, tutte le frecce della figura seguente sono rappresentazioni uguali dello stesso vettore, nonostante siano ancorate in diversi punti.  

<figure>
   <img src="/images/math-image169.png">
   <figcaption>Figura (1): Rappresentazione vettoriale nel sistema di coordinate 3D.</figcaption>
</figure>  

{{< call-out note "Note" >}}

Dato un vettore 3D {{< mathjax >}}$$\vec v = <a_1, a_2, a_3>$${{< /mathjax >}} , tutti i componenti del vettore {{< mathjax >}}$$a_1$${{< /mathjax >}}, {{< mathjax >}}$$a_2$${{< /mathjax >}}, {{< mathjax >}}$$a_3$${{< /mathjax >}} sono numeri reali. Inoltre, tutti i segmenti di linea da un punto {{< mathjax >}}$$A(x,y,z)$${{< /mathjax >}} a un punto {{< mathjax >}}$$B(x+a_1, y+a_2, z+a_3)$${{< /mathjax >}} sono rappresentazioni equivalenti del vettore {{< mathjax >}}$$\vec v$${{< /mathjax >}}.

{{< /call-out >}}   

Quindi, come possiamo definire i punti di fine del segmento di una retta che rappresenta un determinato vettore?
Definiamo un punto di ancoraggio (A) in questo modo:

{{< mathjax >}}$$A = (1, 2, 3)$${{< /mathjax >}}

E un vettore:

{{< mathjax >}}$$\mathbf{\vec v} = <5, 6, 7>$${{< /mathjax >}}

La punta {{< mathjax >}}$$(B)$${{< /mathjax >}} del vettore viene calcolata sommando i componenti corrispondenti dal punto di ancoraggio e dal vettore {{< mathjax >}}$$\vec v$${{< /mathjax >}}:  

{{< mathjax >}}$$B = A + \mathbf{\vec v}$${{< /mathjax >}}  
{{< mathjax >}}$$B = (1+5, 2+6, 3+7) $${{< /mathjax >}}  
{{< mathjax >}}$$B = (6, 8, 10)$${{< /mathjax >}}  


<figure>
   <img src="/images/math-image172.png">
   <figcaption>Figura (2): Rapporto fra un vettore, il punto di ancoraggio di un vettore e il punto che coincide con la posizione della punta del vettore.</figcaption>
</figure>  

{{< youtube ELQ8NgENhJY >}}
{{< youtube INtNgczxyWg >}}

### Vettore posizione

La rappresentazione di un particolare vettore utilizza il punto di origine {{< mathjax >}}$$\text{origin point} (0,0,0)$${{< /mathjax >}} come punto di ancoraggio del vettore.
Il vettore posizione {{< mathjax >}}$$\mathbf{\vec v} = <a_1,a_2,a_3>$${{< /mathjax >}} è rappresentato con un segmento di linea fra due punti, l'origine e B, quindi:  

{{< mathjax >}}$$\text{Origin point} = (0,0,0)$${{< /mathjax >}}  
{{< mathjax >}}$$B = (a_1,a_2,a_3)$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image171.png">
   <figcaption>Figura (3): Vettore posizione. Coordinate della punta del vettore uguali ai componenti vettoriali corrispondenti.</figcaption>
</figure>  

{{< call-out note "Note" >}}

Il *vettore posizione* per un determinato vettore {{< mathjax >}}$$\vec v= < a_1,a_2,a_3 >$${{< /mathjax >}} è una determinata rappresentazione di un segmento di linea dal punto di origine {{< mathjax >}}$$(0,0,0)$${{< /mathjax >}} al punto {{< mathjax >}}$$(a_1, a_2, a_3)$${{< /mathjax >}}.

{{< /call-out >}}

{{< youtube 8BNyMC4EBcw >}}

{{< youtube Ft2edI4g1qY >}}

### Vettori e punti  

Non confondere vettori e punti. Sono concetti molto diversi. Come menzionato, i vettori rappresentano una quantità con una direzione e lunghezza, mentre i punti indicano una posizione. Ad esempio, la direzione nord è un vettore mentre il polo nord è una pozione (punto).
Se abbiamo un vettore e un punto che presentano gli stessi componenti, come:  

{{< mathjax >}}$$\mathbf{\vec v} = <3,1,0>$${{< /mathjax >}}  
{{< mathjax >}}$$P = (3,1,0)$${{< /mathjax >}}  

Possiamo disegnare il vettore e il punto come segue:  

<figure>
   <img src="/images/math-image174.png">
   <figcaption>Figura (4): Un vettore definisce una direzione e una lunghezza. Un punto definisce una posizione.</figcaption>
</figure>  

{{< youtube RRrTz_QO_rA >}}

### Lunghezza del vettore  

Come indicato in precedenza, i vettori presentano una lunghezza. Utilizzeremo {{< mathjax >}}$$\vert a \vert$${{< /mathjax >}} per indicare la lunghezza di un determinato vettore {{< mathjax >}}$$ a $${{< /mathjax >}}. Per esempio:  

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = 5$${{< /mathjax >}}  

In generale, la lunghezza di un vettore {{< mathjax >}}$$\mathbf{\vec a} <a_1,a_2,a_3>$${{< /mathjax >}}  viene calcolata come segue:

{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{(a_1)^2 + (a_2)^2 + (a_3)^2} $${{< /mathjax >}}

<figure>
   <img src="/images/math-image173.png">
   <figcaption>Figura (5): Lunghezza del vettore.</figcaption>
</figure>  

### Vettore di unità

Un vettore di unità è un vettore con una lunghezza uguale a una unità. I vettori di unità sono comunemente usati per mettere a confronto le direzioni dei vettori.

{{< call-out note "Note" >}}

Un vettore di unità è un vettore con una lunghezza uguale a un'unità.

{{< /call-out >}}

Per calcolare un vettore di unità, occorre trovare la lunghezza di un determinato vettore e quindi dividere i componenti del vettore per la lunghezza. Per esempio:

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec a} \vert  = 5 \text{ unit length}$${{< /mathjax >}}  

If {{< mathjax >}}$$\mathbf{\vec b} = \text{unit vector}$${{< /mathjax >}} of {{< mathjax >}}$$a$${{< /mathjax >}}, then:  
&nbsp;&nbsp;     {{< mathjax >}}$$\mathbf{\vec b} = <4/5, 3/5, 0/5>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\mathbf{\vec b} = <0.8, 0.6, 0>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{0.8^2 + 0.6^2 + 0^2}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{0.64 + 0.36 + 0}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{(1)} = 1 \text{ unit length}$${{< /mathjax >}}  

In generale:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  

Il vettore unitario di {{< mathjax >}}$$\mathbf{\vec a} = <a_1/\vert \mathbf{\vec a} \vert , a_2/\vert \mathbf{\vec a} \vert , a_3/\vert \mathbf{\vec a} \vert >$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image176.png">
   <figcaption>Figura (6): Vettore di unità uguale alla lunghezza di una unità del vettore.</figcaption>
</figure>  

{{< youtube yVSigpl3EUo >}}

## 1.2 Operazioni di trasformazione

{{< youtube uInxocphhxI >}}

### Operazione scalare di un vettore

L'operazione scalare di un vettore implica moltiplicare un vettore per un numero. Per esempio:  

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$2* \mathbf{\vec a} = <2*4, 2*3, 2*0> $${{< /mathjax >}}  
{{< mathjax >}}$$2*\mathbf{\vec a} = <8, 6, 0>$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image175.png">
   <figcaption>Figura (7): Operazione scalare di un vettore</figcaption>
</figure>  

In generale, dato un vettore {{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}} e un numero reale {{< mathjax >}}$$t$${{< /mathjax >}}   

{{< mathjax >}}$$t*\mathbf{\vec a} = < t* a_1, t* a_2, t* a_3 >$${{< /mathjax >}}  

{{< youtube S59M8BnDYAQ >}}

### Somma vettoriale

La somma vettoriale coinvolge due vettori e ne crea un terzo. Sommiamo i vettori sommando i loro componenti.

{{< call-out note "Note" >}}

I vettori vengono sommati sommando i loro componenti.

{{< /call-out >}}

Ad esempio, se abbiamo due vettori:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 0> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <4, 1, 3> $${{< /mathjax >}}   
{{< mathjax >}}$$\mathbf{\vec a} = <+4, +1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <5, 3, 3>$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image179.png">
   <figcaption>Figura (8): Somma vettoriale.</figcaption>
</figure>  

In generale, la somma vettoriale dei due vettori a e b viene calcolata come segue:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <a_1+b_1, a_2+b_2, a_3+b_3>$${{< /mathjax >}}  

La somma vettoriale è utile per trovare la direzione media di due o più vettori. In questo caso, usiamo di solito vettori della stessa lunghezza. Ecco un esempio che mostra la differenza fra usare vettori della stessa lunghezza e vettori di lunghezza diversa nella somma vettoriale che ne risulta:  

<figure>
   <img src="/images/math-image177.png">
   <figcaption>Figura (9): Somma di vari vettori di lunghezza (a sinistra). Somma di vettori della stessa lunghezza (a destra) per ottenere la direzione media.</figcaption>
</figure>  

I vettori di input non sono probabilmente della stessa lunghezza. Per trovare la direzione media, occorre usare il vettore di unità dei vettori di input. Come menzionato in precedenza, il vettore di unità è un vettore con lunghezza pari a 1.

{{< youtube VTVk3t3WeAY >}}

### Sottrazione vettoriale

La sottrazione vettoriale coinvolge due vettori e ne crea un terzo. Sottraiamo due vettori sottraendo i componenti corrispondenti. Ad esempio, se abbiamo due vettori {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} e {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} e sottraiamo {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} da {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, allora:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 0> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <4, 1, 4> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <1-4, 2-1, 0-4>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <-3, 1, -4> = \mathbf{\mathbf{\vec b}a}$${{< /mathjax >}}

Se si sottrae {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} da {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, otteniamo un risultato diverso:  

{{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a} = <4-1, 1-2, 4-0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a} = <3, -1, 4> = \mathbf{\mathbf{\vec a}b}$${{< /mathjax >}}  

Nota: il vettore {{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a}$${{< /mathjax >}} presenta la stessa lunghezza del vettore {{< mathjax >}}$$\mathbf{\vec a} - \mathbf{\vec b}$${{< /mathjax >}}, ma va nella direzione opposta.  

<figure>
   <img src="/images/math-image178.png">
   <figcaption>Figura (10): Sottrazione del vettore.</figcaption>
</figure>  

In generale, se abbiamo due vettori, {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} and {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}, then {{< mathjax >}}$$\mathbf{\vec a} - \mathbf{\vec b}$${{< /mathjax >}} è un vettore che viene calcolato come segue:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <a_1 - b_1, a_2 - b_2, a_3 - b_3> = \mathbf{\mathbf{\vec b}a}$${{< /mathjax >}}  

La sottrazione vettoriale è comunemente usata per trovare vettori fra punti. Per trovare un vettore che va dalla punta al vettore posizione {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} alla punta del vettore posizione {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, usiamo quindi la sottrazione {{< mathjax >}}$$(\mathbf{\vec a}-\mathbf{\vec b})$${{< /mathjax >}} come mostrato nella figura (11).  

<figure>
   <img src="/images/math-image180.png">
   <figcaption>Figura (11): Usare la sottrazione vettoriale per trovare un vettore fra due punti. </figcaption>
</figure> 

{{< youtube RQK8pCIWKNY >}} 

### Proprietà vettoriali

I vettori presentano otto proprietà. Se a, b e c sono vettori ed s e t sono numeri, allora:  

{{< mathjax >}}$$\mathbf{\vec a} + \mathbf{\vec b} = \mathbf{\vec b} + \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + 0 = a$${{< /mathjax >}}  
{{< mathjax >}}$$s * (\mathbf{\vec a} + \mathbf{\vec b}) = s * a + s * \mathbf{\vec b}$${{< /mathjax >}}  
{{< mathjax >}}$$s * t * (\mathbf{\vec a}) = s * (t * \mathbf{\vec a})$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + (\mathbf{\vec b} + \mathbf{\vec c}) = (\mathbf{\vec a} + \mathbf{\vec b}) + \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + (-\mathbf{\vec a}) = 0$${{< /mathjax >}}  
{{< mathjax >}}$$(s + t) * \mathbf{\vec a} = s * \mathbf{\vec a} + t * \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$1 * \mathbf{\vec a} = \mathbf{\vec a}$${{< /mathjax >}}  

### Prodotto scalare del vettore

Il prodotto scalare coinvolge due vettori e crea un numero.
Ad esempio, se abbiamo due vettori a e b, allora:

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 3> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <5, 6, 7>$${{< /mathjax >}}  

Quindi, il prodotto scalare è la somma della moltiplicazione dei componenti, come segue:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = 1 * 5 + 2 * 6 + 3 * 7$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = 38$${{< /mathjax >}}  

In generale, dati due vettori a e b:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = a_1 * b_1 + a_2 * b_2 + a_3 * b_3$${{< /mathjax >}}  

Otteniamo sempre un numero positivo per il prodotto scalare fra due vettori quando vanno nella stessa direzione generale. Un prodotto scalare fra due vettori indica che i due vettori vanno nella direzione generale opposta.

<figure>
   <img src="/images/math-image181.png">
   <figcaption>Figura (12): Quando due vettori vanno nella stessa direzione (a sinistra), il risultato è un prodotto scalare positivo. Quando i due vettori vanno nella direzione opposta (a destra), il risultato è un prodotto scalare negativo. </figcaption>
</figure>  

Quando calcoliamo il prodotto scalare di due vettori di unità, il risultato è sempre compreso fra 1 e +1. Per esempio:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <0.6, 0.8, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = (1 * 0.6, 0 * 0.8, 0 * 0) = 0.6$${{< /mathjax >}}  

Inoltre, il prodotto scalare di un vettore in sé è uguale alla lunghezza di tale vettore secondo il potere di due. Per esempio:  

{{< mathjax >}}$$\mathbf{\vec a} = <0, 3, 4>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = 0 * 0 + 3 * 3 + 4 * 4 $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = 25$${{< /mathjax >}}  

Calcolare la lunghezza della radice quadrata di un vettore {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} :  

{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = 5$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert 2 = 25$${{< /mathjax >}}  

### Prodotto scalare del vettore, lunghezze e angoli

Esiste un rapporto fra il prodotto scalare di due vettori e l'angolo fra di loro.  

{{< call-out note "Note" >}}

Il prodotto scalare di due vettori di unità validi (diversi da zero) uguali al coseno dell'angolo fra di loro.

{{< /call-out >}}

In generale:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = \vert \mathbf{\vec a} \vert * \vert \mathbf{\vec b} \vert * cos(ө)$${{< /mathjax >}} oppure  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} / (\vert \mathbf{\vec a} \vert * \vert \mathbf{\vec b} \vert) = cos(ө)$${{< /mathjax >}}

Dove:  

{{< mathjax >}}$$ө$${{< /mathjax >}} è l'angolo incluso fra i vettori.  

Se i vettori a e b sono vettori di unità, possiamo affermare che:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = cos(ө)$${{< /mathjax >}}  

E poiché il coseno di un angolo di 90 gradi è uguale a 0, possiamo affermare che:  

{{< call-out note "Note" >}}

I vettori {{< mathjax >}}$$\vec a$${{< /mathjax >}} and {{< mathjax >}}$$\vec b$${{< /mathjax >}} sono ortogonali se, e solo se {{< mathjax >}}$$\vec{a} \cdot  \vec{b} = 0$${{< /mathjax >}}.

{{< /call-out >}}

Ad esempio, se calcoliamo il prodotto scalare di due vettori ortogonali, l'asse X e l'asse Y del sistema assoluto, il risultato sarà uguale a zero.  

{{< mathjax >}}$$\mathbf{\vec x} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec y} = <0, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}x · y = (1 * 0) + (0 * 1) + (0 * 0){{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec x} · \mathbf{\vec y} = 0$${{< /mathjax >}}  

Esiste inoltre un rapporto fra il prodotto scalare e la lunghezza della proiezione di un vettore su un altro. Per esempio:  

{{< mathjax >}}$$\mathbf{\vec a} = <5, 2, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <9, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$unit(\mathbf{\vec b}) = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · unit(\mathbf{\vec b}) = (5 * 1) + (2 * 0) + (0 * 0) $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · unit(\mathbf{\vec b}) = 2 (\text{which is equal to the projection length of mathbf{\vec a} onto mathbf{\vec b}})$${{< /mathjax >}}

<figure>
   <img src="/images/math-image182.png">
   <figcaption>Figura (13): Il prodotto scalare è uguale alla lunghezza della proiezione di un vettore su un vettore di unità diverso da zero. </figcaption>
</figure>  

In generale, dato un vettore a e un vettore diverso da zero b, possiamo calcolare la lunghezza della proiezione pL del vettore a sul vettore b usando il prodotto scalare.  

{{< mathjax >}}$$pL = \vert \mathbf{\vec a} \vert * cos(ө) $${{< /mathjax >}}  
{{< mathjax >}}$$pL = \mathbf{\vec a} · unit(\mathbf{\vec b})$${{< /mathjax >}} 

 {{< youtube ZsM2RQbVDf4 >}}

### Proprietà del prodotto scalare

Se {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} e {{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} sono vettori e s è un numero, allora:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = \vert  \mathbf{\vec a} \vert ^2$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b} + \mathbf{\vec c}) = \mathbf{\vec a} · \mathbf{\vec b} + \mathbf{\vec a} · \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$0 · \mathbf{\vec a} = 0$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = \mathbf{\vec b} · \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$(s * \mathbf{\vec a}) · \mathbf{\vec b} = s * (\mathbf{\vec a} · \mathbf{\vec b}) = \mathbf{\vec a} · (s * \mathbf{\vec b})$${{< /mathjax >}}  

### Prodotto vettoriale

Il prodotto vettoriale coinvolge due vettori e ne crea un terzo che è ortogonale a entrambi.

<figure>
   <img src="/images/math-image183.png">
   <figcaption>Figura (14): Calcolare il prodotto vettoriale di due vettori. </figcaption>
</figure>  

Ad esempio, se abbiamo due vettori su un piano assoluto XY, il loro prodotto vettoriale è un vettore perpendicolare al piano XY, che va sia nella direzione positiva che negativa dell'asse Z. Per esempio:  

{{< mathjax >}}$$\mathbf{\vec a} = <3, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <1, 2, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = < (1 * 0 – 0 * 2), (0 * 1 - 3 * 0), (3 * 2 - 1 * 1) > $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <0, 0, 5>$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Il vettore {{< mathjax >}}$$\vec a \times \vec b$${{< /mathjax >}} è ortogonale sia a {{< mathjax >}}$$\vec a$${{< /mathjax >}} che a {{< mathjax >}}$$\vec b$${{< /mathjax >}}.

{{< /call-out >}}

Probabilmente, non sarà necessario calcolare manualmente il prodotto vettoriale di due vettori, quindi è possibile ignorare questa sezione. Gli utenti interessati al calcolo del prodotto vettoriale possono continuare a leggere per un maggiore approfondimento. Il prodotto vettoriale {{< mathjax >}}$$a × b$${{< /mathjax >}} viene definito usando determinanti. Ecco una semplice illustrazione su come calcolare un determinante usando i vettori di base standard:  

{{< mathjax >}}$$ \color {red}{i} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$ \color {blue}{j} = <0,1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$ \color {green}{k} = <0, 0, 1>$${{< /mathjax >}}  

<img src="/images/math-image184.png">

Il prodotto vettoriale di due vettori {{< mathjax >}}$$\mathbf{\vec a} = <a1, a2, a3>$${{< /mathjax >}} e {{< mathjax >}}$$\mathbf{\vec b} = <b1, b2, b3>$${{< /mathjax >}} viene calcolato come segue usando il diagramma precedente:  

{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = \color {red}{i (a_2 * b_3)} + \color {blue}{ j (a_3 * b_1)} + \color {green}{k(a_1 * b_2)} - \color {green}{k (a_2 * b_1)} - \color {red}{i (a_3 * b_2)} -\color {blue}{ j (a_1 * b_3)}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = \color {red}{i (a_2 * b_3 - a_3 * b_2)} + \color {blue}{j (a_3 * b_1 - a_1 * b_3)} +\color {green}{k (a_1 * b_2 - a_2 * b_1)}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <\color {red}{a_2 * b_3 – a_3 * b_2},  \color {blue}{a_3 * b_1 - a_1 * b_3},  \color {green}{a_1 * b_2 - a_2 * b_1} >$${{< /mathjax >}}  

{{< youtube I5WkhSo4p6o >}}

### Prodotto vettoriale e angolo fra vettori

Esiste un rapporto fra l'angolo, fra i due vettori e la lunghezza del prodotto vettoriale. Quanto più piccolo è l'angolo (seno più piccolo), tanto minore sarà il prodotto vettoriale. L'ordine degli operandi è importante nel prodotto vettoriale. Per esempio:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <0, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <0, 0, 1>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} × \mathbf{\vec a} = <0, 0, -1>$${{< /mathjax >}}  


<figure>
   <img src="/images/math-image185.png">
   <figcaption>Figura (15): Rapporto fra il seno dell'angolo tra i due vettori e lunghezza del prodotto vettoriale.
</figure>  

Nel sistema destrorso di Rhino, la direzione di  {{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b}$${{< /mathjax >}} è data dalla regola della mano destra (dove {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} = dito indice, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} = dito medio e {{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b}$${{< /mathjax >}} = pollice).  

<img src="/images/math-image186.png" width="375px">  

In generale, per qualsiasi paio di vettori 3D {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} and {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}:  

{{< mathjax >}}$$\vert \mathbf{\vec a} × \mathbf{\vec b} \vert  = \vert  \mathbf{\vec a} \vert  \vert  \mathbf{\vec b} \vert  sin(ө)$${{< /mathjax >}}  

Dove:   

{{< mathjax >}}$$Ө$${{< /mathjax >}} è l'angolo compreso tra i vettori posizione di {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} and {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}  

Se a e b sono vettori di unità, possiamo quindi affermare semplicemente che la lunghezza del loro prodotto vettoriale è uguale al seno dell'angolo fra di loro. In altre parole:  

{{< mathjax >}}$$\vert \mathbf{\vec a} × \mathbf{\vec b} \vert = sin(ө)$${{< /mathjax >}}  

Il prodotto vettoriale fra due vettori ci aiuta a determinare se due vettori sono paralleli. Ciò è dovuto al risultato che è sempre un vettore uguale a zero.  

{{< call-out note "Note" >}}

I vettori {{< mathjax >}}$$\vec a$${{< /mathjax >}} e {{< mathjax >}}$$\vec b$${{< /mathjax >}} sono paralleli e se, e solo se, {{< mathjax >}}$$a \times b = 0$${{< /mathjax >}}.

{{< /call-out >}}

### Proprietà del prodotto vettoriale

Se {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} e {{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} sono vettori e {{< mathjax >}}$$s$${{< /mathjax >}} è un numero, allora:  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = -\mathbf{\vec b} × \mathbf{\vec a}$${{< /mathjax >}}   
{{< mathjax >}}$$(s * \mathbf{\vec a}) × \mathbf{\vec b} = s * (\mathbf{\vec a} × \mathbf{\vec b}) = \mathbf{\vec a} × (s * \mathbf{\vec b})$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × (\mathbf{\vec b} + \mathbf{\vec c}) = \mathbf{\vec a} × \mathbf{\vec b} + \mathbf{\vec a} × \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$(\mathbf{\vec a} + \mathbf{\vec b}) × \mathbf{\vec c} = \mathbf{\vec a} × \mathbf{\vec c} + \mathbf{\vec b} × \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b} × \mathbf{\vec c}) = (\mathbf{\vec a} × \mathbf{\vec b}) · \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × (\mathbf{\vec b} × \mathbf{\vec c}) = (\mathbf{\vec a} · \mathbf{\vec c}) * \mathbf{\vec b} – (\mathbf{\vec a} · \mathbf{\vec b}) * \mathbf{\vec c}$${{< /mathjax >}}  

## 1.3 Equazione vettoriale di una retta

L'equazione vettoriale di una retta è usata nelle applicazioni di modellazione 3D e computer grafica.

<figure>
   <img src="/images/math-image187.png">
   <figcaption>Figura (16): Equazione vettoriale di una retta.</figcaption>
</figure>  

Ad esempio, se conosciamo la direzione di una retta e di un punto su tale retta, allora possiamo trovare qualsiasi altro punto sulla retta usando i vettori, come di seguito:

{{< mathjax >}}$$\overline{L} = line$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec v} = <a, b, c>$${{< /mathjax >}} vettore unitario di direzione della retta  
{{< mathjax >}}$$Q = (x_0, y_0, z_0)$${{< /mathjax >}} punto di posizione della retta  
{{< mathjax >}}$$P = (x, y, z)$${{< /mathjax >}} qualsiasi punto sulla retta  

Sappiamo che:  

{{< mathjax >}}$$\mathbf{\vec a} = t *\mathbf{\vec v}$${{< /mathjax >}}   (2)  
{{< mathjax >}}$$\mathbf{\vec p} = \mathbf{\vec q} + \mathbf{\vec a}$${{< /mathjax >}}   (1)  

Da 1 e 2:  

{{< mathjax >}}$$\mathbf{\vec p} = \mathbf{\vec q} + t * \mathbf{\vec v}$${{< /mathjax >}}  (3)   

Tuttavia, possiamo scrivere (3) quanto segue:  

{{< mathjax >}}$$<x, y, z> = <x_0, y_0, z_0> + <t * a, t * b, t * c>$${{< /mathjax >}}  
{{< mathjax >}}$$<x, y, z> = <x_0 + t * a, y_0 + t * b, z_0 + t * c>$${{< /mathjax >}}  

Quindi:  

{{< mathjax >}}$$x = x_0 + t * a$${{< /mathjax >}}  
{{< mathjax >}}$$y = y_0 + t * b$${{< /mathjax >}}  
{{< mathjax >}}$$z = z_0 + t * c$${{< /mathjax >}}  

Che equivale a:  

{{< mathjax >}}$$P = Q + t * \mathbf{\vec v}$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Dato un punto {{< mathjax >}}$$Q$${{< /mathjax >}} e una direzione {{< mathjax >}}$$\vec v$${{< /mathjax >}} su una retta, qualsiasi punto {{< mathjax >}}$$P$${{< /mathjax >}} sulla retta può essere calcolato usando l'equazione vettoriale di una retta {{< mathjax >}}$$P = Q + t * \vec v$${{< /mathjax >}} where {{< mathjax >}}$$t$${{< /mathjax >}} è un numero.  

{{< /call-out >}}

Un altro esempio comune è trovare un punto medio fra due punti. L'esempio seguente mostra come trovare il punto medio usando l'equazione vettoriale di una retta:  

{{< mathjax >}}$$\mathbf{\vec q}$${{< /mathjax >}} è il vettore posizione per il punto {{< mathjax >}}$$Q$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec p}$${{< /mathjax >}}  è il vettore posizione per il punto {{< mathjax >}}$$P$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} è il vettore che va da {{< mathjax >}}$$Q \rightarrow P$${{< /mathjax >}}  

Della sottrazione vettoriale, sappiamo che:  

{{< mathjax >}}$$\mathbf{\vec a} = \mathbf{\vec p} - \mathbf{\vec q}$${{< /mathjax >}}  

Dell'equazione della retta, sappiamo che:  

{{< mathjax >}}$$M = Q + t * \mathbf{\vec a}$${{< /mathjax >}}  

E visto che dobbiamo trovare un punto medio, allora:  

{{< mathjax >}}$$t = 0.5$${{< /mathjax >}}  

Possiamo quindi affermare che:  

{{< mathjax >}}$$M = Q + 0.5 * \mathbf{\vec a}$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image159.png">
   <figcaption>Figura (17): Trovare il punto medio fra due punti di input.</figcaption>
</figure>  

In generale, è possibile trovare qualsiasi punto fra {{< mathjax >}}$$Q$${{< /mathjax >}} e {{< mathjax >}}$$P$${{< /mathjax >}}  cambiando il valore {{< mathjax >}}$$t$${{< /mathjax >}} fra 0 e 1 usando l'equazione generale:  

{{< mathjax >}}$$M = Q + t * (P - Q)$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Dati due punti  {{< mathjax >}}$$Q$${{< /mathjax >}} e {{< mathjax >}}$$P$${{< /mathjax >}}, qualsiasi punto {{< mathjax >}}$$M$${{< /mathjax >}} fra due punti viene calcolato usando l'equazione {{< mathjax >}}$$M = Q + t * (P - Q)$${{< /mathjax >}} dove t è un numero compreso fra 0 e 1.

{{< /call-out >}}

## 1.4 Equazione vettoriale di un piano

Un modo per definire un piano è usare un punto e un vettore perpendicolare al piano. Il riferimento di tale vettore è di solito la normale al piano. La normale punta nella direzione al di sopra del piano.  

Un esempio di come calcolare la normale a un piano è conoscere tre punti non lineari sul piano.   

La figura (16) mostra quanto segue:  

{{< mathjax >}}$$A$${{< /mathjax >}} = il primo punto sul piano.  
{{< mathjax >}}$$B$${{< /mathjax >}} = il secondo punto sul piano.  
{{< mathjax >}}$$C$${{< /mathjax >}} = il terzo punto sul piano.  

E:  

{{< mathjax >}}$$\mathbf{\vec a} $${{< /mathjax >}} = vettore posizione di un punto {{< mathjax >}}$$A$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} = vettore posizione di un punto {{< mathjax >}}$$B$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} = vettore posizione di un punto {{< mathjax >}}$$C$${{< /mathjax >}}  

Possiamo trovare il vettore normale {{< mathjax >}}$$\mathbf{\vec n}$${{< /mathjax >}} come segue:  

{{< mathjax >}}$$\mathbf{\vec n} = (\mathbf{\vec b} - \mathbf{\vec a}) × (\mathbf{\vec c} - \mathbf{\vec a})$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image160.png">
   <figcaption>Figura (18): Vettori e piani</figcaption>
</figure>  

Possiamo anche derivare l'equazione scalare del piano usando il prodotto scalare:  

{{< mathjax >}}$$\mathbf{\vec n} · (\mathbf{\vec b} - \mathbf{\vec a}) = 0$${{< /mathjax >}}  

Se:  

{{< mathjax >}}$$\mathbf{\vec n} = <a, b, c>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <x, y, z>$${{< /mathjax >}}  
{{< mathjax >}}$$ \mathbf{\vec a} = <x_0, y_0, z_0>$${{< /mathjax >}}  

Possiamo quindi ampliare quanto indicato precedentemente:  

{{< mathjax >}}$$<a, b, c> · <x-x_0, y-y_0, z-z_0 > = 0$${{< /mathjax >}}  

Risolvendo il prodotto scalare, otteniamo l'equazione scalare generale di un piano:  

{{< mathjax >}}$$a * (x - x_0) + b * (y - y_0) + c * (z - z_0) = 0$${{< /mathjax >}}  

## 1.5 Tutorial

Tutti i concetti spiegati in questo capitolo hanno applicazione diretta nella risoluzione dei comuni problemi di geometria riscontrati durante la modellazione. I seguenti tutorial spiegano passo a passo come usare i concetti appresi in Rhinoceros e Grasshopper (GH).

### 1.5.1 Direzione delle facce
Dato un punto e una superficie, come possiamo determinare se il punto è rivolto verso il lato anteriore o posteriore della superficie?  

**Input:**  

1. Una superficie.  
2. Un punto.  

<img src="/images/math-image161.png">  

**Parametri:**  

La direzione è definita dalla direzione alla normale della superficie. Saranno necessarie le seguenti informazioni:  

* La direzione della normale al punto della superficie più vicino al punto di input.  
* La direzione vettoriale dal punto più vicino al punto di input.  

Confronta le due direzioni indicate sopra, se vanno nella stessa direzione, il punto è rivolto verso il lato anteriore altrimenti è rivolto verso il lato posteriore.  

**Soluzione:**  

1\. Trova la posizione del punto più vicino sulla superficie relativo al punto di input usando il componente Pull. In questo modo, troveremo la posizione uv del punto più vicino, utile per valutare la superficie e trovarne le direzioni alla normale.  

<img src="/images/math-image162.png">  

2\. Possiamo ora usare il punto più vicino per disegnare un vettore che va verso il punto di input. Possiamo anche disegnare quanto segue:  

<img src="/images/math-image163.png">  

3\. Possiamo confrontare i due vettori usando il prodotto scalare. Se il risultato è positivo, il punto è di fronte alla superficie. Se il risultato è negativo, il punto si trova dietro la superficie.  

<img src="/images/math-image164.png">  

I passi sopra indicati possono anche essere eseguiti usando altri linguaggi di scripting. Usare il componente VB per Grasshopper:  

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

Usare il componente Grasshopper Python con RhinoScriptSyntax:

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



Usare il componente Grasshopper Python solo con RhinoCommon:

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



Usare il componente C# per Grasshopper:  

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

### 1.5.2 Esplodere un parallelepipedo  

Il seguente tutorial mostra come esplodere una polisuperficie. Il parallelepipedo esploso ha il seguente aspetto:   

<img src="/images/math-image15.jpg">  

**Input:**  

Identifica l'input che corrisponde a un parallelepipedo. Useremo il parametro Box in GH:

<img src="/images/math-image17.jpg">  

**Parametri:**  

* Considera tutti i parametri necessari per seguire questo tutorial.  
* Il centro dell'esplosione.  
* Le facce del parallelepipedo da esplodere.  
* La direzione verso cui si sposta ciascuna faccia.   


<img src="/images/math-image19.jpg">  

Una volta identificati i parametri, si tratta di metterli insieme per trovare una soluzione in base a passi logici che conducono alla risposta.

**Soluzione:**

1\. Trovare il centro del parallelepipedo usando il componente **Box Properties** in GH:

<img src="/images/math-image21.png">  

2\. Estrarre le facce del parallelepipedo con il componente **Deconstruct Brep**:

<img src="/images/math-image23.png">

3\. La parte più difficile riguarda la direzione verso cui spostiamo le facce. Anzitutto, occorre trovare il centro di ciascuna faccia, quindi definire la direzione dal centro del parallelepipedo verso il centro di ciascuna faccia, come segue:

<img src="/images/math-image25.png">

4\. Una volta eseguito lo script per tutti i parametri, possiamo usare il componente **Move** per spostare le facce nella direzione appropriata. Assicurati di impostare i vettori sull'ampiezza desiderata.

<img src="/images/math-image27.png">

I passi sopra indicati possono essere eseguiti usando scripting VB, C# o Python. Di seguito, la soluzione usando i tre linguaggi di scripting.

Usare il componente VB per Grasshopper:

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
Usare il componente Grasshopper Python con RhinoCommon:

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

Usare il componente C# per Grasshopper:

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

### 1.5.3 Sfere tangenti

Questo tutorial mostra come creare due sfere tangenti fra due punti di input.
Ecco come appare il risultato:

<img src="/images/math-image5.png">

**Input:**  
Due punti ({{< mathjax >}}$$A$${{< /mathjax >}} e {{< mathjax >}}$$B$${{< /mathjax >}}) nel sistema di coordinate 3D.

<img src="/images/math-image6.png">

Parametri:
Di seguito, un diagramma dei parametri necessari per risolvere il problema:
{{< mathjax >}}$$A$${{< /mathjax >}} punto tangente {{< mathjax >}}$$D$${{< /mathjax >}} fra le due sfere, nel parametro {{< mathjax >}}$$t$${{< /mathjax >}} (0-1) tra i punti {{< mathjax >}}$$A$${{< /mathjax >}} e {{< mathjax >}}$$B$${{< /mathjax >}}.

* Il centro della prima sfera o il punto medio {{< mathjax >}}$$C1$${{< /mathjax >}} fra {{< mathjax >}}$$A$${{< /mathjax >}} e {{< mathjax >}}$$D$${{< /mathjax >}}.  
* Il centro della seconda sfera o il punto medio {{< mathjax >}}$$C2$${{< /mathjax >}} fra {{< mathjax >}}$$D$${{< /mathjax >}} e {{< mathjax >}}$$B$${{< /mathjax >}}.  
* Il raggio della prima sfera {{< mathjax >}}$$(r1)$${{< /mathjax >}} o la distanza fra {{< mathjax >}}$$A$${{< /mathjax >}} e {{< mathjax >}}$$C1$${{< /mathjax >}}.  
* Il raggio della seconda sfera {{< mathjax >}}$$(r2)$${{< /mathjax >}} o la distanza fra {{< mathjax >}}$$D$${{< /mathjax >}} e {{< mathjax >}}$$C2$${{< /mathjax >}}.  

**Soluzione:**

1\. Utilizzare il componente **Expression** per definire il punto {{< mathjax >}}$$D$${{< /mathjax >}} fra {{< mathjax >}}$$A$${{< /mathjax >}} e {{< mathjax >}}$$B$${{< /mathjax >}} in un parametro {{< mathjax >}}$$t$${{< /mathjax >}}. L'espressione che useremo si basa sull'equazione vettoriale di una retta:  

{{< mathjax >}}$$D = A + t*(B-A)$${{< /mathjax >}}  

{{< mathjax >}}$$B-A$${{< /mathjax >}} : è il vettore che va da {{< mathjax >}}$$B$${{< /mathjax >}} a {{< mathjax >}}$$A  (\vec{BA}) usando l’operazione di sottrazione.  

$${{< /mathjax >}}t*(B-A){{< mathjax >}}$$ : dove $${{< /mathjax >}}t{{< mathjax >}}$$ è compreso fra 0 e 1 per ottenere una posizione sul vettore.  

$${{< /mathjax >}}A+t*(B-A){{< mathjax >}}$$ : ottiene un punto sul vettore A e B.  

<img src="/images/math-image8.png">

2\. Usa il componente Expression per definire inoltre i punti medi $${{< /mathjax >}}C1{{< mathjax >}}$$ e $${{< /mathjax >}}C2{{< mathjax >}}$$.  

<img src="/images/math-image9.png">  

3\. Il raggio della prima sfera $${{< /mathjax >}}(r1){{< mathjax >}}$$ e il raggio della seconda sfera $${{< /mathjax >}}(r2){{< mathjax >}}$$ possono essere calcolati usando il componente **Distance**.  

<img src="/images/math-image10.png">  

4\. Il passo finale implica la creazione della sfera da un piano di base e un raggio. Occorre assicurarsi che le origini siano collegate a $${{< /mathjax >}}C1{{< mathjax >}}$$ e $${{< /mathjax >}}C2{{< mathjax >}}$$ e il raggio da $${{< /mathjax >}}r1{{< mathjax >}}$$ e $${{< /mathjax >}}r2$$.  

<img src="/images/math-image54.png">  

**Usare il componente VB per Grasshopper:**  

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

Usare il componente Python:

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

Usare il componente C# per Grasshopper:

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

## Download dei file di esempio

Download del file [{{< awesome "fas fa-download">}} ](/files/math-samplesandtutorials.zip.zip) [math-samplesandtutorials.zip](/files/math-samplesandtutorials.zip) contenente tutti gli esempi di Grasshopper e i file del codice menzionati in questa guida.

## Passi successivi

Ora che conosciamo la matematica vettoriale, possiamo dare un'occhiata alla guida [Matrici e trasformazioni](/guides/general/essential-mathematics/matrices-transformations/) per ulteriori informazioni sugli oggetti da spostare, ruotare e scalare.

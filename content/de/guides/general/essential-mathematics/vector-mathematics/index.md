+++
aliases = ["/en/5/guides/general/essential-mathematics/vector-mathematics/", "/en/6/guides/general/essential-mathematics/vector-mathematics/", "/en/7/guides/general/essential-mathematics/vector-mathematics/", "/en/wip/guides/general/essential-mathematics/vector-mathematics/"]
authors = [ "rajaa" ]
categories = [ "Essential Mathematics" ]
category_page = "guides/general/essential-mathematics/"
description = "In Kapitel 1 geht es um Vektor-Mathematik einschließlich Vektordarstellung, Vektoroperation und Linien- und Ebenengleichungen."
keywords = [ "mathematics", "geometry", "grasshopper3d" ]
languages = "unset"
sdk = [ "General" ]
title = "1 Vektor-Mathematik"
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
Ein Vektor zeigt eine Menge an, etwa Geschwindigkeit oder Kraft, welche eine Richtung und Länge aufweist. Vektoren in 3D-Koordinatensystemen werden mit einem geordneten Satz drei reeller Zahlen dargestellt und sehen so aus: 

{{< mathjax >}}$$\mathbf{\vec v}  = <a_1, a_2, a_3>$${{< /mathjax >}}

{{< youtube NU34_aCoN3E >}}

## 1.1 Vektor-Darstellung

In diesem Dokument werden fettgedruckte Kleinbuchstaben mit einem Pfeil darüber zur Bezeichnung von Vektoren verwendet. Vektorenkomponenten werden auch in eckige Klammern gesetzt. Großbuchstaben bezeichnen Punkte. Punktkoordinaten erscheinen immer in Klammern.

Bei Verwendung eines Koordinatensystems und eines beliebigen Ankerpunktsatzes in diesem System können diese Vektoren mittels Liniensegmenten dargestellt oder sichtbar gemacht werden. Eine Pfeilspitze zeigt die Richtung des Vektors an.

Wenn wir zum Beispiel einen Vektor mit einer Richtung parallel zur x--Achse eines bestimmten 3D-Koordinatensystems und einer Länge von 5 Einheiten haben, können wir den Vektor wie folgt schreiben:

{{< mathjax >}}$$\mathbf{\vec v} = <5, 0, 0>$${{< /mathjax >}}  

Zur Darstellung dieses Vektors benötigen wir einen Ankerpunkt im Koordinatensystem. Zum Beispiel sind alle Pfeile in der folgenden Abbildung gleichwertige Darstellungen desselben Vektors, ungeachtet der Tatsache, dass sie an unterschiedlichen Standorten verankert sind.  

<figure>
   <img src="/images/math-image169.png">
   <figcaption>Abb. (1): Vektordarstellung im 3D-Koordinatensystem.</figcaption>
</figure>  

{{< call-out note "Note" >}}

Wenn ein 3D-Vektor {{< mathjax >}}$$\vec v = <a_1, a_2, a_3>$${{< /mathjax >}} vorhanden ist, sind alle Vektorkomponenten {{< mathjax >}}$$a_1$${{< /mathjax >}}, {{< mathjax >}}$$a_2$${{< /mathjax >}}, {{< mathjax >}}$$a_3$${{< /mathjax >}} reelle Zahlen. Auch sind alle Liniensegmente von einem Punkt {{< mathjax >}}$$A(x,y,z)$${{< /mathjax >}} hin zu Punkt {{< mathjax >}}$$B(x+a_1, y+a_2, z+a_3)$${{< /mathjax >}} gleichwertige Darstellungen von Vektor {{< mathjax >}}$$\vec v$${{< /mathjax >}}.

{{< /call-out >}}   

Wie definieren wir also die Endpunkte eines Liniensegments, das einen gegebenen Vektor repräsentiert?
Definieren wir zunächst einen Ankerpunkt (A) sodass:

{{< mathjax >}}$$A = (1, 2, 3)$${{< /mathjax >}}

Und einen Vektor:

{{< mathjax >}}$$\mathbf{\vec v} = <5, 6, 7>$${{< /mathjax >}}

Der Endpunkt {{< mathjax >}}$$(B)$${{< /mathjax >}} des Vektors wird durch Hinzufügen der entsprechenden Komponenten von Ankerpunkt und Vektor {{< mathjax >}}$$\vec v$${{< /mathjax >}} berechnet:  

{{< mathjax >}}$$B = A + \mathbf{\vec v}$${{< /mathjax >}}  
{{< mathjax >}}$$B = (1+5, 2+6, 3+7) $${{< /mathjax >}}  
{{< mathjax >}}$$B = (6, 8, 10)$${{< /mathjax >}}  


<figure>
   <img src="/images/math-image172.png">
   <figcaption>Abb. (2): Die Beziehung zwischen einem Vektor, dem Vektor-Ankerpunkt und dem mit dem Standort des Vektor-Endpunkts übereinstimmenden Punkt.</figcaption>
</figure>  

{{< youtube ELQ8NgENhJY >}}
{{< youtube INtNgczxyWg >}}

### Positionsvektor

Eine spezielle Vektordarstellung verwendet den {{< mathjax >}}$$\text{Ursprungspunkt} (0,0,0)$${{< /mathjax >}} als Vektorankerpunkt.
Der Standortvektor {{< mathjax >}}v {{< /mathjax >}}= <a_1,a_2,a_3> wird mit einem Liniensegment zwischen zwei Punkten, nämlich Ursprung und B dargestellt, womit:  

{{< mathjax >}}$$\text{Origin point} = (0,0,0)$${{< /mathjax >}}  
{{< mathjax >}}$$B = (a_1,a_2,a_3)$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image171.png">
   <figcaption>Abb. (3): Positionsvektor. Die Endpunkt-Koordinaten gleichen die entsprechenden Vektorkomponenten einander an.</figcaption>
</figure>  

{{< call-out note "Note" >}}

Ein *Positionsvektor* für einen vorhandenen Vektor {{< mathjax >}}$$\vec v= < a_1,a_2,a_3 >$${{< /mathjax >}} ist eine spezielle Liniensegmentdarstellung vom Ursprungspunkt {{< mathjax >}}$$(0,0,0)$${{< /mathjax >}} zu Punkt {{< mathjax >}}$$(a_1, a_2, a_3)$${{< /mathjax >}}.

{{< /call-out >}}

{{< youtube 8BNyMC4EBcw >}}

{{< youtube Ft2edI4g1qY >}}

### Vektoren im Vergleich zu Punkten  

Vektoren und Punkte dürfen nicht verwechselt werden. Es handelt sich dabei um sehr verschiedene Konzepte. Wie bereits erwähnt, stellen Vektoren eine Menge mit einer Richtung und Länge dar, während Punkte einen Standort anzeigen. Norden als Richtung ist zum Beispiel ein Vektor, während der Nordpol ein Standort (Punkt) ist.
Angenommen, wir haben einen Vektor und einen Punkt mit den gleichen Komponenten, etwa:  

{{< mathjax >}}$$\mathbf{\vec v} = <3,1,0>$${{< /mathjax >}}  
{{< mathjax >}}$$P = (3,1,0)$${{< /mathjax >}}  

Dann können wir Vektor und Punkt folgendermaßen zeichnen:  

<figure>
   <img src="/images/math-image174.png">
   <figcaption>Abb. (4): Ein Vektor definiert eine Richtung und Länge. Ein Punkt definiert einen Standort.</figcaption>
</figure>  

{{< youtube RRrTz_QO_rA >}}

### Vektorlänge  

Wie schon erwähnt, haben Vektoren Länge. Wir verwenden {{< mathjax >}}$$\vert a \vert$${{< /mathjax >}} um die Länge eines gegebenen Vektors {{< mathjax >}}$$ a $${{< /mathjax >}} zu bezeichnen. Zum Beispiel:  

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = 5$${{< /mathjax >}}  

Die Länge eines Vektors {{< mathjax >}}$$\mathbf{\vec a} <a_1,a_2,a_3>$${{< /mathjax >}} wird im Allgemeinen wie folgt berechnet:

{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{(a_1)^2 + (a_2)^2 + (a_3)^2} $${{< /mathjax >}}

<figure>
   <img src="/images/math-image173.png">
   <figcaption>Abb. (5): Vektorlänge.
</figure>  

### Einheitsvektor

Ein Einheitsvektor ist ein Vektor, dessen Länge einer Einheit entspricht. Einheitsvektoren werden gewöhnlich dazu verwendet, die Richtungen von Vektoren zu vergleichen.

{{< call-out note "Note" >}}

Ein Einheitsvektor ist ein Vektor, dessen Länge mit einer Einheit gleich ist.

{{< /call-out >}}

Um einen Einheitsvektor zu berechnen, müssen wir die Länge eines gegebenen Vektors herausfinden und dann die Vektorkomponenten durch die Länge teilen. Zum Beispiel:

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec a} \vert  = 5 \text{ Einheitslänge}$${{< /mathjax >}}  

Wenn {{< mathjax >}}$$\mathbf{\vec b} = \text{Einheitsvektor}$${{< /mathjax >}} von {{< mathjax >}}$$a$${{< /mathjax >}}, dann:  
&nbsp;&nbsp;     {{< mathjax >}}$$\mathbf{\vec b} = <4/5, 3/5, 0/5>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\mathbf{\vec b} = <0.8, 0.6, 0>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{0.8^2 + 0.6^2 + 0^2}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{0.64 + 0.36 + 0}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{(1)} = 1 \text{ Einheitslänge}$${{< /mathjax >}}  

Generell:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  

Der Einheitsvektor von {{< mathjax >}}$$\mathbf{\vec a} = <a_1/\vert \mathbf{\vec a} \vert , a_2/\vert \mathbf{\vec a} \vert , a_3/\vert \mathbf{\vec a} \vert >$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image176.png">
   <figcaption>Abb. (6): Einheitsvektor ist gleich wie die Länge einer Einheit des Vektors.</figcaption>
</figure>  

{{< youtube yVSigpl3EUo >}}

## 1.2 Vektoroperationen

{{< youtube uInxocphhxI >}}

### Skalare Vektoroperation

Skalare Vektoroperation beinhaltet das Multiplizieren eines Vektors mit einer Zahl. Zum Beispiel:  

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$2* \mathbf{\vec a} = <2*4, 2*3, 2*0> $${{< /mathjax >}}  
{{< mathjax >}}$$2*\mathbf{\vec a} = <8, 6, 0>$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image175.png">
   <figcaption>Abb. (7): Skalare Vektoroperation</figcaption>
</figure>  

Im Allgemeinen, ein gegebener Vektor {{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}, und eine reelle Zahl {{< mathjax >}}$$t$${{< /mathjax >}}   

{{< mathjax >}}$$t*\mathbf{\vec a} = < t* a_1, t* a_2, t* a_3 >$${{< /mathjax >}}  

{{< youtube S59M8BnDYAQ >}}

### Vektoraddition

Für die Vektoraddition sind zwei Vektoren nötig, und das Ergebnis ist ein dritter Vektor. Vektoren addieren wir, indem wir ihre Komponenten addieren.

{{< call-out note "Note" >}}

Vektoren werden durch Addition ihrer Komponenten addiert.

{{< /call-out >}}

Wenn wir zum Beispiel zwei Vektoren haben:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 0> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <4, 1, 3> $${{< /mathjax >}}   
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <1+4, 2+1, 0+3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <5, 3, 3>$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image179.png">
   <figcaption>Abb. (8): Vektoraddition.</figcaption>
</figure>  

Im Allgemeinen wird die Vektoraddition der beiden Vektoren a und b wie folgt berechnet:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <a_1+b_1, a_2+b_2, a_3+b_3>$${{< /mathjax >}}  

Vektoraddition eignet sich gut, die mittlere Richtung von zwei oder mehr Vektoren zu ermitteln. In diesem Fall werden gewöhnlich Vektoren der gleichen Länge verwendet. Dieses Beispiel verdeutlicht den Unterschied zwischen der Verwendung von Vektoren der gleichen Länge und Vektoren unterschiedlicher Länge in der resultierenden Vektoraddition:  

<figure>
   <img src="/images/math-image177.png">
   <figcaption>Abb. (9): Addition von Vektoren unterschiedlicher Länge (links). Addition von Vektoren der gleichen Länge (rechts) um die mittlere Richtung zu erhalten.</figcaption>
</figure>  

Dass Eingabevektoren die gleiche Länge haben, ist eher unwahrscheinlich. Um die mittlere Richtung zu erhalten, müssen Sie den Einheitsvektor von Eingabevektoren verwenden. Wie schon erwähnt, ist der Einheitsvektor ein Vektor, dessen Länge gleich 1 ist.

{{< youtube VTVk3t3WeAY >}}

### Vektorsubtraktion

Die Vektorsubtraktion geschieht anhand zweier Vektoren und ergibt einen dritten Vektor. Zwei Vektoren werden durch Subtraktion der jeweiligen Komponenten subtrahiert. Wenn wir zum Beispiel zwei Vektoren {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} und {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} haben und {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} von {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} subtrahieren, dann:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 0> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <4, 1, 4> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <1-4, 2-1, 0-4>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <-3, 1, -4> = \mathbf{\mathbf{\vec b}a}$${{< /mathjax >}}

Wenn wir {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} von {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} subtrahieren, erhalten wir ein unterschiedliches Ergebnis:  

{{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a} = <4-1, 1-2, 4-0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a} = <3, -1, 4> = \mathbf{\mathbf{\vec a}b}$${{< /mathjax >}}  

Beachten Sie, dass der Vektor {{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a}$${{< /mathjax >}} die gleiche Länge hat wie der Vektor {{< mathjax >}}$$\mathbf{\vec a} - \mathbf{\vec b}$${{< /mathjax >}}, jedoch in entgegengesetzter Richtung.  

<figure>
   <img src="/images/math-image178.png">
   <figcaption>Abb. (10): Vektorsubtraktion.</figcaption>
</figure>  

Im Allgemeinen, wenn wir zwei Vektoren {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} und {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} haben, dann ist {{< mathjax >}}$$\mathbf{\vec a} - \mathbf{\vec b}$${{< /mathjax >}} ein Vektor, der wie folgt berechnet wird:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <a_1 - b_1, a_2 - b_2, a_3 - b_3> = \mathbf{\mathbf{\vec b}a}$${{< /mathjax >}}  

Vektorsubtraktion wird gewöhnlich zum Suchen von Vektoren zwischen Punkten verwendet. Wenn wir also einen Vektor suchen, der vom Endpunkt des Positionsvektors {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} zum Endpunkt des Positionsvektors {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} reicht, dann verwenden wir Vektorsubtraktion {{< mathjax >}}$$(\mathbf{\vec a}-\mathbf{\vec b})$${{< /mathjax >}} wie in Abb. (11) zu sehen.  

<figure>
   <img src="/images/math-image180.png">
   <figcaption>Abb. (11): Verwenden Sie Vektorsubtraktion, um einen Vektor zwischen zwei Punkten zu finden. </figcaption>
</figure> 

{{< youtube RQK8pCIWKNY >}} 

### Vektoreigenschaften

Vektoren haben bis zu acht Eigenschaften. Wenn a, b und c Vektoren und s und t Zahlen sind, dann folgt:  

{{< mathjax >}}$$\mathbf{\vec a} + \mathbf{\vec b} = \mathbf{\vec b} + \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + 0 = a$${{< /mathjax >}}  
{{< mathjax >}}$$s * (\mathbf{\vec a} + \mathbf{\vec b}) = s * a + s * \mathbf{\vec b}$${{< /mathjax >}}  
{{< mathjax >}}$$s * t * (\mathbf{\vec a}) = s * (t * \mathbf{\vec a})$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + (\mathbf{\vec b} + \mathbf{\vec c}) = (\mathbf{\vec a} + \mathbf{\vec b}) + \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + (-\mathbf{\vec a}) = 0$${{< /mathjax >}}  
{{< mathjax >}}$$(s + t) * \mathbf{\vec a} = s * \mathbf{\vec a} + t * \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$1 * \mathbf{\vec a} = \mathbf{\vec a}$${{< /mathjax >}}  

### Vektorpunktprodukt

Für das Punktprodukt sind zwei Vektoren nötig, und das Ergebnis ist eine Zahl.
Angenommen, wir haben die beiden Vektoren a und b, so dass:

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 3> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <5, 6, 7>$${{< /mathjax >}}  

Dann ist das Punktprodukt die Summe der Multiplikation der Komponenten wie folgt:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = 1 * 5 + 2 * 6 + 3 * 7$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = 38$${{< /mathjax >}}  

Im Allgemeinen, wenn die beiden Vektoren a und b vorhanden sind:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = a_1 * b_1 + a_2 * b_2 + a_3 * b_3$${{< /mathjax >}}  

Wir erhalten stets eine positive Zahl für das Punktprodukt zwischen zwei Vektoren, wenn sie in derselben allgemeinen Richtung verlaufen. Ein negatives Punktprodukt zwischen zwei Vektoren bedeutet, dass die beiden Vektoren in der entgegengesetzten allgemeinen Richtung verlaufen.

<figure>
   <img src="/images/math-image181.png">
   <figcaption>Abb. (12): Wenn die beiden Vektoren in der gleichen Richtung verlaufen (links), ist das Ergebnis ein positives Punktprodukt. Wenn die beiden Vektoren in entgegengesetzter Richtung verlaufen (rechts), ist das Ergebnis ein negatives Punktprodukt. </figcaption>
</figure>  

Beim Berechnen des Punktprodukts von zwei Einheitsvektoren, liegt das Ergebnis immer zwischen 1 und +1. Zum Beispiel:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <0,6, 0,8, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = (1 * 0.6, 0 * 0.8, 0 * 0) = 0.6$${{< /mathjax >}}  

Außerdem ist das Punktprodukt eines Vektors mit sich selbst gleich wie die Länge dieses Vektors hoch zwei. Zum Beispiel:  

{{< mathjax >}}$$\mathbf{\vec a} = <0, 3, 4>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = 0 * 0 + 3 * 3 + 4 * 4 $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = 25$${{< /mathjax >}}  

Berechnung der Länge von Vektor {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} zum Quadrat:  

{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = 5$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert 2 = 25$${{< /mathjax >}}  

### Vektorpunktprodukt, Längen und Winkel

Es besteht eine Beziehung zwischen dem Punktprodukt zweier Vektoren und dem Winkel zwischen beiden.  

{{< call-out note "Note" >}}

Das Punktprodukt zweier von null verschiedenen Einheitsvektoren ist gleich wie der Kosinus des Winkels dazwischen.

{{< /call-out >}}

Generell:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = \vert \mathbf{\vec a} \vert * \vert \mathbf{\vec b} \vert * cos(ө)$${{< /mathjax >}} , oder  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} / (\vert \mathbf{\vec a} \vert * \vert \mathbf{\vec b} \vert) = cos(ө)$${{< /mathjax >}}

Wobei:  

{{< mathjax >}}$$ө$${{< /mathjax >}} der zwischen den Vektoren enthaltene Winkel ist.  

Wenn die Vektoren a und b Einheitsvektoren sind, können wir einfach sagen:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = cos(ө)$${{< /mathjax >}}  

Und da der Kosinus eines Winkels von 90 Grad gleich 0 ist, können wir sagen:  

{{< call-out note "Note" >}}

Die Vektoren {{< mathjax >}}$$\vec a$${{< /mathjax >}} und {{< mathjax >}}$$\vec b$${{< /mathjax >}} sind orthogonal wenn, und nur wenn, {{< mathjax >}}$$\vec{a} \cdot  \vec{b} = 0$${{< /mathjax >}}.

{{< /call-out >}}

Wenn wir beispielsweise das Punktprodukt der beiden orthogonalen Vektoren, der Welt xAchse und der yAchse berechnen, wird das Ergebnis gleich null sein.  

{{< mathjax >}}$$\mathbf{\vec x} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec y} = <0, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec x} · \mathbf{\vec y} = (1 * 0) + (0 * 1) + (0 * 0)$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec x} · \mathbf{\vec y} = 0$${{< /mathjax >}}  

Es besteht auch eine Beziehung zwischen dem Punktprodukt und der Projektionslänge von einem Vektor auf einen anderen. Zum Beispiel:  

{{< mathjax >}}$$\mathbf{\vec a} = <5, 2, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <9, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$Einheit(\mathbf{\vec b}) = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · Einheit(\mathbf{\vec b}) = (5 * 1) + (2 * 0) + (0 * 0) $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · Einheit(\mathbf{\vec b}) = 2 (\text{was gleich ist wie die Projektionslänge von mathbf{\vec a} auf mathbf{\vec b}})$${{< /mathjax >}}

<figure>
   <img src="/images/math-image182.png">
   <figcaption>Abb. (13): Das Punktprodukt ist gleichwertig mit der Projektionslänge von einem Vektor auf einen von null verschiedenen Einheitsvektor. </figcaption>
</figure>  

Generell können wir mit einem gegebenen Vektor a und einem von null verschiedenen Vektor b die Projektionslänge pL von Vektor a auf Vektor b unter Verwendung des Punktprodukts berechnen.  

{{< mathjax >}}$$pL = \vert \mathbf{\vec a} \vert * cos(ө) $${{< /mathjax >}}  
{{< mathjax >}}$$pL = \mathbf{\vec a} · Einheit(\mathbf{\vec b})$${{< /mathjax >}} 

 {{< youtube ZsM2RQbVDf4 >}}

### Eigenschaften des Punktprodukts

Wenn {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} und {{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} Vektoren sind und s eine Zahl ist, dann:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = \vert  \mathbf{\vec a} \vert ^2$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b} + \mathbf{\vec c}) = \mathbf{\vec a} · \mathbf{\vec b} + \mathbf{\vec a} · \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$0 · \mathbf{\vec a} = 0$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = \mathbf{\vec b} · \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$(s * \mathbf{\vec a}) · \mathbf{\vec b} = s * (\mathbf{\vec a} · \mathbf{\vec b}) = \mathbf{\vec a} · (s * \mathbf{\vec b})$${{< /mathjax >}}  

### Vektor-Kreuzprodukt

Das Kreuzprodukt benötigt zwei Vektoren und ergibt einen dritten Vektor, der orthogonal zu beiden ist.

<figure>
   <img src="/images/math-image183.png">
   <figcaption>Abb. (14): Berechnung des Kreuzprodukts von zwei Vektoren. </figcaption>
</figure>  

Wenn Sie zum Beispiel zwei auf der Welt-xy-Ebene liegende Vektoren haben, dann ist deren Kreuzprodukt ein Vektor, der rechtwinklig zur xy-Ebene liegt und entweder in positiver oder negativer Welt-z-Achsenrichtung verläuft. Zum Beispiel:  

{{< mathjax >}}$$\mathbf{\vec a} = <3, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <1, 2, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = < (1 * 0 – 0 * 2), (0 * 1 - 3 * 0), (3 * 2 - 1 * 1) > $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <0, 0, 5>$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Der Vektor {{< mathjax >}}$$\vec a \times \vec b$${{< /mathjax >}} ist orthogonal sowohl zu {{< mathjax >}}$$\vec a$${{< /mathjax >}} als auch {{< mathjax >}}$$\vec b$${{< /mathjax >}}.

{{< /call-out >}}

Sie werden wahrscheinlich nie von Hand ein Kreuzprodukt von zwei Vektoren berechnen müssen. Wenn Sie die Vorgehensweise trotzdem interessiert, lesen Sie weiter; ansonsten können Sie diesen Abschnitt einfach überspringen. Das Kreuzprodukt {{< mathjax >}}$$a × b$${{< /mathjax >}}  wird durch die Verwendung von Determinanten bestimmt. Was folgt ist eine einfache Veranschaulichung, wie eine Determinante unter Verwendung der Standard-Basisvektoren berechnet wird:  

{{< mathjax >}}$$ \color {red}{i} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$ \color {blue}{j} = <0,1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$ \color {green}{k} = <0, 0, 1>$${{< /mathjax >}}  

<img src="/images/math-image184.png">

Das Kreuzprodukt der beiden Vektoren {{< mathjax >}}$$\mathbf{\vec a} = <a1, a2, a3>$${{< /mathjax >}} und {{< mathjax >}}$$\mathbf{\vec b} = <b1, b2, b3>$${{< /mathjax >}} wird wie folgt unter Verwendung des obigen Diagramms berechnet:  

{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = \color {red}{i (a_2 * b_3)} + \color {blue}{ j (a_3 * b_1)} + \color {green}{k(a_1 * b_2)} - \color {green}{k (a_2 * b_1)} - \color {red}{i (a_3 * b_2)} -\color {blue}{ j (a_1 * b_3)}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = \color {red}{i (a_2 * b_3 - a_3 * b_2)} + \color {blue}{j (a_3 * b_1 - a_1 * b_3)} +\color {green}{k (a_1 * b_2 - a_2 * b_1)}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <\color {red}{a_2 * b_3 – a_3 * b_2},  \color {blue}{a_3 * b_1 - a_1 * b_3},  \color {green}{a_1 * b_2 - a_2 * b_1} >$${{< /mathjax >}}  

{{< youtube I5WkhSo4p6o >}}

### Kreuzprodukte und Winkel zwischen Vektoren

Zwischen dem Winkel zwischen zwei Vektoren und der Länge ihres Kreuzproduktvektors besteht eine Beziehung. Je kleiner der Winkel (kleinerer Sinus), desto kürzer ist der Vektor des Kreuzprodukts. Die Reihenfolge der Operanden ist im Kreuzprodukt eines Vektors von Bedeutung. Zum Beispiel:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <0, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <0, 0, 1>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} × \mathbf{\vec a} = <0, 0, -1>$${{< /mathjax >}}  


<figure>
   <img src="/images/math-image185.png">
   <figcaption>Abb. (15): Beziehung zwischen dem Winkel zwischen zwei Vektoren und der Länge ihres Kreuzproduktvektors.</figcaption>
</figure>  

In Rhinos rechtshändig ausgelegtem System wird die Richtung von {{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b}$${{< /mathjax >}} durch die Dreifingerregel bestimmt ({{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} = Zeigefinger, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} = Mittelfinger und {{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b}$${{< /mathjax >}} = Daumen).  

<img src="/images/math-image186.png" width="375px">  

Generell, für ein beliebiges Paar von 3D-Vektoren {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} und {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}:  

{{< mathjax >}}$$$vert \mathbf{\vec a} × \mathbf{\vec b} \vert = \vert \mathbf{\vec a} \vert \vert \mathbf{\vec b} \vert sin(ө)$${{< /mathjax >}}  

Wobei:   

{{< mathjax >}}$$ө$${{< /mathjax >}} der zwischen den Positionsvektoren von {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} und {{< mathjax >}}$$\mathbf{\vec b}$$ enthaltene Winkel ist.{{< /mathjax >}}  

Wenn a und b Einheitsvektoren sind, können wir ebenso gut sagen, dass die Länge ihres Kreuzprodukts gleichwertig mit dem Sinus des Winkels zwischen ihnen ist. Anders ausgedrückt:  

{{< mathjax >}}$$\vert \mathbf{\vec a} × \mathbf{\vec b} \vert = sin(ө)$${{< /mathjax >}}  

Das Kreuzprodukt zwischen zwei Vektoren hilft uns dabei zu bestimmen, ob zwei Vektoren parallel sind. Der Grund dafür ist, dass das Ergebnis immer ein Nullvektor ist.  

{{< call-out note "Note" >}}

Die Vektoren {{< mathjax >}}$$\vec a$${{< /mathjax >}} und {{< mathjax >}}$$\vec b$${{< /mathjax >}} sind dann und nur dann parallel, wenn {{< mathjax >}}$$a \times b = 0$${{< /mathjax >}}.

{{< /call-out >}}

### Eigenschaften des Kreuzprodukts

Wenn {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}, and {{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} Vektoren sind und {{< mathjax >}}$$s$${{< /mathjax >}} eine Zahl, dann:  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = -\mathbf{\vec b} × \mathbf{\vec a}$${{< /mathjax >}}   
{{< mathjax >}}$$(s * \mathbf{\vec a}) × \mathbf{\vec b} = s * (\mathbf{\vec a} × \mathbf{\vec b}) = \mathbf{\vec a} × (s * \mathbf{\vec b})$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × (\mathbf{\vec b} + \mathbf{\vec c}) = \mathbf{\vec a} × \mathbf{\vec b} + \mathbf{\vec a} × \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$(\mathbf{\vec a} + \mathbf{\vec b}) × \mathbf{\vec c} = \mathbf{\vec a} × \mathbf{\vec c} + \mathbf{\vec b} × \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b} × \mathbf{\vec c}) = (\mathbf{\vec a} × \mathbf{\vec b}) · \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × (\mathbf{\vec b} × \mathbf{\vec c}) = (\mathbf{\vec a} · \mathbf{\vec c}) * \mathbf{\vec b} – (\mathbf{\vec a} · \mathbf{\vec b}) * \mathbf{\vec c}$${{< /mathjax >}}  

## 1.3 Lineare Vektorgleichungen

Die lineare Vektorgleichung wird in Anwendungen für die 3D-Modellierung und für Computergrafiken verwendet.

<figure>
   <img src="/images/math-image187.png">
   <figcaption>Abb. (16): Vektorgleichung einer Linie.</figcaption>
</figure>  

Wenn wir etwa die Richtung einer Linie und einen Punkt auf dieser Linie kennen, dann können wir unter Verwendung von Vektoren auch jeden anderen Punkt auf dieser Linie finden, wie im folgenden Beispiel:

{{< mathjax >}}$$\overline{L} = Linie$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec v} = <a, b, c>$${{< /mathjax >}} Linienrichtung-Einheitsvektor  
{{< mathjax >}}$$Q = (x_0, y_0, z_0)$${{< /mathjax >}} Linienstandortpunkt  
{{< mathjax >}}$$P = (x, y, z)$${{< /mathjax >}} Jeder beliebiger Punkt auf der Linie  

Wir wissen, dass:  

{{< mathjax >}}$$\mathbf{\vec a} = t *\mathbf{\vec v}$${{< /mathjax >}}   (2)  
{{< mathjax >}}$$\mathbf{\vec p} = \mathbf{\vec q} + \mathbf{\vec a}$${{< /mathjax >}}   (1)  

Von 1 und 2:  

{{< mathjax >}}$$\mathbf{\vec p} = \mathbf{\vec q} + t * \mathbf{\vec v}$${{< /mathjax >}}  (3)   

Allerdings können wir (3) auch wie folgt schreiben:  

{{< mathjax >}}$$<x, y, z> = <x_0, y_0, z_0> + <t * a, t * b, t * c>$${{< /mathjax >}}  
{{< mathjax >}}$$<x, y, z> = <x_0 + t * a, y_0 + t * b, z_0 + t * c>$${{< /mathjax >}}  

Daher:  

{{< mathjax >}}$$x = x_0 + t * a$${{< /mathjax >}}  
{{< mathjax >}}$$y = y_0 + t * b$${{< /mathjax >}}  
{{< mathjax >}}$$z = z_0 + t * c$${{< /mathjax >}}  

Was auf das Gleiche herauskommt wie:  

{{< mathjax >}}$$P = Q + t * \mathbf{\vec v}$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Wenn ein Punkt {{< mathjax >}}$$Q$${{< /mathjax >}} und eine Richtung {{< mathjax >}}$$\vec v$${{< /mathjax >}} auf einer Linie vorhanden sind, kann jeder Punkt {{< mathjax >}}$$P$${{< /mathjax >}} auf dieser Linie berechnet werden, und zwar mittels der Vektorgleichung einer Linie {{< mathjax >}}$$P = Q + t * \vec v$${{< /mathjax >}}, wobei {{< mathjax >}}$$t$${{< /mathjax >}} eine Zahl ist.  

{{< /call-out >}}

Ein ebenfalls häufiges Beispiel ist das Auffinden des Mittelpunkts zwischen zwei Punkten. Im Folgenden ist zu sehen, wie der Mittelpunkt unter Verwendung der Vektorgleichung einer Linie zu finden ist:  

{{< mathjax >}}$$\mathbf{\vec q}$${{< /mathjax >}} ist der Standortvektor für Punkt {{< mathjax >}}$$Q$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec p}$${{< /mathjax >}} ist der Standortvektor für Punkt {{< mathjax >}}$$P$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} ist der {{< mathjax >}}$$Q \rightarrow P$$ verlaufende Vektor{{< /mathjax >}}  

Anhand der Vektorsubtraktion wissen wir, dass:  

{{< mathjax >}}$$\mathbf{\vec a} = \mathbf{\vec p} - \mathbf{\vec q}$${{< /mathjax >}}  

Anhand der linearen Gleichung wissen wir, dass:  

{{< mathjax >}}$$M = Q + t * \mathbf{\vec a}$${{< /mathjax >}}  

Und da wir den Mittelpunkt finden müssen, folgt:  

{{< mathjax >}}$$t = 0.5$${{< /mathjax >}}  

Daher können wir sagen:  

{{< mathjax >}}$$M = Q + 0.5 * \mathbf{\vec a}$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image159.png">
   <figcaption>Abb. (17): Suchen Sie den Mittelpunkt zwischen zwei Eingabepunkten.</figcaption>
</figure>  

Im Allgemeinen können Sie jeden beliebigen Punkt zwischen {{< mathjax >}}$$Q$${{< /mathjax >}} und {{< mathjax >}}$$P$${{< /mathjax >}} finden, und zwar indem Sie den Wert {{< mathjax >}}$$t$${{< /mathjax >}} zwischen 0 und 1 ändern, bei Anwendung der allgemeinen Gleichung:  

{{< mathjax >}}$$M = Q + t * (P - Q)$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Wenn zwei Punkte {{< mathjax >}}$$Q$${{< /mathjax >}} und {{< mathjax >}}$$P$${{< /mathjax >}} vorhanden sind, wird jeder Punkt {{< mathjax >}}$$M$${{< /mathjax >}} zwischen den beiden Punkten mittels der Gleichung {{< mathjax >}}$$M = Q + t * (P - Q)$${{< /mathjax >}} berechnet, wobei t eine Zahl zwischen 0 und 1 ist.

{{< /call-out >}}

## 1.4 Vektorgleichung einer Ebene

Eine Möglichkeit zum Bestimmen einer Ebene besteht, wenn Sie einen Punkt haben und einen Vektor, der sich rechtwinklig zur Ebene befindet. Dieser Vektor wird üblicherweise als normal zur Ebene bezeichnet. Die normalen Punkte in der Richtung über der Ebene.  

Eine Ebenennormale ist beispielsweise auch zu berechnen, wenn uns drei nicht-lineare Punkte auf der Ebene bekannt sind.   

In Abb. (16) haben wir:  

{{< mathjax >}}$$A$${{< /mathjax >}} = der erste Punkt auf der Ebene  
{{< mathjax >}}$$B$${{< /mathjax >}} = der zweite Punkt auf der Ebene  
{{< mathjax >}}$$C$${{< /mathjax >}} = der dritte Punkt auf der Ebene  

Sowie:  

{{< mathjax >}}$$\mathbf{\vec a} $${{< /mathjax >}} = ein Positionsvektor des Punktes {{< mathjax >}}$$A$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} = ein Positionsvektor des Punktes {{< mathjax >}}$$B$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} = ein Positionsvektor des Punktes {{< mathjax >}}$$C$${{< /mathjax >}}  

Der Normalenvektor {{< mathjax >}}$$\mathbf{\vec n}$${{< /mathjax >}} ist folgendermaßen zu finden:  

{{< mathjax >}}$$\mathbf{\vec n} = (\mathbf{\vec b} - \mathbf{\vec a}) × (\mathbf{\vec c} - \mathbf{\vec a})$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image160.png">
   <figcaption>Abb. (18): Vektoren und Ebenen</figcaption>
</figure>  

Wir können die skalare Gleichung der Ebene auch unter Verwendung des Vektorpunktprodukts ableiten:  

{{< mathjax >}}$$\mathbf{\vec n} · (\mathbf{\vec b} - \mathbf{\vec a}) = 0$${{< /mathjax >}}  

Wenn:  

{{< mathjax >}}$$\mathbf{\vec n} = <a, b, c>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <x, y, z>$${{< /mathjax >}}  
{{< mathjax >}}$$ \mathbf{\vec a} = <x_0, y_0, z_0>$${{< /mathjax >}}  

Das Obenstehende können wir dann erweitern:  

{{< mathjax >}}$$<a, b, c> · <x-x_0, y-y_0, z-z_0 > = 0$${{< /mathjax >}}  

Die Auflösung des Punktprodukts erbringt die allgemeine skalare Gleichung einer Ebene:  

{{< mathjax >}}$$a * (x - x_0) + b * (y - y_0) + c * (z - z_0) = 0$${{< /mathjax >}}  

## 1.5 Tutorials

Alle in diesem Kapitel besprochenen Konzepte können direkt zur Lösung während des Modellierens häufig auftauchender Probleme angewendet werden. Die Folgenden sind Schritt-für-Schritt-Tutorials, welche die in diesem Kapitel erlernten Konzepte unter Verwendung von Rhinoceros und Grasshopper (GH) anwenden.

### 1.5.1 Seitenrichtung
Angenommen, wir haben einen Punkt und eine Fläche; wie können wir dann bestimmen, ob der Punkt der Vorder- oder Rückseite dieser Fläche zugewandt ist?  

**Eingabe:**  

1. eine Fläche  
2. ein Punkt  

<img src="/images/math-image161.png">  

**Parameter:**  

Die Seitenrichtung ist durch die Normalenrichtung der Fläche gegeben. Wir benötigen die folgenden Informationen:  

* Die Normalenrichtung der Fläche auf einem Flächenstandort möglichst nahe am Eingabepunkt.  
* Eine Vektorrichtung vom nächstmöglichen Punkt zum Eingabepunkt.  

Vergleichen Sie beiden oben genannten Richtungen: wenn die Richtung gleich ist, ist der Punkt der Vorderseite zugewandt, und andernfalls der Rückseite.  

**Lösung:**  

1\. Suchen Sie auf der Fläche den Punktstandort, der am nächsten zum Eingabepunkt liegt, und zwar mittels der Komponente Pull. Daraus ergibt sich für uns der uv-Standort des nächstgelegenen Punkts, den wir dann zur Auswertung der Fläche und zum Finden ihrer Normalenrichtung verwenden können.  

<img src="/images/math-image162.png">  

2\. Jetzt können wir den nächstgelegenen Punkt verwenden, um einen zum Eingabepunkt verlaufenden Vektor zu zeichnen. Wir können auch folgendes zeichnen:  

<img src="/images/math-image163.png">  

3\. Wir können die beiden Vektoren unter Verwendung des Punktprodukts vergleichen. Fällt das Ergebnis positiv aus, befindet sich der Punkt vor der Fläche. Fällt es negativ aus, befindet sich der Punkt hinter der Fläche.  

<img src="/images/math-image164.png">  

Der obige Schritt kann auch unter Verwendung anderer Scripting-Sprachen gelöst werden. Unter Verwendung der Grasshopper-VB-Komponente:  

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

Unter Verwendung der Grasshopper-Python-Komponente mit RhinoScriptSyntax:

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



Unter Verwendung der Grasshopper-Python-Komponente nur mit RhinoCommon:

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



Unter Verwendung der Grasshopper-C#-Komponente:  

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

### 1.5.2 Zerlegter Quader  

Im folgenden Tutorial wird das Zerlegen eines Flächenverbandes gezeigt. So sieht der zerlegte Quader am Ende aus:   

<img src="/images/math-image15.jpg">  

**Eingabe:**  

Identifizierung der Eingabe, die ein Quader ist. Wir verwenden den Quader-Parameter in GH:

<img src="/images/math-image17.jpg">  

**Parameter:**  

* Bedenken Sie alle Parameter, die zur Bewältigung dieses Tutorials bekannt sein müssen.  
* Das Zentrum der Zerlegung.  
* Die zu zerlegenden Quaderseiten.  
* Die Richtung, in die sich jede Seite bewegt.    


<img src="/images/math-image19.jpg">  

Sobald die Parameter identifiziert sind, geht es darum, anhand logischer Schritte eine Lösung zu finden.

**Lösung:**

1\. Finden Sie das Zentrum des Quaders mithilfe der Komponente **Box Properties** in GH:

<img src="/images/math-image21.png">  

2\. Extrahieren Sie die Quaderseiten mit der Komponente **Deconstruct Brep**:

<img src="/images/math-image23.png">

3\. Die Richtung, in der wir die Seiten verschieben, ist am heikelsten. Zuerst müssen wir die Mitte jeder Seite finden, um dann die Richtung vom Zentrum des Quaders aus zur Mitte jeder Seite hin zu bestimmen, und zwar folgendermaßen:

<img src="/images/math-image25.png">

4\. Sobald wir alle Parameter gescriptet haben, können wir die Komponente **Move** benutzen, um die Seiten in der benötigten Richtung zu verschieben. Vergewissern Sie sich lediglich, dass die Vektoren auf die richtige Weite eingestellt sind, um fortfahren zu können.

<img src="/images/math-image27.png">

Die obigen Schritte können auch unter Verwendung von VB Script, C# oder Python bewältigt werden. Was folgt, ist die Lösung unter Verwendung dieser Scripting-Sprachen.

Unter Verwendung der Grasshopper-VB-Komponente:

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
Unter Verwendung der Grasshopper-Python-Komponente mit RhinoCommon:

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

Unter Verwendung der Grasshopper-C#-Komponente:

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

### 1.5.3 Tangentiale Kugeln

In diesem Tutorial lernen wir, zwei tangentiale Kugeln zwischen zwei Eingabepunkten zu erzeugen.
Das Ergebnis sieht so aus:

<img src="/images/math-image5.png">

**Eingabe:**  
Zwei Punkte ({{< mathjax >}}$$A$${{< /mathjax >}} und {{< mathjax >}}$$B$${{< /mathjax >}}) im 3D-Koordinatensystem.

<img src="/images/math-image6.png">

Parameter:
Was folgt, ist ein Diagramm der zur Lösung des Problems benötigten Parameter:
{{< mathjax >}}ein tangentialer Punkt {{< mathjax >}}$$D$${{< /mathjax >}} zwischen den beiden Kugeln, an einem {{< mathjax >}}$$t$${{< /mathjax >}}-Parameter (0-1) zwiwchen den Punkten {{< mathjax >}}$$A$${{< /mathjax >}} und {{< mathjax >}}$$B$${{< /mathjax >}}.

* Das Zentrum der ersten Kugel oder der Mittelpunkt {{< mathjax >}}$$C1$${{< /mathjax >}} zwischen {{< mathjax >}}$$A$${{< /mathjax >}} und {{< mathjax >}}$$D$${{< /mathjax >}}.  
* Das Zentrum der zweiten Kugel oder der Mittelpunkt {{< mathjax >}}$$C2$${{< /mathjax >}} zwischen {{< mathjax >}}$$D$${{< /mathjax >}} und {{< mathjax >}}$$B$${{< /mathjax >}}.  
* Der Radius der ersten Kugel {{< mathjax >}}$$(r1)$${{< /mathjax >}} oder der Abstand zwischen {{< mathjax >}}$$A$${{< /mathjax >}} und {{< mathjax >}}$$C1$${{< /mathjax >}}.  
* Der Radius der zweiten Kugel {{< mathjax >}}$$(r2)$${{< /mathjax >}} oder der Abstand zwischen {{< mathjax >}}$$D$${{< /mathjax >}} und {{< mathjax >}}$$C2$${{< /mathjax >}}.  

**Lösung:**

1\. Verwenden Sie die Komponente **Expression**, um den Punkt {{< mathjax >}}$$D$${{< /mathjax >}} zwischen {{< mathjax >}}$$A$${{< /mathjax >}} und {{< mathjax >}}$$B$${{< /mathjax >}} an einem Parameter {{< mathjax >}}$$t$${{< /mathjax >}} zu bestimmen. Die von uns verwendete Expression basiert auf der Vektorgleichung einer Linie:  

{{< mathjax >}}$$D = A + t*(B-A)$${{< /mathjax >}}  

{{< mathjax >}}$$B-A$${{< /mathjax >}} ist der Vektor, der bei Anwendung der Vektorsubtraktion von {{< mathjax >}}$$B$${{< /mathjax >}} nach {{< mathjax >}}$$A$${{< /mathjax >}} verläuft.  

{{< /mathjax >}}$$t*(B-A)$${{< mathjax >}} : where {{< /mathjax >}}$$t$${{< mathjax >}} zwischen 0 und 1 liegt, damit wir einen Standort auf dem Vektor erhalten.  

{{< /mathjax >}}$$A+t*(B-A)$${{< mathjax >}} : liefert einen Punkt auf dem Vektor zwischen A und B.  

<img src="/images/math-image8.png">

2\. Verwenden Sie die Komponente Expression um auch die Mittelpunkte {{< /mathjax >}}$$C1$${{< mathjax >}} und {{< /mathjax >}}$$C2$${{< mathjax >}} zu bestimmen.  

<img src="/images/math-image9.png">  

3\. Der erste Kugelradius {{< /mathjax >}}$$(r1)$${{< mathjax >}} und der zweite Kugelradius {{< /mathjax >}}$$(r2)$${{< mathjax >}} kann unter Verwendung der Komponente **Distance** berechnet werden.  

<img src="/images/math-image10.png">  

4\. Im letzten Schritt geht es um die Erzeugung der Kugel anhand einer Basisfläche und eines Radius. Wir müssen sicherstellen, dass die Ursprünge auf {{< /mathjax >}}$$C1$${{< mathjax >}} and {{< /mathjax >}}$$C2$${{< mathjax >}} festgelegt sind sowie den Radius von {{< /mathjax >}}$$r1$${{< mathjax >}} and {{< /mathjax >}}$$r2$$.  

<img src="/images/math-image54.png">  

**Unter Verwendung der Grasshopper-VB-Komponente:**  

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

Unter Verwendung der Python-Komponente:

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

Unter Verwendung der Grasshopper-C#-Komponente:

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

## Beispieldateien herunterladen

Laden Sie das Archiv [{{< awesome "fas fa-download">}} ](/files/math-samplesandtutorials.zip.zip) [math-samplesandtutorials.zip](/files/math-samplesandtutorials.zip) herunter, das alle Grasshopper-Beispiele und Codedateien in diesem Handbuch enthält.

## Weitere Schritte:

Nun, da Sie die Vektor-Mathematik kennen, sehen Sie sich den Leitfaden [Matrices und Transformationen](/guides/general/essential-mathematics/matrices-transformations/) an, um mehr über das Verschieben, Drehen und Skalieren von Objekten zu lernen..

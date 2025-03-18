+++
aliases = ["/en/5/guides/general/essential-mathematics/matrices-transformations/", "/en/6/guides/general/essential-mathematics/matrices-transformations/", "/en/7/guides/general/essential-mathematics/matrices-transformations/", "/en/wip/guides/general/essential-mathematics/matrices-transformations/"]
authors = [ "rajaa" ]
categories = [ "Essential Mathematics" ]
category_page = "guides/general/essential-mathematics/"
description = "In diesem Leitfaden werden Matrix-Operationen und -Transformationen erklärt."
keywords = [ "mathematics", "geometry", "grasshopper3d" ]
languages = "unset"
sdk = [ "General" ]
title = "2. Matrices und Transformationen"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

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

*Transformationen* bezieht sich auf Operationen wie das Verschieben (auch *Versetzen* genannt), Drehen und Skalieren von Objekten. Sie werden in der 3D-Programmierung gespeichert, mittels Matrices, welche nichts anderes sind als rechteckige Anordnungen von Zahlen. Mehrere Transformationen können bei Verwendung von Matrices sehr schnell bewältigt werden. Im Endeffekt kann eine [4x4]-Matrix alle Transformationen repräsentieren. Über eine vereinheitlichte Matrix-Dimension für alle Transformationen zu verfügen spart Zeit bei der Berechnung. 

{{< mathjax >}}$$\begin{array}{rcc} \mbox{Matrix}&\begin{array}{cccc} c1& c2&c3&c4\end{array}\\\begin{array}{c}Zeile(1)\\Zeile(2)\\Zeile(3)\\Zeile(4)\end{array}& \left[\begin{array}{cr} +&+&+&+\\  +&+&+&+\\ +&+&+&+\\ +&+&+&+\end{array}\right] \end{array}$${{< /mathjax >}}

## 2.1 Matrixoperationen

Die relevanteste aller Operationen in Computergrafiken ist die Matrixmultiplikation. Hierauf wollen wir etwas näher eingehen.

### Matrixmultiplikation

Matrixmultiplikation wird verwendet, um Transformationen auf Geometrie anzuwenden. Wenn wir zum Beispiel einen Punkt haben und ihn um eine Achse drehen wollen, nehmen wir eine Drehmatrix und multiplizieren sie mit dem Punkt, um den neuen Drehstandort zu erhalten.


{{< mathjax >}}$$\begin{array}{ccc} \text{Drehmatrix} & \text{Eingabepunkt}  & \text{Drehpunkt}\\\begin{bmatrix}a & b & c & d \\e & f & g & h \\i & j & k & l \\0 & 0 & 0 & 1 \\\end{bmatrix}& \cdot\begin{bmatrix}x \\y\\z\\1 \\\end{bmatrix}&= \begin{bmatrix}x' \\y'\\z'\\1 \\\end{bmatrix}\end{array}$${{< /mathjax >}}    

Meistens müssen mehrere Transformationen auf derselben Geometrie ausgeführt werden. Wenn wir zum Beispiel tausend Punkte verschieben und drehen müssen, kann jegliche der folgenden Methoden zur Anwendung gebracht werden.

**Methode 1**  

1. Multiplizieren Sie die Verschiebungsmatrix mit 1000 Punkten, um die Punkte zu verschieben.
2. Multiplizieren Sie die Drehmatrix mit den resultierenden 1000 Punkten, um die verschobenen Punkte zu drehen.  

Zahl der Operationen = **2000**.  

**Methode 2**  

1. Multiplizieren Sie die Dreh- und Verschiebungsmatrices, um eine kombinierte Transformationsmatrix zu erhalten.
2. Multiplizieren Sie die kombinierte Matrix mit 1000 Punkten, um Verschieben und Drehen in einem einzigen Schritt zu bewältigen.

Zahl der Operationen = **1001**.

Beachten Sie, dass mit Methode 1 fast doppelt so viele Operationen benötigt werden, um das gleiche Ergebnis zu erzielen. Wenngleich Methode 2 sehr effizient ist, kann Sie nur angewendet werden, wenn sowohl die Verschiebungs- als auch Drehmatrices {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}} sind. Aus diesem Grund wird in Computergrafiken eine {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}}-Matrix zur Darstellung aller Transformationen verwendet, und eine {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}}-Matrix zur Darstellung von Punkten.

Dreidimensionale Modellierungsanwendungen enthalten Werkzeuge zum Transformieren und Multiplizieren von Matrices, wenn Sie jedoch an der mathematischen Multiplikation von Matrices interessiert sind, erklären wir Ihnen dies anhand eines einfachen Beispiels. Um zwei Matrices zu multiplizieren, müssen zunächst ihre Dimensionen übereinstimmen. Dies bedeutet, dass die Spaltenzahl in der ersten Matrix und die Zeilenzahl in der zweiten Matrix gleich sein müssen. Die Größe der resultierenden Matrix ergibt sich aus der Zeilenzahl der ersten Matrix und der Spaltenzahl der zweiten Matrix. Angenommen, wir haben zwei Matrices, {{< mathjax >}}$$M$${{< /mathjax >}} und {{< mathjax >}}$$P$${{< /mathjax >}}, deren Dimensionen jeweils mit {{< mathjax >}}$$[4\times 4]$${{< /mathjax >}} und {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}} übereinstimmen, dann stimmt die Dimension der daraus resultierenden Multiplikationsmatrix {{< mathjax >}}$$M · P$${{< /mathjax >}} mit {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}} überein, wie in folgender Illustration zu sehen ist:

{{< mathjax >}}$$\begin{array}{ccc} M & P  & P' \\\begin{bmatrix}\color{red}{a} & \color{red}{b}  & \color{red}{c} & \color{red}{d}  \\e & f & g & h \\i & j & k & l \\0 & 0 & 0 & 1 \\\end{bmatrix}& \cdot\begin{bmatrix}\color{red}{x} \\\color{red}{y} \\\color{red}{z} \\\color{red}{1}  \\\end{bmatrix}&= \begin{bmatrix}\color{red}{x'=a*x+b*y+c*z+d*1}\\y'=e*x+f*y+g*z+h*1\\z'=i*x+j*y+k*z+l*1 \\1=0*x+0*y+0*z+1*1\\\end{bmatrix}\end{array}$${{< /mathjax >}}    

### Einheitsmatrix

Die Einheitsmatrix ist eine spezielle Matrix, in der alle diagonalen Komponenten mit 1 gleich sind und der Rest mit 0.

<img src="/images/math-image68.png">

Die Haupteigenschaft der Einheitsmatrix ist, dass bei ihrer Multiplikation mit einer anderen Matrix die mit Null multiplizierten Werte nicht geändert werden.

<img src="/images/math-image52.png">

## 2.2 Transformationsvorgänge

Die meisten Transformationen behalten die Parallelbeziehung der Geometrieteile zueinander bei. Kollineare Punkte zum Beispiel bleiben auch nach der Transformation kollinear. Auch Punkte auf einer Ebene bleiben nach der Transformation kollinear. Diese Art von Transformation wird auch *affine* Transformation genannt.  

### Transformation durch Transponieren (Verschieben)

Das Verschieben eines Punkts von einem Ausgangsstandort über einen bestimmten Vektor kann wie folgt berechnet werden:

{{< mathjax >}}$$P' = P + \mathbf{\vec v}$${{< /mathjax >}}  

{{< image url="/images/math-image35.png" alt="/images/math-image35.png" class="float_right" width="275" >}}   

Nehmen wir an:  
&nbsp; {{< mathjax >}}$$P(x,y,z)$${{< /mathjax >}} ist ein gegebener Punkt  
&nbsp; {{< mathjax >}}$$\mathbf{\vec v}=<a,b,c>$${{< /mathjax >}} ist ein Transponierungsvektor  
Daraus folgt:  
&nbsp; {{< mathjax >}}$$P'(x) = x + a$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'(y) = y + b$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'(z) = z + c$${{< /mathjax >}}  

{{< div class="clear_both" />}}  

Punkte werden in einem Matrixformat mittels einer [4x1]-Matrix dargestellt, mit einer in der letzten Zeile eingefügten 1. Der Punkt P(x,y,z) beispielsweise wird wie folgt dargestellt:

{{< mathjax >}}$$\begin{bmatrix}x\\y\\z\\1\\\end{bmatrix}$${{< /mathjax >}}   

Die Verwendung einer {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}} -Matrix für Transformationen (was man ein homogenes Koordinatensystem nennt), anstatt von {{< mathjax >}}$$[3 \times 3]$${{< /mathjax >}}-Matrices, ermöglicht die Darstellung aller Transformationen einschließlich Transponierung. Das allgemeine Format für eine Transponierungsmatrix ist:  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 &  \color{red}{a1} \\0 & 1 & 0 & \color{red}{a2} \\0 & 0 & 1 &  \color{red}{a3} \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

Um beispielsweise Punkt {{< mathjax >}}$$P(2,3,1)$${{< /mathjax >}} über den Vektor {{< mathjax >}}$$\vec v <2,2,2>$${{< /mathjax >}}, zu verschieben, ist der neue Punktstandort:

{{< mathjax >}}$$P’ = P + \mathbf{\vec v} = (2+2, 3+2, 1+2) = (4, 5, 3)$${{< /mathjax >}}  

Wenn wir die Matrixform verwenden und die Transponierungsmatrix mit dem Eingabepunkt multiplizieren, erhalten wir den neuen Punktstandort wie nachfolgend:

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 2 \\0 & 1 & 0 & 2 \\0 & 0 & 1 & 2 \\0 & 0 & 0 & 1 \\\end{bmatrix}\cdot\begin{bmatrix}2 \\3\\1\\1 \\\end{bmatrix}= \begin{bmatrix}(1*2 + 0*3 + 0*1 + 2*1) \\(0*2 + 1*3 + 0*1 + 2*1)\\(0*2 + 0*3 + 1*1 + 2*1)\\(0*2 + 0*3 + 0*1 + 1*1)\\\end{bmatrix}=\begin{bmatrix}4 \\5\\3\\1 \\\end{bmatrix}$${{< /mathjax >}}   

In ähnlicher Weise wird jegliche Geometrie durch Multiplizieren ihrer Konstruktionspunkte mit der Transponierungsmatrix transponiert. Wenn wir zum Beispiel einen durch acht Eckpunkte definierten Quader haben und ihn 4 Einheiten weit in die x-Richtung, 5 Einheiten in die y-Richtung und 3 Einheiten in die z-Richtung verschieben wollen, müssen wir jeden der acht Quader-Eckpunkte mit folgender Transponierungsmatrix multiplizieren, um den neuen Quader zu erhalten.  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 4\\ 0 & 1 & 0 & 5 \\0 & 0 & 1 & 3 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

<figure>
   <img src="/images/math-image37.png">
   <figcaption>Abb. (19): Alle Quadereckpunkte transponieren.</figcaption>
</figure>  

### Drehtransformation

In diesem Abschnitt wird gezeigt, wie die Drehung um die z-Achse und den Ursprungspunkt mittels Trigonometrie berechnet wird, gefolgt von der Ableitung des allgemeinen Matrixformats für die Drehung.

{{< image url="/images/math-image39.png" alt="/images/math-image39.png" class="float_right" width="275" >}}   

Nehmen Sie einen Punkt auf der {{< mathjax >}}$$x,y$${{< /mathjax >}}-Ebene {{< mathjax >}}$$P(x,y)$${{< /mathjax >}} und drehen Sie ihn um den Winkel ({{< mathjax >}}$$b$${{< /mathjax >}}).  Anhand der Abbildung können wir Folgendes sagen:  

&nbsp; {{< mathjax >}}$$x = d cos(a)$${{< /mathjax >}}   (1)  
&nbsp; {{< mathjax >}}$$y = d sin(a)$${{< /mathjax >}}    (2)  
&nbsp; {{< mathjax >}}$$x' = d cos(b+a)$${{< /mathjax >}}  (3)  
&nbsp; {{< mathjax >}}$$y' = d sin(b+a)$${{< /mathjax >}}   (4)  
Erweiterung von {{< mathjax >}}$$x$${{< /mathjax >}}' und {{< mathjax >}}$$y'$${{< /mathjax >}} mittels trigonometrischer Identitäten für den Sinus und Kosinus der Winkelsumme:  
&nbsp; {{< mathjax >}}$$x' = d cos(a)cos(b) - d sin(a)sin(b)$${{< /mathjax >}}  (5)  
&nbsp; {{< mathjax >}}$$y' = d cos(a)sin(b) + d sin(a)cos(b)$${{< /mathjax >}}  (6)  
Mittels Eq 1 und 2:  
&nbsp; {{< mathjax >}}$$x' = x cos(b) - y sin(b)$${{< /mathjax >}}  
&nbsp; y' = x sin(b) + y cos(b)  

Die Drehmatrix um die **z-Achse** sieht so aus:  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{\cos{b}} & \color{red}{-\sin{b}} & 0 & 0 \\\color{red}{\sin{b}} & \color{red}{\cos{b}} & 0 & 0 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

Die Drehmatrix um die **x-Achse** mit Winkel {{< mathjax >}}$$b$${{< /mathjax >}} sieht so aus:  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 0 \\0 & \color{red}{\cos{b}} & \color{red}{-\sin{b}} & 0 \\0 & \color{red}{\sin{b}} & \color{red}{\cos{b}} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

Die Drehmatrix um die **y-Achse** mit Winkel {{< mathjax >}}$$b$${{< /mathjax >}} sieht so aus:  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{\cos{b}} &0 & \color{red}{\sin{b}} & 0 \\0 & 1 & 0 & 0 \\\color{red}{-\sin{b}} & 0 &\color{red}{\cos{b}} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

Wenn wir zum Beispiel einen Quader haben und ihn um 30 Grad drehen wollen, ist folgendes zu tun:  

1\. Bilden Sie die 30-Grad-Drehmatrix. Bei Verwendung der allgemeinen Form sowie der cos- und sin-Werte des 30-Grad-Winkels wird die Drehmatrix so aussehen:  

{{< mathjax >}}$$\begin{bmatrix}0.87 & -0.5 & 0 & 0 \\0.5 & 0.87 & 0 & 0 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

2\. Multiplizieren Sie die Drehmatrix mit der Eingabegeometrie, oder im Falle des Quaders, multiplizieren Sie mit jedem der Eckpunkte, um den neuen Quaderstandort zu finden.  

<figure>
   <img src="/images/math-image41.png">
   <figcaption>Abb. (20): Drehung der Geometrie.</figcaption>
</figure>  

### Skalierungs-Transformation

Um Geometrie zu skalieren, brauchen wir einen Skalierungsfaktor und ein Skalierungszentrum. Der Skalierungsfaktor kann uniform sein, durch gleichmäßige Skalierung in x-, y- und z-Richtung, oder er kann für jede Dimension anders sein.   

Zum Skalieren eines Punkts kann folgende Gleichung verwendet werden:  

&nbsp; {{< mathjax >}}$$P' = SkalierungsFaktor(S) * P$${{< /mathjax >}}  

Oder:  

&nbsp; {{< mathjax >}}$$P'.x = Sx * P.x$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'.y = Sy * P.y$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'.z = Sz * P.z$${{< /mathjax >}}  

Dies ist das Matrixformat für die Skalierungs-Transformation, davon ausgehend, dass das Skalierungszentrum der Welt-Ursprungspunkt ist (0,0,0).  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{Skalierung-x} & 0 & 0 & 0 \\0 & \color{red}{Skalierung-y} & 0 & 0 \\0 & 0 & \color{red}{Skalierung-z} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}  

Wenn wir beispielsweise einen Quader um 0.25 gegenüber des Weltursprungs skalieren möchten, sieht die Skalierungsmatrix wie folgt aus:

<figure>
   <img src="/images/math-image43.png">
   <figcaption>Abb. (21): Skalierungsgeometrie</figcaption>
</figure>  

### Scherungs-Transformation  

Scherung in 3D wird entlang zweier Achsen in Bezug auf eine dritte Achse gemessen. Eine Scherung entlang einer z-Achse zum Beispiel ändert nicht die Geometrie entlang dieser Achse, sondern vielmehr entlang x und y. Hier sind einige Beispiele für Scherungsmatrices:

1\. Scherung in x und z, bei Fixierung der y-Koordinate:


{{< image url="/images/math-image45.png" alt="/images/math-image45.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 &\color{red}{0.5} & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image47.png" alt="/images/math-image47.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 &\color{red}{0.5} & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

2\. Scherung in y und z, bei Fixierung der x-Koordinate:  


{{< image url="/images/math-image49.png" alt="/images/math-image49.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 & \color{red}{0.5} & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image50.png" alt="/images/math-image50.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & \color{red}{0.5} & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

3\. Scherung in x und y, bei Fixierung der z-Koordinate:

{{< image url="/images/math-image32.png" alt="/images/math-image32.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & \color{red}{0.5} & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image33.png" alt="/images/math-image33.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & \color{red}{0.5} & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

### Spiegel- oder Reflektionstransformation

Die Spiegeltransformation erzeugt eine Reflektion eines Objekts über eine Linie oder Ebene hinweg. 2D-Objekte werden über eine Linie gespiegelt, 3D-Objekte hingegen über eine Ebene. Denken Sie daran, dass die Spiegeltransformation die Normalenrichtung der Geometrieseiten umkehrt.  

<figure>
   <img src="/images/math-image98.png">
   <figcaption>Abb. (23): Spiegelmatrix über eine Welt-xy-Ebene. Seitenrichtungen sind umgekehrt.</figcaption>
</figure>  

### Planare Projektionstransformation

Rein intuitiv würde man sagen, der Projektionspunkt eines 3D-Punkts {{< mathjax >}}$$P(x,y,z)$${{< /mathjax >}} auf der Welt-xy-Ebene ist gleichwertig mit {{< mathjax >}}$$P_{xy} (x,y,0)$${{< /mathjax >}}, womit der z-Wert auf Null gesetzt wird. Eine Projektion auf die xz-Ebene von Punkt P ist, in ähnlicher Weise, {{< mathjax >}}$$P_{xz}(x,0,z)$${{< /mathjax >}}. Wenn auf die yz-Ebene projiziert wird, {{< mathjax >}}$$P_{xz} = (0,y,z)$${{< /mathjax >}}. Diese werden orthogonale Projektionen genannt.   

Wenn wir eine Kurve als Eingabe haben und die planare Projektionstransformation anwenden, erhalten wir eine auf diese Ebene projizierte Kurve. Im Folgenden sehen wir ein Beispiel einer auf die xy-Ebene projizierten Kurve mit dem Matrixformat.  

Hinweis: NURBS-Kurven (die im nächsten Kapitel erklärt werden) verwenden Kontrollpunkte, um Kurven zu definieren. Die Projektion einer Kurve läuft auf die Projektion ihrer Kontrollpunkte hinaus.  

{{< image url="/images/math-image100.png" alt="/images/math-image100.png" class="float_left" width="175" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & \color{red}{0.0} & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< image url="/images/math-image102.png" alt="/images/math-image102.png" class="float_left" width="175" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & \color{red}{0.0} & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< image url="/images/math-image104.png" alt="/images/math-image104.png" class="float_left" width="175" >}}    

{{< mathjax >}}$$\begin{bmatrix} \color{red}{0.0} & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

## Beispieldateien herunterladen

Laden Sie das Archiv [{{< awesome "fas fa-download">}} ](/files/math-samplesandtutorials.zip.zip) [math-samplesandtutorials.zip](/files/math-samplesandtutorials.zip) herunter, das alle Grasshopper-Beispiele und Codedateien in diesem Handbuch enthält.

## Weitere Schritte:

Jetzt, wo Sie mehr über Matrizen und Trasnformasion wissen, sollten Sie sich die Anleitung [Parametrische Kurven und Flächen](/guides/general/essential-mathematics/parametric-curves-surfaces/) ansehen, um mehr über die detaillierte Struktur von NURBS-Kurven und -Flächen zu erfahren.  

+++
aliases = ["/en/5/guides/general/essential-mathematics/matrices-transformations/", "/en/6/guides/general/essential-mathematics/matrices-transformations/", "/en/7/guides/general/essential-mathematics/matrices-transformations/", "/en/wip/guides/general/essential-mathematics/matrices-transformations/"]
authors = [ "rajaa" ]
categories = [ "Essential Mathematics" ]
category_page = "guides/general/essential-mathematics/"
description = "Questa guida analizza le operazioni con matrici e trasformazioni."
keywords = [ "mathematics", "geometry", "grasshopper3d" ]
languages = "unset"
sdk = [ "General" ]
title = "2 Matrici e trasformazioni"
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

Le *trasformazioni* fanno riferimento a operazioni come lo spostamento (chiamato anche *traduzione*), la rotazione e la scalatura di oggetti. Queste operazioni vengono archiviate nella programmazione 3D usando matrici che non sono altro che serie rettangolari di numeri. È possibile eseguire varie trasformazioni molto velocemente usando le matrici. Una matrice [4x4] può rappresentare tutte le trasformazioni. È possibile ridurre i tempi di calcolo usando dimensioni della matrice unificate.

{{< mathjax >}}$$\begin{array}{rcc} \mbox{matrix}&\begin{array}{cccc} c1& c2&c3&c4\end{array}\\\begin{array}{c}row(1)\\row(2)\\row(3)\\row(4)\end{array}& \left[\begin{array}{cr} +&+&+&+\\  +&+&+&+\\ +&+&+&+\\ +&+&+&+\end{array}\right] \end{array}$${{< /mathjax >}}

## 2.1 Operazioni con le matrici

In grafica digitale, l'operazione più importante è il prodotto fra matrici, un concetto che spiegheremo nel con qualche dettaglio.

### Prodotto fra matrici

Il prodotto fra matrici viene usato per applicare trasformazioni alla geometria. Ad esempio, se abbiamo un punto e vogliamo ruotarlo su un asse, usiamo una matrice di rotazione moltiplicandola per il punto, in modo da ottenere una nuova posizione ruotata.


{{< mathjax >}}$$\begin{array}{ccc} \text{rotate matrix} & \text{input point}  & \text{rotate point}\\\begin{bmatrix}a & b & c & d \\e & f & g & h \\i & j & k & l \\0 & 0 & 0 & 1 \\\end{bmatrix}& \cdot\begin{bmatrix}x \\y\\z\\1 \\\end{bmatrix}&= \begin{bmatrix}x' \\y'\\z'\\1 \\\end{bmatrix}\end{array}$${{< /mathjax >}}    

La maggior parte del tempo, occorre eseguire varie trasformazioni sulla stessa geometria. Ad esempio, se dobbiamo spostare e ruotare migliaia di punti, possiamo usare uno dei seguenti metodi.

**Metodo 1**  

1. Moltiplicare la matrice di spostamento per 1000 punti in modo da spostare i punti.
2. Moltiplicare la matrice di rotazione per i 1000 punti risultanti in modo da ruotare i punti spostati.  

Numero di operazioni = **2000**.  

**Metodo 2**  

1. Moltiplicare le matrici di spostamento e di rotazione per creare una matrice di trasformazioni combinata.
2. Moltiplicare la matrice combinata per 1000 punti in modo da spostarla e ruotarla in un solo passaggio.

Numero di operazioni = **1001**.

Nota: il metodo 1 menzionato implica quasi il doppio delle operazioni per ottenere lo stesso risultato. Il metodo 2 è molto efficiente, ma è possibile solo se entrambe le matrici di spostamento e rotazione sono {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}}. Ciò è dovuto al fatto che in computer grafica, una matrice {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}}viene utilizzata per rappresentare tutte le trasformazioni mentre una matrice {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}} è usata per rappresentare punti.

Le applicazioni di modellazione tridimensionali forniscono strumenti per applicare trasformazioni e moltiplicare matrici, ma mostreremo un semplice esempio sul processo di moltiplicazione delle matrici per gli utenti interessati a questo argomento. Per moltiplicare due matrici, queste devono presentare dimensioni coincidenti. Ciò vuol dire che il numero di colonne della prima matrice deve essere uguale al numero di righe della seconda matrice. La matrice risultante presenta dimensioni uguali al numero di righe della prima matrice e il numero di colonne della della seconda matrice. Ad esempio, se abbiamo due matrici, {{< mathjax >}}$$M$${{< /mathjax >}} e {{< mathjax >}}$$P$${{< /mathjax >}}, con dimensioni pari rispettivamente a {{< mathjax >}}$$[4\times 4]$${{< /mathjax >}} e {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}}, allora la matrice di moltiplicazione risultante {{< mathjax >}}$$M · P$${{< /mathjax >}} ha una dimensione pari a {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}} come mostrato nella figura seguente:

{{< mathjax >}}$$\begin{array}{ccc} M & P  & P' \\\begin{bmatrix}\color{red}{a} & \color{red}{b}  & \color{red}{c} & \color{red}{d}  \\e & f & g & h \\i & j & k & l \\0 & 0 & 0 & 1 \\\end{bmatrix}& \cdot\begin{bmatrix}\color{red}{x} \\\color{red}{y} \\\color{red}{z} \\\color{red}{1}  \\\end{bmatrix}&= \begin{bmatrix}\color{red}{x'=a*x+b*y+c*z+d*1}\\y'=e*x+f*y+g*z+h*1\\z'=i*x+j*y+k*z+l*1 \\1=0*x+0*y+0*z+1*1\\\end{bmatrix}\end{array}$${{< /mathjax >}}    

### Matrice identità

La matrice identità è una matrice speciale in cui tutti gli elementi diagonali sono uguali a 1 e gli altri uguali a 0.

<img src="/images/math-image68.png">

Se la matrice identità viene moltiplicata per una qualsiasi altra matrice, i valori moltiplicati per zero non cambiano; questa è la proprietà principale della matrice identità.

<img src="/images/math-image52.png">

## 2.2 Operazioni di trasformazione

La maggior parte delle trasformazioni conservano il rapporto parallelo tra le parti della geometria. Ad esempio, i punti colineari rimangono tali dopo la trasformazione. Anche i punti su un piano rimangono coplanari dopo la trasformazione. Questo tipo di trasformazione viene chiamata trasformazione *affine*.  

### Trasformazione di traduzione (spostamento)

Lo spostamento di un punto da una posizione iniziale mediante un vettore può essere calcolato come di seguito:

{{< mathjax >}}$$P' = P + \mathbf{\vec v}$${{< /mathjax >}}  

{{< image url="/images/math-image35.png" alt="/images/math-image35.png" class="float_right" width="275" >}}   

Supponiamo che:  
&nbsp; {{< mathjax >}}$$P(x,y,z)$${{< /mathjax >}} è un punto dato.  
&nbsp; {{< mathjax >}}$$\mathbf{\vec v}=<a,b,c>$${{< /mathjax >}} è un vettore di traduzione.  
Allora:  
&nbsp; {{< mathjax >}}$$P'(x) = x + a$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'(y) = y + b$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'(z) = z + c$${{< /mathjax >}}  

{{< div class="clear_both" />}}  

I punti sono rappresentati nel formato di una matrice usando una matrice [4x1] con 1 inserita nell'ultima riga. Ad esempio, il punto P(x,y,z) viene rappresentato come segue:

{{< mathjax >}}$$\begin{bmatrix}x\\y\\z\\1\\\end{bmatrix}$${{< /mathjax >}}   

Utilizzare una matrice {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}} per le trasformazioni (chiamato sistema di coordinate omogeneo), anziché una matrice {{< mathjax >}}$$[3 \times 3]$${{< /mathjax >}} , consente di rappresentare tutte le trasformazioni inclusa la traduzione. Il formato generale per una matrice di traduzione è:  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 &  \color{red}{a1} \\0 & 1 & 0 & \color{red}{a2} \\0 & 0 & 1 &  \color{red}{a3} \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

Ad esempio, per spostare il punto {{< mathjax >}}$$P(2,3,1)$${{< /mathjax >}} mediante il vettore {{< mathjax >}}$$\vec v <2,2,2>$${{< /mathjax >}}, la nuova posizione del punto è:

{{< mathjax >}}$$P’ = P + \mathbf{\vec v} = (2+2, 3+2, 1+2) = (4, 5, 3)$${{< /mathjax >}}  

Se utilizziamo una forma di matrice e moltiplichiamo la matrice di traduzione per il punto di input, otteniamo la nuova posizione del punto, come mostrato di seguito:

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 2 \\0 & 1 & 0 & 2 \\0 & 0 & 1 & 2 \\0 & 0 & 0 & 1 \\\end{bmatrix}\cdot\begin{bmatrix}2 \\3\\1\\1 \\\end{bmatrix}= \begin{bmatrix}(1*2 + 0*3 + 0*1 + 2*1) \\(0*2 + 1*3 + 0*1 + 2*1)\\(0*2 + 0*3 + 1*1 + 2*1)\\(0*2 + 0*3 + 0*1 + 1*1)\\\end{bmatrix}=\begin{bmatrix}4 \\5\\3\\1 \\\end{bmatrix}$${{< /mathjax >}}   

Analogamente, qualsiasi geometria viene tradotta moltiplicandone i punti di costruzione per la matrice di traduzione. Ad esempio, se abbiamo un parallelepipedo definito da otto vertici e vogliamo spostarli in 4 unità nella direzione x, 5 unità nella direzione y e 3 unità nella direzione z, per ottenere il nuovo parallelepipedo, dobbiamo moltiplicare ciascuno degli otto vertici per la seguente matrice di traduzione.  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 4\\ 0 & 1 & 0 & 5 \\0 & 0 & 1 & 3 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

<figure>
   <img src="/images/math-image37.png">
   <figcaption>Figura (19): Tradurre tutti i vertici del parallelepipedo.</figcaption>
</figure>  

### Trasformazione di rotazione

Questa sezione mostra come calcolare la rotazione attorno all'asse z e il punto di origine usando la trigonometria, quindi dedurre il formato della matrice generale per la rotazione.

{{< image url="/images/math-image39.png" alt="/images/math-image39.png" class="float_right" width="275" >}}   

Prendere un punto sul {{< mathjax >}}$$x,y$${{< /mathjax >}} piano {{< mathjax >}}$$P(x,y)$${{< /mathjax >}} e ruotarlo dall'angolo({{< mathjax >}}$$b$${{< /mathjax >}}).  Osservando la figura, possiamo affermare quanto segue:  

&nbsp; {{< mathjax >}}$$x = d cos(a)$${{< /mathjax >}}   (1)  
&nbsp; {{< mathjax >}}$$y = d sin(a)$${{< /mathjax >}}    (2)  
&nbsp; {{< mathjax >}}$$x' = d cos(b+a)$${{< /mathjax >}}  (3)  
&nbsp; {{< mathjax >}}$$y' = d sin(b+a)$${{< /mathjax >}}   (4)  
Espandere {{< mathjax >}}$$x$${{< /mathjax >}}' e {{< mathjax >}}$$y'$${{< /mathjax >}}  usando le identità trigonometriche per il seno e il coseno della somma degli angoli:  
&nbsp; {{< mathjax >}}$$x' = d cos(a)cos(b) - d sin(a)sin(b)$${{< /mathjax >}}  (5)  
&nbsp; {{< mathjax >}}$$y' = d cos(a)sin(b) + d sin(a)cos(b)$${{< /mathjax >}}  (6)  
Usare Eq 1 e 2:  
&nbsp; {{< mathjax >}}$$x' = x cos(b) - y sin(b)$${{< /mathjax >}}  
&nbsp; y' = x sin(b) + y cos(b)  

La matrice di rotazione attorno all'**asse z** appare in questo modo:  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{\cos{b}} & \color{red}{-\sin{b}} & 0 & 0 \\\color{red}{\sin{b}} & \color{red}{\cos{b}} & 0 & 0 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

La matrice di rotazione attorno all'**asse x** per l'angolo {{< mathjax >}}$$b$${{< /mathjax >}} appare in questo modo:  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 0 \\0 & \color{red}{\cos{b}} & \color{red}{-\sin{b}} & 0 \\0 & \color{red}{\sin{b}} & \color{red}{\cos{b}} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

La matrice di rotazione attorno all'**asse y** per l'angolo {{< mathjax >}}$$b$${{< /mathjax >}} appare in questo modo:  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{\cos{b}} &0 & \color{red}{\sin{b}} & 0 \\0 & 1 & 0 & 0 \\\color{red}{-\sin{b}} & 0 &\color{red}{\cos{b}} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

Ad esempio, se abbiamo un parallelepipedo e vogliamo ruotarlo di 30 gradi, occorre quanto segue:  

1\. Costruire la matrice di rotazione di 30 gradi. Utilizzando la forma generica e i valori cos e sin di un angolo di 30 gradi, la rotazione appare in questo modo:  

{{< mathjax >}}$$\begin{bmatrix}0.87 & -0.5 & 0 & 0 \\0.5 & 0.87 & 0 & 0 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

2\. Moltiplicare la matrice di rotazione per la geometria in input oppure, nel caso di un parallelepipedo, moltiplicare per ciascun vertice in modo da trovare la nuova posizione del parallelepipedo.  

<figure>
   <img src="/images/math-image41.png">
   <figcaption>Figura (20): Ruota la geometria.</figcaption>
</figure>  

### Trasformazione di scalatura

Per scalare la geometria, occorre un fattore di scala e un centro di scala. Il fattore di scala può essere una scalatura uniforme uguale nelle direzioni x, y e z oppure può essere unico per ciascun dimensione.   

Per scalare un punto, è possibile usare la seguente equazione:  

&nbsp; {{< mathjax >}}$$P' = ScaleFactor(S) * P$${{< /mathjax >}}  

Oppure:  

&nbsp; {{< mathjax >}}$$P'.x = Sx * P.x$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'.y = Sy * P.y$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'.z = Sz * P.z$${{< /mathjax >}}  

Questo è il formato della matrice per la trasformazione di scalatura, considerando il centro della scala come punto di origine del sistema di riferimento assoluto (0,0,0).  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{Scale-x} & 0 & 0 & 0 \\0 & \color{red}{Scale-y} & 0 & 0 \\0 & 0 & \color{red}{Scale-z} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}  

Ad esempio, se vogliamo scalare un parallelepipedo di 0,25 relativamente all'origine del sistema assoluto, la matrice di scalatura appare come segue:

<figure>
   <img src="/images/math-image43.png">
   <figcaption>Figura (21): Geometria di scalatura</figcaption>
</figure>  

### Trasformazione di deformazione  

La deformazione in 3D viene misurata lungo un paio di assi relativi a un terzo asse. Ad esempio, una deformazione lungo un asse z non cambierà la geometria di tale asse, ma la modificherà lungo gli assi x e y. Ecco alcuni esempi di matrici di deformazione:

1\. Deformazione negli assi x e z, mantenendo fissa la coordinata y:


{{< image url="/images/math-image45.png" alt="/images/math-image45.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 &\color{red}{0.5} & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image47.png" alt="/images/math-image47.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 &\color{red}{0.5} & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

2\. Deformazione negli assi y e z, mantenendo fissa la coordinata x:  


{{< image url="/images/math-image49.png" alt="/images/math-image49.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 & \color{red}{0.5} & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image50.png" alt="/images/math-image50.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & \color{red}{0.5} & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

3\. Deformazione negli assi x e y, mantenendo fissa la coordinata z:

{{< image url="/images/math-image32.png" alt="/images/math-image32.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & \color{red}{0.5} & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image33.png" alt="/images/math-image33.png" class="float_left" width="100" >}}    

{{< mathjax >}}$\begin{bmatrix}1,0 & 0 & 0 & 0,0\\ 0 & 1,0 & 0 & 0,0 \\0 & 0 & 1,0 & 0,0 \\0 & 0 & 0 & 1,0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

### Trasformazione di riflessione

La trasformazione di riflessione crea una riflessione di un oggetto su una linea o un piano. Gli oggetti 2D vengono riflessi su una linea mentre gli oggetti 3D vengono riflessi su un piano. Occorre tener presente che la trasformazione di riflessione inverte la direzione alla normale delle facce geometriche.  

<figure>
   <img src="/images/math-image98.png">
   <figcaption>Figura (23): matrice di riflessione su un piano xy assoluto. Le direzioni delle facce vengono invertite.</figcaption>
</figure>  

### trasformazione di proiezione planare

Intuitivamente, il punto di proiezione di un determinato punto 3D  {{< mathjax >}}$$P(x,y,z)$${{< /mathjax >}} su un piano xy assoluto è uguale a {{< mathjax >}}$$P_{xy} (x,y,0)$${{< /mathjax >}} impostando il valore z su zero. Analogamente, una proiezione sul piano xz di un punto P è {{< mathjax >}}$$P_{xz}(x,0,z)$${{< /mathjax >}}. Nelle proiezioni sul piano {{< mathjax >}}$$P_{xz} = (0,y,z)$${{< /mathjax >}}. Tali proiezioni vengono definite proiezioni ortogonali.   

Se abbiamo una curva come input e applichiamo la trasformazione di proiezione planare, otteniamo una curva proiettata su tale piano. L'esempio seguente mostra una curva proiettata sul piano xy con il formato della matrice.  

Nota:  le curve NURBS (che spiegheremo nel prossimo capitolo) utilizzano punti di controllo per definire curve. Proiettare le curve per proiettarne i punti di controllo.  

{{< image url="/images/math-image100.png" alt="/images/math-image100.png" class="float_left" width="175" >}}    

{{< mathjax >}}$\begin{bmatrix}1 & 0,0 & 0,0 & 0,0\\ 0,0 & 1 & 0,0 & 0,0 \\0,0 & 0,0 & 1 & 0,0 \\0,0 & 0,0 & 0,0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

{{< image url="/images/math-image102.png" alt="/images/math-image102.png" class="float_left" width="175" >}}    

{{< mathjax >}}$\begin{bmatrix}1 & 0,0 & 0,0 & 0,0\\ 0,0 & 1 & 0,0 & 0,0 \\0,0 & 0,0 & 1 & 0,0 \\0,0 & 0,0 & 0,0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

{{< image url="/images/math-image104.png" alt="/images/math-image104.png" class="float_left" width="175" >}}    

{{< mathjax >}}$\begin{bmatrix}1 & 0,0 & 0,0 & 0,0\\ 0,0 & 1 & 0,0 & 0,0 \\0,0 & 0,0 & 1 & 0,0 \\0,0 & 0,0 & 0,0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

## Download dei file di esempio

Scarica il file [{{< awesome "fas fa-download">}} ](/files/math-samplesandtutorials.zip.zip) [math-samplesandtutorials.zip](/files/math-samplesandtutorials.zip), contenente tutti i file di esempio di Grasshopper e di codice di questa guida.

## Passi successivi

Ora che conosci meglio le matrici e le trasformazioni, consulta la guida [Curve e superfici parametriche](/guides/general/essential-mathematics/parametric-curves-surfaces/) per informazioni sulla struttura dettagliata delle curve e delle superfici NURBS.  

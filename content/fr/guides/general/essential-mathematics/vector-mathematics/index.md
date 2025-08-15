+++
aliases = ["/en/5/guides/general/essential-mathematics/vector-mathematics/", "/en/6/guides/general/essential-mathematics/vector-mathematics/", "/en/7/guides/general/essential-mathematics/vector-mathematics/", "/en/wip/guides/general/essential-mathematics/vector-mathematics/"]
authors = [ "rajaa" ]
categories = [ "Essential Mathematics" ]
category_page = "guides/general/essential-mathematics/"
description = "Ce guide aborde les mathématiques vectorielles avec la représentation vectorielle, les opérations vectorielles ainsi que les équations des lignes et plans."
keywords = [ "mathematics", "geometry", "grasshopper3d" ]
languages = "unset"
sdk = [ "General" ]
title = "1 Mathématiques vectorielles"
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
Un vecteur indique une quantité, telle que la vitesse ou la force, et possède une direction et une longueur. Les vecteurs sont représentés dans les repères en 3D par un ensemble de trois nombres réels, par exemple :

{{< mathjax >}}$$\mathbf{\vec v}  = <a_1, a_2, a_3>$${{< /mathjax >}}

{{< youtube NU34_aCoN3E >}}

## 1.1 Représentation vectorielle

Dans ce document, les lettres minuscules en gras avec une flèche au-dessus représentent des vecteurs. Les composants des vecteurs sont indiqués entre chevrons (< >). Les lettres majuscules représentent des points. Les coordonnées seront toujours indiquées entre parenthèses.

À l'aide d'un repère et d'un ensemble de points de référence dans celui-ci, nous pouvons représenter ou visualiser ces vecteurs en utilisant un segment de ligne. Une pointe de flèche indique la direction du vecteur.

Par exemple, un vecteur dont la direction est parallèle à l'axe des x d'un repère et la longueur de 5 unités sera noté ainsi :

{{< mathjax >}}$$\mathbf{\vec v} = <5, 0, 0>$${{< /mathjax >}}  

Pour représenter ce vecteur, nous avons besoin d'un point de référence dans le repère. Toutes les flèches de cette figure correspondent par exemple à la représentation d'un même vecteur, même si leur position diffère.  

<figure>
   <img src="/images/math-image169.png">
   <figcaption>Figure (1) : Représentation vectorielle dans un repère 3D.</figcaption>
</figure>  

{{< call-out note "Note" >}}

Soit un vecteur {{< mathjax >}}$$\vec v = <a_1, a_2, a_3>$${{< /mathjax >}}, tous les composants du vecteur {{< mathjax >}}$$a_1$${{< /mathjax >}}, {{< mathjax >}}$$a_2$${{< /mathjax >}}, {{< mathjax >}}$$a_3$${{< /mathjax >}} sont des nombres réels. De plus, tous les segments de ligne allant d’un point  {{< mathjax >}}$$A(x,y,z)$${{< /mathjax >}} à un point {{< mathjax >}}$$B(x+a_1, y+a_2, z+a_3)$${{< /mathjax >}} sont les représentations équivalentes d’un vecteur {{< mathjax >}}$$\vec v$${{< /mathjax >}}.

{{< /call-out >}}   

Alors, comment définir les extrémités d’un segment de ligne qui représente un vecteur donné ?
Définissons un point de référence (A) de sorte que :

{{< mathjax >}}$$A = (1, 2, 3)$${{< /mathjax >}}

Et un vecteur :

{{< mathjax >}}$$\mathbf{\vec v} = <5, 6, 7>$${{< /mathjax >}}

Le point de l’extrémité de la flèche du vecteur {{< mathjax >}}$$(B)$${{< /mathjax >}} est calculé en ajoutant les composants correspondants du point de référence et du vecteur {{< mathjax >}}$$\vec v$${{< /mathjax >}} :  

{{< mathjax >}}$$B = A + \mathbf{\vec v}$${{< /mathjax >}}  
{{< mathjax >}}$$B = (1+5, 2+6, 3+7) $${{< /mathjax >}}  
{{< mathjax >}}$$B = (6, 8, 10)$${{< /mathjax >}}  


<figure>
   <img src="/images/math-image172.png">
   <figcaption>Figure (2) : relation entre un vecteur, son point de référence et le point coïncidant avec la position de la pointe de la flèche.</figcaption>
</figure>  

{{< youtube ELQ8NgENhJY >}}
{{< youtube INtNgczxyWg >}}

### Vecteur de position

Une représentation vectorielle particulière utilise l'{{< mathjax >}}$$\text{origine} (0,0,0)$${{< /mathjax >}} comme point de référence du vecteur.
Le vecteur de position {{< mathjax >}}$$\mathbf{\vec v} = <a_1,a_2,a_3>$${{< /mathjax >}} est représenté par un segment de ligne entre deux points, l’rigine et le point B, de sorte que :  

{{< mathjax >}}$$\text{Origine} = (0,0,0)$${{< /mathjax >}}  
{{< mathjax >}}$$B = (a_1,a_2,a_3)$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image171.png">
   <figcaption>Figure (3) : Vecteur de position. Les coordonnées de l’extrémité de la flèche correspondent aux composants du vecteur.</figcaption>
</figure>  

{{< call-out note "Note" >}}

Un *vecteur de position* pour un vecteur donné {{< mathjax >}}$$\vec v= < a_1,a_2,a_3 >$${{< /mathjax >}} est une représentation particulière du segment de ligne, allant de l’origine {{< mathjax >}}$$(0,0,0)$${{< /mathjax >}} au point {{< mathjax >}}$$(a_1, a_2, a_3)$${{< /mathjax >}}.

{{< /call-out >}}

{{< youtube 8BNyMC4EBcw >}}

{{< youtube Ft2edI4g1qY >}}

### Vecteurs et points  

Attention à ne pas confondre vecteurs et points. Ces deux concepts sont différents. Les vecteurs, comme nous venons de le voir, représentent une quantité possédant une direction et une longueur, alors que les points indiquent une position. Par exemple, la direction du nord est un vecteur, alors que le pôle nord est une position (point).
Imaginons un vecteur et un point dont les composants sont identiques :  

{{< mathjax >}}$$\mathbf{\vec v} = <3,1,0>$${{< /mathjax >}}  
{{< mathjax >}}$$P = (3,1,0)$${{< /mathjax >}}  

Ce vecteur et ce point peuvent être dessinés ainsi :  

<figure>
   <img src="/images/math-image174.png">
   <figcaption>Figure (4) : Un vecteur définit une direction et une longueur. Un point définit une position.</figcaption>
</figure>  

{{< youtube RRrTz_QO_rA >}}

### Longueur d'un vecteur  

Comme mentionné auparavant, les vecteurs ont une longueur. Nous utiliserons la notation {{< mathjax >}}$$\vert a \vert$${{< /mathjax >}} pour représenter la longueur d’un vecteur {{< mathjax >}}$$ a $${{< /mathjax >}} donné. Par exemple :  

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = 5$${{< /mathjax >}}  

En règle générale, la longueur d’un vecteur {{< mathjax >}}$$\mathbf{\vec a} <a_1,a_2,a_3>$${{< /mathjax >}} est calculée de la façon suivante :

{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{(a_1)^2 + (a_2)^2 + (a_3)^2} $${{< /mathjax >}}

<figure>
   <img src="/images/math-image173.png">
   <figcaption>Figure (5) : Longueur d’un vecteur.</figcaption>
</figure>  

### Vecteur unitaire

Un vecteur unitaire est un vecteur dont la longueur est égale à une unité. Les vecteurs unitaires sont couramment utilisés pour comparer les directions de vecteurs.

{{< call-out note "Note" >}}

Un vecteur unitaire est un vecteur dont la longueur est égale à une unité.

{{< /call-out >}}

Pour calculer un vecteur unitaire, nous devons trouver la longueur d'un vecteur donné puis diviser les composants du vecteur par la longueur. Par exemple :

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec a} \vert  = 5 \text{ unités de long}$${{< /mathjax >}}  

Si {{< mathjax >}}$$\mathbf{\vec b} = \text{vecteur unitaire}$${{< /mathjax >}} de {{< mathjax >}}$$a$${{< /mathjax >}}, alors :  
&nbsp;&nbsp;     {{< mathjax >}}$$\mathbf{\vec b} = <4/5, 3/5, 0/5>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\mathbf{\vec b} = <0.8, 0.6, 0>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{0.8^2 + 0.6^2 + 0^2}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{0.64 + 0.36 + 0}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{(1)} = 1 \text{ unité de long}$${{< /mathjax >}}  

Par définition :  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  

Le vecteur unitaire de {{< mathjax >}}$$\mathbf{\vec a} = <a_1/\vert \mathbf{\vec a} \vert , a_2/\vert \mathbf{\vec a} \vert , a_3/\vert \mathbf{\vec a} \vert >$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image176.png">
   <figcaption>Figure (6) : Le vecteur unitaire est égal à une unité de longueur du vecteur.</figcaption>
</figure>  

{{< youtube yVSigpl3EUo >}}

## 1.2 Opérations sur les vecteurs

{{< youtube uInxocphhxI >}}

### Produit d'un vecteur par un scalaire

Le produit d'un vecteur par un scalaire revient à multiplier un vecteur par un nombre. Par exemple :  

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$2* \mathbf{\vec a} = <2*4, 2*3, 2*0>$${{< /mathjax >}}  
{{< mathjax >}}$$2*\mathbf{\vec a} = <8, 6, 0>$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image175.png">
   <figcaption>Figure (7) : Produit d’un vecteur par un scalaire</figcaption>
</figure>  

Soient un vecteur {{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}} et un nombre réel {{< mathjax >}}$$t$${{< /mathjax >}}   

{{< mathjax >}}$$t*\mathbf{\vec a} = < t* a_1, t* a_2, t* a_3 >$${{< /mathjax >}}  

{{< youtube S59M8BnDYAQ >}}

### Somme de deux vecteurs

La somme de deux vecteurs produit un troisième vecteur à partir de deux vecteurs de départ. Pour ajouter deux vecteurs, il faut ajouter leurs composants.

{{< call-out note "Note" >}}

Les vecteurs sont ajoutés en ajoutant leurs composants.

{{< /call-out >}}

Par exemple, soient deux vecteurs :  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 0> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <4, 1, 3> $${{< /mathjax >}}   
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <1+4, 2+1, 0+3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <5, 3, 3>$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image179.png">
   <figcaption>Figure (8) : Somme de deux vecteurs.
</figure>  

En général, la somme de deux vecteurs a et b est calculée de cette façon :  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <a_1+b_1, a_2+b_2, a_3+b_3>$${{< /mathjax >}}  

La somme de plusieurs vecteurs est utile pour trouver la direction moyenne de ces vecteurs. On utilise normalement pour cela des vecteurs de même longueur. Voici un exemple montrant la différence entre la somme de vecteurs de même longueur et la somme de vecteurs de différentes longueurs :  

<figure>
   <img src="/images/math-image177.png">
   <figcaption>Figure (9) : Somme de vecteurs de longueurs différentes (gauche). Somme de vecteurs de même longueur (droite) pour obtenir la direction moyenne.</figcaption>
</figure>  

Les vecteurs de départ ne seront probablement pas de même longueur. Afin de trouver la direction moyenne, vous devez utiliser le vecteur unitaire des vecteurs de départ. Comme indiqué précédemment, le vecteur unitaire est un vecteur dont la longueur est égale à 1.

{{< youtube VTVk3t3WeAY >}}

### Soustraction de vecteurs

La soustraction de deux vecteurs produit un troisième vecteur à partir de deux vecteurs de départ. Pour soustraire deux vecteurs, il faut soustraire les composants correspondants. Par exemple, soient deux vecteurs {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} et {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}, si on soustrait {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} de {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} alors :  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 0> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <4, 1, 4> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <1-4, 2-1, 0-4>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <-3, 1, -4> = \mathbf{\mathbf{\vec b}a}$${{< /mathjax >}}

Si on soustrait {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} de {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}, le résultat est différent :  

{{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a} = <4-1, 1-2, 4-0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a} = <3, -1, 4> = \mathbf{\mathbf{\vec a}b}$${{< /mathjax >}}  

Vous remarquerez que le vecteur {{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a}$${{< /mathjax >}} est de même longueur que le vecteur {{< mathjax >}}$$\mathbf{\vec a} - \mathbf{\vec b}$${{< /mathjax >}} mais leur direction est opposée.  

<figure>
   <img src="/images/math-image178.png">
   <figcaption>Figure (10) : Soustraction de vecteurs.</figcaption>
</figure>  

Soient deux vecteurs, {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} et {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}, alors par définition {{< mathjax >}}$$\mathbf{\vec a} - \mathbf{\vec b}$${{< /mathjax >}} est un vecteur calculé de cette façon :  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <a_1 - b_1, a_2 - b_2, a_3 - b_3> = \mathbf{\mathbf{\vec b}a}$${{< /mathjax >}}  

La soustraction de vecteurs est couramment utilisée pour trouver des vecteurs entre des points. Ainsi, pour trouver le vecteur allant de l'extrémité de la flèche du vecteur de position {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} jusqu’à l'extrémité de la flèche du vecteur de position {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, on utilise la soustraction de vecteurs {{< mathjax >}}$$(\mathbf{\vec a}-\mathbf{\vec b})$${{< /mathjax >}} comme indiqué sur la Figure (11).  

<figure>
   <img src="/images/math-image180.png">
   <figcaption>Figure (11) : Utiliser la soustraction de vecteurs pour trouver un vecteur entre deux points. </figcaption>
</figure> 

{{< youtube RQK8pCIWKNY >}} 

### Propriétés des vecteurs

Les vecteurs possèdent 8 propriétés. Si a, b et c sont des vecteurs, et s et t  des nombres, alors :  

{{< mathjax >}}$$\mathbf{\vec a} + \mathbf{\vec b} = \mathbf{\vec b} + \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + 0 = a$${{< /mathjax >}}  
{{< mathjax >}}$$s * (\mathbf{\vec a} + \mathbf{\vec b}) = s * a + s * \mathbf{\vec b}$${{< /mathjax >}}  
{{< mathjax >}}$$s * t * (\mathbf{\vec a}) = s * (t * \mathbf{\vec a})$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + (\mathbf{\vec b} + \mathbf{\vec c}) = (\mathbf{\vec a} + \mathbf{\vec b}) + \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + (-\mathbf{\vec a}) = 0$${{< /mathjax >}}  
{{< mathjax >}}$$(s + t) * \mathbf{\vec a} = s * \mathbf{\vec a} + t * \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$1 * \mathbf{\vec a} = \mathbf{\vec a}$${{< /mathjax >}}  

### Produit scalaire de vecteurs

Le produit scalaire de deux vecteurs génère un nombre à partir de deux vecteurs.
Par exemple, soient deux vecteurs a et b  :

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 3> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <5, 6, 7>$${{< /mathjax >}}  

Le produit scalaire de ces deux vecteurs est la somme de la multiplication des composants :  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = 1 * 5 + 2 * 6 + 3 * 7$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = 38$${{< /mathjax >}}  

Soient deux vecteurs a et b, par définition :  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = a_1 * b_1 + a_2 * b_2 + a_3 * b_3$${{< /mathjax >}}  

Le résultat d'un produit scalaire entre deux vecteurs est toujours un nombre positif si les deux vecteurs ont la même direction générale. Si la direction générale des deux vecteurs est opposée, alors le résultat du produit scalaire est négatif.

<figure>
   <img src="/images/math-image181.png">
   <figcaption>Figure (12) : Lorsque la direction de deux vecteurs est identique (gauche), le résultat du produit scalaire est un nombre positif. Lorsque la direction de deux vecteurs est opposée (gauche), le résultat du produit scalaire est un nombre négatif. </figcaption>
</figure>  

Le résultat du produit scalaire de deux vecteurs unitaires est toujours entre -1 et +1. Par exemple :  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <0,6, 0,8, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = (1 * 0.6, 0 * 0.8, 0 * 0) = 0.6$${{< /mathjax >}}  

De plus, le produit scalaire d'un vecteur par lui-même est égal à la longueur du vecteur puissance deux. Par exemple :  

{{< mathjax >}}$$\mathbf{\vec a} = <0, 3, 4>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = 0 * 0 + 3 * 3 + 4 * 4 $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = 25$${{< /mathjax >}}  

Calcul de la longueur au carré du vecteur {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} :  

{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = 5$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert 2 = 25$${{< /mathjax >}}  

### Produit scalaire de vecteurs, longueurs et angles

Il existe une relation entre le produit scalaire de deux vecteurs et l'angle entre les deux vecteurs.  

{{< call-out note "Note" >}}

Le produit scalaire de deux vecteurs unitaires non nuls est égal au cosinus de l’angle entre les deux vecteurs.

{{< /call-out >}}

Par définition :  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = \vert \mathbf{\vec a} \vert * \vert \mathbf{\vec b} \vert * cos(ө)$${{< /mathjax >}} , or  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} / (\vert \mathbf{\vec a} \vert * \vert \mathbf{\vec b} \vert) = cos(ө)$${{< /mathjax >}}

Où :  

{{< mathjax >}}$$ө$${{< /mathjax >}} est l’angle inclus entre les vecteurs.  

Si les vecteurs a et b sont des vecteurs unitaires, on peut dire que :  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = cos(ө)$${{< /mathjax >}}  

Et puisque le cosinus d'un angle de 90 degrés est égal à 0, on peut dire que :  

{{< call-out note "Note" >}}

Les vecteurs {{< mathjax >}}$$\vec a$${{< /mathjax >}} et {{< mathjax >}}$$\vec b$${{< /mathjax >}} sont orthogonaux si et seulement si {{< mathjax >}}$$\vec{a} \cdot  \vec{b} = 0$${{< /mathjax >}}.

{{< /call-out >}}

Par exemple, si on calcule le produit scalaire de deux vecteurs orthogonaux, l'axe des x et l'axe des y du repère général, le résultat sera égal à zéro.  

{{< mathjax >}}$$\mathbf{\vec x} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec y} = <0, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec x} · \mathbf{\vec y} = (1 * 0) + (0 * 1) + (0 * 0)$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec x} · \mathbf{\vec y} = 0$${{< /mathjax >}}  

Il existe également une relation entre le produit scalaire et la longueur de projection d'un vecteur sur un autre. Par exemple :  

{{< mathjax >}}$$\mathbf{\vec a} = <5, 2, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <9, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$(\mathbf{\vec b})unitaire = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b})unitaire = (5 * 1) + (2 * 0) + (0 * 0) $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b})unitaire = 2 (\text{qui est égal à la longueur de projection du vecteur a sur le vecteur b})$${{< /mathjax >}}

<figure>
   <img src="/images/math-image182.png">
   <figcaption>Figure (13) : Le produit scalaire est égal à la longueur de projection d'un vecteur sur un vecteur unitaire non nul. </figcaption>
</figure>  

Soient un vecteur a et un vecteur non nul b, par définition on peut calculer la longueur de projection pL du vecteur a sur le vecteur b en utilisant le produit scalaire.  

{{< mathjax >}}$$pL = \vert \mathbf{\vec a} \vert * cos(ө) $${{< /mathjax >}}  
{{< mathjax >}}$$pL = \mathbf{\vec a} · (\mathbf{\vec b})unitaire$${{< /mathjax >}} 

 {{< youtube ZsM2RQbVDf4 >}}

### Propriétés du produit scalaire

Soient les vecteurs {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} et {{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} et le nombre s, alors :  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = \vert  \mathbf{\vec a} \vert ^2$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b} + \mathbf{\vec c}) = \mathbf{\vec a} · \mathbf{\vec b} + \mathbf{\vec a} · \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$0 · \mathbf{\vec a} = 0$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = \mathbf{\vec b} · \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$(s * \mathbf{\vec a}) · \mathbf{\vec b} = s * (\mathbf{\vec a} · \mathbf{\vec b}) = \mathbf{\vec a} · (s * \mathbf{\vec b})$${{< /mathjax >}}  

### Produit vectoriel

Le produit vectoriel de deux vecteurs produit un troisième vecteur orthogonal aux deux vecteurs de départ.

<figure>
   <img src="/images/math-image183.png">
   <figcaption>Figure (14) : Calcul du produit vectoriel de deux vecteurs. </figcaption>
</figure>  

Par exemple, si vous avez deux vecteurs reposant sur le plan xy du repère général, leur produit vectoriel est un vecteur perpendiculaire au plan xy dans la direction positive ou négative de l'axe des z du repère général. Par exemple :  

{{< mathjax >}}$$\mathbf{\vec a} = <3, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <1, 2, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = < (1 * 0 – 0 * 2), (0 * 1 - 3 * 0), (3 * 2 - 1 * 1) > $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <0, 0, 5>$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Le vecteur {{< mathjax >}}$$\vec a \x\vec b$${{< /mathjax >}} est orthogonal à {{< mathjax >}}$$\vec a$${{< /mathjax >}} et {{< mathjax >}}$$\vec b$${{< /mathjax >}}.

{{< /call-out >}}

Vous n'aurez probablement jamais à calculer un produit vectoriel de deux vecteurs à la main, mais si vous voulez savoir comment faire, continuez la lecture ; sinon vous pouvez ignorer cette section. Le produit vectoriel {{< mathjax >}}$$a × b$${{< /mathjax >}} est défini en utilisant des déterminants. Voici une illustration simple du calcul d'un déterminant en utilisant des vecteurs de base standards :  

{{< mathjax >}}$$ \color {red}{i} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$ \color {blue}{j} = <0,1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$ \color {green}{k} = <0, 0, 1>$${{< /mathjax >}}  

<img src="/images/math-image184.png">

Le produit vectoriel des deux vecteurs {{< mathjax >}}$$\mathbf{\vec a} = <a1, a2, a3>$${{< /mathjax >}} et {{< mathjax >}}$$\mathbf{\vec b} = <b1, b2, b3>$${{< /mathjax >}} est calculé ainsi en utilisant le tableau ci-dessus :  

{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = \color {red}{i (a_2 * b_3)} + \color {blue}{ j (a_3 * b_1)} + \color {green}{k(a_1 * b_2)} - \color {green}{k (a_2 * b_1)} - \color {red}{i (a_3 * b_2)} -\color {blue}{ j (a_1 * b_3)}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = \color {red}{i (a_2 * b_3 - a_3 * b_2)} + \color {blue}{j (a_3 * b_1 - a_1 * b_3)} +\color {green}{k (a_1 * b_2 - a_2 * b_1)}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <\color {red}{a_2 * b_3 – a_3 * b_2},  \color {blue}{a_3 * b_1 - a_1 * b_3},  \color {green}{a_1 * b_2 - a_2 * b_1} >$${{< /mathjax >}}  

{{< youtube I5WkhSo4p6o >}}

### Produit vectoriel et angle entre les vecteurs

Il existe une relation entre l'angle formé par deux vecteurs et la longueur du vecteur résultat du produit vectoriel. Plus l'angle est petit (sinus plus petit), plus le vecteur du produit vectoriel est court. L'ordre des opérandes est important dans un produit vectoriel. Par exemple :  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <0, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <0, 0, 1>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} × \mathbf{\vec a} = <0, 0, -1>$${{< /mathjax >}}  


<figure>
   <img src="/images/math-image185.png">
   <figcaption>Figure (15) : Relation entre l’angle formé par deux vecteurs et la longueur du vecteur résultat du produit vectoriel.</figcaption>
</figure>  

Dans le système de Rhino, la direction de {{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b}$${{< /mathjax >}} est donnée par la règle de la main droite (où {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} = index,{{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} = majeur et {{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b}$${{< /mathjax >}} = pouce).  

<img src="/images/math-image186.png" width="375px">  

Soit une paire de vecteurs 3D {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} et {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}, par définition :  

{{< mathjax >}}$$\vert \mathbf{\vec a} × \mathbf{\vec b} \vert  = \vert  \mathbf{\vec a} \vert  \vert  \mathbf{\vec b} \vert  sin(ө)$${{< /mathjax >}}  

Où :   

{{< mathjax >}}$$ө$${{< /mathjax >}} est l'angle inclus entre les vecteurs de position de {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} et {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}  

Si a et b sont des vecteurs unitaires, on peut alors simplement dire que la longueur de leur produit vectoriel est égale au sinus de l’angle qu’ils forment. En d’autres termes :  

{{< mathjax >}}$$\vert \mathbf{\vec a} × \mathbf{\vec b} \vert = sin(ө)$${{< /mathjax >}}  

Le produit vectoriel entre deux vecteurs nous aide à déterminer si deux vecteurs sont parallèles. En effet, le résultat est toujours égal à un vecteur nul.  

{{< call-out note "Note" >}}

Les vecteurs {{< mathjax >}}$$\vec a$${{< /mathjax >}} et {{< mathjax >}}$$\vec b$${{< /mathjax >}} sont parallèles si et seulement si {{< mathjax >}}$$a \x b = 0$${{< /mathjax >}}.

{{< /call-out >}}

### Propriétés du produit vectoriel

Soient les vecteurs {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} et {{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} et le nombre {{< mathjax >}}$$s$${{< /mathjax >}}, alors :  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = -\mathbf{\vec b} × \mathbf{\vec a}$${{< /mathjax >}}   
{{< mathjax >}}$$(s * \mathbf{\vec a}) × \mathbf{\vec b} = s * (\mathbf{\vec a} × \mathbf{\vec b}) = \mathbf{\vec a} × (s * \mathbf{\vec b})$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × (\mathbf{\vec b} + \mathbf{\vec c}) = \mathbf{\vec a} × \mathbf{\vec b} + \mathbf{\vec a} × \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$(\mathbf{\vec a} + \mathbf{\vec b}) × \mathbf{\vec c} = \mathbf{\vec a} × \mathbf{\vec c} + \mathbf{\vec b} × \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b} × \mathbf{\vec c}) = (\mathbf{\vec a} × \mathbf{\vec b}) · \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × (\mathbf{\vec b} × \mathbf{\vec c}) = (\mathbf{\vec a} · \mathbf{\vec c}) * \mathbf{\vec b} – (\mathbf{\vec a} · \mathbf{\vec b}) * \mathbf{\vec c}$${{< /mathjax >}}  

## 1.3 Équation vectorielle d’une ligne

L'équation vectorielle d'une ligne est utilisée dans les applications de modélisation 3D et en infographie.

<figure>
   <img src="/images/math-image187.png">
   <figcaption>Figure (16) : Équation vectorielle d’une ligne.</figcaption>
</figure>  

Si on connaît la direction d'une ligne et un point sur cette ligne, on peut alors trouver tous les autres points sur la ligne en utilisant des vecteurs :

{{< mathjax >}}$$\overline{L} = ligne$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec v} = <a, b, c>$${{< /mathjax >}} - vecteur unitaire définissant la direction de la ligne  
{{< mathjax >}}$$Q = (x_0, y_0, z_0)$${{< /mathjax >}} point sur la ligne  
{{< mathjax >}}$$P = (x, y, z)$${{< /mathjax >}} n’importe quel point sur la ligne  

On sait que :  

{{< mathjax >}}$$\mathbf{\vec a} = t *\mathbf{\vec v}$${{< /mathjax >}}   (2)  
{{< mathjax >}}$$\mathbf{\vec p} = \mathbf{\vec q} + \mathbf{\vec a}$${{< /mathjax >}}   (1)  

À partir de 1 et 2 :  

{{< mathjax >}}$$\mathbf{\vec p} = \mathbf{\vec q} + t * \mathbf{\vec v}$${{< /mathjax >}}  (3)   

Cependant, on peut écrire (3) ainsi :  

{{< mathjax >}}$$<x, y, z> = <x_0, y_0, z_0> + <t * a, t * b, t * c>$${{< /mathjax >}}  
{{< mathjax >}}$$<x, y, z> = <x_0 + t * a, y_0 + t * b, z_0 + t * c>$${{< /mathjax >}}  

Donc :  

{{< mathjax >}}$$x = x_0 + t * a$${{< /mathjax >}}  
{{< mathjax >}}$$y = y_0 + t * b$${{< /mathjax >}}  
{{< mathjax >}}$$z = z_0 + t * c$${{< /mathjax >}}  

Qui équivaut à :  

{{< mathjax >}}$$P = Q + t * \mathbf{\vec v}$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Soient un point {{< mathjax >}}$$Q$${{< /mathjax >}} et une direction {{< mathjax >}}$$\vec v$${{< /mathjax >}} sur une ligne, tout point {{< mathjax >}}$$P$${{< /mathjax >}} sur cette ligne peut être calculé en utilisant l’équation vectorielle d’une ligne {{< mathjax >}}$$P = Q + t * \vec v$${{< /mathjax >}} où {{< mathjax >}}$$t$${{< /mathjax >}} est un nombre.  

{{< /call-out >}}

Autre exemple courant, trouver le milieu entre deux points. La démonstration suivante montre comment trouver le milieu en utilisant l'équation vectorielle d'une ligne :  

{{< mathjax >}}$$\mathbf{\vec q}$${{< /mathjax >}} est le vecteur de position du point {{< mathjax >}}$$Q$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec p}$${{< /mathjax >}} est le vecteur de position du point {{< mathjax >}}$$P$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} est le vecteur allant de {{< mathjax >}}$$Q \rightarrow P$${{< /mathjax >}}  

À partir de la soustraction de vecteurs, on sait que :  

{{< mathjax >}}$$\mathbf{\vec a} = \mathbf{\vec p} - \mathbf{\vec q}$${{< /mathjax >}}  

À partir de l'équation de la ligne, on sait que :  

{{< mathjax >}}$$M = Q + t * \mathbf{\vec a}$${{< /mathjax >}}  

Et puisqu'on cherche le milieu, alors :  

{{< mathjax >}}$$t = 0.5$${{< /mathjax >}}  

On peut alors dire que :  

{{< mathjax >}}$$M = Q + 0.5 * \mathbf{\vec a}$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image159.png">
   <figcaption>Figure (17) : Trouver le milieu entre deux points.</figcaption>
</figure>  

Il est possible de trouver n'importe quel point entre {{< mathjax >}}$$Q$${{< /mathjax >}} et {{< mathjax >}}$$P$${{< /mathjax >}}  en changeant la valeur {{< mathjax >}}$$t$${{< /mathjax >}} entre 0 et 1 et en utilisant l'équation générale :  

{{< mathjax >}}$$M = Q + t * (P - Q)$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Soient deux points {{< mathjax >}}$$Q$${{< /mathjax >}} et {{< mathjax >}}$$P$${{< /mathjax >}}, tout point {{< mathjax >}}$$M$${{< /mathjax >}} se trouvant entre les deux points est calculé en utilisant l'équation {{< mathjax >}}$$M = Q + t * (P - Q)$${{< /mathjax >}} où t est un nombre compris entre 0 et 1.

{{< /call-out >}}

## 1.4 Équation vectorielle d’un plan

Un plan peut être défini par un point et un vecteur perpendiculaire au plan. Ce vecteur est normalement appelé la normale du plan. La normale pointe dans la direction supérieure du plan.  

On peut calculer la normale d'un plan lorsqu'on connaît trois points non linéaires sur le plan.   

Sur la Figure (18), soient :  

{{< mathjax >}}$$A$${{< /mathjax >}} = le premier point sur le plan  
{{< mathjax >}}$$B$${{< /mathjax >}} = le deuxième point sur le plan  
{{< mathjax >}}$$C$${{< /mathjax >}} = le troisième point sur le plan  

Et :  

{{< mathjax >}}$$\mathbf{\vec a} $${{< /mathjax >}} = un vecteur de position du point {{< mathjax >}}$$A$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} = un vecteur de position du point {{< mathjax >}}$$B$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} = un vecteur de position du point {{< mathjax >}}$$C$${{< /mathjax >}}  

On peut trouver le vecteur de la normale {{< mathjax >}}$$\mathbf{\vec n}$${{< /mathjax >}} ainsi :  

{{< mathjax >}}$$\mathbf{\vec n} = (\mathbf{\vec b} - \mathbf{\vec a}) × (\mathbf{\vec c} - \mathbf{\vec a})$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image160.png">
   <figcaption>Figure (18) : Vecteurs et plans</figcaption>
</figure>  

Il est également possible de dériver l'équation scalaire du plan en utilisant le produit scalaire des vecteurs :  

{{< mathjax >}}$$\mathbf{\vec n} · (\mathbf{\vec b} - \mathbf{\vec a}) = 0$${{< /mathjax >}}  

Si :  

{{< mathjax >}}$$\mathbf{\vec n} = <a, b, c>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <x, y, z>$${{< /mathjax >}}  
{{< mathjax >}}$$ \mathbf{\vec a} = <x_0, y_0, z_0>$${{< /mathjax >}}  

On peut alors développer ce qui précède :  

{{< mathjax >}}$$<a, b, c> · <x-x_0, y-y_0, z-z_0 > = 0$${{< /mathjax >}}  

La résolution du produit scalaire donne l'équation scalaire générale d'un plan :  

{{< mathjax >}}$$a * (x - x_0) + b * (y - y_0) + c * (z - z_0) = 0$${{< /mathjax >}}  

## 1.5 Tutoriels

Tous les concepts que nous avons vus dans ce chapitre sont directement applicables pour résoudre des problèmes de géométrie couramment rencontrés en modélisation. Vous trouverez ci-dessous des tutoriels pas à pas utilisant les concepts abordés dans ce chapitre dans Rhino et Grasshopper (GH).

### 1.5.1 Direction d’une face
Soient un point et une surface, comment déterminer si le point est devant ou derrière la surface ?  

**Données de départ :**  

1. une surface  
2. un point  

<img src="/images/math-image161.png">  

**Paramètres :**  

La direction de la face est définie par la direction normale de la surface. Nous aurons besoin des informations suivantes :  

* La direction normale de la surface au point le plus proche du point de départ.  
* La direction d'un vecteur à partir du point le plus proche du point de départ.  

Comparer les deux directions précédentes, si elles sont les mêmes, le point se trouve devant, sinon il se trouve derrière.  

**Solution :**  

1\. Trouver la position du point le plus proche sur la surface par rapport au point de départ en utilisant le composant Pull (Attirer). Ceci donnera la position uv du point le plus proche, qui peut ensuite être utilisée pour analyser la surface et trouver sa direction normale.  

<img src="/images/math-image162.png">  

2\. On peut maintenant utiliser le point le plus proche pour dessiner un vecteur dirigé vers le point de départ. On peut également dessiner :  

<img src="/images/math-image163.png">  

3\. Les deux vecteurs peuvent être comparés en utilisant le produit scalaire. Si le résultat est positif, le point se trouve devant la surface. Si le résultat est négatif, le point se trouve derrière la surface.  

<img src="/images/math-image164.png">  

Les étapes précédentes peuvent également être réalisées en utilisant un autre langage d'écriture de scripts. En utilisant le composant VB de Grasshopper :  

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

En utilisant le composant Python de Grasshopper avec RhinoScriptSyntax :

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



En utilisant le composant Python de Grasshopper avec RhinoCommon uniquement :

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



En utilisant le composant C# de Grasshopper :  

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

### 1.5.2 Décomposition d'une boîte  

Le tutoriel suivant montre comment décomposer une polysurface. Voici à quoi ressemble la boîte finale décomposée :   

<img src="/images/math-image15.jpg">  

**Données de départ :**  

Identifiez l'objet de départ, qui est une boîte. Nous utiliserons le paramètre Box de GH :

<img src="/images/math-image17.jpg">  

**Paramètres :**  

* Pensez à tous les paramètres dont nous avons besoin afin de réaliser ce tutoriel.  
* Le centre de la décomposition.  
* Les faces de la boîte que nous décomposons.  
* La direction dans laquelle chaque face est déplacée.   


<img src="/images/math-image19.jpg">  

Une fois les paramètres identifiés, il faut les assembler en articulant les étapes logiques afin d'obtenir la solution voulue.

**Solution :**

1\. Trouver le centre de la boîte en utilisant le composant **Box Properties** de GH :

<img src="/images/math-image21.png">  

2\. Extraire les faces de la boîte avec le composant **Deconstruct Brep** :

<img src="/images/math-image23.png">

3\. La direction dans laquelle les faces sont déplacées est la partie difficile. Il faut tout d'abord trouver le centre de chaque face puis définir la direction à partir du centre de la boîte vers le centre de chaque face comme suit :

<img src="/images/math-image25.png">

4\. Une fois tous les paramètres scriptés, on peut utiliser le composant **Move** pour déplacer les faces dans la bonne direction. Vérifiez juste que l'amplitude des vecteurs est définie correctement et vous pouvez lancer le processus.

<img src="/images/math-image27.png">

Les étapes précédentes peuvent également être réalisées en utilisant VB script, C# ou Python. Vous trouverez ci-après la solution avec ces langages de scripts.

En utilisant le composant VB de Grasshopper :

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
En utilisant le composant Python de Grasshopper avec RhinoCommon :

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

En utilisant le composant C# de Grasshopper :

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

### 1.5.3 Sphères tangentes

Ce tutoriel montrera comment créer deux sphères tangentes entre deux points de départ.
Voici à quoi ressemble le résultat :

<img src="/images/math-image5.png">

**Données de départ :**  
Deux points ({{< mathjax >}}$$A$${{< /mathjax >}} et {{< mathjax >}}$$B$${{< /mathjax >}}) dans le repère 3D.

<img src="/images/math-image6.png">

Paramètres :
Voici la liste des paramètres dont nous avons besoin pour résoudre ce problème :
{{< mathjax >}}$$Un$${{< /mathjax >}} point {{< mathjax >}}$$D$${{< /mathjax >}} tangent aux deux sphères, au niveau d'un paramètre {{< mathjax >}}$$t$${{< /mathjax >}} (0-1) entre les points {{< mathjax >}}$$A$${{< /mathjax >}} et {{< mathjax >}}$$B$${{< /mathjax >}}.

* Le centre de la première sphère ou le milieu {{< mathjax >}}$$C1$${{< /mathjax >}} entre {{< mathjax >}}$$A$${{< /mathjax >}} et {{< mathjax >}}$$D$${{< /mathjax >}}.  
* Le centre de la deuxième sphère ou le milieu {{< mathjax >}}$$C2$${{< /mathjax >}} entre {{< mathjax >}}$$D$${{< /mathjax >}} et {{< mathjax >}}$$B$${{< /mathjax >}}.  
* Le rayon de la première sphère {{< mathjax >}}$$(r1)$${{< /mathjax >}} ou la distance entre {{< mathjax >}}$$A$${{< /mathjax >}} et {{< mathjax >}}$$C1$${{< /mathjax >}}.  
* Le rayon de la deuxième sphère {{< mathjax >}}$$(r2)$${{< /mathjax >}} ou la distance entre {{< mathjax >}}$$D$${{< /mathjax >}} et {{< mathjax >}}$$C2$${{< /mathjax >}}.  

**Solution :**

1\. Utilisez le composant **Expression** pour définir le point {{< mathjax >}}$$D$${{< /mathjax >}} entre {{< mathjax >}}$$A$${{< /mathjax >}} et {{< mathjax >}}$$B$${{< /mathjax >}} au niveau d’un paramètre {{< mathjax >}}$$t$${{< /mathjax >}}. L’expression que nous utiliserons est basée sur l’équation vectorielle d’une ligne :  

{{< mathjax >}}$$D = A + t*(B-A)$${{< /mathjax >}}  

{{< mathjax >}}$$B-A$${{< /mathjax >}} est le vecteur qui va du point {{< mathjax >}}$$A$${{< /mathjax >}} au point {{< mathjax >}}$$B$${{< /mathjax >}} en utilisant l’opération de soustraction de vecteurs.  

{{< mathjax >}}$$t*(B-A)$${{< /mathjax >}} : où {{< mathjax >}}$$t$${{< /mathjax >}} se trouve entre 0 et 1 pour obtenir une position sur le vecteur.  

{{< mathjax >}}$$A+t*(B-A)$${{< /mathjax >}} : donne un point sur le vecteur entre A et B.  

<img src="/images/math-image8.png">

2\. Utilisez le composant Expression pour définir également les milieux {{< mathjax >}}$$C1$${{< /mathjax >}} et {{< mathjax >}}$$C2$${{< /mathjax >}}.  

<img src="/images/math-image9.png">  

3\. Le rayon de la première sphère {{< mathjax >}}$$(r1)$${{< /mathjax >}} et le rayon de la deuxième sphère {{< mathjax >}}$$(r2)$${{< /mathjax >}} peuvent être calculés en utilisant le composant **Distance**.  

<img src="/images/math-image10.png">  

4\. L'étape finale consiste à créer la sphère à partir d'un plan de base et d'un rayon. Nous devons vérifier que les origines sont verrouillées sur {{< mathjax >}}$$C1$${{< /mathjax >}} et {{< mathjax >}}$$C2$${{< /mathjax >}} et les rayons sur {{< mathjax >}}$$r1$${{< /mathjax >}} et {{< mathjax >}}$$r2$${{< /mathjax >}}.  

<img src="/images/math-image54.png">  

**En utilisant le composant VB de Grasshopper :**  

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

En utilisant le composant Python :

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

En utilisant le composant C# de Grasshopper :

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

## Téléchargement de fichiers d’exemple

Téléchargez le fichier [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6/essentialmathematics/) [Fondements mathématiques](https://www.rhino3d.com/download/rhino/6/essentialmathematics/), qui contient tous les exemples de Grasshopper et les fichiers de code de ce guide.

## Étapes suivantes

Maintenant que vous avez vu les mathématiques vectorielles, consultez le guide [Matrices et transformations](/guides/general/essential-mathematics/matrices-transformations/) pour en apprendre davantage sur le déplacement, la rotation et la mise à l’échelle des objets.

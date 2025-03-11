+++
aliases = ["/en/5/guides/general/essential-mathematics/matrices-transformations/", "/en/6/guides/general/essential-mathematics/matrices-transformations/", "/en/7/guides/general/essential-mathematics/matrices-transformations/", "/en/wip/guides/general/essential-mathematics/matrices-transformations/"]
authors = [ "rajaa" ]
categories = [ "Essential Mathematics" ]
category_page = "guides/general/essential-mathematics/"
description = "Ce guide passe en revue les opérations et les transformations matricielles."
keywords = [ "mathematics", "geometry", "grasshopper3d" ]
languages = "unset"
sdk = [ "General" ]
title = "2 Matrices et transformations"
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

Les *transformations* correspondent aux opérations telles que le déplacement (également appelé *translation*), la rotation et le changement d’échelle d’objets. Elles sont enregistrées en programmation 3D à l’aide de matrices, qui sont tout simplement des tableaux rectangulaires de nombres. Les matrices peuvent être utilisées pour appliquer très rapidement plusieurs transformations. En effet, une matrice [4x4] peut représenter toutes les transformations. L’utilisation d’une taille de matrice unique pour toutes les transformations permet de réduire les temps de calcul.

{{< mathjax >}}$$\begin{array}{rcc} \mbox{matrice}&\begin{array}{cccc} c1& c2&c3&c4\end{array}\\\begin{array}{c}ligne(1)\\ligne(2)\\ligne(3)\\ligne(4)\end{array}& \left[\begin{array}{cr} +&+&+&+\\  +&+&+&+\\ +&+&+&+\\ +&+&+&+\end{array}\right] \end{array}$${{< /mathjax >}}

## 2.1 Opérations matricielles

L’opération la plus importante en infographie est le produit matriciel. Nous l’expliquerons de manière détaillée ici.

### Produit matriciel

Le produit matriciel est utilisé pour appliquer des transformations sur une géométrie. Par exemple, afin de faire tourner un point autour d’un axe, on peut utiliser une matrice de rotation et la multiplier par le point.


{{< mathjax >}}$$\begin{array}{ccc} \text{matrice de rotation} & \text{point d’entrée}  & \text{point de rotation}\\\begin{bmatrix}a & b & c & d \\e & f & g & h \\i & j & k & l \\0 & 0 & 0 & 1 \\\end{bmatrix}& \cdot\begin{bmatrix}x \\y\\z\\1 \\\end{bmatrix}&= \begin{bmatrix}x' \\y'\\z'\\1 \\\end{bmatrix}\end{array}$${{< /mathjax >}}    

La plupart du temps, plusieurs transformations doivent être appliquées à la même géométrie. Par exemple, pour déplacer et faire pivoter des milliers de points, on peut utiliser une des méthodes suivantes :

**Méthode 1**  

1. Multiplier la matrice de déplacement par les 1 000 points pour les déplacer.
2. Multiplier la matrice de rotation par les 1 000 points obtenus afin de les faire pivoter.  

Nombre d’opérations = **2 000**.  

**Méthode 2**  

1. Multiplier les matrices de rotation et de déplacement pour créer une matrice de transformation combinée.
2. Multiplier la matrice combinée par les 1 000 points pour les déplacer et les faire pivoter en une seule opération.

Nombre d’opérations = **1 001**.

La première méthode nécessite presque deux fois plus d’opérations pour arriver au même résultat. Même si la deuxième méthode est plus efficace, elle n’est possible que si les deux matrices sont {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}}. C’est pour cette raison que toutes les transformations sont représentées par des matrices {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}} en infographie alors que les points sont représentés par une matrice {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}}.

Les applications de modélisation en trois dimensions possèdent des outils pour appliquer des transformations et multiplier des matrices, mais si vous voulez savoir comment multiplier des matrices en mathématiques, voici un exemple simple : Afin de pouvoir multiplier deux matrices, leurs dimensions doivent correspondre. Ainsi, le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième matrice. La matrice résultante possède autant de lignes que la première matrice et autant de colonnes que la deuxième. Par exemple, soient deux matrices {{< mathjax >}}$$M$${{< /mathjax >}} et {{< mathjax >}}$$P$${{< /mathjax >}}, de dimensions {{< mathjax >}}$$[4\times 4]$${{< /mathjax >}} et {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}}  respectivement, les dimensions de la matrice résultant du produit {{< mathjax >}}$$M · P$${{< /mathjax >}} seront de  {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}} comme le montre l’illustration suivante :

{{< mathjax >}}$$\begin{array}{ccc} M & P  & P' \\\begin{bmatrix}\color{red}{a} & \color{red}{b}  & \color{red}{c} & \color{red}{d}  \\e & f & g & h \\i & j & k & l \\0 & 0 & 0 & 1 \\\end{bmatrix}& \cdot\begin{bmatrix}\color{red}{x} \\\color{red}{y} \\\color{red}{z} \\\color{red}{1}  \\\end{bmatrix}&= \begin{bmatrix}\color{red}{x'=a*x+b*y+c*z+d*1}\\y'=e*x+f*y+g*z+h*1\\z'=i*x+j*y+k*z+l*1 \\1=0*x+0*y+0*z+1*1\\\end{bmatrix}\end{array}$${{< /mathjax >}}    

### Matrice identité

La matrice identité est une matrice spéciale dont tous les composants de la diagonale sont 1 et les autres 0.

<img src="/images/math-image68.png">

La principale propriété d’une matrice identité est le fait que les valeurs multipliées par zéro ne changent pas lorsqu’elle est multipliée par une autre matrice.

<img src="/images/math-image52.png">

## 2.2 Opérations de transformation

La plupart des transformations conservent les relations de parallélisme entre les éléments de géométrie. Les points colinéaires restent colinéaires après la transformation par exemple. Les points se trouvant sur un même plan restent également coplanaires après la transformation. Ce type de transformation est appelé une *transformation affine*.  

### Transformation de translation (déplacement)

Le déplacement d’un point depuis une position de départ selon un vecteur peut être calculé ainsi :

{{< mathjax >}}$$P' = P + \mathbf{\vec v}$${{< /mathjax >}}  

{{< image url="/images/math-image35.png" alt="/images/math-image35.png" class="float_right" width="275" >}}   

Soit :  
&nbsp; {{< mathjax >}}$$P(x,y,z)$${{< /mathjax >}} un point donné  
&nbsp; {{< mathjax >}}$$\mathbf{\vec v}=<a,b,c>$${{< /mathjax >}} un vecteur de translation  
Alors :  
&nbsp; {{< mathjax >}}$$P'(x) = x + a$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'(y) = y + b$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'(z) = z + c$${{< /mathjax >}}  

{{< div class="clear_both" />}}  

Les points sont représentés dans une matrice [4x1] avec un 1 dans la dernière ligne. Le point P(x,y,z) par exemple est représenté ainsi :

{{< mathjax >}}$$\begin{bmatrix}x\\y\\z\\1\\\end{bmatrix}$${{< /mathjax >}}   

L’utilisation d’une matrice {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}} pour les transformations (appelée système de coordonnées homogènes), au lieu d’une matrice {{< mathjax >}}$$[3 \times 3]$${{< /mathjax >}}, permet de représenter toutes les transformations, y compris la translation. Format général d’une matrice de translation :  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 &  \color{red}{a1} \\0 & 1 & 0 & \color{red}{a2} \\0 & 0 & 1 &  \color{red}{a3} \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

Par exemple, si le point {{< mathjax >}}$$P(2,3,1)$${{< /mathjax >}} est déplacé selon le vecteur {{< mathjax >}}$$\vec v <2,2,2>$${{< /mathjax >}}, sa nouvelle position sera :

{{< mathjax >}}$$P’ = P + \mathbf{\vec v} = (2+2, 3+2, 1+2) = (4, 5, 3)$${{< /mathjax >}}  

En utilisant la forme matricielle et en multipliant la matrice de translation par le point de départ, la nouvelle position du point est déterminée ainsi :

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 2 \\0 & 1 & 0 & 2 \\0 & 0 & 1 & 2 \\0 & 0 & 0 & 1 \\\end{bmatrix}\cdot\begin{bmatrix}2 \\3\\1\\1 \\\end{bmatrix}= \begin{bmatrix}(1*2 + 0*3 + 0*1 + 2*1) \\(0*2 + 1*3 + 0*1 + 2*1)\\(0*2 + 0*3 + 1*1 + 2*1)\\(0*2 + 0*3 + 0*1 + 1*1)\\\end{bmatrix}=\begin{bmatrix}4 \\5\\3\\1 \\\end{bmatrix}$${{< /mathjax >}}   

De même, la translation d’une géométrie quelconque peut se faire en multipliant ses points de construction par la matrice de translation. Par exemple, étant donnée une boîte définie par huit sommets que l’on veut déplacer de 4 unités dans la direction x, 5 unités dans la direction y et 3 unités dans la direction z, on doit multiplier chacun des huit sommets par la matrice de translation suivante pour obtenir la nouvelle boîte :  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 4\\ 0 & 1 & 0 & 5 \\0 & 0 & 1 & 3 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

<figure>
   <img src="/images/math-image37.png">
   <figcaption>Figure (19) : Translation des sommets de la boîte.<<figcaption>
</figure>  

### Transformation de rotation

Cette section montre comment calculer la rotation autour de l’axe des z et de l’origine en utilisant la trigonométrie puis comment déduire le format général de la matrice de rotation.

{{< image url="/images/math-image39.png" alt="/images/math-image39.png" class="float_right" width="275" >}}   

Prenons un point {{< mathjax >}}$$P(x,y)$${{< /mathjax >}} sur le plan {{< mathjax >}}$$x,y$${{< /mathjax >}} et une rotation par l’angle ({{< mathjax >}}$$b$${{< /mathjax >}}).  À partir de la figure on peut dire que :  

&nbsp; {{< mathjax >}}$$x = d cos(a)$${{< /mathjax >}}   (1)  
&nbsp; {{< mathjax >}}$$y = d sin(a)$${{< /mathjax >}}    (2)  
&nbsp; {{< mathjax >}}$$x' = d cos(b+a)$${{< /mathjax >}}  (3)  
&nbsp; {{< mathjax >}}$$y' = d sin(b+a)$${{< /mathjax >}}   (4)  
En développant {{< mathjax >}}$$x$${{< /mathjax >}}' et {{< mathjax >}}$$y'$${{< /mathjax >}} à l’aide des identités trigonométriques pour le sinus et le cosinus de la somme des angles :  
&nbsp; {{< mathjax >}}$$x' = d cos(a)cos(b) - d sin(a)sin(b)$${{< /mathjax >}}  (5)  
&nbsp; {{< mathjax >}}$$y' = d cos(a)sin(b) + d sin(a)cos(b)$${{< /mathjax >}}  (6)  
En utilisant les équations 1 et 2 :  
&nbsp; {{< mathjax >}}$$x' = x cos(b) - y sin(b)$${{< /mathjax >}}  
&nbsp; y' = x sin(b) + y cos(b)  

La matrice de rotation autour de l’**axe des z** devient :  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{\cos{b}} & \color{red}{-\sin{b}} & 0 & 0 \\\color{red}{\sin{b}} & \color{red}{\cos{b}} & 0 & 0 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

La matrice de rotation autour de l’**axe des x** selon l’angle {{< mathjax >}}$$b$${{< /mathjax >}} devient :  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 0 \\0 & \color{red}{\cos{b}} & \color{red}{-\sin{b}} & 0 \\0 & \color{red}{\sin{b}} & \color{red}{\cos{b}} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

La matrice de rotation autour de l’**axe des y** selon l’angle {{< mathjax >}}$$b$${{< /mathjax >}} devient :  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{\cos{b}} &0 & \color{red}{\sin{b}} & 0 \\0 & 1 & 0 & 0 \\\color{red}{-\sin{b}} & 0 &\color{red}{\cos{b}} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

Par exemple, si on veut faire pivoter une boîte de 30 degrés, on doit :  

1\. Construire la matrice de rotation de 30 degrés. À l’aide de la forme générale et des valeurs du cosinus et du sinus de l’angle de 30 degrés, la matrice de rotation deviendra :  

{{< mathjax >}}$$\begin{bmatrix}0.87 & -0.5 & 0 & 0 \\0.5 & 0.87 & 0 & 0 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

2\. Multiplier la matrice de rotation par la géométrie de départ ou, dans le cas d’une boîte, par chaque sommet pour trouver la nouvelle position de la boîte.  

<figure>
   <img src="/images/math-image41.png">
   <figcaption>Figure (20) : Rotation d’une géométrie.</figcaption>
</figure>  

### Changement d’échelle

Afin de changer l’échelle d’une géométrie, nous avons besoin d’un facteur d’échelle et d’un point de référence. Le facteur d’échelle peut définir une échelle uniforme dans les directions x, y et z ou être différent pour chaque dimension.   

L’échelle d’un point peut utiliser l’équation suivante :  

&nbsp; {{< mathjax >}}$$P' = FacteurÉchelle(S) * P$${{< /mathjax >}}  

Ou :  

&nbsp; {{< mathjax >}}$$P'.x = Sx * P.x$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'.y = Sy * P.y$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'.z = Sz * P.z$${{< /mathjax >}}  

Cette matrice correspond à une transformation de changement d’échelle dont le centre est l’origine du repère général (0,0,0).  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{Échelle-x} & 0 & 0 & 0 \\0 & \color{red}{Échelle-y} & 0 & 0 \\0 & 0 & \color{red}{Échelle-z} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}  

Par exemple, si l’on veut appliquer une échelle de 0,25 à une boîte par rapport à l’origine du repère général, la matrice de l’échelle deviendra :

<figure>
   <img src="/images/math-image43.png">
   <figcaption>Figure (21) : Changement d’échelle d’une géométrie</figcaption>
</figure>  

### Transformation de cisaillement  

Le cisaillement en 3D est mesuré le long de deux axes par rapport à un troisième axe. Par exemple, un cisaillement le long de l’axe des z ne modifiera pas la géométrie le long de cet axe mais le fera sur les axes x et y. Voici quelques exemples de matrices de cisaillement :

1\. Cisaillement sur x et z avec conservation de la coordonnée y :


{{< image url="/images/math-image45.png" alt="/images/math-image45.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 &\color{red}{0.5} & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image47.png" alt="/images/math-image47.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 &\color{red}{0.5} & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

2\. Cisaillement sur y et z avec conservation de la coordonnée x :  


{{< image url="/images/math-image49.png" alt="/images/math-image49.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 & \color{red}{0.5} & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image50.png" alt="/images/math-image50.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & \color{red}{0.5} & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

3\. Cisaillement sur x et y avec conservation de la coordonnée z :

{{< image url="/images/math-image32.png" alt="/images/math-image32.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & \color{red}{0.5} & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image33.png" alt="/images/math-image33.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & \color{red}{0.5} & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

### Transformation de symétrie et réflexion

La transformation de symétrie crée le reflet d’un objet par rapport à une ligne ou à un plan. Les objets 2D sont reflétés par rapport à une ligne alors que les objets 3D sont reflétés par rapport à un plan. N’oubliez pas que la transformation de symétrie inverse la direction normale des faces de la géométrie.  

<figure>
   <img src="/images/math-image98.png">
   <figcaption>Figure (23) : Matrice de symétrie sur le plan XY du repère général. Les directions des faces sont inversées.<<figcaption>
</figure>  

### Transformation de projection plane

Intuitivement, le point de projection d’un point 3D donné {{< mathjax >}}$$P(x,y,z)$${{< /mathjax >}} dans le plan xy du repère général correspond à {{< mathjax >}}$$P_{xy} (x,y,0)$${{< /mathjax >}}, avec la valeur z définie sur zéro. De même, une projection sur le plan xz d’un point P devient {{< mathjax >}}$$P_{xz}(x,0,z)$${{< /mathjax >}}. Lors de la projection sur le plan yz, {{< mathjax >}}$$P_{xz} = (0,y,z)$${{< /mathjax >}}. Ces transformations sont appelées projections orthogonales.   

Si l’objet de départ est une courbe à laquelle on applique une transformation de projection plane, on obtient une courbe projetée sur ce plan. L’exemple suivant montre la projection d’une courbe sur le plan xy en utilisant une matrice.  

Remarque : Les courbes NURBS (expliquées dans le chapitre suivant) utilisent des points de contrôle pour leur définition. La projection d’une courbe revient à projeter ses points de contrôle.  

{{< image url="/images/math-image100.png" alt="/images/math-image100.png" class="float_left" width="175" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & \color{red}{0.0} & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< image url="/images/math-image102.png" alt="/images/math-image102.png" class="float_left" width="175" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & \color{red}{0.0} & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< image url="/images/math-image104.png" alt="/images/math-image104.png" class="float_left" width="175" >}}    

{{< mathjax >}}$$\begin{bmatrix} \color{red}{0.0} & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

## Téléchargement de fichiers d’exemple

Téléchargez le fichier [{{< awesome "fas fa-download">}} ](/files/math-samplesandtutorials.zip.zip) [math-samplesandtutorials.zip](/files/math-samplesandtutorials.zip), qui contient tous les exemples de Grasshopper et les fichiers de code de ce guide.

## Étapes suivantes

Maintenant que vous en savez plus sur les matrices et la transformation, consultez le guide [Courbes et surfaces paramétriques](/guides/general/essential-mathematics/parametric-curves-surfaces/) pour en savoir plus sur la structure détaillée des courbes et surfaces NURBS.  

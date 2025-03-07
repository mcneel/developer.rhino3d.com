+++
aliases = ["/en/5/guides/general/essential-mathematics/", "/en/6/guides/general/essential-mathematics/", "/en/7/guides/general/essential-mathematics/", "/en/wip/guides/general/essential-mathematics/"]
authors = [ "rajaa" ]
categories = [ "General" ]
description = "Introduit les professionnels du design aux concepts mathématiques de base pour le développement efficace de modèles 3D computationnels."
keywords = [ "rhino", "developer" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "General" ]
title = "Mathématiques fondamentales pour le design computationnel"
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

*Mathématiques fondamentales pour le design computationnel* introduit les professionnels du design aux concepts mathématiques fondamentaux dont ils auront besoin pour développer efficacement des méthodes de calcul pour la modélisation 3D et l’imagerie de synthèse. L’objectif de cet ouvrage n’est pas d’être exhaustif mais plutôt de présenter les bases et les concepts les plus souvent utilisés. Il est destiné aux concepteurs possédant peu, voire aucune, connaissance en mathématiques au-delà du lycée. Tous les concepts sont expliqués visuellement en utilisant [Grasshopper® (GH)](https://www.grasshopper3d.com), l’environnement de modélisation générative pour [Rhinoceros® (Rhino)](https://www.rhino3d.com).  

Le contenu est divisé en trois chapitres. Le [Chapitre 1](/guides/general/essential-mathematics/vector-mathematics/) aborde les mathématiques vectorielles avec la représentation vectorielle, les opérations vectorielles ainsi que les équations des lignes et plans. Le [Chapitre 2](/guides/general/essential-mathematics/matrices-transformations/) traite des opérations et transformations matricielles. Enfin, le [Chapitre 3](/guides/general/essential-mathematics/parametric-curves-surfaces/) étudie en détails les courbes paramétriques en s’attardant plus particulièrement sur les courbes NURBS et les concepts de continuité et de courbure.  Il couvre également les surfaces et polysurfaces NURBS.

*Je voudrai remercier [Dr. Dale Lear](https://discourse.mcneel.com/u/dalelear/activity) de Robert McNeel & Associates pour son excellente relecture approfondie. Ses précieux commentaires ont été indispensables à la production de cette édition. Je tiens également à remercier Mme [Margaret Becker](https://discourse.mcneel.com/u/margaret/activity) de Robert McNeel & Associates pour sa révision du point de vue de la rédaction technique et de la mise en forme du document.*

{{< /column >}}  
</div>  

<div class="row">  
<div class="col-md-12" markdown="1">  

***[Rajaa Issa](https://discourse.mcneel.com/u/rajaa/activity)***

Robert McNeel & Associates

#### Téléchargements :
* [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6/essentialmathematics) [Téléchargez le guide PDF et tous les exemples Grasshopper (4ème édition)](https://www.rhino3d.com/download/rhino/6/essentialmathematics/) en anglais, français, allemand, espagnol, italien ou chinois simplifié.
* <a href="https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK"><span class="glyphicon glyphicon-play"></span></a> [Regardez les vidéos sur les Mathématiques fondamentales... ](https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK)

### Table des matières  

</div>  
</div>  

{{< row >}}  
{{< column >}}  

### 1. [Mathématiques vectorielles](/guides/general/essential-mathematics/vector-mathematics/)

   1.1 [Représentation vectorielle](/guides/general/essential-mathematics/vector-mathematics/#11-vector-representation)  
&nbsp;&nbsp; Vecteur de position   
&nbsp;&nbsp; Vecteurs et points   
&nbsp;&nbsp; Longueur d’un vecteur   
&nbsp;&nbsp; Vecteur unitaire    

   1.2 [Opérations sur les vecteurs](/guides/general/essential-mathematics/vector-mathematics/#12-vector-operations)  
&nbsp;&nbsp; Produit d’un vecteur par un scalaire   
&nbsp;&nbsp; Somme de deux vecteurs    
&nbsp;&nbsp; Soustraction de vecteurs   
&nbsp;&nbsp; Propriétés des vecteurs  
&nbsp;&nbsp; Produit scalaire de vecteurs   
&nbsp;&nbsp; Produit scalaire de vecteurs, longueurs et angles    
&nbsp;&nbsp; Propriétés du produit scalaire    
&nbsp;&nbsp; Produit vectoriel   
&nbsp;&nbsp; Produit vectoriel et angle entre les vecteurs    
&nbsp;&nbsp; Propriétés du produit vectoriel   

   [1.3 Équation vectorielle d’une ligne](/guides/general/essential-mathematics/vector-mathematics/#13-vector-equation-of-line)  

   [1.4 Équation vectorielle d’un plan](/guides/general/essential-mathematics/vector-mathematics/#14-vector-equation-of-a-plane)  

   1.5 [Tutoriels](/guides/general/essential-mathematics/vector-mathematics/#15-tutorials)   
&nbsp;&nbsp; Direction d’une face  
&nbsp;&nbsp; Décomposition d’une boîte  
&nbsp;&nbsp; Sphères tangentes  

{{< /column >}}
{{< column >}} 

### 2. [Matrices et transformations](/guides/general/essential-mathematics/matrices-transformations/)
   2.1 [Opérations matricielles](/guides/general/essential-mathematics/matrices-transformations/#21-matrix-operations)  
&nbsp;&nbsp; Produit matriciel  
&nbsp;&nbsp; Matrice identité  

   2.2 [Opérations de transformation](/guides/general/essential-mathematics/matrices-transformations/#22-transformation-operations)  
&nbsp;&nbsp; Transformation de translation (déplacement)   
&nbsp;&nbsp; Transformation de rotation  
&nbsp;&nbsp; Changement d’échelle  
&nbsp;&nbsp; Transformation de cisaillement  
&nbsp;&nbsp; Transformation de symétrie et réflexion  
&nbsp;&nbsp; Transformation de projection plane  

{{< /column >}}
{{< column >}} 


### 3. [Courbes et surfaces paramétriques](/guides/general/essential-mathematics/parametric-curves-surfaces/)

   3.1 [Courbes paramétriques](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
&nbsp;&nbsp; Paramètre de la courbe  
&nbsp;&nbsp; Domaine ou intervalle de la courbe  
&nbsp;&nbsp; Évaluation d’une courbe  
&nbsp;&nbsp; Vecteur tangent à une courbe  
&nbsp;&nbsp; Courbes polynomiales cubiques  
&nbsp;&nbsp; Calcul des courbes de Bézier cubiques  

   3.2 [Courbes NURBS](/guides/general/essential-mathematics/parametric-curves-surfaces/#32-nurbs-curves)  
&nbsp;&nbsp; Degré  
&nbsp;&nbsp; Points de contrôle  
&nbsp;&nbsp; Poids des points de contrôle  
&nbsp;&nbsp; Nœuds  
&nbsp;&nbsp; Les nœuds sont des valeurs de paramètre  
&nbsp;&nbsp; Règle d’évaluation  
&nbsp;&nbsp; Caractéristiques des courbes NURBS  
&nbsp;&nbsp; Calcul des courbes NURBS  

   [3.3 Continuité géométrique d’une courbe](/guides/general/essential-mathematics/parametric-curves-surfaces/#33-curve-geometric-continuity)   

   3.4 [Courbure de la courbe](/guides/general/essential-mathematics/parametric-curves-surfaces/#34-curve-curvature)   

   3.5 [Surfaces paramétriques](/guides/general/essential-mathematics/parametric-curves-surfaces/#35-parametric-surfaces)   
&nbsp;&nbsp; Paramètres de surface  
&nbsp;&nbsp; Domaine de la surface  
&nbsp;&nbsp; Calcul de surface  
&nbsp;&nbsp; Plan tangent à une surface  

   [3.6 Continuité géométrique de surfaces](/guides/general/essential-mathematics/parametric-curves-surfaces/#36-surface-geometric-continuity)     

   3.7 [Courbure d’une surface](/guides/general/essential-mathematics/parametric-curves-surfaces/#37-surface-curvature)     
&nbsp;&nbsp; Courbures principales  
&nbsp;&nbsp; Courbure gaussienne  
&nbsp;&nbsp; Courbure moyenne  

   3.8 [Surfaces NURBS](/guides/general/essential-mathematics/parametric-curves-surfaces/#38-nurbs-surfaces)     
&nbsp;&nbsp; Caractéristiques des surfaces NURBS  
&nbsp;&nbsp; Singularité des surfaces NURBS  
&nbsp;&nbsp; Surfaces NURBS limitées  

   3.9 [Polysurfaces](/guides/general/essential-mathematics/parametric-curves-surfaces/#39-polysurfaces)     

   3.10 [Tutoriels](/guides/general/essential-mathematics/parametric-curves-surfaces/#310-tutorials)     
Continuité entre courbes  
&nbsp;&nbsp; Surfaces avec une singularité  

{{< /column >}}
{{< /row >}}

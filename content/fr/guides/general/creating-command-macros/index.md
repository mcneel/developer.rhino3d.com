+++
aliases = ["/en/5/guides/general/creating-command-macros/", "/en/6/guides/general/creating-command-macros/", "/en/7/guides/general/creating-command-macros/", "/en/wip/guides/general/creating-command-macros/"]
authors = [ "scottd" ]
categories = [ "Overview" ]
description = "Tutoriel de base sur l’écriture de macros (scriptage conjoint de plusieurs commandes de Rhino)"
keywords = [ "macro", "overview", "rhinoceros", "command" ]
languages = [ "Macro" ]
sdk = [ "Macro" ]
title = "Création de macros"
type = "guides"
weight = 1
override_last_modified = "2018-12-06T15:12:10Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/rhino/basicmacros"
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

Dans Rhino, vous pouvez créer des macros pour automatiser de nombreuses tâches, personnaliser vos commandes et améliorer vos méthodes de travail.

Le terme « scriptage » peut parfois prêter à confusion.  On l’emploie généralement pour décrire à la fois l’écriture de macros (le sujet de cet article) mais aussi de scripts plus sophistiqués dans [RhinoScript](/guides/rhinoscript/), [Rhino.Python](/guides/rhinopython/) ou d’autres langages de programmation.  

Ce sont en fait deux choses complètement différentes. Écrire des fonctions dans RhinoScript ou d’autres langages de programmation est bien plus complexe que de créer des macros et requiert des connaissances et des compétences en programmation.  Nous ne parlerons pas de ce sujet ici.

Nous utilisons ici le terme « macro » exclusivement pour décrire l’assemblage de chaînes de commandes normales de Rhino et de leurs options afin de créer une fonction automatisée.  Il s’agit ici du scriptage à son niveau le plus simple et il est facilement accesible à tous les utilisateurs de Rhino même ceux qui n’ont aucune connaissance en programmation.  Il suffit de comprendre les commandes de Rhino et leur structure, de raisonner logiquement et d’aimer faire des expériences et de la résolution d’erreurs.

#### De quels outils avez-vous besoin ?
1. Votre cerveau ;

2. Le fichier d’aide de Rhino qui liste toutes les commandes de Rhino et leurs options. C’est votre document de référence ;

3. L’**ÉditeurMacro** de Rhino, pour exécuter et déboguer facilement vos macros.


## Vous avez déjà utilisé une ou deux macros...
Tout d’abord, si vous êtes utilisateur de Rhino, vous ne le savez peut-être pas mais vous avez déjà utilisé des macros.  Dans Rhino, de nombreuses commandes sont déjà écrites sous forme de macros pour vous. Lorsque vous cliquez sur un bouton dans une barre d’outils ou sur une commande dans un menu, c’est souvent une macro prédéfinie.  Pour vous en rendre compte, cliquez du bouton droit sur le bouton **Extruder droit** tout en maintenant la touche Maj enfoncée :

![Extrude](/images/extrudecrvbuttoneditor.gif)

C’est le plus simple exemple de macro qui définit une série d’options à l’intérieur d’une seule commande afin que vous n’ayez pas à les indiquer à chaque fois que vous l’utilisez.  **ExtruderCourbe** a plusieurs boutons avec des options prédéfinies : **Dépouille, SuivreCourbe, VersPoint, Solide=Oui (ou Non)** etc.  Vérifiez les macros sous tous les boutons **ExtruderCourbe** pour voir comment elles sont organisées.

En un sens, cela revient au même que si vous cliquiez sur les boutons ou tapiez les options une par une dans la ligne de commandes.  En fait, les macros sont précisément cela : un ensemble d’instructions pour répéter une séquence de commandes que vous devriez autrement saisir manuellement une par une.

Le scriptage d’options pour une commande peut aussi être combiné avec la saisie de données (par exemple des coordonnées ou d’autres données numériques). Il est aussi possible d’enchaîner plusieurs commandes à la suite pour avoir une séquence automatisée d’événements afin de manipuler ou créer des objets.

**Remarque :** À quoi servent les tirets bas (_) ?  Le tiret bas prévient Rhino que la commande qui suit est en anglais (sans tenir compte de la langue dans laquelle vous utilisez le logiciel), ce qui fait que votre macro sera universelle.  Si vous utilisez Rhino en anglais, vous n’en avez pas besoin et vous pouvez éliminer tous les tirets bas de vos macros si vous le souhaitez. Cela n’aura aucune incidence.  Et à quoi sert le point d’exclamation (!) ?  Il annule toute commande précédente qui pourrait être en cours d’exécution ; c’est une mesure de sécurité.

## Bien démarrer

Imaginons que vous vouliez créer une série de boîtes de 10x10x10 en positionnant le centre de la base à l’endroit de votre choix, et que vous vouliez indiquer ce point d’insertion soit en cliquant avec la souris, soit en tapant les coordonnées au clavier.

Vous pourriez utiliser la commande Boîte standard (**Sommet à sommet + Hauteur**) mais par défaut le point d’insertion sera sur le premier sommet de la boîte.  Pour que le point d’insertion soit celui que nous voulons, il faut utiliser la commande Boîte, Centre.   C’est en fait tout simplement la commande Boîte avec l’option Centre et vous allez donc devoir l’activer dans votre macro.

Ouvrez l’**ÉditeurMacro** et tapez le texte suivant :

```
 ! _Box _Center
```

(C’est en fait la macro qui se trouve sous le bouton Boîte, Centre. Vous pouvez vérifier.) 
Toutes les entrées (mots et chiffres des commandes) doivent être séparées par un seul espace.

Nous devons à présent indiquer le point central.  Pour cela, vous allez dire à Rhino d’arrêter de traiter la commande temporairement et d’attendre une entrée sous la forme d’un clic ou d’une saisie au clavier.  Vous allez alors insérer la commande Pause.

```
 ! _Box _Center _Pause
```

Une fois les données saisies, vous pouvez indiquer la taille de la boîte directement dans la commande.  Étant donné que l’option Centre dans Boîte attend un sommet de la boîte en tant que deuxième entrée, vous pouvez indiquer ses coordonnées X et Y :

```
 ! _Box _Center _Pause r5,5
```

(Pourquoi le « r » ?  Les coordonnées du sommet de la boîte doivent être relatives au dernier point sélectionné, à savoir le centre de la base de la boîte.  Autrement, le sommet arriverait toujours sur X5, Y5.)

Vous pouvez maintenant indiquer la hauteur, qui dans ce cas est relative au point de départ d’origine.

```
 ! _Box _Center _Pause r5,5 10
```

Comme il n’y a pas d’autre entrée nécessaire et qu’il n’y a plus d’autres options possibles, la macro se termine et votre boîte est créée.  Notez que comme nous voulions une hauteur égale à la largeur, nous aurions aussi pu utiliser « _Enter » (Entrée) au lieu de 10 pour la dernière entrée.

```
 ! _Box _Center _Pause r5,5 _Enter
```

À présent que la macro fonctionne, [[rhino:macroscriptsetup|créez un nouveau bouton dans la barre d’outils]] et copiez la macro dedans. Donnez-lui un nom reconnaissable comme « Boîte centrée base 10x10x10 ».  Souvenez-vous qu’une fois que la macro est exécutée, cliquer du bouton droit de la souris répète toute la séquence de cette macro. Vous pouvez donc l’utiliser plusieurs fois de suite sans cliquer sur le bouton à chaque fois.

## Et maintenant, compliquons un peu les choses…

Certaines commandes appellent des boîtes de dialogue contenant de nombreuses options.  Normalement, votre macro s’arrête et attend que vous cliquiez sur les options de votre choix dans la boîte de dialogue, puis reprend.  Comme vous voulez automatiser le processus, vous pouvez sauter la boîte de dialogue en mettant un tiret haut (-) avant la commande.  Vous écrirez alors toutes vos options dans le script et la macro fonctionnera jusqu’à la fin sans que vous n’ayez à intervenir.  Certaines commandes ont plusieurs niveaux d’options.  Si vous voulez voir les différentes options disponibles, tapez la commande dans la ligne de commandes précédée du tiret haut et regardez quelles sont les options proposées.  Cliquez sur les options et voyez si elles ont des sous-options.

#### Créer une surface par sections à partir de deux courbes ouvertes

Imaginons que vous vouliez créer de manière répétitive une surface par sections à partir de deux courbes *OUVERTES*.  Si vous utilisez la commande `SurfaceParSections` standard, vous devrez à chaque fois passer par la boîte de dialogue.  Si vous utilisez la version `–Loft` (SurfaceParSections précédée du tiret), vous évitez cette étape et allez beaucoup plus vite.  Regardez par exemple :

```
_-Loft
_Pause
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Remarquez que lorsque vous appelez la commande, vous avez immédiatement une Pause pour sélectionner vos courbes.  Si vous supprimez la Pause, la macro ne fonctionnera pas à moins que vous n’ayez sélectionné vos courbes au préalable.  Si vous avez déjà présélectionné vos courbes, vous avez raison d’ignorer la Pause.  La commande est ensuite paramétrée avec toutes les options que vous avez indiquées. Une fois cette étape réalisée, elle crée la surface et se termine. Essayez cette macro avec deux courbes ouvertes, en les sélectionnant avant ou après.  Essayez de modifier une ou plusieurs options, par exemple de remplacer Fermée=Oui ou Simplifier=Reconstruire. (Pour cela vous devrez aussi ajouter une ligne avec Reconstruire=20 ou une autre valeur.)

#### Modifier cette macro pour l’utiliser avec des courbes fermées

Essayez à présent avec deux courbes fermées.  Vous avez un problème.  Pourquoi ? Pour les courbes fermées, SurfaceParSections a besoin que vous lui donniez une autre information : la position de la jointure.  Vous devez indiquer cette donnée dans la macro au bon endroit.  Vous pouvez donc soit choisir à partir de différentes options de jointures automatiques (qui sont dans un sous-niveau d’options) soit l’ajuster à l’écran.  Dans les deux cas, vous devrez modifier la macro.

Ajoutez une pause au bon endroit pour vérifier et ajuster la jointure à l’écran :

```
_-Loft
_Pause
_Pause  <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Si vous écrivez `Enter` au lieu de `Pause`, vous indiquez à Rhino que vous ne souhaitez rien spécifier. Que la jointure peut être laissée telle qu’elle est par défaut.

```
_-Loft
_Pause
_Enter  <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Ou, vous pouvez indiquer une autre option de jointure pour SurfaceParSections en descendant au niveau de la sous-option de jointure :

```
_-Loft
_Pause
_Natural  <--
_Enter    <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

(`Enter` après « Natural » est nécessaire pour sortir du niveau de l’option « jointure » et revenir au niveau des options de SurfaceParSections.)

Malheureusement, la même macro ne fonctionnera pas correctement pour les courbes ouvertes et fermées à cause de l’option jointure supplémentaire.  C’est l’une des limites du système de macros et de la manière dont certaines commandes de Rhino ont été écrites.


## Utiliser des macros pour définir rapidement les options de votre interface

Les macros peuvent aussi être utilisées pour définir automatiquement diverses options GUI et des propriétés du document sans avoir à naviguer dans la boîte de dialogue d’options.  J’utilise la macro suivante pour définir le maillage de rendu comme je le veux. (Notez bien le tiret haut avant -_DocumentProperties.)

```
-_DocumentProperties
_Mesh _Custom
_MaxAngle=0 _AspectRatio=0
_MinEdgeLength=0 _MaxEdgeLength=0
_MaxEdgeSrf=0.01 _GridQuads=16
_Refine=Yes _JaggedSeams=No
_SimplePlanes=No
_Enter
_Enter
```

Pourquoi y a-t-il deux fois « Entrée » à la fin ?

Vous êtes descendu deux niveaux dans -_DocumentProperties (PropriétésDocument), d’abord au niveau du Maillage, ensuite au sous-niveau Personnaliser (_Custom) dans Maillage.  Vous devez taper une fois sur Entrée pour quitter le sous-niveau et revenir au niveau principal, et une deuxième fois pour quitter la commande.  Dans certains scripts, vous aurez même besoin de trois « Entrée ».  

La macro suivante a été créée par Jeff LaSor, pour activer ou désactiver le pointeur en croix :

Pour ACTIVER ou DÉSACTIVER le pointeur en croix, écrivez la macro suivante pour un bouton :

```
  -_Options _Appearance _Visibility
  _Crosshairs _Enter _Enter _Enter
```
Vous constatez qu’il indique à chaque fois le nom de l’option et de la sous-option de la commande.  Les écrire dans le script revient à cliquer dessus avec la souris.  Remarquez aussi les trois « Entrée ».  Comme chaque option de la commande vous fait descendre dans un sous-niveau d’options de commande, vous devez écrire « _Enter » (Entrée) pour revenir au niveau supérieur.  Comme ce script est descendu de trois niveaux, la macro contient trois fois « Entrée » pour sortir complètement de la commande.

Ou, si vous utilisez tout simplement un point d’exclamation `!` à la fin (ce qui dans un script signifie « terminer maintenant ! »), vous ressortirez complètement de la commande, quel que soit le sous-niveau dans lequel vous vous trouvez. Attention : si vous voulez continuer votre macro avec autre chose, n’utilisez pas le point d’exclamation, mais plutôt Entrée, faute de quoi votre macro se terminera toujours au `!`.

Le script ACTIVE ou DÉSACTIVE simplement le pointeur en croix. Mais si vous voulez un script qui l’ACTIVE toujours et un autre qui le DÉSACTIVE toujours, voici à quoi cela ressemblerait :

Version toujours ACTIVÉ :

```
  -_Options _Appearance _Visibility
  _Crosshairs=_Show !
</code>
Version toujours DÉSACTIVÉ :
<code>
  -_Options _Appearance _Visibility
  _Crosshairs=_Hide !
```

Remarquez bien que nous utilisons un `!` ici. Remarquez aussi que vous pouvez assigner directement les valeurs disponibles pour les options en utilisant l’opérateur « = ».  L’option Pointeur en croix a deux valeurs possibles (« Afficher » (Show) et « Cacher » (Hide) et c’est donc ce qui est utilisé dans cette macro.

(Merci, Jeff)

## Autres outils et commandes utiles pour l’écriture de macros

Voici quelques astuces pratiques pour écrire des macros plus complexes.  La première consiste à utiliser avec discernement différents filtres de sélection, en particulier `SélDerniers` (qui sélectionne le dernier objet créé/transformé), `SélPréc` (qui sélectionne le dernier objet sélectionné) et `RienSélectionner` (qui désélectionne tout).  Vous pouvez aussi nommer des objets, les grouper (et nommer le groupe) pour ensuite les rappeler plus tard en utilisant le nom d’objet ou de groupe que vous avez défini.

```
_Select (Sélectionner)
_SelLast (SélDerniers)
_SelPrev (SélPréc)
_SelNone (RienSélectionner)
_SetObjectName (DéfinirNomObjet)
_SetGroupName (NommerGroupe)
_SelGroup (SélGroupe)
_SelName (SélNom)
_Group (Grouper)
_Ungroup (Dégrouper)
```

Pour définir le nom d’un seul objet (ce qui est déjà une macro !) :

```
  _Properties _Pause _Object _Name
  I[nsérez le nom de votre objet ici] _Enter _Enter
```

Pour annuler le nom d’un seul objet (sans supprimer l’objet)

```
  _Properties _Pause _Object _Name
  “ “ _Enter _Enter (guillemets espace guillemets pour le nom)
```

## Exemples d’utilisation des outils précédents

Regardez la macro suivante :

```
_Select _Pause _Setredrawoff
_BoundingBox _World _Enter
_Selnone _Sellast
_OffsetSrf _Solid _Pause
_Delete _Sellast
_BoundingBox _World _Enter
_Delete _Setredrawon
```

Elle crée une boîte de contour décalée autour d’un objet. Le décalage est indiqué par l’utilisateur.  Essayez de suivre la séquence logique.  Les commandes DésactiverRégénération (_Setredrawoff) et ActiverRégénération (_Setredrawon) arrêtent ou redémarrent la réactualisation de l’écran, éliminent le vacillement de l’écran puisque tout est exécuté et accélèrent le processus.  Attention, si vous terminez la commande avant ActiverRégénération (_Setredrawon), vous allez croire que Rhino est tombé en panne car l’écran ne s’actualisera plus.  Si cela se produit, ne vous inquiétez pas, tapez la commande `ActiverRégénération` (_Setredrawon) pour rétablir le rafraichissement de l’affichage.

**En tant que dernier exemple**, la macro suivante crée un point centré sur un objet plat en 2D ou un objet de texte et le groupe avec l’objet. Elle considère que vous êtes dans la même vue que celle dans laquelle le texte a été créé et que l’objet est réellement en 2D ou plat (autrement il est probable qu’elle échoue).

Remarquez l’utilisation d’un groupe nommé et de plusieurs commandes de sélection.  La commande `CopierInvitesDésactivé` (_NoEcho) arrête temporairement le signalement d’information dans la ligne de commande, ce qui, combiné à DésactiverRégénération (_Setredrawoff) ou ActiverRégénération (_Setredrawon) fait fonctionner la macro sans faire clignoter l’affichage et sans qu’il n’y ait trop d’informations dans l’historique des commandes.  Toutefois, elle pourrait fonctionner sans.

```
_Select _Pause _Noecho _Setredrawoff
_Group _Enter _SetGroupName TexTemp
_BoundingBox _CPlane _Enter
_SelNone _SelLast _PlanarSrf
_SelPrev _Delete _SelLast
_AreaCentroid _Delete
_Sellast _SelGroup TexTemp
_Ungroup _Group _Setredrawon
```

**N’hésitez pas à ajouter des éléments ou à modifier ce tutoriel !**
C’est un article en cours de développement...

## Voir aussi

- [Syntaxe de base de Python](/guides/rhinopython/)
- [Rhinoscript](/guides/rhinoscript/)
- [Rubrique d’aide sur la syntaxe des macros](http://docs.mcneel.com/rhino/6/help/fr-fr/information/rhinoscripting.htm)
- [Lancer une macro](/guides/rhinoscript/running-scripts-from-macros/)

+++
aliases = ["/en/5/guides/compute/what-is-hops/", "/en/6/guides/compute/what-is-hops/", "/en/7/guides/compute/what-is-hops/", "/en/wip/guides/compute/what-is-hops/"]
authors = [ "andy.payne" ]
categories = [ "Hops" ]
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "Qu’est-ce que Hops ?"
type = "guides"
weight = 1
override_last_modified = "2022-03-21T17:57:18Z"

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

Hops vous permet de simplifier les définitions longues et complexes. Les définitions de Grasshopper peuvent parfois être interminables, compliquées et répétitives. En programmation, on qualifie souvent cet état de désorganisation par le terme [« code spaghetti »](https://www.pcmag.com/encyclopedia/term/spaghetti-code). De nombreux facteurs contribuent au code spaghetti, notamment les contraintes de temps, le niveau de compétence du programmeur, la complexité du projet et les limites du langage de programmation. Si vous avez déjà essayé de déchiffrer un enchevêtrement de définitions de Grasshopper, vous vous en êtes rendu compte : le code spaghetti est difficile à lire et à comprendre. **Heureusement, il existe maintenant Hops pour simplifier un code spaghetti difficile à lire.**

{{< image url="/images/hops_spaghetti_code_1.png" alt="/images/hops_spaghetti_code_1.png" class="image_center" width="100%" >}}

### Appeler des fonctions dans Grasshopper

En programmation, une **fonction** est un module de code « autonome » qui traite les entrées et renvoie un résultat. Les définitions de Grasshopper traitent également des entrées et renvoient des résultats. Cependant, Grasshopper n’a pas été écrit dans cette optique. Les clusters fonctionnent assez bien en ce sens, mais ne facilitent pas la réutilisation de définitions simples dans des projets complexes.

C’est pour remédier à cette situation que le composant « Hops » a été ajouté. Hops permet d’utiliser des définitions de Grasshopper indépendantes comme s’il s’agissait de fonctions. La clé est d’apprendre à décomposer un problème en sous-définitions plus petites que nous utiliserons comme des fonctions.

Imaginez que vous deviez effectuer une analyse des ombres pour une tour paramétrique que vous concevez pour la ville de New York. Ce problème peut être décomposé en quatre tâches plus petites :
1. Créer la superficie au sol du bâtiment ;
1. Créer l’enveloppe du bâtiment ;
1. Créer les étages ;
1. Effectuer l’analyse des ombres à partir de l’enveloppe du bâtiment et des bâtiments environnants.

Une fois que vous avez clairement défini les tâches, vous pouvez déterminer les informations nécessaires à l’exécution de chacune (c’est-à-dire les entrées) et les données qui seront renvoyées à la fin (c’est-à-dire les sorties). Pour la première étape, les données d’entrée nécessaires pour générer la superficie au sol du bâtiment comprennent les marges de recul du site et d’autres paramètres réglementaires que l’on trouve dans les codes de construction et de zonage. Le résultat de cette fonction comprendra probablement une polyligne représentant la superficie maximale du bâtiment au niveau du rez-de-chaussée. 

Pour définir les paramètres qui seront utilisés dans une fonction de Grasshopper, utilisez les composants **Get** pour les entrées et le composant **Context Bake** pour les sorties. Ils se trouvent sous l’onglet *Params* > groupe *Util*.

{{< image url="/images/hops_context_getters.png" alt="/images/hops_context_getters.png" class="image_center" width="92%" >}}

Maintenant que nous avons défini les entrées et les sorties, il ne reste plus qu’à compléter les étapes pour transformer ces entrées en sorties. Lorsqu’une fonction a été entièrement définie en tant que définition de Grasshopper, elle peut être appelée par Hops. Hops expose les entrées et les sorties que vous avez définies à l’intérieur de votre fonction dans la définition dans laquelle il se trouve. Contrairement aux clusters, Hops vous permet de référencer des fichiers externes qui peuvent être enregistrés localement ou sur une unité en réseau, ce qui facilite le partage des définitions entre les membres d’une même équipe et les collaborateurs.

Grâce à Hops vous améliorez la lisibilité de votre code en simplifiant les définitions complexes, en réduisant les doublons et en partageant et réutilisant les fonctions. Par ailleurs, Hops vous permet de résoudre des fonctions en parallèle, ce qui peut accélérer les projets de grande envergure. Il sert également à résoudre des fonctions de manière asynchrone, sans bloquer les interactions entre Rhino et Grasshopper.

## Comment fonctionne-t-il ?

En arrière-plan, le client Hops transmet la définition de Grasshopper que vous avez spécifiée à une instance sans tête du serveur Rhino et Grasshopper.  

### Le client Hops

Un client est un dispositif matériel (c’est-à-dire un ordinateur) ou une application logicielle qui envoie une requête de ressource numérique à un serveur par le biais d’une connexion réseau. 

Le composant Hops est le client. Après avoir installé Hops via le gestionnaire de paquets, vous le trouverez sous l’onglet *Params* > groupe *Util*. Hops a besoin du chemin ou de l’URL de la définition qu’il va résoudre.
{{< image url="/images/hops_hello_world4.png" alt="/images/hops_hello_world4.png" class="image_center" width="55%" >}} 

Une fois la définition spécifiée, le composant s’actualise pour afficher les entrées et les sorties figurant dans la définition.
{{< image url="/images/hops_io.png" alt="/images/hops_io.png" class="image_center" width="30%" >}} 

### Le serveur Rhino

Un serveur fournit des données à ses clients à travers une connexion réseau. 

Dans le contexte de Hops, le serveur est une version sans tête (c’est-à-dire sans interface utilisateur avec laquelle interagir) de Rhino et Grasshopper. Le serveur sans tête de Rhino résout la définition de Grasshopper envoyée par Hops et renvoie le résultat.
{{< image url="/images/hops_console.png" alt="/images/hops_console.png" class="image_center" width="100%" >}}

Hops vous permet aussi de pointer vers un serveur Rhino.Compute fonctionnant sur un autre ordinateur pour résoudre les définitions de Grasshopper. Ainsi, vous déléguez une partie ou la totalité de la résolution à une ressource informatique externe.

## Commencer

Pour créer une fonction pouvant être référencée par Hops, nous devons diviser notre définition en trois sections distinctes : une pour définir nos paramètres d’entrée, une autre pour spécifier les sorties et enfin une section qui exécute les *actions* de la fonction. Pour commencer à utiliser Hops, vous pouvez soit regarder la vidéo, soit suivre les étapes décrites ci-après.

{{< vimeo 713836707 >}}

<br><br>
Dans cet exemple, nous voulons créer une fonction simple qui prendra en entrée le nom d’un utilisateur (David) et renverra le message *« Salut David! »*.

### Installer Hops

Avant de commencer, vérifions d’abord que Hops est correctement installé. Il y a plusieurs façons d’installer Hops sur votre machine.
  1. [Installez Hops](rhino://package/search?name=hops) (Cela lancera Rhino.)
  1. Ou tapez `PackageManager` dans la ligne de commande de Rhino.
      1. Ensuite, recherchez « Hops ».
      1. Sélectionnez Hops et installez-le.

### Créer une entrée

Maintenant que nous avons installé Hops, commençons à définir notre fonction en créant un paramètre de texte d’entrée. Sous l’onglet *Params* > groupe *Util*, vous verrez un ensemble de composants commençant par Get qui permettent d’obtenir des données contextuelles. Placez un composant **Get String** sur votre toile. Faites un clic droit au milieu de ce composant et changez-en le nom : tapez `Name` au lieu de `Get String`. Cette valeur est celle que Hops utilisera pour le nom du paramètre d’entrée.
{{< image url="/images/hops_getting_started_01.png" alt="/images/hops_getting_started_01.png" class="image_center" width="100%" >}}

Vous pouvez attribuer une valeur par défaut à ce paramètre en connectant une chaîne à l’entrée du composant Get String. Ajoutez un **panneau de texte** sur la toile. Vous le trouverez sous l’onglet *Params* > groupe *Input*. Double-cliquez sur le panneau de texte et écrivez votre nom dedans.
{{< image url="/images/hops_getting_started_02.png" alt="/images/hops_getting_started_02.png" class="image_center" width="100%" >}}

### Définir la fonction

Maintenant que nous avons créé un paramètre d’entrée, nous devons effectuer une action utilisant cette valeur. Nous allons créer un message en utilisant le nom que vous venez de définir dans le composant Get String. Ajoutez un composant **Concatenate** sur la toile. Il se trouve dans l’onglet *Sets* > groupe *Text*. 

Le composant Concatenate permet de combiner une série de morceaux de texte en un seul message. Dans notre cas, nous voulons créer la chaîne de caractères suivante : `Bonjour, votre nom!`. 

Le composant Concatenate est un type de composant spécial dans Grasshopper qui utilise une interface utilisateur zoomable (ZUI). Si vous effectuez un zoom avant sur le composant (à l’aide de la molette de la souris), un petit bouton (+) apparaît sur le côté gauche du composant. Cliquez sur le (+) sous le deuxième paramètre (B) pour ajouter un troisième paramètre d’entrée.

Maintenant, faites un zoom arrière et ajoutez un autre panneau de texte sur la toile. Double-cliquez dessus pour entrer du texte. Tapez `Salut ` dans le panneau (Attention : n’oubliez pas de laisser un espace après « Salut »). Connectez ce panneau à l’entrée A du composant Concatenate.

Ensuite, connectez la sortie du composant Get String à l’entrée B du composant Concatenate. Enfin, ajoutez un autre panneau de texte sur votre toile et tapez un point d’exclamation `!` dans le panneau. Connectez la sortie de ce panneau de texte à l’entrée C du composant Concatenate.

Reliez un panneau de texte à la sortie du composant Concatenate pour afficher ce message. Votre définition devrait ressembler à ceci.
{{< image url="/images/hops_getting_started_03.png" alt="/images/hops_getting_started_03.png" class="image_center" width="100%" >}}

### Créer une sortie

La dernière étape de la création de notre fonction Hops consiste à créer un paramètre de sortie pour renvoyer la chaîne que nous venons de créer. Allez dans l’onglet *Param* > groupe *Util* et ajoutez un composant **Context Print** sur votre toile.

Cliquez avec le bouton droit de la souris sur le paramètre d’entrée (étiqueté Tx) et changez le nom par `Message`. Vous pouvez lui donner le nom que vous voulez, mais c’est cette valeur que Hops utilisera pour le paramètre de sortie.

Enregistrez maintenant votre fichier dans un dossier sur votre ordinateur. Appelez le fichier **Hello_World.gh**.
{{< image url="/images/hops_getting_started_04.png" alt="/images/hops_getting_started_04.png" class="image_center" width="100%" >}}

### Appeler la fonction

Nous avons créé une fonction compatible avec Hops. Nous allons maintenant utiliser Hops pour appeler cette fonction. Commençons par créer une nouvelle définition de Grasshopper (Ctrl + N).

Allez dans l’onglet *Param* > groupe *Util* et ajoutez un composant **Hops** sur votre toile. Cliquez avec le bouton droit de la souris sur ce composant et sélectionnez l’élément de menu **Path**. Dans la boîte de dialogue, sélectionnez le fichier **Hello_World.gh** que nous venons de créer. Sélectionnez **OK** après avoir indiqué l’emplacement.

À ce stade, le composant Hops devrait changer d’apparence : vous devriez voir une entrée appelée `Name` et une sortie appelée `Message`. Hops a regroupé l’exemple Hello_World.gh que nous avons créé et l’a envoyé à un serveur rhino.compute local pour qu’il effectue le calcul et renvoie le résultat.

Essayez d’ajouter un nouveau **panneau de texte** sur la toile et reliez-le à l’entrée Name du composant Hops. Double-cliquez pour modifier le nom dans le panneau de texte. Ajoutez un autre panneau de texte à la sortie du composant Hops pour voir le résultat renvoyé par le serveur rhino.compute.
{{< image url="/images/hops_getting_started_05.png" alt="/images/hops_getting_started_05.png" class="image_center" width="100%" >}}

Nous venons de voir comment créer et appeler votre toute première fonction Hops. Si vous souhaitez en savoir plus sur la façon dont Hops communique avec le serveur rhino.compute ou sur la mise en place de votre propre environnement de production, cliquez sur les liens ci-dessous.

 ---

## Liens rapides

 - [Comment fonctionne Hops](../how-hops-works)
 - [Le composant Hops](../hops-component)
 - [Mettre en place un environnement de production](../deploy-to-iis)

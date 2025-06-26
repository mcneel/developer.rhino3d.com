+++
aliases = ["/en/5/guides/compute/hops-component/", "/en/6/guides/compute/hops-component/", "/en/7/guides/compute/hops-component/", "/en/wip/guides/compute/hops-component/"]
authors = [ "steve", "scottd", "andy.payne" ]
categories = [ "Hops" ]
description = "Hops ajoute des fonctions à Grasshopper."
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "Le composant Hops"
type = "guides"
weight = 3
override_last_modified = "2024-10-28T11:35:10Z"

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

## Description 


{{< image url="/images/hops-overview.png" alt="/images/hops-overview.png" class="image_center" width="100%" >}}

Hops est un composant pour Grasshopper dans Rhino 7 et Rhino 8 pour Windows. Hops ajoute des **fonctions** externes à Grasshopper. Comme d’autres langages de programmation, les fonctions vous permettent :

* de simplifier des algorithmes complexes en utilisant plusieurs fois la même fonction ;
* d’éliminer les combinaisons de composants dupliquées en plaçant les combinaisons communes dans une fonction ;
* de partager des documents de Grasshopper avec d’autres membres de l’équipe ;
* de référencer des documents de Grasshopper dans plusieurs projets ;
* de résoudre des documents externes en parallèle, ce qui permet d’accélérer les grands projets ;
* d’exécuter de manière asynchrone des calculs longs sans bloquer les interactions entre Rhino et Grasshopper.

Les fonctions de Hops sont stockées en tant que documents de Grasshopper distincts. Le composant Hops adaptera ses entrées et sorties afin de correspondre à la fonction spécifiée. Pendant le calcul, Hops résout la définition dans un processus indépendant, puis renvoie les résultats dans le document dans lequel vous travaillez.

## Comment utiliser Hops ? <img src="/images/hops.svg" alt="Windows" class="guide_icon">

{{< vimeo 713836707 >}}

### Installer Hops

Il y a plusieurs façons d’installer Hops sur votre machine.
  1. [Installez Hops](rhino://package/search?name=hops) (Cela lancera Rhino.)
  1. Ou tapez `PackageManager` dans la ligne de commande de Rhino.
      1. Ensuite, recherchez « Hops ».
      1. Sélectionnez Hops et installez-le.

{{< image url="/images/hops-package-manager.png" alt="/images/hops-package-manager.png" class="image_center" width="100%" >}}

### Créer une fonction Hops

Les fonctions Hops sont des documents de Grasshopper avec des entrées et des sorties spéciales.

{{< image url="/images/hops_simple_function.png" alt="/images/hops_simple_function.png" class="image_center" width="100%" >}}

#### Définition des entrées

Les entrées de Hops sont créées à partir des composants **Get**. Les composants Get disponibles dans Grasshopper se trouvent sous l’onglet *Params* > groupe *Util* :

{{< image url="/images/hops_context_getters1.png" alt="/images/hops_context_getters1.png" class="image_center" width="65%" >}}

Le nom du composant sera le nom du paramètre d’entrée de Hops. Ainsi, dans l’exemple ci-dessous, nous avons trois composants Get Number que nous avons appelés A, B et C. Chacun de ces composants Get devient un paramètre d’entrée lorsque Hops compile la définition.

{{< image url="/images/hops_getter_inputs.png" alt="/images/hops_getter_inputs.png" class="image_center" width="80%" >}}

Chaque composant Get dispose d’un menu contextuel (accessible par clic droit) permettant d’accéder à différentes options.

{{< image url="/images/hops-get-component-menu.png" alt="/images/hops-get-component-menu.png" class="image_center" width="50%" >}}

* **Nom du composant** - Il s’agit du nom qui sera attribué à l’entrée du composant Hops.
* **Prompt** - Cette entrée sera l’infobulle qui s’affichera lorsque vous survolerez ce paramètre dans le composant Hops.
* **Enable/Disable** - Permet d’activer ou de désactiver ce composant.
* **At Least** - Cette option n’est utilisée que par le lecteur de Grasshopper et permet de définir le nombre minimum de valeurs à accepter pour cette entrée.
* **At Most** - Cette option permet de définir le nombre maximum de valeurs à accepter pour cette entrée (par défaut = 1). Si cette valeur est fixée à 1, le composant Hops traitera cette entrée comme un *Item Access*. Toutefois, si cette valeur est supérieure à un (ou non définie), Hops traitera cette entrée comme un *List Access*.
* **Tree Access** - Cette option permet de définir si vous souhaitez introduire un arbre de données par cette entrée. Cette entrée n’est utilisée que dans Hops et si elle est définie sur True, elle remplacera la valeur *At Most* définie précédemment.
* **Minimum et Maximum** - Ces options facultatives ne sont utilisées que pour le lecteur de Grasshopper. Elles permettent de limiter le nombre d’entrées numériques.
* **Presets** - Cette option facultative n’est utilisée que pour le lecteur de Grasshopper et ne se trouve que sur les composants *Get String*, *Integer* et *Number*. Cette boîte de dialogue vous permet de définir une liste d’options prédéfinies qui s’afficheront pour l’utilisateur dans l’invite de la ligne de commande.

#### Définition des sorties

Les sorties de Hops peuvent être définies à l’aide des composants **Context Bake** ou **Context Print**. Le nom du paramètre d’entrée dans l’un ou l’autre des composants contextuels sera utilisé comme nom du paramètre de sortie de Hops.

{{< image url="/images/hops_getter_outputs.png" alt="/images/hops_getter_outputs.png" class="image_center" width="67%" >}}

### Utiliser le composant Hops

1. Placez le composant Hops de Grasshopper sur la toile. Vous le trouverez dans l’onglet *Params* > groupe *Util*.
1. Cliquez avec le bouton droit de la souris sur le composant Hops, puis cliquez sur Path.
1. Sélectionnez une fonction de Hops. Il peut s’agir d’une définition de Grasshopper sur votre ordinateur, sur un ordinateur distant ou d’un point de terminaison REST.
1. Le composant affichera les entrées et les sorties.
1. Vous pouvez à présent utiliser ce nouveau composant comme n’importe quel autre composant de Grasshopper.

{{< image url="/images/hops_multiplyadd.png" alt="/images/hops_multiplyadd.png" class="image_center" width="80%" >}}

### Remarque à propos de Hops pour les utilisateurs de macOS

Le composant Hops fonctionne en tandem avec une instance locale d’un serveur [Rhino.compute](https://developer.rhino3d.com/guides/compute/) qui, en général, est lancé à chaque fois que vous ouvrez Grasshopper. Cependant, ce serveur ne fonctionnera pas sous macOS, ce qui signifie que deux autres options s’offrent à vous. Vous pouvez :

1. faire en sorte qu’une API REST appelle un serveur distant fonctionnant sous Windows.
1. faire en sorte qu’une API REST appelle un serveur python ghhops_server fonctionnant localement.

La première option (appeler un serveur Windows distant) nécessitera quelques modifications au niveau de l’installation de la machine distante. Pour plus d’informations sur la configuration d’un serveur distant, reportez-vous à la section [Configuration d’une machine distante](../hops-component/#remote-machine-configuration).

La deuxième option (appeler un serveur python local) est couverte plus en détail dans la section intitulée [Appeler un serveur CPython](../hops-component/#calling-a-cpython-server).

## Paramètres de Hops

### Paramètres d’application

Les paramètres de Hops contrôlent le fonctionnement de Hops au niveau de l’application.  Pour y accéder, cliquez sur le menu déroulant de Grasshopper File > Preferences > Solver.

{{< image url="/images/hops-preferences.png" alt="/images/hops-preferences.png" class="image_center" width="60%" >}}

* **Hops-Compute server URLs** - Liste des adresses IP ou URL de toutes les machines ou serveurs Compute distants.
* **API Key** - La clé API est une chaîne de texte secrète réservée à votre serveur Compute et aux applications qui utilisent l’API Compute, par exemple `b8f91f04-3782-4f1c-87ac-8682f865bf1b`. Elle n’est pas obligatoire si vous effectuez des tests localement, mais doit être utilisée dans un environnement de production. En essence, c’est ainsi que le serveur Compute s’assure que les appels de l’API proviennent uniquement de vos applications. Vous pouvez saisir n’importe quelle chaîne de caractères unique et secrète pour vous et vos applications informatiques. Conservez-la en lieu sûr.
* **Max Concurrent requests** - Ce paramètre permet de limiter le nombre de requêtes actives dans des situations asynchrones. Ainsi, Hops ne fait pas des milliers de demandes pendant que la demande initiale est en cours de traitement.
* **Clear Hops Memory cache** - En cliquant sur ce bouton, vous effacez de la mémoire toutes les solutions enregistrées précédemment.
* **Hide Rhino.Compute Console Window** - Hops résoudra les définitions en arrière-plan ; mais parfois, l’affichage de la fenêtre peut être utile pour détecter des erreurs.
* **Launch Local Rhino.Compute at Start** - Cochez cette case pour les machines distantes lorsque Compute doit démarrer avant que des requêtes ne soient envoyées.
* **Child Process Count** - Cette option sert à limiter le nombre de demandes de processus parallèles supplémentaires. Il est recommandé de définir ce paramètre selon le nombre de cœurs disponibles.
* **Function Sources** - Cette section vous permet d’ajouter un chemin (soit vers un répertoire local, soit vers une URL) menant aux fonctions de Hops fréquemment utilisées (c’est-à-dire des définitions de Grasshopper).

{{< call-out "note" "Remarque" >}}
Depuis la version 7.13 de Rhino, les tolérances du modèle actif (c’est-à-dire les tolérances de distance absolue et d’angle) sont transmises par Hops à l’instance de Rhino.compute en cours d’exécution dans le cadre de la requête JSON.
{{< /call-out >}}

### Paramètres des composants

Cliquez avec le bouton droit de la souris sur le composant Hops pour sélectionner les options permettant de contrôler le fonctionnement de Hops.

{{< image url="/images/gh-hops-component-settings.png" alt="/images/gh-hops-component-settings.png" class="image_center" width="60%" >}}

* **Parallel Computing** - Pour passer chaque élément vers un nouveau nœud parallèle si cela est possible.
* **Path...** - C’est là que vous indiquez l’emplacement de la fonction GH à résoudre. Il peut s’agir d’un nom de fichier, d’une adresse IP ou d’une URL.
* **Show Input: Path** - Le chemin d’accès devient une entrée du composant de sorte qu’il peut être défini directement sur la toile de GH.
* **Show Input: Enabled** - Affiche une entrée Enabled qui exécute le composant en fonction d’une valeur booléenne `True` ou `False`.
* **Asynchronous** - L’interface utilisateur ne sera pas bloquée en attendant qu’un processus distant résolve la définition et la définition sera mise à jour lorsque la résolution sera terminée.
* **Cache In Memory** - Les solutions précédentes sont enregistrées en mémoire sur la machine locale afin d’améliorer les performances si les mêmes entrées ont déjà été calculées.
* **Cache On Server** - Les solutions précédentes sont enregistrées sur le serveur distant pour améliorer les performances. Actuellement, cette option n’est disponible que pour les services Hops distants.

## Configuration de la machine distante

Par défaut, Hops utilise votre ordinateur local pour résoudre les fonctions de Grasshopper. Toutefois, il est possible de configurer des ordinateurs distants (c’est-à-dire des serveurs) ou des machines virtuelles que Hops pourra appeler.

Pour effectuer des appels API vers une machine distante, veuillez suivre ce [guide sur la mise en place d’un environnement de production](../deploy-to-iis/).

## Appeler un serveur CPython

Utiliser Hops pour appeler CPython. Les principaux avantages de ce composant sont les suivants :

1. Il appelle des bibliothèques CPython, y compris Numpy et SciPy ;
1. Il utilise certaines des bibliothèques les plus récentes disponibles pour CPython, telles que TensorFlow ;
1. Il permet de créer des fonctions réutilisables et d’utiliser le traitement parallèle ;
1. Il prend en charge des modes de débogage réels, y compris les points d’arrêt ;
1. Prise en charge intégrale de Visual Studio Code ;
1. D’autres applications et services prenant en charge une API Python peuvent également utiliser les bibliothèques incluses ici ;
1. Le composant Hops essaie de détecter les changements au niveau des entrées et des sorties sur un serveur et se reconstruit lui-même.  

### Démarrer avec CPython dans Grasshopper

Ce module Python vous aide à créer des fonctions Python (plus précisément CPython) et à les utiliser dans vos scripts de Grasshopper avec les nouveaux composants Hops.

**Obligatoire :**

1. [Rhino 7.4 ou une version plus récente.](https://www.rhino3d.com/download/)
1. [CPython 3.8 ou supérieur](https://www.python.org/downloads/)
1. [Composant Hops pour Grasshopper](https://developer.rhino3d.com/guides/grasshopper/hops-component/)
1. [Visual Studio Code](https://code.visualstudio.com/) fortement recommandé

**Tutoriel vidéo :**

{{< vimeo 524032610 >}}

Ce module peut utiliser son serveur HTTP intégré par défaut pour fournir les fonctions en tant que composants de Grasshopper, ou agir en tant qu’intergiciel pour une application [Flask](https://flask.palletsprojects.com/en/1.1.x/). Il peut également fonctionner avec [Rhino.Inside.CPython](https://discourse.mcneel.com/t/rhino-inside-python/78987) pour donner un accès complet à l’API [RhinoCommon](https://developer.rhino3d.com/api/).

## Questions fréquentes

#### Est-il possible d’imbriquer des fonctions Hops dans d’autres fonctions ?

Oui, il est possible d’imbriquer la fonction Hops dans d’autres fonctions. On appelle cela _recursion_ et la limite de récursion par défaut est fixée à 10.

#### L’utilisation de Hops est-elle payante ?

Hops est gratuit.

#### Peut-on utiliser Hops avec le lecteur de Grasshopper pour créer des commandes ?

Oui, les fonctions Hops peuvent utiliser les composants Context Bake et Context Print pour créer des commandes de Rhino dans le lecteur de Grasshopper.

#### Hops prend-il en charge le traitement parallèle ?

Oui, Hops lance par défaut un processus parallèle pour chaque branche de flux d’entrée d’un arbre de données.

#### Quels sont les types d’entrée et de sortie pris en charge par Hops ? (Il prend en charge tous les types courants, demandez-en d’autres si vous en avez besoin)

Hops transmet les types de données standard de Grasshopper (chaînes de caractères, nombres, lignes, etc.). Pour d’autres types de données tels que les images ou les fichiers météorologiques EPW, utilisez une chaîne de caractères pour le nom du fichier afin que la fonction externe puisse également lire le même fichier.

#### Les composants des modules peuvent-ils être exécutés dans des fonctions Hops ?

Oui, tous les modules de Grasshopper installés peuvent être exécutés dans une fonction Hops.

#### Peut-on l’utiliser pour des calculs extrêmement longs dans une fonction ?

Oui, chaque composant Hops dispose d’une option permettant de résoudre les problèmes de manière asynchrone. L’interface utilisateur ne sera pas bloquée dans l’attente de la résolution d’un processus distant et la définition sera mise à jour lorsque la résolution sera terminée. Hops attendra que tous les appels de fonction aient été retournés avant de transmettre les résultats aux composants en aval.
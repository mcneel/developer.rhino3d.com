+++
aliases = ["/en/8/guides/general/rhino-ui-system/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "Ce guide présente le système d’interface utilisateur de Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Le système d’interface utilisateur de Rhino"
type = "guides"
weight = 3
override_last_modified = "2023-11-20T08:29:10Z"

[admin]
TODO = ""
origin = ""
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

Ce guide présente une vue d’ensemble du système d’interface utilisateur (UI) de Rhino et compare le nouveau système de Rhino 8 avec le système précédent de Rhino 7 et des versions antérieures.

## Le système d’interface utilisateur de Rhino 8

Les objectifs du nouveau système d’UI de Rhino 8 étaient les suivants :

- Afficher des panneaux et des barres d’outils dans un même conteneur ;
- Référencer des barres d’outils et des macros à partir de plusieurs sources sans avoir à copier les définitions d’un fichier RUI à l’autre ;
- Apporter des modifications à l’interface utilisateur de Rhino (RUI) sans écraser ou remplacer les fichiers existants dans les versions révisées de Rhino ou des modules (Dans les versions précédentes de Rhino, le remplacement du fichier RUI pour la mise à jour des barres d’outils et des macros entraînait l’écrasement des modifications apportées par l’utilisateur aux fichiers RUI) ;
- Changer rapidement l’UI de Rhino pour afficher des outils adaptés aux tâches spécifiques ;
- Partager les dispositions de l’interface utilisateur entre les utilisateurs ;
- Permettre aux utilisateurs de modifier arbitrairement l’UI sans avoir à connaître l’emplacement ou la source d’un composant de l’UI et garantir un suivi automatique des modifications ;
- Fournir une UI unifiée pour Windows et Mac.

Les principales modifications apportées au nouveau système d’interface utilisateur de Rhino 8 sont les suivantes :

- Les groupes de barres d’outils ont été remplacés par des conteneurs. Les conteneurs peuvent afficher des panneaux et des barres d’outils ;
- Les fichiers RUI servent à fournir des bibliothèques de barres d’outils et de macros, et ne sont plus modifiés directement. Rhino effectue le suivi des modifications apportées à l’interface utilisateur de Rhino et les applique lors du chargement. Cela permet à Rhino de fournir des fichiers RUI mis à jour sans perdre les modifications apportées par l’utilisateur à une barre d’outils ou à une macro ;
- Des dispositions de l’écran ont été ajoutées et peuvent être utilisées pour passer rapidement d’une configuration d’UI à une autre. Elles peuvent être exportées sous forme de fichiers et incluent les modifications des barres d’outils, des macros et des fichiers RUI des utilisateurs ;
- L’importation d’une disposition de l’écran permet d’extraire les fichiers RUI de l’utilisateur si nécessaire et d’appliquer les modifications de l’interface de Rhino.

Le nouveau système d’UI de Rhino 8 est conçu pour permettre le référencement des composants de l’UI à partir de nombreuses sources y compris des panneaux, des barres d’outils et des macros, définis par n’importe quel fichier RUI ou module. Lorsque l’utilisateur ferme Rhino, les modifications apportées à l’UI sont sauvegardées et les fichiers RUI d’origine ne sont jamais modifiés, à moins que cela ne soit spécifiquement requis. Les configurations de l’UI peuvent être enregistrées, restaurées, exportées et importées en tant que dispositions de l’écran et partagées entre Windows et Mac.

### Conteneurs

Les conteneurs contiennent des références à des panneaux et à des barres d’outils. Les barres d’outils peuvent être référencées à partir de n’importe quelle source RUI valide. Chaque élément est affiché sous la forme d’un onglet dans le conteneur. Les conteneurs peuvent être visibles ou cachés.

L’utilisateur peut modifier un conteneur en faisant glisser des onglets d’un conteneur vers un autre, ou en cliquant sur l’icône de l’engrenage du conteneur afin d’ajouter ou de supprimer des références à certains panneaux ou barres d’outils. Un même panneau peut être référencé par plusieurs conteneurs, ce qui signifie qu’il est possible d’afficher l’onglet Calques, par exemple, dans plusieurs conteneurs.

Les définitions, la visibilité, l’emplacement et la taille des conteneurs sont sauvegardés à la fermeture de Rhino et restaurés au redémarrage de Rhino. Ces informations peuvent également être stockées et partagées via les dispositions de l’écran.

Dans Rhino, la commande **[Conteneurs](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/containers.htm#(null))** permet de gérer les conteneurs.

### Dispositions de l’écran

Les dispositions de l’écran sont un instantané des définitions, du statut de visibilité, des emplacements et de la taille des conteneurs. La restauration d’une disposition de l’écran reconfigure l’UI actuelle afin qu’elle apparaisse telle qu’elle était lorsque la disposition a été créée. Dans les conteneurs restaurés, les onglets s’afficheront dans l’ordre dans lequel ils se trouvaient lors de la création de la disposition de l’écran et apparaîtront au même endroit et dans la même taille. Les onglets des barres d’outils référencent la définition actuelle d’une barre d’outils ; si la barre d’outils n’existe plus, l’onglet ne s’affiche pas.

Dans Rhino, la commande **[DispositionÉcran](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/windowlayout.htm#(null))** permet de gérer les dispositions de l’écran.

#### Exporter et importer des dispositions de l’écran

Les dispositions de l’écran peuvent être exportées vers un fichier de disposition de l’écran de Rhino (*.rhw). Les fichiers .rhw exportés comprennent les fichiers RUI personnalisés référencés et les modifications associées à tous les fichiers RUI au moment de la création du fichier .rhw.

Lorsque l’utilisateur importe un fichier .rhw, le système vérifie si un fichier RUI personnalisé intégré est ouvert. Si ce n’est pas le cas, le système extrait et ouvre le fichier personnalisé. Une fois la liste personnalisée extraite ou vérifiée, les modifications apportées à l’interface et enregistrées dans le fichier .rhw seront appliquées aux actuels fichiers RUI. Les informations de modifications associées aux barres d’outils définies par des fichiers de modules qui n’existent pas seront ignorées. Une fois les données RUI restaurées, les conteneurs seront créés ou modifiés pour correspondre à la définition stockée dans le fichier .rhw. Les conteneurs qui ne référencent que des barres d’outils provenant de modules non installés seront ignorés. Une fois importée, la disposition apparaît dans la liste des dispositions de l’écran et peut ensuite être restaurée.

Les dispositions de l’écran peuvent être exportées et importées à l’aide de la commande **[DispositionÉcran](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/windowlayout.htm#(null))** de Rhino.

### Fichiers RUI

Dans Rhino 8, les fichiers RUI sont désormais un simple ensemble de barres d’outils, de macros et d’images. Ces fichiers sont destinés à fournir des bibliothèques de barres d’outils qui peuvent être référencées par des conteneurs. Les modifications apportées aux barres d’outils et aux macros peuvent à présent être livrées avec les mises à jour de Rhino et des modules. Les nouvelles barres d’outils définies dans la bibliothèque RUI actualisée apparaîtront automatiquement dans la liste des commandes de la barre d’outils. Les boutons ajoutés ou supprimés d’une barre d’outils seront ajoutés ou supprimés dans la référence de la barre d’outils.

Les groupes de barres d’outils définis dans les fichiers RUI sont convertis en conteneurs lorsqu’ils sont chargés afin de prendre en charge les fichiers RUI anciens et de modules ; ils fournissent aux fichiers RUI de modules un moyen de créer des conteneurs associés au module.

Dans Rhino, il est possible de gérer les fichiers RUI liés en allant dans **[Options > Apparence > Barres d’outils](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#options/appearance_toolbars.htm#(null))**.

### Barres d’outils

Les barres d’outils sont des ensembles de boutons. Les boutons des barres d’outils référencent des macros qui peuvent provenir de n’importe quelle source RUI valide. Les barres d’outils sont affichées sous forme d’onglets dans un conteneur.

#### Groupes de barres d’outils

Les groupes de barres d’outils sont désormais convertis en conteneurs lors du chargement initial. Leur fonction est de prendre en charge les anciens fichiers RUI. Les développeurs de modules peuvent également utiliser les groupes pour livrer des définitions de conteneurs associées à un module.

#### Barres d’outils

Les barres d’outils sont des ensembles de boutons de barre d’outils et peuvent être référencées par plusieurs conteneurs. Pour les modifier, il suffit de faire un glisser-déposer à partir de boutons d’autres barres d’outils ou d’utiliser l’assistant de création de boutons.

Dans Rhino, la commande **[BarreOutils](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/toolbar.htm#(null))** permet de gérer les barres d’outils.

#### Boutons de barre d’outils

Les boutons de barre d’outils peuvent être actionnables à partir d’un clic gauche et/ou droit de la souris. Les actions des clics gauche et droit de la souris sont associées à des macros qui contiennent un script à exécuter au moment du clic. Les boutons de barre d’outils affichent l’image associée à la macro assignée à l’action du clic gauche de la souris, si elle existe ; dans le cas contraire, c’est l’image de la macro du clic droit qui est utilisée.

#### Menus

Le système de menus de Rhino peut être étendu à l’aide d’objets de menu définis dans un fichier RUI. Le fichier RUI contient des informations sur l’emplacement décrivant où insérer un élément dans le système de menus. Les nouveaux éléments de menu sont définis en référençant une macro qui contient :

- Le texte du menu ;
- L’image de l’élément du menu ;
- Le texte d’aide qui apparaît dans la barre d’état quand l’utilisateur survole l’élément du menu avec la souris ;
- Le script de la commande à exécuter lorsque l’utilisateur clique sur l’élément du menu.

Dans Rhino, la commande **[Menus](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#toolbarsandmenus/workspace_editor.htm#(null))** permet de gérer les menus.

#### Macros

Les macros contiennent les informations nécessaires pour décrire le script de la commande à lancer lorsque la macro est exécutée. Les définitions des macros comprennent les éléments suivants :

- Le nom ;
- L’image (pour la version en mode clair et en mode foncé) ;
- Le script de la commande ;
- Le texte du bouton ;
- L’info-bulle du bouton ;
- Le texte du menu ;
- Le texte d’aide.

Dans Rhino, la commande **[Macros](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/macros.htm#(null))** permet de gérer les macros.

### Panneaux

Les panneaux sont des formes d’interface utilisateur sans modèle créées par Rhino ou par des modules. Ils peuvent apparaître dans n’importe quel conteneur sous forme d’onglet et être déplacés d’un conteneur à l’autre par glisser-déposer.

Les panneaux peuvent être référencés par plusieurs conteneurs, mais ils ne peuvent pas apparaître plus d’une fois dans un même conteneur.

## Système d’UI dans la version précédente de Rhino

Le système d’interface utilisateur que l’on trouve dans Rhino pour Windows version 7 et précédentes, se compose des éléments suivants :

### Barres d’outils

Les barres d’outils de Rhino sont des ensembles de boutons de barre d’outils. Les boutons de barres d’outils référencent des macros qui doivent être définies dans le même fichier RUI que la barre d’outils. Les boutons contiennent une image, une info-bulle, un texte de menu, un texte d’aide et un script. Les barres d’outils sont affichées dans des groupes de barres d’outils.

### Groupe de barres d’outils

Les groupes de barres d’outils sont des ensembles de références à des barres d’outils provenant du même fichier RUI. En faisant glisser une barre d’outils d’un fichier vers un groupe dans un autre fichier, la barre d’outils et ses macros référencées sont copiées du fichier source vers le fichier de destination. Les groupes de barres d’outils ne peuvent pas référencer des panneaux de Rhino.

### Barres d’outils

Les barres d’outils sont des ensembles de boutons de barre d’outils et ne peuvent être référencées et affichées que par des groupes de barres d’outils.

### Boutons de barre d’outils

Les boutons de barre d’outils peuvent être actionnables à partir d’un clic gauche et/ou droit de la souris. Les actions associées aux clics de souris sont attribuées à des macros qui contiennent un script à exécuter en cas de clic. Les boutons de barre d’outils affichent l’image associée à la macro assignée à l’action du clic gauche de la souris, si elle existe ; dans le cas contraire, c’est l’image de la macro du clic droit qui est utilisée.

Les boutons de barre d’outils peuvent éventuellement être configurés de manière à déployer temporairement d’autres barres d’outils.

Les boutons de barre d’outils ne peuvent faire référence qu’à des macros provenant du même fichier RUI que la barre d’outils à laquelle ils appartiennent.

### Menu

Le système de menus de Rhino peut être étendu à l’aide d’objets de menu définis dans un fichier RUI. Le fichier RUI contient des informations sur l’emplacement décrivant où insérer un élément dans le système de menus. Les nouveaux éléments de menu sont définis en référençant une macro qui contient :

- Le texte du menu ;
- L’image de l’élément du menu ;
- Le texte d’aide qui apparaît dans la barre d’état quand l’utilisateur survole l’élément du menu avec la souris ;
- Le script de la commande à exécuter lorsque l’utilisateur clique sur l’élément du menu.

### Macros

Les macros contiennent les informations nécessaires pour afficher ou décrire le script de la commande à lancer lorsque la macro est exécutée. Les définitions des macros comprennent les éléments suivants :
L’image affichée sur un bouton de barre d’outils ou un élément de menu référencé ;

- L’info-bulle du bouton ;
- Le texte du bouton ;
- Le texte de l’élément du menu ;
- Le texte d’aide qui apparaît dans la barre d’état quand l’utilisateur survole l’élément du menu avec la souris ;
- Le script de la commande à exécuter.

### Ficher RUI

Les fichiers RUI contiennent les éléments ci-dessus et sont stockés dans un répertoire accessible en écriture. Les éléments enregistrés dans un fichier RUI ne peuvent référencer que des éléments définis dans le même fichier. Les modifications apportées aux éléments du fichier sont sauvegardées automatiquement à la fermeture de Rhino. Il est possible d’ouvrir ou de fermer les fichiers RUI, ou de choisir manuellement d’enregistrer un fichier à tout moment. La version actuelle d’un fichier est sauvegardée et les modifications sont enregistrées sous le nom du fichier. Si un fichier est endommagé, vous pouvez le supprimer et renommer le fichier de sauvegarde pour tenter de restaurer la version précédente. Si le fichier de sauvegarde est endommagé, vous ne pourrez rien récupérer.

Les modules de Rhino peuvent installer un fichier RUI portant le même nom que le module ; ce fichier sera alors copié dans un emplacement accessible en écriture et ouvert automatiquement au démarrage de Rhino. Cela permet à un module d’étendre l’interface de Rhino sans être chargé tant que le module n’est pas référencé.

Remarque : dans Rhino 7, la commande **[BarreOutils](https://docs.mcneel.com/rhino/7/help/en-us/index.htm#options/toolbars.htm#(null))** permet de gérer tous les éléments précédents.

### Panneaux de Rhino

Les panneaux de Rhino sont des définitions d’interface utilisateur sans modèle créées par le noyau de Rhino ou un module.

Les panneaux sont affichés dans un ensemble d’onglets. Les ensembles d’onglets ne peuvent contenir que des références à des panneaux et un panneau ne peut être référencé que par un seul ensemble. L’affichage d’un panneau dans un ensemble supprime les références à ce panneau dans tous les autres ensembles.

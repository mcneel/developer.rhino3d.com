+++
aliases = ["/en/5/guides/yak/package-sources/", "/en/6/guides/yak/package-sources/", "/en/7/guides/yak/package-sources/", "/en/wip/guides/yak/package-sources/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Ce guide explique comment configurer les répertoires de paquets personnalisés dans Rhino."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Répertoires de paquets personnalisés"
type = "guides"
weight = 20
override_last_modified = "2021-02-12T11:31:53Z"

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

<!-- {{< call-out "note" "Remarque" >}}
Cette fonctionnalité implique de modifier des paramètres avancés dans Rhino !
{{< /call-out >}} -->

Par défaut, Rhino utilise le serveur de paquets officiel de McNeel, https://yak.rhino3d.com. Il est possible de configurer Rhino pour qu’il utilise en plus de ce serveur (ou au lieu de celui-ci) vos propres répertoires de paquets.

Un répertoire de paquets personnalisé est simplement un dossier qui contient des fichiers de paquets .yak. Le dossier peut se trouver sur votre machine locale ou sur un serveur partagé de fichiers. Vous pouvez configurer Rhino pour qu’il inclue les paquets de ce répertoire dans le Gestionnaire de paquets en suivant les étapes ci-dessous :


1. Allez dans _Options > Options avancées_ et cherchez le paramètre `Rhino.Options.PackageManager.Sources`.
1. Ajoutez le chemin complet du dossier de votre répertoire de paquets, en le séparant du serveur de paquets par défaut par un point-virgule. Cela donnera par exemple `https://yak.rhino3d.com;C:\rhino_packages`.
1. Lancez la commande `_GestionnairePaquets` et recherchez l’un des paquets présents dans le nouveau répertoire de paquets.

Pour l’instant, il prend en charge tout ce que Directory.EnumerateFiles() prend en charge, c’est-à-dire, pour autant que je sache, les chemins d’accès ordinaires, les lecteurs mappés (Windows), les chemins UNC (Windows) et les partages de fichiers montés (macOS).

### Conseils pour les dossiers partagés

Sous Windows, utilisez le chemin d’accès UNC, c’est-à-dire `\\server\share\packages`. Si le partage nécessite des informations d’identification, naviguez d’abord vers `\\server` dans l’explorateur, connectez-vous et cochez la case « se souvenir de moi ».

Sous macOS, le partage de fichiers doit d'abord être monté dans Finder via _Aller > Se connecter au serveur..._ (<kbd>⌘</kbd> + <kbd>K</kbd>). Saisissez l’adresse (`smb://server/share`) et, le cas échéant, renseignez les informations d’identification. Maintenant le chemin monté peut être utilisé comme source de paquets, c’est-à-dire `/Volumes/share/packages`. Le montage n’est pas persistant, il faudra donc le remonter plus tard.

### Paramètres bloqués par l’administrateur

Consultez la section [Paramètres bloqués par l’administrateur](https://docs.mcneel.com/rhino/8/help/fr-fr/index.htm#information/admin-enforced_settings.htm) pour savoir comment déployer et appliquer ce paramètre pour les utilisateurs de Windows dans votre organisation.

### Performances

Rhino 8.15 comporte des améliorations de performance significatives pour les répertoires de paquets privés.

L’outil yak.exe dispose d’une nouvelle commande « cache » qui, lorsqu’elle est exécutée dans le dossier des paquets privés, génère un indice des paquets disponibles. Lorsque le gestionnaire de paquets voit ce fichier d’indice, il l’utilise _au lieu_ de parcourir tout le répertoire. Cela réduit considérablement le temps de chargement du Gestionnaire de paquets lorsqu’il s’agit de répertoires privés contenant de nombreux paquets ou des paquets volumineux, ou encore pour les connexions réseau lentes.

```
$ cd X:\private\repo\directory
$ "C:\Program Files\Rhino 8\System\yak.exe" cache

Building cache for local package repository in X:\private\repo\directory

[...]
```

N’oubliez pas de reconstruire le cache si vous ajoutez ou supprimez des fichiers de paquets du répertoire. Supprimez les fichiers _.cache*_ du répertoire pour revenir à l’ancien comportement.

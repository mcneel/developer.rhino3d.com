+++
aliases = ["/en/5/guides/yak/the-anatomy-of-a-package/", "/en/6/guides/yak/the-anatomy-of-a-package/", "/en/7/guides/yak/the-anatomy-of-a-package/", "/en/wip/guides/yak/the-anatomy-of-a-package/"]
authors = [ "will", "callum" ]
categories = [ "Fundamentals" ]
description = "Ce guide explique la structure d’un paquet Yak."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Anatomie d’un paquet"
type = "guides"
weight = 1

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

## Structure d’un paquet

Les paquets sont simplement des fichiers d’archivage ZIP avec une extension .yak. Prenons un exemple simple :

```
howler-0.4.0-any-any.yak
├── manifest.yml
├── Howler.rhp
├── Howler.rui
├── HowlerCommon.dll
├── HowlerGrasshopper.gha
└── misc/
    ├── README.md
    └── LICENSE.txt
```

### À propos du multiciblage .NET

À partir de Rhino 8, Yak prend également en charge les applications multicibles, de sorte que votre module de Rhino puise être exécuté dans .NET Core ou .NET Framework.
Notez que le fichier `manifest.yml` doit maintenant se trouver à l’extérieur du répertoire du framework et non pas à l’intérieur.

```
howler-0.4.0-rh8-any.yak
├── manifest.yml
├── net48/
│  ├── Howler.rhp
│  ├── Howler.rui
│  ├── HowlerCommon.dll
│  ├── HowlerGrasshopper.gha
│  └── misc/
│     ├── README.md
│     └── LICENSE.txt
└── net7.0/
   ├── Howler.rhp
   ├── Howler.rui
   ├── HowlerCommon.dll
   ├── HowlerGrasshopper.gha
   └── misc/
      ├── README.md
      └── LICENSE.txt
```

## Conditions requises

1. Les paquets **doivent** contenir un fichier `manifest.yml` dans le répertoire de premier niveau. 
   Vous trouverez tous les détails concernant le manifeste dans le guide sur le [référencement du manifeste](../the-package-manifest).
1. Tous les modules (fichiers `.rhp`, `.gha`, `.ghpy`) **doivent** se trouver dans le répertoire de premier niveau, ou dans un [répertoire multicible](#a-note-on-net-multi-targeting), afin que Rhino et Grasshopper puissent les trouver et les charger.
1. Les numéros de version des paquets **doivent** soit suivre la [gestion sémantique de version 2.0.0](https://semver.org/lang/fr/) (par exemple `1.1.0-beta`) ou `Système.Version`, connu sous le nom de norme à quatre chiffres de Microsoft (par exemple `1.2.3.4`). Il est recommandé d’utiliser la gestion sémantique de version car cette approche permet aux auteurs de paquets de spécifier des versions préliminaires. C’est pratique pour des essais limités, puisque la dernière version _stable_ est installée par défaut.

## Distributions

Lorsque qu’une version ne contient qu’un seul paquet, il est possible de télécharger plusieurs « distributions » pour cibler différentes versions de Rhino et différentes plateformes. Ces informations sont codées dans une « étiquette de distribution » qui est ajoutée au nom de fichier du paquet, par exemple : _exemple-1.0.0-rh7-win.yak_.

L’étiquette de distribution comprend l’identifiant de l’application et sa version, ainsi que la plateforme. Actuellement, les seules applications prises en charge sont `rh` et `any` (Grasshopper est livré avec Rhino et n’a donc pas besoin de son propre identifiant). A moins que l’application ne soit `any`, une version de l’application doit être indiquée sous la forme `<majeure>_<mineure>`. La version mineure est facultative ; c’est utile si un module dépend d’une modification du SDK apportée dans une version révisée. La plateforme peut être `win`, `mac` ou `any` (c'est-à-dire multiplateforme).

Quelques exemples...

* `rh7-win` - Rhino 7 pour Windows >= 7.0
* `rh6_14-mac` - Rhino 6 pour Mac >= 6.14
* `rh6_9-any` - Rhino 6 (les deux plateformes) >= 6.9
* `any-any` - tout est permis ! (comportement existant)

Lors de l’installation de paquets, le gestionnaire de paquets vérifie si une distribution compatible existe pour la version demandée. Seules les versions de paquets qui ont au moins une distribution compatible apparaissent lorsque l’utilisateur lance la commande `GestionnairePaquets` dans Rhino 7+.

Le serveur mis à jour fonctionne parfaitement avec les paquets existants et les anciennes versions de Rhino. Les versions préexistantes sur le serveur (sans distribution) seront traitées comme `any-any` lors de l’installation. Les nouvelles versions de paquets qui ne comportent pas d’étiquette de distribution, par exemple celles créées par des versions antérieures de l’interface de programmation, seront également traitées comme `any-any` lors de la publication.

## Étapes suivantes

Maintenant que vous avez vu ce que contient un paquet, pourquoi ne pas en créer un ?

* [Créer un paquet Grasshopper](../pushing-a-package-to-the-server) de votre module.
* [Créer un paquet Rhino](../pushing-a-package-to-the-server) pour tout le monde.
* [Créer un paquet multicibles](../creating-a-multi-targeted-rhino-plugin-package) pour Rhino 8.

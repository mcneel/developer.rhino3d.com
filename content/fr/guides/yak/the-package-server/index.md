+++
aliases = ["/en/5/guides/yak/the-package-server/", "/en/6/guides/yak/the-package-server/", "/en/7/guides/yak/the-package-server/", "/en/wip/guides/yak/the-package-server/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Ce guide présente le serveur du Gestionnaire de paquets de Rhino - https://yak.rhino3d.com"
keywords = [ "yak" ]
sdk = [ "Yak" ]
title = "Le serveur de paquets"
type = "guides"
weight = 1
override_last_modified = "2020-08-26T11:56:44Z"

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

Nous hébergeons un serveur de paquets public accessible à tous. Vous n’avez rien à configurer. L’outil CLI de Yak et Rhino savent déjà où aller le chercher.

Les paquets partagés sur le serveur public de paquets peuvent être téléchargés et installés gratuitement. Ils peuvent être libres d’utilisation ou nécessiter une licence (voir les guides sur [Cloud Zoo](/guides/rhinocommon/cloudzoo/cloudzoo-overview/) et [Zoo](/guides/rhinocommon/rhinocommon-zoo-plugins/) pour savoir comment mettre en place une licence dans votre module à l’aide de nos outils).

Vous trouverez ci-dessous quelques informations utiles sur notre serveur de paquets.

## Authentification et autorisation

L’authentification, fournie par [Rhino Accounts](https://accounts.rhino3d.com), n’est requise que pour [publier des paquets](../pushing-a-package-to-the-server) ; pas pour en télécharger ou en installer.

Une fois qu’un auteur de paquet a publié un paquet, il est le seul à pouvoir publier des versions ultérieures en utilisant le même nom de paquet.

{{< call-out "note" "Remarque" >}}
Une fonction permettant d’ajouter des « collaborateurs » sera mise en place dans le futur.
{{< /call-out >}}

## Conventions

Plusieurs conventions s’appliquent au serveur de paquets.

### Noms

Les règles d’attribution de nom pour les paquets sont assez strictes. Seuls les lettres, les chiffres, les tirets intermédiaires et les tirets bas sont admis, par exemple `Hello_World` ou `hello-world1`.

Les noms des paquets prennent la casse utilisée dans la toute première version qui a été téléchargée. Les téléchargements suivants ne tiennent pas compte de la casse du nom du paquet et les requêtes ne tiennent pas compte de la casse.

### Gestion des versions

Les numéros de version des paquets doivent soit suivre la [gestion sémantique de version 2.0.0](https://semver.org/lang/fr/) (par exemple `1.1.0-beta`) ou `Système.Version`, que l’on appelle aussi norme à quatre chiffres de Microsoft (par exemple `1.2.3.4`).

Il est recommandé d’utiliser la gestion sémantique de version car cette approche permet aux auteurs de paquets de spécifier des versions préliminaires. C’est pratique pour des essais limités, puisque la dernière version _stable_ est installée par défaut.

Les numéros de version à quatre chiffres ont été ajoutés dans la v0.8 (août 2019) pour prendre en charge les modules existants qui utilisent des numéros de version de type `System.Version`. Ils ne prennent pas en charge les métadonnées de préversion ou de compilation.

#### Numéros de version partiels et normalisation

Quand un paquet est créé, vous remarquerez peut-être que le numéro de version dans le nom du fichier est différent de celui qui se trouve dans le fichier `manifest.yml`. Cela s’explique par la normalisation des numéros de version. Ce même processus a lieu en coulisses sur le serveur de paquets, afin d’éviter toute ambiguïté entre des versions équivalentes du point de vue sémantique.

Il existe deux cas où des numéros de version peuvent être sémantiquement équivalents :

* Les versions sémantiques qui ne diffèrent que par les métadonnées de compilation[^1], c'est-à-dire `1.0.0+build.1` et `1.0.0+build.2`.
* Une version à quatre chiffres et une version sémantique qui sont identiques à l’exception d’un quatrième chiffre « 0 » (pas de préversion ou de métadonnées de compilation), par exemple `1.2.3` et `1.2.3.0`.

La normalisation est différente de l’expansion des numéros de version partiels (par exemple `1.0`). Les numéros de versions partiels sont développés et stockés sous leur forme complète. Par exemple, si vous téléchargez un paquet en tant que `1.0`, il sera en fait sauvegardé en tant que `1.0.0`. Par la suite, toutes les requêtes (REST, CLI, etc.) recherchant la version `1.0` seront automatiquement redirigées.

[^1]: [_« Les méta-données de construction DEVRAIENT être ignorées dans l’ordre des versions. Autrement dit, deux versions qui diffèrent seulement par leurs informations de construction ont la même priorité. »_](https://semver.org/lang/fr/#spec-item-10)
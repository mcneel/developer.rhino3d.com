+++
aliases = ["/en/5/guides/yak/what-is-yak/", "/en/6/guides/yak/what-is-yak/", "/en/7/guides/yak/what-is-yak/", "/en/wip/guides/yak/what-is-yak/"]
authors = [ "will" ]
categories = [ "Overview" ]
description = "Ce guide présente le Gestionnaire de paquets de Rhino (alias Yak)."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Qu’est-ce que le gestionnaire de paquets ?"
type = "guides"
weight = 1
override_last_modified = "2020-11-12T12:17:36Z"

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

## Présentation

Le gestionnaire de paquets aide à rechercher, à installer et à gérer les ressources dans l’écosystème de Rhino (y compris Grasshopper !). À l’heure actuelle, il prend en charge les modules de Rhino et de Grasshopper, mais l’objectif est qu’il inclue à l’avenir des éléments tels que des scripts, des matériaux, des fenêtres, etc.

{{< call-out "note" "Remarque" >}}
Le gestionnaire de paquets de Rhino a d’abord été désigné par le nom de code « Yak ». Le nom Yak est toujours utilisé pour l’outil de ligne de commande qui crée et publie les paquets.
{{< /call-out >}}

Le gestionnaire de paquets a plusieurs objectifs :

- Aider les utilisateurs à rechercher et à gérer des modules et d’autres éléments ;
- Aider les développeurs et les auteurs de contenu réutilisable à partager leur travail ;
- Fournir des outils d’administration de système simples.

Ne cherchant pas à réinventer la roue, nous nous sommes inspirés de Linux et du monde du développement de logiciels.
 Le système de gestion des paquets peut être décomposé en trois domaines principaux.


1. [Serveur](#server)
2. [Intégrations](#integrations)
3. [Outil de ligne de commande](#command-line-tool)

## Serveur

Le serveur de paquets est le cœur du système. Une fois créés, les paquets sont téléchargés sur le serveur afin d’être partagés.
 Il veille à l’organisation des paquets pour ses clients : l’outil de ligne de commande et Rhino (via des intégrations).


{{< call-out "note" "Remarque" >}}
Outre le serveur de paquets public (https://yak.rhino3d.com), le gestionnaire de paquets prend également en charge les [répertoires de paquets personnalisés](../package-sources) basés sur des fichiers/dossiers.
{{< /call-out >}}

## Intégrations

Les intégrations offrent un accès direct à l’écosystème des paquets au sein de Rhino.
 Actuellement, cela se fait de deux manières : la restauration de paquets pour Grasshopper et l’interface utilisateur du gestionnaire de paquets.


### Restauration de paquets pour Grasshopper

Le gestionnaire de paquets de Rhino a été intégré dans la boîte de dialogue « Unrecognized Objects » de Grasshopper au moyen d’une fonction de [restauration de paquets](../package-restore-in-grasshopper)

. Lorsqu’il ouvre un nouveau fichier contenant des composants appartenant à un module qui n’est pas installé sur sa machine, l’utilisateur a la possibilité d’aller voir sur le serveur de paquets pour trouver les modules manquants et les installer directement.

![Package restore for Grasshopper](/images/yak-gh-restore-guid.gif)

### Interface utilisateur du gestionnaire de paquets

L’interface du gestionnaire de paquets est accessible via la commande `GestionnairePaquets`. Une interface de type NuGet s’ouvre et permet aux utilisateurs de rechercher des paquets, de les installer et de voir si des mises à jour sont disponibles pour les paquets installés.



![The package manager UI](/images/testpackagemanager-wip.jpg)

## Outil de ligne de commande

L’outil de ligne de commande offre une interface basique mais avec toutes les fonctionnalités.
Il s’inspire de gestionnaires de paquets bien connus spécifiques à des domaines, tels que `gem` de Ruby et `pip` de Python.
 Il communique avec le serveur et fait le lien avec Rhino Accounts pour l’authentification.


Sous Windows, l’outil se trouve à l’adresse `"C:\Program Files\Rhino {{< latest-rhino-version >}}\System\yak.exe"`.
Pour Mac, il existe un script, `"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"`.

Tapez `<path_to_yak> help` pour commencer.



## Voir aussi

- [Anatomie d’un paquet](/guides/yak/the-anatomy-of-a-package/)
- [Le manifeste du paquet](/guides/yak/the-package-manifest/)
- [Référence CLI Yak](/guides/yak/yak-cli-reference)

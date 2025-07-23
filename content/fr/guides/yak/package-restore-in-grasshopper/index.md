+++
aliases = ["/en/5/guides/yak/package-restore-in-grasshopper/", "/en/6/guides/yak/package-restore-in-grasshopper/", "/en/7/guides/yak/package-restore-in-grasshopper/", "/en/wip/guides/yak/package-restore-in-grasshopper/"]
authors = [ "will" ]
categories = [ "Features" ]
description = "Comment Grasshopper peut-il utiliser Yak pour vous faciliter la vie ?"
keywords = [ "yak", "grasshopper" ]
sdk = [ "Yak" ]
title = "Restauration de paquets dans Grasshopper"
type = "guides"
weight = 1
override_last_modified = "2020-10-21T15:58:32Z"

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

Tout d’abord, il ne s’agit pas tant d’un guide pour les développeurs que d’une description de la façon dont cet outil fonctionne, afin que vous, en tant que développeur, puissiez mieux comprendre comment votre paquet et votre module doivent être configurés pour en tirer le meilleur parti.



Il peut être frustrant d’ouvrir une définition de Grasshopper et de constater que les modules nécessaires ne sont pas installés.
 Le Gestionnaire de paquets peut aider en rationalisant le processus de résolution de ces dépendances.


Depuis Rhino 6, la boîte de dialogue « Objets non reconnus » offre à l’utilisateur une option permettant de _télécharger et installer_ les modules manquants. Cette fonction de restauration de paquets s’appelle « Package Restore ».

![Grasshopper package restore](/images/yak-gh-restore.gif)

Elle va utiliser le nom, l’ID et la version des modules manquants pour lancer une recherche sur le serveur de paquets. Si des paquets correspondent à la requête, ils seront installés et, si possible, chargés avant d’ouvrir la définition[^3].


<iframe width="560" height="315" src="https://www.youtube.com/embed/MsjRdRtHW08" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Correspondance

### Noms

Dans l’idéal, le nom du module de Grasshopper et celui du paquet doivent correspondre. Si cela n’est pas possible (en raison des contraintes du schéma de dénomination des paquets[^1] ou du fait qu’il existe plusieurs modules dans un paquet et que chacun porte un nom différent) un paquet peut également être identifié à partir de l’ID du module.

Pour chaque fichier .gha, l’ID du module est extrait et ajouté au fichier `manifest.yml` lorsque vous lancez `yak build`.

### Numéros de version

Les numéros de version des paquets peuvent suivre la [gestion sémantique de version 2.0.0](https://semver.org/lang/fr/) (SemVer) ou comporter quatre chiffres[^2], comme dans `System.Version`. Reportez-vous au guide sur le [serveur de paquets](../the-package-server) pour en savoir plus sur les formats de numéro de version autorisés.

Le serveur admet à la fois le format SemVer et celui à quatre chiffres étant donné que certains modules de Grasshopper spécifieront leur numéro de version sous forme de `chaîne de texte` dans une classe dérivée de `GH_AssemblyInfo` alors que d’autres s’appuieront sur `AssemblyVersionAttribute`.

Lors de la restauration des paquets, s’il existe un paquet sur le serveur qui correspond au nom ou à l’ID du paquet manquant, mais que la version exacte n’existe pas, la dernière version stable sera installée.

[^1]: Les règles d'attribution de nom pour les paquets sont relativement strictes. Seuls des lettres, des chiffres, des tirets bas et des tirets intermédiaires sont admis.
[^2]: La prise en charge des numéros de version selon le système à quatre chiffres (`System.Version`) a été ajoutée dans Yak 0.8.
[^3]: Ajouté dans Grasshopper en décembre 2019. Un chargement dynamique n'est possible que si une autre version de la bibliothèque de Grasshopper n'est pas déjà installée et chargée. Autrement, Rhino devra être redémarré pour charger la nouvelle version de la bibliothèque.

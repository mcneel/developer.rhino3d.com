+++
aliases = ["/en/5/guides/yak/the-package-manifest/", "/en/6/guides/yak/the-package-manifest/", "/en/7/guides/yak/the-package-manifest/", "/en/wip/guides/yak/the-package-manifest/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Qu’est-ce qu’un « manifeste de paquet » et que doit-il contenir ?"
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Le manifeste du paquet"
type = "guides"
weight = 1
override_last_modified = "2021-07-21T10:09:56Z"

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

Chaque paquet doit avoir un fichier manifeste contenant des spécifications qui seront résumées dans la base de données lorsque le paquet sera envoyé sur le serveur. Le manifeste doit être écrit en [YAML](http://www.yaml.org), en suivant la structure de l’exemple ci-dessous.

Le fichier manifeste doit être nommé `manifest.yml` et doit se trouver à la racine du paquet (Ne vous inquiétez pas, la [commande `build`](/guides/yak/yak-cli-reference#build) de l’outil Yak CLI se charge de cela pour vous !).

L’objectif du manifeste est de favoriser la rationalisation (et potentiellement l’automatisation) du processus de publication des paquets, en évitant de devoir avoir recours à des formulaires Web pour publier des paquets.

**Attributs requis**
 - [Name](#name)
 - [Version](#version)
 - [Authors](#authors)
 - [Description](#description)

**Attributs recommandés**
 <!-- - [`licence`](#license) -->
 - [URL](#url)
 - [Keywords](#keywords)
 - [Icon](#icon)

<!-- ### Attributs facultatifs
 - [`dépendances`](#dependencies) -->

## Exemple

Voici un exemple de module de Grasshopper.

```yaml
name: plankton
version: 0.3.4
authors:
  - Daniel Piker
  - Will Pearson
description: >
  Plankton is a flexible and efficient library for handling n-gonal meshes.
  Plankton is written in C# and implements the halfedge data structure. The
  structure of the library is loosely based on Rhinocommon's mesh classes and
  was originally created for use within C#/VB scripting components in
  Grasshopper.
url: "https://github.com/meshmash/Plankton"
```

## Attributs requis

### Name

Il s’agit d’un nom court décrivant le paquet. Choisissez de préférence un seul mot ; mais il est aussi possible d’avoir plusieurs mots séparés par des tirets bas ou des tirets intermédiaires.

_**Remarque 1 :** le nom du paquet ne peut contenir que des lettres, des chiffres, des tirets intermédiaires et des tirets bas.

_**Remarque 2 :** les noms des paquets prennent la casse utilisée dans la toute première version qui a été téléchargée. Les téléchargements suivants ne tiennent pas compte de la casse du nom du paquet et les requêtes ne tiennent pas compte de la casse.

```yaml
name: plankton
```

### Version

_Depuis la version 0.8 les numéros de version à quatre chiffres sont autorisés._
_Depuis la version 0.9 vous pouvez utiliser le caractère générique `$version`._

C’est le numéro de version attribué au paquet.

Les numéros de version des paquets **doivent** soit suivre la [gestion sémantique de version 2.0.0](https://semver.org/lang/fr/) (par exemple `1.1.0-beta`) ou `Système.Version`, que l’on appelle aussi norme à quatre chiffres de Microsoft (par exemple `1.2.3.4`). Il est recommandé d’utiliser la gestion sémantique de version car cette approche permet aux auteurs de paquets de spécifier des versions préliminaires. C’est pratique pour des essais limités, puisque la dernière version _stable_ est installée par défaut.

Pour faciliter le processus de création, il est possible de remplacer le numéro de version par `$version`. Le numéro de version sera alors déduit du contenu du paquet et substitué lors du processus de `yak build`.

```yaml
version: 0.3.4
```

### Authors

Liste des auteurs du paquet.

```yaml
authors:
  - Daniel Piker
  # indiquez les autres auteurs du paquet en dessous
  - Will Pearson
```

### Description

Cette section sert à décrire le paquet. À vous de voir si vous souhaitez entrer dans les détails ou être succinct.

```yaml
description: This is an awesome package.
```

Si vous souhaitez en écrire davantage, vous pouvez utiliser la [structure](http://www.yaml.org/spec/1.2/spec.html#id2796251) YAML.

```yaml
description: >
  This is such an awesome package
  that I'm going to write a whole
  bunch of text describing it!

  This sentence will be on a new line.
```

<!-- Ou, si vous voulez garder de nouvelles lignes, utilisez le [style littéral](https://yaml.org/spec/1.2-old/spec.html#id2795688)

```yaml
description: |
  This is the first line of the description.
  This sentence is (and will be) on a new line!
``` -->


## Attributs recommandés

<!-- ### Licence

C’est la licence pour ce paquet. Elle ne doit pas comporter plus de 64 caractères et doit être l’un des [identifiants SPDX](spdx.org/licenses/)standard.

```yaml
license: MIT
```

Si votre intention est de rendre le paquet disponible en open source, l’idéal est d’en choisir une qui est approuvée par l’[Open Source Initiative (OSI)](opensource.org/licenses/alphabetical). Les licences approuvées par l’OSI les plus couramment utilisées sont BSD-3-Clause et MIT. GitHub propose également un sélecteur de licence à l’adresse http://choosealicense.com.

Cela ne devrait être que le nom de votre licence. Le texte complet de la licence doit être inclus dans le paquet sous la forme `LICENSE[.ext]` (au niveau supérieur) lorsque vous le compilez.

Vous devez spécifier une licence pour votre paquet afin que les utilisateurs sachent l’utilisation qu’ils peuvent en faire et les restrictions imposées. Ne pas spécifier de licence signifie que tous les droits sont réservés ; personne n’a le droit d’utiliser le code à quelque fin que ce soit. -->

### URL

Site Web pour le paquet. Il peut s’agir de n’importe quelle URL, par exemple les coordonnées de l’auteur, des forums, des tutoriels ou toute autre information sur le module.

<!-- NOTE: I'm thinking that, where this is a github repository, there is the possibility to build direct from HEAD. -->

```yaml
url: "https://github.com/meshmash/Plankton"
```

### Keywords

Liste de mots clés qui aideront les utilisateurs à trouver le paquet.

```yaml
keywords:
- one
- two
```

### Icon

Fichier d’icône dans le paquet. Il doit être de petite taille (par exemple 64x64) et doit être au format PNG ou JPEG.

```yaml
icon: icon.png
```


<!-- ##Attributs facultatifs -->

<!-- ### Dépendances

Liste de paquets dont dépend ce paquet. Elle peut également inclure des spécifications concernant des versions facultatives, en respectant toujours le principe de gestion sémantique de version.

_Cet attribut n’est pas utilisé actuellement, mais le serveur est capable de stocker des dépendances, il faut donc s’en servir !_

```yaml
dependencies:
  - name: plankton
    spec: "< 0.4.0, >= 0.3.0"
  - name: package_without_spec
​``` -->


<!--## Alternative (JSON)

​```json
{
  "name": "plankton",
  "version": "0.3.4",
  "author": [
    "Daniel Piker",
    "Will Pearson"
  ],
  "dependencies": [

  ],
  "description": "Plankton is a flexible and efficient library for handling n-gonal meshes. Plankton is written in C# and implements the halfedge data structure. The structure of the library is loosely based on Rhinocommon's mesh classes and was originally created for use within C#/VB scripting components in Grasshopper.",
  "license": "LGPL-3",
  "url": "https://github.com/meshmash/Plankton",
  "type": "gh-plugin"
}
``` -->

## Attributs obsolètes

### Icon URL

{{< call-out "warning" "Avertissement" >}}
⚠️ Remplacé par l’attribut <a href="#icon" class="alert-link">icon</a>.
{{< /call-out >}}

Lien **direct** vers une icône qui sera utilisée par le gestionnaire de paquets dans Rhino. Elle doit être de petite taille (32x32 dans l’idéal) et être au format PNG ou JPEG.

```yaml
icon_url: "https://example.com/path/to/icon.png"
```

## Voir aussi

- [Guides et tutoriels pour Yak](/guides/yak/)
- [Anatomie d’un paquet](/guides/yak/the-anatomy-of-a-package/)
- [Référence CLI Yak](/guides/yak/yak-cli-reference)


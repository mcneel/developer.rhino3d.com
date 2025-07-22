+++
aliases = ["/en/5/guides/yak/installing-and-managing-packages/", "/en/6/guides/yak/installing-and-managing-packages/", "/en/7/guides/yak/installing-and-managing-packages/", "/en/wip/guides/yak/installing-and-managing-packages/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "Ce guide explique pas à pas comment installer et désinstaller un paquet Yak en utilisant le CLI."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Installer et gérer des paquets"
type = "guides"
weight = 30
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

{{< call-out "note" "Remarque" >}}
Yak est multiplateforme. Les exemples ci-dessous concernent Windows.
Pour Mac, remplacez le chemin d’accès à l’outil CLI de Yak par
<code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.
{{< /call-out >}}



## Installation

L’installation d’un paquet yak à l’aide de l’outil CLI est simple.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" install marmoset

Downloading marmoset (1.0.0)...
Downloaded marmoset (1.0.0)
Installing marmoset (1.0.0)...
Successfully installed marmoset (1.0.0)
```

{{< call-out "note" "Remarque" >}}
Rhino chargera les nouveaux paquets au prochain démarrage.
{{< /call-out >}}

Vous pouvez également demander à Yak d’installer une version spécifique.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" install marmoset 1.0.0

...
```

Le paquet est installé dans un dossier spécial, similaire au dossier Grasshopper Libraries, mais avec une structure de dossiers/fichiers contrôlée par Yak.



## Désinstallation

Les paquets peuvent aussi être facilement désinstallés à l’aide de l’outil CLI de Yak.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" uninstall marmoset

marmoset successfully uninstalled
```

{{< call-out "note" "Remarque" >}}
Rhino se souviendra que le paquet a été désinstallé au prochain démarrage.

{{< /call-out >}}


## Liste

Vous pouvez à tout moment vérifier quels paquets sont actuellement installés.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" list

marmoset (1.0.0)
```

## Voir aussi

- [Guides et tutoriels pour Yak](/guides/yak/)
- [Créer un paquet pour un module de Grasshopper](/guides/yak/creating-a-grasshopper-plugin-package/)
- [Créer un paquet pour un module de Rhino](/guides/yak/creating-a-rhino-plugin-package/)

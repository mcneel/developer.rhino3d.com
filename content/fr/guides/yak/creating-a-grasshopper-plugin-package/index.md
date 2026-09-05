+++
aliases = ["/en/5/guides/yak/creating-a-grasshopper-plugin-package/", "/en/6/guides/yak/creating-a-grasshopper-plugin-package/", "/en/7/guides/yak/creating-a-grasshopper-plugin-package/", "/en/wip/guides/yak/creating-a-grasshopper-plugin-package/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "Ce guide explique étape par étape comment créer un paquet pour un module de Grasshopper (.gha)."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Créer un paquet pour un module de Grasshopper"
type = "guides"
weight = 10

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

Le [Gestionnaire de paquets](../yak/) a été introduit dans Rhino 7. Il permet à l’utilisateur de rechercher, d’installer et de gérer plus facilement des modules de Grasshopper à partir de Rhino. Ce guide explique comment créer un paquet publiable sur le serveur de paquets à partir d’un module de Grasshopper.

{{< call-out "note" "Remarque" >}}
Le gestionnaire de paquets est multiplateforme. Les exemples ci-dessous concernent Windows.
Pour Mac, remplacez le chemin d’accès à l’outil CLI de Yak par <code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.

{{< /call-out >}}



Tout d’abord, supposons que vous avez sur votre ordinateur un dossier qui contient tous les fichiers que vous souhaitez distribuer dans votre paquet.
 Quelque chose comme cela...

```commandline
C:\Users\Bozo\dist
├── Marmoset.gha
├── icon.png
└── misc\
    ├── README.md
    └── LICENSE.txt
```

{{< call-out "note" "Remarque" >}}
Ce n’est qu’un exemple. Les seuls fichiers qui comptent sont Marmoset.gha et icon.png (nous référencerons l’icône dans le fichier manifest.yml plus tard).
{{< /call-out >}}

Nous allons utiliser l’outil Yak CLI pour créer le paquet ; pour cela, ouvrez une invite de commande et naviguez jusqu’au répertoire ci-dessous.


```commandline
> cd C:\Users\Bozo\dist
```

Maintenant, il nous faut un fichier `manifest.yml` ! Vous pouvez facilement créer le vôtre en vous aidant du [guide de référence du manifeste](../the-package-manifest).
 Vous pouvez aussi utiliser la commande `spec` pour générer un fichier squelette.
 C’est ce que nous allons faire ici.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" spec

Inspecting content: Marmoset.gha

---
name: marmoset
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com


Saved to C:\Users\Bozo\dist\manifest.yml
```

La commande `spec` examine le répertoire actuel et, le cas échéant, glane des informations utiles dans l’ensemble`.gha` et les utilise pour générer un fichier `manifest.yml` pré-rempli avec le nom, la version, les auteurs, etc.

 Si vous n’avez pas fourni ces informations, des caractères de remplissage seront utilisés.


{{< call-out "note" "Remarque" >}}
La commande `spec` est utile pour générer le fichier manifest.yml la première fois.
 Une fois que vous en avez un, enregistrez-le avec votre projet et mettez-le à jour lors de chaque version.

{{< /call-out >}}

Ouvrez le fichier manifeste avec votre [éditeur préféré](https://code.visualstudio.com) et renseignez les champs vides.


Vous devriez ensuite obtenir quelque chose qui ressemble à ceci...

```yaml
---
name: marmoset
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
icon: icon.png
keywords:
- mammal
```

Maintenant que nous avons un fichier manifeste, nous pouvons construire le paquet !

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" build

Building package from contents of C:\Users\Bozo\dist

Found manifest.yml for package: marmoset (1.0.0)
Inspecting content: Marmoset.gha
Creating marmoset-1.0.0-rh6_18-any.yak

---
name: marmoset
version: 1.0.0
authors:
- Will Pearson
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: example.com
keywords:
- mammal
- guid:c9beedb9-07ec-4974-a0a2-44670ddb17e4

C:\Users\Bozo\dist\marmoset-1.0.0-rh6_18-any.yak
├── Marmoset.dll
├── Marmoset.gha
├── manifest.yml
├── misc\LICENSE.txt
└── misc\README.md
```

{{< call-out "note" "Remarque" >}}
Le nom du fichier comprend une <a href="../the-anatomy-of-a-package#distributions" class="alert-link">« étiquette de distribution »</a> (dans ce cas <code>rh6_18-any</code>). La première partie, <code>rh6_18</code>, est déduite de la version de Grasshopper.dll ou Rhinocommon.dll référencée dans le projet de module. La deuxième partie, <code>any</code>, fait référence à la plateforme à laquelle le module est destiné. Pour construire un paquet spécifique à une plateforme, lancez à nouveau la commande <code>build</code> avec l’argument <code>&#45;&#45;platform &lt;platform&gt;</code> où <code>&lt;platform&gt;</code> peut être <code>win</code> ou <code>mac</code>.
{{< /call-out >}}

{{< call-out "warning" "Avertissement" >}}
Actuellement, si vous publiez un paquet avec une étiquette de distribution <code>rh6*</code>, il ne sera pas installable pour Rhino 7. Si votre module fonctionne également sous Rhino 7, indiquez qu’il est compatible en copiant le fichier .yak, en mettant à jour la partie de l’étiquette de distribution du nom de fichier (c’est-à-dire <code>rh6_18</code> ➡ <code>rh7_0</code>) et en <a href="../pushing-a-package-to-the-server" class="alert-link">téléchargeant les deux sur le serveur de paquets</a>.
{{< /call-out >}}

{{< call-out "note" "Remarque" >}}
Vous remarquerez peut-être que le GUID de votre module se cache dans les mots clés.
 Pour en savoir plus à ce sujet, consultez le guide sur la restauration de paquets dans Grasshopper.
<a href="../package-restore-in-grasshopper" class="alert-link">
</a> 
{{< /call-out >}}

Félicitations ! 🙌 Vous venez de créer un paquet pour votre module de Grasshopper.

## Étapes suivantes

Maintenant que vous avez créé un paquet, [téléchargez-le sur le serveur de paquets](../pushing-a-package-to-the-server) afin qu’il soit disponible dans le gestionnaire de paquets !


## Voir aussi

- [Guides et tutoriels sur le gestionnaire de paquets](/guides/yak/)
- [Créer un paquet pour un module de Rhino](/guides/yak/creating-a-rhino-plugin-package/)
- [Restauration de paquets dans Grasshopper](/guides/yak/package-restore-in-grasshopper/)
- [Grasshopper : votre premier composant (Windows)](/guides/grasshopper/your-first-component-windows/)
- [Grasshopper : votre premier composant (Mac)](/guides/grasshopper/your-first-component-mac/)

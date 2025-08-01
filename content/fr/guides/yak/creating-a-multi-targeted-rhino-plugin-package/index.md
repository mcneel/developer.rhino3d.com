+++
aliases = ["/5/guides/yak/creating-a-rhino-plugin-package/", "/6/guides/yak/creating-a-rhino-plugin-package/", "/7/guides/yak/creating-a-rhino-plugin-package/", "/wip/guides/yak/creating-a-rhino-plugin-package/"]
authors = [ "callum" ]
categories = [ "Getting Started" ]
description = "Ce guide explique étape par étape comment créer un paquet pour un module de Rhino (.rhp)."
keywords = [ "developer", "yak", "C#", "multi", "target", "C/C++", "plugin", "installer" ]
sdk = [ "Yak", "C#" ]
title = "Créer un paquet pour un module de Rhino multicible"
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

Le [Gestionnaire de paquets](/guides/yak/) a été introduit dans Rhino 7. Il permet à l’utilisateur de rechercher, d’installer et de gérer plus facilement des modules de Rhino à partir de Rhino. Ce guide explique comment créer un paquet publiable sur le serveur de paquets à partir d’un module de Rhino.

{{< call-out "note" "Remarque" >}}
Le gestionnaire de paquets est multiplateforme. Les exemples ci-dessous concernent Windows.
Pour Mac, remplacez le chemin d’accès à l’outil CLI de Yak par <code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.

{{< /call-out >}}

Tout d’abord, supposons que vous avez sur votre ordinateur un répertoire de compilation qui contient tous les fichiers que vous souhaitez distribuer dans votre paquet multicible.
 Quelque chose comme ce qui suit.

```commandline
C:\Users\Bozo\dist\
├───net48                            
│   │   icon.png                     
│   │   Tamarin.rhp                  
│   └───misc                         
│           License.txt              
│           README.md                
└───net7.0                           
    │   icon.png                     
    │   Tamarin.rhp                  
    └───misc                         
            License.txt              
            README.md                
```

{{< call-out "note" "Remarque" >}}
Ce n’est qu’un exemple. Les seuls fichiers qui comptent sont Tamarin.rhp et icon.png (nous référencerons l’icône dans le fichier manifest.yml plus tard).
{{< /call-out >}}

Nous allons utiliser l’outil Yak CLI pour créer le paquet ; pour cela, ouvrez une invite de commande et naviguez jusqu’au répertoire ci-dessous.


``` commandline
cd C:\Users\Bozo\dist\
```

Maintenant, il nous faut un fichier `manifest.yml` ! Vous pouvez facilement créer le vôtre en vous aidant du [guide de référence du manifeste](../the-package-manifest).
 Vous pouvez aussi utiliser la commande `spec` pour générer un fichier squelette.
 C’est ce que nous allons faire ici.

``` commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" spec

Inspecting content: Tamarin.rhp

---
name: tamarin
version: 1.0.0
authors:
- Park Ranger
description: An example RhinoCommon plug-in
url: https://example.com


Saved to C:\Users\Bozo\dist\manifest.yml
```

La commande `spec` examine le répertoire actuel et, le cas échéant, glane des informations utiles dans l’ensemble`.rhp` et les utilise pour générer un fichier `manifest.yml` pré-rempli avec le nom, la version, les auteurs, etc.

 Si vous n’avez pas fourni ces informations, des caractères de remplissage seront utilisés.


L’inspecteur de modules de RhinoCommon extrait les attributs de l’ensemble que vous avez définis lors de la création de votre module. L’attribut `AssemblyInformationalVersion` est utilisé pour remplir le champ version, puisque cet attribut n’est pas lié à la spécification de version à quatre chiffres de Microsoft et peut contenir une chaîne de version compatible avec SemVer.


 L’attribut `AssemblyVersion` est utilisé comme solution de repli.


{{< call-out "note" "Remarque" >}}
La commande `spec` est utile pour générer le fichier manifest.yml la première fois.
 Une fois que vous en avez un, enregistrez-le avec votre projet et mettez-le à jour lors de chaque version.

{{< /call-out >}}

Ouvrez le fichier manifeste avec votre [éditeur préféré](https://code.visualstudio.com) et renseignez les champs vides.


Vous devriez ensuite obtenir quelque chose qui ressemble à ceci...

``` yaml
---
name: tamarin
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
icon: icon.png
keywords:
- something
```

Maintenant que nous avons un fichier manifeste, nous pouvons construire le paquet !

``` commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" build

Building package from contents of C:\Users\Bozo\dist

Found manifest.yml for package: tamarin (1.0.0)
Inspecting content: Tamarin.rhp
Creating tamarin-1.0.0-rh8_0-any.yak

---
name: tamarin
version: 1.0.0
authors:
- Will Pearson
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
keywords:
- something
- guid:c9beedb9-07ec-4974-a0a2-44670ddb17e4

C:\Users\Bozo\dist\tamarin-1.0.0-rh8_0-any.yak
├── manifest.yml
├── net48/
│   ├── Tamarin.dll
│   ├── Tamarin.rhp
│   ├── icon.png
│   └── misc/
│       ├── License.txt
│       └── README.md
└── net7.0/
    ├── Tamarin.dll
    ├── Tamarin.rhp
    ├── icon.png
    └── misc/
        ├── License.txt
        └── README.md
```

{{< call-out "note" "Remarque" >}}
Le nom du fichier comprend une <a href="../the-anatomy-of-a-package#distributions" class="alert-link">« étiquette de distribution »</a> (dans ce cas <code>rh8_0-any</code>). La première partie, <code>rh8_0</code>, est déduite de la version de Rhinocommon.dll ou Rhino C++ SDK référencée dans le projet du module. La deuxième partie, <code>any</code>, fait référence à la plateforme à laquelle le module est destiné. Pour construire un paquet spécifique à une plateforme, lancez à nouveau la commande <code>build</code> avec l’argument <code>&#45;&#45;platform &lt;platform&gt;</code> où <code>&lt;platform&gt;</code> peut être <code>win</code> ou <code>mac</code>.
{{< /call-out >}}

{{< call-out "note" "Remarque" >}}
Vous remarquerez peut-être que le GUID de votre module se cache dans les mots clés.
 Pour en savoir plus à ce sujet, consultez le guide sur la restauration de paquets dans Grasshopper.
<a href="../package-restore-in-grasshopper" class="alert-link">
</a> 
{{< /call-out >}}

Félicitations ! 🙌 Vous venez de créer un paquet multicible pour votre module de Rhino.

## Étapes suivantes

Maintenant que vous avez créé un paquet, [téléchargez-le sur le serveur de paquets](../pushing-a-package-to-the-server) afin qu’il soit disponible dans le gestionnaire de paquets !


## Voir aussi

- [Créer un paquet pour un module de Grasshopper](/guides/yak/creating-a-grasshopper-plugin-package/)
- [RhinoCommon : votre premier module (Windows)](/guides/rhinocommon/your-first-plugin-windows)
- [RhinoCommon : votre premier module (Mac)](/guides/rhinocommon/your-first-plugin-mac)
- [Créer son premier module C/C++ pour Rhino](/guides/cpp/your-first-plugin-windows/)

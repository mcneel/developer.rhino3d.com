+++
title = "L’interface de ligne de commande RhinoCode"
description = "Ce guide explique comment utiliser l’utilitaire de ligne de commande Rhinocode fourni avec Rhino."
authors = ["ehsan"]

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

<style>
    .main-content img { zoom: 50%; }
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
    }

    .language-plaintext {
        font-size: .9em;
    }
</style>

Rhino3D (>=8.11) est livré avec l’utilitaire de ligne de commande (CLI) `rhinocode` qui permet d’accéder à l’infrastructure de script de Rhino. Cet utilitaire communique avec un serveur de scripts qui fonctionne dans Rhino.

{{< call-out "note" "Remarque" >}}
Pour des raisons de performance, le serveur de scripts n’est pas lancé au démarrage de Rhino. Pour lancer le serveur, utilisez la commande `DémarrerServeurScript`. Si vous voulez forcer le lancement du serveur lors du démarrage de Rhino, ajoutez-la aux commandes de démarrage de Rhino.
{{< /call-out >}}

`rhinocode` a plusieurs fonctions : il peut fournir des informations sur les instances de Rhino en cours d’exécution ; exécuter des scripts de n’importe quel langage pris en charge dans une instance de Rhino ; et enfin, compiler des projets créés dans l’éditeur de scripts de Rhino pour en faire des modules de Rhino et de Grasshopper.

Pour lancer `rhinocode` :

- Assurez-vous que le serveur de scripts est démarré en tapant la commande `DémarrerServeurScript` dans Rhino.

Sous Windows :
- Ajoutez `%PROGRAMFILES%\Rhino 8\System` à la variable d’environnement `PATH` de l’utilisateur ou du système. Ouvrez ensuite un terminal et exécutez `rhinocode`.

Sous macOS :
- Selon le type de shell que vous utilisez, ajoutez `/Applications/Rhino 8.app/Contents/Resources/bin` à la variable d’environnement `PATH`. Ensuite, rechargez le terminal et lancez `rhinocode`.

Si, pour une raison quelconque, vous ne voulez pas modifier la variable d’environnement `PATH`, naviguez jusqu’au dossier d’installation de Rhino dans le terminal et exécutez `.\rhinocode` à partir de là.


Essayez de lancer `rhinocode` en spécifiant l’argument `-V` pour obtenir la version. À l’heure actuelle, la version correspond à la version de Rhino qui livre cet utilitaire :

```text
$ rhinocode -V
8.11.24224
```

## Présentation

Si vous lancez `rhinocode --help`, vous obtiendrez une vue d’ensemble des sous-commandes accompagnées de leurs descriptions (le message peut être différent du message ci-dessous en fonction de la version de l’utilitaire) :


```text
$ rhinocode --help
Usage:  rhinocode [<OPTIONS>] <COMMAND> <ARGUMENTS>

RhinoCode command line interface

Commands:
  list                   List all running instances of Rhino3D
  command                Run given command in Rhino3D
  script                 Run given script in Rhino3D
  project                Manage and publish Rhino3D projects

Options:
  -V, --version                   Print version of this utility
  -v, --verbose                   Enable verbose reporting
  -r, --rhino <RHINO-ID>          Use this instance of Rhino3D (get id from list command)
  -d, --debug                     Debug outputs
  -t, --trace                     Trace outputs

Run 'rhinocode COMMAND --help' for more information on a command
```

Vous pouvez obtenir des informations supplémentaires pour chaque sous-commande en ajoutant l’option `--help` :

```text
$ rhinocode script --help
Usage:  rhinocode script <PATH>

Run given script in Rhino3D

Arguments :
  <PATH>                   Full path of script to be executed

Examples:
  > rhinocode script C:\path\to\script.py
```

## Dresser la liste des instances de Rhino

Utilisez la sous-commande `list` pour obtenir une liste de toutes les instances de Rhino en cours d’exécution. Chaque instance possède un identifiant de processus (PID) et un identifiant unique (ID). Le rapport indique également le nom et le chemin d’accès de tout document ouvert dans l’instance de Rhino afin de faciliter l’identification de chaque Rhino :

Vous pouvez utiliser ID avec l’option `--rhino` pour lancer une sous-commande sur cette instance spécifique de Rhino.

```text
$ rhinocode list
       PID ID                             DOC                  PATH
     75029 rhinocode_remotepipe_75029     Sphere.3dm           C:\path\to\rhinofiles\Sphere.3dm
```

Ajoutez l’option `--json` pour obtenir les résultats en JSON. Cela peut vous permettre d’analyser plus facilement les résultats de cette commande dans vos intégrations personnalisées :

```text
$ rhinocode list --json
[
  {
    "pipeId": "rhinocode_remotepipe_75029",
    "processId": 75029,
    "processName": "Rhinoceros",
    "processVersion": "8.11.24224,1000",
    "processAge": 103,
    "activeDoc": {
      "title": "Sphere.3dm",
      "location": "C:\\path\\to\\rhinofiles\\Sphere.3dm"
    },
    "activeViewport": "Perspective",
    "$meta": {
      "version": "1.0"
    },
    "$type": "status"
  }
]
```
## Exécuter des commandes de Rhino

Utilisez la sous-commande `command` pour exécuter une commande dans une instance de Rhino. Dans l’exemple suivant, la commande `Circle` (Cercle) est exécutée dans Rhino avec quelques arguments pour dessiner un cercle :

```text
$ rhinocode command "_circle 0 0 0 20"
```

Si vous avez plusieurs instances de Rhino en cours d’exécution, vous pouvez spécifier l’instance sur laquelle vous voulez exécuter la commande en utilisant l’option `--rhino` :

```text
$ rhinocode --rhino rhinocode_remotepipe_75029 command "_circle 0 0 0 20"
```

## Exécuter des scripts

Utilisez la sous-commande `script` pour exécuter un script dans une instance de Rhino :

```text
$ rhinocode script C:\path\to\scripts\foo.py
$ rhinocode script C:\path\to\scripts\foo.cs
$ rhinocode script C:\path\to\scripts\foo.py2
```

Si vous avez plusieurs instances de Rhino en cours d’exécution, vous pouvez spécifier l’instance sur laquelle vous voulez exécuter le script en utilisant l’option `--rhino` :

```text
$ rhinocode --rhino rhinocode_remotepipe_75029 script C:\path\to\scripts\foo.py
```

## Travailler avec des projets

{{< call-out "note" "Remarque" >}}
- La commande `project` compile des projets sans avoir besoin d’une instance de Rhino en cours d’exécution. Elle peut être utilisée pour construire des scripts dans votre pipeline CI/CD.
- Consultez les pages [Créer des projets de Rhino](/guides/scripting/projects-create) et [Créer des modules de Rhino et de Grasshopper](/guides/scripting/projects-publish) pour plus d’informations sur la création de projets dans l’éditeur de scripts de Rhino.
{{< /call-out >}}

Utilisez la sous-commande `project` pour travailler avec les projets créés dans l’éditeur de scripts de Rhino.

### Construire un projet

La sous-commande `build` permet de compiler des modules de Rhino et de Grasshopper à partir d’un projet. Le fichier de projet ne contient que des références à des scripts, des définitions de Grasshopper et des bibliothèques, de sorte que ces ressources peuvent être mises à jour en dehors du projet sans modifier le fichier de projet en lui-même. Pour la compilation d’un projet, c’est l’état le plus récent de ces références qui est utilisé.

```text
$ rhinocode project build C:\path\to\projects\MyTools.rhproj
  0% - Preparing project
 10% - Preparing build path
 20% - Preparing plugin assembly
 50% - Preparing grasshopper plugin assembly
 60% - Adding shared resources
 90% - Creating yak package
100% - Complete
```

Pour personnaliser davantage la compilation, utilisez les options suivantes :

- Version de la compilation `--buildversion <BUILD-VERSION>`
- Cible de la compilation `--buildtarget <BUILD-TARGET>`
- Chemin de la compilation `--buildpath <BUILD-PATH>`

Consultez `rhinocode project --help` pour obtenir de plus amples informations et des exemples sur chacune de ces options :

```text
Options:
  -bv, --buildversion <BUILD-VERSION>  Build version formatted as <major>.<minor>
                                       with optional <patch>, <prerelease>, and <build> numbers
                                       formatted as <major>.<minor>.<patch>-<prerelease>+<build>
                                       Examples: 0.1
                                                 0.1.1234
                                                 0.1.1234-beta
                                                 0.1.1234+8989
                                                 0.1.1234-beta+8989

  -bt, --buildtarget <BUILD-TARGET>    Target Rhino version formatted as <major>.<minor>
                                       with optional <operating-system>
                                       formatted as <major>.<minor>-<operating-system>
                                       Examples: 8.*
                                                 8.10
                                                 8.8-macOS
                                                 8.9-mac

  -bp, --buildpath <BUILD-PATH>        Absolute or relative build path
                                       Examples: .\mybuild
                                                 C:\path\to\mybuild
```

Le dossier de compilation (qui dépend de la cible) contiendra les modules générés ainsi qu’un paquet yak qui regroupe les modules et d’autres ressources :

- Paquet Yak : `mytools-0.1.18292.8990-rh8-any.yak`
- Module de Rhino contenant des commandes : `MyTools.rhp`
- Définition de barre d’outils de Rhino : `MyTools.rui`
- Module de Grasshopper contenant des composants : `MyTools.Components.gha`

Utilisez l’utilitaire de ligne de commande `yak` qui est livré avec Rhino pour envoyer le paquet `.yak` sur le serveur de paquets de votre choix.

{{< call-out "note" "Remarque" >}}
Consultez le guide [Envoyer un paquet sur le serveur](/guides/yak/pushing-a-package-to-the-server) expliquant comment publier des fichiers `.yak` sur le serveur de paquets.
{{< /call-out >}}

Pour obtenir un rapport plus détaillé pendant le processus de compilation, utilisez les options `-d|--debug` or `-t|--trace` :

```text
rhinocode -t project build C:\path\to\projects\MyTools.rhproj
```

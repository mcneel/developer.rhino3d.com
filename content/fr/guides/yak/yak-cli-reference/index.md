+++
aliases = ["/en/5/guides/yak/yak-cli-reference/", "/en/6/guides/yak/yak-cli-reference/", "/en/7/guides/yak/yak-cli-reference/", "/en/wip/guides/yak/yak-cli-reference/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Référence pour l’outil de ligne de commande Yak."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Référence pour l’outil de ligne de commande Yak"
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

L’outil de ligne de commande Yak est inclus dans Rhino 7 WIP. Sous Windows, l’outil se trouve sur `"C:\Program Files\Rhino {{< latest-rhino-version >}}\System\yak.exe"`. Pour Mac, il existe un script pratique sur `"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"`.

## Commandes

### Build

* _Depuis la version 0.2 : Commande ajoutée_
* _Depuis la version 0.4 : Prise en charge de plusieurs fichiers .gha, .rhp ou autres_
* _Depuis la version 0.9 : Ajout de l’étiquette de distribution au nom de fichier et extension de l’espace réservé $version_.
* _Depuis 0.10.1 : Ajout de l’argument `--platform`_.

Lorsque cette commande est exécutée dans un répertoire contenant un fichier `manifest.yaml` valide, elle crée un paquet contenant tous les fichiers du répertoire.

```commandline
Utilisation : yak build [options]

Options :
    --platform PLATFORM  La plateforme sur laquelle le paquet sera exécuté ('win', 'mac' ou 'any')
    -h, --help           Obtenir de l’aide (équivalent de `yak help build`)
```

{{< call-out "note" "Remarque" >}}
  Une <a class="alert-link" href="../the-anatomy-of-a-package#distributions">étiquette de distribution</a> (par exemple <code>rh7-win</code>) est ajoutée au nom de fichier du paquet créé. L’étiquette est déterminée au moment de la création du paquet après inspection de son contenu. Si l’auteur souhaite réaliser une distribution multiplateforme, il peut utiliser l’argument <code>&#45;&#45;platform=any</code>, par exemple <code>rh7-any</code>. À l’heure actuelle, seuls les fichiers .rhp et .gha peuvent être inspectés. Si un paquet n’en contient aucun, l’étiquette de distribution associée sera <code>any-any</code>.
{{< /call-out >}}

<!-- Lors de la compilation, le composant GUID est extrait pour faciliter la recherche ultérieure du paquet. -->

### Install

* _Depuis la version 0.1 : Commande ajoutée_
* _Depuis 0.13.0 : Prise en charge de l’installation de fichiers .yak locaux_

Cette commande installe un paquet (éventuellement avec une version spécifique).

```commandline
Utilisation :
    yak install [--source=URL] <package> [<version>]
    yak install <package>
```

Dans cet exemple `<package>` est soit le nom d’un paquet soit le chemin vers un fichier .yak local.

### List

_Depuis la version 0.2 :_

Liste les paquets installés sur la machine

```commandline
yak list
```

### Login

* _Depuis la version 0.2 : Commande ajoutée_
* _Depuis la version 0.10 : Enregistrement de l’utilisateur lors de la connexion_

Cette commande authentifie l’utilisateur avec Rhino Accounts et enregistre un jeton d’accès OAuth2 d’une durée de validité limitée afin que l’utilisateur puisse accéder aux commandes requérant une authentification.

```commandline
Utilisation : yak login [options]

Options :
    --ci              Génère une clé API qui n’expire pas et l’affiche
    -s, --source URL  Emplacement du répertoire du paquet [par défaut : https://yak.rhino3d.com/].
    -h, --help        Obtenir de l’aide (équivalent de `yak help login`)
```

Sous Windows, le jeton est stocké dans `%appdata%\McNeel\yak.yml` ; sous macOS, dans `~/.mcneel/yak.yml`.

Lors de la première connexion, l’utilisateur est enregistré sur le serveur.

{{< call-out "note" "Remarque" >}}
  Dans un environnement de compilation automatisé (par exemple une machine de compilation, GitHub Actions, etc.) l’outil CLI `yak` peut lire le jeton d’accès depuis la variable d’environnement `YAK_TOKEN`. Utilisez l’option `--ci` pour vous connecter et générer un jeton à cet effet !
{{< /call-out >}}

### Push

_Depuis la version 0.1 :_

Envoie un paquet sur le serveur.

```commandline
yak push [--source=URL] <filename>
```

{{< call-out "note" "Remarque" >}}
  Cette commande requiert une <a class="alert-link" href="#login">authentification</a>.
{{< /call-out >}}

### Search

* _Depuis la version 0.1 : Commande ajoutée_
* _Depuis la version 0.5 : Ajout des options `--all` et `--prerelease`.

Cette commande permet de rechercher sur le serveur les paquets qui correspondent à `query`.

```commandline
Utilisation : yak search [options] <query>

  Options :
    --prerelease      Affiche les versions préliminaires du paquet
    -a, --all         Affiche toutes les versions su paquet
    -s, --source URL  Emplacement du répertoire du paquet
    -h, --help        Obtenir de l’aide (équivalent de `yak help search`)
```

### Spec

* _Depuis la version 0.2 : Commande ajoutée_
* _Depuis la version 0.4 : Ajout de la prise en charge de l’inspection des fichiers .rhp (RhinoCommon uniquement)_

Cette commande crée un fichier `manifest.yml` squelette à partir du contenu du répertoire en cours.
Lorsqu’elle est exécutée dans un répertoire contenant un ensemble Grasshopper (`.gha`) ou un module RhinoCommon (`.rhp`), le fichier sera inspecté et utilisé pour préremplir le fichier `manifest.yml`.



```commandline
yak spec
```

### Uninstall

_Depuis la version 0.1_

Cette commande désinstalle un paquet.

```commandline
yak uninstall <package>
```
<!-- option de désactivation supprimée dans la v0.6-->
<!-- {{< call-out "note" "Remarque" >}}
  Depuis la version 0.3, Yak tentera de supprimer le paquet de la machine. Si ce n’est pas possible (probablement parce que Rhino est en cours d’exécution) le paquet sera <em>désactivé</em>.
{{< /call-out >}} -->

### Yank

_Depuis la version 0.6_

Cette commande supprime une version de l’indice du paquet.

```commandline
yak yank <package> <version>
```

{{< call-out "note" "Remarque" >}}
  Cette commande requiert une <a class="alert-link" href="#login">authentification</a>.
{{< /call-out >}}

Les versions occultées n’apparaissent pas dans les recherches ; elles peuvent néanmoins être installées si la version exacte du paquet est connue. Dans tous les cas, elles sont cachées.

Il n’est pas possible d’envoyer de nouveau une version de paquet qui a été occultée. Si vous vous trouvez dans cette situation, vous devrez alors modifier le numéro de version de votre paquet et recommencer.

Si toutes les versions d’un paquet sont supprimées, celui-ci n’apparaîtra plus dans l’indice des paquets.

{{< call-out danger "Danger" >}}
  <p><strong>Suppression d’un paquet du serveur de McNeel</strong></p>
  <p>Si vous devez absolument supprimer votre paquet du serveur public, envoyez un e-mail à <a href="mailto:support@mcneel.com">support@mcneel.com</a>. Une fois qu’un paquet a été supprimé, le nom qu’il portait ne peut plus être utilisé.</p>
{{< /call-out >}}

### Unyank

Fonctionne de la même manière que la commande « yank », mais en sens inverse !

### Owner

_Depuis la version 0.10_

Ajout, suppression ou énumération des propriétaires d’un paquet. Les propriétaires de paquets peuvent envoyer de nouvelles versions du paquet et annuler l’occultation des versions existantes.

```commandline
Utilisation :
    yak owner add [--source=URL] <package> <email>
    yak owner remove [--source=URL] <package> <email>
    yak owner list [--source=URL] <package>
    
Options :
    -h, --help
    -s, --source URL  Emplacement du répertoire du paquet [par défaut : https://yak.rhino3d.com/].
```

Les nouveaux propriétaires peuvent faire tout ce que le propriétaire d’origine peut faire. Tenez-en compte !

Les nouveaux propriétaires doivent être enregistrés sur le serveur avant de pouvoir être ajoutés à un paquet. Pour cela, ils devront exécuter la commande [`login`](#login).

## Téléchargements

Le CLI `yak` est disponible en tant qu’exécutable autonome pour une utilisation dans des environnements où Rhino n’est pas installé, comme sur des machines de compilation automatisées.

* https://files.mcneel.com/yak/tools/0.13.0/yak.exe
* https://files.mcneel.com/yak/tools/0.13.0/win-arm64/yak.exe
* https://files.mcneel.com/yak/tools/0.13.0/mac/yak
* https://files.mcneel.com/yak/tools/0.13.0/linux-x64/yak
* https://files.mcneel.com/yak/tools/0.13.0/linux-arm64/yak


## Voir aussi

- [Guides et tutoriels pour Yak](/guides/yak/)
- [Anatomie d’un paquet](/guides/yak/the-anatomy-of-a-package/)
- [Le manifeste du paquet](/guides/yak/the-package-manifest/)

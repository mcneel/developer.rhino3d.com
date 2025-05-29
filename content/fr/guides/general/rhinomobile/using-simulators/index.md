+++
aliases = ["/en/5/guides/rhinomobile/using-simulators/", "/en/6/guides/rhinomobile/using-simulators/", "/en/7/guides/rhinomobile/using-simulators/", "/en/wip/guides/rhinomobile/using-simulators/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "Ce guide explique les bases de l’utilisation d’émulateurs ou de simulateurs pour déboguer une application mobile."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Utiliser des simulateurs"
type = "guides"
weight = 6

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/simulators_and_emulators"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac" ]
since = 5
until = 7

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true

[_build]
list = "never"
+++

{{< call-out "warning" "RhinoMobile est obsolète" >}}
RhinoMobile n’est plus pris en charge. Les E/S de fichiers 3dm de Rhino restent disponibles sur iOS et Android via la [bibliothèque rhino3dm](https://github.com/mcneel/rhino3dm).
{{< /call-out >}}
 
Android propose des émulateurs et iOS des simulateurs, chacun présentant des avantages et des inconvénients.

## Emulateurs Android

<img align="right" src="/images/using-simulators-01.png" width="121">

Les émulateurs Android se rapprochent beaucoup des appareils réels, bien que leurs performances soient quelque peu variables. L’émulateur Android parvient tout à fait à virtualiser les configurations matérielles et à échouer lorsqu’il le faut (vous pouvez par exemple limiter la quantité de mémoire, d’une manière qui n’est pas possible avec le simulateur iOS). Cela dit, il est toujours important de tester sur des appareils réels, en particulier compte tenu des limitations fonctionnelles de l’émulateur (pas d’interaction multipoint, par exemple) et de la grande variété d’appareils Android sur le marché, avec leurs diverses configurations matérielles et capacités. Une fois correctement configurés, les émulateurs peuvent vous permettre de progresser considérablement dans le processus de développement avant les tests sur des appareils réels.

### Rotation et interaction multipoint

Utilisez les combinaisons de touches suivantes pour faire pivoter les émulateurs :

- <kbd>Fn</kbd> + <kbd>Ctrl</kbd> + <kbd>F12</kbd> = Rotation de l’émulateur (macOS)
- <kbd>Ctrl gauche</kbd> + <kbd>F12</kbd> = Rotation de l’émulateur (Windows)

*Remarque* : il n’est pas possible de simuler plusieurs touches sur l’émulateur Android.

### Système de fichiers de l’émulateur

La meilleure façon d’accéder aux composants internes d’un appareil Android ou d’un émulateur est d’utiliser [Android Debug Bridge](http://developer.android.com/tools/help/adb.html) (adb) qui est fourni avec le SDK Android dans le kit d’outils Xamarin. adb est livré avec un utilitaire de shell qui vous permet de parcourir le système de fichiers Android comme s’il s’agissait d’un système de fichiers Linux standard (ce qui est le cas). L’exécution du shell adb sur un Mac est légèrement différente de celle sur Windows, mais voici les principes de base.

**macOS**

Avant de plonger dans les outils adb, il est important de vérifier que le SDK et le NDK Android font partie de notre environnement de terminal Bash. Ouvrez le fichier *.bash_profile* (dans votre *~* ou dossier personnel) avec un éditeur de texte de confiance (nous recommandons [TextWrangler](http://www.barebones.com/products/textwrangler/) ou [BBEdit](http://www.barebones.com/products/bbedit/)). Ajoutez les lignes suivantes à votre profil si elles n’y figurent pas déjà :

```
export ANDROID_SDK="/Utilisateurs/VotreNom/Library/Developer/Xamarin/android-sdk-mac_x86/"
export ANDROID_NDK="/Utilisateurs/VotreNom/Library/Developer/Xamarin/android-ndk/android-ndk-r8d/"
export PATH="$PATH:$ANDROID_SDK/tools:$ANDROID_SDK/platform-tools:$ANDROID_NDK"
export _JAVA_OPTIONS="-Xmx1g"
```

Les deux premières lignes indiquent à votre environnement Bash où chercher le SDK et le NDK Android. L’option `_JAVA_OPTIONS="-Xmx1g"` augmente la taille du tas que Xamarin Studio peut utiliser pour les binaires natifs Java.

Enregistrez votre profil et ouvrez une fenêtre de Terminal. Vous devriez maintenant pouvoir taper « adb shell ». Si vous n’avez pas d’émulateur en cours d’exécution ni d’appareil branché, vous obtiendrez le message d’erreur suivant : « device not found » (appareil introuvable). C’est parfait, cela signifie que le Shell adb est configuré. Branchez un appareil ou lancez un émulateur et réessayez la commande `adb shell`. Vous devriez maintenant voir quelque chose comme ce qui suit dans votre terminal :

![adb shell](/images/using-simulators-02.png)

Vous pouvez utiliser de nombreuses commandes linux standard pour vous déplacer et manipuler des fichiers. Notez qu’il existe un certain nombre de commandes spéciales permettant d’envoyer et de récupérer des fichiers de l’appareil ou de l’émulateur. Consultez la [documentation sur l’adb d’Android](http://developer.android.com/tools/help/adb.html) pour accéder à une liste pratique. Les données de nombreuses applications sont enregistrées dans le dossier *data/data/NomApp/*.

**Windows**

Avant de plonger dans les outils adb, il est important de vérifier que le SDK et le NDK Android font partie des variables d’environnement. Voici comment faire :

1. Naviguez jusqu’aux *Contrôles du système* dans le Panneau de configuration (*Démarrer* > *Panneau de configuration* > *Système*).
1. Cliquez sur le bouton *Paramètres avancés du système* sur la gauche.
1. Vous vous trouvez à présent dans la fenêtre *Propriétés du système*. Cliquez sur le bouton *Variables d’environnement* dans l’onglet Avancé.
1. Dans l’encadré *Variables système* (l’encadré inférieur), parcourez la liste jusqu’à ce que vous voyiez *Chemin* dans la colonne Variable.
1. Cliquez sur *Chemin* pour le mettre en surbrillance, puis cliquez sur le bouton *Modifier...*.
1. Nous allons ajouter notre chemin vers adb, là où Xamarin a installé le SDK Android. Assurez-vous que votre curseur se trouve à la fin de la dernière entrée, puis tapez : *;C:\Utilisateurs\VotreNom\AppData\Local\Android\android-sdk\platform-tools\* en remplaçant *VotreNom* par le nom de votre compte. Assurez-vous qu’il n’y a pas d’espace dans ce chemin. Si le chemin vers votre android-sdk est personnalisé, remplacez-le par ce chemin.
1. Cliquez sur *OK* pour tout et *fermez le panneau de configuration* s’il est encore ouvert.

Ouvrez une invite de commandes `cmd.exe`. Tapez ensuite `adb shell`. Assurez-vous d’avoir démarré un émulateur ou d’avoir connecté un appareil et vous devriez voir apparaître un outil shell adb similaire à celui présenté ci-dessus dans les instructions pour Mac. Vous pouvez utiliser de nombreuses commandes linux standard pour vous déplacer et manipuler des fichiers. Notez qu’il existe un certain nombre de commandes spéciales permettant d’envoyer et de récupérer des fichiers de l’appareil ou de l’émulateur. Consultez la [documentation sur l’adb d’Android](http://developer.android.com/tools/help/adb.html) pour accéder à une liste pratique. Les données de nombreuses applications sont enregistrées dans le dossier *data/data/NomApp/*.

### Réinitialisation des émulateurs

Il est rarement nécessaire de réinitialiser un émulateur Android étant donné que toute l’application est supprimée entre les versions. Néanmoins, si vous devez le faire, le meilleur moyen est de supprimer tout l’AVD et d’en créer un nouveau à partir de zéro. Ouvrez le gestionnaire d’appareils virtuels Android (Dans Xamarin Studio, allez dans *Tools* > *Open Android Emulator Manager...* dans la barre d’outils Application), dans l’onglet *Android Virtual Devices*, sélectionnez l’émulateur dans la liste des AVD et cliquez sur le bouton *Delete* (supprimer).

## Simulateurs iOS

<img align="right" src="/images/using-simulators-03.png" width="121">

Les simulateurs iOS sont un moyen pratique de tester rapidement votre application avec plusieurs tailles d’écran, plusieurs versions d’iOS et sur différents appareils. Vous pouvez accéder au simulateur en exécutant votre application en mode « Debug » ou « Release » et en sélectionnant un simulateur et des appareils dans le menu déroulant à droite des commandes *Run* et *Configuration*.

<div class="bs-callout bs-callout-danger">
  <h4>ATTENTION</h4>
  <p>Les simulateurs ne remplacent PAS les tests sur un appareil iOS réel. Le comportement et les performances de l’application sur un appareil peuvent varier considérablement par rapport au simulateur, en particulier avec le code OpenGL ES 2.0.</p>
</div>

Pour installer des versions plus anciennes du Simulateur iOS, lancez Xcode, et allez dans *Xcode* > *Preferences* > onglet *Downloads* > section *Components* > *cliquez sur les petites flèches de téléchargement* à droite de la version du simulateur que vous souhaitez installer.

### Rotation et interaction multipoint

Pour effectuer une rotation et simuler plusieurs pressions, utilisez les combinaisons de touches suivantes :

- <kbd>Cmd</kbd> + flèches <kbd>gauche/droite</kbd> = Faire pivoter le simulateur
- <kbd>Option</kbd> + *déplacement du curseur* = Simuler deux pressions
- <kbd>Option</kbd> + <kbd>Maj</kbd> + *déplacement du curseur* = Panoramique à deux doigts

### Système de fichiers du simulateur

Pour accéder au contenu du système de fichiers du simulateur, le plus simple consiste à utiliser un Terminal. Sous macOS, ouvrez une fenêtre Terminal et allez dans :

`~/Developer/CoreSimulator/Devices/<code>/data/Containers/Data/Application/<numéro UDID App>/`

(N’oubliez pas que vous pouvez utiliser la touche Tab pour compléter automatiquement les chemins lorsque vous changez de répertoire. C’est utile pour compléter automatiquement les UDID des applications qui sont très longs).

Vous pouvez également utiliser le Finder pour naviguer dans le même dossier, mais n’oubliez pas de modifier les préférences du Finder pour afficher les fichiers cachés, si vous ne l’avez pas encore fait.

Pour savoir où enregistrer les ressources temporaires ou persistantes, consultez la [documentation de Xamarin](http://docs.xamarin.com/guides/ios/application_fundamentals/working_with_the_file_system/).

### Réinitialisation des simulateurs

Il est souvent nécessaire de nettoyer l’ensemble du contenu du simulateur entre deux compilations, en particulier lorsque vous avez modifié ou supprimé des ressources susceptibles d’être mises en cache sur le simulateur. Si vous souhaitez repartir à zéro, vous pouvez réinitialiser le simulateur aux « paramètres d’usine » virtuels en allant dans *iOS Simulator* > *Reset Content and Settings...* dans le menu *Application*. Notez que cette opération supprime toutes les données de l’application et réinitialise l’UDID de l’application.

## Voir aussi

- [Tester sur des appareils](/guides/rhinomobile/testing-on-devices/)

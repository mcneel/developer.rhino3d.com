+++
aliases = ["/en/5/guides/rhinomobile/your-first-app-windows/", "/en/6/guides/rhinomobile/your-first-app-windows/", "/en/7/guides/rhinomobile/your-first-app-windows/", "/en/wip/guides/rhinomobile/your-first-app-windows/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "Ce guide vous accompagne dans la réalisation de votre première application mobile avec RhinoMobile et Visual Studio sur Windows."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Votre première application (Windows)"
type = "guides"
weight = 5

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/hellorhinomobile"
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

Ce guide suppose que vous avez pris connaissance du guide [Installation des outils (Windows)](/guides/rhinomobile/installing-tools-windows) et que vous avez installé avec succès Xamarin et toutes les bibliothèques requises.  Ces instructions sont données pour des développeurs utilisant Visual Studio 2017 Professional.

## HelloRhinoMobile

Ce guide a été élaboré en considérant que vous utilisez Visual Studio 2017 Professional ; toutefois, le processus décrit devrait également fonctionner pour Visual Studio 2013.

### Build standard pour Android

1. *Lancez Visual Studio* et ouvrez la solution *HelloRhinoMobile*.
1. *Cliquez avec le bouton droit de la souris* sur le projet *HelloRhino.Droid* et sélectionnez *Set As StartUp Project* dans le menu déroulant. *HelloRhino.Droid* devient alors le projet actif pour la génération (HelloRhino.Droid est le projet cible pour Android. Le suffixe .Droid est une convention d’appellation de Mono qui évite les conflits d’espace de noms avec les principales bibliothèques Android).
![hellorhinomobile solution](/images/your-first-app-windows-01.png)
1. Ouvrez le gestionnaire d’émulateurs Android *Android Emulator Manager* et allez dans *Tools* > *Open Android Emulator Manager*. Une fenêtre intitulée *Android Virtual Device (AVD) Manager* devrait apparaître. Cela fait partie du SDK Android et vous le connaissez certainement si vous avez déjà fait du développement Android. C’est ici que vous définissez les appareils virtuels Android (AVD) qui s’exécutent dans l’émulateur.
![avd manager](/images/your-first-app-windows-02.png)
1. Les AVD par défaut sont beaucoup trop lents pour le développement ; *sélectionnez tous les AVD existants* et cliquez sur le bouton *Delete*.
1. Pour créer un nouvel appareil virtuel AVD cliquez sur le bouton *New*. La fenêtre permettant de créer un nouvel appareil virtuel Android (AVD) s’affiche. Créez un nouvel AVD avec les paramètres suivants : *AVD Name* : Nexus7-API17 ; *Device* : Nexus 7 (7.02“, 1200 x 1920:xhdpi) ; *Target* : Android 4.3 - API Level 18 ; *CPU/ABI* : Intel Atom (x86) ; *Skin* : Skin with dynamic hardware controls ; *Front Camera* : Webcam0 ; *VM Heap* : 64 *Emulation Options* : Cochez la case « Use Host GPU »...
![create new avd](/images/your-first-app-windows-03.png)
1. Vous devriez voir votre nouvel AVD dans la liste. Vous venez de créer votre premier AVD. De plus amples informations sur la création d’émulateurs sont disponibles dans la [Documentation Android sur la gestion des dispositifs](http://developer.android.com/tools/devices/index.html). Vous pouvez en créer autant que vous voulez. Le guide [Utiliser des simulateurs](/guides/rhinomobile/using-simulators/) contient des conseils sur l’utilisation de l’émulateur.
1. *Fermez* le *gestionnaire d’AVD* et revenez à *Visual Studio*.
1. Cliquez sur le bouton *Info* dans la barre d’outils Xamarin.Android.
![info button](/images/your-first-app-windows-04.png)
1. La fenêtre *Android Device Logging* s’affiche. Cliquez sur le bouton permettant de changer d’appareil :
![select device window](/images/your-first-app-windows-05.png)
1. Cela fait apparaître la fenêtre *Select Device* qui répertorie tous les appareils en cours d’exécution (émulateurs et dispositifs physiques). Cliquez sur le bouton *Start emulator image*.
![start emulator](/images/your-first-app-windows-06.png)
1. Vous voyez alors la même liste d’images d’AVD disponibles que dans la fenêtre du gestionnaire d’appareils virtuels Android (AVD). Sélectionnez le *Nexus7-API18 AVD* que vous venez de créer. Cliquez sur *OK*.
![select device](/images/your-first-app-windows-07.png)
1. Si tout s’est bien passé, après une brève période de démarrage (croyez-nous, c’est beaucoup plus rapide que les émulateurs standard), vous devriez voir Android démarrer. La première fois, le lancement peut prendre plus de temps et il est fortement recommandé de laisser cette fenêtre ouverte pendant votre session de développement. Une fois qu’Android a démarré, tout est prêt... il vous suffit de déverrouiller l’appareil en faisant glisser le cadenas vers la droite. Nous allons maintenant pouvoir envoyer l’application à l’émulateur.
1. Dans l’explorateur *Solution Explorer*, *cliquez avec le bouton droit de la souris* sur le projet *HelloRhino.Droid* et sélectionnez *Deploy*. HelloRhino.Droid sera généré, ainsi que sa dépendance, RhinoMobile.Droid. (Remarque : La première fois que vous générez RhinoMobile.Droid, la bibliothèque libopennurbs doit être compilée... cela peut prendre jusqu’à 20 minutes. Les générations suivantes seront beaucoup plus rapides).
1. Une fois l’application déployée dans l’émulateur ouvert, vous pouvez l’exécuter. Dans *Visual Studio*, cliquez sur le bouton *Start*. Si tout se passe bien, vous devriez voir quelque chose comme ceci...
![hellorhinomobile android](/images/your-first-app-windows-08.png)

*Félicitations !*  Vous venez de créer une application RhinoMobile pour Android.

### Build standard pour iOS

BIENTÔT DISPONIBLE

## Voir aussi

- [Installation des outils (Windows)](/guides/rhinomobile/installing-tools-windows)
- [Votre première application (Mac)](/guides/rhinomobile/your-first-app-mac)
- [Utiliser des simulateurs](/guides/rhinomobile/using-simulators)
- [Tester sur des appareils](/guides/rhinomobile/testing-on-devices)
- [Gérer des appareils (Documentation Android)](http://developer.android.com/tools/devices/index.html)

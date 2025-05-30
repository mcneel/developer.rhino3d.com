+++
aliases = ["/en/5/guides/rhinomobile/your-first-app-mac/", "/en/6/guides/rhinomobile/your-first-app-mac/", "/en/7/guides/rhinomobile/your-first-app-mac/", "/en/wip/guides/rhinomobile/your-first-app-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "Ce guide vous accompagne dans la réalisation de votre première application mobile avec RhinoMobile et Xamarin Studio sur Mac."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Votre première application (Mac)"
type = "guides"
weight = 4

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
 
Ce guide suppose que vous avez pris connaissance du guide [Installation des outils (Mac)](/guides/rhinomobile/installing-tools-mac) et que vous avez installé avec succès Xamarin Studio, Xcode et toutes les bibliothèques requises.

## HelloRhinoMobile

Nous considérons que vous n’avez jamais utilisé Xamarin Studio et nous allons donc expliquer les étapes une par une.  Au moment où nous écrivons ces lignes, nous utilisons Xamarin Studio 5.9.7.

### Build standard pour iOS

1. *Lancez Xamarin Studio* et ouvrez la solution *HelloRhinoMobile*.
1. *Cliquez avec le bouton droit de la souris* sur le projet *HelloRhino.iOS* et sélectionnez *Set As Startup Project* dans le menu déroulant. *HelloRhino.iOS* devient alors le projet actif pour la génération (HelloRhino.Touch est le projet cible pour iOS.  Les projets HelloRhino.Touch utilisent monotouch.dll qui est l’ancienne version de Xamarin.iOS).
![hellorhinomobile solution](/images/your-first-app-mac-01.png)
1. Vérifiez que le build est paramétré sur *Debug* et l’appareil sur *iPhone Simulator* > *iPhone iOS 5 iOS 9*. Cliquez sur le bouton *Play/Run*.
1. [Activez la version d’essai de Xamarin](http://docs.xamarin.com/guides/cross-platform/getting-started/beginning_a_xamarin_trial). L’édition Xamarin Business vous permet de débloquer une version d’essai de 30 jours. Vous en aurez besoin pour la génération et l’utilisation de RhinoMobile. Vous allez devoir [créer un compte Xamarin](https://auth.xamarin.com/account/register). Si vous n’arrivez pas à activer la version d’essai après avoir créé votre compte, ne vous inquiétez pas, Xamarin Studio vous y invitera lorsque vous essaierez de générer des projets RhinoMobile. Il se peut que vous deviez supprimer le projet et le regénérer si des erreurs continuent à apparaître concernant l’évaluation.
1. *Quittez* et *redémarrez* Xamarin Studio.
1. Sur l’écran d’accueil de Xamarin Studio, ouvrez à nouveau la solution *HelloRhinoMobile*.
1. Vérifiez que l’édition complète de Xamarin Studio a été activée. Allez dans *Xamarin Studio* > *About Xamarin Studio* > *Show Details*. Faites défiler vers le bas et assurez-vous que *Xamarin.iOS* et *Xamarin.Android* sont paramétrés sur *Trial Edition*.
1. Fermez la fenêtre *About Xamarin Studio*.
1. Cliquez à nouveau sur le bouton *Play/Run*. Cette fois, la génération devrait se dérouler sans erreur (Remarque : la première fois que vous générez RhinoMobile.iOS, la bibliothèque libopennurbs doit être compilée. Les générations suivantes seront beaucoup plus rapides). Après avoir téléchargé le paquet d’applications dans le simulateur, vous devriez voir apparaître l’image suivante :
![hellorhinomobile on ios](/images/your-first-app-mac-02.png)
1. Lorsque vous avez fini avec l’exemple de HelloRhino sur le simulateur iOS, cliquez sur le bouton *Stop* dans Xamarin Studio pour arrêter la session de débogage.  Et maintenant, faisons un...

### Build standard pour Android

1. Cliquez avec le bouton droit de la souris sur le projet *HelloRhino.Droid* et sélectionnez *Set As Startup Project* dans le menu déroulant. Comme vous pouvez vous y attendre, cela fait du projet Android le projet par défaut pour la génération...
![hellorhinomobile solution with android](/images/your-first-app-mac-03.png)
1. *Vérifiez que le build est configuré sur Debug.*  Cette fois-ci, la liste déroulante de sélection de l’appareil devrait être désactivée. C’est parce que vous n’avez pas configuré d’émulateur ; nous allons le faire maintenant.
1. Cliquez sur le bouton *Play/Run* pour démarrer le build de débogage *HelloRhino.Droid*. (Remarque : La première fois que vous générez RhinoMobile.Droid, la bibliothèque libopennurbs doit être compilée... cela peut prendre jusqu’à 20 minutes. Les générations suivantes seront beaucoup plus rapides).
1. La fenêtre *Select Device* devrait apparaître. C’est dans cette fenêtre que vous indiquez au SDK Android l’émulateur ou l’appareil que vous souhaitez utiliser pour les tests. Aucune des options par défaut ne nous conviendra ; nous allons donc créer un émulateur plus rapide...
1. Cliquez sur le bouton *Create Emulator*.
1. Le gestionnaire de périphériques virtuels Android (*Android Virtual Device Manager*) devrait s’ouvrir. Il fait partie du SDK Android et vous le connaissez certainement si vous avez déjà fait du développement Android. C’est ici que vous définissez les appareils virtuels Android (AVD) qui s’exécutent dans l’émulateur.
1. *Sélectionnez tous les AVD existants* et cliquez sur le bouton *Delete*. Ces AVD sont beaucoup trop lents pour le développement.
1. Pour créer un nouvel AVD, cliquez sur le bouton *Create*. La fenêtre permettant de créer un nouvel appareil virtuel Android (AVD) s’affiche. Créez un nouvel AVD avec les paramètres suivants : *AVD Name* : Nexus7-API17-IntelHAXM ; *Device* : Nexus 7 ; *Target* : Android 4.2.2 - API Level 17 ; *CPU/ABI* : Intel Atom (x86) ; *Front Camera* : Webcam0 ; *VM Heap* : 64 *Emulation Options* : Cochez la case « Use Host GPU »...
![create new android virtual device](/images/your-first-app-mac-04.png)
1. Vous devriez voir votre nouvel AVD dans la liste. Vous venez de créer votre premier AVD.  De plus amples informations sur la création d’émulateurs sont disponibles dans la [Documentation Android sur la gestion des dispositifs ](http://developer.android.com/tools/devices/index.html). Vous pouvez en créer autant que vous voulez. Le guide [Utiliser des simulateurs](/guides/rhinomobile/using-simulators/) contient des conseils sur l’utilisation de l’émulateur.  Pour l’instant, *quittez le gestionnaire de périphériques virtuels Android* et retournez dans Xamarin Studio.
1. Dans fenêtre *Select Device*, vous devriez à présent voir l’AVD que vous venez de créer dans la liste. Mettez l'AVD en surbrillance et cliquez sur le bouton *Start Emulator*. Si tout s’est bien passé, après une brève période de démarrage (croyez-nous, c’est beaucoup plus rapide que les émulateurs standard), vous devriez voir Android démarrer. La première fois, le lancement peut prendre plus de temps et il est fortement recommandé de laisser cette fenêtre ouverte pendant votre session de développement. Une fois qu’Android a démarré, tout est prêt... il vous suffit de déverrouiller l’appareil en faisant glisser le cadenas vers la droite.
1. Ne fermez pas l’émulateur Android. *Repasser à Xamarin Studio*. Dans la fenêtre *Select Device*, si l’étiquette *not started* n’a pas encore disparu, cliquez sur le bouton *Refresh*. Une fois que vous voyez l’AVD en caractères noirs sélectionnables, vous savez que Xamarin Studio est prêt à lancer l’application sur l’émulateur.  Sélectionnez l’AVD et cliquez sur *OK*.
1. Si tout se passe bien, comme sur iOS, vous devriez voir ce qui suit :
![hellorhino android](/images/your-first-app-mac-05.png)
1. Lorsque vous avez fini avec le build HelloRhino.Droid, cliquez sur le bouton *Stop* dans Xamarin Studio pour arrêter la session de débogage.

*Félicitations !*  Vous avez créé une application RhinoMobile pour deux plateformes avec un seul code.

## Voir aussi

- [Installation des outils (Mac)](/guides/rhinomobile/installing-tools-mac)
- [Votre première application (Windows)](/guides/rhinomobile/your-first-app-windows)
- [Utiliser des simulateurs](/guides/rhinomobile/using-simulators)
- [Tester sur des appareils](/guides/rhinomobile/testing-on-devices)
- [Gérer des appareils (Documentation Android)](http://developer.android.com/tools/devices/index.html)

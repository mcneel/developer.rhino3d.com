+++
aliases = ["/en/5/guides/rhinomobile/installing-tools-mac/", "/en/6/guides/rhinomobile/installing-tools-mac/", "/en/7/guides/rhinomobile/installing-tools-mac/", "/en/wip/guides/rhinomobile/installing-tools-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "Ce guide aborde tous les outils nécessaires pour RhinoMobile sur Mac."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Installation des outils (Mac)"
type = "guides"
weight = 2

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/getting-started"
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
 
À la fin de ce guide, vous devriez avoir installé tous les outils nécessaires pour créer, construire et déboguer des applications mobiles en C# à l’aide de RhinoMobile dans Xamarin Studio.

## Conditions préalables

Si vous ne l’avez pas encore fait, veuillez lire le guide [Qu’est-ce que RhinoMobile ?](/guides/rhinomobile/what-is-rhinomobile/)

Ce guide suppose que vous disposez d’un :

- [Apple Mac](http://store.apple.com/) fonctionnant sous [OS X Yosemite](https://www.apple.com/osx/) (10.10) ou une version ultérieure.

## Installer Xcode

[Xcode](https://developer.apple.com/xcode/) est la plateforme de développement et l’environnement de développement intégré (IDE) d’Apple.

#### Pas à pas

1. *[Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)* est téléchargeable gratuitement depuis l’[App Store de Mac](https://itunes.apple.com/us/app/xcode/id497799835?mt=12).  Cliquez sur le bouton *Voir dans l’App Store sur Mac*.
1. Cliquez sur le bouton *Obtenir* > *Installer App* sous l’icône Xcode.
1. Vous devrez indiquer votre [ID Apple](https://appleid.apple.com/) (nécessaire pour télécharger des applications dans l’App Store).
1. Xcode est volumineux (près de 2,6 Go).  Vous pouvez suivre la progression du téléchargement dans le Launchpad.  Une fois le téléchargement et l’installation d’Xcode terminés, vous le trouverez dans votre dossier */Applications*.
1. *Lancez* Xcode.  Lors du lancement initial, Xcode installera des composants supplémentaires.
1. *Quittez* Xcode.

## Installer Xamarin

La plateforme Xamarin est actuellement nécessaire pour créer des applications RhinoMobile.  Consultez le guide intitulé [Qu’est-ce que Mono et Xamarin ?](/guides/rhinocommon/what-are-mono-and-xamarin/) pour plus d’informations.

#### Pas à pas

1. *[Téléchargez la plateforme Xamarin](http://xamarin.com/download)*.
1. Xamarin utilise une application d’installation, qui télécharge et installe les composants que vous sélectionnez.  Une fois que vous avez téléchargé le fichier *XamarinInstaller.dmg*, double-cliquez dessus pour monter l’image disque.  Double-cliquez sur la grande icône *Install Xamarin* pour lancer le programme d’installation.
1. Vous devez accepter le contrat de licence du logiciel Xamarin pour utiliser la plateforme Xamarin.
1. La *Plateforme Xamarin* comprend les éléments suivants :
   - Xamarin Studio
   - Xamarin.Android[^1]
   - Xamarin.iOS[^2]
   - Xamarin.Mac[^3]
...vérifiez que *Xamarin.Android* et *Xamarin.iOS* sont cochés et cliquez sur *Continuer*.
1. Si Xcode n’est pas installé sur votre ordinateur, Xamarin vous demandera de le faire.  Reportez-vous à la section [Installer Xcode](#install-xcode) ci-dessus.
1. Xamarin installe *Mono Framework*, *Xamarin Studio*, *Xamarin.Android* et *Xamarin.iOS*.  Cliquez sur *Continuer*.
1. Xamarin est maintenant téléchargé et installé.  Selon les produits que vous avez sélectionnés à l'étape 4 ci-dessus, cette opération peut prendre un certain temps.
1. Une fois l’installation terminée, cliquez sur le bouton *Launch Xamarin Studio*.
1. *Xamarin Studio*, ainsi que Mono Framework, Xamarin.Android et Xamarin.iOS, sont maintenant installés.
1. Xamarin Studio est installé dans votre dossier */Applications*. Nous vous recommandons de faire un *glisser-déposer de l’icône de Xamarin Studio vers votre Dock* pour y accéder ensuite facilement (si le programme est en cours d’exécution, faites un clic droit sur l’icône dans le Dock et sélectionnez *Garder dans le Dock*).

## Mettre à jour le SDK Android

Une fois que Xamarin Studio a été mis à jour, vous devez aller chercher les mises à jour du SDK Android.

#### Pas à pas

1. Dans *Xamarin Studio*, allez dans *Tools* > *Open Android SDK Manager...*.
1. Dans la fenêtre *Android SDK Manager*, attendez que le gestionnaire ait fini de récupérer le manifeste de mise à jour.
1. En fonction de la date à laquelle vous avez téléchargé les outils Xamarin, vous devrez installer l’API la plus récente (21 au moment de la rédaction de cet article) ainsi que les deux dernières (20 et 19) pour une compatibilité descendante. Cochez les cases à côté des noms et cliquez sur le bouton *Install N packages...*.
1. Une fenêtre (remplie de bugs) s’affiche dans laquelle vous devez accepter toutes les licences de chaque élément avant de continuer. Si vous ne parvenez pas à faire fonctionner le bouton *Install*, quittez la fenêtre, ouvrez-la à nouveau et acceptez différentes licences en cochant une par une les cases sur la gauche jusqu’à ce que cela fonctionne.
![android sdk](/images/rhinomobile-installing-tools-mac-01.png)
1. *Remarque :* les téléchargements peuvent prendre un certain temps en fonction de votre connexion à Internet.

## Installer Intel HAXM

[Intel HAXM est le gestionnaire d’exécution de l’accélération matérielle d’Intel](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/).  HAXM est un moteur de visualisation assistée par matériel pour les émulateurs Android x86. Sans HAXM, les émulateurs sont presque inutilisables, tant leurs performances sont faibles. Cependant, avec HAXM, les émulateurs x86 sont réactifs et utiles. Ils ne sont pas aussi rapides qu’un appareil réel, mais ils permettent de tester les applications de manière satisfaisante. Vous pouvez l’installer à partir du gestionnaire SDK Android, mais la version disponible est inefficace. Nous vous recommandons plutôt de cliquer sur le lien ci-dessus.  HAXM ne fonctionne pas dans un environnement virtualisé, par exemple une VM. Si vous réalisez votre développement Android sur une VM Windows, vous devrez utiliser un dispositif.

#### Pas à pas

1. Visitez le site Internet [Intel Hardware Acceleration Execution](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/).
1. Trouvez la section *macOS* de la page.
1. Téléchargez le fichier *haxm-macosx_rxx.zip*.  Vous devrez peut-être accepter un accord de licence avant de commencer le téléchargement.
1. Décompressez *haxm-macosx_rxx.zip*.
1. Montez *IntelHAXM_x.x.x.dmg* en double-cliquant dessus.
1. Installez le HAXM en double-cliquant sur le fichier *IntelHAXM_x.x.x.mpkg*.

## Cloner RhinoCommon

RhinoMobile est construit autour de la branche [rhino3dmio de RhinoCommon](https://github.com/mcneel/rhinocommon/tree/rhino3dmio). Vous pouvez télécharger RhinoCommon sous la forme d’un fichier compressé ou cloner le répertoire avec Git (recommandé). (Si vous ne connaissez pas GitHub, il existe une application [GitHub Mac Desktop](https://desktop.github.com/) pour vous aider à démarrer).

#### Pas à pas

1. Décompressez ou clonez *[rhinocommon (branche rhino3dmio)](https://github.com/mcneel/rhinocommon/tree/rhino3dmio)* dans un dossier approprié, tel que le dossier */Utilisateurs/VotreNom/Development/Repositories/rhinocommon* :
![clone rhinocommon](/images/rhinomobile-installing-tools-mac-02.png)
1. *Téléchargez [openNURBS](http://www.rhino3d.com/download/opennurbs/5.0/commercial)*. RhinoMobile nécessite le SDK C++ openNURBS.
1. Décompressez openNURBS et placez le contenu dans le dossier *rhinocommon/c/opennurbs/* (le dossier contenant uniquement le fichier *readme.md*) :
![opennurbs](/images/rhinomobile-installing-tools-mac-03.png)

## Cloner RhinoMobile

Vous devez télécharger ou cloner les répertoires [RhinoMobile](http://github.com/mcneel/RhinoMobile) et [RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples). (Si vous ne connaissez pas GitHub, il existe une application [GitHub Mac Desktop](https://desktop.github.com/) pour vous aider à démarrer).

#### Pas à pas

1. Décompressez ou clonez *[RhinoMobile](http://github.com/mcneel/RhinoMobile)* dans un dossier *parallèle à rhinocommon* (cloné précédemment). Par exemple, si *rhinocommon* se trouve dans le dossier     */Utilisateurs/VotreNom/Development/Repositories/rhinocommon*, RhinoMobile se trouvera dans le dossier */Utilisateurs/VotreNom/Development/Repositories/RhinoMobile* :
![rhinomobile](/images/rhinomobile-installing-tools-mac-04.png)
1. Décompressez ou clonez *[RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples)* dans un dossier *parallèle à rhinocommon* et *RhinoMobile* :
![rhinomobilesamples](/images/rhinomobile-installing-tools-mac-05.png)

## Étapes suivantes

*Félicitations !*  Vous disposez maintenant de tous les outils nécessaires pour créer une application mobile utilisant RhinoMobile.  *Et maintenant ?*

Consultez le guide [Votre première application (Mac)](/guides/rhinomobile/your-first-app-mac) dans lequel vous trouverez des instructions pour créer (vous l’aurez deviné) votre première application.

## Voir aussi

- [Qu’est-ce que RhinoMobile ?](/guides/rhinomobile/what-is-rhinomobile/)
- [Qu’est-ce que RhinoCommon ?](/guides/rhinocommon/what-is-rhinocommon/)
- [Que sont Mono et Xamarin ?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Installation des outils (Windows)](/guides/rhinomobile/installing-tools-windows/)
- [Votre première application (Mac)](/guides/rhinomobile/your-first-app-mac)

**Notes de bas de page**

[^1]: Xamarin.Android permet de créer des applications .NET en C# pour les appareils Android.

[^2]: Xamarin.Android permet de créer des applications .NET en C# pour les appareils Apple iOS.

[^3]: Xamarin.Mac est la boîte à outils à source fermée appartenant à Xamarin, construite sur le logiciel libre MonoMac (alias Mono pour macOS).  Xamarin.Mac fournit une licence commerciale de Mono, des liaisons avec d'autres frameworks et la possibilité de créer des ensembles d'applications autonomes qui ne nécessitent pas Mono.  À l'heure actuelle, RhinoMobile n'utilise pas Xamarin.Mac.

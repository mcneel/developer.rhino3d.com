+++
aliases = ["/en/5/guides/rhinomobile/testing-on-devices/", "/en/6/guides/rhinomobile/testing-on-devices/", "/en/7/guides/rhinomobile/testing-on-devices/", "/en/wip/guides/rhinomobile/testing-on-devices/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "Ce guide vous aide à configurer des appareils pour tester des applications mobiles."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Tester sur des appareils"
type = "guides"
weight = 7

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/devices_and_testing"
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
 
## Appareils Android

Pour déboguer votre code sur un appareil Android, vous devez activer le débogage USB sur l’appareil. Ce mode rend votre appareil un peu plus vulnérable aux dommages, qu’ils soient causés par vous ou par d’autres, et doit donc être utilisé avec prudence. Vous pouvez l’activer lorsque vous en avez besoin, puis le désactiver entre les sessions de développement si vous le souhaitez.

#### Appareils Android 4.0 (JellyBean - API 14) ou version supérieure

Activez l’option *USB Debugging* sous *Settings* > *Developer options*.

Par défaut, pour Android 4.2 et les versions plus récentes, *les options pour les développeurs sont cachées*. Vous devez donc procéder comme suit :

1. Sur l’appareil, allez dans *Settings* > *About* <appareil>.
1. Appuyez sept fois sur le *numéro de build*. Les options *Settings* > *Developer* deviennent alors disponibles.
1. Activez ensuite l’option *USB Debugging*.

Sous Windows, il est parfois nécessaire de basculer votre appareil en mode Appareil photo (PTP) plutôt qu’en mode Appareil multimédia (MTP). Pour cela, suivez ces étapes :

1. Sur l’appareil, allez dans *Paramètres* > *Stockage* > *Plus d’options (...)* > *Connexion USB de l’ordinateur*.
1. Passez de *Dispositif multimédia (MTP)* à *Appareil photo (PTP)*.

#### Tablettes Fire

Sur l’appareil, sélectionnez *Paramètres* > *Sécurité* et activez l’option « Activer ADB ».

Pour plus d’informations, voir la [Documentation pour les développeurs d’Amazon](https://developer.amazon.com/sdk/fire/connect-adb.html#Connecting).

Vous pouvez également désactiver la mise en veille, afin d’empêcher votre appareil Android de passer en veille lorsqu’il est branché sur le port USB.

## Appareils iOS

Les appareils iOS doivent être enregistrés auprès d’Apple avant de pouvoir les utiliser pour le développement ou les tests. On appelle ce processus le provisionnement d’appareils. Suivez les instructions de Xamarin pour préparer votre appareil iOS.

Une fois votre appareil provisionné et connecté via USB, vous pouvez exécuter et déboguer votre application à partir de Xamarin Studio ou de Visual Studio (via l’hôte Build Mac).

La meilleure manière de tester votre application est sur un appareil. Les quatre domaines dans lesquels les appareils diffèrent le plus du simulateur sont les suivants :

1. Connexions et connectivité
1. Services de localisation
1. *Mémoire*
1. *OpenGL ES*

Les deux derniers sont les plus importants pour les applications RhinoMobile. Les grands maillages dans les fichiers .3dm peuvent consommer beaucoup de mémoire ; le simulateur essaiera de déclencher des avertissements « OutOfMemory », mais ils ne seront pas aussi cohérents (ou réalistes) que si vous exécutez et déboguez votre application sur un appareil. Enfin, les appels E/S OpenGL seront interprétés différemment sur le simulateur et sur l’appareil. Il se peut qu’un code fonctionne sur le simulateur et ne fonctionne pas sur tous les appareils.

## Voir aussi

- [Utiliser des simulateurs](/guides/rhinomobile/using-simulators/)

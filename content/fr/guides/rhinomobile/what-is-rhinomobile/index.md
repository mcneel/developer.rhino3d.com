+++
aliases = ["/en/5/guides/rhinomobile/what-is-rhinomobile/", "/en/6/guides/rhinomobile/what-is-rhinomobile/", "/en/7/guides/rhinomobile/what-is-rhinomobile/", "/en/wip/guides/rhinomobile/what-is-rhinomobile/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "Ce guide offre une vue d’ensemble de RhinoMobile."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Qu’est-ce que RhinoMobile ?"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile"
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
 
{{< image url="/images/rhinomobile-overview-01.png" alt="/images/rhinomobile-overview-01.png" class="float_right" width="325" >}}

RhinoMobile est une bibliothèque .NET C# pour le développement d’applications mobiles 3D multi-plateformes. RhinoMobile, comme RhinoCommon, est basé sur le framework Xamarin Mono, un runtime .NET entièrement fonctionnel utilisable sur Android, iOS et macOS. RhinoMobile utilise openNURBS (la bibliothèque 3dm NURBS) et RhinoCommon (le SDK .NET pour Rhinoceros et Grasshopper) et gère les E/S de fichiers, la reconnaissance des gestes et l’affichage 3D (OpenGL ES 2.0). Il ne s’agit pas de la totalité de RhinoCommon, mais d’un sous-ensemble.

## Qui devrait l’utiliser ?

Toute personne intéressée par le développement et le prototypage ou souhaitant simplement s’essayer au développement mobile 3D. Bien qu’il existe de nombreuses bibliothèques 3D de qualité pour les jeux mobiles, aucune n’est dédiée à la modélisation et à la conception 3D. L’objectif de RhinoMobile est de combler cette lacune. Si vous souhaitez développer en C# et cibler le plus grand nombre d’appareils possible, cette bibliothèque est faite pour vous. Aucune expérience en matière de développement mobile n’est nécessaire... il suffit d’avoir une bonne connaissance de C# et .NET.

## Où puis-je obtenir de l’aide ?
{{< div class="clear_both" />}}
Visitez le [Forum de Rhino](http://discourse.mcneel.com/) et posez votre question dans la [catégorie Rhino Developer](http://discourse.mcneel.com/c/rhino-developer) ; n’oubliez pas de @mentionner le développeur @dan.

## Téléchargements et liens

### Outils pour les développeurs

- [Plateforme Xamarin](http://xamarin.com/download). Pour utiliser RhinoMobile, vous devez posséder une version d’essai gratuite de 30 jours de l’édition Business (Xamarin propose des prix réduits pour les étudiants).
- [Xcode](http://developer.apple.com/xcode/) sur un Mac fonctionnant sous OS X 10.8 (Mountain Lion) ou une version supérieure pour la création d’applications iOS.
- [Visual Studio 2012](http://https//www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx) ou une version supérieure : éditions non Express uniquement (les extensions de Xamarin nécessitent des versions payantes).
- [Intel Hardware Accelerated Execution Manager (HAXM)](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/) qui permet aux émulateurs Android de fonctionner plus rapidement et plus efficacement.

### Bibliothèques et échantillons

- [RhinoCommon (branche rhino3dmio)](https://github.com/mcneel/rhinocommon/tree/rhino3dmio) : le kit de développement logiciel (SDK) .NET pour Rhino et Grasshopper.
- [openNURBS](http://www.rhino3d.com/opennurbs) : pour télécharger SDK openNURBS C++.
- [RhinoMobile](http://github.com/mcneel/RhinoMobile) : pour télécharger ou cloner la bibliothèque RhinoMobile.
- [RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples) : pour télécharger ou cloner quelques exemples de projets qui utilisent RhinoMobile.

## FAQ

**RhinoMobile est-il gratuit ?**

Oui.

**Puis-je vendre les applications que je développe avec RhinoMobile ?**

Oui.

**Les applications créées avec RhinoMobile fonctionneront-elles sur les ordinateurs Mac et Windows ainsi que sur les dispositifs mobiles ?**

Non, avec une réserve : bien que nous ne l’ayons pas encore ajouté à la bibliothèque, nous prévoyons de prendre en charge Windows Phone, qui utilise DirectX comme pipeline d’affichage et peut être exécuté (avec certaines limitations) en tant qu’ « application du Windows Store » (que l’on appelle aussi App Metro UI).

**Les développeurs de McNeel utilisent-ils RhinoMobile pour développer iRhino 3D ?**

Bien-sûr !

**Mais attendez, dans RhinoMobile il y a tout RhinoCommon ?**

Non. RhinoMobile utilise un sous-ensemble de RhinoCommon (rhino3dmio), dont les limites sont définies par le symbole : MOBILE_BUILD. Il y a beaucoup de choses dedans : Rhino.DocObjects, Rhino.Geometry, Rhino.FileIO... à peu près tout ce dont vous avez besoin pour lire, écrire et dessiner dans Rhino 3dm.

**Je ne peux donc probablement pas effectuer de maillage ou exécuter une commande Dessin2D ?**

Désolé, pas encore. Compte tenu des contraintes liées aux processeurs des plateformes mobiles, vous consommeriez probablement toute votre batterie si vous le faisiez.

## Étapes suivantes

Si vous êtes prêt à commencer avec RhinoMobile, vérifiez tout d’abord que vous avez bien installé tous les outils.  Lisez :

- [Installation des outils (Mac)](/guides/rhinomobile/installing-tools-mac/) ; ou
- [Installation des outils (Windows)](/guides/rhinomobile/installing-tools-windows/)

## Voir aussi

- [Qu’est-ce que RhinoCommon ?](/guides/rhinocommon/what-is-rhinocommon/)
- [Installation des outils (Mac)](/guides/rhinomobile/installing-tools-mac/)
- [Installation des outils (Windows)](/guides/rhinomobile/installing-tools-windows/)

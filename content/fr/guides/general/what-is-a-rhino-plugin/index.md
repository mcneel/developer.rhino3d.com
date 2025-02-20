+++
aliases = ["/en/5/guides/general/what-is-a-rhino-plugin/", "/en/6/guides/general/what-is-a-rhino-plugin/", "/en/7/guides/general/what-is-a-rhino-plugin/", "/en/wip/guides/general/what-is-a-rhino-plugin/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "Ce guide explique ce que sont les modules de Rhino et comment ils se présentent."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Qu’est-ce qu’un module de Rhino ?"
type = "guides"
weight = 3
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/developer/whatisarhinoplugin"
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


Un module de Rhino est un module logiciel qui étend les fonctionnalités de Rhino ou de Grasshopper en ajoutant des commandes, des fonctions ou des options.  Un module de Rhino est une bibliothèque de liens dynamiques, ou DLL.

Sous Windows, un module de Rhino construit avec le [SDK C/C++](/guides/cpp/what-is-the-cpp-sdk/) est une DLL ordinaire utilisant une DLL MFC partagée.

Sous Windows et Mac, un module de Rhino construit avec le [SDK RhinoCommon](/guides/rhinocommon/what-is-rhinocommon/) est un assemblage .NET.

Parmi les exemples de modules de Rhino, on trouve [Grasshopper](http://www.grasshopper3d.com), [Brazil](http://brazil.rhino3d.com/), [Flamingo](http://nxt.flamingo3d.com/) ou encore [Bongo](http://bongo.rhino3d.com/).  Visitez [food4rhino.com](http://www.food4rhino.com/) pour voir d’autres exemples.


## Types de modules

Rhino prend en charge cinq types de modules différents :

1. *Utilité générale* : utilitaire général qui peut contenir une ou plusieurs commandes.
1. *Importation de fichiers* : module qui importe dans Rhino des données provenant d’autres formats de fichiers ; il peut prendre en charge plusieurs formats.
1. *Exportation de fichiers* : module qui exporte les données de Rhino vers d’autres formats de fichiers ; il peut prendre en charge plusieurs formats.
1. *Rendu personnalisé* : module qui applique des matériaux, des textures et des lumières à une scène pour produire des rendus.
1. *Numérisation 3D* : module qui fait interface avec les dispositifs de numérisation 3D, tels que ceux fabriqués par MicroScribe, Faro et Romer.

***Remarque*** : les modules d’importation et d’exportation de fichiers, de rendu personnalisé et de numérisation 3D sont tous des améliorations spécialisées du module d’utilité générale.  Ainsi, tous les types de modules peuvent contenir une ou plusieurs commandes.


## Compatibilité des modules

Pour que Rhino puisse charger et exécuter votre module avec succès, plusieurs conditions sont requises :

1. Le numéro « RhinoSdkVersion » de votre module doit correspondre à la « RhinoSdkVersion » de Rhino.
1. Le numéro « RhinoSdkServiceRelease » de Rhino doit être supérieur ou égal au numéro « RhinoSdkServiceRelease » de votre module.

Nous apportons occasionnellement des modifications à nos SDK.  Lorsque nous le faisons, nous modifions le numéro « RhinoSdkServiceRelease ».  

En tant que développeur de modules, il est peu probable que vous rencontriez un problème avec la première condition.  Cela se produirait, par exemple, si un utilisateur essayait de charger dans Rhino 4 un module conçu pour Rhino 6.

Cependant, vous pouvez parfois rencontrer des problèmes avec la deuxième condition.  Si vous avez compilé votre module en utilisant le SDK 6.2 (RhinoSdkVersion.RhinoSdkServiceRelease) et qu’un utilisateur travaillant avec Rhino 6.1 essaie de l’exécuter, un message d’erreur s’affichera et le module ne pourra pas être chargé.  Si votre client reçoit ce message, il doit se procurer la dernière version de Rhino (6.2 ou une version supérieure, dans cet exemple) et cela devrait résoudre le problème.

## Voir aussi

- [Conditions préalables pour les développeurs](/guides/general/rhino-developer-prerequisites)

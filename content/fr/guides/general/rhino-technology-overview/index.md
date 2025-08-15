+++
aliases = ["/en/5/guides/general/rhino-technology-overview/", "/en/6/guides/general/rhino-technology-overview/", "/en/7/guides/general/rhino-technology-overview/", "/en/wip/guides/general/rhino-technology-overview/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "Résumé de l’architecture de la technologie de Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Vue d’ensemble de la technologie de Rhino"
type = "guides"
weight = 0

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


## Vue d’ensemble

Rhinocéros est composé de nombreuses couches, écrites dans plusieurs langages, toutes empilées les unes sur les autres.  S’il est vrai que les couches les plus fondamentales sont celles qui sont situées à la base, les couches supérieures ne doivent pas pour autant être considérées comme superficielles.

![The Rhino Stack](/images/rhino-technology-overview-01.png)

Examinons ces différentes couches les unes après les autres, en commençant par la base.

## La base

### Le noyau C++ de Rhino

Le noyau C++ de Rhino est l’ensemble de code le plus ancien et le plus vaste.  Nous utilisons MFC de Microsoft pour certaines parties y compris le SDK.  C’est là que le document de l’environnement d’exécution est géré, que tout le code de dessin de la fenêtre OpenGL existe et que le code de géométrie computationnelle écrit par nos mathématiciens vit.  C’est aussi là que se trouvent la plupart des commandes de Rhino.

Dans le noyau de Rhino, il y a également une grande partie de l’interface utilisateur : la ligne de commande, le mainframe de l’application, la barre d'état et les boîtes de dialogue pour de nombreuses commandes.

### openNURBS

openNURBS est un code source C++ gratuit qui vous permet de lire et d’écrire des fichiers Rhino *3dm*, en remontant même jusqu’à la version 1.  openNURBS a été notre premier projet open-source.

Le code se compile sous Windows, macOS, Linux, iOS et Android.  Il est utilisé dans diverses applications tierces telles qu’ArchiCAD, SolidWorks, Inventor, SketchUp et de nombreux autres produits pour lire ou écrire directement les fichiers *3dm*.

openNURBS est ce que Rhino utilise nativement pour lire et écrire les fichiers *3dm*.  Cette boîte à outils a été publiée avant Rhino, de sorte que tout produit, y compris nos concurrents, peut être compatible avec les derniers fichiers *3dm*.  Il n’y a pas de différence entre les fichiers *3dm* que Rhino écrit et ceux d’autres applications utilisant openNURBS pour lire et écrire les fichiers *3dm*.

Pour en savoir plus sur openNURBS, nous vous invitons à consulter les [guides d’openNURBS](/guides/opennurbs/).

### SDK en C++

Sur cette première couche repose notre SDK en C++ qui n’est disponible que sous Windows.

La compilation avec le SDK en C++ nécessite une version spécifique de Microsoft Visual Studio et Microsoft C-Runtime.  Il faut recompiler pour chaque version majeure de Rhino.

Pratiquement tout ce que Rhino peut faire est exposé à travers le SDK en C++. Certaines commandes et fonctionnalités n’ont pas encore été exposées, mais ce SDK est extrêmement vaste et riche.

Malheureusement, comme il est étroitement lié au noyau de Rhino, les développeurs de modules doivent recompiler leurs modules pour chaque version de Rhino.

Pour en savoir plus sur le SDK en C++, consultez les [guides de C/C++](/guides/cpp/).

## Pile de C++

La colonne de droite du diagramme ci-dessus représente la partie C++ de Rhino.  La pile de C++ nous permet, ainsi qu’aux développeurs de modules tiers, d’écrire des modules pour Rhino en utilisant le même SDK en C++ que celui que nous utilisons pour développer Rhino.  Notez que vous ne pouvez pas créer de composants de Grasshopper en utilisant C++.

### Modules C++

Sur le SDK en C++ on trouve les modules C++.  De nombreuses fonctionnalités livrées avec Rhino, notamment certaines commandes, les entrées/sorties de fichiers ou encore les moteurs de rendu, qui sont en fait des modules C++.  Il existe également des dizaines de modules C++ tiers, comme [VisualARQ d’Asuni](http://www.visualarq.com/), [RhinoCAM de MecSoft](https://mecsoft.com/rhinocam-software/) ou [V-Ray de Chaos Software](https://www.chaosgroup.com/vray/rhino).

Pour en savoir plus sur le SDK en C++, consultez les [guides de C/C++](/guides/cpp/).

### RhinoScript

L’un des modules C++ fournis avec Rhino est [RhinoScript](/guides/rhinoscript/what-are-vbscript-rhinoscript/).  RhinoScript expose un sous-ensemble utile du SDK de Rhino via VBScript, un langage de script largement utilisé.  RhinoScript vous permet d’accéder non seulement à Rhino, mais aussi à tout autre objet COM de Windows.

Pour plus d'informations, reportez-vous aux [guides de RhinoScript](/guides/rhinoscript/) et plus particulièrement au guide [Qu’est-ce que VBScript et RhinoScript ?](/guides/rhinoscript/what-are-vbscript-rhinoscript/).

## Pile .NET

Le SDK .NET est ici représenté en trois couches :

- API C
- .NET Framework
- RhinoCommon
- Eto

### API C

Une API C directe enveloppe le SDK en C++, ce qui nous permet d’invoquer la plate-forme (P/Invoke) dans le SDK en C++ pour former ainsi un pont entre le code C++ natif et les couches gérées de .NET.

### .NET Framework

Microsoft développe [.NET Framework](https://www.microsoft.com/net/framework).  .NET permet d’écrire des modules en C#, F#, VB.NET et tout autre langage qui se compile selon l’IL de Microsoft.

.NET framework de Microsoft est fourni avec Windows.

Dans Rhino pour Mac, nous intégrons [.NET Core](/guides/rhinocommon/moving-to-dotnet-core/) directement dans l’application.

### RhinoCommon

RhinoCommon est notre SDK .NET pour Rhino, construit au-dessus des portions de .NET framework qui sont *communes* à Windows et macOS (via Mono).  RhinoCommon permet aux développeurs d’exécuter du code .NET sur Rhino pour Windows et sur Rhino pour Mac.

Pour plus d'informations sur RhinoCommon, reportez-vous aux [guides de RhinoCommon](/guides/rhinocommon/) ou plus spécifiquement au guide [Qu’est-ce que RhinoCommon ?](/guides/rhinocommon/what-is-rhinocommon).

### Eto

Grâce à RhinoCommon, vous pouvez écrire des modules .NET qui fonctionnent sous Windows et sous Mac... à l’exception de l’interface utilisateur.  L’équipe de Mono n’a pas cloné WinForms ou WPF, de sorte qu’aucune de ces technologies ne fonctionne sous Mac.  Pour résoudre ce problème, Rhino est maintenant livré avec Eto.Forms.  Eto vous permet d’écrire une interface utilisateur en C#, XAML ou JSON et de l’utiliser sous Windows et sous macOS.  Votre interface utilisateur écrite en Eto peut même fonctionner sous iOS, Android et Linux.

Pour en savoir plus à propos d’Eto, consultez [Eto.Forms sur GitHub](https://github.com/picoe/Eto).

### Modules .NET

De nombreux modules, développés en interne ou par des tiers, sont construits au-dessus de RhinoCommon.  [Grasshopper](http://www.grasshopper3d.com/), par exemple, est un module de RhinoCommon.  Certaines commandes, certains moteurs de rendu et certains modules d’E/S de fichiers dans Rhino sont en fait écrits en tant que modules de RhinoCommon.  Au fil du temps, nous transférons de plus en plus de fonctionnalités pratiques dans les modules RhinoCommon/.NET afin de partager davantage de code entre les plateformes.  De nombreux modules tiers performants sont également écrits avec RhinoCommon et .NET, tels que [RhinoGold](http://www.tdmsolutions.com/), [Matrix by GEMVision](http://www.stuller.com/matrix) ou encore [Orca3D](http://orca3d.com/).

Pour plus d’informations sur RhinoCommon, nous vous recommandons de lire les [guides de RhinoCommon](/guides/rhinocommon/).

### Composants de Grasshopper

Rhino est désormais livré avec Grasshopper, notre langage de programmation visuelle pour la conception algorithmique et paramétrique.  Grasshopper est une plateforme de développement à part entière, avec [des centaines de composants Grasshopper créés par des tiers](http://www.food4rhino.com/grasshopper-addons) pour faire toutes sortes de choses de la [simulation physique](http://www.food4rhino.com/project/kangaroo) à la [création d’interfaces utilisateur personnalisées](http://www.food4rhino.com/project/human-ui), en passant par la [programmation et le contrôle de la robotique industrielle](http://www.food4rhino.com/project/hal).

Pour en savoir plus à propos de Grasshopper, et plus particulièrement du développement de composants de Grasshopper, consultez les [guides de Grasshopper](/guides/grasshopper/).

### Scripts Python

RhinoPython est l’un des modules .NET fournis avec Rhino.  Écrit avec [IronPython](http://ironpython.net/), une implémentation .NET de l’environnement d’exécution [python](https://www.python.org/), RhinoPython expose l’ensemble du SDK de RhinoCommon au langage de script python.  Cela signifie que chaque fois que nous ajoutons une fonctionnalité à RhinoCommon, elle apparaît automatiquement dans RhinoPython.

Pour plus d’informations sur RhinoPython, consultez les [guides de RhinoPython](/guides/rhinopython/).

## Voir aussi

- [Guides de C/C++](/guides/cpp/)
- [Guides d’openNURBS](/guides/opennurbs/)
- [Guides de RhinoScript](/guides/rhinoscript/)
- [Microsoft .NET Framework (sur microsoft.com)](https://www.microsoft.com/net/framework)
- [Qu’est-ce que RhinoCommon ?](/guides/rhinocommon/what-is-rhinocommon)
- [Guides de RhinoCommon](/guides/rhinocommon/)
- [Projet Mono](https://www.mono-project.com)
- [Eto.Forms sur GitHub](https://github.com/picoe/Eto)
- [Guides de Grasshopper](/guides/grasshopper/)
- [Guides de RhinoPython](/guides/rhinopython/)

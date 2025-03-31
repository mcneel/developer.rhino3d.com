+++
aliases = ["/en/5/guides/general/rhino-developer-prerequisites/", "/en/6/guides/general/rhino-developer-prerequisites/", "/en/7/guides/general/rhino-developer-prerequisites/", "/en/wip/guides/general/rhino-developer-prerequisites/"]
authors = [ "dan", "callum" ]
categories = [ "Getting Started" ]
description = "Ce guide décrit les principales conditions requises pour développer pour Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Conditions préalables pour les développeurs"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/learningresources"
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


Un certain nombre de conditions préalables sont requises pour développer Rhino.  D’une manière générale, on peut les diviser en trois catégories, classées par ordre croissant de difficulté :

1. [Configuration matérielle](#hardware)
1. [Configuration logicielle](#software)
1. [Connaissances en programmation](#programming-knowledge)

## Configuration matérielle

Si vous lisez ce guide, vous disposez probablement déjà d’un ordinateur capable d’exécuter Rhino. Si ce n'est pas le cas, Rhino a une [configuration minimale nécessaire](http://www.rhino3d.com/system_requirements/) à propos de laquelle nous vous conseillons de vous renseigner avant d’investir dans du matériel.  En général, tout ordinateur capable d’exécuter Rhino *devrait* être capable d’exécuter les outils de développement décrits dans le paragraphe [Configuration logicielle](#software).

Si vous utilisez Windows et que vous souhaitez développer des modules de Rhino pour Mac, vous aurez besoin d’un ordinateur Mac d’Apple.  Inversement, si vous êtes un utilisateur de macOS et que vous souhaitez développer pour Rhino pour Windows, vous aurez besoin d’un ordinateur capable d’exécuter Rhino sous Windows (cependant, les machines virtuelles exécutant Windows sous macOS peuvent en principe fonctionner parfaitement).


## Configuration logicielle

La configuration logicielle requise variera en fonction de ce que vous voulez faire.  Cependant, en général, vous aurez besoin de :

- [Rhinoceros.](http://www.rhino3d.com/download)
- Un éditeur de code.  Il existe de nombreuses options... en voici quelques-unes :
   - [Visual Studio pour Windows](https://www.visualstudio.com) : environnement de développement intégré (IDE) phare de Microsoft pour Windows.
   - [Visual Studio Code](https://code.visualstudio.com/) : le meilleur éditeur multiplateforme gratuit.

Consultez les [guides spécifiques au SDK](/guides/) pour la configuration logicielle. Ils se trouvent normalement dans les guides des *outils d’installation*.

## Connaissances en programmation

L’acquisition de connaissances en programmation est la condition préalable qui demande le plus de travail.  Cependant, apprendre à programmer (et même essayer un nouveau langage) est amusant et enrichissant.  Apprendre à programmer avec Rhino est une excellente façon de commencer.

### Apprendre C# .NET

Si vous souhaitez écrire des modules avec RhinoCommon, vous devrez comprendre un langage de programmation compatible avec .NET tel que C# (ou VB).  Nous recommandons [C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)) (C Sharp) parce qu’il est moderne, sûr et facile à apprendre, mais aussi parce que vous pouvez développer en C# à la fois pour Windows et macOS.

*À regarder*...

- [Beginning C# Programming](http://shop.oreilly.com/product/0636920036036.do) par Eric Lippert, Publié par O'Reilly Media
- [C# Fundamentals for Absolute Beginners](https://learn.microsoft.com/fr-fr/shows/csharp-fundamentals-for-absolute-beginners/) sur Microsoft Virtual Academy
- [C# et .NET Essential Training](https://www.linkedin.com/learning/c-sharp-and-dot-net-essential-training) sur LinkedIn Learning

*À lire*...

- [Programming C# 5.0](http://shop.oreilly.com/product/0636920024064.do) par Ian Griffiths, Publié par O'Reilly Media
- [C# 5.0 in a Nutshell](http://shop.oreilly.com/product/0636920023951.do) par Joseph Albahari et Ben Albahari, publié par O'Reilly Media

*À faire*...

- [Consultez des exemples](/samples/#rhinocommon) sur ce site
- [Demandez de l’aide sur Discourse](http://discourse.mcneel.com/c/rhino-developer)

### Apprendre C/C++

Pour écrire des modules pour Rhino à l'aide du SDK C/C++, vous devez d’abord apprendre le [langage de programmation C++](https://en.wikipedia.org/wiki/C%2B%2B).  C/C++ est parfois considéré comme un langage de programmation « avancé ».

*À regarder*...

- [C++ : Un langage à usage général](https://learn.microsoft.com/fr-fr/shows/cplusplus-language-library/) sur Microsoft Virtual Academy
- [C++ Essential Training](https://www.linkedin.com/learning/c-plus-plus-essential-training-15106801) avec Bill Weinmann sur LinkedIn Learning

*À lire*...

- [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language) par Ian Kernighan et Dennis Ritchie
- [Practical C++ Programming](http://shop.oreilly.com/product/9780596004194.do) par Steve Oualline, publié par O'Reilly Media
- [C++ Primer Plus](http://www.amazon.com/Primer-Plus-Edition-Developers-Library/dp/0321776402) par Stephen Prata

*À faire*...

- [Consultez des exemples](/samples/#cc) sur ce site
- [Demandez de l’aide sur Discourse](http://discourse.mcneel.com/c/rhino-developer)

### Apprendre Python

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) est un premier langage fantastique et un langage supplémentaire incroyablement flexible à ajouter à votre boîte à outils.

*À regarder*...

- [Cours Python de Google](https://developers.google.com/edu/python/) par Google for Education
- [Up and Running with Python](http://www.lynda.com/Python-tutorials/Up-Running-Python/122467-2.html) avec Joe Marini sur Lynda.com


*À lire*...

- [Le tutoriel Python](https://docs.python.org/2/tutorial/index.html)
- [RhinoPython Primer](http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101) par Skylar Tibbits, Arthur van der Harten, Steve Baer et David Rutten
- [Le tutoriel Python](https://docs.python.org/2/tutorial/index.html) par la Python Software Foundation
- [Learn Python the Hard Way](http://learnpythonthehardway.org/book/) par Zed A. Shaw. Comme ne l’indique pas son titre (« Apprenez Python à la dure »), cet ouvrage s’adresse aux débutants.
- [Automate The Boring Stuff With Python](https://automatetheboringstuff.com/) par Al Sweigart

*À faire*...

- [Consultez des exemples](/samples/#rhinopython) sur ce site
- [Demandez de l’aide sur Discourse](http://discourse.mcneel.com/c/scripting)

### Apprendre RhinoScript

RhinoScript est un outil de script basé sur le langage VBScript de Microsoft.  RhinoScript s’exécute dans Rhino pour Windows.

*À lire*...

- [RhinoScript Primer](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101) par David Rutten
- [Microsoft VBScript User's Guide and Language Reference](https://msdn.microsoft.com/en-us/library/t0aew7h6(VS.85).aspx)

*À faire*...

- [Consultez des exemples](/samples/#rhinoscript) sur ce site
- [Demandez de l’aide sur Discourse](http://discourse.mcneel.com/c/scripting)

### Pour aller plus loin...

- [Crafting Interpreters](https://craftinginterpreters.com/) par Robert Nystrom
- [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) par Robert C. Martin


## Voir aussi

- [Qu’est-ce qu’un module de Rhino ?](/guides/general/what-is-a-rhino-plugin/)
- <a href="https://en.wikipedia.org/wiki/C_Sharp_(programming_language">C Sharp sur Wikipedia</a>
- [C++ sur Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B)
- [Python sur Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))

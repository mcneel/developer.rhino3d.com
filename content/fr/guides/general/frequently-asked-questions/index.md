+++
aliases = ["/en/5/guides/general/frequently-asked-questions/", "/en/6/guides/general/frequently-asked-questions/", "/en/7/guides/general/frequently-asked-questions/", "/en/wip/guides/general/frequently-asked-questions/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "Ce guide est une liste de questions fréquemment posées (FAQ)."
keywords = [ "developer", "rhino", "faq" ]
languages = [ "All" ]
sdk = [ "General" ]
title= "Questions fréquentes"
type = "guides"
weight = 4

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptspage"
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


**Quel SDK me convient le mieux ?**

Tout dépend de ce que vous voulez faire. Si vous cherchez à automatiser des tâches répétitives dans Rhino, l’écriture d’un script [Python](/guides/#rhinopython) est la meilleure solution.  Si vous souhaitez écrire un module complet ou un composant de Grasshopper, nous vous conseillons vivement le [SDK RhinoCommon](/guides/rhinocommon/what-is-rhinocommon/).  Si vous maîtrisez très bien C/C++, vous devriez envisager d’utiliser le SDK C/C++ natif (uniquement pris en charge par Rhino pour Windows).

**Puis-je écrire des modules qui fonctionnent à la fois sous Windows et sous Mac ?**

Oui... et même en utilisant [le même code](/guides/rhinocommon/what-is-rhinocommon/).

**Qu’est-ce qu'une macro ?**

Les macros sont des chaînes de commandes et d’options de commande de Rhino qui vous permettent de créer une séquence automatisée d’opérations.  Cette macro (séquence) peut ensuite être répétée en appuyant sur un bouton de la barre d’outils ou en tapant un alias.

**Qu’est-ce qu’un script ?**

Pour les tâches plus complexes, les macros sont insuffisantes.  Elles n’ont pas la capacité d’effectuer des calculs complexes, de stocker et d’extraire des données, d’analyser ces données et de prendre des décisions conditionnelles, ou de pénétrer dans les rouages de Rhino.  Pour cela, il faut un véritable outil de programmation.  Le plus simple et le plus accessible d’entre eux est Python, qui comprend également sa version de la syntaxe RhinoScript.  Lorsque nous parlons de scripts, nous faisons généralement référence à des fonctions écrites avec RhinoScript ou Python.

**Qu’est-ce qu’un module ?**

Les modules sont des outils encore plus sophistiqués : il s’agit de programmes informatiques compilés qui peuvent être intégrés dans Rhino.  Il peut s’agir de simples fonctions de type script ou de programmes complexes et complets pour le rendu, l’animation, l’usinage, etc.

**Quelle est votre cadence de publication ?**

Toutes les semaines (si tout se passe bien), mais pour la plupart des utilisateurs, la réponse est tous les mois. Consultez notre [Planing de publication](/guides/general/developing-software-in-public/#publish) pour plus d’informations.

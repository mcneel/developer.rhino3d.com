+++
aliases = ["/en/5/guides/general/developing-software-in-public/", "/en/6/guides/general/developing-software-in-public/", "/en/7/guides/general/developing-software-in-public/", "/en/wip/guides/general/developing-software-in-public/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "Aperçu du processus de développement de McNeel."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Développer un logiciel publiquement"
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

Au cours des 20 dernières années, nous avons mis au point un processus qui contribue à la satisfaction de nos clients.  Ce processus comporte huit étapes, toutes aussi importantes les unes que les autres.  Pendant des années, nous avons développé nos propres outils pour prendre en charge la plupart des étapes de ce processus.  Mais aujourd’hui, il existe d’excellents outils disponibles dans le commerce et nous vous encourageons à les utiliser.

Comme tout processus, notre processus de développement logiciel est un cycle.  Il est possible de commencer à n’importe quelle étape.

![Rhino Development Cycle](/images/developing-software-in-public-01.png)

## Le cycle

Attendu que ce guide s’adresse aux développeurs, nous allons commencer par l’écriture du code.

### Écriture du code

C’est ce à quoi nous, développeurs de logiciels, consacrons une grande partie de notre temps.  Dans notre environnement de développement intégré (IDE) préféré, nous écrivons du code, nous déboguons, nous résolvons des problèmes.  Existe-il des développeurs de logiciels qui n’aiment pas résoudre les problèmes ?

Lorsque nous avons quelque chose, nous le validons (*commit*) dans notre système de contrôle de version.

### Validation

Nous validons le code dans un [système de contrôle de version](https://en.wikipedia.org/wiki/Version_control).  Dans notre cas, nous utilisons [git](https://git-scm.com/) avec [GitHub](https://github.com/).  Il existe de nombreux autres systèmes de contrôle de version.  Nous utilisions [Subversion](https://subversion.apache.org/) auparavant, mais nous sommes à présent passés à [GitHub](https://github.com/).  [GitHub](https://github.com/) est compatible avec de nombreux autres outils et possède une API très riche.  Mais il y en a d’autres qui méritent d’être mentionnés tels que [BitBucket](https://bitbucket.org), [Mercurial](https://www.mercurial-scm.org/), etc.

Si vous n’utilisez pas de système de contrôle de version, nous vous en supplions : commencez à le faire !  C’est vraiment facile.  Cela vous offre la possibilité de revenir à une version de votre logiciel antérieure à la survenue d’un problème.  Cela permet de travailler en équipe.  C’est nécessaire pour tout type d’automatisation des compilations.  Avons-nous déjà mentionné que c’était facile ?

En tant que développeurs, nous utilisons une version modifiée de [GitHub Flow](https://guides.github.com/introduction/flow/) pour créer et fusionner les demandes de rapatriement dans notre branche principale (master).

Après avoir validé notre code, nous le compilons.

### Compilation

En plus de compiler sur nos bureaux, nous avons des serveurs [TeamCity](https://www.jetbrains.com/teamcity/) dédiés qui compilent constamment notre code et vérifient qu’il fonctionne avec notre branche master sur [GitHub](https://github.com/).  Cela permet de s’assurer que nous ne nous empêchons pas mutuellement d’obtenir le code le plus récent et de le compiler.

Ces serveurs [TeamCity](https://www.jetbrains.com/teamcity/) vérifient chaque validation et compilent également nos (très nombreuses) versions quotidiennes toutes les quatre heures environ.  Ils compilent aussi nos versions publiques WIP (en cours de développement) et nos versions révisées.

À chaque nouvelle compilation, nous exécutons des tests.

### Tests

Lorsque les développeurs corrigent des erreurs et résolvent des problèmes, notre équipe de test interne s’assure que la version publique fonctionne correctement.  Nous comptons également sur nos clients pour tester les versions WIP et révisées.

Les tests ont lieu avant et après l'étape suivante : la publication.

### Publication

Chaque fois que nous avons une version prête à être envoyée aux clients, nous la déployons (ou publions).

Nous publions notamment...

- [Des fichiers d’installation téléchargeables](http://www.rhino3d.com/download)
- [Des SDK](http://developer.mcneel.com)
- De la documentation (ce site)

...et communiquons publiquement par e-mail, sur nos blogs et nos réseaux sociaux.

{{< call-out "note" "Planning de publication" >}}

Nous nous attachons à publier de nouvelles versions de Rhino le **deuxième mardi de chaque mois** comprenant :

- Une version révisée pour tous les utilisateurs ayant activé les mises à jour.
- Une [candidate à la version révisée](https://discourse.mcneel.com/t/rhino-service-release-candidates/53358). Une fois qu’une version candidate à la version révisée a passé la phase finale de test, elle devient la prochaine version révisée qui sera publiée le deuxième mardi suivant. Des versions candidates sont également publiées chaque semaine (en général le mardi) et nous encourageons les utilisateurs à [installer les candidates à la version révisée](https://discourse.mcneel.com/t/rhino-service-release-candidates/53358) car ils nous aident ainsi à tester la mise à jour suivante.
- Une [version WIP (en cours de développement)](https://discourse.mcneel.com/t/welcome-to-serengeti/9612).

{{< /call-out >}}

### Écoute

Nous restons constamment à l’écoute par toutes les voies possibles :

- [Chat](http://www.rhino3d.com/support#)
- [E-mail](mailto:tech@mcneel.com)
- Téléphone (au +34 933 199 002)
- [Forum (Discourse)](https://discourse.mcneel.com/)

Et souvent, c’est en écoutant que nous découvrons des problèmes à résoudre.  Parfois, ils sont petits... parfois ils sont ÉNORMES.  Nous enregistrons toujours un incident.

### Suivi

Nous enregistrons chaque incident dans [YouTrack](https://mcneel.myjetbrains.com).

[YouTrack](https://mcneel.myjetbrains.com) fonctionne bien pour nous car il nous permet de nous assurer que chaque problème est correctement testé et documenté.

### Hiérarchisation

Déterminer quelle sera la priorité suivante n’est pas chose aisée.  Nous discutons avec nos clients.  Nous parlons entre nous.  Nous utilisons Gmail, Google Drive et Google Docs pour communiquer.  Nous échangeons 24 heures sur 24 sur [Slack](https://slack.com/).

Nous nous réunissons une fois par semaine, le mardi.  Avant la réunion, chacun écrit ce qu’il a fait dans un document Google. Dans ce document, nous partageons nos objectifs pour nos prochains lancements et pour les différents groupes de fonctionnalités sur lesquels nous travaillons, nous incluons des graphiques de progression dans le temps, des liens vers les incidents [YouTrack](https://mcneel.myjetbrains.com) et des présentations orales des membres de l’équipe travaillant sur les fonctionnalités.

En outre, chaque développeur écrit ce sur quoi il a travaillé, ce qu'il prévoit de faire ensuite et les raisons qui l’empêchent d’achever son travail.

### Automatisation

Enfin, nous automatisons ÉNORMÉMENT de choses.

En voici quelques-unes :

- La compilation de chaque validation de chaque développeur avant qu’elle ne passe à notre branche de développement master.
- La clôture des incidents dans [YouTrack](https://mcneel.myjetbrains.com) lorsque les corrections sont fusionnées dans notre branche de développement master par les serveurs [TeamCity](https://www.jetbrains.com/teamcity/).
- La compilation des versions internes et publiques sur nos serveurs [TeamCity](https://www.jetbrains.com/teamcity/).
- La publication de nouvelles versions WIP en tapant une commande dans [Slack](https://slack.com/).
- Le téléchargement des versions publiques sur nos serveurs de téléchargement.

## Accès public

Jusqu’à récemment, les étapes suivantes de nos processus étaient accessibles publiquement :

- Tests
- Publication
- Ecoute

Au cours des deux dernières années, nous avons rendu public notre outil de suivi des incidents en adoptant YouTrack.  Certains incidents ne sont pas publics pour des raisons de sécurité ou de respect de la vie privée des utilisateurs.

Nous aimerions bientôt rendre ces informations encore plus accessibles à tous :

- Partager une partie de notre code en tant que répertoires publics sur GitHub afin que les développeurs puissent travailler à partir d’exemples de code réels.
- Permettre aux développeurs d’apporter des corrections et des améliorations à notre code.
- Faciliter la création de projets de modules en publiant RhinoCommon en tant que package NuGet.
- Aider à l’automatisation des compilations si nécessaire.

## Voir aussi

- [Vue d’ensemble de la technologie de Rhino](/guides/general/rhino-technology-overview)
- [Contribuer](/guides/general/contributing)
- [Conditions préalables pour les développeurs](/guides/general/rhino-developer-prerequisites)

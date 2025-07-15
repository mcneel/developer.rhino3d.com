+++
aliases = ["/en/5/guides/compute/development/", "/en/6/guides/compute/development/", "/en/7/guides/compute/development/", "/en/wip/guides/compute/development/"]
authors = [ "pedro" ]
categories = [ "Getting Started", "Development" ]
description = "Déployer Compute pour la production"
keywords = [ "developer", "compute", "production" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Exécuter et déboguer Compute localement"
type = "guides"
weight = 2
override_last_modified = "2024-05-13T15:49:48Z"

[admin]
TODO = "needs editing"
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

Rhino.Compute vous permet d’utiliser les capacités de calcul géométrique de Rhino dans le cloud. Avant de déployer votre application dans un environnement de production, vous devez vous assurer que tout fonctionne parfaitement dans un environnement contrôlé.

Ce guide est destiné aux développeurs qui ont l’habitude d’utiliser Windows et qui ont des connaissances de base de [Visual Studio](https://visualstudio.microsoft.com/downloads/) et de [Git](https://git-scm.com/downloads). Que vous soyez un utilisateur chevronné de Rhino ou que vous découvriez Rhino.Compute, vous trouverez dans ce document toutes les étapes nécessaires pour mettre en place votre environnement de développement et commencer à déboguer efficacement.

## Conditions préalables

Avant de vous lancer dans l’installation de Rhino.Compute sur votre machine locale, vous devez vous assurer que vous disposez des outils adaptés. Vous aurez besoin :

- Du système d’exploitation Windows. Rhino.Compute ne fonctionne que sous Windows.
- D’un environnement de développement. [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) sera nécessaire pour compiler le code.
- D’un système de contrôle des versions. [Git](https://git-scm.com/downloads) est indispensable pour cloner le répertoire compute.rhino3d et gérer les branches en fonction de votre version de Rhino.
- De Rhino. Visitez notre page de téléchargements pour obtenir les dernières versions de [Rhino 8](https://www.rhino3d.com/download/rhino-for-windows/8/latest) ou [Rhino 7](https://www.rhino3d.com/download/rhino-for-windows/7/latest). Après l’avoir téléchargé et installé, démarrez Rhino et suivez les instructions au démarrage pour valider votre licence sur votre machine ou via le Cloud Zoo.

{{< call-out "note" "Remarque" >}}
Vous devrez exécuter la version spécifique de Rhino.Compute en fonction de la version de Rhino que vous avez installée. Dans la section suivante, vous allez cloner le code source du répertoire compute.rhino3d. Si vous avez installé Rhino 8 sur votre machine, vous devrez cloner la branche 8.x. En revanche, si vous avez installé Rhino 7, assurez-vous de cloner la branche 7.x.
{{< /call-out >}}

## Cloner le répertoire

Pour obtenir la dernière version de Rhino.Compute, vous devrez cloner son [répertoire](https://github.com/mcneel/compute.rhino3d) depuis notre compte officiel sur Github.

1. Allez sur [https://github.com/mcneel/compute.rhino3d](https://github.com/mcneel/compute.rhino3d)

1. Dans le menu déroulant « branch », sélectionnez la branche à cloner (8.x ou 7.x).

1. Ensuite, cliquez sur le bouton vert « <> Code » et copiez l’URL du répertoire.
![compute_geometry_clone](/images/compute_geometry_clone.png)

1. Sur votre ordinateur local, créez un dossier dans lequel vous clonerez le répertoire.

1. Naviguez vers ce répertoire via l’invite de commande de votre choix, puis tapez `git clone` et collez l’URL que vous avez copiée plus tôt.
    ```python
    git clone https://github.com/mcneel/compute.rhino3d.git
    ```
1. Une fois l’opération de clonage terminée, vous devriez voir un certain nombre de fichiers et de répertoires qui ont été téléchargés depuis le répertoire compute.rhino3d dans le dossier que vous avez créé.

## Anatomie de la solution

Dans le répertoire Rhino.Compute, vous trouverez deux projets principaux, chacun servant des objectifs distincts. Bien les comprendre vous aidera à appréhender clairement le fonctionnement de Rhino.Compute, en particulier si vous souhaitez travailler ou à contribuer à son développement. Voici une explication détaillée des deux projets :

- **compute.geometry**. Ce projet se concentre principalement sur les aspects de calcul géométrique. Essentiellement, compute.geometry fournit une API REST qui expose le moteur de géométrie de Rhino à utiliser sur Internet. Cela signifie que des opérations géométriques peuvent être effectuées sur un serveur et que les résultats peuvent être récupérés à distance, ce qui est très utile pour les applications ou les services Web qui nécessitent un traitement géométrique complexe.

- **rhino.compute**. Ce projet peut être considéré comme une couche de service de haut niveau qui gère et orchestre les appels à l’API compute.geometry, en gérant des tâches telles que l’authentification, la création de processus enfants et la configuration de délais pour le processus d’arrêt.

## Compiler la solution

Maintenant que vous avez le code, il est temps d’ouvrir le projet dans Visual Studio 2022 et de le préparer pour le débogage.

1. Naviguez jusqu’au répertoire où vous avez cloné les dossiers et fichiers, et trouvez le fichier **compute.sln**. Double-cliquez dessus pour ouvrir le projet dans Visual Studio 2022.

1. Passez la configuration de la solution en mode débogage (**Debug**). Cela vous permet d’exécuter le code avec toutes les fonctionnalités de débogage, ce qui facilite le suivi du code et la détection des erreurs.
![compute_geometry_vs_debug](/images/compute_geometry_vs_debug.png)

1. Dans le menu File, cliquez sur Build -> Build Solution (Ctrl + Shift + B). Cette opération compile tous les fichiers du projet.
![compute_geometry_vs_build](/images/compute_geometry_vs_build.png)

1. Dans le panneau de l’explorateur de solutions, faites un clic droit sur le projet **rhino.compute** et sélectionnez **Set as Startup Project**. Ainsi vous êtes sûr que lorsque vous lancez le débogueur, Visual Studio démarre ce projet particulier.
![compute_geometry_vs_startup](/images/compute_geometry_vs_startup.png)

1. Cliquez sur **rhino.compute** pour démarrer l’application dans le débogueur. Une application console devrait apparaître dans votre barre des tâches, indiquant l’état du processus de chargement de Rhino.Compute.
![compute_geometry_vs_run](/images/compute_geometry_vs_run.png)

1. Il ne vous reste plus qu’à attendre quelques secondes durant le chargement de Rhino.Compute. N’oubliez pas que les informations enregistrées dépendent de la version de Rhino que vous avez choisie précédemment.
![compute.geometry.exe](/images/compute_geometry_screenshot.png)

## Tester un point de terminaison

Avec l’application console Rhino.Compute en cours d’exécution, naviguez vers l’un de ces points de terminaison pour vérifier que tout fonctionne !
- [http://localhost:6500/version](http://localhost:6500/version)
- [http://localhost:6500/healthcheck](http://localhost:6500/healthcheck)
- [http://localhost:6500/activechildren](http://localhost:6500/activechildren)
- [http://localhost:6500/sdk](http://localhost:6500/sdk)
+++
aliases = ["/en/5/guides/compute/compute-faq/", "/en/6/guides/compute/compute-faq/", "/en/7/guides/compute/compute-faq/", "/en/wip/guides/compute/compute-faq/", "/en/guides/compute/faq/"]
authors = [ "andy.payne" ]
categories = [ "Getting Started" ]
description = "Ce guide est une liste de questions fréquemment posées (FAQ) pour Rhino.Compute."
keywords = [ "developer", "compute", "faq" ]
languages = []
sdk = [ "Compute" ]
title= "Questions fréquentes"
type = "guides"
weight = 1
override_last_modified = "2025-05-07T09:45:21Z"

[admin]
TODO = ""
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

## Général

### Qu’est-ce que Rhino.Compute ?

Pour faire simple, Rhino.Compute est un serveur web capable d’effectuer des calculs de géométrie en utilisant la bibliothèque de géométrie de Rhino (c’est-à-dire [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/)). Il reçoit des requêtes sur Internet (via [HTTP](https://en.wikipedia.org/wiki/HTTP) ou [HTTPS](https://en.wikipedia.org/wiki/HTTPS)), les traite avec le moteur de géométrie de Rhino, puis retourne les résultats. Toute application capable d’envoyer des requêtes web peut interagir avec Rhino.Compute, ce qui facilite son intégration dans différents flux de travail.

### Pourquoi est-il intéressant pour moi de l’utiliser ?

Rhino.Compute vous permet d’utiliser les puissants outils et fonctionnalités de Rhino en dehors de l’interface normale de Rhino ou de Grasshopper. Il est idéal pour les équipes, car vous pouvez exécuter des définitions de Grasshopper ou des fonctions de Rhino à partir d’un point central, ce qui facilite la collaboration. Il peut également traiter plusieurs tâches en même temps (en parallèle), ce qui permet de gagner du temps sur les grands projets. Pour les calculs plus longs, il s’exécute en arrière-plan (de manière asynchrone) et évite ainsi de figer ou de ralentir votre interface principale.

### Fonctionnera-t-il sur macOS ?

Non. Rhino.Compute dépend de [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/) qui permet à Rhino et Grasshopper de fonctionner *dans* d’autres applications 64 bits. Actuellement, Rhino.Inside n’est compatible qu’avec le système d’exploitation Windows.

### Coûte-t-il cher ?

La réponse courte est : cela dépend d’*où* vous exécutez Rhino.Compute. Si vous l’utilisez sur un ordinateur Windows ordinaire, comme votre PC personnel, il n’y a aucun coût supplémentaire. Rhino.Compute vérifiera votre licence standard de Rhino au démarrage (remarque : [les versions d’évaluation de Rhino](https://www.rhino3d.com/download/) fonctionnent parfaitement). Mais si vous l’exécutez sur un serveur Windows (comme une machine virtuelle dans le cloud), vous serez facturé sur la base de notre modèle de [facturation par cœur et par heure](../core-hour-billing/).

### Quelle est la différence avec Hops ?

[Hops](../what-is-hops/) est un module de Grasshopper (disponible à partir du [gestionnaire de paquets](../../yak/what-is-yak/)) qui facilite la résolution des définitions de Grasshopper à l’aide de Rhino.Compute. Lorsqu’il est installé, Hops démarre automatiquement une instance de Rhino.Compute en arrière-plan chaque fois que vous ouvrez Grasshopper. Vous pouvez ensuite utiliser le composant Hops pour envoyer votre définition de Grasshopper à Rhino.Compute, qui la résout et vous renvoie les résultats. Dans ce contexte, Hops est le « client » et Rhino.Compute le « serveur ».

### Puis-je créer ma propre interface pour travailler avec Rhino.Compute ?

Oui. Comme nous l’avons expliqué, toute application capable d’envoyer des requêtes web peut fonctionner avec Rhino.Compute. Pour vous faciliter la tâche, nous vous proposons trois bibliothèques que vous pouvez utiliser en fonction du langage que vous préférez :
1. [Bibliothèque Rhino.Compute Python](https://pypi.org/project/compute-rhino3d/)
1. [Bibliothèque Rhino.Compute Javascript](https://www.npmjs.com/package/compute-rhino3d)
1. [Bibliothèque Rhino.Compute .NET (C#)](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs)

Nous avons également des guides étape par étape pour vous aider à démarrer avec les bibliothèques précédentes :
1. [Appeler Compute avec Python](../compute-python-getting-started/)
1. [Appeler Compute avec Javascript](../compute-javascript-getting-started/)
1. [Appeler Compute avec .NET](../compute-net-getting-started/)

Enfin, nous avons un [répertoire GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute) contenant de nombreux projets et exemples qui illustrent comment utiliser Rhino.Compute pour différentes tâches sur la géométrie.

### Puis-je utiliser Rhino.Compute dans un environnement de production ?

Oui. Nous avons élaboré un [guide étape par étape](../deploy-to-iis/) pour vous aider à configurer Rhino.Compute dans un environnement de production, par exemple sur une machine virtuelle (VM). L’installation est facile : il suffit d’exécuter un simple script PowerShell, et Rhino.Compute sera opérationnel, prêt à traiter les requêtes.

## Résolution des problèmes

Nous mettons tout en œuvre pour que Rhino.Compute soit aussi facile à utiliser que possible. Mais il arrive que les choses ne se passent pas comme prévu. Cette section a pour but de vous aider à dépanner et à résoudre les problèmes que vous pourriez rencontrer.

### Où puis-je trouver les fichiers journaux ?

Si vous utilisez Rhino.Compute avec Hops, vous devez vous assurer que l’application console de Rhino.Compute est visible à chaque démarrage. Pour cela, suivez ces étapes :
1. Lancez Grasshopper
1. Cliquez sur **File -> Preferences** pour ouvrir la boîte de dialogue des paramètres de Grasshopper.
1. Cliquez sur l’onglet **Solver** dans le menu de gauche.
1. **Décochez** l’option « Hide Rhino.Compute Console Window ».
1. Redémarrez Rhino et Grasshopper.

{{< image url="/images/hops-preferences-1.png" alt="/images/hops-preferences-1.png" class="image_center" width="75%" >}}

À ce stade, vous devriez voir une nouvelle application apparaître dans votre barre des tâches (si vous utilisez Windows) lorsque vous démarrez Grasshopper. C’est l’application console de Rhino.Compute. Des informations de dépannage utiles s’afficheront ici lorsque vous travaillerez avec Rhino.Compute.

{{< image url="/images/hops-console-2.png" alt="/images/hops-console-2.png" class="image_center" width="100%" >}}

<br>
Si vous exécutez Rhino.Compute sur une machine virtuelle, les fichiers journaux sont enregistrés sous forme de fichiers texte. De nouveaux fichiers journaux seront créés chaque jour. Par défaut, les fichiers journaux sont enregistrés à l’emplacement suivant :

```cs
C:\inetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute\logs\
```

### Est-il possible d’activer la journalisation détaillée ?

Par défaut, Rhino.Compute consigne un ensemble minimal d’informations dans les journaux. Pour enregistrer davantage de détails dans les journaux, vous devrez créer une variable d’environnement sur votre machine.

1. Cliquez avec le bouton droit de la souris sur l’icône **Ce PC** dans l’explorateur de fichiers, puis sélectionnez **Propriétés** ou **Système** dans le Panneau de configuration.
1. Dans la fenêtre Informations du système, cliquez sur **Paramètres avancés du système**
1. Dans l’onglet **Avancé**, cliquez sur **Variables d’environnement**
1. Cliquez sur le bouton **Nouveau** pour créer une nouvelle variable système.
1. Dans le champ **Nom de la variable**, tapez « RHINO_COMPUTE_DEBUG »
1. Dans le champ **Valeur de la variable**, tapez « true »
1. Cliquez sur OK pour enregistrer la variable d’environnement du système, puis cliquez à nouveau sur OK pour fermer la boîte de dialogue Variables d’environnement et la fenêtre Informations du système.

### Que dois-je faire si l’erreur « HRESULT E_FAIL » apparaît ?

Si Rhino.Compute renvoie l’erreur suivante :

```cs
Application startup exception
System.Runtime.InteropServices.COMException (0x80004005): Error HRESULT E_FAIL has been returned from a call to a COM component.
   at Rhino.Runtime.InProcess.RhinoCore.InternalStartup(Int32 argc, String[] argv, StartupInfo& info, IntPtr hostWnd)
```

Cela signifie très probablement que Rhino.Compute ne parvient pas à trouver une licence valide au démarrage. Si vous utilisez une machine basée sur un serveur Windows (c’est-à-dire une machine virtuelle), procédez comme suit :

1. Allez sur le [Portail des licences](https://www.rhino3d.com/licenses?_forceEmpty=true) et sélectionnez l’équipe que vous avez configurée avec la facturation par cœur et par heure.
1. Cliquez sur **Gérer une équipe -> Gérer une facturation par cœur et par heure**.
1. Cliquez sur **Action -> Obtenir un jeton d’autorisation** pour obtenir un jeton.
1. Créez une nouvelle variable d’environnement que vous nommerez `RHINO_TOKEN` et utilisez le jeton comme valeur. Le jeton étant trop long pour la boîte de dialogue Variables d’environnement de Windows, il est plus facile de réaliser cette opération via une commande PowerShell.

```ps
[System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'votre jeton', 'Machine')
```

Dorénavant, lorsque vous démarrerez Rhino sur cette machine, il utilisera votre équipe de facturation par cœur et par heure.

{{< call-out "warning" "Avertissement" >}}
<strong>Attention !</strong> Votre jeton de facturation par cœur et par heure permet à toute personne qui le possède de facturer votre équipe à volonté. Ne le partagez <strong>EN AUCUN CAS</strong>.
{{< /call-out >}}

### Un message « Erreur 401 » s’affiche. Qu’est-ce que cela signifie ?

Si Rhino.Compute renvoie une erreur 401, cela signifie que la requête n’a pas été autorisée. Cela se produit généralement lorsqu’il manque une clé API à la requête. Rhino.Compute vérifie cette clé, qui est enregistrée en tant que variable d’environnement sur la machine sur laquelle il fonctionne, afin de s’assurer que seuls les clients approuvés peuvent se connecter.

Si vous utilisez Hops, vous pouvez paramétrer la clé API dans la section des préférences.

1. Lancez Grasshopper
1. Cliquez sur **File -> Preferences** pour ouvrir la boîte de dialogue des paramètres de Grasshopper.
1. Cliquez sur l’onglet **Solver** dans le menu de gauche.
1. **Saisissez la clé API** dans la boîte de dialogue.
1. Redémarrez Rhino et Grasshopper.

{{< image url="/images/hops-api-key.png" alt="/images/hops-api-key.png" class="image_center" width="75%" >}}

<br>
Si vous envoyez une requête web à Rhino.Compute en utilisant une méthode différente, n’oubliez pas d’inclure une paire clé-valeur dans l’en-tête de la requête. La clé doit être nommée « RhinoComputeKey » et sa valeur doit correspondre à la clé API définie sur la machine exécutant Rhino.Compute.

### Que signifie le code d’erreur 500 ?

Si vous recevez une réponse de Rhino.Compute contenant un code d’erreur 500, cela signifie que le serveur fonctionne mal et n’est pas en mesure de traiter la demande correctement. Si cela se produit, vous devrez peut-être essayer d’exécuter Rhino.Compute en mode débogage pour obtenir des informations supplémentaires sur la raison de l’échec du serveur. [Consultez ce guide](../development/) pour apprendre à exécuter Rhino.Compute en mode débogage.

### Que dois-je faire si j’obtiens une exception de dépassement de délai d’attente ?

Si Rhino.Compute renvoie l’erreur suivante :

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Connection id "...", Request id "...": An unhandled exception was thrown by the application.
      System.Threading.Tasks.TaskCanceledException: The request was canceled due to the configured HttpClient.Timeout of 100 seconds elapsing.
```

Un dépassement de délai lors du traitement d’une requête HTTP se produit lorsqu’un client (comme Hops) ne reçoit pas de réponse d’un serveur (comme Rhino.Compute) dans un délai spécifié. Il existe donc deux valeurs de délai d’attente dont il convient de tenir compte : 1) le délai d’attente du client et 2) le délai d’attente du serveur.

Le paramètre de délai d’attente que vous voyez dans les préférences de Hops contrôle le délai d’attente côté client. La valeur par défaut est de 100 secondes, mais elle peut être étendue pour remédier à cette erreur.

{{< image url="/images/hops-timeout.png" alt="/images/hops-timeout.png" class="image_center" width="75%" >}}

Le délai d’attente côté serveur est géré séparément : il est défini par une variable d’environnement sur la machine qui exécute le serveur. Pour paramétrer la variable d’environnement, procédez comme suit :

1. Cliquez avec le bouton droit de la souris sur l’icône **Ce PC** dans l’explorateur de fichiers, puis sélectionnez **Propriétés** ou **Système** dans le Panneau de configuration.
1. Dans la fenêtre Informations du système, cliquez sur **Paramètres avancés du système**
1. Dans l’onglet **Avancé**, cliquez sur **Variables d’environnement**
1. Cliquez sur le bouton **Nouveau** pour créer une nouvelle variable système
1. Dans le champ **Nom de la variable**, tapez « RHINO_COMPUTE_TIMEOUT »
1. Dans le champ **Valeur de la variable** tapez le **nombre de secondes** que vous souhaitez utiliser comme valeur de délai d’attente côté serveur
1. Cliquez sur OK pour enregistrer la variable d’environnement du système, puis cliquez à nouveau sur OK pour fermer la boîte de dialogue Variables d’environnement et la fenêtre Propriétés du système.

### Je reçois un message d’erreur indiquant que le corps de la requête est trop volumineux. Que dois-je faire ?

Si Rhino.Compute renvoie l’erreur suivante :

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Connection id "...", Request id "...": An unhandled exception was thrown by the application.
      Microsoft.AspNetCore.Server.Kestrel.Core.BadHttpRequestException: Request body too large.
```

Cette erreur peut se produire si vous essayez d’envoyer une grande quantité de données à Rhino.Compute dans le corps d’une requête. La limite par défaut pour la taille d’une demande est d’environ 50 Mo. Pour augmenter cette limite, suivez ces instructions :

1. Cliquez avec le bouton droit de la souris sur l’icône **Ce PC** dans l’explorateur de fichiers, puis sélectionnez **Propriétés** ou **Système** dans le Panneau de configuration.
1. Dans la fenêtre Informations du système, cliquez sur **Paramètres avancés du système**
1. Dans l’onglet **Avancé**, cliquez sur **Variables d’environnement**
1. Cliquez sur le bouton **Nouveau** pour créer une nouvelle variable système
1. Dans le champ **Nom de la variable**, tapez « RHINO_COMPUTE_MAX_REQUEST_SIZE »
1. Dans le champ **Valeur de la variable**, tapez le **nombre maximum d’octets** autorisé dans le corps d’une requête HTTP. La valeur par défaut est de 52 428 800 octets (environ 50 Mo). Augmentez cette valeur pour autoriser des demandes plus importantes.
1. Cliquez sur OK pour enregistrer la variable d’environnement du système, puis cliquez à nouveau sur OK pour fermer la boîte de dialogue Variables d’environnement et la fenêtre Informations du système.

<br><br>
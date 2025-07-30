+++
aliases = ["/en/5/guides/compute/deploy-to-iis/", "/en/6/guides/compute/deploy-to-iis/", "/en/7/guides/compute/deploy-to-iis/", "/en/wip/guides/compute/deploy-to-iis/", "/en/guides/compute/deploy/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
description = "Comment déployer Rhino.Compute pour la production sur une machine avec Internet Information Services (IIS)."
keywords = [ "developer", "compute", "production", "IIS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Déploiement sur des serveurs de production"
type = "guides"
weight = 4
override_last_modified = "2022-05-18T09:45:21Z"

[admin]
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

## Présentation

Ce guide vous explique comment configurer une instance de Rhino.Compute sur une machine virtuelle avec Internet Information Services (IIS). [IIS](https://www.iis.net/), est un serveur Web flexible et polyvalent développé par Microsoft qui peut être configuré pour livrer les pages ou les fichiers HTML demandés. IIS peut être configuré de sorte à traiter les requêtes entrantes (provenant de Hops ou d’un autre client) et les transmette à l’instance de Rhino.Compute. 

Mais vous vous demandez peut-être : « Pourquoi ai-je besoin d’IIS ? Ne pourrait-on pas simplement lancer le serveur Rhino.Compute et envoyer des requêtes API directement à cette instance ? » Techniquement parlant, vous n’avez pas besoin d’IIS. Cependant, vous devrez trouver un moyen de relancer le serveur Compute en cas de panne ou de dysfonctionnement. Vous devrez également configurer Rhino.Compute pour qu’il démarre à chaque lancement de la machine virtuelle. 

L’un des principaux avantages de l’utilisation d’IIS en tant qu’intergiciel est qu’il est capable de lancer automatiquement une instance du serveur Rhino.Compute à chaque fois qu’une requête est reçue. Cette configuration permet d’éviter que Compute ne fonctionne en permanence. Au lieu de cela, IIS peut lancer une instance de Compute lorsque cela est nécessaire, qui à son tour lancera un ou plusieurs processus enfants. Ce sont ces processus enfants qui effectuent les calculs proprement dits et qui requièrent l’autorisation de votre licence. 

Lorsque Rhino.Compute.exe ne reçoit pas de requête de résolution pendant une certaine période donnée en secondes (que l’on appelle fenêtre d’inactivité ou « idlespan » en anglais, et qui est fixée par défaut à 1 heure), les processus compute.geometry.exe enfants s’arrêtent et cessent d’être facturés par cœur et par heure. Plus tard, lorsqu’une nouvelle requête arrive, IIS vérifiera que Rhino.Compute.exe est en cours d’exécution, ce qui relancera les processus enfants. Notez qu’il peut y avoir un léger retard dans la réponse pendant le lancement des processus enfants.

{{< image url="/images/IIS_Request.png" alt="/images/IIS_Request.png" class="image_center" width="100%" >}}
<figcaption align = "left"><b>Fig.1 - Diagramme montrant comment IIS reçoit une requête entrante et lance Rhino.Compute.exe qui, à son tour, lance des processus enfants.</b></figcaption>

## Conditions préalables

Avant d’exécuter le script de démarrage sur votre serveur ou votre machine virtuelle, vous aurez besoin des informations suivantes :

* **`EmailAddress`** - Le script utilisera cette adresse e-mail pour télécharger une copie de Rhino à installer. C’est similaire à la page de téléchargement de Rhino.
* **`ApiKey`** - La clé API est une chaîne de texte secrète réservée à votre serveur Compute et aux applications qui utilisent l’API Compute, par exemple `b8f91f04-3782-4f1c-87ac-8682f865bf1b`. En essence, c’est ainsi que le serveur Compute s’assure que les appels de l’API proviennent uniquement de vos applications. Vous pouvez saisir n’importe quelle chaîne de caractères unique et secrète pour vous et vos applications informatiques. Conservez-la en lieu sûr.
* **`RhinoToken`** – Il s’agit d’un jeton qui identifie votre instance de Rhino Compute auprès du système de facturation par cœur et par heure. Allez sur le [Portail des licences](https://www.rhino3d.com/licenses?_forceEmpty=true) pour générer cet identifiant unique à partir de votre licence. Consultez le [guide sur la facturation par cœur et par heure](../core-hour-billing/) pour plus d’informations.

{{< call-out "note" "Remarque" >}}
Lorsque vous exécutez Rhino Compute localement, vous utilisez votre licence de Rhino existante et cela n’entraîne aucun coût supplémentaire (hormis votre investissement initial dans la licence de Rhino). Exécuter Compute localement est la meilleure option durant la phase de développement et de tests. Pour en savoir plus, lisez <a href="../development"><u>Exécuter et déboguer Compute localement</u></a>.<br><br>

Cependant, lors de la mise en place d’un environnement de production, vous aurez besoin d’un serveur ou d’une machine virtuelle préinstallée avec Windows Server 2019 ou une version plus récente. La licence fonctionne différemment lorsque vous utilisez Rhino (via Compute) dans un environnement de production (c'est-à-dire sur un serveur) et vous serez facturé à un taux de 0,10 $ par cœur et par heure. <br><br>

Suivez le <a href="../core-hour-billing"><u>guide sur la facturation par cœur et par heure</u></a> pour commencer. <b>Cette étape est importante, ne la négligez pas.</b>
{{< /call-out >}}

## Créer la machine virtuelle

La première étape du processus de déploiement de **Rhino.Compute** pour la production consiste à configurer une machine physique qui jouera le rôle de serveur ou à créer une machine virtuelle (VM). Pour ce guide, nous utiliserons une machine virtuelle. Il existe plusieurs services populaires qui peuvent être configurés pour mettre en place un large éventail de machines virtuelles en fonction de vos besoins en ressources. Les deux fournisseurs les plus connus sont [Azure](https://azure.microsoft.com/en-us/free/virtual-machines/) et [AWS](https://aws.amazon.com/ec2/instance-types/).  

Nous vous recommandons de commencer par une machine virtuelle Azure ou AWS, selon vos préférences. Les guides suivants vous aideront pour ce processus :

* [Créer une machine virtuelle sur Azure](../creating-an-Azure-VM).

* [Créer une machine virtuelle sur AWS](../creating-an-aws-vm).

### Connexion via RDP

Maintenant que nous avons configuré la machine virtuelle, nous allons devoir nous y connecter afin de configurer IIS et l’instance de Rhino.Compute. Pour ce faire, nous utiliserons un protocole Remote Desktop (RDP) qui permet de connecter deux ordinateurs sur un réseau.

Pour commencer, nous allons télécharger le fichier RDP. Nous utiliserons le portail Azure VM, mais le processus est similaire pour AWS.

1. Tout d’abord, assurez-vous que la machine virtuelle est en cours d’exécution. Cliquez sur **Vue d’ensemble** dans le menu de gauche. Si le *statut* indique *Stopped (Deallocated)*, cliquez sur le bouton **Démarrer** en haut pour démarrer la machine distante. Après quelques secondes, le statut devrait indiquer *Running*.

1. Cliquez sur **Connecter** dans le menu de gauche pour faire apparaître le volet des paramètres de connexion.

1. Cliquez sur le bouton **Télécharger le fichier RDP** et enregistrez le fichier quelque part sur votre ordinateur.
{{< image url="/images/Azure_VM_Connect1.png" alt="/images/Azure_VM_Connect1.png" class="image_center" width="100%" >}}

1. Cliquez sur le menu **Démarrer** de Windows et commencez à taper *connexion bureau à distance* dans la barre de recherche. Cliquez sur le lien pour lancer l’application.

1. Cliquez sur le bouton en bas de la fenêtre pour **Afficher les options**.

1. Dans *Paramètres de connexion*, cliquez sur **Ouvrir** et naviguez jusqu’au répertoire où vous avez enregistré votre fichier RDP. Sélectionnez ce fichier et cliquez sur Ouvrir.

1. Cochez la case **Enregistrer mes identifiants**.

1. Cliquez sur **Connexion**.
{{< image url="/images/Azure_VM_Connect2.png" alt="/images/Azure_VM_Connect2.png" class="image_center" width="60%" >}}

1. Une boîte de dialogue de sécurité s’ouvre. Cochez la case **Ne plus me demander sur cet ordinateur**, puis cliquez sur **Connexion**.

1. Tapez les informations d’identification d’administrateur que vous avez saisies à l’étape 7 du processus de [création d’une machine virtuelle](../deploy-to-iis/#setting-up-a-virtual-machine).

1. Il se peut qu’une autre boîte de dialogue de sécurité s’affiche. Sélectionnez à nouveau **Ne plus me demander sur cet ordinateur** et cliquez sur **Oui**.

Félicitations ! Vous avez maintenant accès au bureau de la machine distante exécutant Windows Server 2019 ou une version plus récente.

## Exécuter le script de démarrage
À présent que vous êtes connecté à la machine virtuelle (via RDP), vous allez suivre les étapes suivantes pour installer Rhino.Compute derrière IIS. Attention : nous considérons pour les étapes suivantes qu’il s’agit d’une installation sur une nouvelle machine virtuelle ou un nouveau serveur (ce qui signifie que Rhino.Compute n’a encore jamais été installé sur cette machine). Si vous avez déjà installé Rhino.Compute et IIS sur cette machine et que vous avez simplement besoin de mettre à jour Rhino et/ou Rhino.Compute sur la machine virtuelle, passez directement à la section [Mise à jour de Rhino Compute](../deploy-to-iis/#updating-the-deployment).

### Étape 1

1. Cliquez sur le menu Démarrer de Windows et tapez « Powershell ». Dans le menu qui apparaît, faites un clic droit sur l’application **Windows Powershell** et choisissez **Exécuter en tant qu’administrateur**.
{{< image url="/images/powershell_1.png" alt="/images/powershell_1.png" class="image_center" width="50%" >}}

1. **Copiez et collez** la commande ci-dessous dans l’invite Powershell et appuyez sur **Entrée**. Cette commande téléchargera le dernier script de démarrage de l’étape 1 et installera Rhino et IIS sur votre machine virtuelle. Remarque : il vous sera demandé de saisir votre **adresse e-mail**, votre **Clé API** et votre **jeton de Rhino** ; veillez donc à avoir ces informations à portée de main.
    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-1')">Rhino 7 : Étape 1
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-1')" id="defaultOpen1">Rhino 8 : Étape 1
    </div>

    <div class="tab-content">
    <div class="codetab-content1" id="r7-1">

    ```powershell
    $F="/bootstrap_step-1.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/bootstrap_step-1.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-1\boostrap_step-1.ps1" 
    ```

    </div>

    <div class="codetab-content1" id="r8-1">

    ```powershell
    $F="/bootstrap_step-1.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/bootstrap_step-1.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-1\boostrap_step-1.ps1" 
    ```

    </div>
    </div>

1. A l’issue de la première étape, votre machine virtuelle sera automatiquement redémarrée (vous serez déconnecté de la connexion Bureau à distance).

### Étape 2

1. Reconnectez-vous à votre machine virtuelle via la connexion Bureau à distance.

1. Ouvrez une nouvelle instance de **Windows Powershell**. Cliquez avec le bouton de droite sur l’application et sélectionnez **Exécuter en tant qu’administrateur**.

1. **Copiez et collez** la commande ci-dessous dans l’invite Powershell et appuyez sur **Entrée**. Cette commande téléchargera le dernier script de démarrage de l’étape 2 et configurera IIS pour qu’il fonctionne avec Rhino.Compute.
    <div class="codetab">
      <button class="tablinks2" onclick="openCodeTab(event, 'r7-2')">Rhino 7 : Étape 2
      <button class="tablinks2" onclick="openCodeTab(event, 'r8-2')" id="defaultOpen2">Rhino 8 : Étape 2
    </div>

    <div class="tab-content">
    <div class="codetab-content2" id="r7-2">

    ```powershell
    $F="/bootstrap_step-2.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/bootstrap_step-2.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-2\boostrap_step-2.ps1"
    ```

    </div>

    <div class="codetab-content2" id="r8-2">

    ```powershell
    $F="/bootstrap_step-2.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/bootstrap_step-2.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-2\boostrap_step-2.ps1"
    ```

    </div>
    </div>

1. A la fin du script d’installation de l’étape 2, vous devriez voir le message *Congratulations! All components have now been installed.* Vous verrez ensuite des instructions sur la façon d’installer des modules tiers afin qu’ils fonctionnent correctement avec Rhino.Compute. Notez bien le nouveau **nom d’utilisateur** et le nouveau **mot de passe** qui seront nécessaires lorsque vous vous reconnecterez pour installer un autre module.

## Tester l’application

A ce stade, IIS doit être configuré pour lancer l’instance de Rhino.Compute lorsqu’une requête API est effectuée. Nous allons demander à Hops d’envoyer une définition à l’URL de notre machine virtuelle. 

1. Lancez **Rhino** sur votre machine locale.

1. Si vous n’avez pas encore installé Hops, faites-le en le recherchant dans le **Gestionnaire de paquets**de Rhino.

1. Lancez **Grasshopper** en tapant le mot *Grasshopper* dans l’invite de commande, puis appuyez sur Entrée.

1. Allez dans **File** puis **Preferences** pour ouvrir la boîte de dialogue des préférences. 

1. Cliquez sur l’onglet **Solver** dans le menu de gauche. 

1. Dans la section **Hops - Compute server URLs**, saisissez l’adresse Web de votre machine virtuelle. Tapez `http://` suivi de l’adresse IP de la machine virtuelle, puis `:` et enfin le numéro de port `80`. Ainsi, l’adresse complète devrait ressembler à ceci :
            
        http://52.168.38.105:80/

1. Dans la section **API Key**, saisissez la clé API que vous avez enregistrée dans le paragraphe [Conditions préalables](../deploy-to-iis/#prerequisites).
{{< image url="/images/Hops_To_IIS_4.png" alt="/images/Hops_To_IIS_4.png" class="image_center" width="80%" >}}

1. Ajoutez un composant **Hops** sur la **toile de Grasshopper** (Params/Util).

1. Cliquez avec le bouton droit de la souris sur le composant **Hops** et configurez **Path** en saisissant une définition valide de Hops/Grasshopper. Pour savoir comment créer une définition de Grasshopper fonctionnant avec Hops, [consultez ce guide](../hops-component/).
{{< image url="/images/Hops_To_IIS_2.png" alt="/images/Hops_To_IIS_2.png" class="image_center" width="50%" >}}

Une fois le chemin configuré, le composant Hops crée la requête API appropriée et l’envoie à l’URL que nous avons spécifiée à l’étape 6 (le serveur Rhino.Compute fonctionnant sur IIS). Le serveur Compute traite la requête et envoie une réponse à Hops, qui renvoie le résultat.
{{< image url="/images/Hops_To_IIS_3.png" alt="/images/Hops_To_IIS_3.png" class="image_center" width="70%" >}}

Félicitations ! Vous avez configuré avec succès une instance de Rhino.Compute fonctionnant derrière IIS sur une machine virtuelle. 

## Modifier les paramètres de Compute après le déploiement

Un certain nombre d’arguments de ligne de commande permettent de modifier le comportement de Rhino.Compute. Dans cette section, vous verrez comment modifier ces paramètres après le déploiement de Rhino.Compute.

1. Connectez-vous à votre machine virtuelle (via RDP). Voir la section [Se connecter via RDP](#connect-via-rdp) pour plus d’informations.

1. Dans le menu **Démarrer**, cliquez dans la zone de recherche et tapez *Gestionnaire des services Internet (IIS)*. Cliquez pour lancer l’application.

1. Dans le gestionnaire IIS, **cliquez** sur le nœud du serveur Web dans le panneau **Connexions** à gauche. Notez que le nom du serveur Web doit être le même que celui que vous avez utilisé lors de la configuration du nom de votre machine virtuelle. 

1. Dans le volet **Actions** à droite, cliquez sur **Arrêter** pour arrêter le serveur Web.
{{< image url="/images/iis_manager.png" alt="/images/iis_manager.png" class="image_center" width="100%" >}}

Maintenant que le serveur Web IIS a été arrêté, nous allons modifier le fichier **web.config* pour Rhino.Compute. Le fichier [web.config](https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/web-config?view=aspnetcore-6.0) est un fichier lu par IIS et le module ASP.NET Core pour configurer un site hébergé par IIS. 

1. Ouvrez une fenêtre de l’**Explorateur de fichiers** et naviguez jusqu’à *C:\Ninetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute*. Dans ce répertoire, vous devriez trouver un fichier intitulé **web.config**. Remarque : il se peut que vous deviez cliquer sur l’onglet **Afficher** et cocher la case pour activer les **extensions de noms de fichiers**. Ouvrez le fichier web.config avec **Notepad** ou tout autre éditeur de texte.

Le fichier web.config doit ressembler à ceci :

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.webServer>
    <handlers>
      <add name="aspNetCore" path="*" verb="*" modules="AspNetCoreModuleV2" resourceType="Unspecified"/>
    </handlers>
    <aspNetCore processPath=".\rhino.compute.exe" arguments="--port 80" stdoutLogEnabled="true" stdoutLogFile="..\..\..\..\..\logs\LogFiles\W3SVC1\" forwardWindowsAuthToken="true" hostingModel="InProcess"/>
  </system.webServer>
</configuration>
```
La ligne à modifier est celle qui commence par l’étiquette **`<aspNetCore>`**. Vous voyez que le deuxième paramètre de cette ligne s’appelle **`arguments`**. C’est la section que vous changerez pour ajouter d’autres arguments de ligne de commande afin de modifier Rhino.Compute. 

Vous trouverez ci-dessous une description de chaque argument de ligne de commande qui peut être modifié.

- **port** - Il s’agit du numéro de port sur lequel Rhino.Compute est exécuté. Le numéro de port 80 est généralement réservé à la communication HTTP, tandis que le 443 est utilisé pour le protocole HTTPS. Nous avons configuré Rhino.Compute pour qu’il soit lié au port 80 dans le script de démarrage ; ne modifiez pas cette valeur à moins que vous ne sachiez ce que vous faites. Exemple d’utilisation : `--port 80`.

- **childcount** - Ce paramètre contrôle le nombre de processus compute.geometry enfants à gérer. La *valeur par défaut est 4*, ce qui signifie que Rhino.Compute créera quatre processus enfants, chacun d’entre eux pouvant traiter les requêtes entrantes. Exemple d’utilisation : `--childcount 8` indiquerait à Rhino.Compute de lancer huit processus enfants.

- **childof** - Il s’agit de l’identifiant du processus parent. Compute vérifie si 
ce handle existe et s’arrête lorsque ce processus prend fin. Comme IIS se charge de démarrer et d’arrêter Rhino.Compute, vous n’avez pas besoin de ce paramètre si vous travaillez dans un environnement de production.

- **spawn-on-startup** - Cette option détermine si un processus compute.geometry enfant doit être lancé au démarrage de Rhino.Compute. Par défaut la *valeur est égale à « false »*. Ce paramètre est une option, ce qui signifie que s’il n'est pas inclus dans la liste des arguments, la valeur sera « false ». Si vous incluez ce paramètre, sa valeur sera « true ». Pour les environnements de production, cette valeur doit rester « false ».

- **idlespan** - C’est le nombre de secondes pendant lesquelles un processus compute.geometry enfant doit rester ouvert entre les requêtes. Par défaut la *valeur est égale à 1 heure*. Lorsque Rhino.Compute.exe ne reçoit pas de requêtes pendant une période de `idlespan` secondes, les processus compute.geometry.exe enfants s’arrêtent et cessent d’être facturés par cœur et par heure. Plus tard, lorsqu’une nouvelle requête arrivera, les processus enfants seront relancés, ce qui entraînera un léger retard dans les requêtes pendant le lancement des processus enfants. Exemple d’utilisation : `--idlespan 1800` indiquera à Rhino.Compute d’arrêter les processus enfants après 30 minutes (30 mins x 60 secs = 1800).

    Si vous changez la valeur `idelspan` dans les arguments de ligne de commande pour Rhino.Compute, vous devrez également modifier la configuration de IIS. En effet, IIS contient également un paramètre déterminant l’arrêt de Rhino.Compute si aucune nouvelle requête n’est reçue après un certain temps. Lorsque Rhino.Compute est arrêté, il arrête à son tour tous les processus enfants. 

    Par exemple, supposons que vous changiez la valeur de `idlespan` à 7 200 (2 heures). Le script de démarrage fixe la valeur `IdleTimeout` d’IIS à 65 minutes (légèrement plus que la valeur `idlespan` par défaut). Au bout de 65 minutes, IIS arrête Rhino.Compute, qui arrête alors tous ses processus enfants bien avant le délai de 2 heures prévu. Par conséquent, si vous modifiez la valeur `idlespan`, vous devez également changer la valeur `IdleTimeout` dans les paramètres IIS.

    1. Pour ce faire, retournez dans le gestionnaire IIS et cliquez sur l'élément **Pools d’applications** dans le volet **Connexions** à gauche. 
    
    1. Dans la fenêtre centrale, cliquez sur le **RhinoComputeAppPool**.

    1. Dans le volet **Actions** à droite, cliquez sur **Paramètres avancés**.

    1. Trouvez la ligne **Délai d’inactivité** sous la section **Modèle de processus** et modifiez la valeur pour qu’elle soit légèrement plus longue que la valeur `idlespan` que vous avez définie dans les arguments de ligne de commande. Attention : la valeur `idlespan` est en secondes tandis que la valeur `Idle Timeout` est en minutes.
    {{< image url="/images/iis_idletimout.png" alt="/images/iis_idletimout.png" class="image_center" width="60%" >}}

Une fois que vous avez modifié le fichier web.config, **enregistrez** et fermez le fichier. Vous pouvez ensuite retourner dans le gestionnaire IIS et **démarrer** le serveur Web en cliquant sur le nœud du serveur Web dans le panneau **Connexions** à gauche puis en cliquant sur **Démarrer** dans le volet **Actions** à droite.

## Mettre à jour le déploiement
Si vous avez déjà installé Rhino.Compute sur votre machine, il se peut que vous deviez périodiquement mettre à jour Rhino et/ou les fichiers de compilation de Rhino.Compute pour avoir la dernière version. Suivez les étapes suivantes pour mettre à jour ces applications.

### Mettre à jour Rhino

1. Cliquez sur le menu Démarrer de Windows et tapez « Powershell ». Dans le menu qui apparaît, faites un clic droit sur l’application **Windows Powershell** et choisissez **Exécuter en tant qu’administrateur**.

1. **Copiez et collez** la commande ci-dessous dans l’invite Powershell et appuyez sur **Entrée**. Cette commande téléchargera la dernière version de Rhino pour Windows. Remarque : il vous sera demandé de saisir votre **adresse e-mail** ; assurez-vous que vous disposez de cette information.

    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-3')">Installer la dernière mise à jour pour Rhino 7</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-3')" id="defaultOpen3">Installer la dernière mise à jour pour Rhino 8</button>
    </div>

    <div class="tab-content">
    <div class="codetab-content1" id="r7-3">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/module_update_rhino.ps1 -outfile update_rhino.ps1; .\update_rhino.ps1 
    ```

    </div>

    <div class="codetab-content1" id="r8-3">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/module_update_rhino.ps1 -outfile update_rhino.ps1; .\update_rhino.ps1 
    ```

    </div>
    </div>

### Mise à jour de Compute

1. Cliquez sur le menu Démarrer de Windows et tapez « Powershell ». Dans le menu qui apparaît, faites un clic droit sur l’application **Windows Powershell** et choisissez **Exécuter en tant qu’administrateur**.

1. **Copiez et collez** la commande ci-dessous dans l’invite Powershell et appuyez sur **Entrée**. Cette commande téléchargera la dernière version de Rhino.Compute.

    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-4')">Mettre à jour Rhino.Compute pour Rhino 7</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-4')" id="defaultOpen4">Mettre à jour Rhino.Compute pour Rhino 8</button>
    </div>

    <div class="tab-content">
    <div class="codetab-content1" id="r7-4">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/module_update_compute.ps1 -outfile update_compute.ps1; .\update_compute.ps1 
    ```

    </div>

    <div class="codetab-content1" id="r8-4">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/module_update_compute.ps1 -outfile update_compute.ps1; .\update_compute.ps1 
    ```

    </div>
    </div>

 
## Liens rapides

 - [Qu’est-ce que Hops ?](../what-is-hops)
 - [Comment fonctionne Hops](../how-hops-works)
 - [Le composant Hops](../hops-component)

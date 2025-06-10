+++
aliases = ["/en/5/guides/compute/configure-https/", "/en/6/guides/compute/configure-https/", "/en/7/guides/compute/configure-https/", "/en/wip/guides/compute/configure-https/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "AWS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Configurer Compute pour utiliser HTTPS"
type = "guides"
weight = 5
override_last_modified = "2025-02-25T08:16:19Z"

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

## Description

Dans ce guide, nous allons suivre le processus de création d’un certificat SSL valide afin que Rhino.Compute puisse communiquer avec les clients en utilisant le protocole HTTPS.

## Conditions préalables

Les conditions suivantes doivent être satisfaites :

1. Vous devez avoir une instance de machine virtuelle (VM) active. Utilisez les guides suivants pour configurer une VM.

    * [Créer une machine virtuelle sur Azure](../creating-an-Azure-VM).
    * [Créer une machine virtuelle sur AWS](../creating-an-aws-vm).

1. La VM doit être accessible via Internet (ouvrez les ports 80 et 443).

1. Une adresse IPv4 publique statique doit être associée à votre machine virtuelle. Pour en savoir plus sur la configuration d’une adresse IP statique, cliquez sur les liens suivants :
     [Configurer les adresses IP pour une interface réseau Azure](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/virtual-network-network-interface-addresses?tabs=nic-address-portal#add-ip-addresses)
     [Associer une adresse IP élastique à une instance EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)

1. Vous devez avoir un domaine existant et avoir accès à ses paramètres DNS. Un **enregistrement A** dans vos paramètres DNS doit pointer vers l’adresse IPv4 publique de votre machine virtuelle.

{{< call-out "note" "Remarque" >}}
Pour ce guide, j'ai associé une adresse IP élastique à mon instance de machine virtuelle. J’ai également configuré un enregistrement A dans mes paramètres DNS pour que *rhino.compute.rhino3d.com* pointe vers l’adresse IP de ma machine virtuelle.
{{< /call-out >}}

## Modifier le nom d’hôte

Avant de commencer à générer un certificat SSL, nous devons modifier notre configuration IIS pour Rhino.Compute.

1. Si vous ne l’avez pas encore fait, connectez-vous à votre VM (via RDP). Voir la section [Se connecter via RDP](../deploy-to-iis/#connect-via-rdp) pour plus d’informations.

1. Dans le menu **Démarrer**, cliquez dans la zone de recherche et tapez *Gestionnaire des services Internet (IIS)*. Cliquez pour lancer l’application.

1. Dans le gestionnaire IIS, **cliquez** sur le nœud du serveur Web dans le panneau **Connexions** à gauche pour développer l’arborescence du menu. Ensuite, **cliquez** sur **Sites** pour développer le sous-menu. Enfin, sélectionnez **Rhino.Compute** dans l'arborescence de menus pour modifier ses paramètres.

1. Dans le volet **Actions** à droite, cliquez sur **Liaisons**. {{< image url="/images/Site_Binding_2.png" alt="/images/Site_Binding_2.png" class="image_center" width="100%" >}}

1. Dans le volet **Liaisons de site**, cliquez sur le bouton **Ajouter**. {{< image url="/images/Site_Binding_3.png" alt="/images/Site_Binding_3.png" class="image_center" width="100%" >}}

1. Dans le champ de texte **Nom d’hôte**, tapez le nom du sous-domaine que vous avez créé lors de la configuration de l’enregistrement A. Cliquez sur **OK** une fois que vous avez terminé.
{{< image url="/images/Site_Binding_1.png" alt="/images/Site_Binding_1.png" class="image_center" width="80%" >}}

1. À ce stade, vous devez avoir deux liaisons de site dans la liste. Cliquez sur **Fermer**. {{< image url="/images/Site_Binding_4.png" alt="/images/Site_Binding_4.png" class="image_center" width="100%" >}}

## Générer le certificat

L'étape suivante consiste à créer et à installer un certificat SSL pour le serveur IIS local. Un certificat SSL est un certificat numérique qui authentifie l’identité d’un site web et permet une connexion cryptée. Il est nécessaire pour utiliser le protocole HTTPS.

Pour générer le certificat, nous recommandons d’utiliser [Win-ACME](https://www.win-acme.com/). Win-ACME est un client interactif simple qui peut créer et installer le certificat mais aussi gérer le renouvellement du certificat si nécessaire.

1. [Téléchargez le client Win-ACME](https://github.com/win-acme/win-acme/releases/download/v2.2.2.1449/win-acme.v2.2.2.1449.x64.pluggable.zip) sur la machine virtuelle. Remarque : Win-ACME est distribué sous forme d’un fichier .zip.

1. Cliquez avec le bouton droit de la souris sur le fichier .zip téléchargé et sélectionnez **Extraire tout**. Le répertoire dans lequel vous choisissez d’extraire les fichiers n’a pas vraiment d'importance, car nous les déplacerons/renommerons manuellement à l’étape suivante. Cliquez sur **Extraire**.

1. Sélectionnez le dossier de fichiers que vous venez d’extraire et appuyez sur les touches **Ctrl+X** pour **Couper** puis **Ctrl+V** pour **Coller** ce dossier dans le répertoire racine <i>C:\\</i>. 

1. Maintenant, cliquez avec le bouton droit de la souris sur le dossier que vous venez de copier dans <i>C:\\</i> et sélectionnez **Renommer** dans le menu. Raccourcissez le nom du dossier en tapant *« win-acme »*. 
{{< image url="/images/win_acme_1.png" alt="/images/win_acme_1.png" class="image_center" width="100%" >}}

1. Cliquez sur le menu Démarrer de Windows et tapez « Powershell ». Dans le menu qui apparaît, faites un clic droit sur l’application **Windows Powershell app** et choisissez **Exécuter en tant qu’administrateur**.

1. Tapez la commande suivante et appuyez sur **Entrée** pour lancer l’application Win-ACME.
```powershell
    C:\win-acme\wacs.exe
```
1. Vous devriez voir apparaître un menu interactif qui affichera une série d’instructions que vous exécuterez en tapant une lettre spécifique.
{{< image url="/images/win_acme_7.png" alt="/images/win_acme_7.png" class="image_center" width="100%" >}} 

1. Tapez la lettre **N** et appuyez sur **Entrée** pour créer un certificat avec les paramètres par défaut. Vous devriez voir une liste de sites IIS disponibles. Si vous ne voyez pas d’entrée pour **Rhino.Compute (1 binding)**, il est probable que vous n’ayez pas défini correctement le nom d’hôte à l’étape précédente. Reportez-vous à la section [modifier le nom d’hôte](#modify-the-host-name).
{{< image url="/images/win_acme_8.png" alt="/images/win_acme_8.png" class="image_center" width="100%" >}} 

1. Tapez le numéro associé à la ligne **Rhino.Compute (1 binding)** et appuyez sur **Entrée**.
{{< image url="/images/win_acme_9.png" alt="/images/win_acme_9.png" class="image_center" width="100%" >}} 

1. Appuyez sur **Entrée** à nouveau pour accepter la valeur par défaut **Pick all bindings**.

1. Le programme vous demande ensuite si vous souhaitez continuer avec la sélection (*Continue with this selection?*). Appuyez sur **Entrée** ou tapez **Y** pour « yes » (oui).
{{< image url="/images/win_acme_10.png" alt="/images/win_acme_10.png" class="image_center" width="100%" >}} 

1. Des informations s’affichent alors dans la console au fur et à mesure que le certificat SSL est généré.
{{< image url="/images/win_acme_11.png" alt="/images/win_acme_11.png" class="image_center" width="100%" >}} 

Félicitations ! Si tout se passe bien, l’application exécute une série de tests d’autorisation et de validation pour confirmer que l’hôte est sécurisé. Win-ACME génère alors le certificat SSL et l’installe avec IIS, puis ajoute une nouvelle liaison **(*:443)** au site Rhino.Compute. Le certificat SSL est valable pendant 90 jours. Cependant, l’application Win-ACME créera un planificateur de tâches qui tentera de renouveler le certificat après 60 jours. Vous devriez maintenant pouvoir envoyer une requête HTTPS à votre serveur Rhino.Compute et obtenir une réponse valide en retour.

<br>

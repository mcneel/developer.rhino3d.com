+++
aliases = ["/en/5/guides/compute/creating-an-Azure-VM/", "/en/6/guides/compute/creating-an-Azure-VM/", "/en/7/guides/compute/creating-an-Azure-VM/", "/en/wip/guides/compute/creating-an-Azure-VM/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "Azure" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Comment créer une machine virtuelle (VM) dans Azure ?"
type = "guides"
weight = 2
override_last_modified = "2022-02-14T14:13:06Z"

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

## Créer la machine virtuelle

Dans ce guide, vous apprendrez comment configurer une machine virtuelle dans le portail Azure. 

Pour commencer, vérifiez que vous disposez d’un abonnement Azure valide et que vous avez déjà configuré un groupe de ressources pour stocker les différentes ressources de cette instance. Pour en savoir plus sur la configuration d’un groupe de ressources sur Azure, [visitez cette page](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal).

1. Connectez-vous au [portail Azure](https://portal.azure.com/#home).

1. Tapez **machines virtuelles** dans la barre de recherche.

1. Sous **Services**, sélectionnez **Machines virtuelles**.

1. Sur la page **Machines virtuelles**, sélectionnez **Créer** puis **Machine virtuelle**.

1. Dans l’onglet **De base**, sous **Détails du projet**, assurez-vous que l’abonnement et le groupe de ressources corrects sont sélectionnés.

1. Sous **Détails de l’instance**, donnez un nom unique à votre machine virtuelle. Nous appellerons notre machine virtuelle *Rhino-Compute-VM*. Choisissez une région proche de chez vous, puis sélectionnez *Windows Server 2022 Datacenter - Azure Edition Gen2* pour l’**Image**. Choisissez la **taille** de votre VM en fonction de vos besoins. Nous utiliserons *Standard DS2_v2* pour cet exemple. Laissez les autres valeurs par défaut.
{{< image url="/images/Azure_VM_Create3.png" alt="/images/Azure_VM_Create3.png" class="image_center" width="100%" >}}

1. Sous **Compte d’administrateur**, indiquez un nom d’utilisateur et un mot de passe. Notez bien ces informations d’identification, car vous les utiliserez pour vous connecter à la machine distante.

1. Sous **Règles des ports d’entrée**, choisissez **Autoriser les ports sélectionnés** puis sélectionnez **RDP (3389)**, **HTTPS (443)** et **HTTP (80)**.
{{< image url="/images/Azure_VM_Create4.png" alt="/images/Azure_VM_Create4.png" class="image_center" width="100%" >}}

1. Sélectionnez **Suivant : Disques >**.

1. Sélectionnez **Suivant : Mise en réseau >**.

1. Dans la section **Interface réseau**, cliquez sur le bouton *Créer* sous la sous-section **Adresse IP publique**.

1. Lorsque la fenêtre contextuelle s’ouvre, sélectionnez **Statique** sous l’onglet Affectation. Cliquez sur **Ok** pour enregistrer cette configuration.
{{< image url="/images/Azure_VM_Create5.png" alt="/images/Azure_VM_Create5.png" class="image_center" width="100%" >}}

1. Laissez toutes les autres valeurs par défaut. Cliquez sur **Vérifier + créer**.

1. Une fois que votre configuration a passé le contrôle de validation, cliquez sur **Créer** pour déployer votre machine virtuelle.

1. Après avoir terminé le déploiement, sélectionnez **Accéder à la ressource**.

### Ajouter une règle de port d’entrée

Une fois que votre machine virtuelle a été déployée, vous devriez pouvoir accéder à la page d’accueil des ressources. Vous pouvez y modifier divers paramètres de votre configuration. Nous allons ajouter une règle de port d’entrée afin de pouvoir envoyer des demandes d’API sur un port dédié.

Par défaut, Azure refuse et bloque tout le trafic public entrant, y compris le trafic ICMP. C’est une bonne chose étant donné que cela renforce la sécurité en réduisant la surface d’attaque. Le protocole [ICMP (Internet Control Message Protocol)](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) est généralement utilisé pour les diagnostics et pour résoudre les problèmes de mise en réseau. 

Nous allons activer le trafic ICMP pour notre VM afin d’essayer d’envoyer un ping à l’adresse IP et de nous assurer que nous obtenons une réponse. La première chose à faire est d’ajouter une règle de port d’entrée pour le trafic ICMP. 

1. Dans le menu de gauche, sélectionnez **Mise en réseau**. Cela ouvrira le panneau Mise en réseau.

1. Cliquez sur le bouton **Ajouter une règle de port d’entrée**.
{{< image url="/images/Azure_VM_Create6.png" alt="/images/Azure_VM_Create6.png" class="image_center" width="100%" >}}

1. Dans le volet **Ajouter une règle de sécurité d’entrée**, configurez les **Plages des ports de destination** sur *, mettez le **Protocole** sur **ICMP**, la **Priorité** sur **100** et tapez **ICMP** dans le champ **Nom**.
{{< image url="/images/Azure_VM_Create8.png" alt="/images/Azure_VM_Create8.png" class="image_center" width="75%" >}}

1. Cliquez sur **Ajouter** pour créer la nouvelle règle de port d’entrée.

Félicitations ! Vous venez de déployer une machine virtuelle simple sur Azure.
+++
aliases = ["/en/5/guides/compute/creating-an-aws-vm/", "/en/6/guides/compute/creating-an-aws-vm/", "/en/7/guides/compute/creating-an-aws-vm/", "/en/wip/guides/compute/creating-an-aws-vm/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "AWS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Comment créer une machine virtuelle (VM) sur Amazon Web Service ?"
type = "guides"
weight = 3
override_last_modified = "2021-12-14T13:16:19Z"

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

Dans ce guide, vous apprendrez comment configurer une machine virtuelle en utilisant Amazon Elastic Compute Cloud (Amazon EC2). 

Pour commencer, vous allez devoir confirmer votre abonnement à AWS. Si vous ne connaissez pas encore AWS, vous pouvez commencer à utiliser Amazon EC2 avec l’[offre gratuite d’AWS](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all). 

{{< call-out "note" "Remarque" >}}
Si vous avez créé votre compte AWS il y a moins de 12 mois et que vous n’avez pas encore dépassé les avantages du niveau gratuit pour Amazon EC2, vous allez pouvoir réaliser toutes les étapes de ce tutoriel gratuitement. Dans le cas contraire, vous devrez payer les frais d’utilisation standard d’Amazon EC2 à partir du moment où vous lancez l’instance et jusqu’à ce que vous la résiliiez, même si elle reste inactive.
{{< /call-out >}}

## Conditions préalables

1. [Créer un compte AWS](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#sign-up-for-aws)

1. [Créer une paire de clés](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-key-pair).  Nous vous recommandons d’enregistrer le **fichier de clé privée** au format **.pem** avec un cryptage **RSA**.

1. [Créer un groupe de sécurité ](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-base-security-group). Nous vous recommandons d’ajouter une règle pour **HTTP**, **HTTPS**, **RDP** et **Tous les ICMP - IPv4**.

## Lancer l’instance

Pour créer une nouvelle instance de machine virtuelle sur AWS, procédez comme suit :

1. Ouvrez la [console Amazon EC2](https://console.aws.amazon.com/ec2/).

1. Dans le tableau de bord de la console EC2, sélectionnez **Launch Instance**.

1. Donnez un nom à votre instance de machine virtuelle. Pour ce tutoriel, nous utiliserons le nom **« RhinoComputeVM »**.

1. Dans la section intitulée Application and OS Images, cliquez sur le bouton **Windows** sous l’onglet Quick Start. Dans la section Amazon Machine Image (AMI), vous trouverez un menu déroulant répertoriant toutes les images de machines disponibles. Sélectionnez l’AMI pour **Microsoft Windows Server 2022 Base**.</p>
{{< image url="/images/AWS_Setup_11.png" alt="/images/AWS_Setup_11.png" class="image_left" width="90%" >}}

1. Dans la section **Instance Type**, sélectionnez le type d’instance **t2.micro** (par défaut) ou un type d’instance plus grand si nécessaire. Remarque : le type d’instance *t2.micro* est disponible avec l’offre gratuite. Si *t2.micro* n’est pas disponible dans votre région, vous pouvez utiliser une instance *t3.micro** dans le cadre de l’offre gratuite.</p>
{{< image url="/images/AWS_Setup_12.png" alt="/images/AWS_Setup_12.png" class="image_left" width="90%" >}}

1. Dans la section **Key Pair (login)**, sélectionnez dans la liste déroulante le nom de la paire de clés que vous avez créée à l’étape 2 du paragraphe [conditions préalables](../creating-an-aws-vm/#prerequisites).</p>
{{< image url="/images/AWS_Setup_13.png" alt="/images/AWS_Setup_13.png" class="image_left" width="90%" >}}

1. Dans la section **Network Settings**, sous **Firewall (security groups)** cliquez sur le bouton **Select existing security group**. Ensuite, dans la liste déroulante **Common Security Groups**, sélectionnez le groupe de sécurité que vous avez créé à l’étape 3 du paragraphe [conditions préalables](../creating-an-aws-vm/#prerequisites).{{< call-out "warning" "Important" >}}Si le paramètre **Auto-assign public IP** est configuré sur **Disabled**, cliquez sur le bouton **Edit** en haut à droite de ce panneau et sélectionnez **Enabled** pour ce paramètre.{{< /call-out >}}
{{< image url="/images/AWS_Setup_14.png" alt="/images/AWS_Setup_14.png" class="image_left" width="90%" >}}

1. Dans la section **Configure storage**, sélectionnez l’espace de stockage par défaut pour cette instance.

1. Maintenant, tout à fait à droite, cliquez sur **Launch Instance**.

1. Une page de confirmation vous indique que votre instance a été lancée avec succès. Tout en haut, dans le menu intitulé **EC2 > Instances > Launch an instance**, sélectionnez **Instances** pour afficher la fenêtre de la console des instances.</p>
{{< image url="/images/AWS_Setup_15.png" alt="/images/AWS_Setup_15.png" class="image_left" width="90%" >}}

1. Sur l’écran **Instances**, vous pouvez voir l’état de l’instance lancée. L’instance devrait s’exécuter automatiquement après le lancement, mais si ce n’est pas le cas, cochez la case de la ligne d’instance et sélectionnez ensuite l'élément **Instance State** en haut. Sélectionnez **Start Instance** pour démarrer la machine virtuelle.

1. Après avoir sélectionné la ligne d’instance, cliquez sur le bouton **Connect** dans le menu supérieur.

1. Sur la page **Connect to instance**, sélectionnez l’onglet **RDP client**.

1. Ensuite, cliquez sur le bouton **Get password**.

1. Choisissez **Upload private key file** et naviguez jusqu’au fichier de clé privée (.pem) que vous avez créé lorsque vous avez lancé l’instance.

1. Cliquez sur **Decrypt Password**. Sous **Password**, à la place du lien **Get password**, la console affiche le mot de passe administrateur par défaut pour l’instance. **Conservez ce mot de passe en lieu sûr**. Vous en aurez besoin pour vous connecter à l’instance.

1. Sélectionnez **Download remote desktop file** pour enregistrer le fichier .rdp sur votre ordinateur local. Vous aurez besoin de ce fichier lorsque vous vous connecterez à votre instance à travers l’application Remote Desktop Connect.

Félicitations ! Dans ce tutoriel, vous avez mis en place une machine virtuelle sur AWS et téléchargé le fichier RDP qui vous permettra de vous connecter à cette instance.
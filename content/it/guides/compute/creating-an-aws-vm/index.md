+++
aliases = ["/en/5/guides/compute/creating-an-aws-vm/", "/en/6/guides/compute/creating-an-aws-vm/", "/en/7/guides/compute/creating-an-aws-vm/", "/en/wip/guides/compute/creating-an-aws-vm/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "AWS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title= "Come creare una macchina virtuale (VM) su Amazon Web Service"
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

## Panoramica

In questa guida, illustreremo il processo di impostazione di una macchina virtuale utilizzando Amazon Elastic Compute Cloud (Amazon EC2). 

Per iniziare, è necessario confermare l'abbonamento ad AWS. Se non hai mai usato AWS, puoi iniziare con Amazon EC2 utilizzando il [AWS Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all). 

{{< call-out "note" "Nota" >}}
Se hai creato un account AWS meno di 12 mesi fa e non hai già superato i vantaggi del livello gratuito per Amazon EC2, non ti sarà difficile completare questo tutorial. In caso contrario, si dovranno sostenere le tariffe d'uso standard di Amazon EC2 dal momento in cui si avvia l'istanza fino al termine, anche se rimane inattiva.
{{< /call-out >}}

## Prerequisiti

1. [Creare un account per AWS](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#sign-up-for-aws)

1. [Creare una coppia di chiavi](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-key-pair). Nota: Si consiglia di salvare il file della **chiave privata** in formato **.pem** con crittografia **RSA** .

1. Crea un nuovo gruppo Si consiglia di aggiungere una regola per **HTTP**, **HTTPS**, **RDP** e **All ICMP - IPv4**.

## Avviare l'istanza

Per creare una nuova istanza di macchina virtuale su AWS, procedere come segue:

1. Aprire la [console Amazon EC2](https://console.aws.amazon.com/ec2/).

1. Dalla dashboard della console EC2, selezionare **Launch Instance**.

1. Assegnare un nome alla tipologia VM. Per questo tutorial, utilizzeremo il nome **"RhinoComputeVM"**.

1. Nella sezione Application and OS Images, fare clic sul pulsante **Windows** sotto il pannello Quick Start. Nella sezione Amazon Machine Image (AMI), dovrebbe essere presente un menu a discesa che elenca tutte le immagini macchina disponibili. Selezionare l'AMI per **Microsoft Windows Server 2022 Base**.</p>
{{< image url="/images/AWS_Setup_11.png" alt="/images/AWS_Setup_11.png" class="image_left" width="90%" >}}

1. Nella sezione **Instance Type**, selezionare il tipo di istanza **t2.micro** (predefinito) o un tipo di istanza più grande, se necessario. Nota: il tipo di istanza *t2.micro* è idonea per il livello gratuito. Nelle regioni in cui *t2.micro* non è disponibile, è possibile utilizzare un'istanza *t3.micro** con il livello gratuito.</p>
{{< image url="/images/AWS_Setup_12.png" alt="/images/AWS_Setup_12.png" class="image_left" width="90%" >}}

1. Nella sezione **Key Pair (login)**, selezionare il nome della coppia di chiavi creata nel passaggio 2 della sezione prerequisiti [sezione prerequisiti](../creating-an-aws-vm/#prerequisites) dall'elenco a discesa.</p>
{{< image url="/images/AWS_Setup_13.png" alt="/images/AWS_Setup_13.png" class="image_left" width="90%" >}}

1. Nella sezione **Network Settings**, in **Firewall (security groups)** selezionare il pulsante di opzione **Select existing security group**. Quindi, nell'elenco a discesa **Common Security Groups**, selezionare il gruppo di sicurezza creato al punto 3 della [sezione prerequisiti](../creating-an-aws-vm/#prerequisites).{{< call-out "warning" "Importante" >}}Se l'impostazione **Auto-assign public IP** è impostata su **Disabled**, fare clic sul pulsante **Edit** in alto a destra del pannello di questa sezione e modificare l’impostazione in **Enabled**.{{< /call-out >}}
{{< image url="/images/AWS_Setup_14.png" alt="/images/AWS_Setup_14.png" class="image_left" width="90%" >}}

1. Nella sezione **Configure storage**, selezionare la quantità di archiviazione predefinita per questa istanza.

1. Ora, a destra, selezionare **Launch Instance**.

1. Una pagina di conferma informa che l'istanza è stata avviata correttamente. Nel menu in alto **EC2 > Istances > Launch an instance**, selezionate la voce di menu **Istances** per visualizzare la finestra della console delle istanze.</p>
{{< image url="/images/AWS_Setup_15.png" alt="/images/AWS_Setup_15.png" class="image_left" width="90%" >}}

1. Nella schermata **Istances**, è possibile visualizzare lo stato dell'istanza avviata. L'istanza dovrebbe essere automaticamente in esecuzione dopo l'avvio, ma in caso contrario selezionare la casella di controllo della riga dell'istanza e quindi selezionare la voce di menu **Stato dell'istanza** in alto. Selezionare **Instance State** per avviare la macchina virtuale.

1. Con la riga dell'istanza selezionata, fare clic sul pulsante **Connect** nel menu superiore.

1. Nella pagina **Connect to instance**, selezionare il pannello **Client RDP**.

1. Quindi, selezionare il pulsante **Get password**.

1. Scegliere **Upload private key file** e navigare fino al file della chiave privata (.pem) creato all'avvio dell'istanza.

1. Scegliere **Decrypt password**. La console visualizza la password di amministratore predefinita per l'istanza in**Password**, sostituendo il link **Get password** mostrato in precedenza. **Salvare questa password in un luogo sicuro**. Questa password è necessaria per connettersi all'istanza.

1. Selezionare **Download remote desktop file** per salvare il file .rdp sul computer locale. Questo file è necessario quando ci si connette all'istanza utilizzando l'applicazione Remote Desktop Connect.

Ottimo lavoro! In questo tutorial, è stata avviata correttamente una macchina virtuale su AWS ed è stato scaricato il file RDP che può essere usato per connettersi all'istanza.
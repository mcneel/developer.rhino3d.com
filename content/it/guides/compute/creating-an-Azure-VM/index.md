+++
aliases = ["/en/5/guides/compute/creating-an-Azure-VM/", "/en/6/guides/compute/creating-an-Azure-VM/", "/en/7/guides/compute/creating-an-Azure-VM/", "/en/wip/guides/compute/creating-an-Azure-VM/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "Azure" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title= "Come creare una macchina virtuale (VM) su Azure"
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

## Creazione della macchina virtuale

In questa guida, illustreremo il processo di impostazione di una macchina virtuale utilizzando i servizi di Azure. 

Per iniziare, confermiamo di avere un abbonamento valido ad Azure e di aver già impostato un gruppo di risorse per contenere le varie risorse di questa istanza. Per informazioni sull'impostazione di un gruppo di risorse su Azure, [visita questa pagina](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal).

1. Accedere al [portale Azure](https://portal.azure.com/#home).

1. Digitare **virtual machine** nella barra di ricerca.

1. In **Services**, selezionare **Virtual machines**.

1. Nella pagina **Virtual machines**, selezionare **Create**, quindi **Virtual Machine**.

1. In **Basics**, sotto **Project details**, assicurarsi che siano selezionati i gruppi corretti Subscription e Resource.

1. In **Instance details**, creare un nome univoco per la macchina virtuale. Utilizzeremo *Rhino-Compute-VM* per il nome della nostra VM. Selezionare una regione vicina, quindi selezionare *Windows Server 2022 Datacenter - Azure Edition Gen2* per **Image**. Scegliere una macchina virtuale di **dimensioni** adatte alle proprie esigenze. Per questo esempio utilizzeremo *Standard DS2_v2*. Lasciare le altre impostazioni predefinite.
{{< image url="/images/Azure_VM_Create3.png" alt="/images/Azure_VM_Create3.png" class="image_center" width="100%" >}}

1. In **Administrator account**, fornire un nome utente e una password. Prendere nota di queste credenziali, perché le utilizzeremo quando ci collegheremo al computer remoto.

1. In **Inbound port rules**, scegliere **Allow selected ports** e selezionare **RDP (3389)**, **HTTPS (443)**e **HTTP (80)**.
{{< image url="/images/Azure_VM_Create4.png" alt="/images/Azure_VM_Create4.png" class="image_center" width="100%" >}}

1. Selezionare **Next : Disk >**.

1. Selezionare **Next : Networking >**.

1. In **Network interface**, fare clic sul pulsante *Create new* nella sottosezione **Public IP**.

1. Quando si apre il menu a comparsa, selezionare **Static** nel pannello Assegnazione. Fare clic su **OK** per salvare le modifiche.
{{< image url="/images/Azure_VM_Create5.png" alt="/images/Azure_VM_Create5.png" class="image_center" width="100%" >}}

1. Lasciare tutte le altre impostazioni predefinite. Selezionare **Review + create**.

1. Una volta che la configurazione ha superato il controllo di convalida, selezionare **Create** per distribuire la macchina virtuale.

1. Al termine della distribuzione, selezionare **Go to resource**.

### Aggiungere una regola di porta in entrata

Una volta che la macchina virtuale è stata distribuita, si dovrebbe essere in grado di accedere alla pagina iniziale della risorsa. Qui è possibile modificare varie impostazioni e configurazioni. Aggiungeremo una regola di porta in entrata, in modo da poter inviare le richieste API su una porta dedicata.

Di default, Azure rifiuta e blocca tutto il traffico pubblico in entrata, che include anche il traffico ICMP. Questo è un aspetto positivo, poiché migliora la sicurezza riducendo la superficie di attacco. Il protocollo [ICMP (Internet Control Message Protocol)](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) è tipicamente utilizzato per la diagnostica e la risoluzione di problemi di rete. 

Vogliamo attivare il traffico ICMP per la nostra macchina virtuale, in modo da poter provare a eseguire il ping dell'indirizzo IP e assicurarci di ottenere una risposta. La prima cosa da fare è aggiungere una regola di porta in entrata per il traffico ICMP. 

1. Nel menu a sinistra, selezionare la voce di menu **Networking**. Si apre il menu Networking.

1. Fare clic sul pulsante **Add inbound port rule**.
{{< image url="/images/Azure_VM_Create6.png" alt="/images/Azure_VM_Create6.png" class="image_center" width="100%" >}}

1. Sul pannello **Add inbound port rule**, impostare **Destination port ranges** su *, cambiare **Protocol** in **ICMP**, impostare **Priority** su **100**e digitare **ICMP** nell'input **Name**.
{{< image url="/images/Azure_VM_Create8.png" alt="/images/Azure_VM_Create8.png" class="image_center" width="75%" >}}

1. Fare clic su **Add** per creare la nuova regola della porta in entrata.

Ottimo lavoro! In questa guida è stata distribuita una semplice macchina virtuale su Azure.
+++
aliases = ["/en/5/guides/compute/configure-https/", "/en/6/guides/compute/configure-https/", "/en/7/guides/compute/configure-https/", "/en/wip/guides/compute/configure-https/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "AWS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Configurazione di Compute per usare HTTPS."
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

## Panoramica

In questa guida, illustreremo il processo di creazione di un certificato SSL valido, in modo che Rhino.Compute possa comunicare con i client utilizzando il protocollo HTTPS.

## Prerequisiti

È necessario completare quanto segue:

1. È richiesta un'istanza di macchina virtuale (VM) attiva. Utilizzare le seguenti guide per configurare una macchina virtuale.

    * [Creare una macchina virtuale su Azure](../creating-an-Azure-VM).
    * [Creare una macchina virtuale su AWS](../creating-an-aws-vm).

1. La macchina virtuale deve essere accessibile al web (aprire le porte 80 e 443).

1. Alla macchina virtuale deve essere associato un indirizzo IPv4 pubblico statico. Per ulteriori informazioni sulla configurazione dell'indirizzo IP statico, utilizzare i seguenti link:
    * [Configurare gli indirizzi IP per un'interfaccia di rete di Azure](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/virtual-network-network-interface-addresses?tabs=nic-address-portal#add-ip-addresses)
    * [Indirizzi IP elastici](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)

1. È necessario avere un dominio esistente e avere accesso alle impostazioni DNS. Un **record A** nelle impostazioni DNS deve puntare all'indirizzo IPv4 pubblico della macchina virtuale.

{{< call-out "note" "Nota" >}}
Per questa guida, abbiamo associato un indirizzo IP elastico all'istanza della macchina virtuale. Ho anche impostato un record A nelle mie impostazioni DNS per puntare *rhino.compute.rhino3d.com* all'indirizzo IP della macchina virtuale.
{{< /call-out >}}

## Modificare il nome host

Prima di procedere alla creazione di un certificato SSL, occorre modificare la configurazione IIS esistente per Rhino.Compute.

1. Se non è stato ancora fatto, accedere alla macchina virtuale (tramite RDP). Per ulteriori informazioni, consultare la sezione [Collegamento mediante RDP](../deploy-to-iis/#connect-via-rdp) .

1. Nel menu **Start**, fare clic nell'area di ricerca e digitare *Internet Information Services (IIS) Manager*. Fare clic per avviare l'applicazione.

1. In IIS Manager, **fare clic** sul nodo del server web, sul pannello **Connections** a sinistra per espandere il menu. Quindi **fare clic** sul nodo **Sites** per espandere il sottomenu. Infine, selezionare il nodo **Rhino.Compute** dal menu per regolarne le impostazioni.

1. Sul pannello **Actions** a destra, fare clic su **Bindings**. {{< image url="/images/Site_Binding_2.png" alt="/images/Site_Binding_2.png" class="image_center" width="100%" >}}

1. Sul pannello **Site Bindings**, selezionare il pulsante **Add**. {{< image url="/images/Site_Binding_3.png" alt="/images/Site_Binding_3.png" class="image_center" width="100%" >}}

1. Nel campo di testo **Host name**, digitare il nome del sottodominio creato durante l'impostazione del record A. Al termine, fare clic su **OK**.
{{< image url="/images/Site_Binding_1.png" alt="/images/Site_Binding_1.png" class="image_center" width="80%" >}}

1. A questo punto, dovrebbero essere elencati due associazioni. Al termine, fare clic su **Close**. {{< image url="/images/Site_Binding_4.png" alt="/images/Site_Binding_4.png" class="image_center" width="100%" >}}

## Creare il certificato

Il passo successivo consiste nel creare e installare un certificato SSL per il server IIS locale. Un certificato SSL è un certificato digitale che autentica l'identità di un sito web e consente una connessione crittografata. Il certificato SSL è necessario per utilizzare il protocollo HTTPS.

Per crearlo, si consiglia di utilizzare [Win-ACME](https://www.win-acme.com/). Win-ACME è un semplice client interattivo in grado di creare e installare il certificato e di gestirne il rinnovo quando necessario.

1. [Scaricare il client Win-ACME](https://github.com/win-acme/win-acme/releases/download/v2.2.2.1449/win-acme.v2.2.2.1449.x64.pluggable.zip) sulla macchina virtuale. Nota: Win-ACME è distribuito come file .zip.

1. Fare clic con il pulsante destro del mouse sul file .zip scaricato e selezionare **Estrai tutto**. Non è importante quale sia la directory in cui estrarre i file, perché li sposteremo/rinomineremo manualmente nella fase successiva. Fare clic su **Estrai**.

1. Selezionare la cartella appena estratta e digitare **Ctrl+X** per **tagliare** e quindi **Ctrl+V** per **incollare** questa cartella nell'unità principale <i>C:\\</i>. 

1. A questo punto, fare clic con il pulsante destro del mouse sulla directory appena copiata nell'unità <i>C:\\</i> e selezionare **Rinomina** dal menu. Abbreviare il nome della cartella in *"win-acme"*. 
{{< image url="/images/win_acme_1.png" alt="/images/win_acme_1.png" class="image_center" width="100%" >}}

1. Fare clic sul menu di avvio di Windows e digitare "Powershell". Nel menu visualizzato, fare clic con il pulsante destro del mouse sull'applicazione **Windows Powershell** e scegliere **Run As Administrator**.

1. Digitare il seguente comando e premere **Invio** per avviare l'applicazione Win-ACME.
```powershell
    C:\win-acme\wacs.exe
```
1. Dovrebbe apparire un menu interattivo con una serie di istruzioni che possono essere eseguite digitando una lettera specifica.
{{< image url="/images/win_acme_7.png" alt="/images/win_acme_7.png" class="image_center" width="100%" >}} 

1. Digitare la lettera **N** e premere **Invio** per creare un certificato con le impostazioni predefinite. Dovrebbe essere visualizzato un elenco di siti IIS disponibili. Se non appare una voce per **Rhino.Compute (1 binding)** è probabile che non sia stato impostato correttamente il nome host nel passaggio precedente. Consultare la sezione [Modificare il nomehost](#modify-the-host-name).
{{< image url="/images/win_acme_8.png" alt="/images/win_acme_8.png" class="image_center" width="100%" >}} 

1. Digitare il numero associato alla riga per **Rhino.Compute (1 binding)** e premere **Invio**.
{{< image url="/images/win_acme_9.png" alt="/images/win_acme_9.png" class="image_center" width="100%" >}} 

1. Premere di nuovo **Invio** per accettare l'impostazione predefinita **Pick all bindings**.

1. Quando appare il messaggio *Continue with this selection?* premere **Invio** o digitare **Y** per confermare.
{{< image url="/images/win_acme_10.png" alt="/images/win_acme_10.png" class="image_center" width="100%" >}} 

1. Dovrebbero apparire alcune informazioni sulla console durante la creazione del certificato SSL.
{{< image url="/images/win_acme_11.png" alt="/images/win_acme_11.png" class="image_center" width="100%" >}} 

Ottimo lavoro! Se la procedura è stata eseguita correttamente, l'applicazione eseguirà una serie di test di autorizzazione e convalida per confermare la sicurezza dell'host. Win-ACME creerà quindi il certificato SSL, lo installerà con IIS e aggiungerà una nuova associazione **(*:443)** al sito Rhino.Compute. Il certificato SSL sarà valido per 90 giorni. Tuttavia, l'applicazione Win-ACME creerà un’utilità di pianificazione che cercherà di rinnovare il certificato dopo 60 giorni. Ora dovremmo essere in grado di inviare una richiesta HTTPS al server Rhino.Compute e ricevere una risposta valida.

<br>

+++
aliases = ["/en/5/guides/compute/deploy-to-iis/", "/en/6/guides/compute/deploy-to-iis/", "/en/7/guides/compute/deploy-to-iis/", "/en/wip/guides/compute/deploy-to-iis/", "/en/guides/compute/deploy/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
description = "Come distribuire Rhino Compute per la produzione su una macchina con Internet Information Services (IIS)."
keywords = [ "developer", "compute", "production", "IIS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Distribuzione sui server di produzione"
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

## Panoramica

Questa guida spiegherà come configurare un'istanza di Rhino.Compute su una macchina virtuale con Internet Information Services (IIS). [IIS](https://www.iis.net/) è un server web flessibile e generico sviluppato da Microsoft, che può essere configurato per servire le pagine o i file HTML richiesti. Possiamo impostare IIS in modo che elabori le richieste in arrivo (da Hops o da un altro client) e le inoltri all'istanza di Rhino.Compute. 

Potremmo chiederci: "Perché ho bisogno di IIS? Perché non posso semplicemente lanciare il server Rhino.Compute e inviare le richieste API direttamente a quell'istanza?" Tecnicamente parlando, non è necessario IIS. Tuttavia, occorre capire come rilanciare il server Compute in caso di arresto o malfunzionamento. È inoltre necessario configurare Rhino.Compute in modo che venga avviato ogni volta che si apre la macchina virtuale. 

Uno dei principali vantaggi dell'uso di IIS come middleware è che può avviare automaticamente un'istanza del server Rhino.Compute ogni volta che viene ricevuta una richiesta. Con questa configurazione, non è necessario che Compute sia in funzione continuamente. Invece, se necessario, IIS può avviare un'istanza di Compute, che a sua volta avvierà uno o più processi figli. Questi processi figli sono quelli che eseguono i calcoli veri e propri e che richiedono l'autorizzazione della licenza. 

Quando Rhino.Compute.exe non riceve richieste di risoluzione per alcuni secondi (questo periodo è chiamato idlespans e l'impostazione predefinita è di 1 ora), i processi figli di compute.geometry.exe si chiuderanno e smetteranno di incorrere nella fatturazione nucleo per ora. In futuro, quando verrà ricevuta una nuova richiesta, IIS si accerterà che Rhino.Compute.exe sia in esecuzione e riavvierà i processi figli. Nota: la risposta potrebbe subire un piccolo ritardo durante l'avvio dei processi figli.

{{< image url="/images/IIS_Request.png" alt="/images/IIS_Request.png" class="image_center" width="100%" >}}
<figcaption align = "left"><b>Fig.1 - Un diagramma di flusso che mostra come IIS riceve una richiesta in entrata e apre Rhino.Compute.exe che a sua volta avvia processi figli.</b></figcaption>

## Prerequisiti

Prima di eseguire lo script di bootstrap sul server o sulla macchina virtuale, sono necessarie le seguenti informazioni.

* **`EmailAddress`** - Lo script utilizzerà questo indirizzo e-mail per scaricare una copia di Rhino da installare. È simile al comportamento della pagina di download di Rhino.
* **API Key** - La chiave API è una stringa di testo segreta per il server di il server Compute e per le applicazioni che utilizzano l'API di calcolo, ad esempio `b8f91f04-3782-4f1c-87ac-8682f865bf1b`. In pratica, è il modo in cui il server Compute si assicura che le chiamate API provengano solo dalle tue applicazioni. È possibile inserire qualsiasi stringa che sia unica e segreta per l'utente e per le app di calcolo. Assicurati di conservarla in un luogo sicuro.
* **`RhinoToken`** – Questo è un token esteso che identifica l’istanza di Rhino Compute nel sistema di fatturazione nucleo per ora. Accedere al [Portale licenze](https://www.rhino3d.com/licenses?_forceEmpty=true) per creare questo ID univoco in base alla licenza. Per ulteriori informazioni, consultare la guida ["Fatturazione nucleo per ora](../core-hour-billing/) .

{{< call-out "note" "Nota" >}}
L'esecuzione di Rhino Compute a livello locale utilizza la licenza di Rhino esistente e non comporta costi aggiuntivi (a parte l'investimento iniziale nella licenza di Rhino). L'esecuzione di Compute in locale è l'opzione migliore per lo sviluppo e i test e per ulteriori informazioni, consultare <a href="../development"><u>Esecuzione e debug di Compute in locale</u></a>.<br><br>

Tuttavia, quando si configura un ambiente di produzione, è necessario un server o una macchina virtuale preinstallata con Windows Server 2019 o superiore. Le licenze funzionano in modo diverso quando si esegue Rhino (cioè tramite Compute) in un ambiente di produzione (cioè con un server) e verrà addebitata una tariffa di 0,10 dollari per nucleo all'ora. <br><br>

Consulta la <a href="../core-hour-billing"><u>guida "Fatturazione nucleo per ora"</u></a> per configurarla. Questo punto è importante, quindi consigliamo di non saltarlo.
{{< /call-out >}}

## Creare la macchina virtuale

Il primo passo nel processo di distribuzione di **Rhino.Compute** per la produzione consiste nell'impostare una macchina fisica che funga da server o nel creare una macchina virtuale (VM). Per questa guida, utilizzeremo una macchina virtuale. Esistono diversi servizi popolari che possono essere configurati per impostare un'ampia gamma di macchine virtuali, a seconda delle risorse richieste. Due dei fornitori più importanti sono [Azure](https://azure.microsoft.com/en-us/free/virtual-machines/) e [AWS](https://aws.amazon.com/ec2/instance-types/).  

A seconda delle preferenze, si consiglia di iniziare con una macchina virtuale Azure o AWS. Utilizzare le seguenti guide per configurare una macchina virtuale.

* [Creare una macchina virtuale su Azure](../creating-an-Azure-VM).

* [Creare una macchina virtuale su AWS](../creating-an-aws-vm).

### Connettersi tramite RDP

Ora che abbiamo configurato la macchina virtuale, dobbiamo essere in grado di accedervi per poter configurare IIS e l'istanza di Rhino.Compute. A tale scopo utilizzeremo un protocollo di desktop remoto (RDP) che collega due computer in rete.

Per iniziare, scarichiamo il file RDP. Utilizzeremo il portale delle macchine virtuali di Azure e per AWS si utilizza una procedura simile.

1. Innanzitutto, dobbiamo assicurarci che la macchina virtuale sia in funzione. Fare clic sul pannello **Overview** nel menu a sinistra. Se in *Status* viene indicato *Stopped (Deallocated)*, fare clic sul pulsante **Start** in alto per avviare il computer remoto. Dopo qualche secondo, lo stato dovrebbe indicare *Running*.

1. Fare clic sulla voce del menu **Connect** nel menu di sinistra per aprire la finestra delle impostazioni di connessione.

1. Fare clic sul pulsante **Download RDP File** e salvare il file sul computer.
{{< image url="/images/Azure_VM_Connect1.png" alt="/images/Azure_VM_Connect1.png" class="image_center" width="100%" >}}

1. Fare clic sul menu **Avvio** di Windows e digitare *remote desktop connection* nella barra di ricerca. Fare clic sul link per avviare l'applicazione.

1. Fare clic sul pulsante **Show Options** in fondo alla pagina.

1. Nell'area *Connection Settings*, selezionare **Open** e navigare nella directory in cui è stato salvato il file RDP. Scegliere il file e premere Open.

1. Selezionare l’opzione **Allow me to save credentials**.

1. Fare clic su **Connetti**.
{{< image url="/images/Azure_VM_Connect2.png" alt="/images/Azure_VM_Connect2.png" class="image_center" width="60%" >}}

1. Si aprirà un pop-up di sicurezza. Fare clic sull’opzione **Don't ask me again for connections to this computer** e quindi su **Connect**.

1. Immettere le credenziali dell'amministratore inserite nel passaggio 7 in [Creazione di una macchina virtuale](../deploy-to-iis/#setting-up-a-virtual-machine).

1. Potrebbe apparire un altro pop-up di sicurezza. Di nuovo, selezionare **Don't ask me again for connections to this computer** e fare clic su **Yes**.

Ottimo lavoro! A questo punto dovremmo avere accesso al desktop del computer remoto con Windows Server 2019 o superiore.

## Esecuzione dello script Bootstrap
Supponendo di aver effettuato l'accesso alla macchina virtuale (usando RDP), seguire la procedura per installare Rhino.Compute dietro IIS. Nota: I passi che seguono presuppongono che si tratti di un'installazione su una nuova macchina virtuale o server (il che significa che Rhino.Compute non è stato installato in precedenza su questa macchina). Se abbiamo configurato Rhino.Compute e IIS su questa macchina e dobbiamo semplicemente aggiornare Rhino e/o Rhino.Compute su questa macchina virtuale, passiamo alla sezione [Aggiornamento di Rhino Compute](../deploy-to-iis/#updating-the-deployment).

### Passo 1

1. Fare clic sul menu di avvio di Windows e digitare "Powershell". Nel menu visualizzato, fare clic con il pulsante destro del mouse sull'applicazione **Windows Powershell** e scegliere **Run As Administrator**.
{{< image url="/images/powershell_1.png" alt="/images/powershell_1.png" class="image_center" width="50%" >}}

1. **Copiare e incollare** il comando sottostante nel prompt di Powershell e premere **Invio**. Questo comando scaricherà l'ultimo script di bootstrap del passo 1 e installerà Rhino e IIS sulla macchina virtuale. Nota: verrà richiesto di inserire **indirizzo e-mail**, **chiave API**e **token di Rhino**, quindi occorre avere queste informazioni a portata di mano.
    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-1')">Rhino 7: Passo 1</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-1')" id="defaultOpen1">Rhino 8: Passo 1</button>
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

1. Al termine del passo 1, la macchina virtuale verrà automaticamente riavviata (si verrà disconnessi da Remote Desktop).

### Passo 2

1. Accedere nuovamente alla macchina virtuale utilizzando Remote Desktop.

1. Aprire una nuova istanza di **Windows Powershell**. Fare clic con il tasto destro sul file e selezionate **Run As Administrator**.

1. **Copiare e incollare** il comando sottostante nel prompt di Powershell e premere **Invio**. Questo comando scaricherà l'ultimo script di bootstrap del passo 2 e configurerà IIS per lavorare con Rhino.Compute.
    <div class="codetab">
      <button class="tablinks2" onclick="openCodeTab(event, 'r7-2')">Rhino 7: Passo 2</button>
      <button class="tablinks2" onclick="openCodeTab(event, 'r8-2')" id="defaultOpen2">Rhino 8: Passo 2</button>
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

1. Al termine dello script di installazione del passo 2, dovrebbe apparire il messaggio *Congratulations!*.* All components have now been installed.* Seguiranno alcune istruzioni su come installare i plug-in di terze parti in modo che funzionino correttamente con Rhino.Compute. Prendere nota dei nuovi **Username** e **Password** che saranno richiesti quando si accederà nuovamente per installare qualsiasi plug-in aggiuntivo.

## Testare l'applicazione

A questo punto, IIS dovrebbe essere configurato per lanciare l'istanza di Rhino.Compute quando viene effettuata una richiesta API. Proviamo a fare in modo che Hops invii una definizione all'URL della nostra macchina virtuale. 

1. Avviare **Rhino** sul computer locale.

1. Se non è stato ancora installato Hops su questa macchina, cercatelo nel **Gestore pacchetti** di Rhino.

1. Avviare **Grasshopper** digitando la parola *Grasshopper* nel prompt dei comandi e premendo Invio.

1. Andare su **File** e **Preferences** per aprire la finestra delle preferenze. 

1. Fare clic sul pannello **Solver** nel menu a sinistra. 

1. Nella sezione **Hops - URL del server di calcolo**, digitare l'indirizzo web della macchina virtuale. Iniziamo digitando `http://` seguito dall'indirizzo IP della macchina virtuale, seguito da `:` e dal numero di porta `80`. Quindi, l'indirizzo completo sarebbe simile a questo:
            
        http://52.168.38.105:80/

1. Nella sezione **API Key**, inserire la chiave API salvata nella sezione [Prerequisiti](../deploy-to-iis/#prerequisites).
{{< image url="/images/Hops_To_IIS_4.png" alt="/images/Hops_To_IIS_4.png" class="image_center" width="80%" >}}

1. Aggiungere un componente **Hops** all’**area di lavoro di Grasshopper** (Params/Util)

1. Fare clic con il pulsante destro del mouse sul componente **Hops** e impostare il **Path** su una definizione Hops/Grasshopper valida. Per informazioni sull'impostazione di una definizione di Grasshopper che funzioni correttamente con Hops, [seguire questa guida](../hops-component/).
{{< image url="/images/Hops_To_IIS_2.png" alt="/images/Hops_To_IIS_2.png" class="image_center" width="50%" >}}

Una volta impostato il percorso, il componente Hops creerà la richiesta API appropriata e la invierà all'URL specificato al punto 6 (il server Rhino.Compute in esecuzione su IIS). Il server di calcolo elabora la richiesta e invia una risposta a Hops che restituisce il risultato.
{{< image url="/images/Hops_To_IIS_3.png" alt="/images/Hops_To_IIS_3.png" class="image_center" width="70%" >}}

Ottimo lavoro! Abbiamo configurato correttamente un'istanza di Rhino.Compute in esecuzione tramite IIS su una macchina virtuale. 

## Modifica dei parametri di calcolo dopo la distribuzione

Esiste una serie di argomenti della linea di comando che possono essere usati per modificare il comportamento di Rhino.Compute. Questa sezione spiega come modificare questi parametri dopo che Rhino.Compute è stato distribuito.

1. Accedere alla macchina virtuale (tramite RDP). Per ulteriori informazioni, consultare la sezione [Collegamento mediante RDP](#connect-via-rdp) .

1. Nel menu **Start**, fare clic nell'area di ricerca e digitare *Internet Information Services (IIS) Manager*. Fare clic per avviare l'applicazione.

1. In IIS Manager, **fare clic** sul nodo del server web, sul pannello **Connections** a sinistra. Nota: il nome del server web deve essere lo stesso utilizzato durante l'impostazione del nome della macchina virtuale. 

1. Nel riquadro **Actions** a destra, fare clic su **Stop** per arrestare il server web.
{{< image url="/images/iis_manager.png" alt="/images/iis_manager.png" class="image_center" width="100%" >}}

Ora che il server web IIS è stato fermato, dobbiamo modificare il file **web.config* di Rhino.Compute. Il file [web.config](https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/web-config?view=aspnetcore-6.0) è un file che viene letto da IIS e dal modulo ASP.NET Core per configurare un sito ospitato da IIS. 

1. Aprire una finestra di **Esplora file** e navigare in *C:\inetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute*. Alla fine di questa directory, si dovrebbe vedere un file chiamato **web.config**. Nota: potrebbe essere necessario fare clic sulla scheda **View** e fare clic sulla casella di controllo per attivare le **file name extensions**. Aprire il file web.config con **Notepad** o qualsiasi altro editor di testo.

L'immagine finale dovrebbe essere simile a questa:

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
La linea che desideriamo modificare è una che inizia con l’etichetta **`<aspNetCore>`**. Possiamo vedere che il secondo parametro su questa linea si chiama **`arguments`**. Questa è la sezione da modificare per aggiungere altri argomenti della linea di comando per modificare Rhino.Compute. 

Di seguito, è riportata una descrizione di ciascun argomento della linea di comando che può essere modificato.

- **port** - Questo è il numero di porta su cui eseguire Rhino.Compute. La porta 80 è tipicamente riservata alla comunicazione HTTP, mentre la porta 443 è utilizzata per il protocollo HTTPS. Nello script di avvio abbiamo impostato Rhino.Compute sulla porta 80, quindi non bisogna modificare questo valore se non sappiamo di cosa si tratta. Esempio di utilizzo: `--port 80`.

- **childcount** - Questo parametro controlla il numero di processi compute.geometry figli da gestire. Il *valore di default è 4*, il che significa che Rhino.Compute creerà quattro processi figli, ognuno dei quali potrà gestire le richieste in arrivo. Esempio di utilizzo: `--childcount 8` indicherebbe a Rhino.Compute di lanciare otto processi figli.

- **childof** - È l'handle del processo genitore. Compute controlla l’esistenza 
di questo handle e si chiuderà una volta terminato il processo. Poiché ci affidiamo all'avvio e all'arresto di Rhino.Compute da parte di IIS, questo parametro non è necessario se si opera in un ambiente di produzione.

- **spawn-on-startup** - Questo flag determina se lanciare un processo figlio compute.geometry quando Rhino.Compute viene avviato. Il *valore di default è falso*. Questo parametro è un flag, il che significa che, se non è incluso nell'elenco degli argomenti, il valore sarà falso. Se si include questo parametro, il valore sarà vero. Per gli ambienti di produzione, questo valore deve rimanere falso.

- **idlespan** - Questo è il numero di secondi in cui un processo figlio di compute.geometry deve rimanere aperto tra le richieste. Il *valore di default è 1 ora*. Quando Rhino.Compute.exe non riceve richieste di risoluzione per un periodo di `idlespan` secondi, i processi figli di compute.geometry.exe si chiudono e smettono di essere fatturati per nucleo ora. In futuro, quando verrà ricevuta una nuova richiesta, i processi figli verranno rilanciati, causando un piccolo ritardo nelle richieste durante il riavvio dei processi figli. Esempio di utilizzo: `--idlespan 1800` indicherebbe a Rhino.Compute di chiudere i processi figli dopo 30 minuti (30 minuti x 60 secondi = 1800).

    Se modifichiamo il valore `idelspan` negli argomenti della linea di comando di Rhino.Compute, occorre modificare anche la configurazione di IIS. Questo perché IIS contiene anche un'impostazione che spegne Rhino.Compute se non vengono ricevute nuove richieste dopo un certo periodo di tempo. Quando Rhino.Compute viene chiuso, chiuderanno a sua volta tutti i processi figli. 

    Ad esempio, supponiamo di modificare il valore `idlespan` a 7.200 (2 ore). Lo script di bootstrap imposta il valore `IdleTimeout` di IIS a 65 minuti (leggermente più lungo del valore `idlespan` predefinito). Dopo 65 minuti, IIS chiudeva Rhino.Compute, che a sua volta chiudeva tutti i suoi processi figli molto prima del limite previsto di 2 ore. Pertanto, se si modifica il valore `idlespan`, si consiglia di modificare anche il valore `IdleTimeout` nelle impostazioni di IIS.

    1. Per farlo, aprire IIS Manager e fare clic sulla voce **Application Pools** in **Connections** a sinistra. 
    
    1. Nella finestra centrale fare clic su **RhinoComputeAppPool**.

    1. Sul pannello **Actions** a destra, fare clic su **Advanced Settings**.

    1. Individuare la riga **Idle Time-out** nella sezione **Process Model** e modificare il valore del time out in modo che sia leggermente più lungo del valore `idlespan` impostato negli argomenti della linea di comando. Nota: il valore `idlespan` è espresso in secondi, mentre il valore `Idle Timeout` è espresso in minuti.
    {{< image url="/images/iis_idletimout.png" alt="/images/iis_idletimout.png" class="image_center" width="60%" >}}

Una volta modificato il file web.config, **salvare** e chiudere il file. È quindi possibile tornare a IIS Manager e **avviare** il server web facendo clic sul nodo del server web nel pannello **Connections** a sinistra e facendo clic su **Start** nel pannello **Actions** a destra.

## Aggiornamento del deployment
Se hai già configurato Rhino.Compute su questa macchina, potrebbe essere necessario aggiornare periodicamente Rhino e/o i file di build di Rhino.Compute alla versione più recente. Per aggiornare queste applicazioni, procedere come segue.

### Aggiornamento di Rhino

1. Fare clic sul menu di avvio di Windows e digitare "Powershell". Nel menu visualizzato, fare clic con il pulsante destro del mouse sull'applicazione **Windows Powershell** e scegliere **Run As Administrator**.

1. **Copiare e incollare** il comando sottostante nel prompt di Powershell e premere **Invio**. Questo comando scaricherà l'ultima versione di Rhino per Windows. Nota: verrà richiesto di inserire l’**indirizzo e-mail**, quindi consigliamo di tenerlo a portata di mano.

    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-3')">Update to Latest Rhino 7 Install</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-3')" id="defaultOpen3">Update to Latest Rhino 8 Install</button>
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

### Aggiornamento di Compute

1. Fare clic sul menu di avvio di Windows e digitare "Powershell". Nel menu visualizzato, fare clic con il pulsante destro del mouse sull'applicazione **Windows Powershell** e scegliere **Run As Administrator**.

1. **Copiare e incollare** il comando sottostante nel prompt di Powershell e premere **Invio**. Questo comando scaricherà l'ultima versione di Rhino.Compute.

    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-4')">Update Rhino.Compute for Rhino 7</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-4')" id="defaultOpen4">Update Rhino.Compute for Rhino 8</button>
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

 
## Collegamenti rapidi

 - [Che cos'è Hops](../what-is-hops)
 - [Come funziona Hops](../how-hops-works)
 - [Il componente Hops](../hops-component)

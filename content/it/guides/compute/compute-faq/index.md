+++
aliases = ["/en/5/guides/compute/compute-faq/", "/en/6/guides/compute/compute-faq/", "/en/7/guides/compute/compute-faq/", "/en/wip/guides/compute/compute-faq/", "/en/guides/compute/faq/"]
authors = [ "andy.payne" ]
categories = [ "Getting Started" ]
description = "Questa guida include un elenco di domande frequenti (FAQ) per Rhino.Compute."
keywords = [ "developer", "compute", "faq" ]
languages = []
sdk = [ "Compute" ]
title = "Domande frequenti (FAQ)"
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

## Generali

### Che cos'è Rhino.Compute?

Nella sua definizione più semplice, Rhino.Compute è un server web che può eseguire calcoli geometrici usando la libreria geometrica di Rhino (cioè [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/)). Rhino.Compute funziona ricevendo le richieste via web (usando [HTTP](https://en.wikipedia.org/wiki/HTTP) o [HTTPS](https://en.wikipedia.org/wiki/HTTPS)), elaborandole con il motore geometrico di Rhino e quindi inviando i risultati. Qualsiasi applicazione in grado di inviare richieste web può interagire con Rhino.Compute, semplificandone l'integrazione in diversi flussi di lavoro.

### Perché dovrei volerlo usare?

Rhino.Compute consente di utilizzare i potenti strumenti e le funzioni di Rhino al di fuori della normale interfaccia di Rhino o Grasshopper. È ottimo per i team, perché è possibile eseguire le definizioni di Grasshopper o le funzioni di Rhino da un unico punto centrale, facilitando la collaborazione. Può anche gestire più attività contemporaneamente (in parallelo), contribuendo a velocizzare i progetti di grandi dimensioni. E per i calcoli più lunghi, viene eseguito in background (in modo asincrono), in modo da non bloccare o rallentare l'interfaccia principale.

### Funzionerà su macOS?

No. Rhino.Compute dipende da [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/) che permette a Rhino e Grasshopper di funzionare *all'interno* di altre applicazioni a 64 bit. Attualmente, Rhino.Inside è compatibile solo con il sistema operativo Windows.

### Quanto costa?

La risposta breve è: dipende da *dove* si esegue Rhino.Compute. Se viene utilizzato su un normale computer Windows, come un PC personale, non ci sono costi aggiuntivi. Rhino.Compute controllerà la licenza standard di Rhino all'avvio (nota: [le versioni di valutazione di Rhino](https://www.rhino3d.com/download/) funzionano benissimo). Ma se viene eseguito su un server Windows (ad esempio una macchina virtuale cloud), verrà addebitato il costo in base al modello di [fatturazione ore per nucleo](../core-hour-billing/).

### In cosa si differenzia dal Hops?

[Hops](../what-is-hops/) è un plug-in di Grasshopper (disponibile nel [gestore pacchetti](../../yak/what-is-yak/)) che facilita la risoluzione delle definizioni di Grasshopper usando Rhino.Compute. Quando si installa Hops, questo avvia automaticamente un'istanza di Rhino.Compute in background ogni volta che si apre Grasshopper. È quindi possibile utilizzare il componente Hops per inviare la definizione di Grasshopper a Rhino.Compute, che la risolve e invia i risultati. In questo contesto, Hops è il “client” e Rhino.Compute è il “server.”

### Posso creare un’interfaccia personalizzata per lavorare con Rhino.Compute?

Sì. Come già detto, qualsiasi applicazione in grado di inviare richieste web può lavorare con Rhino.Compute. Per semplificare le cose, offriamo tre librerie da utilizzare a seconda della lingua desiderata:
1. [Libreria Python Rhino.Compute.](https://pypi.org/project/compute-rhino3d/)
1. [Libreria Javascript Rhino.Compute.](https://www.npmjs.com/package/compute-rhino3d)
1. [Libreria .NET (C#) Rhino.Compute.](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs)

Abbiamo anche delle guide passo-passo per iniziare ad utilizzare le librerie menzionate in precedenza:
1. [Chiamare Compute con Python.](../compute-python-getting-started/)
1. [Chiamare Compute con Javascript.](../compute-javascript-getting-started/)
1. [Chiamare Compute con .NET.](../compute-net-getting-started/)

Infine, abbiamo un [repository GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute) con molti progetti campione ed esempi che mostrano come usare Rhino.Compute per diverse operazioni di geometria.

### Posso usare Rhino.Compute in un ambiente di produzione?

Sì. Offriamo una [guida passo-passo](../deploy-to-iis/) per aiutare a configurare Rhino.Compute in un ambiente di produzione, ad esempio su una macchina virtuale (VM). La configurazione è semplice: basta eseguire un semplice script PowerShell e Rhino.Compute sarà attivo e funzionante, pronto a gestire le richieste.

## Risoluzione dei problemi

Abbiamo lavorato duramente per rendere Rhino.Compute il più semplice possibile da usare. Ma, a volte, le cose non vanno come previsto. Questa sezione è stata creata per aiutare a risolvere possibili problemi.

### Dove trovo i file di registro?

Per eseguire Rhino.Compute con Hops, occorre assicurarsi che l'applicazione console di Rhino.Compute sia visibile all'avvio. Per modificare questa modalità, procedere come segue:
1. Avviare Grasshopper.
1. Fare clic su **File -> Preferences** per aprire la finestra di dialogo delle impostazioni di Grasshopper.
1. Fare clic sul pannello **Solver** nel menu a sinistra.
1. **Deselezionare** l’opzione del menu Hide Rhino.Compute Console Window.
1. Riavviare Rhino e Grasshopper. 

{{< image url="/images/hops-preferences-1.png" alt="/images/hops-preferences-1.png" class="image_center" width="75%" >}}

A questo punto, quando si avvia Grasshopper, dovrebbe apparire una nuova applicazione nella barra delle applicazioni (se si utilizza Windows). Questa è l'applicazione console di Rhino.Compute. Qui vengono visualizzate le informazioni utili per la risoluzione dei problemi mentre si lavora con Rhino.Compute.

{{< image url="/images/hops-console-2.png" alt="/images/hops-console-2.png" class="image_center" width="100%" >}}

<br>
Se Rhino.Compute è in esecuzione su una macchina virtuale VM, i file di registro vengono salvati come file di testo. Ogni giorno vengono creati nuovi file di registro. Di default, i file di registro vengono salvati nella seguente posizione: 

```cs
C:\inetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute\logs\
```

### È possibile abilitare le informazioni di registro verbose?

Di dafault, Rhino.Compute invia ai registri una serie minima di informazioni. Per abilitare una registrazione più verbosa è necessario creare una variabile d'ambiente sulla macchina.

1. Fare clic con il tasto destro del mouse sull'icona **Questo PC** in Esplora file, quindi selezionare **Proprietà** o **Sistema** dal Pannello di controllo.
1. Nella finestra Proprietà del sistema, fare clic su **Impostazioni di sistema avanzate**.
1. Nella scheda **Opzioni avanzate** , fare clic su **Variabili di ambiente**.
1. Fare clic sul pulsante **Nuova** per creare una nuova variabile di sistema.
1. Nell'immissione **Nome variabile**, digitare "RHINO_COMPUTE_DEBUG".
1. Nell'input **Valore variabile**, digitare "true".
1. Fare clic su OK per salvare la variabile d'ambiente del sistema, quindi fare nuovamente clic su OK per chiudere la finestra di dialogo Variabili d'ambiente e la finestra Proprietà del sistema.

### Cosa fare se si ottiene un errore HRESULT E_FAIL?

Se Rhino.Compute restituisce il seguente errore:

```cs
Application startup exception
System.Runtime.InteropServices.COMException (0x80004005): Error HRESULT E_FAIL has been returned from a call to a COM component.
   at Rhino.Runtime.InProcess.RhinoCore.InternalStartup(Int32 argc, String[] argv, StartupInfo& info, IntPtr hostWnd)
```

Il problema è probabilmente dovuto al fatto che Rhino.Compute non riesce a trovare una licenza valida all'avvio. Se si utilizza un computer basato su Windows Server (cioè su una macchina virtuale), seguire i seguenti passaggi:

1. Accedere al [Portale Licenze](https://www.rhino3d.com/licenses?_forceEmpty=true) e selezionare il team che è stato impostato con la fatturazione nucleo per ora.
1. Fare clic su **Gestione team -> Gestione fatturazione nucleo per ora**.
1. Fare clic su **Azione -> Ottieni token di autenticazione** per ottenere un token.
1. Creare una nuova variabile d'ambiente con il nome `RHINO_TOKEN` e utilizzare il token come valore. Poiché il token è troppo lungo per la finestra di dialogo delle variabili d'ambiente di Windows, è più facile farlo tramite un comando PowerShell.

```ps
[System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'your token here', 'Machine')
```

D'ora in poi, quando si avvia Rhino su questo computer, si utilizzerà il team di fatturazione nucleo per ora.

{{< call-out "warning" "Avviso" >}}
<strong>Avviso</strong> Il token per la fatturazione nucleo per ora consente a chiunque ne sia in possesso di addebitare spese al team. <strong>NON</strong> condividere questo token con nessuno.
{{< /call-out >}}

### Ho ricevuto il messaggio di errore 401. Cosa significa?

Se Rhino.Compute restituisce l’errore 401, significa che la richiesta non è stata autorizzata. Questo accade di solito quando alla richiesta manca una chiave API. Rhino.Compute controlla questa chiave, che viene salvata come variabile d'ambiente sulla macchina su cui è in esecuzione, per assicurarsi che solo i client approvati possano connettersi.

Se si utilizza Hops, è possibile impostare la chiave API nella sezione delle preferenze.

1. Avvia Grasshopper
1. Fare clic su **File -> Preference** per aprire la finestra di dialogo delle impostazioni di Grasshopper.
1. Fare clic sul pannello **Solver** nel menu a sinistra.
1. **Inserire la chiave API** nella finestra di dialogo di immissione.
1. Riavviare Rhino e Grasshopper.

{{< image url="/images/hops-api-key.png" alt="/images/hops-api-key.png" class="image_center" width="75%" >}}

<br>
Per inviare una richiesta web a Rhino.Compute usando un metodo diverso, occorre assicurarsi di includere una coppia chiave/valore nell'intestazione della richiesta. La chiave deve essere chiamata "RhinoComputeKey" e il suo valore deve corrispondere alla chiave API impostata sulla macchina che esegue Rhino.Compute.

### Cosa significa il codice di errore 500?

La risposta di Rhino.Compute contenente un codice di errore 500 significa che il server non funziona correttamente e non è in grado di elaborare la richiesta. In questo caso, potrebbe essere necessario provare ad eseguire Rhino.Compute in modalità di debug per ottenere ulteriori informazioni sull’errore del server. [Seguire questa guida](../development/) per imparare ad eseguire Rhino.Compute in modalità di debug.

### Cosa devo fare se ricevo un'eccezione di timeout?

Se Rhino.Compute restituisce il seguente errore:

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Connection id "...", Request id "...": An unhandled exception was thrown by the application.
      System.Threading.Tasks.TaskCanceledException: The request was canceled due to the configured HttpClient.Timeout of 100 seconds elapsing.
```

Il timeout di una richiesta HTTP si verifica quando un client (come Hops) non riceve una risposta da un server (come Rhino.Compute) entro un determinato periodo di tempo. Esistono quindi due valori di timeout di cui è bene tenere conto: 1) il timeout del client e 2) il timeout del server.

L'impostazione del timeout visualizzata nelle preferenze Hops controlla il timeout del lato client. Il valore predefinito è di 100 secondi, ma può essere esteso per ovviare a  questo errore.

{{< image url="/images/hops-timeout.png" alt="/images/hops-timeout.png" class="image_center" width="75%" >}}

Il timeout lato server è gestito separatamente: è impostato da una variabile d'ambiente sulla macchina che esegue il server. Per impostare la variabile d'ambiente, procedere come segue:

1. Fare clic con il tasto destro del mouse sull'icona **Questo PC** in Esplora file, quindi selezionare **Proprietà** o **Sistema** dal Pannello di controllo.
1. Nella finestra Proprietà del sistema, fare clic su **Impostazioni di sistema avanzate**.
1. Nella scheda **Opzioni avanzate**, fare clic su **Variabili di ambiente**.
1. Fare clic sul pulsante **Nuova** per creare una nuova variabile di sistema.
1. In **Nome variabile**, digitare "RHINO_COMPUTE_TIMEOUT".
1. In **Valore variabile**, digitare il **numero di secondi** da usare come valore di timeout lato server
1. Fare clic su OK per salvare la variabile d'ambiente del sistema, quindi fare nuovamente clic su OK per chiudere la finestra di dialogo Variabili d'ambiente e la finestra Proprietà del sistema.

### Ricevo un errore che indica che il corpo della richiesta è troppo grande. Cosa faccio?

Se Rhino.Compute restituisce il seguente errore:

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Connection id "...", Request id "...": An unhandled exception was thrown by the application.
      Microsoft.AspNetCore.Server.Kestrel.Core.BadHttpRequestException: Request body too large.
```

Questo errore può verificarsi se si sta cercando di inviare una grande quantità di dati a Rhino.Compute nel corpo di una richiesta. Il limite predefinito per le dimensioni di una richiesta è di circa 50 mb. Per aumentare questo limite, procedere come segue:

1. Fare clic con il tasto destro del mouse sull'icona **Questo PC** in Esplora file, quindi selezionare **Proprietà** o **Sistema** dal Pannello di controllo.
1. Nella finestra Proprietà del sistema, fare clic su **Impostazioni di sistema avanzate**.
1. Nella scheda **Opzioni avanzate**, fare clic su **Variabili di ambiente**.
1. Fare clic sul pulsante **Nuova** per creare una nuova variabile di sistema.
1. In **Nome variabile**, digitare "RHINO_COMPUTE_MAX_REQUEST_SIZE".
1. In **Valore variabile**, digitare il **numero massimo di byte** consentito in un corpo di richiesta HTTP. Il valore predefinito è 52.428.800 byte (circa 50 mb). Aumentare questo valore per consentire richieste più grandi.
1. Fare clic su OK per salvare la variabile d'ambiente del sistema, quindi fare nuovamente clic su OK per chiudere la finestra di dialogo Variabili d'ambiente e la finestra Proprietà del sistema.

<br><br>
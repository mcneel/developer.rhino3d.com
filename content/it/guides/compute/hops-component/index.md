+++
aliases = ["/en/5/guides/compute/hops-component/", "/en/6/guides/compute/hops-component/", "/en/7/guides/compute/hops-component/", "/en/wip/guides/compute/hops-component/"]
authors = [ "steve", "scottd", "andy.payne" ]
categories = [ "Hops" ]
description = "Hops aggiunge funzioni a Grasshopper."
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "Il componente Hops"
type = "guides"
weight = 3
override_last_modified = "2024-10-28T11:35:10Z"

[admin]
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

## Panoramica 


{{< image url="/images/hops-overview.png" alt="/images/hops-overview.png" class="image_center" width="100%" >}}

Hops è un componente per Grasshopper in Rhino 7 e Rhino 8 per Windows. Hops aggiunge **funzioni** esterne a Grasshopper. Come altri linguaggi di programmazione, le funzioni consentono di:

* Semplificare algoritmi complessi utilizzando più volte la stessa funzione.
* Eliminare le combinazioni di componenti duplicate inserendo le combinazioni comuni in una funzione.
* Condividere i documenti di Grasshopper con gli altri membri del team.
* Referenziare documenti di Grasshopper su più progetti.
* Risolvere documenti esterni in parallelo, accelerando potenzialmente i progetti di grandi dimensioni.
* Eseguire in modo asincrono calcoli di lunga durata senza bloccare le interazioni con Rhino e Grasshopper.

Le funzioni di Hops vengono memorizzate come documenti di Grasshopper separati. Il componente Hops adatta i propri input e output alla funzione specificata. Durante il calcolo Hops risolve la definizione in un processo separato, quindi restituisce i risultati al documento corrente.

## Come usare le Hops <img src="/images/hops.svg" alt="Windows" class="guide_icon">

{{< vimeo 713836707 >}}

### Installare Hops:

Esistono alcuni modi per installare Hops sul computer.
  1. [Install Hops](rhino://package/search?name=hops) (questa opzione aprirà Rhino).
  1. Oppure, digitate `PackageManager` sulla linea di comando di Rhino.
      1. Quindi, cercare "Hops".
      1. Selezionare Hops e fare clic su Install.

{{< image url="/images/hops-package-manager.png" alt="/images/hops-package-manager.png" class="image_center" width="100%" >}}

### Creare una funzione di Hops

Le funzioni di Hops sono documenti di Grasshopper con input e output speciali.

{{< image url="/images/hops_simple_function.png" alt="/images/hops_simple_function.png" class="image_center" width="100%" >}}

#### Definizione degli input

Gli input di Hops vengono creati utilizzando il comando **Get Components**. I componenti Get disponibili in Grasshopper si trovano in *Params Tab > Util Group*:

{{< image url="/images/hops_context_getters1.png" alt="/images/hops_context_getters1.png" class="image_center" width="65%" >}}

Il nome del componente viene utilizzato per il nome del parametro di input di Hops. Quindi, nell'esempio precedente, abbiamo tre componenti Get Number con i nomi A, B e C. Ciascuno di questi componenti Get diventa un parametro di input quando Hops compila la definizione.

{{< image url="/images/hops_getter_inputs.png" alt="/images/hops_getter_inputs.png" class="image_center" width="80%" >}}

Ogni componente Get presenta un menu contestuale (clic destro) con varie impostazioni.

{{< image url="/images/hops-get-component-menu.png" alt="/images/hops-get-component-menu.png" class="image_center" width="50%" >}}

* **Component Name** - Questo è il nome che verrà assegnato all'input del componente Hops.
* **Prompt** - Questo input sarà il tooltip visualizzato quando si passa il mouse su questo parametro nel componente Hops.
* **Enable/Disable** - Abilita o disabilita questo componente.
* **At least** - Questo parametro viene utilizzato solo per il lettore Grasshopper e definisce il numero minimo di valori da accettare per questo input.
* **At most** - Definisce il numero massimo di valori da accettare per questo input (Default = 1). Se questo valore è impostato su 1, il componente Hops tratterà questo input come *Item Access*. Tuttavia, se questo valore è più di uno (o non impostato) Hops tratterà questo input come *List Access*.
* **Tree Access** - Questa opzione definisce se si prevede di passare un albero dati nell’input. Questo input è usato solo in Hops e se è impostato su True, questo valore sostituisce il valore *At Most* impostato sopra.
* **Minimum & Maximum** - Questi input facoltativi vengono utilizzati solo per Grasshopper Player e vincolano gli input numerici a questi limiti.
* **Preset** - Questo input facoltativo è usato solo per Grasshopper Player e si trova solo nei componenti Get *String*, *Integer*e *Number*. Questa finestra di dialogo consente di impostare un elenco di opzioni predefinite che verranno visualizzate dall'utente tramite il prompt della linea di comando.

#### Definizione degli input

Gli output di Hops possono essere definiti utilizzando i componenti **Context Bake** o **Context Print**. Il nome del parametro di input in uno dei componenti Context sarà usato come nome del parametro di output quando viene calcolato Hops.

{{< image url="/images/hops_getter_outputs.png" alt="/images/hops_getter_outputs.png" class="image_center" width="67%" >}}

### Utilizzo del componente Hops

1. Posizionare il componente Grasshopper *Params Tab > Util Group > Hops component* sull'area di disegno.
1. Fare clic con il pulsante destro del mouse sul componente Hops, quindi fare clic su Path.
1. Selezionare una funzione di Hops. Nota: questa può essere una definizione di Grasshopper sul proprio computer, su un computer remoto o un endpoint REST.
1. Il componente mostrerà gli input e gli output.
1. Utilizzare il nuovo componente come qualsiasi altro componente di Grasshopper.

{{< image url="/images/hops_multiplyadd.png" alt="/images/hops_multiplyadd.png" class="image_center" width="80%" >}}

### Nota su Hops per gli utenti di macOS

Il componente Hops lavora in tandem con un'istanza locale di un server [Rhino.compute](https://developer.rhino3d.com/guides/compute/) che, in genere, viene avviato ogni volta che si apre Grasshopper. Tuttavia, questo server non funziona su macOS, il che significa occorre considerare altre due opzioni. È possibile:

1. Effettuare una chiamata API REST a un server remoto in esecuzione su Windows.
1. Effettuare una chiamata API REST a un server python ghhops_server in esecuzione localmente.

La prima opzione (chiamata a un server Windows remoto) richiede alcune modifiche di configurazione al computer remoto. Per ulteriori informazioni su come configurare un server remoto, consultare la sezione [Configurazione della macchina remota](../hops-component/#remote-machine-configuration).

La seconda opzione (chiamata a un server python locale) è trattata in modo più dettagliato nella sezione [Chiamare un server CPython](../hops-component/#calling-a-cpython-server).

## Impostazioni di Hops

### Impostazioni dell'applicazione

Le impostazioni di Hops controllano il funzionamento di Hops a livello di applicazione.  È disponibile attraverso il menu a comparsa Grasshopper File > Preferences > Solver.

{{< image url="/images/hops-preferences.png" alt="/images/hops-preferences.png" class="image_center" width="60%" >}}

* **Hops-Compute server URL** - Elenca l'indirizzo IP o l'URL di qualsiasi macchina o server Compute remoto.
* **API Key** - La chiave API è una stringa di testo segreta per il server di calcolo e per le applicazioni che utilizzano l'API di calcolo, ad esempio `b8f91f04-3782-4f1c-87ac-8682f865bf1b`. È facoltativo se si effettua un test locale, ma dovrebbe essere usato in ambiente di produzione. In pratica, è il modo in cui il server di calcolo si assicura che le chiamate API provengano solo dalle tue applicazioni. È possibile inserire qualsiasi stringa che sia unica e segreta per l'utente e per le app di calcolo. Assicurati di conservarlo in un luogo sicuro.
* **Max Concurrent requests** - Utilizzato per limitare il numero di richieste attive in situazioni asincrone. In questo modo, Hops non effettua migliaia di richieste mentre la richiesta originale viene elaborata.
* **Clear Hops Memory cache** - Cancella dalla memoria tutte le soluzioni precedentemente memorizzate.
* **Hide Rhino.Compute Console Window** - Hops verrà eseguito in background, ma mostrare la finestra può essere utile per la risoluzione dei problemi.
* **Launch Local Rhino.Compute at Start** - Utilizzare questa opzione per le macchine remote quando Compute deve avviarsi prima che vengano inviate le richieste.
* **Child Process Count** - Questa opzione viene utilizzata per limitare il numero di richieste di processi paralleli aggiuntivi. Si consiglia di impostare questo valore sul numero di core disponibili.
* **Function Sources** - Questa sezione consente di aggiungere un percorso (a una directory locale o a un URL) alle funzioni di Hops utilizzate di frequente (ad esempio  definizioni di Grasshopper).

{{< call-out "note" "Nota" >}}
Dalla versione 7.13 di Rhino, le tolleranze attive del modello (cioè le tolleranze assolute di distanza e angolo) vengono passate da Hops all'istanza in esecuzione di Rhino.compute come parte della richiesta JSON.
{{< /call-out >}}

### Impostazioni dei componenti

Fare clic con il tasto destro del mouse sul componente Hops per selezionare una serie di opzioni che controllano il funzionamento di Hops.

{{< image url="/images/gh-hops-component-settings.png" alt="/images/gh-hops-component-settings.png" class="image_center" width="60%" >}}

* **Parallel Computing** - Passa ogni elemento a un nuovo nodo parallelo, se disponibile.
* **Path...** - Aggiunge il percorso della funzione GH da risolvere. Può trattarsi di un nome di file, di un indirizzo IP o di un URL.
* **Mostrare l’input: Path** - Rende il percorso un input del componente, in modo che il percorso possa essere impostato tramite l’area di lavoro di GH.
* **Mostrare l’input: Enabled** - Mostra un input abilitato che esegue il componente in base a un valore booleano `True` o `False`.
* **Asynchronous** - L'interfaccia utente non verrà bloccata in attesa della risoluzione di un processo remoto e la definizione verrà aggiornata al termine della risoluzione.
* **Cache In Memory** - Le soluzioni precedenti vengono memorizzate sul computer locale per migliorare le prestazioni se gli stessi input sono stati calcolati in precedenza.
* **Cache On Server** - Le soluzioni precedenti vengono memorizzate sul server remoto per migliorare le prestazioni. Attualmente, è disponibile solo per i servizi Remote Hops.

## Configurazione della macchina remota

Di default, Hops utilizza il computer locale per risolvere le funzioni di Grasshopper. Tuttavia, è possibile impostare computer remoti (ad esempio server) o macchine virtuali da chiamare con Hops.

Per effettuare chiamate API a un computer remoto, seguire questa [guida alla configurazione di un ambiente di produzione](../deploy-to-iis/).

## Chiamare un server CPython

Usare Hops per chiamare CPython. Alcuni vantaggi di questo componente:

1. Chiamata delle librerie CPython, tra cui Numpy e SciPy.
1. Utilizzare alcune delle più recenti librerie disponibili per CPython, come TensorFlow.
1. Creare funzioni riutilizzabili ed elaborazione parallela.
1. Supporta modalità di debug reali, compresi i punti di interruzione.
1. Supporto completo di Visual Studio Code.
1. Anche altre applicazioni e servizi che supportano un'API Python possono utilizzare le librerie qui incluse.
1. Il componente Hops cerca di rilevare quando gli input e gli output cambiano su un server e si compila da solo.  

### Iniziare a usare CPython in Grasshopper

Il modulo Python aiuta a creare funzioni Python (in particolare CPython) e a utilizzarle all'interno di script di Grasshopper utilizzando i nuovi componenti Hops.

**Requisiti:**

1. [Rhino 7.4 o versione successiva.](https://www.rhino3d.com/download/)
1. [CPython 3.8 o superiore.](https://www.python.org/downloads/)
1. [Componente Hops per Grasshopper.](https://developer.rhino3d.com/guides/grasshopper/hops-component/)
1. [Visual Studio Code](https://code.visualstudio.com/) consigliato.

**Tutorial video:**

{{< vimeo 524032610 >}}

Questo modulo può usare il server HTTP predefinito per servire le funzioni come componenti di Grasshopper o agire come middleware per un'applicazione [Flask](https://flask.palletsprojects.com/en/1.1.x/). Può anche lavorare insieme a [Rhino.Inside.CPython](https://discourse.mcneel.com/t/rhino-inside-python/78987) per dare pieno accesso all'API [RhinoCommon](https://developer.rhino3d.com/api/).

## FAQ - Domande Frequenti:

#### È possibile annidare le funzioni di Hops all'interno di altre funzioni?

Sì, è possibile annidare la funzione di Hops all'interno di altre funzioni. Questa operazione è chiamata _recursion_ e il limite di ricorsione predefinito è impostato su 10.

#### L'utilizzo di Hops prevede un costo?

L'utilizzo di Hops è gratuito.

#### È possibile utilizzare Hops con Grasshopper Player per creare comandi?

Sì, le funzioni di Hops possono usare i componenti Context Bake e Context Print per creare comandi Rhino in Grasshopper Player.

#### Hops supporta l'elaborazione parallela?

Sì, di default Hops avvia un processo parallelo per ogni ramo di un flusso di input di un albero di dati.

#### Quali tipi di input e output supporta Hops? Supporta tutti i tipi più comuni ed è possibile richiederne altri, se necessario.

Hops passa i tipi di dati standard di Grasshopper (stringhe, numeri, linee, ecc.). Per altri tipi di dati, come immagini o file meteo EPW, utilizzare una stringa per il nome del file, in modo che la funzione esterna possa leggere lo stesso file.

#### I componenti dei plug-in possono essere eseguiti nelle funzioni di Hops?

Sì, tutti i plug-in di Grasshopper installati possono essere eseguiti all'interno di una funzione di Hops.

#### Può essere utilizzato per calcoli estremamente lunghi all'interno di una funzione?

Sì, ogni componente Hops ha un'opzione per risolvere in modo asincrono. L'interfaccia utente non verrà bloccata in attesa della risoluzione di un processo remoto e la definizione verrà aggiornata al termine della risoluzione. Hops attende il ritorno di tutte le chiamate di funzione prima di passare gli output ai componenti downstream.
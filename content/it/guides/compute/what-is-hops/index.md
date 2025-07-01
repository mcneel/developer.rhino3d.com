+++
aliases = ["/en/5/guides/compute/what-is-hops/", "/en/6/guides/compute/what-is-hops/", "/en/7/guides/compute/what-is-hops/", "/en/wip/guides/compute/what-is-hops/"]
authors = [ "andy.payne" ]
categories = [ "Hops" ]
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "Che cos'è Hops?"
type = "guides"
weight = 1
override_last_modified = "2022-03-21T17:57:18Z"

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

Hops consente di semplificare definizioni complesse di grandi dimensioni. Le definizioni di Grasshopper possono essere lunghe, complicate e ripetitive. Questo stato di disorganizzazione viene talvolta chiamato [Codice Spaghetti](https://www.pcmag.com/encyclopedia/term/spaghetti-code). Molti fattori contribuiscono a creare codice spaghetti, tra cui: vincoli di tempo, livello di competenza dei programmatori, complessità del progetto e limitazioni del linguaggio di programmazione. Dopo aver cercato di decifrare una grossa palla di spaghetti di Grasshopper, è emersa una verità universale: il codice spaghetti è difficile da leggere e da capire. **Ora è possibile utilizzare Hops per semplificare il codice spaghetti di difficile lettura.**

{{< image url="/images/hops_spaghetti_code_1.png" alt="/images/hops_spaghetti_code_1.png" class="image_center" width="100%" >}}

### Chiamare funzioni logiche di Grasshopper

In programmazione, una **funzione** è un modulo di codice "autonomo" che elabora gli input e restituisce un risultato. Anche le definizioni di Grasshopper elaborano gli input e restituiscono i risultati. Tuttavia, Grasshopper non è stato scritto pensando alle funzioni. I cluster funzionano, ma non facilitano il riutilizzo di definizioni semplici in progetti complessi.

Per risolvere questo problema, è stato aggiunto il componente Hops. Hops consente di utilizzare definizioni di Grasshopper separate come funzioni. La chiave è imparare a scomporre un problema in sotto-definizioni più piccole che utilizzeremo come funzioni.

Immaginiamo di dover eseguire un'analisi delle ombre per una torre parametrica progettata per New York. Questo problema potrebbe essere suddiviso in quattro compiti più piccoli:
1. Creare il contorno del lotto di costruzione.
1. Creare l'involucro edilizio.
1. Creare le piastre del pavimento.
1. Eseguire l'analisi dell'ombra dall'involucro edilizio e dagli edifici circostanti.

Una volta definiti chiaramente i compiti, è possibile determinare quali informazioni saranno necessarie per eseguire ciascuna operazione (cioè gli input) e quali dati saranno restituiti alla fine (cioè gli output). Per la fase 1, gli input necessari per creare la sagoma del lotto edificabile includono le arretratezze del sito e altri parametri normativi tratti dai codici edilizi e di zonizzazione. L'output di questa funzione includerà probabilmente una polilinea che delinea l'area massima dell'edificio al piano terra. 

Per definire i parametri che verranno utilizzati in una funzione di Grasshopper, utilizzare i componenti **Context Get** per gli input e il componente **Context Bake** per gli output. Ognuno di essi si trova nella scheda *Params > Util Group*.

{{< image url="/images/hops_context_getters.png" alt="/images/hops_context_getters.png" class="image_center" width="92%" >}}

Ora che abbiamo definito input e output, non resta che compilare i passaggi per trasformare gli input in output. Dopo che una funzione è stata completamente definita come definizione di Grasshopper, può essere chiamata da Hops. Hops espone gli input le gli output definiti all'interno della funzione nella definizione contenente. A differenza dei cluster, Hops consente di fare riferimento a file esterni che possono essere salvati localmente o su un'unità di rete, facilitando la condivisione delle definizioni tra i membri del team e i collaboratori.

Hops consente di aumentare la leggibilità del codice semplificando le definizioni complesse, riducendo le duplicazioni e condividendo e riutilizzando le funzioni. Hops consente di risolvere le funzioni in parallelo, accelerando potenzialmente i progetti di grandi dimensioni. Inoltre, consente di risolvere le funzioni in modo asincrono, senza bloccare le interazioni tra Rhino e Grasshopper.

## Come funziona

Dietro le quinte, il client Hops passa la definizione di Grasshopper specificata a un'istanza headless di Rhino e al server Grasshopper.  

### Il client Hops

Un client è un dispositivo hardware (ad esempio, un computer) o un'applicazione software che richiede una risorsa digitale a un server tramite una connessione di rete. 

Il componente Hops è il client. Si trova in *Params > Util Group* dopo aver installato Hops tramite il gestore di pacchetti. Hops ha bisogno del percorso o dell'URL della definizione che sta per risolvere.
{{< image url="/images/hops_hello_world4.png" alt="/images/hops_hello_world4.png" class="image_center" width="55%" >}} 

Una volta specificata la definizione, il componente si aggiorna per mostrare gli input e gli output definiti nella definizione.
{{< image url="/images/hops_io.png" alt="/images/hops_io.png" class="image_center" width="30%" >}} 

### Il server di Rhino

Un server fornisce i dati ai propri client attraverso una connessione di rete. 

Nel contesto di Hops, il server è una versione headless, cioè priva di interfaccia utente con cui interagire, di Rhino e Grasshopper. Il server headless di Rhino risolve la definizione di Grasshopper inviata da Hops e poi restituisce il risultato.
{{< image url="/images/hops_console.png" alt="/images/hops_console.png" class="image_center" width="100%" >}}

Hops consente di puntare a un server Rhino.Compute in esecuzione su un altro computer per risolvere le definizioni di Grasshopper. Ciò consente di scaricare parzialmente o interamente la risoluzione a una risorsa di calcolo esterna.

## Introduzione

Per creare una funzione che possa essere referenziata da Hops, dobbiamo dividere la nostra definizione in tre sezioni distinte: una per definire i parametri di ingresso, un'altra per specificare gli output e infine una sezione che esegue le *azioni* della funzione. Per iniziare a lavorare con Hops, è possibile seguire il video o i passaggi elencati di seguito.

{{< vimeo 713836707 >}}

<br><br>
In questo esempio, si vuole creare una semplice funzione che prenda in input il nome di un utente (ad esempio, David) e restituisca un messaggio del tipo *"Ciao David!"*.

### Installare Hops

Prima di iniziare, assicuriamoci che Hops sia installato correttamente. Esistono alcuni modi per installare Hops sul computer.
  1. [Install Hops](rhino://package/search?name=hops) (questa opzione aprirà Rhino).
  1. Oppure, digitate `PackageManager` sulla linea di comando di Rhino.
      1. Quindi, cercare "Hops".
      1. Selezionare Hops e fare clic su Install.

### Creare un input

Ora che abbiamo installato Hops, iniziamo a definire la nostra funzione creando un parametro di testo di input. In *Params > Util Group* verrà mostrata una raccolta di componenti Context Getter. Posizionare un componente **Get String** sull’area di disegno. Fare clic con il pulsante destro del mouse al centro di questo componente e cambiare il nome da `Get String` a `Name`. Questo valore è quello che Hops utilizzerà come nome del parametro di input.
{{< image url="/images/hops_getting_started_01.png" alt="/images/hops_getting_started_01.png" class="image_center" width="100%" >}}

È possibile assegnare un valore predefinito a questo parametro collegando una stringa nell’input del componente Get String. Aggiungere **Text Panel** all'area di disegno. Questo si trova in *Params Tab > Input Group*. Fare doppio clic su Text Panel e scrivere il proprio nome nell'input.
{{< image url="/images/hops_getting_started_02.png" alt="/images/hops_getting_started_02.png" class="image_center" width="100%" >}}

### Definire la funzione

Ora che abbiamo creato un parametro di input, dobbiamo eseguire una sorta di azione utilizzando quel valore. Creiamo un messaggio utilizzando il nome appena usato nel componente Get String. Aggiungere **Concatenate Component** all’area di disegno. Questo si trova in *Sets Tab > Text Group*. 

Il componente Concatenate aggiunge una serie di frammenti di testo in un unico messaggio. Nel nostro caso, vogliamo creare una stringa che dica `Hello Your Name Here!`. 

Il componente Concatenate è un tipo speciale di componente in Grasshopper che utilizza un'interfaccia ZUI (Zoomable User Interface). Se ingrandiamo il componente (usando la rotella di scorrimento centrale), appare un piccolo pulsante (+) sul lato sinistro del componente. Fare clic sul simbolo (+) sotto il secondo parametro (B) per aggiungere un terzo parametro di input.

Ora, ingrandiamo e aggiungiamo un altro pannello di testo all'area di disegno. Fare doppio clic sopra per inserire il testo. Digitare `Hello ` nel pannello (nota: dopo la parola viene aggiunto uno spazio). Collegare il pannello all'input A del componente Concatenate.

Quindi, collegare l'output del componente Get String all'input B del componente Concatenate. Infine, aggiungere un altro pannello di testo all’area di disegno e digitare un punto esclamativo `!` nel pannello. Connettere l'output G del componente Mirror all'input G del componente Concatenate.

Collegare un pannello di testo all'output del componente Concatena per visualizzare questo messaggio. La vista visualizzata dovrebbe essere simile a quella dell'immagine.
{{< image url="/images/hops_getting_started_03.png" alt="/images/hops_getting_started_03.png" class="image_center" width="100%" >}}

### Creare un output

L'ultimo passo per creare la nostra funzione Hops consiste nel creare un parametro di output per restituire la stringa appena creata. Aprire *Param Tab> Util Group* e aggiungere un componente **Context Print** all’area di lavoro.

Fare clic con il pulsante destro del mouse sul parametro di input (etichettato come Tx) e modificare il nome in `Message`. Possiamo assegnare questo nome a qualsiasi cosa, ma questo valore è quello che Hops utilizzerà per il parametro di output.

Ora salviamo il file in una cartella del computer. Chiamiamo il file **Hello_World.gh**.
{{< image url="/images/hops_getting_started_04.png" alt="/images/hops_getting_started_04.png" class="image_center" width="100%" >}}

### Chiamare la funzione

Abbiamo creato una funzione compatibile con Hops. Usiamo Hops per chiamare questa funzione. Iniziamo creando una nuova definizione di Grasshopper (Ctrl + N).

Aprire *Param Tab > Util Group* e aggiungere un componente **Hops** all’area di lavoro. Fare clic con il pulsante destro del mouse su questo componente e selezionare l’opzione de menu **Path**. Sulla finestra di dialogo a comparsa, selezionare il file **Hello_World.gh** appena creato. Selezionare **OK** una volta selezionato il percorso.

A questo punto, il componente Hops dovrebbe cambiare aspetto, aggiungendo un input chiamato `Name` e un output chiamato `Message`. Hops ha essenzialmente raccolto l'esempio Hello_World.gh che abbiamo creato e lo ha inviato a un server locale rhino.compute per eseguire il calcolo e restituire il risultato.

Provare ad aggiungere un nuovo **pannello di testo** sull'area di disegno e collegarlo all'input Name del componente Hops. Fare doppio clic per modificare il nome sul pannello di testo. Aggiungere un altro pannello di testo all'output del componente Hops per vedere il risultato restituito dal server rhino.compute.
{{< image url="/images/hops_getting_started_05.png" alt="/images/hops_getting_started_05.png" class="image_center" width="100%" >}}

Abbiamo appena visto come creare e chiamare la prima funzione Hops. Per ulteriori informazioni su come Hops comunica con il server rhino.compute o per configurare l’ambiente di produzione, consultare i link di seguito.

 ---

## Collegamenti rapidi

 - [Come funziona Hops](../how-hops-works)
 - [Il componente Hops](../hops-component)
 - [Impostazione di un ambiente di produzione](../deploy-to-iis)

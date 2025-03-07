+++
aliases = ["/en/5/guides/general/creating-command-macros/", "/en/6/guides/general/creating-command-macros/", "/en/7/guides/general/creating-command-macros/", "/en/wip/guides/general/creating-command-macros/"]
authors = [ "scottd" ]
categories = [ "Overview" ]
description = "Un tutorial di base sulla creazione di macro (scripting insieme ai comandi di Rhino)"
keywords = [ "macro", "overview", "rhinoceros", "command" ]
languages = [ "Macro" ]
sdk = [ "Macro" ]
title = "Creazione di macro"
type = "guides"
weight = 1
override_last_modified = "2018-12-06T15:12:10Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/rhino/basicmacros"
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

È possibile creare macro in Rhino per automatizzare molte attività, personalizzare i comandi e migliorare il flusso di lavoro.

Potrebbe esserci un po' di confusione sull'uso del termine “scripting”.  Il termine descrive, in generale, sia il processo di scrittura delle macro (di cui tratta questa sezione), sia la scrittura di script più sofisticati in [RhinoScript](/guides/rhinoscript/), [Rhino.Python](/guides/rhinopython/) o altri linguaggi di programmazione.  

Le due cose sono in realtà molto diverse. La scrittura di funzioni in RhinoScript o in altri linguaggi di programmazione è molto più complessa della creazione di macro e richiede alcune conoscenze e competenze di programmazione.  Non tratteremo questo argomento in questa sede.

Qui, uso il termine "Macro" esclusivamente per descrivere l'unione di stringhe di comandi ordinari di Rhino e delle loro opzioni per creare una funzione automatizzata.  Si tratta di scripting al livello più semplice, facilmente accessibile a qualsiasi utente di Rhino, anche se non ha conoscenze di programmazione.  Tutto ciò che serve è una ragionevole comprensione dei comandi di Rhino e della loro struttura, oltre a una mente logica e al gusto per un po' di sperimentazione e debug.

#### Ecco gli strumenti necessari
1. Il cervello.

2. Il file di aiuto di Rhino: elenca tutti i comandi di Rhino e le loro sotto-opzioni. È il riferimento più importante.

3. Rhino **MacroEditor**, per eseguire facilmente le macro e realizzare operazioni di debug.


## Hai già usato una o due macro...
Innanzitutto, se sei utente di Rhino, utilizzi già le macro, anche se forse non lo sai.  Molti dei comandi di Rhino sono già "macro". Quando si fa clic su un pulsante della barra degli strumenti o si richiama un comando dal menu, spesso si tratta di una macro preimpostata.  Per vedere il processo, premi Maiusc e fai clic con il tasto destro sul pulsante **Extrude Straight**:

![Extrude](/images/extrudecrvbuttoneditor.gif)

Questo è un esempio della macro più semplice, che imposta una serie di opzioni all'interno di un singolo comando, in modo da non doverle specificare ogni volta che si usa.  **ExtrudeCrv** ha diversi pulsanti con opzioni preimpostate, **Tapered, AlongCurve, ToPoint, Cap=Yes** (solido) ecc.  Controlla le macro sotto tutti i pulsanti **ExtrudeCrv** per vedere come sono disposti.

In un certo senso, si fa la stessa cosa come quando si fa clic o si digita le opzioni una alla volta sulla linea di comando.  In realtà, le macro sono solo un insieme di istruzioni per ripetere una sequenza di comandi che altrimenti verrebbero inseriti manualmente uno alla volta.

Questo scripting di opzioni per un singolo comando può anche essere combinato con l'inserimento di dati (ad esempio, coordinate o altri dati numerici). È anche possibile mettere insieme più comandi in fila, per ottenere una sequenza automatica di eventi per manipolare o creare oggetti.

**Note:** Perché gli _Underscore?  Questi indicano a Rhino che il comando che segue è in inglese (indipendentemente dalla lingua in cui si esegue Rhino), il che renderà la macro universale.  Se si utilizza la versione in inglese, è possibile eliminare i trattini bassi nelle macro, se lo si desidera. Non influisce su nient'altro.  Inoltre, perché il punto esclamativo (!)?  Questo annulla qualsiasi comando precedente in esecuzione, per sicurezza.

## Introduzione

Supponiamo di dover posizionare una serie di parallelepipedo 10x10x10 con il centro della faccia inferiore che atterra nel punto desiderato, da specificare con un clic del mouse nella posizione desiderata o inserendo le coordinate da tastiera.

È possibile utilizzare il comando standard _Box (**Angolo a angolo + Altezza**), ma per impostazione predefinita il punto di inserimento viene posizionato sul primo angolo del parallelepipedo.  Per avere il punto di inserimento nel punto desiderato, è più facile utilizzare il comando Parallelepipedo, Centro.   In realtà, si tratta solo del comando Parallelepipedo con l'opzione Centro, quindi è necessario attivarlo nella macro.

Apri **MacroEditor** e digita questo testo:

```
 ! _Box _Center
```

Questa è in realtà la macro sotto il pulsante Box, Center, se si controlla. 
Tutte le voci (parole di comando e input numerici) devono essere separate da un singolo spazio.

Ora, è necessario specificare il punto centrale.  Per farlo, occorre dire a Rhino di interrompere temporaneamente l'elaborazione del comando e di attendere un input sotto forma di clic o input da tastiera.  A questo scopo, inseriamo il comando Pausa.

```
 ! _Box _Center _Pause
```

Una volta inseriti i dati, è possibile specificare le dimensioni del parallelepipedo direttamente nel comando.  Poiché l'opzione Centro in Parallelepipedo richiede un angolo del parallelepipedo come secondo input, è possibile specificarne le coordinate X,Y:

```
 ! _Box _Center _Pause r5,5
```

Perché `r`?  Vogliamo che questa coordinata sia relativa all'ultimo punto selezionato, cioè al centro in basso del parallelepipedo.  Altrimenti l'angolo si troverà sempre in X5, Y5.

A questo punto, è possibile inserire l'altezza, che in questo caso è relativa al punto di partenza originale.

```
 ! _Box _Center _Pause r5,5 10
```

Poiché non sono necessari ulteriori input né sono possibili opzioni, la macro viene completata e il parallelepipedo è pronto.  Dal momento che volevamo un'altezza pari alla larghezza, un'altra possibilità sarebbe stata quella di usare Enter invece di 10 per l'ultima voce.

```
 ! _Box _Center _Pause r5,5 _Enter
```

Ora che la macro è in esecuzione, [[rhino:macroscriptsetup|crea un nuovo pulsante della barra degli strumenti]] e incolla la macro. Assegna un nome riconoscibile, come "10x10x10 box centrato in basso".  Nota: una volta eseguita la macro, il clic con il tasto destro ripete l'intera sequenza di questa macro, quindi è possibile utilizzarla più volte di seguito senza dover fare clic sul pulsante ogni volta.

## OK, ora complichiamo po' lo scenario...

Alcuni comandi richiamano finestre di dialogo con molte opzioni.  Normalmente, questa operazione interrompe la macro e attende che l'utente faccia clic sulle opzioni desiderate, quindi continua.  Dal momento che si vuole automatizzare il processo, possiamo evitare la finestra di dialogo anteponendo al comando un -hyphen (noto anche come trattino).  A questo punto, è possibile inserire tutte le opzioni e la macro verrà eseguita fino al completamento senza bisogno dell’intervento dell’utente.  Alcuni comandi hanno diversi livelli di sotto-opzioni.  Per vedere le opzioni disponibili, digita il comando sulla linea di comando con il trattino e guarda cosa viene proposto per le opzioni.  Fai clic sulle opzioni e controlla se esistono delle sotto-opzioni.

#### Loft due curve aperte

Supponiamo di voler ripetere il `Loft` di due curve aperte *OPEN* per formare una superficie.  Se si usa il comando standard `Loft`, occorre usare sempre la finestra di dialogo.  Se si usa la versione `Loft`, è possibile evitare questo passaggio e andare più veloci.  Ecco come:

```
-Loft
_Pause
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Nota: quando si richiama il comando, immediatamente una pausa consente di scegliere le curve.  Se si rimuove la pausa, la macro non funzionerà se non sono state selezionate le curve prima di chiamarla.  Se le curve sono già state preselezionate, la pausa viene intelligentemente ignorata.  Il comando imposta quindi tutte le opzioni specificate. Una volta fatto questo, crea la superficie e le finiture. Prova con due curve aperte, sia prima che dopo averle selezionate.  Prova a modificare una o più opzioni, ad esempio sostituendo Closed=Yes o Simplify=Rebuild. Per questa operazione, è necessario aggiungere una riga con Rebuild=20 o un altro valore.

#### Modificalo per utilizzarlo con curve chiuse.

Ora prova a farlo con due curve chiuse.  Sorge un problema.  Perché? Per le curve chiuse, Loft ha bisogno di un altro input: la posizione della cucitura.  È un elemento che deve essere inserito nella macro nella giusta sequenza.  È quindi possibile scegliere tra le varie opzioni di cucitura automatica (che si trovano a livello di sotto-opzione) o regolarle sullo schermo.  In ogni caso, è necessario modificare la macro.

L'aggiunta di una pausa nel punto giusto consente di controllare e regolare la cucitura sullo schermo:

```
-Loft
_Pause
_Pause
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

L'aggiunta di un `Enter' al posto di `Pause` indica a Rhino che non ti interessa. Lascia la cucitura così com'è di default.

```
-Loft
_Pause
_Enter
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

In alternativa, è possibile specificare un'altra opzione di cucitura Loft scendendo al livello delle sotto-opzioni di cucitura:

```
-Loft
_Pause
_Natural  <--
_Enter    <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

L'opzione `Enter` dopo Natural è necessaria per uscire dal livello di opzioni  “cuciture” e tornare al livello di opzioni Loft.

Purtroppo, la stessa macro non funziona correttamente sia per le curve aperte che per quelle chiuse, a causa dell'opzione di cucitura aggiuntiva richiesta.  Questo è uno dei limiti del sistema di macro e del modo in cui sono stati scritti alcuni comandi di Rhino.


## Usa le macro per impostare rapidamente le opzioni dell'interfaccia

Le macro possono anche essere usate per impostare automaticamente varie opzioni dell'interfaccia grafica e delle proprietà del documento senza dover entrare nella finestra di dialogo delle opzioni.  Per impostare la mesh di rendering nel modo desiderato, utilizzo quanto segue. Nota: il trattino prima di -_DocumentProperties.

```
-_DocumentProperties
_Mesh _Custom
_MaxAngle=0 _AspectRatio=0
_MinEdgeLength=0 _MaxEdgeLength=0
_MaxEdgeSrf=0.01 _GridQuads=16
_Refine=Yes _JaggedSeams=No
_SimplePlanes=No
_Enter
_Enter
```

Perché ci sono due Enter alla fine?

Si è scesi di due livelli in -_DocumentProperties, prima al livello Mesh e poi al sottolivello Custom all'interno di Mesh.  È necessario un Invio per uscire dal sottolivello e tornare al livello principale e un altro per uscire dal comando.  Per alcuni script potrebbero essere necessari anche tre inserimenti.  

Quanto segue è di Jeff LaSor, per attivare o disattivare il cursore a croce:

Per attivare o disattivare il mirino, inserisci il seguente comando in un pulsante:

```
  -_Options _Appearance _Visibility
  _Crosshairs _Enter _Enter _Enter
```
Nota: il riferimento al nome di ogni singola opzione di comando.  Specificarli all'interno dello script è come fare clic su di essi con il mouse.  Nota anche le tre voci di Invio.  Poiché ogni opzione di comando porta a una nuova serie di opzioni di comando di livello inferiore, per risalire è necessario premere Invio.  Poiché questo script è sceso di tre livelli, deve specificare tre Invio per uscire dal comando.

Oppure, se si usa un punto esclamativo `!` alla fine (che in uno script significa "termina ora!"), si arriva fino alla fine, indipendentemente dal numero di sottolivelli in cui ci si trova. Se si vuole continuare la macro con qualcos'altro, non si deve usare `!`, ma piuttosto l'Invio, altrimenti la macro si fermerà sempre al `!` e terminerà.

Lo script si limita ad attivare e disattivare il mirino. Ma se si volesse uno script che li attivi sempre e un altro che li disattivi sempre, ecco come apparirebbero:

Versione sempre attiva:

```
  -_Options _Appearance _Visibility
  _Crosshairs=_Show !
</code>
Always OFF version:
<code>
  -_Options _Appearance _Visibility
  _Crosshairs=_Hide !
```

In questo caso viene usato `!`. Inoltre, è possibile assegnare direttamente i valori che le opzioni possono assumere a quell'opzione usando l'operatore '='.  L'opzione Mirino ha due valori possibili, "Mostra" e "Nascondi", e quindi è quella utilizzata nell'assegnazione.

Grazie, Jeff!

## Altri strumenti e comandi utili per la scrittura di macro

Esistono alcuni trucchi pratici per eseguire macro più complesse.  Uno è l'uso discriminante di vari filtri di selezione, in particolare `SelLast`, che seleziona l'ultimo oggetto creato/trasformato, `SelPrev`, che seleziona l'oggetto di input precedente, e `SelNone`, che deseleziona tutto.  Esiste anche la possibilità di dare un nome agli oggetti, di raggrupparli (e di dare un nome al gruppo) e di richiamarli in seguito con il nome dell'oggetto o del gruppo.

```
Select
SelLast
SelPrev
SelNone
SetObjectName
SetGroupName
SelGroup
SelName
Group
Ungroup
```

Per impostare il nome di un singolo oggetto (questa è di per sé una macro!):

```
  _Properties _Pause _Object _Name
  [inserire qui il nome dell'oggetto] _Enter _Enter
```

Per selezionare solo un oggetto, fare clic sull'oggetto.

```
  _Properties _Pause _Object _Name
  " " _Enter_Enter (virgolette spaziali per il nome)
```

## Esempi di utilizzo degli strumenti di cui sopra

Osserva la seguente macro:

```
_Select _Pause _Setredrawoff
_BoundingBox _World _Enter
_Selnone _Sellast
_OffsetSrf _Solid _Pause
_Delete _Sellast
_BoundingBox _World _Enter
_Delete _Setredrawon
```

Crea un riquadro di delimitazione sfalsato attorno a un oggetto. L'offset viene inserito dall'utente.  Cerca di seguire la sequenza logica.  L'opzione Setredrawoff/on arresta/riavvia il refresh dello schermo, elimina lo sfarfallio del display durante l'esecuzione e velocizza il processo.  Attenzione, se il comando viene terminato prima di Setredrawon, potremmo pensare che Rhino è “morto” poiché lo schermo non si aggiorna più.  Se ciò accade, niente panico: digitando il comando `Setredrawon` lo schermo si aggiorna.

**Come esempio finale,** la macro seguente crea un punto centrato su un oggetto 2D planare o di testo e raggruppato con esso. Presuppone che ci si trovi nella stessa vista in cui è stato creato il testo e che l'oggetto sia realmente 2D e planare. Altrimenti è probabile che l’operazione fallisca.

Da notare l'uso di un gruppo con nome e di vari comandi di selezione.  Il comando `NoEcho` interrompe temporaneamente la segnalazione di informazioni alla riga di comando, il che, combinato con Setredrawoff/on, fa sì che la macro venga eseguita senza lampeggiare e senza troppe informazioni riportate nella cronologia dei comandi.  Tuttavia, funziona anche senza di essi.

```
_Select _Pause _Noecho _Setredrawoff
_Group _Enter _SetGroupName TexTemp
_BoundingBox _CPlane _Enter
_SelNone _SelLast _PlanarSrf
_SelPrev _Delete _SelLast
_AreaCentroid _Delete
_Sellast _SelGroup TexTemp
_Ungroup _Group _Setredrawon
```

**Modificare questo tutorial come meglio credi!**
Il sito web è in fase di costruzione.

## Argomenti correlati

- [Sintassi di base di Python](/guides/rhinopython/)
- [Rhinoscript](/guides/rhinoscript/)
- [Argomento della guida sulla sintassi delle macro](http://docs.mcneel.com/rhino/6/help/en-us/information/rhinoscripting.htm)
- [Eseguire una macro](/guides/rhinoscript/running-scripts-from-macros/)

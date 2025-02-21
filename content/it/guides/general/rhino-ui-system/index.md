+++
aliases = ["/en/8/guides/general/rhino-ui-system/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "Questa guida illustra il sistema interfaccia utente di Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Il sistema interfaccia utente di Rhino"
type = "guides"
weight = 3
override_last_modified = "2023-11-20T08:29:10Z"

[admin]
TODO = ""
origin = ""
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

Questa guida offre una panoramica sul sistema interfaccia utente (UI) di Rhino e confronta il nuovo sistema presente in Rhino 8 con il sistema di Rhino 7 e versioni precedenti.

## Sistema interfaccia utente di Rhino

Ecco gli obiettivi del nuovo sistema interfaccia utente di Rhino 8:

- Visualizzare pannelli e barre strumenti nello stesso contenitore.
- Creare riferimenti a barre strumenti e macro da più fonti senza dover copiare le definizioni da un file RUI all'altro.
- Inviare le modifiche all'interfaccia utente di Rhino (file RUI) senza sovrascrivere o sostituire i file esistenti in Rhino o nelle service release di plug-in. Nelle versioni precedenti di Rhino, la sostituzione del file RUI per fornire barre degli strumenti e macro aggiornate causava la sovrascrittura delle modifiche apportate dall'utente ai file RUI.
- Modificare rapidamente l'interfaccia utente di Rhino per visualizzare gli strumenti orientati alle attività.
- Condividere i layout dell'interfaccia utente tra gli utenti.
- Consentire agli utenti di modificare arbitrariamente l'interfaccia utente senza dover conoscere la posizione o l'origine di un componente dell'interfaccia e di tenere automaticamente traccia delle modifiche.
- Fornire un'interfaccia utente unificata per Windows e Mac.

Di seguito, le principali modifiche apportate al nuovo sistema di interfaccia utente di Rhino 8:

- I gruppi di barre strumenti sono stati sostituiti da Contenitori. I contenitori possono visualizzare sia pannelli che barre degli strumenti.
- I file RUI vengono utilizzati per fornire le librerie delle barre degli strumenti e delle macro e non vengono più modificati direttamente. Rhino tiene traccia delle modifiche apportate al file RUI e le applica al momento del caricamento. In questo modo Rhino può fornire file RUI aggiornati senza perdere le modifiche apportate dall'utente a una barra degli strumenti o a una macro.
- Sono stati aggiunti layout finestra, che possono essere utilizzati per passare rapidamente da una configurazione all'altra dell'interfaccia utente. Possono essere esportati come file e includono le modifiche alle barre degli strumenti, alle macro e ai file RUI dell'utente.
- L'importazione di un layout finestra estrae i file RUI dell'utente come necessario e applica le modifiche RUI.

Il nuovo sistema di interfaccia utente di Rhino 8 è stato progettato per consentire il riferimento a componenti dell'interfaccia utente provenienti da diverse fonti, tra cui pannelli, barre degli strumenti e macro, definiti da qualsiasi file RUI o plug-in. Alla chiusura di Rhino, le modifiche all'interfaccia utente vengono salvate e i file RUI originali non vengono mai modificati, a meno che non venga richiesto espressamente. Le configurazioni dei layout dell'interfaccia utente possono essere salvate, ripristinate, esportate e importate come layout di finestra e condivise tra Windows e Mac.

### Contenitori

I contenitori contengono riferimenti a pannelli e barre degli strumenti. Le barre degli strumenti possono essere referenziate da qualsiasi sorgente RUI valida. Gli elementi vengono visualizzati come pannelli in un contenitore. I contenitori possono essere visibili o nascosti.

I contenitori possono essere modificati trascinando le schede da un contenitore a un altro, oppure facendo clic sul menu `Gear` del contenitore per aggiungere o rimuovere riferimenti a pannelli o barre degli strumenti. Lo stesso pannello può essere referenziato da più contenitori, il che significa che è possibile visualizzare la scheda `Layers`, ad esempio, in più contenitori.

Le definizioni dei contenitori, la visibilità, la posizione e le dimensioni vengono salvate alla chiusura di Rhino e ripristinate al riavvio di Rhino. Queste informazioni possono essere memorizzate e condivise anche tramite i Layout di finestra.

I contenitori possono essere gestiti usando il comando **[_Containers](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/containers.htm#(null))** di Rhino.

### Layout finestra

I layout finestra sono un'istantanea delle definizioni dei contenitori, degli stati di visibilità, delle posizioni e delle dimensioni. Il ripristino di un layout finestra riconfigura l'interfaccia utente corrente in modo che appaia come quando è stato creato il layout. I contenitori ripristinati visualizzeranno le schede nell'ordine in cui erano al momento della creazione del layout finestra e appariranno nella stessa posizione e dimensione. I pannelli delle barre degli strumenti fanno riferimento alla definizione corrente di una barra degli strumenti; se la barra degli strumenti non esiste più, il pannello non verrà visualizzato.

I layout finestra possono essere gestiti usando il comando **[_WindowLayout](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/windowlayout.htm#(null))** di Rhino.

#### Esportazione e importazione di layout finestra

I layout finestra possono essere esportati in un file di layout finestra di Rhino (RHW). I file RHW esportati includono i file RUI personalizzati di riferimento e le modifiche associate a tutti i file RUI al momento della creazione del file RHW.

L'importazione di un file RHW controlla se è aperto un file RUI personalizzato incorporato. Se il file non è aperto, il file personalizzato viene estratto e aperto. Una volta estratto o verificato l'elenco personalizzato, le modifiche RUI salvate nel file RHW verranno applicate ai file RUI correnti. Le informazioni di modifica associate alle barre degli strumenti definite da file plug-in non esistenti verranno ignorate. Una volta ripristinati i dati RUI, i contenitori verranno creati o modificati per corrispondere alla definizione memorizzata nel file RHW. I contenitori che fanno riferimento solo a barre degli strumenti di plug-in non installati saranno ignorati. Una volta importato, il layout appare nell'elenco dei layout finestra e può essere ripristinato.

I layout finestra possono essere esportati e importati usando il comando **[_WindowLayout](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/windowlayout.htm#(null))** di Rhino.

### File RUI

In Rhino 8, i file RUI sono ora semplicemente una raccolta di barre degli strumenti, macro e immagini. Questi file sono destinati a fornire librerie di barre degli strumenti che possono essere referenziate dai contenitori. Le modifiche alle barre degli strumenti e alle macro possono ora essere fornite con gli aggiornamenti di Rhino e dei plug-in. Le nuove barre degli strumenti definite nella libreria RUI aggiornata appariranno automaticamente nell'elenco dei comandi della barra degli strumenti. I pulsanti aggiunti o rimossi da una barra degli strumenti verranno aggiunti o rimossi al riferimento della barra degli strumenti.

I gruppi di barre degli strumenti definiti nei file RUI vengono convertiti in contenitori quando vengono caricati, per supportare i file RUI legacy e plug-in e fornire a un file RUI plug-in un modo per creare contenitori associati al plug-in.

I file RUI collegati possono essere gestiti usando l'opzione **[Opzioni > Aspetto > Barre degli strumenti](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#options/appearance_toolbars.htm#(null))** di Rhino.

### Barre degli strumenti

Le barre degli strumenti sono raccolte di pulsanti. I pulsanti della barra degli strumenti fanno riferimento a macro che possono provenire da qualsiasi fonte RUI valida. Le barre degli strumenti vengono visualizzate come schede in un contenitore.

#### Gruppi di barre degli strumenti

I gruppi di barre degli strumenti vengono ora convertiti in contenitori quando vengono caricati inizialmente. Sono un modo per supportare i file RUI legacy. I gruppi possono essere utilizzati anche dagli sviluppatori di plug-in per fornire definizioni di contenitori associati a un plug-in.

#### Barra strumenti

Le barre degli strumenti sono raccolte di pulsanti di barre degli strumenti e possono essere referenziate da più contenitori. Possono essere modificati trascinando e rilasciando i pulsanti da altre barre degli strumenti o utilizzando la procedura guidata per i nuovi pulsanti.

Le barre degli strumenti possono essere gestite usando il comando **[_Toolbar](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/toolbar.htm#(null))** di Rhino.

#### Pulsante barra strumenti

I pulsanti della barra degli strumenti possono contenere azioni da eseguire con il tasto sinistro e/o destro del mouse. Le azioni del clic sinistro e destro del mouse sono assegnate a macro che contengono uno script da eseguire quando si fa clic. I pulsanti della barra degli strumenti visualizzano l'immagine associata alla macro assegnata all'azione del tasto sinistro del mouse, se presente; in caso contrario, viene utilizzata l'immagine della macro del tasto destro.

#### Menu

Il sistema di menu di Rhino può essere esteso utilizzando oggetti di menu definiti in un file RUI. Il file RUI contiene informazioni sulla posizione che descrivono dove inserire una voce nel sistema di menu. Le nuove voci di menu vengono definite facendo riferimento a una macro che contiene:

- Testo menu.
- Imagine elemento del menu.
- Il testo che appare sulla barra di stato al passaggio del mouse su una voce di menu.
- Script di comando che viene eseguito quando si fa clic sulla voce di menu.

I menu possono essere gestiti usando il comando **[_Menus](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#toolbarsandmenus/workspace_editor.htm#(null))** di Rhino.

#### Macro

Le macro contengono le informazioni necessarie per descrivere lo script di comando che viene eseguito quando la macro viene eseguita. Le definizioni di macro includono le seguenti:

- Nome
- Immagine, versione in modalità chiara e scura
- Script dei comandi
- Testo pulsante
- Descrizione (tooltip) di un pulsante
- Testo menu
- Testo guida

Le macro possono essere gestite usando il comando **[_Macros](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/macros.htm#(null))** di Rhino.

### Pannelli

I pannelli sono forme di interfaccia utente senza modello create da Rhino o da plug-in. Possono apparire in qualsiasi contenitore come schede e possono essere spostate da un contenitore all'altro trascinandole.

I pannelli possono essere referenziati da più contenitori, ma non possono apparire più di una volta nello stesso contenitore.

## Sistema interfaccia utente di Rhino

Il sistema dell'interfaccia utente di Rhino, presente in Rhino per Windows versione 7 e precedenti, consiste in quanto segue:

### Barre degli strumenti

Le barre degli strumenti di Rhino sono raccolte di pulsanti della barra degli strumenti. I pulsanti della barra degli strumenti fanno riferimento a macro che devono essere definite nello stesso file RUI della barra. I pulsanti contengono: immagine, tooltip, testo del menu, testo di aiuto e script. Le barre degli strumenti vengono visualizzate in gruppi.

### Gruppi di barre degli strumenti

I gruppi di barre degli strumenti sono raccolte di riferimenti alle barre degli strumenti dello stesso file RUI. Trascinando una barra degli strumenti da un file a un gruppo di un altro file, la barra degli strumenti e le macro a cui fa riferimento vengono copiate dal file di origine a quello di destinazione. I gruppi della barra degli strumenti non possono fare riferimento ai pannelli di Rhino.

### Barra strumenti

Le barre degli strumenti sono raccolte di pulsanti della barra degli strumenti e sono sempre riferite e visualizzate solo dai gruppi di barre degli strumenti.

### Pulsante barra strumenti

I pulsanti della barra degli strumenti possono contenere azioni da eseguire con il tasto sinistro e/o destro del mouse. Le azioni del clic del mouse sono assegnate a macro che contengono uno script da eseguire quando si fa clic. I pulsanti della barra degli strumenti visualizzano l'immagine associata alla macro assegnata all'azione del tasto sinistro del mouse, se presente; in caso contrario, viene utilizzata l'immagine della macro del tasto destro.

I pulsanti della barra degli strumenti possono essere configurati in modo da escludere temporaneamente altre barre degli strumenti, se lo si desidera.

I pulsanti delle barre degli strumenti possono fare riferimento solo alle macro dello stesso file RUI della barra degli strumenti a cui appartengono.

### Menu

Il sistema di menu di Rhino può essere esteso utilizzando oggetti di menu definiti in un file RUI. Il file RUI contiene informazioni sulla posizione che descrivono dove inserire una voce nel sistema di menu. Le nuove voci di menu vengono definite facendo riferimento a una macro che contiene:

- Testo menu.
- Immagine elemento del menu.
- Il testo che appare sulla barra di stato al passaggio del mouse su un elemento del menu.
- Script di comando che viene eseguito quando si fa clic sulla voce di menu.

### Macro

Le macro contengono le informazioni necessarie per visualizzare o descrivere lo script di comando che viene eseguito quando la macro viene eseguita. Le definizioni di macro includono le seguenti:
Immagine visualizzata su un pulsante della barra degli strumenti o su una voce di menu.

- Suggerimento del pulsante.
- Testo pulsante:
- Testo elemento del menu.
- Il testo che appare sulla barra di stato al passaggio del mouse su un elemento del menu.
- Script di comando da eseguire.

### File RUI

I file RUI sono raccolte di elementi di cui sopra e sono memorizzati in una directory scrivibile. Gli elementi memorizzati in un file RUI possono fare riferimento solo agli elementi definiti nello stesso file. Le modifiche agli elementi del file vengono salvate automaticamente alla chiusura di Rhino. È possibile aprire o chiudere i file RUI o scegliere manualmente di salvare un file in qualsiasi momento. Viene eseguito il backup della versione corrente di un file e le modifiche vengono salvate nel nome del file. Se un file viene danneggiato, è possibile eliminarlo e rinominare il file di backup nel tentativo di ripristinare la versione precedente. Se il file di backup è danneggiato, non è possibile recuperare nulla.

I plug-in di Rhino possono installare un file RUI con lo stesso nome del plug-in, che verrà copiato in una posizione scrivibile e aperto automaticamente all'avvio di Rhino. Questo permette a un plug-in di estendere l'interfaccia di Rhino, consentendo al contempo al plug-in di non essere caricato fino a quando non viene richiamato.

Si noti che tutto ciò può essere gestito utilizzando il comando **[_Toolbars](https://docs.mcneel.com/rhino/7/help/en-us/index.htm#options/toolbars.htm#(null))** di Rhino 7.

### Pannelli Rhino

I pannelli di Rhino sono definizioni di interfaccia utente senza modello create dal nucleo di Rhino o da un plug-in.

I pannelli vengono visualizzati in un insieme di schede. Le raccolte di pannelli possono contenere solo riferimenti a pannelli e un pannello può essere referenziato solo da una singola raccolta. La visualizzazione di un pannello in una collezione rimuove i riferimenti a tale pannello da qualsiasi altra collezione.

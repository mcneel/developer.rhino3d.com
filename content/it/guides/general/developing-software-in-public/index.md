+++
aliases = ["/en/5/guides/general/developing-software-in-public/", "/en/6/guides/general/developing-software-in-public/", "/en/7/guides/general/developing-software-in-public/", "/en/wip/guides/general/developing-software-in-public/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "Una panoramica del processo di sviluppo di McNeel."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Sviluppo pubblico di un software"
type = "guides"
weight = 0
override_last_modified = "2018-12-05T14:59:06Z"

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


## Panoramica

Negli ultimi 20 anni abbiamo messo a punto un processo che contribuisce alla soddisfazione del cliente.  Questo processo è composto da otto elementi, tutti ugualmente importanti.  Per anni abbiamo sviluppato i nostri strumenti proprietari per supportare la maggior parte di questo processo.  Ma ora, esistono ottimi strumenti disponibili in commercio e invitiamo gli utenti a utilizzarli.

Il nostro processo di sviluppo software, così come altri processi, è un ciclo.  Quindi, possiamo iniziare ovunque.

![Rhino Development Cycle](/images/developing-software-in-public-01.png)

## Il ciclo

Poiché questa è una guida per sviluppatori, iniziamo con la scrittura del codice.

### Codice

Noi sviluppatori di software passiamo la maggior parte del tempo a scrivere il codice.  Abbiamo il nostro IDE aperto preferito, scriviamo il codice, eseguiamo il debug e risolviamo i problemi.  Non conosciamo nessuno sviluppatore di software che non ami risolvere i problemi.

Quando ne troviamo uno, lo *registriamo* sul nostro sistema di controllo delle versioni...

### Git Commit

Il codice viene registrato su un [sistema di controllo delle versioni](https://en.wikipedia.org/wiki/Version_control).  Nel nostro caso, usiamo [git](https://git-scm.com/) con [GitHub](https://github.com/).  Esistono molti altri sistemi di controllo delle versioni.  Prima usavamo [Subversion](https://subversion.apache.org/), ma ora usiamo [GitHub](https://github.com/).  [GitHub](https://github.com/) funziona bene con tanti altri strumenti e ha un'API molto ricca.  Ma ce ne sono altri che vale la pena considerare: [BitBucket](https://bitbucket.org), [Mercurial](https://www.mercurial-scm.org/), ecc.

Se non utilizzi nessuno strumento di controllo delle versioni, ti suggeriamo di iniziare.  Ora è così facile.  Consente di tornare ad altre versioni del software che non presentavano un determinato  problema.  Aiuta a collaborare come team.  Si tratta di uno strumento necessario per qualsiasi tipo di automazione della compilazione software.  Abbiamo già detto che è facile?

Come sviluppatori, usiamo una versione modificata di [GitHub Flow](https://guides.github.com/introduction/flow/) per creare e unire pull request nel master branch.

Dopo aver eseguito il commit del codice, lo compiliamo...

### Compilazione

Oltre a compilare in locale sui nostri computer, utilizziamo server dedicati [TeamCity](https://www.jetbrains.com/teamcity/) che compilano costantemente il nostro codice e verificano che funzioni con il nostro master branch su [GitHub](https://github.com/).  In questo modo ci assicuriamo di non impedire ad altri utenti di ottenere il codice più recente e di compilare.

Questi server [TeamCity](https://www.jetbrains.com/teamcity/) verificano ogni operazione di commit e compilano anche le nostre versioni giornaliere (molte), rilasciate ogni quattro ore circa.  Compilano anche le versioni WIP e le service release pubbliche.

Con ogni nuova versione, eseguiamo il testing...

### Testing

Quando gli sviluppatori risolvono i bug e chiudono i report sui problemi, il nostro staff di testing interno si assicura che la build pubblica funzioni correttamente.  Ci affidiamo anche ai nostri clienti per testare le build WIP e le release candidate.

Il test avviene prima e dopo la fase successiva: La pubblicazione...

### Pubblicazione

Quando abbiamo una build pronta per essere distribuita ai clienti, la distribuiamo (o pubblichiamo).

Questo include il rilascio di ...

- [Programmi di installazione scaricabili.](http://www.rhino3d.com/download)
- [SDK.](http://developer.mcneel.com)
- Documentazione (questo sito).

Annunci pubblici tramite e-mail, blog e social media.

### Feedback

Ascoltiamo gli utenti attraverso tutti i canali possibili:

- [Chat.](http://www.rhino3d.com/support#)
- [E-mail.](mailto:tech@mcneel.com)
- Supporto tecnico: +34 933 19 90 02.
- [Forum (Discourse).](https://discourse.mcneel.com/)

E spesso, quando ascoltiamo, troviamo problemi che devono essere risolti.  A volte sono piccoli errori, a volte sono ENORMI.  Registriamo sempre un problema...

### Monitoraggio

Registriamo i problemi in [YouTrack](https://mcneel.myjetbrains.com).

[YouTrack](https://mcneel.myjetbrains.com) funziona bene per noi perché ci aiuta a garantire che ogni problema venga testato e documentato in modo adeguato.

### Definire le priorità

Capire qual è il prossimo passo più importante è DIFFICILE.  Parliamo con i nostri clienti.  Parliamo tra di noi.  Per comunicare utilizziamo Gmail, Google Drive e Google Docs.  Comunichiamo 24 ore su 24 su [Slack](https://slack.com/).

Ci riuniamo ogni settimana il martedì.  Prima della riunione, condividiamo ciò che abbiamo fatto su un Google Doc. In questo documento, condividiamo i nostri obiettivi per ciascuno dei prodotti che stiamo rilasciando e per ciascuno dei gruppi di funzionalità su cui stiamo lavorando, compresi i grafici dei progressi compiuti nel tempo, con link diretti ai problemi di [YouTrack](https://mcneel.myjetbrains.com) e riceviamo report verbali da ciascuna delle persone che lavorano alle funzionalità.

Inoltre, ogni sviluppatore scrive su cosa ha lavorato, cosa ha in programma di fare dopo e cosa lo ostacola nel completamento del lavoro.

### Automazione

E infine, ma non per questo meno importante, automatizziamo i processi.

Ecco alcuni delle attività aggiunte di recente:

- Compilazione dei commit di ogni sviluppatore prima che venga inserito nel branch di sviluppo master.
- Chiusura dei problemi in [YouTrack](https://mcneel.myjetbrains.com) quando le correzioni vengono unite al branch di sviluppo master dai server di [TeamCity](https://www.jetbrains.com/teamcity/) .
- Creazione di release interne e pubbliche sui server [TeamCity](https://www.jetbrains.com/teamcity/) .
- Pubblicazione di nuove versioni WIP digitando un comando in [Slack](https://slack.com/).
- Caricamento delle versioni pubbliche sui server di download.

## Sviluppo pubblico

Fino a poco tempo fa, rendevamo pubbliche queste parti dei processi di sviluppo:

- Testing.
- Pubblicazione.
- Feedback.

E negli ultimi due anni abbiamo reso pubblico il nostro sistema di monitoraggio dei problemi passando a YouTrack.  Alcune questioni non vengono rese pubbliche per motivi di sicurezza o privacy degli utenti.

Una cosa che vorremmo fare presto è rendere pubblici alcuni aspetti di sviluppo.

- Condividere alcuni dei nostri codici come repository pubblici su GitHub, in modo che gli utenti possano avere esempi di codice reali, rivolti alla produzione.
- Permettere la condivisione di correzioni e miglioramenti del codice.
- Facilitare la creazione di plug-in pubblicando RhinoCommon come pacchetto NuGet.
- Contribuire all'automazione delle compilazioni, se necessario.

## Argomenti correlati

- [Panoramica sulla tecnologia di Rhino](/guides/general/rhino-technology-overview)
- [Contributo](/guides/general/contributing)
- [Prerequisiti per gli sviluppatori](/guides/general/rhino-developer-prerequisites)

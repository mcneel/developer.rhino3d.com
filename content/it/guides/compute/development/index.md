+++
aliases = ["/en/5/guides/compute/development/", "/en/6/guides/compute/development/", "/en/7/guides/compute/development/", "/en/wip/guides/compute/development/"]
authors = [ "pedro" ]
categories = [ "Getting Started", "Development" ]
description = "Distribuire Compute per la produzione"
keywords = [ "developer", "compute", "production" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Esecuzione e debug di Compute in locale"
type = "guides"
weight = 2
override_last_modified = "2024-05-13T15:49:48Z"

[admin]
TODO = "needs editing"
origin = ""
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

Rhino.Compute consente di utilizzare le funzionalità di calcolo geometrico di Rhino nel cloud. Prima di distribuire un’applicazione in un ambiente di produzione, bisogna assicurarsi che tutto funzioni perfettamente in un ambiente controllato.

Questa guida è destinata agli sviluppatori che hanno familiarità con Windows e una conoscenza di base di [Visual Studio](https://visualstudio.microsoft.com/downloads/) e [Git](https://git-scm.com/downloads). Sia per esperti di Rhino, che per utenti alle prime armi con Rhino.Compute, questa documentazione fornirà i passi necessari per configurare l’ambiente di sviluppo e iniziare il debug in modo efficace.

## Prerequisiti

Prima di immergerci nella configurazione di Rhino.Compute sulla macchina locale, dobbiamo assicurarci di avere gli strumenti giusti. Ecco cosa serve:

- Sistemi operativi supportati: Rhino.Compute funziona solo su Windows.
- Ambiente di sviluppo. Per compilare il codice è necessario [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) .
- Controllo della versione. [Git](https://git-scm.com/downloads) è necessario per clonare il repository di compute.rhino3d e gestire i rami in base alla versione di Rhino.
- Rhino. Visitare la pagina dei download per ottenere le ultime build di [Rhino 8](https://www.rhino3d.com/download/rhino-for-windows/8/latest) o [Rhino 7](https://www.rhino3d.com/download/rhino-for-windows/7/latest) . Dopo il download e l’installazione, avviare Rhino e seguire le istruzioni all'avvio per convalidare la licenza sul computer o attraverso Cloud Zoo.

{{< call-out "note" "Nota" >}}
È necessario eseguire la versione specifica di Rhino.Compute in base alla versione di Rhino installata. Nella prossima sezione, si clonerà il codice sorgente dal repository compute.rhino3d. Se Rhino 8 è installato sulla macchina, occorre assicurarsi di clonare il ramo 8.x. In alternativa, se hai installato Rhino 7, occorre clonare il ramo 7.x.
{{< /call-out >}}

## Clonare il repository

Per ottenere l'ultima versione di Rhino.Compute è necessario clonare il suo [repository](https://github.com/mcneel/compute.rhino3d) dal nostro account ufficiale su Github.

1. Accedere a [https://github.com/mcneel/compute.rhino3d](https://github.com/mcneel/compute.rhino3d)

1. Dal menu a discesa del ramo, assicurarsi di selezionare il ramo 8.x o 7.x da clonare.

1. Fare clic sul pulsante verde "<> Code" e copiare l'URL del repository.
![compute_geometry_clone](/images/compute_geometry_clone.png)

1. Sul computer locale, creare una cartella in cui clonare il repository.

1. Navigare in quella directory attraverso il prompt dei comandi preferito e digitare `git clone` e incollare l'URL copiato in precedenza.
    ```python
    git clone https://github.com/mcneel/compute.rhino3d.git
    ```
1. Al termine dell'operazione di clonazione, dovrebbe apparire una serie di file e directory scaricati dal repository compute.rhino3d nella cartella creata.

## Anatomia della soluzione

Il repository di Rhino.Compute è costituito da due progetti principali, ognuno dei quali serve a scopi diversi all'interno del framework. Comprenderli può aiutare a chiarire il funzionamento di Rhino.Compute, soprattutto se si vuole lavorare o contribuire al suo sviluppo. Ecco la ripartizione dei due progetti:

- **compute.geometry**. Questo progetto si incentra principalmente sugli aspetti di calcolo geometrico. In sostanza, compute.geometry fornisce API REST che espone il motore di geometria di Rhino per essere usato sul web. Ciò significa che le operazioni geometriche possono essere eseguite su un server e i risultati possono essere recuperati in remoto, il che lo rende molto utile per le applicazioni o i servizi basati sul web che richiedono un'elaborazione geometrica complessa.

- **rhino.compute**. Questo progetto può essere considerato come un servizio di livello superiore che gestisce e orchestra le chiamate all'API di compute.geometry, gestendo compiti come l'autenticazione, la creazione di processi figli e l'impostazione di limiti di tempo per la chiusura del processo.

## Compilare la soluzione

Ora che abbiamo il codice, è il momento di aprire il progetto in Visual Studio 2022 e prepararlo per il debug.

1. Navigare nella directory in cui è stato clonato il repository e cercare il file **compute.sln** . Fare doppio clic su di esso per aprire il progetto in Visual Studio 2022.

1. Impostare la configurazione della soluzione in modalità **Debug** . Ciò consente di eseguire il codice con tutte le funzioni di debug, rendendo più facile la ricerca del codice e l'individuazione degli errori.
![compute_geometry_vs_debug](/images/compute_geometry_vs_debug.png)

1. Nel menu File, fare clic su Build -> Build Solution (Ctrl + Maiusc + B). Questo compila tutti i file del progetto.
![compute_geometry_vs_build](/images/compute_geometry_vs_build.png)

1. Nel pannello Solution Explorer, fare clic con il pulsante destro del mouse sul progetto **rhino.compute** e selezionare **Set as Startup Project**. In questo modo, si garantisce che durante l’esecuzione del debugger, Visual Studio avvierà questo particolare progetto.
![compute_geometry_vs_startup](/images/compute_geometry_vs_startup.png)

1. Fare clic su **rhino.compute** per avviare l'applicazione nel debugger. Nella barra delle applicazioni dovrebbe apparire un'applicazione della console che mostra lo stato del processo di caricamento di Rhino.Compute.
![compute_geometry_vs_run](/images/compute_geometry_vs_run.png)

1. Ora non resta che attendere qualche secondo per il caricamento di Rhino.Compute. Tenere presente che le informazioni registrate dipendono dalla versione di Rhino scelta in precedenza.
![compute.geometry.exe](/images/compute_geometry_screenshot.png)

## Testare un endpoint

Con l'applicazione console di Rhino.Compute in esecuzione, controllare uno qualsiasi di questi endpoint per verificare che tutto funzioni.
- [http://localhost:6500/version](http://localhost:6500/version)
- [http://localhost:6500/healthcheck](http://localhost:6500/healthcheck)
- [http://localhost:6500/activechildren](http://localhost:6500/activechildren)
- [http://localhost:6500/sdk](http://localhost:6500/sdk)
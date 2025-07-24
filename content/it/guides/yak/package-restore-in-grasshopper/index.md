+++
aliases = ["/en/5/guides/yak/package-restore-in-grasshopper/", "/en/6/guides/yak/package-restore-in-grasshopper/", "/en/7/guides/yak/package-restore-in-grasshopper/", "/en/wip/guides/yak/package-restore-in-grasshopper/"]
authors = [ "will" ]
categories = [ "Features" ]
description = "In che modo Grasshopper può utilizzare Yak per semplificarti la vita?"
keywords = [ "yak", "grasshopper" ]
sdk = [ "Yak" ]
title = "Ripristino dei pacchetti in Grasshopper"
type = "guides"
weight = 1
override_last_modified = "2020-10-21T15:58:32Z"

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

Per cominciare, questa non è tanto una guida per lo sviluppo quanto una descrizione di questa funzione, in modo che come sviluppatori possiate capire meglio come il pacchetto e il plug-in devono essere impostati.



Può essere frustrante aprire una definizione di Grasshopper e scoprire che i plug-in necessari non sono installati nel sistema.
 Il Gestore pacchetti può aiutare a semplificare il processo su come soddisfare i requisiti delle dipendenze.


Da Rhino 6 in poi, la finestra di dialogo "Unrecognized Objects" presenta all'utente un'opzione per _scaricare e installare_ i plug-in mancanti. Questa funzione è chiamata Package Restore.

![Grasshopper package restore](/images/yak-gh-restore.gif)

Package Restore utilizza il nome, l'ID e la versione dei plug-in mancanti per cercare il server dei pacchetti. Se un pacchetto corrisponde alla richiesta di ricerca, viene installato e, se possibile, caricato prima dell'apertura della definizione[^1].


<iframe width="560" height="315" src="https://www.youtube.com/embed/MsjRdRtHW08" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Corrispondenza

### Assegnazione del nome

Idealmente, il nome del plug-in di Grasshopper e del pacchetto devono coincidere. Nel caso in cui non sia possibile, a causa dei vincoli dello schema di denominazione dei pacchetti[^2] o del fatto che ci sono più plug-in in un pacchetto, ciascuno con un nome diverso, il pacchetto corretto può essere identificato anche dall'ID del plug-in.

Per ogni file .gha, l'ID del plug-in viene estratto e aggiunto al file `manifest.yml` quando si esegue `yak build`.

### Numeri di versione

I numeri di versione dei pacchetti possono seguire le specifiche [Semantic Versioning 2.0.0](https://semver.org) (SemVer) o possono essere di quattro cifre[^3], come da `System.Version`. Consultare la guida [Il server dei pacchetti](../the-package-server) per maggiori dettagli sui formati dei numeri di versione consentiti.

Il server consente sia SemVer che quattro cifre perché alcuni plug-in di Grasshopper specificano il loro numero di versione come `string` in una classe derivata da `GH_AssemblyInfo` mentre altri si affidano all'attributo `AssemblyVersionAttribute`.

Durante il ripristino dei pacchetti, se sul server esiste un pacchetto che corrisponde al nome o all'ID del plug-in mancante, ma la versione esatta non esiste, verrà installata l'ultima versione stabile.

[^1]: Added to Grasshopper in December 2019. On-the-fly loading is only possible if another version of the Grasshopper library is not already installed and loaded. Otherwise, Rhino will need to be restarted to load the new version of the library.
[^2]: Package names are pretty strict. They only allow letters, numbers, hyphens and underscores.
[^3]: Support for four-digit (`System.Version`) version numbers was added in Yak 0.8.

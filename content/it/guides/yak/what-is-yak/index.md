+++
aliases = ["/en/5/guides/yak/what-is-yak/", "/en/6/guides/yak/what-is-yak/", "/en/7/guides/yak/what-is-yak/", "/en/wip/guides/yak/what-is-yak/"]
authors = [ "will" ]
categories = [ "Overview" ]
description = "Questa guida introduce il Gestore di pacchetti di Rhino (alias Yak)."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Che cos'è il Gestore pacchetti?"
type = "guides"
weight = 1
override_last_modified = "2020-11-12T12:17:36Z"

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

Il Gestore pacchetti di Rhino aiuta a trovare, installare e gestire le risorse nell'ecosistema di Rhino (Grasshopper compreso!). Attualmente supporta i plug-in di Rhino e Grasshopper, ma l'obiettivo è quello di includere in futuro elementi come script, materiali, viste, ecc.

{{< call-out "note" "Nota" >}}
Il Gestore pacchetti di Rhino era inizialmente indicato con il nome in codice "Yak". Il nome Yak è ancora utilizzato per lo strumento a linea di comando che crea e pubblica i pacchetti.
{{< /call-out >}}

Il Gestore pacchetti ha diversi obiettivi.

- Facilitare agli utenti la ricerca e gestione di plug-in e altro ancora.
- Aiutare gli sviluppatori e gli autori di contenuti riutilizzabili a condividere il loro lavoro.
- Fornire semplici strumenti di amministrazione del sistema.

Non volevamo scoprire l’acqua calda, quindi ci siamo ispirati a Linux e al mondo dello sviluppo software.
 Il sistema di gestione dei pacchetti può essere suddiviso in tre aree principali.


1. [Server.](#server)
2. [Integrazioni.](#integrations)
3. [Strumento a linea di comando.](#command-line-tool)

## Server

Il server dei pacchetti è il cuore del sistema. Una volta creati, i pacchetti vengono inviati al server per condividerli con gli altri.
 Il server mantiene i pacchetti organizzati per i client: lo strumento a linea di comando e Rhino (tramite integrazioni).


{{< call-out "note" "Nota" >}}
Oltre al server dei pacchetti pubblici (https://yak.rhino3d.com), il Gestore pacchetti supporta anche i [repository di pacchetti personal](../package-sources) basati su file-/cartella.
{{< /call-out >}}

## Integrazioni

Le integrazioni forniscono un accesso diretto all'ecosistema dei pacchetti direttamente in Rhino.
 Attualmente questo è stato fatto in due modi: "ripristino dei pacchetti" per Grasshopper e l'interfaccia utente del Gestore dei pacchetti.


### Ripristino dei pacchetti in Grasshopper

Il Gestore pacchetti di Rhino è stato integrato nella finestra di dialogo "Unrecognized Objects" di Grasshopper, fornendo la funzionalità di [ripristino dei pacchetti](../package-restore-in-grasshopper) .

 Quando si apre un nuovo file che contiene componenti di un plug-in non installato sul computer, l'utente ha la possibilità di controllare il server dei pacchetti per trovare i plug-in mancanti e installarli direttamente.



![Package restore for Grasshopper](/images/yak-gh-restore-guid.gif)

### Interfaccia utente del Gestore pacchetti

L'interfaccia utente del Gestore pacchetti è disponibile tramite il comando `_PackageManager`. Fornisce un'interfaccia in stile NuGet che consente agli utenti di cercare i pacchetti, installarli e vedere se sono disponibili aggiornamenti per i pacchetti attualmente installati.



![The package manager UI](/images/testpackagemanager-wip.jpg)

## Strumento a linea di comando

Lo strumento a linea di comando offre un'interfaccia di base ma con funzionalità complete.
È modellato su noti gestori di pacchetti specifici per il dominio, come `gem` di Ruby e `pip` di Python.
 Comunica con il server e si collega a Rhino Accounts per l'autenticazione.


In Windows, lo strumento si trova in `"C:\Program Files\Rhino {{< latest-rhino-version >}}System\yak.exe"`.
Su Mac esiste uno script, `"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"`.

Digitare `<path_to_yak> help` per iniziare.



## Argomenti correlati

- [Anatomia di un pacchetto](/guides/yak/the-anatomy-of-a-package/)
- [Il manifesto del pacchetto](/guides/yak/the-package-manifest/)
- [Riferimento CLI Yak](/guides/yak/yak-cli-reference)

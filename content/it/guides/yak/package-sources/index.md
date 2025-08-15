+++
aliases = ["/en/5/guides/yak/package-sources/", "/en/6/guides/yak/package-sources/", "/en/7/guides/yak/package-sources/", "/en/wip/guides/yak/package-sources/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Questa è una guida rapida alla configurazione dei repository di pacchetti personalizzati in Rhino."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Repository di pacchetti personalizzati"
type = "guides"
weight = 20
override_last_modified = "2021-02-12T11:31:53Z"

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

<!-- {{< call-out "note" "Nota" >}}
Questa funzione richiede la modifica delle impostazioni avanzate di Rhino!
{{< /call-out >}} -->

Di default, Rhino utilizza il server ufficiale dei pacchetti McNeel: https://yak.rhino3d.com. In aggiunta o come alternativa, è possibile configurare Rhino per utilizzare i propri repository di pacchetti.

Un repository di pacchetti personalizzati è semplicemente una cartella che contiene file di pacchetti .yak. La cartella può trovarsi sul computer locale o su un file server condiviso. È possibile configurare Rhino in modo che includa i pacchetti di questo repository nel Gestore pacchetti seguendo questi passaggi.


1. _Options > Advanced_ e cercare l’impostazione `Rhino.Options.PackageManager.Sources`.
1. Aggiungere il percorso completo della cartella del repository dei pacchetti, separandolo dal server dei pacchetti predefinito con punto e virgola, ad esempio `https://yak.rhino3d.com;C:\rhino_packages`.
1. Eseguire il comando `_PackageManager` e cercare uno dei pacchetti aggiunti al nuovo repository dei pacchetti.

Per ora supporta solo ciò che Directory.EnumerateFiles() supporta, che è costituito da percorsi regolari, unità mappate (Windows), percorsi UNC (Windows) e condivisioni montate (macOS)

### Suggerimenti per le cartelle condivise

In Windows, utilizzare il percorso UNC, ad esempio `server\share\packages`. Se la condivisione richiede le credenziali, navigare prima in `\\server` in Explorer, accedere e selezionare la casella "remember my credentials".

Su macOS la condivisione di file deve essere montata prima nel Finder tramite _Vai > Connetti al server..._ (<kbd>⌘</kbd> + <kbd>K</kbd>). Inserire l'indirizzo (`smb://server/share`) e fornire le credenziali, se necessario. Ora il percorso montato può essere usato come sorgente di pacchetti, cioè `/Volumes/share/packages`. Il montaggio non è persistente, quindi dovrà essere rimontato in futuro.

### Impostazioni amministratore

Vedere le opzioni in [Administrator-Enforced Settings](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#information/admin-enforced_settings.htm) per suggerimenti su come distribuire e applicare questa impostazione agli utenti Windows dell'organizzazione.

### Prestazioni

Rhino 8.15 include alcuni miglioramenti delle prestazioni per i repository privati dei pacchetti.

Lo strumento yak.exe ha un nuovo comando "cache" che, se eseguito all'interno della cartella dei pacchetti privati, crea un indice dei pacchetti disponibili. Quando il Gestore pacchetti rileva questo file di indice, lo userà _anziché_ passare per la directory. Questo riduce notevolmente il tempo di caricamento del Gestore pacchetti quando si ha a che fare con repository privati con molti pacchetti, pacchetti di grandi dimensioni o connessioni di rete lente.

```
$ cd X:\private\repo\directory
$ "C:\Program Files\Rhino 8\System\yak.exe" cache

Building cache for local package repository in X:\private\repo\directory

[...]
```

Assicurarsi di ricostruire la cache se i file dei pacchetti vengono aggiunti o rimossi dalla directory. Rimuovere i file _.cache*_ dalla directory per tornare al comportamento precedente.

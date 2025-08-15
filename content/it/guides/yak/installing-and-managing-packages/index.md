+++
aliases = ["/en/5/guides/yak/installing-and-managing-packages/", "/en/6/guides/yak/installing-and-managing-packages/", "/en/7/guides/yak/installing-and-managing-packages/", "/en/wip/guides/yak/installing-and-managing-packages/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "Questa è una guida passo passo per installare e disinstallare un pacchetto Yak usando la CLI."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Installazione e gestione dei pacchetti"
type = "guides"
weight = 30
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

{{< call-out "note" "Nota" >}}
Yak è multipiattaforma. Gli esempi che seguono sono per Windows.
Per Mac, sostituire il percorso dello strumento Yak CLI con<code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.

{{< /call-out >}}



## Installazione

Installare un pacchetto yak con lo strumento CLI è semplice.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" install marmoset

Downloading marmoset (1.0.0)...
Downloaded marmoset (1.0.0)
Installing marmoset (1.0.0)...
Successfully installed marmoset (1.0.0)
```

{{< call-out "note" "Nota" >}}
Rhino caricherà i nuovi pacchetti al prossimo avvio.
{{< /call-out >}}

È possibile indicare a Yak di installare una versione specifica.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" install marmoset 1.0.0

...
```

Il pacchetto viene installato in una cartella speciale, simile a quella di Grasshopper.
La cartella delle librerie, ma con una struttura di cartelle/file controllata da Yak.


## Disinstallazione

I pacchetti possono essere facilmente disinstallati utilizzando lo strumento Yak CLI.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" uninstall marmoset

marmoset successfully uninstalled
```

{{< call-out "note" "Nota" >}}
Rhino registrerà che il pacchetto è stato disinstallato al prossimo avvio.

{{< /call-out >}}


## Elenchi

In qualsiasi momento è possibile verificare quali pacchetti sono attualmente installati.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" list

marmoset (1.0.0)
```

## Argomenti correlati

- [Guide e tutorial su Yak](/guides/yak/)
- [Creazione di un pacchetto di plug-in per Grasshopper](/guides/yak/creating-a-grasshopper-plugin-package/)
- [Creazione di un pacchetto di plug-in per Rhino](/guides/yak/creating-a-rhino-plugin-package/)

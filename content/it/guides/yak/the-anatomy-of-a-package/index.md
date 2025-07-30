+++
aliases = ["/en/5/guides/yak/the-anatomy-of-a-package/", "/en/6/guides/yak/the-anatomy-of-a-package/", "/en/7/guides/yak/the-anatomy-of-a-package/", "/en/wip/guides/yak/the-anatomy-of-a-package/"]
authors = [ "will", "callum" ]
categories = [ "Fundamentals" ]
description = "Questa guida spiega la struttura di un pacchetto Yak."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "L'anatomia di un pacchetto"
type = "guides"
weight = 1

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

## Struttura del pacchetto

I pacchetti sono semplicemente archivi ZIP con estensione .yak. Prendiamo questo semplice esempio...

```
howler-0.4.0-any-any.yak
├── manifest.yml
├── Howler.rhp
├── Howler.rui
├── HowlerCommon.dll
├── HowlerGrasshopper.gha
└── misc/
    ├── README.md
    └── LICENSE.txt
```

### Una nota sul multitargeting .NET

Da Rhino 8, Yak supporta anche le applicazioni multitarget, in modo che il plug-in di Rhino possa essere eseguito sia in dotnet core che in dotnet framework.
Nota: il file `manifest.yml` deve ora trovarsi fuori dalla cartella del framework, anziché al suo interno.

```
howler-0.4.0-rh8-any.yak
├── manifest.yml
├── net48/
│  ├── Howler.rhp
│  ├── Howler.rui
│  ├── HowlerCommon.dll
│  ├── HowlerGrasshopper.gha
│  └── misc/
│     ├── README.md
│     └── LICENSE.txt
└── net7.0/
   ├── Howler.rhp
   ├── Howler.rui
   ├── HowlerCommon.dll
   ├── HowlerGrasshopper.gha
   └── misc/
      ├── README.md
      └── LICENSE.txt
```

## Requisiti

1. I pacchetti **devono** avere un file `manifest.yml` nella directory di primo livello. 
   I dettagli sul manifesto si trovano nella [Guida di riferimento al manifesto](../the-package-manifest).
1. Qualsiasi plug-in (file `.rhp`, `.gha`, `.ghpy`) **deve** trovarsi nella directory di primo livello o in una directory [multi-targeting](#a-note-on-net-multi-targeting), in modo che Rhino e Grasshopper possano trovarli e caricarli.
1. I numeri di versione dei pacchetti **devono** seguire [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) (ad esempio `1.1.0-beta`) o `System.Version`, ovvero lo standard a quattro cifre di Microsoft (ad esempio `1.2.3.4`). Si consiglia di usare il versionamento semantico, perché consente agli autori dei pacchetti di specificare le versioni precedenti al rilascio. Questi sono utili per effettuare test limitati, poiché di default viene installata l'ultima versione _stabile_.

## Distribuzioni

Per una singola versione del pacchetto è possibile caricare più "distribuzioni" per indirizzare diverse versioni e piattaforme di Rhino. Queste informazioni sono codificate in un "tag di distribuzione" che viene aggiunto al nome del file del pacchetto, ad esempio _example-1.0.0-rh7-win.yak_.

Il tag di distribuzione è composto da un identificatore di "app" e versione e da una piattaforma. Attualmente le uniche applicazioni supportate sono `rh` e `any` - Grasshopper viene fornito con Rhino, quindi non ha bisogno di un proprio identificatore. A meno che l'applicazione non sia `any', la versione dell'applicazione deve essere inclusa nella forma `_`. La versione minore è opzionale ed è utile se un plug-in si basa su una modifica dell'SDK apportata in una release del servizio. La piattaforma può essere `win`, `mac` o `any` (cioè multipiattaforma).

Ecco alcuni esempi.

* `rh7-win` - Rhino 7 per Windows >= 7.0
* `rh6_14-mac` - Rhino 6 per Mac >= 6.14
* `rh6_9-any` - Rhino 6 (entrambe le piattaforme) >= 6.9
* `any-any` - ammette qualsiasi cosa (comportamento esistente)

Quando si installano i pacchetti, il gestore dei pacchetti controlla se esiste una distribuzione compatibile per la versione richiesta. Solo le versioni dei pacchetti che hanno almeno una distribuzione compatibile verranno visualizzate quando il comando `_PackageManager` viene eseguito in Rhino 7 o superiore.

Il server aggiornato funziona perfettamente con i pacchetti esistenti e le versioni precedenti di Rhino. Le versioni preesistenti sul server (senza distribuzioni) saranno trattate secondo il tipo `any-any` durante l'installazione. Anche le nuove versioni di pacchetti che non includono un tag di distribuzione, ad esempio quelle create da versioni precedenti della CLI, saranno trattate come `any-any` al momento della pubblicazione.

## Passi successivi

Ora che abbiamo visto cosa c'è in un pacchetto, perché non creare un pacchetto?

* [Creare un pacchetto di Grasshopper](../pushing-a-package-to-the-server) del plug-in.
* [Creare un pacchetto di Rhino](../pushing-a-package-to-the-server) per tutti.
* [Crea un pacchetto multitarget](../creating-a-multi-targeted-rhino-plugin-package) per Rhino 8.

+++
aliases = ["/en/5/guides/yak/the-package-server/", "/en/6/guides/yak/the-package-server/", "/en/7/guides/yak/the-package-server/", "/en/wip/guides/yak/the-package-server/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Questa guida introduce il Gestore di pacchetti di Rhino, https://yak.rhino3d.com"
keywords = [ "yak" ]
sdk = [ "Yak" ]
title = "Il server dei pacchetti"
type = "guides"
weight = 1
override_last_modified = "2020-08-26T11:56:44Z"

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

Ospitiamo un server di pacchetti pubblico a disposizione di tutti. Non è necessario configurare nulla. Sia lo strumento Yak CLI che Rhino sanno già dove cercare.

I pacchetti condivisi sul server pubblico dei pacchetti possono essere scaricati e installati liberamente. Possono essere usati in modo gratuito o possono richiedere una licenza: consultare le guide [Cloud Zoo](/guides/rhinocommon/cloudzoo/cloudzoo-overview/) e [Zoo](/guides/rhinocommon/rhinocommon-zoo-plugins/) per i modi di implementare le licenze nel proprio plug-in usando i nostri strumenti.

Di seguito, sono riportate alcune informazioni utili sul nostro server di pacchetti.

## Autenticazione e autorizzazione

L'autenticazione, fornita da [Rhino Accounts](https://accounts.rhino3d.com), è necessaria solo per [pubblicare pacchetti](../pushing-a-package-to-the-server), non per scaricare/installare.

Una volta che l'autore ha pubblicato un pacchetto, solo lui può pubblicare versioni future utilizzando lo stesso nome del pacchetto.

{{< call-out "note" "Nota" >}}
La funzionalità per aggiungere "collaboratori" sarà aggiunta in futuro.
{{< /call-out >}}

## Convenzioni

Il server dei pacchetti ha alcune convenzioni che devono essere seguite.

### Assegnazione nome

I nomi dei pacchetti sono piuttosto rigidi. Sono ammessi solo lettere, numeri, trattini e trattini bassi, ad esempio `Hello_World` o `hello-world1`.

I nomi dei pacchetti adottano la distinzione fra maiuscole/minuscole usata nella prima versione caricata. I caricamenti futuri ignorano le maiuscole e le minuscole del nome del pacchetto e tutte le query non sono sensibili a maiuscole/minuscole.

### Versioni

I numeri di versione dei pacchetti devono seguire [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) (ad esempio `1.1.0-beta`) o `System.Version`, ovvero lo standard a quattro cifre di Microsoft (ad esempio `1.2.3.4`).

Si consiglia di usare il versionamento semantico, perché consente agli autori dei pacchetti di specificare le versioni precedenti al rilascio. Questi sono utili per effettuare test limitati, poiché di default viene installata l'ultima versione _stabile_.

I numeri di versione a quattro cifre sono stati aggiunti alla versione 0.8 (agosto 2019) per supportare i plug-in esistenti che utilizzano numeri di versione in stile `System.Version`. Non supportano i metadati di pre-release o di build.

#### Numeri di versione parziali e normalizzazione

Quando viene creato un pacchetto, notiamo che il numero di versione nel nome del file è diverso da quello in `manifest.yml`. Ciò è dovuto alla normalizzazione del numero di versione. Questo stesso processo avviene dietro le quinte del server dei pacchetti e serve a evitare ambiguità tra versioni semanticamente equivalenti.

Ci sono due casi in cui i numeri di versione possono essere semanticamente equivalenti.

* Versioni semantiche che differiscono solo nei metadati di compilazione[^1], cioè `1.0.0+build.1` e `1.0.0+build.2`.
* Una versione a quattro cifre e una versione semantica che sono identiche tranne che per la quarta cifra "0" (senza metadati di prerelease o build), ad esempio `1.2.3` e `1.2.3.0`.

La normalizzazione è diversa dall'espansione di numeri di versione parziali (ad esempio `1.0`). I numeri delle versioni parziali vengono espansi e memorizzati nella loro forma completa. Ad esempio, se si carica un pacchetto come `1.0`, questo verrà effettivamente salvato come `1.0.0`. Successivamente, qualsiasi richiesta (REST, CLI, ecc.) per la versione `1.0` sarà automaticamente reindirizzata.

[^1]: [I metadati di compilazione DEVONO essere ignorati quando si determina la precedenza della versione. Pertanto, due versioni che differiscono solo nei metadati di compilazione hanno la stessa precedenza"_.](https://semver.org/#spec-item-10)
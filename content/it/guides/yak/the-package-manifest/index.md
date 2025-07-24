+++
aliases = ["/en/5/guides/yak/the-package-manifest/", "/en/6/guides/yak/the-package-manifest/", "/en/7/guides/yak/the-package-manifest/", "/en/wip/guides/yak/the-package-manifest/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Cos'è un manifesto del pacchetto e cosa dovrebbe includere?"
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Il manifesto dei pacchetti"
type = "guides"
weight = 1
override_last_modified = "2021-07-21T10:09:56Z"

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

Ogni pacchetto dovrebbe avere un file manifesto contenente una specifica che può essere distillata nel database quando il pacchetto viene inviato al server. Il manifesto deve essere scritto in [YAML](http://www.yaml.org), seguendo la struttura dell'esempio seguente.

Il file manifesto deve essere chiamato `manifest.yml` e deve trovarsi nella radice del pacchetto. Lo strumento Yak CLI del [comando `build`](/guides/yak/yak-cli-reference#build) si occupa di questo aspetto.

Lo scopo del file manifesto è quello di aiutare a semplificare (e potenzialmente automatizzare) il processo di rilascio dei pacchetti, eliminando la necessità di moduli web per la pubblicazione dei pacchetti.

**Attributi richiesti**
 - [Name](#name)
 - [Version](#version)
 - [Authors](#authors)
 - [Description](#description)

**Attributi consigliati**
 <!-- - [`license`](#license) -->
 - [URL](#url)
 - [Keywords](#keywords)
 - [Icon](#icon)

<!-- ### Attributi opzionali
 - [`dependencies`](#dependencies) -->

## Esempio

Ecco un esempio di plug-in per Grasshopper.

``yaml
name: plankton
version: 0.3.4
authors:
  - Daniel Piker
  - Will Pearson
descrizione: >
  Plankton is a flexible and efficient library for handling n-gonal meshes.
  Plankton is written in C# and implements the halfedge data structure. The structure of the library is loosely based on Rhinocommon's mesh classes and was originally created for use within C#/VB scripting components in Grasshopper.
  
  
  
url: "https://github.com/meshmash/Plankton"
```

## Attributi richiesti

### Name

Il nome breve che descrive il pacchetto. Preferibilmente un solo mondo, anche se più parole possono essere separate da trattini o trattini bassi.

_**Nota:** Il nome del pacchetto può includere solo lettere, numeri, trattini e trattini bassi.

Nota 2:** I nomi dei pacchetti adottano la distinzione fra maiuscole/minuscole usata nella prima versione caricata. I caricamenti futuri ignorano le maiuscole e le minuscole del nome del pacchetto e tutte le query non sono sensibili a maiuscole/minuscole.

```yaml
name: plankton
```

### Version

_Since 0.8: four-digit version numbers allowed_
_Since 0.9: `$version` placeholder_

Il numero di versione assegnato al pacchetto.

I numeri di versione dei pacchetti **devono** seguire [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) (ad esempio `1.1.0-beta`) o `System.Version`, ovvero lo standard a quattro cifre di Microsoft (ad esempio `1.2.3.4`). Si consiglia di usare il versionamento semantico, perché consente agli autori dei pacchetti di specificare le versioni precedenti al rilascio. Questi sono utili per effettuare test limitati, poiché di default viene installata l'ultima versione _stabile_.

Per facilitare il processo di creazione, è possibile sostituire il numero di versione con `$version` - il numero di versione sarà dedotto dal contenuto del pacchetto e sostituito durante `yak build`.

```yaml
version: 0.3.4
```

### Authors

Un elenco degli autori del pacchetto.

```yaml
authors:
  - Daniel Piker
  # list additional package authors below
  - Will Pearson
```

### Description

Descrivere il pacchetto. La descrizione può essere breve o approfondita.

```yaml
description: This is an awesome package.
```

Se si vuole scrivere di più, si può usare lo [stile folded](http://www.yaml.org/spec/1.2/spec.html#id2796251) di YALM.

```yaml
description: >
  This is such an awesome package
  that I'm going to write a whole
  bunch of text describing it!

  This sentence will be on a new line.
```

<!-- Oppure, se si desidera preservare le linee nuove, utilizzare lo [stile letterale](https://yaml.org/spec/1.2-old/spec.html#id2795688).

```yaml
description: |
  Questa operazione imposta il primo punto della linea di riflessione speculare.
  Questa frase è (e sarà) su una nuova riga!
``` -->


## Attributi consigliati

<!-- ### License

La licenza di questo pacchetto. Non deve superare i 64 caratteri e deve essere uno degli identificatori standard [SPDX](spdx.org/licenses/).

```yaml
license: MIT
```

Se l'intenzione è quella di rendere il pacchetto open source, l'ideale sarebbe sceglierne uno che sia approvato dalla [OSI (Open Source Initiative)](opensource.org/licenses/alphabetical) . Le licenze approvate dall'OSI più comunemente utilizzate sono BSD-3-Clause e MIT. GitHub fornisce anche un selezionatore di licenze all'indirizzo http://choosealicense.com.

Questo dovrebbe essere solo il nome della licenza. Il testo completo della licenza deve essere incluso nel pacchetto come `LICENSE[.ext]` (al livello superiore) quando lo si costruisce.

Dovete specificare una licenza per il vostro pacchetto, in modo che le persone sappiano come possono usarlo e quali restrizioni avete posto. Non specificare una licenza significa che tutti i diritti sono riservati; altri non hanno il diritto di utilizzare il codice per alcuno scopo. -->

### URL

Una pagina web per il pacchetto. Può trattarsi di qualsiasi URL, ad esempio informazioni di contatto sull'autore, forum, tutorial o qualsiasi altra informazione sul plug-in.

<!-- NOTA: Sto pensando che, se si tratta di un repository github, c'è la possibilità di costruire direttamente da HEAD. -->

```yaml
url: "https://github.com/meshmash/Plankton"
```

### Keywords

Un elenco di parole chiave che aiutano gli utenti a trovare il pacchetto.

```yaml
keywords:
- one
- two
```

### Icon

Un file di icona nel pacchetto. Deve essere piccolo (ad esempio 64x64) e deve essere un PNG o un JPEG.

```yaml
icon: icon.png
```


<!-- ## Attributi opzionali -->

<!-- ### Dependencies

Un elenco di pacchetti da cui dipende questo pacchetto. Può anche includere specifiche di versione opzionali, sempre nel rispetto del Semantic Versioning.

Non è attualmente utilizzato, ma il server è in grado di memorizzare le dipendenze, quindi è necessario collegarlo!

```yaml
dependencies:
  - name: plankton
    spec: "< 0.4.0, >= 0.3.0"
  - name: package_without_spec
​``` -->


<!--## Alternativa(JSON)

​```json
{
  "name": "plankton",
  "version": "0.3.4",
  "author": [
    "Daniel Piker",
    "Will Pearson"
  ],
  "dependencies": [

  ],
  "description": "Plankton è una libreria flessibile ed efficiente per la gestione di maglie n-gonali. Plankton è scritto in linguaggio C# e implementa la struttura dati halfedge. La struttura della libreria si basa vagamente sulle classi mesh di Rhinocommon ed è stata originariamente creata per essere utilizzata all'interno di componenti di scripting C#/VB in Grasshopper",
  "license": "LGPL-3",
  "url": "https://github.com/meshmash/Plankton",
  "type": "gh-plugin"
}
``` -->

## Attributi obsoleti

### Icona URL

{{< call-out "warning" "Avviso" >}}
⚠️ Sostituito dall'attributo <a href="#icon" class="alert-link">icon</a>.
{{< /call-out >}}

Specificare un collegamento **diretto** ad un'icona che verrà usata dal Gestore pacchetti in Rhino. Deve essere piccolo (32x32 sarebbe l'ideale) e deve essere un file PNG o JPEG.

```yaml
icon_url: "https://example.com/path/to/icon.png"
```

## Argomenti correlati

- [Guide e tutorial su Yak](/guides/yak/)
- [Anatomia di un pacchetto](/guides/yak/the-anatomy-of-a-package/)
- [Riferimento CLI Yak](/guides/yak/yak-cli-reference)


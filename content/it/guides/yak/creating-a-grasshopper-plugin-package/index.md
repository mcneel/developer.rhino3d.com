+++
aliases = ["/en/5/guides/yak/creating-a-grasshopper-plugin-package/", "/en/6/guides/yak/creating-a-grasshopper-plugin-package/", "/en/7/guides/yak/creating-a-grasshopper-plugin-package/", "/en/wip/guides/yak/creating-a-grasshopper-plugin-package/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "Questa è una guida passo passo per la creazione di un plug-in per Grasshopper (.gha)."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Creazione di un pacchetto di plug-in per Grasshopper"
type = "guides"
weight = 10
override_last_modified = "2021-02-04T18:27:17Z"

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

Il [Gestore pacchetti](../yak/) è stato introdotto in Rhino 7. Rende più facile scoprire, installare e gestire i plug-in direttamente da Grasshopper. Questa guida descrive come creare un pacchetto da un plug-in di Grasshopper, che può essere pubblicato sul server dei pacchetti.

{{< call-out "note" "Nota" >}}
Il Gestore pacchetti è multipiattaforma. Gli esempi che seguono sono per Windows.
Per Mac, sostituire il percorso dello strumento Yak CLI con<code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.

{{< /call-out >}}



Per prima cosa, supponiamo di avere una cartella sul computer che contiene tutti i file che si desidera distribuire nel pacchetto.
 Qualcosa del tipo...

```commandline
C:\Users\Bozo\dist
├── Marmoset.gha
├── icon.png
└── misc\
    ├── README.md
    └── LICENSE.txt
```

{{< call-out "note" "Nota" >}}
Questo è solo un esempio. Gli unici file importanti sono Marmoset.gha e icon.png (faremo riferimento all'icona nel file manifest.yml più avanti).
{{< /call-out >}}

Utilizzeremo lo strumento Yak CLI per creare il pacchetto, quindi apriamo un prompt dei comandi e navighiamo nella directory di cui sopra.


```commandline
> cd C:\Users\Bozo\dist
```

Adesso, ci serve un file `manifest.yml`! Si può facilmente creare il proprio studiando la [Guida di riferimento ai manifesti](../the-package-manifest).
 In alternativa, possiamo usare il comando `spec` per creare un file con la struttura.
 In questo caso, ci occuperemo di quest'ultimo aspetto.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" spec

Inspecting content: Marmoset.gha

---
name: marmoset
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com


Saved to C:\Users\Bozo\dist\manifest.yml
```

Il comando `spec` esamina la directory corrente e, se presente, ricava informazioni utili dall'assembly `.gha`  e le usa per creare un `manifest.yml` con nome, versione, autori e contenuti preinseriti.

 Se non sono state aggiunte queste informazioni, verranno utilizzati dei segnaposto.


{{< call-out "note" "Nota" >}}
Il comando `spec` è utile per creare inizialmente il file manifest.yml.
 Una volta creato, è utile tenerlo con il progetto e aggiornarlo per ogni release.

{{< /call-out >}}

Quindi, aprire il file manifest l’[editor desiderato](https://code.visualstudio.com) e riempire gli spazi vuoti.


In seguito, otterremo qualcosa del genere...

```yaml
---
name: marmoset
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
icon: icon.png
keywords:
- mammal
```

Ora che abbiamo un file manifest, possiamo compilare il pacchetto!

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" build

Building package from contents of C:\Users\Bozo\dist

Found manifest.yml for package: marmoset (1.0.0)
Inspecting content: Marmoset.gha
Creating marmoset-1.0.0-rh6_18-any.yak

---
name: marmoset
version: 1.0.0
authors:
- Will Pearson
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: example.com
keywords:
- mammal
- guid:c9beedb9-07ec-4974-a0a2-44670ddb17e4

C:\Users\Bozo\dist\marmoset-1.0.0-rh6_18-any.yak
├── Marmoset.dll
├── Marmoset.gha
├── manifest.yml
├── misc\LICENSE.txt
└── misc\README.md
```

{{< call-out "note" "Nota" >}}
Il nome del file include un <a href="../the-anatomy-of-a-package#distributions" class="alert-link">"tag di distribuzione"</a> (in questo caso<code>rh6_18-any</code>). La prima parte, <code>rh6_18</code>, viene dedotta dalla versione di Grasshopper.dll o Rhinocommon.dll a cui si fa riferimento nel progetto del plug-in. La seconda parte,  <code>any</code>, si riferisce alla piattaforma a cui il plug-in è destinato. Per creare un pacchetto specifico per la piattaforma, eseguire nuovamente il comando<code>build</code> con l'argomento  <code>&#45;&#45;platform &lt;platform&gt;</code> dove <code>&lt;platform&gt;</code> può essere <code>win</code> o <code>mac</code>.
{{< /call-out >}}

{{< call-out "warning" "Avviso" >}}
Attualmente, se si pubblica un pacchetto con un tag di distribuzione <code>rh6*</code>, questo non sarà installabile per Rhino 7. Se il plug-in funziona anche in Rhino 7, occorre contrassegnarlo come compatibile copiando il file .yak, aggiornando la parte del nome del file relativa al tag di distribuzione (ad esempio<code>rh6_18</code> ➡ <code>rh7_0</code>) e <a href="../pushing-a-package-to-the-server" class="alert-link">inviando entrambi al server dei pacchetti</a>.
{{< /call-out >}}

{{< call-out "note" "Nota" >}}
Potremmo notare che il GUID del plug-in si trova tra le parole chiave.
 Per ulteriori informazioni sull'utilizzo di questa funzione, consultare la guida "Ripristino dei pacchetti in Grasshopper".
<a href="../package-restore-in-grasshopper" class="alert-link">
</a> 
{{< /call-out >}}

Ottimo lavoro! 🙌 Abbiamo appena creato un pacchetto per il plug-in di Grasshopper.

## Passi successivi

Ora che abbiamo creato un pacchetto, [possiamo inviarlo al server dei pacchetti](../pushing-a-package-to-the-server) per renderlo disponibile nel Gestore pacchetti.


## Argomenti correlati

- [Guide e tutorial sul Gestore pacchetti](/guides/yak/)
- [Creazione di un pacchetto di plug-in per Rhino](/guides/yak/creating-a-rhino-plugin-package/)
- [Ripristino dei pacchetti in Grasshopper](/guides/yak/package-restore-in-grasshopper/)
- [Grasshopper: Il tuo primo componente (Windows)](/guides/grasshopper/your-first-component-windows/)
- [Grasshopper: Il tuo primo componente (Mac)](/guides/grasshopper/your-first-component-mac/)

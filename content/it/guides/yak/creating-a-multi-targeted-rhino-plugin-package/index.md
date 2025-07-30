+++
aliases = ["/5/guides/yak/creating-a-rhino-plugin-package/", "/6/guides/yak/creating-a-rhino-plugin-package/", "/7/guides/yak/creating-a-rhino-plugin-package/", "/wip/guides/yak/creating-a-rhino-plugin-package/"]
authors = [ "callum" ]
categories = [ "Getting Started" ]
description = "Questa è una guida passo passo per inviare un pacchetto al server dei pacchetti."
keywords = [ "developer", "yak", "C#", "multi", "target", "C/C++", "plugin", "installer" ]
sdk = [ "Yak", "C#" ]
title = "Creazione di un pacchetto di plug-in per Rhino"
type = "guides"
weight = 10

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

Il [Gestore pacchetti](/guides/yak/) è stato introdotto in Rhino 7. Rende più facile scoprire, installare e gestire i plug-in direttamente da Rhino. Questa guida descrive come creare un pacchetto da un plug-in di Rhino, che può essere pubblicato sul server dei pacchetti.

{{< call-out "note" "Nota" >}}
Il Gestore pacchetti è multipiattaforma. Gli esempi che seguono sono per Windows.
Per Mac, sostituire il percorso dello strumento Yak CLI con<code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.

{{< /call-out >}}

Per prima cosa, supponiamo di avere una directory di compilazione sul computer che contiene tutti i file che si desidera distribuire nel pacchetto multitarget.
 Qualcosa di simile a quanto segue.

```commandline
C:\Users\Bozo\dist\
├───net48                            
│   │   icon.png                     
│   │   Tamarin.rhp                  
│   └───misc                         
│           License.txt              
│           README.md                
└───net7.0                           
    │   icon.png                     
    │   Tamarin.rhp                  
    └───misc                         
            License.txt              
            README.md                
```

{{< call-out "note" "Nota" >}}
Questo è solo un esempio. Gli unici file importanti sono Tamarin.rhp e icon.png (faremo riferimento all'icona nel file manifest.yml più avanti).
{{< /call-out >}}

Utilizzeremo lo strumento Yak CLI per creare il pacchetto, quindi apriamo un prompt dei comandi e navighiamo nella directory di cui sopra.


``` commandline
cd C:\Users\Bozo\dist\
```

Adesso, ci serve un file `manifest.yml`! Si può facilmente creare il proprio studiando la [Guida di riferimento ai manifesti](../the-package-manifest).
 In alternativa, possiamo usare il comando `spec` per creare un file con la struttura.
 In questo caso, ci occuperemo di quest'ultimo aspetto.

``` commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" spec

Inspecting content: Tamarin.rhp

---
name: tamarin
version: 1.0.0
authors:
- Park Ranger
description: An example RhinoCommon plug-in
url: https://example.com


Saved to C:\Users\Bozo\dist\manifest.yml
```

Il comando `spec` esamina la directory corrente e, se presente, ricava informazioni utili dall'assembly `.rhp` e le usa per creare un `manifest.yml` con nome, versione, descrizione e contenuti preinseriti.

 Se non sono state aggiunte queste informazioni, verranno utilizzati dei segnaposto.


L'ispettore dei plug-in di RhinoCommon estrae gli attributi dell'assieme impostati durante la creazione del plug-in. L'attributo `AssemblyInformationalVersion` viene usato per popolare il campo della versione, poiché questo attributo non è vincolato alle specifiche di versione a quattro cifre di Microsoft e può contenere una stringa di versione compatibile con SemVer.


 L'attributo `AssemblyVersion` è usato come ultima spiaggia.


{{< call-out "note" "Nota" >}}
Il comando `spec` è utile per creare inizialmente il file manifest.yml.
 Una volta creato, è utile tenerlo con il progetto e aggiornarlo per ogni release.

{{< /call-out >}}

Quindi, aprire il file manifest l’[editor desiderato](https://code.visualstudio.com) e riempire gli spazi vuoti.


In seguito, otterremo qualcosa del genere...

``` yaml
---
name: tamarin
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
icon: icon.png
keywords:
- something
```

Ora che abbiamo un file manifest, possiamo compilare il pacchetto!

``` commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" build

Building package from contents of C:\Users\Bozo\dist

Found manifest.yml for package: tamarin (1.0.0)
Inspecting content: Tamarin.rhp
Creating tamarin-1.0.0-rh8_0-any.yak

---
name: tamarin
version: 1.0.0
authors:
- Will Pearson
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
keywords:
- something
- guid:c9beedb9-07ec-4974-a0a2-44670ddb17e4

C:\Users\Bozo\dist\tamarin-1.0.0-rh8_0-any.yak
├── manifest.yml
├── net48/
│   ├── Tamarin.dll
│   ├── Tamarin.rhp
│   ├── icon.png
│   └── misc/
│       ├── License.txt
│       └── README.md
└── net7.0/
    ├── Tamarin.dll
    ├── Tamarin.rhp
    ├── icon.png
    └── misc/
        ├── License.txt
        └── README.md
```

{{< call-out "note" "Nota" >}}
Il nome del file include un <a href="../the-anatomy-of-a-package#distributions" class="alert-link">"tag di distribuzione"</a> (in questo caso<code>rh8_0-any</code>). La prima parte, <code>rh8_0</code>, viene dedotta dalla versione di Rhinocommon.dll o Rhino C++ SDK a cui si fa riferimento nel progetto del plug-in. La seconda parte,  <code>any</code>, si riferisce alla piattaforma a cui il plug-in è destinato. Per creare un pacchetto specifico per la piattaforma, eseguire nuovamente il comando<code>build</code> con l'argomento  <code>&#45;&#45;platform &lt;platform&gt;</code> dove <code>&lt;platform&gt;</code> può essere <code>win</code> o <code>mac</code>.
{{< /call-out >}}

{{< call-out "note" "Nota" >}}
Potremmo notare che il GUID del plug-in si trova tra le parole chiave.
 Per ulteriori informazioni sull'utilizzo di questa funzione, consultare la guida "Ripristino dei pacchetti in Grasshopper".
<a href="../package-restore-in-grasshopper" class="alert-link">
</a> 
{{< /call-out >}}

Ottimo lavoro! 🙌 Abbiamo appena creato un pacchetto multitarget per il plug-in di Rhino.

## Passi successivi

Ora che abbiamo creato un pacchetto, [possiamo inviarlo al server dei pacchetti](../pushing-a-package-to-the-server) per renderlo disponibile nel Gestore pacchetti.


## Argomenti correlati

- [Creazione di un pacchetto di plug-in per Grasshopper](/guides/yak/creating-a-grasshopper-plugin-package/)
- [RhinoCommon La tua prima app (Windows)](/guides/rhinocommon/your-first-plugin-windows)
- [RhinoCommon: La tua prima app (Mac)](/guides/rhinocommon/your-first-plugin-mac)
- [Creare il primo plug-in C/C++ per Rhino](/guides/cpp/your-first-plugin-windows/)

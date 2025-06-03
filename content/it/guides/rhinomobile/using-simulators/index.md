+++
aliases = ["/en/5/guides/rhinomobile/using-simulators/", "/en/6/guides/rhinomobile/using-simulators/", "/en/7/guides/rhinomobile/using-simulators/", "/en/wip/guides/rhinomobile/using-simulators/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "Questa guida riguarda le nozioni di base sull'uso di emulatori o simulatori per il debug delle applicazioni mobili."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Utilizzo dei simulatori"
type = "guides"
weight = 6

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/simulators_and_emulators"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac" ]
since = 5
until = 7

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true

[_build]
list = "never"
+++

{{< call-out "avviso" "RhinoMobile: Deprecato" >}}
RhinoMobile non è più supportato. La funzione I/O dei file 3dm di Rhino è ancora disponibile su iOS e Android tramite la [libreria rhino3dm](https://github.com/mcneel/rhino3dm).
{{< /call-out >}}
 
Android offre emulatori e iOS offre simulatori, ciascuno con i propri vantaggi e punti deboli.

## Emulatori Android

<img align="right" src="/images/using-simulators-01.png" width="121">

Gli emulatori Android sono una discreta approssimazione dei dispositivi reali, anche se le prestazioni possono variare leggermente. L'emulatore Android fa un buon lavoro di virtualizzazione delle configurazioni hardware e fallisce quando dovrebbe (è possibile limitare la quantità di memoria, ad esempio, in un modo non fattibile con il simulatore iOS). Detto questo, è comunque importante eseguire i test su dispositivi reali, soprattutto considerando le limitazioni funzionali dell'emulatore (niente multitouch, per esempio) e dell'ampia varietà di dispositivi Android presenti sul mercato, con le loro diverse configurazioni e capacità hardware. Una volta configurati correttamente, gli emulatori possono agevolare nel processo di sviluppo prima di effettuare i test sui dispositivi reali.

### Rotazione e multi-touch

Per ruotare gli emulatori, è possibile usare le seguenti combinazioni di tasti:

- <kbd>fn</kbd> + <kbd>Ctrl</kbd> + <kbd>F12</kbd> = Emulatore di rotazione (macOS)
- <kbd>Tasto sinistro - Ctrl</kbd> + <kbd>F12</kbd> = Emulatore di rotazione (Windows).

*Nota*: Non è possibile simulare più tocchi sull'emulatore Android.

### File System emulatore

Il modo migliore per accedere all'interno di un dispositivo Android o di un emulatore è utilizzare [Android Debug Bridge](http://developer.android.com/tools/help/adb.html) (ADB) che viene fornito con l'SDK Android come parte di Xamarin Toolkit. ADB è dotato di un'utilità di shell che consente di sfogliare il file system di Android come se si trattasse di un file system Linux standard, come in effetti è. L'esecuzione di adb shell su Mac è leggermente diversa da quella su Windows, ma ecco le basi.

**macOS**

Prima di avviare gli strumenti adb, assicuriamoci che SDK e NDK di Android facciano parte del nostro ambiente terminale bash. Aprire *.bash_profile* (nella cartella *~* o home) con un editor di testo affidabile (consigliamo [TextWrangler](http://www.barebones.com/products/textwrangler/) o [BBEdit](http://www.barebones.com/products/bbedit/)). Aggiungere le seguenti righe al profilo, se non sono già presenti:

```
export ANDROID_SDK="/Users/you/Library/Developer/Xamarin/android-sdk-mac_x86/"
export ANDROID_NDK="/Users/you/Library/Developer/Xamarin/android-ndk/android-ndk-r8d/"
export PATH="$PATH:$ANDROID_SDK/tools:$ANDROID_SDK/platform-tools:$ANDROID_NDK"
export _JAVA_OPTIONS="-Xmx1g"
```

Le prime due righe indicano all'ambiente bash dove cercare SDK e NDK di Android. L'opzione `_JAVA_OPTIONS="-Xmx1g"` aumenta la dimensione dell'heap che Xamarin Studio può utilizzare per i file binari nativi Java.

Salvare il profilo e avviare una finestra del Terminale. A questo punto dovrebbe essere possibile digitare adb shell. Se non si dispone di un emulatore in esecuzione o di un dispositivo collegato, si otterrà un errore: device not found response. In questo caso, significa che la shell adb è configurata. Collegare un dispositivo o lanciare un emulatore e riprovare il comando `adb shell`. Ora, il terminale dovrebbe mostrare quanto segue:

![adb shell](/images/using-simulators-02.png)

È possibile utilizzare molti comandi standard di Linux per spostarsi e gestire i file. Nota: esistono una serie di comandi speciali per abilitare/disabilitare i file dal dispositivo/emulatore. Consultare la [Documentazione di Android ADB](http://developer.android.com/tools/help/adb.html) per un pratico elenco. I dati di molte applicazioni sono memorizzati nella cartella *data/data/AppName/* .

**Windows**

Prima di lanciare gli strumenti adb, occorre assicurarsi che SDK e NDK di Android facciano parte delle variabili d’ambiente. Come procedere:

1. Aprire *System Controls* sul Pannello di controllo (*Start* > *Control Panel* > *System*).
1. Fare clic sul pulsante *Advanced systems settings* a sinistra.
1. Dovrebbe apparire la finestra *System Properties* . Fare clic sul pulsante *Environment Variables...* in Advanced Tab.
1. Nell’opzione *System variables* (il riquadro inferiore), scorrere l'elenco fino a visualizzare *Path* sotto la colonna Variable.
1. Fare clic su *Path* per evidenziarlo, quindi fare clic sul pulsante *Edit...* .
1. Aggiungeremo il nostro percorso ad adb, dove Xamarin ha installato android-sdk. Controllare che il cursore si trovi alla fine dell'ultima voce e digitare: *;C:\Users\you\AppData\Local\Android\android-sdk\platform-tools\* sostituendo *you* con il nome dell’account. Assicurarsi che non ci siano spazi in questo percorso. Se il percorso di android-sdk è personalizzato, sostituirlo con quello.
1. Fare clic su *OK* su tutto e *close the Control Panel* se è ancora aperto.

Aprire un prompt `cmd.exe`. Digitare quindi `adb shell`. Assicurarsi di avere un emulatore avviato o un dispositivo collegato; dovrebbe apparire uno strumento adb shell simile a quello mostrato sopra nelle istruzioni per Mac. È possibile utilizzare molti comandi standard di Linux per spostarsi e gestire i file. Nota: esistono una serie di comandi speciali per abilitare/disabilitare i file dal dispositivo/emulatore. Consultare la [Documentazione di Android ADB](http://developer.android.com/tools/help/adb.html) per un pratico elenco. I dati di molte applicazioni sono memorizzati nella cartella *data/data/AppName/* .

### Ripristino degli emulatori

Raramente è necessario ripristinare gli emulatori Android, poiché l'intera applicazione viene rimossa tra una build e l'altra. In caso di necessità di ripristino, il modo migliore è cancellare l'intero AVD e crearne uno nuovo. Aprire Android Virtual Device Manager (In Xamarin Studio, aprire *Tools* > *Open Android Emulator Manager...* Nella barra strumenti dell’applicazione), in *Android Virtual Devices Tab*, selezionate l'emulatore dall'elenco degli AVD e fare clic sul pulsante *Delete*.

## Simulatori iOS

<img align="right" src="/images/using-simulators-03.png" width="121">

I simulatori iOS sono un modo pratico per testare rapidamente l’applicazione con diverse dimensioni dello schermo, versioni di iOS e su diversi dispositivi. È possibile accedere al simulatore eseguendo l'applicazione in modalità Debug o Release e selezionando un simulatore e dei dispositivi dal menu a discesa a destra dei controlli Run e Configuration.

<div class="bs-callout bs-callout-danger">
  <h4>AVVISO</h4>
  <p>I simulatori NON sono un buon sostituto per i test sull'hardware iOS reale. Il comportamento/prestazioni dell'applicazione su un dispositivo possono variare in modo sostanziale rispetto al simulatore, specialmente con il codice OpenGL ES 2.0.</p>
</div>

Per installare versioni precedenti del Simulatore iOS, avviare Xcode e aprire *Xcode* > *Preferences* > *Downloads* > *Components* sezione > *click small download arrows* a destra della versione del Simulatore da installare.

### Rotazione e multi-touch

Le seguenti combinazioni di tasti possono essere utilizzate per ruotare la simulazione e simulare più tocchi:

- <kbd>Comando</kbd> + <kbd>tasti freccia Destra/Sinistra</kbd> = rotazione del simulatore.
- <kbd>opzione</kbd> + *move the cursor around* = simulazione di due tocchi.
- <kbd>opzione</kbd> + <kbd>Maiuscole</kbd> + *move the cursor around* = panoramica a due tocchi

### File System del simulatore

Il modo migliore per accedere al contenuto del filesystem del simulatore è utilizzare un terminale. In macOS, aprire una finestra di terminale e indicare:

`~/Developer/CoreSimulator/Devices/<code>/data/Containers/Data/Application/<app UDID number>/`

Nota: è possibile usare Tab per completare automaticamente i percorsi quando cambiamo directory, utile per completare automaticamente gli UDID delle applicazioni più lunghi.

In alternativa, è possibile utilizzare il Finder per navigare nella stessa cartella, ma è necessario modificare le preferenze del Finder per mostrare i file nascosti, se non lo si è già fatto.

Per ulteriori informazioni su dove memorizzare le risorse temporanee o persistenti, consultare la seguente documentazione di [Xamarin](http://docs.xamarin.com/guides/ios/application_fundamentals/working_with_the_file_system/).

### Ripristino dei simulatori

Spesso è necessario ripulire l'intero contenuto del simulatore tra una compilazione e l'altra, in particolare quelle in cui sono state modificate o rimosse risorse che possono essere memorizzate nella cache del simulatore. Per ricominciare da capo, è possibile ripristinare il simulatore alle "impostazioni di fabbrica" virtuali accedendo alla voce *iOS Simulator* > *Reset Content and Settings..* nel menu *Application* . Nota: questa operazione cancella tutti i dati dell'applicazione e ripristina il numero UDID dell'applicazione.

## Argomenti correlati

- [Test sui dispositivi](/guides/rhinomobile/testing-on-devices)

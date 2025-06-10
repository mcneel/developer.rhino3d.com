+++
aliases = ["/en/5/guides/rhinomobile/your-first-app-windows/", "/en/6/guides/rhinomobile/your-first-app-windows/", "/en/7/guides/rhinomobile/your-first-app-windows/", "/en/wip/guides/rhinomobile/your-first-app-windows/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "Questa guida illustra la procedura per la creazione della prima applicazione mobile utilizzando RhinoMobile e Visual Studio su Windows."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "La tua prima app (Windows)"
type = "guides"
weight = 5

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/hellorhinomobile"
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

Questa guida implica la consultazione della guida [Installazione degli strumenti (Windows)](/guides/rhinomobile/installing-tools-windows) e la corretta installazione di Xamarin Studio, Xcode e tutte le librerie necessarie.  Queste istruzioni implicano l'utilizzo di Visual Studio 2017 Professional.

## HelloRhinoMobile

Questa guida implica l'utilizzo di Visual Studio 2017 Professional, anche se il processo dovrebbe funzionare con Visual Studio 2013.

### Compilazione del codice boilerplate in Android

1. *Avviare Xamarin Studio* e aprire la soluzione *HelloRhinoMobile* .
1. Fare clic con il pulsante destro del mouse sul progetto *HelloRhino.Droid* e selezionare *Set As Startup Project* dal menu a discesa. Questa operazione rende *HelloRhino.iOS* il progetto attivo per la compilazione. HelloRhino.Touch è il progetto di destinazione Android. Il suffisso .Droid è una convenzione di denominazione di Mono che evita collisioni di spazi dei nomi con le principali librerie Android).
![hellorhinomobile solution](/images/your-first-app-windows-01.png)
1. Aprire *Android Emulator Manager*: Aprire *Tools* > *Open Android Emulator Manager*. Dovrebbe apparire una finestra chiamata *Android Virtual Device (AVD) Manager* . Fa parte dell'SDK di Android e risulterà familiare se sono già state eseguite procedure di sviluppo in Android. Qui si definiscono i dispositivi virtuali Android (AVD) che vengono eseguiti nell'emulatore.
![avd manager](/images/your-first-app-windows-02.png)
1. Gli AVD predefiniti sono troppo lenti per lo sviluppo; selezionare *Highlight each of the existing AVDs* e fare clic sul pulsante *Delete*.
1. Per creare una nuovo AVD: Fare clic sul pulsante *New*. Viene visualizzata la finestra di creazione di un nuovo ADV: Create new Android Virtual Device (AVD). Creare un nuovo AVD con i seguenti parametri: *AVD Name*: Nexus7-API17; *Device*: Nexus 7 (7.02“, 1200 x 1920:xhdpi); *Target*: Android 4.3 - API Level 18; *CPU/ABI*: Intel Atom (x86); *Skin*: Skin with dynamic hardware controls; *Front Camera*: Webcam0; *VM Heap*: 64 *Emulation Options*: Utilizzare la GPU host abilitata...
![create new avd](/images/your-first-app-windows-03.png)
1. Dovrebbe apparire il nuovo AVD nell'elenco. È stato appena creato il primo AVD. Ulteriori informazioni sulla creazione di emulatori sono disponibili nella [documentazione di Android sulla gestione dei dispositivi](http://developer.android.com/tools/devices/index.html). È possibile creare un numero illimitato di emulatori. I suggerimenti per l'uso dell'emulatore si trovano nella guida [Utilizzo dei simulatori](/guides/rhinomobile/using-simulators/] ).
1. *Chiudere* *AVD Manager*. Tornare a *Visual Studio*.
1. Fare clic sul pulsante *Info* sulla barra strumenti Xamarin.Android.
![info button](/images/your-first-app-windows-04.png)
1. Viene visualizzata la finestra *Android Device Logging*. Fare clic sul pulsante *Change Device*...
![select device window](/images/your-first-app-windows-05.png)
1. Viene visualizzata la finestra *Select Device*, che elenca tutti i dispositivi in esecuzione (emulatori e dispositivi fisici). Fare clic sul pulsante *Start emulator image*.
![start emulator](/images/your-first-app-windows-06.png)
1. Viene visualizzato lo stesso elenco di immagini AVD disponibili della finestra di gestione dei dispositivi virtuali Android (AVD). Selezionare *Nexus7-API18 AVD* creato in precedenza. Fare clic su *OK*.
![select device](/images/your-first-app-windows-07.png)
1. Se tutto è andato bene, dopo un breve periodo di avvio (è molto più veloce degli emulatori standard) dovrebbe avvisarsi Android. Il primo avvio potrebbe richiedere più tempo e si consiglia di lasciare questa finestra aperta durante la sessione di sviluppo. Una volta avviato Android, siamo pronti, sblocchiamo il dispositivo facendo scorrere il blocco verso destra. Ora possiamo inviare l'applicazione all'emulatore.
1. In *Solution Explorer*, *fare clic con il tasto destro del mouse* sul progetto *HelloRhino.Droid* e selezionare *Deploy*. HelloRhino.Droid verrà compilato, insieme alla dipendenza RhinoMobile.Droid. NOTA: La prima volta che si crea RhinoMobile.Droid, la libreria libopennurbs deve essere compilata. Questa operazione può richiedere fino a 20 minuti. Le build successive saranno di gran lunga molto più veloci.
1. Una volta distribuita l'applicazione sull'emulatore in esecuzione, è possibile eseguirla. In *Visual Studio*, fare clic sul pulsante *Start*. Se tutto va bene, dovrebbe apparire quanto segue.
![hellorhinomobile android](/images/your-first-app-windows-08.png)

*Ottimo lavoro!*  Abbiamo compilato un'app RhinoMobile per Android.

### Compilazione del codice boilerplate in iOS

PROSSIMAMENTE

## Argomenti collegati

- [Installazione degli strumenti (Windows)](/guides/rhinomobile/installing-tools-windows)
- [La tua prima app (Mac)](/guides/rhinomobile/your-first-app-mac)
- [Utilizzo dei simulatori](/guides/rhinomobile/using-simulators)
- [Test sui dispositivi](/guides/rhinomobile/testing-on-devices)
- [Gestione dei dispositivi (Documentazione Android)](http://developer.android.com/tools/devices/index.html)

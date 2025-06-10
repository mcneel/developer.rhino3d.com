+++
aliases = ["/en/5/guides/rhinomobile/your-first-app-mac/", "/en/6/guides/rhinomobile/your-first-app-mac/", "/en/7/guides/rhinomobile/your-first-app-mac/", "/en/wip/guides/rhinomobile/your-first-app-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "Questa guida illustra la procedura per la creazione della prima applicazione mobile utilizzando RhinoMobile e Visual Studio su Mac."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "La tua prima app (Mac)"
type = "guides"
weight = 4

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
 
Questa guida implica la consultazione della guida [Installazione degli strumenti (Mac)](/guides/rhinomobile/installing-tools-mac) e la corretta installazione di Xamarin Studio, Xcode e tutte le librerie necessarie.

## HelloRhinoMobile

Partiamo dal presupposto che non sia mai stato usato Xamarin Studio prima, quindi procederemo un passo alla volta.  Al momento della stesura di questo articolo, stiamo utilizzando Xamarin Studio 5.9.7.

### Compilazione del codice boilerplate in iOS

1. *Avviare Xamarin Studio* e aprire la soluzione *HelloRhinoMobile* .
1. *Fare clic con il tasto destro del mouse* sul progetto *HelloRhino.iOS* e selezionare *Set As Startup Project* dal menu a discesa. Questa operazione rende *HelloRhino.iOS* il progetto attivo per la compilazione. HelloRhino.Touch è il progetto di destinazione iOS.  I progetti HelloRhino.Touch utilizzano monotouch.dll, la versione precedente di Xamarin.iOS.
![hellorhinomobile solution](/images/your-first-app-mac-01.png)
1. Verificare che la build sia impostata su *Debug* e il dispositivo su *iPhone Simulator* > *iPhone iOS 5 iOS 9*. Fare clic sul pulsante *Play/Run*.
1. [Avviare una prova di Xamarin](http://docs.xamarin.com/guides/cross-platform/getting-started/beginning_a_xamarin_trial). La versione Xamarin Business Edition consente di attivare una prova di 30 giorni, necessaria per compilare e utilizzare RhinoMobile. È necessario [creare un accesso Xamarin](https://auth.xamarin.com/account/register). Se non è possibile avviare una prova dopo aver creato un login, non è un problema: Xamarin Studio chiederà di farlo durante la creazione dei progetti RhinoMobile. Potrebbe essere necessario ripulire il progetto e ricompilarlo se si verificano ancora errori di valutazione.
1. *Chiudere* quindi e *riavviare* Xamarin Studio.
1. Dalla schermata iniziale di Xamarin Studio, aprire nuovamente la soluzione *HelloRhinoMobile* .
1. Verificate che la versione completa di Xamarin Studio sia stata attivata. Andare su *Xamarin Studio* > *About Xamarin Studio* > *Show Details*. Scorrere verso il basso e assicurasi che *Xamarin.iOS* e *Xamarin.Android* siano impostati su *Trial Edition*.
1. Chiudere la finestra *About Xamarin Studio* .
1. Fare nuovamente clic sul pulsante *Play/Run* . Questa volta la compilazione dovrebbe concludersi senza errori. NOTA:  La prima volta che si crea RhinoMobile.iOS, occorre compilare la libreria libopennurbs. Le build successive saranno di gran lunga molto più veloci. Dopo aver caricato il bundle dell'applicazione nel simulatore, il risultato dovrebbe mostrare quanto segue:
![hellorhinomobile on ios](/images/your-first-app-mac-02.png)
1. Al termine dell’esempio HelloRhino sul simulatore iOS, fare clic sul pulsante *Stop* in Xamarin Studio per interrompere la sessione di debug.  E di seguito...

### Compilazione del codice boilerplate in Android

1. Fare clic con il pulsante destro del mouse sul progetto *HelloRhino.Droid* e selezionare *Set As Startup Project* dal menu a discesa. Come previsto, questo rende il progetto Android il progetto predefinito per la compilazione...
![hellorhinomobile solution with android](/images/your-first-app-mac-03.png)
1. *Verificare che la compilazione sia impostata su Debug.*  Stavolta, il menu a discesa per la selezione del dispositivo deve essere disabilitato. Ciò è dovuto al fatto che non è stato configurato un emulatore.
1. Fare clic sul pulsante *Play/Run* per avviare la build di debug *HelloRhino.Droid* . NOTA: La prima volta che si crea RhinoMobile.Droid, la libreria libopennurbs deve essere compilata. Questa operazione può richiedere fino a 20 minuti. Le build successive saranno di gran lunga molto più veloci.
1. Appare la finestra *Select Device**. Questa è la finestra in cui si indica all'SDK Android quale emulatore o dispositivo si desidera utilizzare per i test. Nessuno dei valori predefiniti va bene, quindi creiamo un emulatore più veloce.
1. Fare clic sul pulsante *Create Emulator*.
1. Dovrebbe avviarsi *Android Virtual Device Manager*. Fa parte dell'SDK di Android e risulterà familiare se sono già state eseguite procedure di sviluppo in Android. Qui si definiscono i dispositivi virtuali Android (AVD) che vengono eseguiti nell'emulatore.
1. Selezionare *Highlight each of the existing AVDs* e fare clic sul pulsante *Delete*. Questi AVD sono troppo lenti per lo sviluppo.
1. Per creare un nuovo AVD, fare clic sul pulsante *Create* . Viene visualizzata la finestra di creazione di un nuovo ADV: Create new Android Virtual Device (AVD). Creare un nuovo AVD con i seguenti parametri: *AVD Name*: Nexus7-API17-IntelHAXM; *Device*: Nexus 7; *Target*: Android 4.2.2 - API Level 17; *CPU/ABI*: Intel Atom (x86); *Front Camera*: Webcam0; *VM Heap*: 64 *Emulation Options*: Utilizzare la GPU host abilitata...
![create new android virtual device](/images/your-first-app-mac-04.png)
1. Dovrebbe apparire il nuovo AVD nell'elenco. È stato appena creato il primo AVD.  Ulteriori informazioni sulla creazione di emulatori sono disponibili nella [documentazione di Android sulla gestione dei dispositivi](http://developer.android.com/tools/devices/index.html). È possibile creare un numero illimitato di emulatori. I suggerimenti per l'uso dell'emulatore si trovano nella guida [Utilizzo dei simulatori](/guides/rhinomobile/using-simulators/] ).  Per il momento, *chiudere Android Virtual Device Manager* e tornate a Xamarin Studio.
1. Dovrebbe apparire nuovamente la finestra *Select Devide*, stavolta con il nuovo AVD nell'elenco. Selezionare l'AVD e fare clic sul pulsante *Start Emulator*. Se tutto è andato bene, dopo un breve periodo di avvio (è molto più veloce degli emulatori standard) dovrebbe avvisarsi Android. Il primo avvio potrebbe richiedere più tempo e si consiglia di lasciare questa finestra aperta durante la sessione di sviluppo. Una volta avviato Android, siamo pronti, sblocchiamo il dispositivo facendo scorrere il blocco verso destra.
1. Non chiudere l'emulatore Android. *Torniamo a Xamarin Studio*. Nella finestra *Select Device*, se l'etichetta *not started* non è ancora scomparsa, fare clic sul pulsante *Refresh*. Quando l'AVD appare in nero, con un carattere selezionabile, indica che Xamarin Studio è pronto per lanciare l'applicazione sull'emulatore.  Selezionare l'AVD e fare clic su *OK*.
1. Se tutto va bene, come su iOS, dovrebbe apparire quanto segue:
![hellorhino android](/images/your-first-app-mac-05.png)
1. Al termine della build HelloRhino.Droid, fare clic sul pulsante *Stop* in Xamarin Studio per interrompere la sessione di debug.

*Ottimo lavoro!*  Abbiamo compilato un'app RhinoMobile per due piattaforme con codice condiviso.

## Argomenti collegati

- [Installazione degli strumenti (Mac)](/guides/rhinomobile/installing-tools-mac)
- [La tua prima app (Windows)](/guides/rhinomobile/your-first-app-windows)
- [Utilizzo dei simulatori](/guides/rhinomobile/using-simulators)
- [Test sui dispositivi](/guides/rhinomobile/testing-on-devices)
- [Gestione dei dispositivi (Documentazione Android)](http://developer.android.com/tools/devices/index.html)

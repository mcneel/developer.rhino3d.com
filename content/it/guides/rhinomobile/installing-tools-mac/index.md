+++
aliases = ["/en/5/guides/rhinomobile/installing-tools-mac/", "/en/6/guides/rhinomobile/installing-tools-mac/", "/en/7/guides/rhinomobile/installing-tools-mac/", "/en/wip/guides/rhinomobile/installing-tools-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "Questa guida tratta tutti gli strumenti necessari per RhinoMobile su Mac."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
titolo = "Installazione degli strumenti (Mac)"
type = "guides"
weight = 2

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/getting-started"
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
 
Alla fine di questa guida, l’utente dovrebbe avere installato tutti gli strumenti necessari per creare, compilare ed eseguire il debug di applicazioni mobili C# utilizzando RhinoMobile in Xamarin Studio.

## Prerequisiti

Consigliamo di leggere la guida [Che cos'è RhinoMobile?](/guides/rhinomobile/what-is-rhinomobile/) .

Questa guida richiede l’utilizzo di:

- Un computer [Mac Apple](http://store.apple.com/) con [OS X Yosemite](https://www.apple.com/osx/) (10.10) o successivo.

## Installare Xcode

[Xcode](https://developer.apple.com/xcode/) è la piattaforma di sviluppo e IDE di Apple.

#### Procedura passo a passo

1. *[Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)* è gratuito su [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12).  Fare clic sul pulsante *View in Mac App Store*.
1. Fare clic sul pulsante *Get* > *Install App* sotto l'icona di Xcode.
1. Verrà richiesto il proprio [ID Apple](https://appleid.apple.com/) (necessario per scaricare le applicazioni su App Store).
1. Xcode prevede un download di grandi dimensioni, quasi 2,6 GB.  È possibile monitorare l'avanzamento del download in Launchpad.  Quando Xcode ha terminato il download e l'installazione, la cartella sarà */Applications* .
1. *Aprire* Xcode.  Al primo avvio, Xcode installerà alcuni componenti aggiuntivi.
1. *Chiudere* Xcode.

## Installare Xamarin

La piattaforma Xamarin è attualmente necessaria per compilare applicazioni RhinoMobile.  Per ulteriori informazioni, consultare la guida [Cosa sono Mono e Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/) .

#### Procedura passo a passo

1. *[Scaricare la piattaforma Xamarin](http://xamarin.com/download)*.
1. Xamarin utilizza un'applicazione Installer, che scarica e installa i componenti selezionati.  Una volta scaricato il file *XamarinInstaller.dmg*, fare doppio clic su di esso per montare l'immagine del disco.  Fare doppio clic sull’icona *Install Xamarin* per avviare il programma di installazione.
1. Per utilizzare la piattaforma Xamarin è necessario accettare il Contratto di licenza software Xamarin.
1. *Xamarin Platform* include questi elementi:
   - Xamarin Studio
   - Xamarin.Android[^1]
   - Xamarin.iOS[^2]
   - Xamarin.Mac[^3]
Controllare che *Xamarin.Android* e *Xamarin.iOS* siano selezionati e fare clic su *Continue*.
1. Se non è stato installato Xcode, Xamarin chiederà di farlo.  Consultare [Installare Xcode](#install-xcode) sopra.
1. L’installazione di Xamarin include: *Mono Framework*, *Xamarin Studio*, *Xamarin.Android* e *Xamarin.iOS*.  Fare clic su *Continue*.
1. Xamarin verrà quindi scaricato e installato.  A seconda dei prodotti selezionati al punto 4, questa operazione può richiedere un tempo.
1. Al termine dell'installazione, fare clic sul pulsante *Launch Xamarin Studio*.
1. *Xamarin Studio* -  è installato insieme a Mono Framework, Xamarin.Android e Xamarin.iOS.
1. Xamarin Studio è installato nella cartella */Applications* . Si consiglia di *trascinare l'icona nel Dock* per un uso futuro oppure, se è in esecuzione, fare clic con il tasto destro/Opzione sull'icona nel Dock e selezionare *Keep in Dock*.

## Aggiornare l'SDK Android

Una volta che Xamarin Studio è stato aggiornato, è necessario recuperare gli aggiornamenti per l'SDK Android.

#### Procedura passo a passo

1. In *Xamarin Studio*, aprire *Tools* > *Open Android SDK Manager...*.
1. Nella finestra *Android SDK Manager*, attendere che il gestore abbia finito di recuperare il manifest di aggiornamento.
1. A seconda della data di download degli strumenti di Xamarin, sarà necessario installare le API più recenti (21 al momento in cui scriviamo) e le ultime due (20 e 19) per la compatibilità con le versioni precedenti. Selezionare le opzioni accanto ai nomi e fare clic sul pulsante *Install N packages...*.
1. Si apre una finestra in cui è necessario accettare tutte le licenze di ciascun elemento prima di continuare. Se non si riesce a far funzionare il pulsante *Installa*, chiudere la finestra, riaprirla e fare clic singolarmente sul pulsante opzione Accept a sinistra finché non funziona.
![android sdk](/images/rhinomobile-installing-tools-mac-01.png)
1. *Nota:* Il download può richiedere tempo a seconda della connessione a Internet.

## Installare Intel HAXM

[Intel HAXM è il gestore Intel Hardware Acceleration Execution Manager](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/).  HAXM fornisce un motore con accelerazione hardware per gli emulatori Android x86. Senza HAXM, gli emulatori sono quasi inutilizzabili poiché le loro prestazioni sono molto inferiori. Tuttavia, con HAXM, gli emulatori x86 sono reattivi e utilizzabili. Non è veloce come un dispositivo vero e proprio, ma almeno è passabile. È disponibile per l'installazione tramite il gestore dell'SDK di Android, ma la versione è inefficace. Invece, è possibile ottenerlo dal link qui sopra.  HAXM non funziona in un ambiente virtualizzato, ad esempio in una macchina virtuale, quindi per sviluppare Android in una macchina virtuale Windows, occorre utilizzare un dispositivo.

#### Procedura passo a passo

1. Visitate il sito web [Intel Hardware Acceleration Execution](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/).
1. Trovare la sezione *macOS* della pagina.
1. Scaricare il file *haxm-macosx_rxx.zip*.  Prima di iniziare il download, potrebbe essere necessario accettare un contratto di licenza.
1. Decomprimere *haxm-macosx_rxx.zip*.
1. Montare il file *IntelHAXM_x.x.x.dmg* facendo doppio.
1. Installare HAXM facendo doppio clic sul file *IntelHAXM_x.x.x.mpkg*.

## Clonare RhinoCommon

RhinoMobile viene compilato usando il [ramo rhino3dmio di RhinoCommon](https://github.com/mcneel/rhinocommon/tree/rhino3dmio). È possibile scaricare RhinoCommon come zip o clonare il repository usando git (consigliato). Gli utenti che non utilizzano GitHub, possono usare un'applicazione [GitHub Mac Desktop](https://desktop.github.com/) per iniziare).

#### Procedura passo a passo

1. Decomprimere o clonare *[rhinocommon (ramo rhino3dmio)](https://github.com/mcneel/rhinocommon/tree/rhino3dmio)* in una cartella, ad esempio in */Users/you/Development/Repositories/rhinocommon*:
![clone rhinocommon](/images/rhinomobile-installing-tools-mac-02.png)
1. *[Scaricare openNURBS](http://www.rhino3d.com/download/opennurbs/5.0/commercial)*. RhinoMobile richiede l'SDK openNURBS C++.
1. Decomprimere openNURBS e posizionare il contenuto nella cartella *rhinocommon/c/opennurbs/* (la cartella contenente solo il file *readme.md*):
![opennurbs](/images/rhinomobile-installing-tools-mac-03.png)

## Clonare RhinoMobile

È necessario scaricare o clonare [RhinoMobile](http://github.com/mcneel/RhinoMobile) e i repository [RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples). Gli utenti che non utilizzano GitHub, possono usare un'applicazione [GitHub Mac Desktop](https://desktop.github.com/) per iniziare.

#### Procedura passo a passo

1. Decomprimere o clonare *[RhinoMobile](http://github.com/mcneel/RhinoMobile)* in una cartella *parallela a rhinocommon* (clonata sopra). Ad esempio, se *rhinocommon* si trova nella cartella     */Users/you/Development/Repositories/rhinocommon*, allora RhinoMobile dovrebbe trovarsi nella cartella */Users/you/Development/Repositories/RhinoMobile*:
![rhinomobile](/images/rhinomobile-installing-tools-mac-04.png)
1. Decomprimere o clonare *[RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples)* in una cartella *parallela a rhinocommon* e *RhinoMobile*:
![rhinomobilesamples](/images/rhinomobile-installing-tools-mac-05.png)

## Passi successivi

*Congratulazioni!*  Adesso sono disponibile tutti gli strumenti necessari per creare un'applicazione mobile che utilizzi RhinoMobile.  *E adesso?*

Consultare la guida [La tua prima app (Mac))](/guides/rhinomobile/your-first-app-mac) per le istruzioni sulla compilazione della prima applicazione.

## Argomenti correlati

- [Che cos'è RhinoMobile?](/guides/rhinomobile/what-is-rhinomobile/)
- [Che cos'è RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon/)
- [Cosa sono Mono e Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Installazione degli strumenti (Windows)](/guides/rhinomobile/installing-tools-windows/)
- [La tua prima app (Mac)](/guides/rhinomobile/your-first-app-mac)

**Note a piè di pagina**

[^1]: Xamarin.Android is used to build C# .NET applications for Android devices.

[^2]: Xamarin.iOS is used to build C# .NET applications for Apple iOS devices.

[^3]: Xamarin.Mac is Xamarin's proprietary closed-source toolkit build on the open-source MonoMac (aka Mono for macOS).  Xamarin.Mac provides a commercial license of Mono, bindings to additional frameworks, and the ability to create self-contained application bundles that do not require mono.  RhinoMobile does not currently use Xamarin.Mac.

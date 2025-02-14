+++
aliases = ["/en/5/guides/general/rhino-technology-overview/", "/en/6/guides/general/rhino-technology-overview/", "/en/7/guides/general/rhino-technology-overview/", "/en/wip/guides/general/rhino-technology-overview/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "Una sintesi dell'architettura tecnologica di Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Panoramica sulla tecnologia di Rhino"
type = "guides"
weight = 0
override_last_modified = "2018-12-05T14:59:06Z"

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

Rhinoceros è composto da molti livelli, scritti in molte lingue, tutti impilati l'uno sull'altro.  I livelli più importanti sono quelli inferiori, ma quelli superiori non devono assolutamente essere considerati superficiali...

![The Rhino Stack](/images/rhino-technology-overview-01.png)

Analizziamo ciascuno dei livelli in successione, iniziando dal basso con...

## Nozioni di base

### C++ Rhino Core

Il nucleo C++ Core di Rhino è il set di codice precedente e più ampio.  Utilizziamo MFC di Microsoft in alcuni punti, compreso il pacchetto SDK.  È qui che viene gestito il documento in runtime, dove esiste il codice di disegno della vista OpenGL e dove risiede il codice di geometria digitale scritto dai nostri matematici.  Molti dei comandi di Rhino si trovano qui.

La maggior parte dell’interfaccia utente, la linea di comando, il mainframe dell'applicazione, la barra di stato e le finestre di dialogo per molti comandi del nucleo di Rhino.

### openNURBS

openNURBS è un codice sorgente C++ gratuito, che consente di leggere e scrivere i file *3dm* di Rhino, a partire dalla versione 1.  openNURBS è stato il nostro primo progetto open-source.

Il codice viene compilato su Windows, macOS, Linux, iOS e Android.  È utilizzato in varie applicazioni di terze parti, come ArchiCAD, SolidWorks, Inventor, SketchUp e molti altri prodotti per leggere o scrivere direttamente i file *3dm* .

openNURBS è ciò che Rhino usa in modo nativo per leggere/scrivere i file *3dm* .  Questo toolkit viene rilasciato prima di Rhino, quindi qualsiasi prodotto, compresi quelli della concorrenza, può essere compatibile con i file *3dm* più recenti.  Non c'è alcuna differenza tra i file *3dm* che Rhino scrive e quelli di altre applicazioni che usano openNURBS per leggere e scrivere *3dm*.

Per ulteriori informazioni su openNURBS, consultare le guide [openNURBS](/guides/opennurbs/).

### C++ SDK

A tutto questo si aggiunge il nostro SDK C++, disponibile solo su Windows.

La compilazione con il pacchetto SDK C++ richiede una versione specifica di Microsoft Visual Studio e di Microsoft C-Runtime.  È necessario ricompilare per ogni versione principale di Rhino.

Praticamente, tutto ciò che Rhino può fare è esposto attraverso il pacchetto SDK C++. Alcuni comandi e funzioni non sono ancora stati esposti, ma questo pacchetto SDK è molto ampio e ricco.

Purtroppo, essendo strettamente legato al nucleo di Rhino, gli sviluppatori di plug-in devono ricompilare i loro plug-in per ogni release di Rhino.

Per ulteriori informazioni sul pacchetto SDK C++, consulta le [guide C/C++](/guides/cpp/).

## C++ Stack

La colonna di destra del diagramma di stack qui sopra è la parte C++ di Rhino.  Lo stack C++ ci consente, così come agli sviluppatori di plug-in di terze parti, di scrivere plug-in per Rhino utilizzando lo stesso pacchetto SDK C++ che usiamo per sviluppare Rhino.  Nota: non è possibile creare componenti di Grasshopper utilizzando il C++.

### Plug-in C++

Oltre al pacchetto SDK C++ ci sono i plug-in C++.  Molte funzionalità fornite con Rhino, tra cui alcuni comandi, I/O dei file e i motori di rendering, sono in realtà plug-in C++.  Esistono anche decine di plug-in C++ di terze parti, come [VisualARQ di Asuni](http://www.visualarq.com/), [RhinoCAM di MecSoft](https://mecsoft.com/rhinocam-software/)e [V-Ray di Chaos Software](https://www.chaosgroup.com/vray/rhino).

Per ulteriori informazioni sul pacchetto SDK C++, consulta le [guide C/C++](/guides/cpp/).

### RhinoScript

Uno dei plug-in C++ forniti con Rhino è [RhinoScript](/guides/rhinoscript/what-are-vbscript-rhinoscript/).  RhinoScript mostra un sottoinsieme del pacchetto SDK di Rhino davvero utile tramite VBScript, un linguaggio di scripting molto diffuso e popolare.  RhinoScript consente di accedere non solo a Rhino, ma a qualsiasi altro oggetto COM di Windows.

Per ulteriori informazioni, consulta le [guide RhinoScript](/guides/rhinoscript/) e in particolare la guida [Che cosa sono VBScript e RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript/) .

## .NET Stack

Il pacchetto SDK .NET è rappresentato qui in tre livelli:

- C API
- .NET Framework
- RhinoCommon
- Eto

### C API

Un'API C diretta include il pacchetto SDK C++, includendo Platform Invoke (P/Invoke) nel pacchetto SDK C++, formando un ponte tra il codice nativo C++ e i livelli gestiti .NET.

### .NET Framework

Microsoft sviluppa [.NET Framework](https://www.microsoft.com/net/framework).  .NET consente di scrivere plug-in in C#, F#, VB.NET e qualsiasi altro linguaggio che compili secondo Microsoft IL.

Il framework Microsoft .NET è fornito con Windows.

Nel prodotto Rhino per Mac è incorporato [Mono Runtime](https://www.mono-project.com), un'implementazione parziale multipiattaforma di .NET Runtime.

Per ulteriori informazioni su .NET e su come riporta lo sviluppo di Rhino, consulta la sezione [Cosa sono Mono e Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/).

### RhinoCommon

RhinoCommon è il nostro pacchetto SDK .NET per Rhino, compilato sulla base delle porzioni del framework .NET,  sono *comuni* sia su Windows che su macOS (tramite Mono).  RhinoCommon consente agli sviluppatori di eseguire codice .NET sia su Rhino per Windows che su Rhino per Mac.

Per ulteriori informazioni su RhinoCommon, consulta le [guide RhinoCommon](/guides/rhinocommon/) o più precisamente la guida [Che cos'è RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon) .

### Eto

Usando RhinoCommon, è possibile scrivere plug-in .NET che funzionano su Windows e Mac, tranne che per l'interfaccia utente.  Il team di Mono non ha clonato WinForms o WPF, quindi nessuna di queste tecnologie funziona su Mac.  Per risolvere questo problema, Rhino viene ora fornito con Eto.Forms.  Eto consente di scrivere un'interfaccia utente in C#, XAML o JSON e di utilizzarla su Windows e macOS.  In realtà, l'interfaccia utente scritta in Eto può essere eseguita anche su iOS, Android e Linux.

Per ulteriori informazioni su Eto, consulta [Eto.Forms on GitHub](https://github.com/picoe/Eto).

### Plug-in .NET

Esistono numerosi plug-in, sia interni che di terze parti, sviluppati in base a RhinoCommon.  [Grasshopper](http://www.grasshopper3d.com/), ad esempio, è un plug-in di RhinoCommon.  Alcuni comandi, mortori di rendering e plug-in di file IO di Rhino sono in realtà scritti come plug-in di RhinoCommon.  Con il passare del tempo, stiamo spostando un numero sempre maggiore di  funzionalità utili nei plug-in di RhinoCommon/.NET, in modo da condividere più codice tra le varie piattaforme.  Molti plug-in di terze parti di successo sono stati scritti utilizzando RhinoCommon e .NET, come [RhinoGold](http://www.tdmsolutions.com/) e [Matrix by GEMVision](http://www.stuller.com/matrix), e [Orca3D](http://orca3d.com/).

Per ulteriori informazioni su openNURBS, consulta le [guide openNURBS](/guides/rhinocommon/).

### Componenti di Grasshopper

Rhino viene ora fornito con Grasshopper, il nostro linguaggio di programmazione visuale per la progettazione algoritmica e parametrica.  Grasshopper è una piattaforma di sviluppo a sé stante, con [centinaia di componenti di Grasshopper creati da terzi](http://www.food4rhino.com/grasshopper-addons), per eseguire svariate operazioni, dalla [simulazione fisica](http://www.food4rhino.com/project/kangaroo), alla [creazione di interfacce utente personalizzate](http://www.food4rhino.com/project/human-ui), alla [programmazione e controllo robotico industriale](http://www.food4rhino.com/project/hal).

Per ulteriori informazioni su Grasshopper e, in particolare, sullo sviluppo di componenti Grasshopper, consulta le [guide di Grasshopper](/guides/grasshopper/).

### Scripting di Python

Uno dei plug-in .NET forniti con Rhino è RhinoPython.  Scritto usando [IronPython](http://ironpython.net/), un'implementazione .NET del runtime [python](https://www.python.org/) , RhinoPython espone l'intero pacchetto SDK RhinoCommon al linguaggio di scripting di Python.  Ciò significa che ogni volta che aggiungiamo una funzione a RhinoCommon, questa viene automaticamente visualizzata in RhinoPython.

Per ulteriori informazioni su RhinoPython, consulta le [guide su RhinoPython](/guides/rhinopython/).

## Argomenti collegati

- [Guide su C/C++](/guides/cpp/)
- [Guide su openNURBS](/guides/opennurbs/)
- [Guide su RhinoScript](/guides/rhinoscript/)
- [Microsoft .NET Framework (su microsoft.com)](https://www.microsoft.com/net/framework)
- [Che cos'è RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon)
- [Guide su RhinoCommon](/guides/rhinocommon/)
- [Cosa sono Mono e Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Progetto Mono](https://www.mono-project.com)
- [Eto.Forms on GitHub](https://github.com/picoe/Eto)
- [Guide su Grasshopper](/guides/grasshopper/)
- [Guide su RhinoPython](/guides/rhinopython/)

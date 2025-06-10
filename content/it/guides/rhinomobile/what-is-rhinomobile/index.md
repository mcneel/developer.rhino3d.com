+++
aliases = ["/en/5/guides/rhinomobile/what-is-rhinomobile/", "/en/6/guides/rhinomobile/what-is-rhinomobile/", "/en/7/guides/rhinomobile/what-is-rhinomobile/", "/en/wip/guides/rhinomobile/what-is-rhinomobile/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "Questa guida fornisce una panoramica su RhinoMobile."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Che cos'è RhinoMobile?"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile"
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
 
{{< image url="/images/rhinomobile-overview-01.png" alt="/images/rhinomobile-overview-01.png" class="float_right" width="325" >}}

RhinoMobile è una libreria C# .NET per lo sviluppo di applicazioni mobile 3D multipiattaforma. RhinoMobile, come RhinoCommon, si basa sul framework Xamarin Mono, un runtime .NET completamente funzionale che funziona su Android, iOS e macOS. RhinoMobile utilizza openNURBS (la libreria 3dm NURBS) e RhinoCommon (SDK .NET per Rhinoceros e Grasshopper) e gestisce la funzione IO dei file, il riconoscimento dei gesti e la visualizzazione 3D (OpenGL ES 2.0). Non si tratta interamente di RhinoCommon, ma di un sottoinsieme.

## Chi dovrebbe usarlo?

Chiunque sia interessato a sviluppare, creare prototipi o semplicemente sperimentare lo sviluppo mobile in 3D. Sebbene esistano ottime librerie 3D per i giochi mobili, nessuna si concentra sulla modellazione e progettazione 3D. RhinoMobile cerca di colmare questa lacuna. Per sviluppare in C# e puntare al maggior numero possibile di dispositivi, questa è la libreria perfetta. Non è necessaria alcuna esperienza di sviluppo mobile; basta avere familiarità con C# e .NET.

## Dove posso trovare aiuto?
{{< div class="clear_both" />}}
Sul [Forum di Rhino](http://discourse.mcneel.com/) e pubblicare i dubbi nella [Categoria sviluppatori di Rhino](http://discourse.mcneel.com/c/rhino-developer) e @menzionare lo sviluppatore @dan.

## Download e link

### Strumenti per sviluppatori

- [Piattaforma Xamarin](http://xamarin.com/download). L'utilizzo di RhinoMobile richiede una prova gratuita di 30 giorni della versione Business Edition. - Xamarin prevede prezzi ridotti per studenti e personale accademico.
- [Xcode](http://developer.apple.com/xcode/) su un Mac con OS X 10.8 (Mountain Lion) o superiore per la creazione di app iOS.
- [Visual Studio 2012](http://https//www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx) o superiore: Solo edizioni Non-Express (le estensioni di Xamarin richiedono versioni a pagamento).
- [Intel Hardware Accelerated Execution Manager](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/) fornisce l'accelerazione hardware per gli emulatori Android.

### Librerie ed esempi

- [RhinoCommon (ramo rhino3dmio)](https://github.com/mcneel/rhinocommon/tree/rhino3dmio): SDK del plug-in .NET per Rhino e Grasshopper.
- [openNURBS](http://www.rhino3d.com/opennurbs) Download: SDK C++ openNURBS.
- [RhinoMobile](http://github.com/mcneel/RhinoMobile) Scaricare o clonare la libreria RhinoMobile.
- [RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples) Scaricare o clonare alcuni progetti di esempio che utilizzano RhinoMobile.

## Domande frequenti

**RhinoMobile è gratuito?**

Sì.

**Posso vendere le app che sviluppo con RhinoMobile?**

Sì.

**Le app create con RhinoMobile funzioneranno sia sui computer Mac e Windows che su dispositivi mobili?**

No, con un'avvertenza: anche se non è stato ancora aggiunto alla libreria, abbiamo intenzione di supportare Windows Phone, che utilizza DirectX come pipeline di visualizzazione e può essere eseguito (con alcune limitazioni) come “Windows Store App” (aka: applicazione Metro UI).

**McNeel utilizza RhinoMobile per sviluppare iRhino 3D?**

Sì.

**Questo è tutto su RhinoCommon?**

No. RhinoMobile utilizza un sottoinsieme di RhinoCommon (rhino3dmio), i cui limiti sono definiti dal simbolo: MOBILE_BUILD. C'è molto da fare: Rhino.DocObjects, Rhino.Geometry, Rhino.FileIO... praticamente tutto ciò che serve per leggere, scrivere e disegnare in Rhino 3dm.

**Quindi probabilmente non posso eseguire una mesh o il comando Crea2D?**

No, non ancora. Mi dispiace. Considerando i limiti della CPU delle piattaforme mobili, probabilmente il consumo della batteria sarebbe totale.

## Passi successivi

Per iniziare a lavorare con RhinoMobile, occorre assicurarsi di avere installato tutti gli strumenti.  Leggi:

- [Installazione degli strumenti (Mac)](/guides/rhinomobile/installing-tools-mac/) o
- [Installazione degli strumenti (Windows)](/guides/rhinomobile/installing-tools-windows/)

## Argomenti correlati

- [Che cos'è RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon/)
- [Installazione degli strumenti (Mac)](/guides/rhinomobile/installing-tools-mac/)
- [Installazione degli strumenti (Windows)](/guides/rhinomobile/installing-tools-windows/)

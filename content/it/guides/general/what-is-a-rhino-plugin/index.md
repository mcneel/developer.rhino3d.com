+++
aliases = ["/en/5/guides/general/what-is-a-rhino-plugin/", "/en/6/guides/general/what-is-a-rhino-plugin/", "/en/7/guides/general/what-is-a-rhino-plugin/", "/en/wip/guides/general/what-is-a-rhino-plugin/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "Questa guida spiega cos'è un plug-in di Rhino e quali sono le sue forme."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Che cos’è un plug-in di Rhino?"
type = "guides"
weight = 3
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/developer/whatisarhinoplugin"
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


Un plug-in di Rhino è un modulo software che estende le funzionalità di Rhino o Grasshopper, aggiungendo comandi, funzionalità o capacità.  Un plug-in di Rhino è una libreria DLL (Dynamic Link Library).

Su Windows, un plug-in di Rhino compilato con [C/C++ SDK](/guides/cpp/what-is-the-cpp-sdk/) è una normale DLL che utilizza la DLL condivisa MFC.

Su Windows e Mac, un plug-in di Rhino compilato con [RhinoCommon SDK](/guides/rhinocommon/what-is-rhinocommon/) è un assembly .NET.

Esempi di plug-in di Rhino sono [Grasshopper](http://www.grasshopper3d.com), [Brazil](http://brazil.rhino3d.com/), [Flamingo](http://nxt.flamingo3d.com/)e [Bongo](http://bongo.rhino3d.com/).  Per ulteriori informazioni, visita [food4rhino.com](http://www.food4rhino.com/).


## Tipi di plug-in

Rhino supporta cinque diversi tipi di plug-in:

1. *Utility generale*: Un'utility di uso generale che può contenere uno o più comandi.
1. *Importazione file*: Importa i dati da altri formati di file in Rhino; può supportare più di un formato.
1. *Esportazione file*: Esporta i dati da Rhino ad altri formati di file; può supportare più di un formato.
1. *Rendering personalizzato*: Applica materiali, texture e luci a una scena per creare immagini renderizzate.
1. *Digitalizzazione 3D*: Si interfaccia con dispositivi di digitalizzazione 3D, come quelli prodotti da MicroScribe, Faro e Romer.

***Nota***: I plug-in di importazione file, esportazione file, rendering personalizzato e digitalizzazione 3D Digitalizing sono tutti strumenti specializzati migliorati del plug-in di utility generale.  Tutti i tipi di plug-in possono quindi contenere uno o più comandi.


## Compatibilità dei plug-in

Affinché Rhino riesca a caricare ed eseguire il plug-in, devono verificarsi determinate condizioni:

1. Il numero "RhinoSdkVersion" del plug-in deve corrispondere a "RhinoSdkVersion" di Rhino.
1. Il numero "RhinoSdkServiceRelease" di Rhino deve essere maggiore o uguale a "RhinoSdkServiceRelease" del plug-in.

Di tanto in tanto, apportiamo modifiche ai nostri SDK.  Quando lo facciamo, cambiamo il numero "RhinoSdkServiceRelease".  

Come sviluppatore di plug-in, è improbabile che si verifichi un problema con la prima condizione.  Ciò si verificherebbe, ad esempio, se un utente tentasse di caricare un plug-in creato per Rhino 6 in Rhino 4.

Tuttavia, è possibile che si verifichino occasionalmente problemi con la seconda condizione.  Se il  è stato compilato utilizzando l'SDK 6.2 (RhinoSdpluginkVersion.RhinoSdkServiceRelease) e un utente che utilizza Rhino 6.1 tenta di eseguirlo, riceverà un messaggio di errore e il plug-in si rifiuterà di essere caricato.  Se il cliente riceve questo messaggio, deve utilizzare l'ultima versione di Rhino (che in questo esempio potrebbe essere la 6.2 o superiore) e questo dovrebbe risolvere il problema.

## Argomenti collegati

- [Prerequisiti per gli sviluppatori](/guides/general/rhino-developer-prerequisites)

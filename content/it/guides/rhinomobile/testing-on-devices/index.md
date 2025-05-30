+++
aliases = ["/en/5/guides/rhinomobile/testing-on-devices/", "/en/6/guides/rhinomobile/testing-on-devices/", "/en/7/guides/rhinomobile/testing-on-devices/", "/en/wip/guides/rhinomobile/testing-on-devices/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "Questa guida illustra come impostare i dispositivi per testare le applicazioni mobili."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Testare i dispositivi"
type = "guides"
weight = 7

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/devices_and_testing"
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
 
## Dispositivi Android

Per eseguire il debug del codice su un dispositivo Android, è necessario attivare il debug USB sul dispositivo. Questa modalità rende il dispositivo più vulnerabile ai danni, quindi deve essere usata con cautela. È possibile attivarla e disattivarla tra le sessioni di sviluppo, se si desidera.

#### Dispositivi Android 4.0 (JellyBean - API 14) o superiori

Attivare l'opzione *USB Bebugger* in *Settings* > *Developer options*.

Per Android 4.2 e versioni successive, l’opzione *Developer options è nascosta* di default, seguire questi passi:

1. Sul dispositivo, aprire *Settings* > *About* <device>.
1. Toccare sette volte *Build number* per rendere disponibili le opzioni *Settings* > *Developer*.
1. Attivare quindi l'opzione *USB Debugging* .

In Windows, a volte è necessario impostare il dispositivo in modalità Camera (PTP) piuttosto che in modalità Media device (MTP). Per modificare questa modalità, procedere come segue:

1. Sul dispositivo, aprire *Settings* > *Storage* > *More options (…)* > *USB computer connection*.
1. Passare da *Media device (MTP)* a *Camera (PTP)*.

#### Dispositivi Kindle Fire

Sul dispositivo, selezionare *Settings* > *Security* e impostare Enable ADB su On.

Per ulteriori informazioni, consultare la [Documentazione per sviluppatori di Amazon](https://developer.amazon.com/sdk/fire/connect-adb.html#Connecting).

Si potrebbe anche voler attivare l'opzione Stay awake, per evitare che il dispositivo Android vada in stop mentre è collegato alla porta USB.

## Dispositivi iOS

I dispositivi iOS devono essere registrati con Apple prima di poterli utilizzare per lo sviluppo o il test. Questo processo viene denominato Device Provisioning. Seguire le indicazioni di Xamarin per preparare il dispositivo iOS.

Una volta che il dispositivo è stato fornito e collegato via USB, è possibile eseguire ed eseguire il debug dell'applicazione da Xamarin Studio o Visual Studio (tramite l'host Mac Build).

Per testare l’applicazione, occorre utilizzare i dispositivi. Le quattro aree in cui i dispositivi differiscono maggiormente dal simulatore sono:

1. Rete e connettività.
1. Servizi di localizzazione.
1. *Memoria.*
1. *OpenGL ES.*

Gli ultimi due sono i più critici per le applicazioni di RhinoMobile. Le mesh di grandi dimensioni nei file .3dm possono consumare molta memoria; il simulatore cercherà di richiamare gli avvisi OutOfMemory, ma non sarà coerente (o realistico) come l'esecuzione e il debug sul dispositivo. Infine, le chiamate OpenGL ES saranno interpretate in modo diverso sul simulatore rispetto al dispositivo. È possibile che il codice funzionante sul simulatore non funzioni su tutti i dispositivi.

## Argomenti correlati

- [Utilizzo dei simulatori](/guides/rhinomobile/using-simulators/)

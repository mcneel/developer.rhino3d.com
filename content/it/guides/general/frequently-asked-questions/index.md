+++
aliases = ["/en/5/guides/general/frequently-asked-questions/", "/en/6/guides/general/frequently-asked-questions/", "/en/7/guides/general/frequently-asked-questions/", "/en/wip/guides/general/frequently-asked-questions/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "Questa guida include un elenco di domande frequenti (FAQ)."
keywords = [ "developer", "rhino", "faq" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Domande frequenti (FAQ)"
type = "guides"
weight = 4
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptspage"
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


**Quale SDK è adatto a me?**

Tutto dipende da ciò che si vuole fare.  Se vuoi automatizzare attività ripetitive in Rhino, creare uno script di [Python](/guides/#rhinopython) può essere la soluzione.  Se vuoi scrivere un plug-in o un componente di Grasshopper completo, consigliamo di utilizzare il [pacchetto SDK di RhinoCommon](/guides/rhinocommon/what-is-rhinocommon/).  Se sei un utente esperto di C/C++, dovresti prendere in considerazione il pacchetto SDK nativo C/C++ (supportato solo da Rhino per Windows).

**È possibile scrivere plug-in che funzionino sia su Windows che su Mac?**

Sì... anche usando [lo stesso codice](/guides/rhinocommon/what-is-rhinocommon/).

**Cosa sono Mono e Xamarin?**

Mono è una versione open-source di .NET runtime di Microsoft, che funziona su Linux, macOS, iOS e Android.  Per ulteriori informazioni, consulta la guida [Cosa sono Mono e Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/) .

**Cosa sono le macro?**
Le macro sono stringhe di comandi e opzioni di comando di Rhino, che consentono di creare una sequenza automatizzata di operazioni.  Questa macro (sequenza) può essere ripetuta premendo un pulsante della barra degli strumenti o digitando un alias.

**Cosa sono gli script?**
Per le attività più complesse, le macro sono insufficienti.  Non hanno la capacità di eseguire calcoli complessi, di memorizzare e recuperare dati, di analizzarli e di prendere decisioni condizionate, né di entrare in profondità nei meccanismi interni di Rhino.  Per questo, è necessario un vero e proprio strumento di programmazione.  Il più semplice e accessibile è Python che include anche una versione della sintassi di RhinoScript.  Quando parliamo di script, di solito ci riferiamo a funzioni scritte con RhinoScript o Python.

**Cosa sono i plug-in?**
I plug-in sono strumenti ancora più sofisticati: si tratta di programmi informatici compilati che possono essere integrati in Rhino.  Questi possono andare da semplici funzioni di script a programmi complessi e completi per il rendering, l'animazione, la lavorazione, ecc.

+++
aliases = ["/en/5/guides/general/rhino-developer-prerequisites/", "/en/6/guides/general/rhino-developer-prerequisites/", "/en/7/guides/general/rhino-developer-prerequisites/", "/en/wip/guides/general/rhino-developer-prerequisites/"]
authors = [ "dan", "callum" ]
categories = [ "Getting Started" ]
description = "Questa guida descrive i principali requisiti per lo sviluppo di Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Prerequisiti per sviluppatori"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/learningresources"
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


Esistono alcuni prerequisiti necessari per lo sviluppo in Rhino.  In linea di massima, si possono suddividere in tre categorie, classificate in ordine crescente di difficoltà:

1. [Prerequisiti hardware.](#hardware)
1. [Prerequisiti software.](#software)
1. [Conoscenze di programmazione.](#programming-knowledge)

## Hardware

Se stai leggendo questa guida, probabilmente ha già un computer in grado di eseguire Rhino. In caso contrario, l’utilizzo di Rhino prevede alcuni [requisiti di sistema minimi](http://www.rhino3d.com/system_requirements/) che dovresti esaminare prima di acquistare qualsiasi hardware.  In generale, qualsiasi computer che supporta Rhino *dovrebbe* essere in grado di eseguire gli strumenti di sviluppo descritti nella sezione [Software](#software) .

Se sei un utente Windows e desideri sviluppare plug-in per Rhino per Mac, ti occorre un computer Mac di Apple.  Al contrario, se sei un utente di macOS e desideri sviluppare plug-in per Rhino per Windows, ti serve un computer in grado di eseguire Rhino per Windows (tuttavia, le macchine virtuali che eseguono Windows in macOS possono potenzialmente funzionare benissimo).


## Software

A seconda di ciò che si vuole fare, i prerequisiti del software variano.  Tuttavia, in generale, è necessario:

- [Rhinoceros.](http://www.rhino3d.com/download)
- Un editor di codice.  Esistono molte opzioni. Eccone alcune:
   - [Visual Studio per Windows](https://www.visualstudio.com): L'ambiente di sviluppo integrato (IDE) di punta di Microsoft per Windows.
   - [Visual Studio Code](https://code.visualstudio.com/): Il miglior editor multipiattaforma gratuito.

Consulta le [guide specifiche per i pacchetti SDK](/guides/) per i prerequisiti del software. Di solito, si trovano nelle guide *"Installare strumenti"* .

## Conoscenze di programmazione

L'acquisizione di conoscenze di programmazione è il prerequisito più impegnativo.  Tuttavia, imparare a programmare, anche provando un nuovo linguaggio, è divertente e stimolante.  Imparare a programmare con Rhino è un ottimo modo per iniziare.

### Imparare C# .NET

Se desideri scrivere plug-in con RhinoCommon, dovrai conoscere un linguaggio di programmazione compatibile con .NET, come C# o VB.  Consigliamo [C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)) (C Sharp) perché è moderno, sicuro e facile da imparare, e si può sviluppare in C# sia su Windows che su macOS.

*Guarda*...

- [Beginning C# Programming](http://shop.oreilly.com/product/0636920036036.do) di Eric Lippert - Pubblicato da O'Reilly Media.
- [C# Fundamentals for Absolute Beginners](https://www.microsoftvirtualacademy.com/en-US/training-courses/c-fundamentals-for-absolute-beginners-16169) su Microsoft's Virtual Academy.
- [C# Essential Training](http://www.lynda.com/C-tutorials/C-Essential-Training/188207-2.html) con David Gassner su Lynda.com.

*Leggi*...

- [Programming C# 5.0](http://shop.oreilly.com/product/0636920024064.do) di Ian Griffiths - Pubblicato da O'Reilly Media.
- [C# 5.0 in a Nutshell](http://shop.oreilly.com/product/0636920023951.do) di Joseph Albahari, Ben Albahari - Pubblicato da O'Reilly Media.

*Cosa fare*...

- [Controlla gli esempi](/samples/#rhinocommon) su questo sito.
- [Chiedi aiuto su Discourse.](http://discourse.mcneel.com/c/rhino-developer)

### Imparare C/C++

Per scrivere plug-in per Rhino usando il pacchetto SDK C/C++, devi innanzitutto imparare il linguaggio di programmazione [C++](https://en.wikipedia.org/wiki/C%2B%2B) .  Il linguaggio C/C++ è talvolta considerato un linguaggio di programmazione "avanzato".

*Guarda*...

- [C++: ](https://www.microsoftvirtualacademy.com/en-us/training-courses/c-a-general-purpose-language-and-library-jump-start-8251)[A General Purpose Language](https://www.microsoftvirtualacademy.com/en-us/training-courses/c-a-general-purpose-language-and-library-jump-start-8251) su Microsoft Virtual Academy.
- [C++ Essential Training](http://www.lynda.com/C-tutorials/C-Essential-Training/182674-2.html) con Bill Weinmann su Lynda.com.

*Leggi*...

- [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language) di Ian Kernighan e Dennis Ritchie.
- [Practical C++ Programming](http://shop.oreilly.com/product/9780596004194.do) di Steve Oualline - Pubblicato da O'Reilly Media.
- [C++ Primer Plus](http://www.amazon.com/Primer-Plus-Edition-Developers-Library/dp/0321776402) di Stephen Prata.

*Cosa fare*...

- [Controlla gli esempi](/samples/#cc) su questo sito.
- [Chiedi aiuto su Discourse.](http://discourse.mcneel.com/c/rhino-developer)

### Imparare Python

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) è un linguaggio di programmazione fantastico, incredibilmente flessibile, che consigliamo di aggiungere al tuo kit di strumenti.

*Guarda*...

- [Google's Python Class](https://developers.google.com/edu/python/) in Google for Education.
- [Up and Running with Python](http://www.lynda.com/Python-tutorials/Up-Running-Python/122467-2.html) con Joe Marini su Lynda.com.


*Leggi*...

- [Tutorial su Python](https://docs.python.org/2/tutorial/index.html)
- [RhinoPython Primer](http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101) di Skylar Tibbits, Arthur van der Harten, Steve Baer e David Rutten.
- [The Python Tutorial](https://docs.python.org/2/tutorial/index.html) di ThePython Software Foundation.
- [Learn Python the Hard Way](http://learnpythonthehardway.org/book/) di Zed A. Shaw. Si tratta di un libro per principianti nonostante il titolo.
- [Automate The Boring Stuff With Python](https://automatetheboringstuff.com/) di Al Sweigart.

*Cosa fare*...

- [Controlla gli esempi](/samples/#rhinopython) su questo sito.
- [Chiedi aiuto su Discourse.](http://discourse.mcneel.com/c/scripting)

### Imparare RhinoScript

RhinoScript è uno strumento di scripting basato sul linguaggio VBScript di Microsoft.  RhinoScript viene eseguito in Rhino per Windows.

*Leggi*...

- [RhinoScript Primer](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101) di David Rutten.
- [Microsoft VBScript User's Guide and Language Reference](https://msdn.microsoft.com/en-us/library/t0aew7h6(VS.85).aspx).

*Cosa fare*...

- [Controlla gli esempi](/samples/#rhinoscript) su questo sito.
- [Chiedi aiuto su Discourse.](http://discourse.mcneel.com/c/scripting)

### Ulteriori informazioni

- [Crafting Interpreters](https://craftinginterpreters.com/) di Robert Nystrom.
- [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) di Robert C. Martin.


## Argomenti collegati

- [Che cos'è un plug-in di Rhino?](/guides/general/what-is-a-rhino-plugin/)
- <a href="https://en.wikipedia.org/wiki/C_Sharp_(programming_language">C Sharp su Wikipedia.</a>
- [C++ su Wikipedia.](https://en.wikipedia.org/wiki/C%2B%2B)
- [Python su Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))

+++
aliases = ["/en/5/guides/compute/hops-component/", "/en/6/guides/compute/hops-component/", "/en/7/guides/compute/hops-component/", "/en/wip/guides/compute/hops-component/"]
authors = [ "steve", "scottd", "andy.payne" ]
categories = [ "Hops" ]
description = "Hops fügt Funktionen zu Grasshopper hinzu."
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "Die Hops-Komponente"
type = "guides"
weight = 3
override_last_modified = "2024-10-28T11:35:10Z"

[admin]
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

## Übersicht 


{{< image url="/images/hops-overview.png" alt="/images/hops-overview.png" class="image_center" width="100%" >}}

Hops ist eine Komponente für Grasshopper in Rhino 7 und Rhino 8 für Windows. Hops fügt Grasshopper externe **Funktionen** hinzu. Wie in anderen Programmiersprachen ermöglichen Ihnen die Funktionen:

* Komplexe Algorithmen zu vereinfachen, indem Sie die gleiche Funktion mehrfach verwenden.
* Doppelte Komponentenkombinationen zu eliminieren, indem Sie gemeinsame Kombinationen in einer Funktion unterbringen.
* Grasshopper-Dokumente mit anderen Teammitgliedern zu teilen.
* Grasshopper-Dokumente über mehrere Projekte hinweg zu definieren.
* Externe Dokumente parallel zu lösen, wodurch große Projekte beschleunigt werden können.
* Lang laufende Berechnungen asynchron auszuführen, ohne die Interaktionen zwischen Rhino und Grasshopper zu blockieren.

Hops-Funktionen werden als separate Grasshopper-Dokumente gespeichert. Die Hops-Komponente passt ihre Ein- und Ausgänge an die angegebene Funktion an. Während der Berechnung löst Hops die Definition in einem separaten Prozess und gibt die Ergebnisse dann an das aktuelle Dokument zurück.

## Verwendung von Hops <img src="/images/hops.svg" alt="Windows" class="guide_icon">

{{< vimeo 713836707 >}}

### Hops installieren:

Es gibt mehrere Möglichkeiten, Hops auf Ihrem Rechner zu installieren.
  1. [Hops installieren](rhino://package/search?name=hops) (Dadurch wird Rhino gestartet)
  1. Oder geben Sie `PaketManager` in die Rhino-Befehlszeile ein.
      1. Suchen Sie dann nach "Hops".
      1. Wählen Sie Hops, und dann Install

{{< image url="/images/hops-package-manager.png" alt="/images/hops-package-manager.png" class="image_center" width="100%" >}}

### Eine Hops-Funktion erstellen

Hops-Funktionen sind Grasshopper-Dokumente mit speziellen Eingaben und Ausgaben.

{{< image url="/images/hops_simple_function.png" alt="/images/hops_simple_function.png" class="image_center" width="100%" >}}

#### Definieren von Eingaben

Hops-Eingaben werden mit **Get Components** erstellt. Die verfügbaren Get Components in Grasshopper finden Sie unter den *Reiter Params > Gruppe Util*:

{{< image url="/images/hops_context_getters1.png" alt="/images/hops_context_getters1.png" class="image_center" width="65%" >}}

Der Name der Komponente wird für den Namen des Hops-Eingabeparameters verwendet. Im obigen Beispiel haben wir also drei Get Number Components mit den Namen A, B und C. Alle diese Get Components werden zu Eingabeparametern, wenn Hops die Definition kompiliert.

{{< image url="/images/hops_getter_inputs.png" alt="/images/hops_getter_inputs.png" class="image_center" width="80%" >}}

Jede Get Component hat ein Kontextmenü (Rechtsklick) mit verschiedenen Einstellungen.

{{< image url="/images/hops-get-component-menu.png" alt="/images/hops-get-component-menu.png" class="image_center" width="50%" >}}

* **Komponentenname** - Dies ist der Name, welcher der Eingabe der Hops-Komponente zugewiesen wird.
* **Prompt** - Diese Eingabe ist der Tooltip, der angezeigt wird, wenn Sie den Mauszeiger über diesen Parameter in der Hops-Komponente bewegen.
* **Enable/Disable** - Zum Aktivieren oder Deaktivieren dieser Komponente.
* **At Least** - Dies wird nur für den Grasshopper Player verwendet und definiert die minimale Anzahl der Werte, die für diese Eingabe akzeptiert werden.
* **At Most** - Dies definiert die maximale Anzahl der Werte, die für diese Eingabe akzeptiert werden (Standard = 1). Wenn dieser Wert auf 1 gesetzt ist, behandelt die Hops-Komponente diese Eingabe als *Item Access*. Ist dieser Wert jedoch größer als eins (oder nicht gesetzt), so behandelt Hops diese Eingabe als *List Access*.
* **Tree Access** - Hier wird festgelegt, ob ein Datenbaum in dieser Eingabe übergeben werden soll. Diese Eingabe wird nur in Hops verwendet, und wenn sie auf True gesetzt ist, dann ersetzt dieser Wert den oben eingestellten Wert *At Most*.
* **Minimum bzw. Maximum** - Diese optionalen Eingaben werden nur für den Grasshopper Player verwendet und klemmen numerische Eingaben an diese Begrenzung.
* **Presets** - Diese optionale Eingabe wird nur für den Grasshopper Player verwendet und ist nur bei den Get components *String*, *Integer* und *Number* zu finden. In diesem Dialogfeld können Sie eine Liste vordefinierter Optionen festlegen, die dem Benutzer als Aufforderungen in der Befehlszeile angezeigt werden.

#### Definieren von Ausgaben

Hops-Ausgaben können mit den Komponenten **Context Bake** oder **Context Print** definiert werden. Der Name des Eingabeparameters in einem der Kontextkomponenten wird als Name des Ausgabeparameters verwendet, wenn Hops berechnet wird.

{{< image url="/images/hops_getter_outputs.png" alt="/images/hops_getter_outputs.png" class="image_center" width="67%" >}}

### Die Hops-Komponente verwenden

1. Platzieren Sie die Grasshopper-Komponente *Reiter Params > Gruppe Util > Hops* auf der Arbeitsfläche.
1. Klicken Sie mit der rechten Maustaste auf die Komponente Hops und dann auf Path.
1. Wählen Sie eine Hops-Funktion. Hinweis: Dies kann eine Grasshopper-Definition auf Ihrem Computer, auf einem remoten Computer oder ein REST-Endpunkt sein.
1. Die Komponente zeigt die Eingaben und Ausgaben an.
1. Verwenden Sie die neue Komponente wie jede andere Grasshopper-Komponente.

{{< image url="/images/hops_multiplyadd.png" alt="/images/hops_multiplyadd.png" class="image_center" width="80%" >}}

### Ein Hinweis zu Hops für macOS-Anwender

Die Hops-Komponente arbeitet mit einer lokalen Instanz eines [Rhino.compute](https://developer.rhino3d.com/guides/compute/)-Servers zusammen, der in der Regel immer dann hochgefahren wird, wenn Sie Grasshopper starten. Allerdings läuft dieser Server nicht auf macOS, so dass Sie zwei weitere Optionen in Betracht ziehen müssen. Sie können:

1. einen REST-API-Aufruf an einen unter Windows laufenden Remote-Server tätigen.
1. einen REST-API-Aufruf an einen lokal laufenden Python ghhops_server tätigen.

Die erste Option (Aufruf eines Remote-Windows-Servers) erfordert einige Änderungen an den Einstellungen des remoten Rechners. Weitere Informationen zum Einrichten eines Remote-Servers finden Sie im Abschnitt [Konfiguration von Remote-Geräten](../hops-component/#remote-machine-configuration).

Die zweite Option (Aufruf eines lokalen Python-Servers) wird in dem Abschnitt [Aufruf eines CPython-Servers](../hops-component/#calling-a-cpython-server) ausführlicher behandelt.

## Hops-Einstellungen

### Anwendungseinstellungen

Die Hops-Einstellungen steuern, wie Hops auf Anwendungsebene läuft.  Sie sind über Grasshoppers Pulld-down-Menü File > Preferences > Solver verfügbar.

{{< image url="/images/hops-preferences.png" alt="/images/hops-preferences.png" class="image_center" width="60%" >}}

* **Hops - Compute Server URLs** - Listen die IP-Adresse oder URL aller Remote-Rechner oder Compute-Server auf.
* **API Key** - Der API-Schlüssel ist eine für Ihren Compute-Server und Ihre Anwendungen, welche die Compute API verwenden, geheime Zeichenfolge, z.B. `b8f91f04-3782-4f1c-87ac-8682f865bf1b`. Er ist optional, wenn Sie lokal testen, sollte aber in einer Produktionsumgebung verwendet werden. Auf diese Weise stellt der Compute-Server sicher, dass die API-Aufrufe nur von Ihren Anwendungen kommen. Sie können eine beliebige Zeichenfolge eingeben, die für Sie und Ihre Computeranwendungen eindeutig und geheim ist. Bewahren Sie diese an einem sicheren Ort auf.
* **Max Concurrent requests** - Wird verwendet, um die Anzahl der aktiven Anfragen in asynchronen Situationen zu begrenzen. Auf diese Weise stellt Hops nicht Tausende von Anfragen, während die ursprüngliche Anfrage bearbeitet wird.
* **Clear Hops Memory cache** - Löscht alle zuvor gespeicherten Lösungen aus dem Speicher.
* **Hide Rhino.Compute Console Window** - Hops wird im Hintergrund gelöst, aber das Einblenden des Fensters kann bei der Fehlersuche hilfreich sein.
* **Launch Local Rhino.Compute at Start** - Verwenden Sie dies für Remote-Maschinen, wenn Compute gestartet werden muss, bevor irgendwelche Anfragen gesendet werden.
* **Child Process Count** - Wird verwendet, um die Anzahl der Anfragen für zusätzliche parallele Prozesse zu begrenzen. Sie können dies auf die Anzahl der verfügbaren Kerne einstellen.
* **Funktionsquellen** - In diesem Abschnitt können Sie einen Pfad (entweder zu einem lokalen Verzeichnis oder einer URL) zu häufig verwendeten Hops-Funktionen hinzufügen (z.B. Grasshopper-Definitionen).

{{< call-out "note" "Anmerkung" >}}
Ab Rhino Version 7.13 werden die aktiven Modelltoleranzen (d.h. absolute Abstands- und Winkeltoleranzen) von Hops an die laufende Instanz von Rhino.compute als Teil der JSON-Anfrage übergeben.
{{< /call-out >}}

### Einstellungen der Komponenten

Klicken Sie mit der rechten Maustaste auf die Komponente Hops, um eine beliebige Anzahl von Optionen auszuwählen, die den Ablauf von Hops steuern.

{{< image url="/images/gh-hops-component-settings.png" alt="/images/gh-hops-component-settings.png" class="image_center" width="60%" >}}

* **Parallel Computing** - Jedes Element an einen neuen parallelen Knoten weiterleiten, falls verfügbar.
* **Path...** - Fügen Sie den Ort der zu lösenden GH-Funktion ein. Dies kann ein Dateiname, eine IP-Adresse oder eine URL sein.
* **Show Input: Path** - Macht den Pfad zu einer Eingabe für die Komponente, so dass der Pfad über die GH-Arbeitsfläche eingestellt werden kann.
* **Show Input: Enabled** - Zeigt eine Aktivierte Eingabe an, die die Komponente basierend auf einem booleschen Wert `True` oder `False` ausführt.
* **Asynchronous** - Die Benutzerschnittstelle wird nicht blockiert, während auf die Lösung eines entfernten Prozesses gewartet wird, und die Definition wird aktualisiert, wenn die Lösung abgeschlossen ist.
* **Cache In Memory** - Vorherige Lösungen werden im Speicher des lokalen Rechners abgelegt, um die Leistung zu verbessern, wenn dieselben Eingaben zuvor berechnet wurden.
* **Cache On Server** - Vorherige Lösungen werden auf dem Remote-Server gespeichert, um die Leistung zu verbessern. Derzeit nur bei Remote-Hops-Diensten verfügbar.

## Konfiguration der Remote-Maschine

Standardmäßig verwendet Hops Ihren lokalen Computer, um Grasshopper-Funktionen zu lösen. Es ist jedoch möglich, remote Computer (z. B. Server) oder virtuelle Maschinen einzurichten, die Hops aufrufen kann.

Um API-Aufrufe an einen entfernten Rechner zu tätigen, folgen Sie bitte diesem [Leitfaden zum Einrichten einer Produktionsumgebung](../deploy-to-iis/).

## Aufrufen eines CPython-Servers

Verwenden Sie Hops, um CPython aufzurufen. Einige Vorteile dieser Komponente:

1. Aufruf von CPython-Bibliotheken einschließlich Numpy und SciPy.
1. Verwendung einiger der neuesten für CPython verfügbaren Bibliotheken, wie TensorFlow.
1. Erstellung von wiederverwendbaren Funktionen und Parallelverarbeitung.
1. Unterstützt echte Debugging-Modi einschließlich Haltepunkte.
1. Volle Unterstützung von Visual Studio Code.
1. Andere Anwendungen und Dienste, die eine Python-API unterstützen, können die hier enthaltenen Bibliotheken ebenfalls nutzen.
1. Die Komponente Hops versucht zu erkennen, ob sich Eingaben und Ausgaben auf einem Server geändert haben, und baut sich selbst neu auf.  

### Erste Schritte mit CPython in Grasshopper

Dieses Python-Modul hilft Ihnen, Python-Funktionen (speziell CPython) zu erstellen und diese in Ihren Grasshopper-Skripten mit den neuen Hops-Komponenten zu verwenden.

**Erforderlich:**

1. [Rhino 7.4 oder neuer](https://www.rhino3d.com/download/)
1. [CPython 3.8 oder darüber](https://www.python.org/downloads/)
1. [Hops-Komponente für Grasshopper](https://developer.rhino3d.com/guides/grasshopper/hops-component/)
1. [Visual Studio Code](https://code.visualstudio.com/) wird sehr empfohlen

**Video-Tutorial:**

{{< vimeo 524032610 >}}

Dieses Modul kann seinen eingebauten Standard-HTTP-Server verwenden, um die Funktionen als Grasshopper-Komponenten bereitzustellen, oder als Middleware für eine [Flask](https://flask.palletsprojects.com/en/1.1.x/)-Anwendung fungieren. Es kann auch mit [Rhino.Inside.CPython](https://discourse.mcneel.com/t/rhino-inside-python/78987) zusammenarbeiten, um vollen Zugriff auf die [RhinoCommon API](https://developer.rhino3d.com/api/) zu gewähren.

## Häufig gestellte Fragen:

#### Kann man Hops-Funktionen innerhalb anderer Funktionen verschachteln?

Ja, es ist möglich, die Hops-Funktion innerhalb anderer Funktionen zu verschachteln. Dies wird _recursion_ genannt, und die Standardrekursionsgrenze ist auf 10 gesetzt.

#### Muss man für die Verwendung von Hops bezahlen?

Die Nutzung von Hops ist kostenlos.

#### Kann Hops mit Grasshopper Player verwendet werden, um Befehle zu erstellen?

Ja, Hops-Funktionen können die Komponenten Context Bake und Context Print verwenden, um Rhino-Befehle in Grasshopper Player zu erstellen.

#### Unterstützt Hops die Parallelverarbeitung?

Ja, Hops startet standardmäßig einen parallelen Prozess für jeden Zweig eines Datenstroms.

#### Welche Eingabe- und Ausgabetypen unterstützt Hops? (Es werden alle gängigen Typen unterstützt, fragen Sie nach, wenn Sie weitere benötigen)

Hops übergibt standardmäßige Grasshopper-Datentypen (Strings, Zahlen, Linien, etc...). Für andere Datentypen wie Bilder oder EPW-Wetterdateien verwenden Sie eine Zeichenkette für den Dateinamen, damit die externe Funktion auch die gleiche Datei einlesen kann.

#### Können Plug-in-Komponenten in Hops-Funktionen ausgeführt werden?

Ja, alle installierten Grasshopper-Plug-ins können innerhalb einer Hops-Funktion ausgeführt werden.

#### Kann dies für extrem lange Berechnungen innerhalb einer Funktion verwendet werden?

Ja, jede Hops-Komponente verfügt über eine Option zur asynchronen Lösung. Die Benutzeroberfläche wird nicht blockiert, während sie auf die Lösung eines entfernten Prozesses wartet, und die Definition wird aktualisiert, wenn die Lösung abgeschlossen ist. Hops wartet auf die Rückkehr aller Funktionsaufrufe, bevor es die Ausgaben an die nachgeschalteten Komponenten weitergibt.
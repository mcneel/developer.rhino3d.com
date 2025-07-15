+++
aliases = ["/en/5/guides/compute/what-is-hops/", "/en/6/guides/compute/what-is-hops/", "/en/7/guides/compute/what-is-hops/", "/en/wip/guides/compute/what-is-hops/"]
authors = [ "andy.payne" ]
categories = [ "Hops" ]
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "Was ist Hops"
type = "guides"
weight = 1
override_last_modified = "2022-03-21T17:57:18Z"

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

Mit Hops können Sie große, komplexe Definitionen vereinfachen. Grasshopper-Definitionen können umfangreich, kompliziert und repetitiv sein. Dieser unorganisierte Zustand wird manchmal [Spaghetti Code](https://www.pcmag.com/encyclopedia/term/spaghetti-code) genannt. Es gibt viele Faktoren, die zu Spaghetti-Code führen, wie z. B. Zeitmangel, die Fähigkeiten der Programmierer, die Komplexität des Projekts und die Einschränkungen der Programmiersprache. Wenn man versucht, ein großes Knäuel Grasshopper-Spaghetti zu entziffern, wird einem vor allem eins klar: Spaghetti-Code ist schwer zu lesen und zu verstehen. **Jetzt können Sie Hops verwenden, um schwer zu lesenden Spaghetti-Code zu vereinfachen.**

{{< image url="/images/hops_spaghetti_code_1.png" alt="/images/hops_spaghetti_code_1.png" class="image_center" width="100%" >}}

### Aufrufen von Funktionen in Grasshopper

In der Programmierung ist eine **Funktion** ein "in sich geschlossenes" Modul von Code, das Eingaben verarbeitet und ein Ergebnis zurückgibt. Grasshopper-Definitionen verarbeiten auch Eingaben und liefern Ergebnisse. Grasshopper wurde jedoch nicht im Hinblick auf Funktionen geschrieben. Cluster funktionieren zwar gewissermaßen, aber sie erleichtern es nicht, einfache Definitionen in komplexen Projekten wiederzuverwenden.

Zur Verbesserung wurde die Hops-Komponente hinzugefügt. Mit Hops können Sie separate Grasshopper-Definitionen als Funktionen verwenden. Der Schlüssel liegt darin, zu lernen, ein Problem in kleinere Unterdefinitionen aufzuteilen, die wir als Funktionen verwenden werden.

Stellen Sie sich vor, Sie müssen eine Schattenanalyse für einen parametrischen Turm durchführen, den Sie für New York City entwerfen. Dieses Problem könnte in vier kleinere Aufgaben unterteilt werden:
1. Umreisen des Bauplatzes
1. Erstellen der Gebäudehülle
1. Erstellen der Bodenplatten
1. Durchführung der Schattenanalyse der Gebäudehülle und der umliegenden Gebäude.

Sobald die Aufgaben klar definiert sind, können Sie festlegen, welche Informationen zur Durchführung jeder Aufgabe benötigt werden (also die Eingaben) und welche Daten am Ende zurückgegeben werden (also die Ausgaben). Für Schritt 1 würden die Eingaben, die für die Umreisung des Grundstücks benötigt werden, Grundstücksabstände und andere regulatorische Parameter aus den Bau- und Flächennutzungsvorschriften umfassen. Die Ausgabe für diese Funktion würde wahrscheinlich eine Polylinie enthalten, die die maximale Gebäudefläche im Erdgeschoss umreißt. 

Um die Parameter zu definieren, die in einer Grasshopper-Funktion verwendet werden, verwenden Sie die **Context-Get**-Komponenten für die Eingaben und die Komponente **Context Bake** für die Ausgaben. Diese finden Sie unter dem *Reiter Params > Gruppe Util*.

{{< image url="/images/hops_context_getters.png" alt="/images/hops_context_getters.png" class="image_center" width="92%" >}}

Nun, da wir die Eingaben und Ausgaben definiert haben, müssen wir nur noch die Schritte eingeben, um diese Eingaben in Ausgaben umzuwandeln. Nachdem eine Funktion vollständig als Grasshopper-Definition definiert wurde, kann sie von Hops aufgerufen werden. Hops legt die Eingaben und Ausgaben offen, die Sie in Ihrer Funktion in der enthaltenden Definition definiert haben. Im Gegensatz zu Clustern können Sie in Hops auf externe Dateien verweisen, die lokal oder auf einem Netzlaufwerk gespeichert werden können, was die gemeinsame Nutzung von Definitionen durch andere Teammitglieder und Mitarbeiter erleichtert.

Mit Hops können Sie die Lesbarkeit Ihres Codes verbessern, indem Sie komplexe Definitionen vereinfachen, Doppelarbeit reduzieren und Funktionen gemeinsam nutzen und wiederverwenden. Mit Hops können Sie Funktionen parallel lösen, was große Projekte beschleunigen kann. Es ermöglicht Ihnen auch, Funktionen asynchron zu lösen, ohne die Interaktionen zwischen Rhino und Grasshopper zu blockieren.

## Wie funktioniert das?

Hinter den Kulissen übergibt der Hops-Client die von Ihnen angegebene Grasshopper-Definition an eine Headless-Instanz des Rhino- und Grasshopper-Servers.  

### Der Hops Client

Ein Client ist ein Hardware-Gerät (d.h. ein Computer) oder eine Software-Anwendung, die über eine Netzverbindung eine digitale Ressource von einem Server anfordert. 

Die Hops-Komponente ist der Client. Sie finden sie unter dem *Reiter Parameter > Gruppe Util*, nachdem Sie Hops über den Paketmanager installiert haben. Hops benötigt den Pfad oder die URL für die Definition, die es lösen soll.
{{< image url="/images/hops_hello_world4.png" alt="/images/hops_hello_world4.png" class="image_center" width="55%" >}} 

Sobald Sie die Definition festgelegt haben, wird die Komponente aktualisiert, um die in der Definition festgelegten Eingaben und Ausgaben anzuzeigen.
{{< image url="/images/hops_io.png" alt="/images/hops_io.png" class="image_center" width="30%" >}} 

### Der Rhino-Server

Ein Server stellt seinen Clients über eine Netzwerkverbindung Daten zur Verfügung. 

Im Zusammenhang mit Hops ist der Server eine Headless-Version von Rhino und Grasshopper (d.h. er hat keine Benutzeroberfläche, mit der man interagieren kann). Der Headless-Rhino-Server löst die von Hops gesendete Grasshopper-Definition und gibt dann das Ergebnis zurück.
{{< image url="/images/hops_console.png" alt="/images/hops_console.png" class="image_center" width="100%" >}}

Mit Hops können Sie optional auf einen Rhino.Compute-Server verweisen, der auf einem anderen Computer läuft, um die Grasshopper-Definitionen zu lösen. Auf diese Weise können Sie einen Teil oder die gesamte Lösung auf eine externe Rechenressource auslagern.

## Erste Schritte

Um eine Funktion zu erstellen, die von Hops referenziert werden kann, müssen wir unsere Definition in drei verschiedene Abschnitte unterteilen: einen zur Definition unserer Eingabeparameter, einen weiteren zur Angabe der Ausgaben und schließlich einen Abschnitt, der die *Aktionen* der Funktion ausführt. Um mit Hops zu beginnen, können Sie entweder dem Video folgen oder die unten aufgeführten Schritte ausführen.

{{< vimeo 713836707 >}}

<br></br>
In diesem Beispiel wollen wir eine einfache Funktion erstellen, die den Namen eines Benutzers als Eingabe erhält (z. B. David) und eine Nachricht wie *"Hallo David!“* zurückgibt.

### Hops installieren

Bevor wir beginnen, müssen wir zunächst sicherstellen, dass Hops ordnungsgemäß installiert ist. Es gibt mehrere Möglichkeiten, Hops auf Ihrem Rechner zu installieren.
  1. [Hops installieren](rhino://package/search?name=hops) (Dadurch wird Rhino gestartet)
  1. Oder geben Sie `PaketManager` in die Rhino-Befehlszeile ein.
      1. Suchen Sie dann nach "Hops".
      1. Wählen Sie Hops, und dann Install

### Eine Eingabe erstellen

Nachdem wir nun Hops installiert haben, können wir mit der Definition unserer Funktion beginnen, indem wir einen Parameter für den Eingabetext erstellen. Unter dem *Reiter Params > Gruppe Util* sehen Sie eine Sammlung von Context-Getter-Komponenten. Platzieren Sie eine Komponente **Get-String** auf Ihrer Arbeitsfläche. Klicken Sie mit der rechten Maustaste auf die Mitte dieser Komponente und ändern Sie den Namen von `Get String` zu `Name`. Dieser Wert wird von Hops als Name für den Eingabeparameter verwendet.
{{< image url="/images/hops_getting_started_01.png" alt="/images/hops_getting_started_01.png" class="image_center" width="100%" >}}

Sie können diesem Parameter einen Standardwert zuweisen, indem Sie eine Zeichenfolge an den Eingang der Komponente Get String anschließen. Fügen Sie ein **Textfeld** auf der Arbeitsfläche hinzu. Diese finden Sie unter dem *Reiter Params > Gruppe Input*. Doppelklicken Sie auf das Textfeld und schreiben Sie Ihren Namen in das Eingabefeld.
{{< image url="/images/hops_getting_started_02.png" alt="/images/hops_getting_started_02.png" class="image_center" width="100%" >}}

### Die Funktion definieren

Nachdem wir nun einen Eingabeparameter erstellt haben, müssen wir eine Aktion mit diesem Wert durchführen. Erstellen wir eine Nachricht mit dem Namen, den Sie gerade in die Get-String-Komponente eingegeben haben. Fügen Sie eine **Concatenate-Komponente** auf der Arbeitsfläche hinzu. Diese finden Sie unter dem *Reiter Sets > Gruppe Text*. 

Die Komponente Concatenate fügt eine Reihe von Textfragmenten zu einer einzigen Nachricht zusammen. In unserem Fall wollen wir eine Zeichenkette erstellen, die `Hallo, Ihr Name hier!` lautet. 

Die Komponente Concatenate ist eine spezielle Art von Komponenten in Grasshopper, die eine zoombare Benutzeroberfläche (kurz ZUI) verwendet. Wenn Sie die Komponente vergrößern (mit dem Scrollrad der Maus), erscheint eine kleine Schaltfläche (+) auf der linken Seite der Komponente. Klicken Sie auf das (+) unter dem zweiten Parameter (B), um einen dritten Eingabeparameter hinzuzufügen.

Zoomen Sie nun heraus und fügen Sie ein weiteres Textfeld auf der Leinwand hinzu. Doppelklicken Sie darauf, um einen Text einzugeben. Geben Sie `Hallo` in das Feld ein (Achtung: nach dem Wort wird ein Leerzeichen eingefügt). Verbinden Sie dieses Panel mit der A-Eingabe der Komponente Concatenate.

Verbinden Sie anschließend den Ausgang der Komponente Get String mit dem B-Eingang der Komponente Concatenate. Fügen Sie schließlich ein weiteres Textfeld auf Ihrer Leinwand hinzu und geben Sie ein Ausrufezeichen `!` in das Feld ein. Verbinden Sie die Ausgabe dieses Textfeldes mit der C-Eingabe der Komponente Concatenate.

Verbinden Sie ein Textfeld mit der Ausgabe der Komponente Concatenate, um diese Nachricht anzuzeigen. Ihre Definition sollte nun ungefähr so aussehen.
{{< image url="/images/hops_getting_started_03.png" alt="/images/hops_getting_started_03.png" class="image_center" width="100%" >}}

### Eine Ausgabe erstellen

Der letzte Schritt bei der Erstellung unserer Hops-Funktion besteht darin, einen Ausgabeparameter zu erstellen, der die soeben erstellte Zeichenfolge zurückgibt. Gehen Sie zum *Reiter Params > Gruppe Util* und fügen Sie eine **Context-Print**-Komponente auf Ihrer Arbeitsfläche hinzu.

Klicken Sie mit der rechten Maustaste auf den Eingangsparameter (mit der Bezeichnung Tx) und ändern Sie den Namen in `Message` um. Den Namen können Sie frei wählen, aber dieser Wert wird von Hops für den Ausgabeparameter verwendet.

Speichern Sie nun Ihre Datei in einem Verzeichnis auf Ihrem Computer. Rufen Sie die Datei **Hello_World.gh** auf.
{{< image url="/images/hops_getting_started_04.png" alt="/images/hops_getting_started_04.png" class="image_center" width="100%" >}}

### Aufruf der Funktion

Wir haben jetzt eine mit Hops kompatible Funktion erstellt. Verwenden wir Hops, um diese Funktion aufzurufen. Beginnen Sie mit der Erstellung einer neuen Grasshopper-Definition (Ctrl + N).

Gehen Sie zum *Reiter Params > Gruppe Util* und fügen Sie eine **Hops**-Komponente auf Ihrer Arbeitsfläche hinzu. Klicken Sie mit der rechten Maustaste auf diese Komponente und wählen Sie den Menüpunkt **Pfad**. Wählen Sie im Pop-up-Dialog die gerade erstellte Datei **Hello_World.gh** aus. Wählen Sie **OK**, wenn der Pfad ausgewählt wurde.

An dieser Stelle sollte die Komponente Hops ihr Aussehen ändern und eine Eingabe `Name` und eine Ausgabe `Message` hinzufügen. Hops hat im Wesentlichen das von uns erstellte Beispiel Hello_World.gh gebündelt und an einen lokalen rhino.compute-Server gesendet, der die Berechnung durchführt und das Ergebnis zurückgibt.

Fügen Sie ein neues **Textfeld** auf der Arbeitsfläche hinzu und verbinden Sie es mit der Name-Eingabe der Komponente Hops. Doppelklicken Sie, um den Namen im Textfeld zu ändern. Fügen Sie der Ausgabe der Komponente Hops ein weiteres Textfeld hinzu, um das vom rhino.compute-Server zurückgegebene Ergebnis anzuzeigen.
{{< image url="/images/hops_getting_started_05.png" alt="/images/hops_getting_started_05.png" class="image_center" width="100%" >}}

Wir haben soeben beschrieben, wie Sie Ihre allererste Hops-Funktion erstellen und aufrufen. Wenn Sie mehr darüber erfahren möchten, wie Hops mit dem rhino.compute Server kommuniziert oder Ihre eigene Produktionsumgebung einrichten möchten, besuchen Sie die folgenden Links.

 ---

## Quick Links

 - [Wie funktioniert Hops?](../how-hops-works)
 - [Die Hops-Komponente](../hops-component)
 - [Einrichten einer Produktionsumgebung](../deploy-to-iis)

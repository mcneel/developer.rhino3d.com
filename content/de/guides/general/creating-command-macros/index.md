+++
aliases = ["/en/5/guides/general/creating-command-macros/", "/en/6/guides/general/creating-command-macros/", "/en/7/guides/general/creating-command-macros/", "/en/wip/guides/general/creating-command-macros/"]
authors = [ "scottd" ]
categories = [ "Overview" ]
description = "Ein Anfänger-Tutorial zur Erzeugung von Makros (Scripting von Rhino-Befehlen)"
keywords = [ "macro", "overview", "rhinoceros", "command" ]
languages = [ "Macro" ]
sdk = [ "Macro" ]
title = "Makros erstellen"
type = "guides"
weight = 1
override_last_modified = "2018-12-06T15:12:10Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/rhino/basicmacros"
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

Die Erstellung von Makros in Rhino dient dazu, viele Aufgaben zu automatisieren, Ihre Befehle zu personalisieren und Ihren Workflow zu verbessern.

Die Verwendung des Begriffs Scripting mag hier eventuell einige Verwirrung stiften.  Generell bezeichnet er den Prozess des Schreibens sowohl von Makros (darum geht es in dieser Sektion) als auch anspruchsvollerer Skripts in [RhinoScript](/guides/rhinoscript/), [Rhino.Python](/guides/rhinopython/) oder anderen Programmiersprachen.  

Dabei handelt es sich jedoch um zwei verschiedene Dinge. Das Schreiben von Funktionen in Rhinoscript und anderen Programmiersprachen ist weitaus komplexer als das Erstellen von Makros und erfordert echte Programmierkenntnisse.  Dies wird hier nicht behandelt.

Mit dem Begriff "Makro" werden hier ausschließlich das Zusammensetzen von gewöhnlichen Rhino-Befehlen und die Optionen zur Erzeugung einer automatisierten Funktion bezeichnet.  Dies ist Scripting in seiner einfachsten Form und für jeden normalen Rhino-Nutzer leicht anwendbar, selbst wenn keine Programmierkenntnisse vorliegen.  Alles, was Sie dafür benötigen, ist ein grundlegendes Verständnis der Rhino-Befehle und ihrer Struktur sowie etwas logisches Denken und die Bereitschaft, sich auf kleine Experimente und das Debuggen einzulassen.

#### Verwendete Tools
1. Ihr Verstand.

2. Die Rhino-Hilfedatei - darin sind alle Rhino-Befehle samt Unterbefehlen aufgeführt. Dies ist Ihre wichtigste Referenz.

3. Der Rhino-**MakroEditor**, mit dem Sie Ihre Makros einfach ausführen und Debuggen können.


## Sie haben bereits ein wenig Erfahrung mit Makros ...
Als Rhino-Anwender nutzen Sie bereits Makros, selbst wenn Ihnen dies nicht bewusst ist.  Viele der Befehle in Rhino sind bereits für Sie "makroisiert". Wenn Sie eine Schaltfläche der Werkzeugleiste klicken oder einen Befehl aus dem Menü ausführen, handelt es sich oft um ein voreingestelltes Makro.  Klicken Sie beispielsweise mit Umschalttaste und rechter Maustaste auf die Schaltfläche **Gerade extrudieren**:

![Extrude](/images/extrudecrvbuttoneditor.gif)

Dies ist ein Beispiel für das einfachste Makro, bei dem eine Reihe Optionen in einen einzigen Befehl gesteckt werden, sodass Sie nicht jeden einzelnen jedes Mal spezifizieren müssen, wenn Sie ihn verwenden.  **KurveExtrudieren** hat mehrere Schaltflächen mit voreingestellten Optionen, **Verjüngen, EntlangKurve, AnPunkt, Deckfläche=Ja** (solid) usw.  Sehen Sie sich die Makros unter allen **KurveExtrudieren**-Schaltflächen an, um zu sehen, wie sie aufgebaut sind.

In gewisser Weise funktionieren diese, als würden Sie die einzelnen Optionen nacheinander anklicken oder in der Eingabeaufforderung eingeben.  Mehr sind Makros eigentlich auch nicht: eine Ansammlung von Anweisungen zur Wiederholung einer Abfolge von Befehlen, die Sie ansonsten einen nach dem anderen manuell eingeben müssten.

Das Scripting mit Optionen eines einzelnen Befehls kann außerdem mit der Eingabe von Daten (z.B. Koordinaten oder andere numerische Daten) kombiniert werden. Es können außerdem mehrere Befehle in einer Reihe zusammengeschrieben werden, für eine automatische Sequenz zur Bearbeitung oder Erstellung von Objekten.

**Hinweis:** Warum die _Understriche?  Diese teilen Rhino mit, dass ein englischer Befehl folgt (unabhängig von der Sprachversion Ihres Programms), so dass Ihr Makro universell ist.  Falls Sie eine englische Version von Rhino besitzen und Ihre Makros nur in dieser laufen sollen, können Sie die Unterstriche weg lassen. Es wird weiter keine Auswirkungen haben.  Und wozu das Ausrufezeichen (!)?  Damit wird jeder eventuell bereits laufende Befehl aus Sicherheitsgründen beendet.

## Erste Schritte

Wenn Sie beispielsweise mehrere Würfel mit 10 cm Kantenlänge mit dem Zentrum der Unterseite auf einem gewünschten Punkt platzieren möchten, muss der entsprechende Punkt entweder durch einen Mausklick oder durch Eingabe der Koordinaten über die Tastatur bestimmt werden.

Sie könnten dafür den Standardbefehl Quader verwenden (**Ecke zu Ecke + Höhe**), wodurch jedoch standardmäßig der Einfügungspunkt auf die erste Ecke des Quaders gesetzt wird.  Für unseren Fall ist es einfacher, den Befehl Quader, Zentrum zu verwenden.   Dies ist eigentlich auch nur der Quader-Befehl unter Verwendung der Option Zentrum, sodass Sie ihn in Ihrem Makro aktivieren müssen.

Öffnen Sie den **MakroEditor** und geben Sie ein:

```
 ! _Box _Center
```

(Dies ist zugleich das der Schaltfläche Quader, Zentrum zugrundeliegende Makro.) 
Alle Einträge (Befehle und numerische Eingaben) müssen durch ein einfaches Leerzeichen getrennt sein.

Nun muss der zentrale Punkt bestimmt werden.  Dazu muss Rhino mitgeteilt werden, dass es die Ausführung des Befehls vorübergehend anhält und auf eine Eingabe in Form eines Klicks oder einer Tastatureingabe wartet.  Tun Sie dies, indem Sie den Befehl Pause eingeben.

```
 ! _Box _Center _Pause
```

Wenn die Daten eingegeben sind, kann die Größe des Quaders direkt als Befehl eingegeben werden.  Da die Option Zentrum des Befehls Quader eine Ecke desselben als zweiten Eingabewert erwartet, können wir die X- und Y-Koordinate eingeben:

```
 ! _Box _Center _Pause r5,5
```

(Wofür das `r`?  Weil wir möchten, dass die Koordinate relativ zum zuletzt gewählten Punkt, also zur Unterseite des Würfels ist.  Ansonsten würde die Ecke immer bei der Koordinate (5,5) landen.)

Nun können wir die Höhe eingeben, die in diesem Fall relativ zum ursprünglichen Startpunkt ist.

```
 ! _Box _Center _Pause r5,5 10
```

Da es nun keiner weiteren Eingabe bedarf und keine weiteren Möglichkeiten zur Verfügung stehen, ist das Makro und auch unser Quader fertig.  Da wir die gleiche Höhe wie Breite haben wollten, wäre eine weitere Möglichkeit gewesen, anstatt der 10 des letzten Eintrags Enter zu verwenden.

```
 ! _Box _Center _Pause r5,5 _Enter
```

Jetzt, wo das Makro läuft, [erstellen Sie eine neue Werkzeugleistenschaltfläche](https://wiki.mcneel.com/rhino/macroscriptsetup) und fügen Sie das Makro ein. Geben Sie ihm einen leicht wiedererkennbaren Namen, z. B. "10x10x10 unten zentrierter Quader".  Sobald das Makro ausgeführt ist, wird die gesamte Sequenz des Makros durch einen Rechtsklick wiederholt, so dass Sie es mehrmals hintereinander verwenden können, ohne jedes Mal auf die Schaltfläche klicken zu müssen.

## Nun zum etwas komplizierteren Teil...

Manche Befehle rufen Dialogfenster mit zahlreichen Optionen auf.  Normalerweise stoppt dies die Ausführung Ihres Makros so lange, bis Sie eine der gewünschten Optionen gewählt haben.  Da wir aber an einer automatisierten Ausführung interessiert sind, kann das Abarbeiten des Dialogfensters durch Einsetzen eines -Bindestrichs vor den jeweiligen Befehl umgangen werden.  Sie können dann alle nötigen Optionen per Script abarbeiten lassen, sodass das Makro ohne Ihr Zutun bis zum Ende fortgesetzt wird.  Manche Befehle haben mehrere Ebenen an Unteroptionen.  Um die verschiedenen Möglichkeiten zu konsultieren, geben Sie den entsprechenden Befehl mit vorangestelltem Bindestrich in der Befehlszeile ein und sehen Sie nach, was in den Optionen vorgeschlagen wird.  Klicken Sie auf die Optionen und sehen Sie nach, ob Unteroptionen verfügbar sind.

#### Loft zweier offener Kurven

Nehmen wir an, Sie möchten wiederholt zwei *OFFENE* Kurven „zusammenloften“, um eine Fläche zu bilden.  Wenn Sie den Standardbefehl „Loften“ verwenden, müssen Sie immer durch den Dialog gehen.  Wenn Sie stattdessen die Version „-Loften“ verwenden, geht das Ganze viel schneller.  Sehen Sie sich Folgendes an:

```
_-Loft
_Pause
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Beachten Sie, dass Sie beim Aufrufen des Befehls dank einer sofortigen Pause Ihre Kurven auswählen können.  Wenn Sie die Pause entfernen, funktioniert das Makro nicht, wenn Sie vor dem Aufruf desselben die Kurven nicht ausgewählt haben.  Wenn Sie Ihre Kurven bereits vorausgewählt haben, wird die Pause automatisch ignoriert.  Der Befehl setzt dann alle von Ihnen angegebenen Optionen. Danach werden die Oberfläche und die Endbearbeitung erstellt. Versuchen Sie es einmal mit zwei offenen Kurven, die Sie entweder vorher oder nachher auswählen.  Versuchen Sie, eine oder mehrere der Optionen zu ändern, also beispielsweise Geschlossen=Ja oder Vereinfachen=Neuaufbauen zu ersetzen. (Hierfür müssen Sie auch eine Zeile mit Rebuild=20 oder einem anderen Wert hinzufügen).

#### Verändern zum Gebrauch mit geschlossenen Kurven

Versuchen Sie es jetzt einmal mit zwei geschlossenen Kurven.  Sie stehen vor einem Problem.  Warum? Für geschlossene Kurven erwartet Loft eine weitere Eingabe von Ihnen - die Position der Naht.  Diese müssen Sie im Makro in der richtigen Reihenfolge angeben.  Sie können entweder aus mehreren automatischen Nahtoptionen (als Unteroptionen) wählen oder diese mithilfe von Benutzereingaben einstellen.  In jedem Fall müssen Sie dazu das Makro modifizieren.

Durch Hinzufügen einer Pause an der richtigen Stelle können Sie die Naht durch Benutzereingaben überprüfen und einstellen:

```
_-Loft
_Pause
_Pause  <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Durch das Hinzufügen einer `Eingabe` anstelle der `Pause` wird Rhino mitgeteilt, dass es Ihnen egal ist. Lassen Sie die Naht einfach so, wie sie standardmäßig ist.

```
_-Loft
_Pause
_Enter  <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

Sie können außerdem in den Unteroptionen der Naht eine andere Loft-Nahtoption wählen.

```
_-Loft
_Pause
_Natural  <--
_Enter    <--
_Type=_Normal
_Simplify=_None
_Closed=_No
_Enter
```

(`Enter` nach Natural ist notwendig, um die Nahtoptionsebene zu verlassen und zurück zu den Loftoptionen zu gelangen)

Leider funktioniert dasselbe Makro aufgrund der zusätzlich notwendigen Nahtoption nicht korrekt, sowohl für offene als auch geschlossene Kurven.  Dies ist eine der Beschränkungen des Makrosystems und beruht auf der Art und Weise, wie einige Rhino-Befehle geschrieben sind.


## Verwendung von Makros zur schnellen Einstellung Ihrer Interface-Optionen

Makros können außerdem dazu verwendet werden, verschiedene GUI- und Dokumenteigenschaften automatisch einzustellen, ohne dabei lange durch den Optionendialog gehen zu müssen.  Folgendes Makro stellt beispielsweise das Rendernetz benutzerdefiniert ein. (Beachten Sie den Bindestrich vor -_DocumentProperties.)

```
-_DocumentProperties
_Mesh _Custom
_MaxAngle=0 _AspectRatio=0
_MinEdgeLength=0 _MaxEdgeLength=0
_MaxEdgeSrf=0.01 _GridQuads=16
_Refine=Yes _JaggedSeams=No
_SimplePlanes=No
_Enter
_Enter
```

Wozu die zwei Enter am Ende?

Das Makro bewegt sich in -_DocumentProperties zwei Ebenen nach unten - zuerst auf die Polygonnetzebene und anschließend auf die benutzerdefinierte Unterebene im Polygonnetz.  Mit dem ersten Enter verlassen Sie die Unterebene und gelangen wieder auf die Hauptebene und mit dem zweiten verlassen Sie den Befehl als solchen.  Manche Skripts benötigen eventuell sogar drei Enter.  

Das folgende ist von Jeff LaSor und dient dem An-/Abschalten des Fadenkreuzes:

Um Fadenkreuze mithilfe eines Skripts EIN- und AUSzuschalten, muss einer Schaltfläche folgendes zugewiesen werden:

```
  -_Options _Appearance _Visibility
  _Crosshairs _Enter _Enter _Enter
```
Beachten Sie die Referenz zu jeder einzelnen Befehlsoption.  Die Spezifizierung in einem Skript ist, als ob Sie mit der Maus darauf klicken würden.  Beachten Sie zudem die drei Eingaben.  Da Sie mit jeder Befehlsoption auf eine weitere Unterebene gelangen, wird ein Enter benötigt, um wieder hinauf und aus dem Befehl hinaus zu gelangen.  Da das Skript drei Ebenen nach unten geht, benötigt es auch drei Enter, um wieder den ganzen Weg aus dem Befehl hinaus zu finden.

Oder, wenn Sie einfach ein Ausrufezeichen `!` am Ende verwenden (was in einem Skript "Ende jetzt!" bedeutet), bringt es Sie ganz nach draußen, egal in wie vielen Unterebenen Sie sich befinden. Hinweis: Wenn Sie Ihr Makro mit etwas anderem fortsetzen wollen, verwenden Sie nicht `!`, sondern stattdessen Enter, da Ihr Makro sonst immer am `!` aufhört und beendet wird.

Das Skript schaltet das Fadenkreuz einfach EIN und AUS. Falls Sie aber ein Skript wollen, das sie immer EIN und ein anderes, das sie immer AUS schaltet, sähen sie folgendermaßen aus:

Immer eingeschaltet:

```
  -_Options _Appearance _Visibility
  _Crosshairs=_Show !
```

Immer ausgeschaltet:

```
  -_Options _Appearance _Visibility
  _Crosshairs=_Hide !
```

Beachten Sie hier die Verwendung von `!`. Beachten Sie auch, dass Sie die Werte, welche die Optionen annehmen können, dieser Option mit dem Operator '=' direkt zuweisen können.  Für das Fadenkreuz gibt es zwei mögliche Werte: "Anzeigen" und "Ausblenden".

(Danke, Jeff)

## Weitere nützliche Tools und Befehle für Makros

Es gibt einige geschickte Tricks für komplexere Makros.  Eine Möglichkeit ist die Verwendung verschiedener Auswahlfilter wie „LetzteAuswahl“, wodurch das zuletzt erstellte/bearbeitete Objekt ausgewählt wird, „VorherigeAuswahl“, wodurch das vorherige Input-Objekt ausgewählt wird und „AuswahlAufheben“, wodurch alle Auswahlen aufgehoben werden.  Es gibt zudem Möglichkeiten, Objekte zu benennen, zu gruppieren (und die Gruppe zu benennen) und dann später mit dem Objekt- bzw. Gruppennamen auf sie zuzugreifen.

```
Auswählen
LetzteAuswahl
VorherigeAuswahl
AuswahlAufheben
ObjektNamenDefinieren
GruppennamenDefinieren
GruppeAuswählen
NamenAuswählen
Gruppieren
GruppierungAufheben
```

Setzung eines einzelnen Objektnamens (dies ist ein Makro für sich!):

```
  _Properties _Pause _Object _Name
  [Geben Sie hier Ihren Objektnamen ein] _Enter _Enter
```

Entfernen eines einzelnen Objektnamens (ohne dabei das Objekt zu löschen)

```
  _Properties _Pause _Object _Name
  “ “ _Enter _Enter (Abstand zwischen den Anführungszeichen für den Namen)
```

## Beispiele zur Verwendung der obigen Tools

Sehen Sie sich folgendes Makro an:

```
_Select _Pause _Setredrawoff
_BoundingBox _World _Enter
_Selnone _Sellast
_OffsetSrf _Solid _Pause
_Delete _Sellast
_BoundingBox _World _Enter
_Delete _Setredrawon
```

Es erstellt einen versetzten Begrenzungsquader um ein Objekt. Der Versatz wird vom Benutzer eingegeben.  Versuchen Sie, der logischen Sequenz zu folgen.  Durch das Deaktivieren und anschließende erneute Aktivieren des Bildaufbaus durch BildaufbauDeaktivieren/Aktivieren wird das Flackern der Anzeige verhindert und der Prozess beschleunigt.  Beachten Sie dabei, dass wenn Sie den Befehl beenden, bevor Sie erneut BildaufbauAktivieren ausführen, Rhino deaktiviert zu sein scheint, da die Anzeige nicht mehr aktualisiert wird.  Wenn dies passiert, geben Sie einfach den Befehl BildaufbauAktivieren ein, damit die Anzeige aktualisiert wird.

**Als letztes Beispiel** erzeugt das folgende Makro einen auf einem 2D-Planar oder Textobjekt zentrierten und mit diesem gruppierten Punkt. Es wird davon ausgegangen, dass Sie sich in derselben Ansicht befinden, in der der Text erstellt wurde und dass das Objekt tatsächlich ein planares 2D-Objekt ist. (Ansonsten schlägt die Verwendung des Makros vermutlich fehl.)

Beachten Sie dabei die Verwendung von benannten Gruppen und verschiedenen Auswahlbefehlen.  Der Befehl „EchoAus“ verhindert vorübergehend, dass Informationen an die Befehlszeile gesendet werden, was in Kombination mit dem Deaktivieren des Bildaufbaus den Effekt hat, dass das Makro ohne Flackern und unnötig viel Info in der Befehlschronik ausgeführt wird.  Es funktioniert natürlich aber auch ohne diese Befehle.

```
_Select _Pause _Noecho _Setredrawoff
_Group _Enter _SetGroupName TexTemp
_BoundingBox _CPlane _Enter
_SelNone _SelLast _PlanarSrf
_SelPrev _Delete _SelLast
_AreaCentroid _Delete
_Sellast _SelGroup TexTemp
_Ungroup _Group _Setredrawon
```

**Sie können diese Anleitung gerne ergänzen oder bearbeiten!**
Die aktuelle Version ist eine Work-in-Progress-Version.

## Verwandte Themen

- [Grundlegende Python-Syntax](/guides/rhinopython/)
- [Rhinoscript](/guides/rhinoscript/)
- [Hilfethema Makro-Syntax](http://docs.mcneel.com/rhino/6/help/en-us/information/rhinoscripting.htm)
- [Ein Makro ausführen](/guides/rhinoscript/running-scripts-from-macros/)

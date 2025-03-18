+++
aliases = ["/en/8/guides/general/rhino-ui-system/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "Dieses Handbuch beschreibt das Benutzeroberflächensystem von Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Das Rhino-UI-System"
type = "guides"
weight = 3
override_last_modified = "2023-11-20T08:29:10Z"

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

Dieses Handbuch bietet einen Überblick über das Sytem der Rhino-Benutzeroberfläche oder UI (User Interface) und vergleicht das neue System in Rhino 8 mit dem vorherigen System in Rhino 7 und früher.

## UI-System in 8

Die Zielsetzungen für das neue UI-System in  Rhino 8 waren die folgenden:

- Anzeige von Panels und Werkzeugleisten im selben Container.
- Verweise auf Werkzeugleisten und Makros aus mehreren Quellen, ohne Definitionen von einer RUI-Datei in eine andere kopieren zu müssen.
- Änderungen an der Rhino-Benutzeroberfläche (RUI), ohne in Rhino oder Plug-in-Serviceversionen vorhandene Dateien zu überschreiben oder zu ersetzen. (In früheren Rhino-Versionen führte das Ersetzen der RUI-Datei zugunsten aktualisierter Werkzeugleisten und Makros dazu, dass Benutzeränderungen an RUI-Dateien überschrieben wurden).
- Schnelles Ändern der Rhino-Benutzeroberfläche, um aufgabenorientierte Werkzeuge anzuzeigen.
- Gemeinsame Nutzung von UI-Layouts durch Anwender.
- Beliebige Abänderung der Benutzeroberfläche durch die Anwender, ohne dass diese wissen müssen, wo sich eine UI-Komponente befindet oder woher sie kommt, und automatische Verfolgung der Änderungen.
- Vereinheitlichung der Benutzeroberfläche für Windows und Mac.

Die wichtigsten Änderungen im neuen Rhino 8 UI-System sind:

- Werkzeugleistengruppen wurden durch Container ersetzt. In Containern können sowohl Panels als auch Werkzeugleisten angezeigt werden.
- RUI-Dateien werden verwendet, um Werkzeugleisten- und Makrobibliotheken bereitzustellen, und sie werden nicht mehr direkt geändert. Rhino verfolgt RUI-Änderungen und wendet sie beim Laden an. Auf diese Weise kann man in Rhino aktualisierte RUI-Dateien erhalten, ohne dass Benutzeränderungen an einer Werkzeugleiste oder einem Makro verloren gehen.
- Fensterlayouts wurden hinzugefügt und können verwendet werden, um schnell zwischen verschiedenen UI-Konfigurationen zu wechseln. Sie können als Dateien exportiert werden und enthalten Änderungen an Werkzeugleisten und Makros sowie RUI-Benutzer-Dateien.
- Beim Importieren eines Fenster-Layouts werden die erforderlichen RUI-Dateien der Benutzer extrahiert und die RUI-Änderungen angewendet.

Das neue Rhino 8 UI-System ist so konzipiert, dass es die Referenzierung von UI-Komponenten aus vielen Quellen ermöglicht: einschließlich Panels, Werkzeugleisten und Makros, die durch eine RUI-Datei oder ein Plug-in definiert sind. Wenn Rhino geschlossen wird, werden die Änderungen an der Benutzeroberfläche gespeichert und die ursprünglichen RUI-Dateien werden nie geändert, es sei denn, dies wird ausdrücklich angefordert. Konfigurationen von UI-Layouts können gespeichert, wiederhergestellt, exportiert und als Fensterlayouts importiert und zwischen Windows und Mac ausgetauscht werden.

### Container

Container enthalten Verweise auf Panels und Werkzeugleisten. Werkzeugleisten können von jeder gültigen RUI-Quelle referenziert werden. Die Elemente werden als Reiter in einem Container angezeigt. Die Container können sichtbar oder ausgeblendet sein.

Container können geändert werden, indem man Reiter von einem Container in einen anderen zieht oder indem man auf das Zahnradmenü des Containers klickt, um Verweise auf Bereiche oder Werkzeugleisten hinzuzufügen oder zu entfernen. Ein und dasselbe Panel kann von mehreren Containern referenziert werden, d.h. es ist möglich, den Reiter "Ebenen" in mehreren Containern anzeigen zu lassen.

Containerdefinitionen, Sichtbarkeit, Position und Größe werden beim Schließen von Rhino gespeichert und beim Neustart von Rhino wiederhergestellt. Diese Informationen können auch über Fensterlayouts gespeichert und weitergegeben werden.

Container können mit dem Befehl **[Container](https://docs.mcneel.com/rhino/8/help/de-de/index.htm#commands/containers.htm#(null))** von Rhino verwaltet werden.

### Fenster-Layouts

Fensterlayouts sind ein Schnappschuss von Containerdefinitionen, Sichtbarkeitsstatus, Position und Größe. Durch die Wiederherstellung eines Fensterlayouts wird die aktuelle Benutzeroberfläche wieder so konfiguriert, wie sie zum Zeitpunkt der Erstellung des Layouts aussah. Wiederhergestellte Container zeigen die Reiter in der Reihenfolge an, in der sie bei der Erstellung des Fensterlayouts angeordnet waren, und erscheinen an derselben Stelle und in derselben Größe. Die Reiter der Werkzeugleisten verweisen auf die aktuelle Definition einer Werkzeugleiste. Wenn die Werkzeugleiste nicht mehr vorhanden ist, wird der Reiter nicht angezeigt.

Fensterlayouts können mit dem Rhino-Befehl **[FensterAnordnung](https://docs.mcneel.com/rhino/8/help/de-de/index.htm#commands/windowlayout.htm#(null))** verwaltet werden.

#### Exportieren und Importieren von Fensterlayouts

Fensterlayouts können in eine Rhino-Fensterlayoutdatei (RHW) exportiert werden. Exportierte RHW-Dateien enthalten referenzierte benutzerdefinierte RUI-Dateien und die mit allen RUI-Dateien verbundenen Änderungen zum Zeitpunkt der Erstellung der RHW-Datei.

Beim Importieren einer RHW-Datei wird geprüft, ob eine eingebettete benutzerdefinierte RUI-Datei derzeit geöffnet ist. Wenn die Datei nicht geöffnet ist, wird die benutzerdefinierte Datei extrahiert und geöffnet. Sobald die benutzerdefinierte Liste extrahiert oder überprüft wurde, werden die in der RHW-Datei gespeicherten RUI-Änderungen auf die aktuellen RUI-Dateien angewendet. Mit Werkzeugleisten verbundene Änderungsinformationen, die durch nicht vorhandene Plug-in-Dateien definiert sind, werden ignoriert. Sobald die RUI-Daten wiederhergestellt sind, werden die Container entsprechend der in der RHW-Datei gespeicherten Definition erstellt oder geändert. Container, die nur auf Werkzeugleisten von nicht installierten Plug-ins verweisen, werden ignoriert. Nach dem Import erscheint das Layout in der Liste der Fensterlayouts und kann dann wiederhergestellt werden.

Fensterlayouts können mit dem Rhino-Befehl **[FensterAnordung](https://docs.mcneel.com/rhino/8/help/de-de/index.htm#commands/windowlayout.htm#(null))** exportiert und importiert werden.

### RUI-Dateien

In Rhino 8 sind RUI-Dateien jetzt einfach eine Sammlung von Werkzeugleisten, Makros und Bildern. Diese Dateien sollen Bibliotheken von Werkzeugleisten bereitstellen, die von Containern referenziert werden können. Änderungen an Werkzeugleisten und Makros können jetzt mit Rhino- und Plug-in-Updates ausgeführt werden. Neue Werkzeugleisten, die in der aktualisierten RUI-Bibliothek definiert wurden, erscheinen automatisch in der Befehlsliste der Werkzeugleiste. Schaltflächen, die zu einer Werkzeugleiste hinzugefügt oder von ihr entfernt werden, werden der Werkzeugleistenreferenz hinzugefügt oder entfernt.

In RUI-Dateien definierte Werkzeugleistengruppen werden in Container umgewandelt, wenn sie geladen werden, um Legacy- und Plug-in-RUI-Dateien zu unterstützen und einer Plug-in-RUI-Datei die Möglichkeit zu geben, mit dem Plug-in verbundene Container zu erstellen.

Verknüpfte RUI-Dateien können mit den **[Rhino-Optionen > Werkzeugleisten](https://docs.mcneel.com/rhino/8/help/de-de/index.htm#options/appearance_toolbars.htm#(null))** verwaltet werden.

### Werkzeugleisten

Werkzeugleisten sind Sammlungen von Schaltflächen. Die Schaltflächen der Werkzeugleiste verweisen auf Makros, die aus jeder gültigen RUI-Quelle stammen können. Werkzeugleisten werden als Reiter in einem Container angezeigt.

#### Werkzeugleistengruppen

Werkzeugleistengruppen werden jetzt beim ersten Laden in Container umgewandelt. Sie dienen dazu, ältere RUI-Dateien zu unterstützen. Gruppen können auch von Plug-in-Entwicklern verwendet werden, um mit einem Plug-in verbundene Container-Definitionen bereitzustellen.

#### Werkzeugleiste

Werkzeugleisten sind Sammlungen von Werkzeugleistenschaltflächen und können von mehreren Containern referenziert werden. Sie können durch Ziehen und Ablegen von Schaltflächen aus anderen Werkzeugleisten oder mit dem Assistenten für neue Schaltflächen geändert werden.

Werkzeugleisten können mit dem Befehl **[Werkzeugleiste](https://docs.mcneel.com/rhino/8/help/de-de/index.htm#commands/toolbar.htm#(null))** von Rhino verwaltet werden.

#### Werkzeugleistenschaltfläche

Die Schaltflächen der Werkzeugleiste können Aktionen mit der linken und/oder rechten Maustaste enthalten. Die Aktionen des linken und rechten Mausklicks werden Makros zugewiesen, die ein Skript enthalten, das beim Anklicken ausgeführt wird. Die Schaltflächen der Werkzeugleiste zeigen das Bild des Makros an, das der linken Mausaktion zugewiesen ist, falls vorhanden, andernfalls wird das Bild des Rechtsklick-Makros verwendet.

#### Menü

Das Rhino-Menüsystem kann mit Menüobjekten erweitert werden, die in einer RUI-Datei definiert sind. Die RUI-Datei enthält Ortsangaben, die beschreiben, wo ein Element in das Menüsystem eingefügt werden soll. Neue Menüpunkte werden definiert, indem auf ein Makro verwiesen wird, das folgende Elemente enthält:

- Menütext
- Bild des Menüelements
- Der Hilfe-Text, der in der Statusleiste erscheint, wenn sich der Mauszeiger über einem Menüelement befindet.
- Befehlsskript, das beim Klicken auf das Menüelement ausgeführt wird.

Menüs können mit dem Befehl **[Menüs](https://docs.mcneel.com/rhino/8/help/de-de/index.htm#toolbarsandmenus/workspace_editor.htm#(null))** in Rhino verwaltet werden.

#### Makro

Makros enthalten Informationen, die zur Beschreibung des Befehlsskripts benötigt werden, das bei der Ausführung des Makros ausgeführt wird. Zu den Makro-Definitionen gehören die folgenden:

- Name
- Bild, sowohl im hellen als auch im dunklen Modus
- Befehlsskript
- Text der Schaltfläche
- Schaltflächen-Tooltip
- Menütext
- Hilfetext

Makros können mit dem Befehl **[Makros](https://docs.mcneel.com/rhino/8/help/de-de/index.htm#commands/macros.htm#(null))** in Rhino verwaltet werden.

### Panels

Panels sind amodale Formen der Benutzeroberfläche, die von Rhino oder von Plug-ins erstellt werden. Sie können in jedem Container als Reiter erscheinen und durch Ziehen und Ablegen zwischen Containern verschoben werden.

Panels können von mehreren Containern referenziert werden, aber sie können nicht mehr als einmal im selben Container erscheinen.

## Vorheriges Rhino-UI-System

Das Rhino-UI-System, das in Rhino für Windows Version 7 und früher zu finden ist, besteht aus folgenden Elementen:

### Werkzeugleisten

Rhino-Werkzeugleisten sind Sammlungen von Werkzeugleisten-Schaltflächen. Die Schaltflächen der Werkzeugleiste verweisen auf Makros, die in der gleichen RUI-Datei wie die Werkzeugleiste definiert sein müssen. Schaltflächen enthalten ein Bild, einen Tooltip, einen Menütext, einen Hilfetext und ein Skript. Werkzeugleisten werden in Werkzeugleistengruppen angezeigt.

### Werkzeugleistengruppe

Werkzeugleistengruppen sind Sammlungen von Verweisen auf Werkzeugleisten aus derselben RUI-Datei. Wenn Sie eine Werkzeugleiste aus einer Datei in eine Gruppe in einer anderen Datei ziehen, werden die Werkzeugleiste und die referenzierten Makros aus der Quelldatei in die Zieldatei kopiert. Werkzeugleistengruppen können nicht auf Rhino-Panels verweisen.

### Werkzeugleiste

Werkzeugleisten sind Sammlungen von Werkzeugleistenschaltflächen und werden immer nur von Werkzeugleistengruppen referenziert und angezeigt.

### Werkzeugleistenschaltfläche

Die Schaltflächen der Werkzeugleiste können Aktionen mit der linken und/oder rechten Maustaste enthalten. Mausklick-Aktionen werden Makros zugewiesen, die ein Skript enthalten, das beim Anklicken ausgeführt wird. Die Schaltflächen der Werkzeugleiste zeigen das Bild des Makros an, das der linken Mausaktion zugewiesen ist, falls vorhanden, andernfalls wird das Bild des Rechtsklick-Makros verwendet.

Die Schaltflächen der Werkzeugleiste können optional so konfiguriert werden, dass sie andere Werkzeugleisten vorübergehend ausklappen.

Werkzeugleistenschaltflächen können nur auf Makros aus derselben RUI-Datei verweisen wie die Werkzeugleiste, zu der sie gehören.

### Menü

Das Rhino-Menüsystem kann mit Menüobjekten erweitert werden, die in einer RUI-Datei definiert sind. Die RUI-Datei enthält Ortsangaben, die beschreiben, wo ein Element in das Menüsystem eingefügt werden soll. Neue Menüpunkte werden definiert, indem auf ein Makro verwiesen wird, das folgende Elemente enthält:

- Menütext
- Bild des Menüelements
- Der Hilfe-Text, der in der Statusleiste erscheint, wenn sich der Mauszeiger über einem Menüelement befindet.
- Befehlsskript, das beim Klicken auf das Menüelement ausgeführt wird.

### Makro

Makros enthalten Informationen, die zur Anzeige oder Beschreibung des Befehlsskripts benötigt werden, das bei der Ausführung des Makros ausgeführt wird. Zu den Makro-Definitionen gehören die folgenden:
Bild, das entweder auf einer referenzierten Werkzeugleistenschaltfläche oder einem Menüelement angezeigt wird.

- Tooltip der Schaltfläche.
- Text der Schaltfläche
- Text des Menüelements
- Der Hilfe-Text, der in der Statusleiste erscheint, wenn sich der Mauszeiger über einem Menüelement befindet.
- Auszuführendes Befehlsskript.

### RUI-Datei

RUI-Dateien sind Sammlungen der oben genannten Elemente und werden in einem beschreibbaren Verzeichnis gespeichert. In einer RUI-Datei gespeicherte Elemente können nur auf Elemente verweisen, die in derselben Datei definiert sind. Änderungen an Elementen in der Datei werden automatisch gespeichert, wenn Rhino geschlossen wird. Sie können RUI-Dateien jederzeit öffnen oder schließen oder eine Datei manuell speichern. Die aktuelle Version einer Datei wird gesichert und Änderungen werden unter dem Dateinamen gespeichert. Wenn eine Datei beschädigt wird, können Sie sie löschen und die Sicherungsdatei umbenennen, um die vorherige Version wiederherzustellen. Wenn die Sicherungsdatei beschädigt ist, kann nichts wiederhergestellt werden.

Rhino-Plug-ins können eine RUI-Datei mit demselben Namen wie das Plug-in installieren, die dann in einen beschreibbaren Speicherort kopiert und beim Start von Rhino automatisch geöffnet wird. Dies gibt einem Plug-in die Möglichkeit, die Rhino-Schnittstelle zu erweitern, während das Plug-in nicht geladen wird, bis es referenziert wird.

Beachten Sie, dass alle oben genannten Punkte mit dem Befehl **[Werkzeugleisten](https://docs.mcneel.com/rhino/7/help/de-de/index.htm#options/toolbars.htm#(null))** von Rhino 7 verwaltet werden können.

### Rhino-Panels

Rhino-Panels sind vom Rhino-Kern oder einem Plug-in erstellte amodale Benutzeroberflächendefinitionen.

Die Panels werden in einer Sammlung von Reitern angezeigt. Reiter-Sammlungen können nur Verweise auf Panels enthalten und ein Panel kann nur von einer einzigen Sammlung referenziert werden. Wenn Sie ein Panel in einer Sammlung anzeigen, werden Verweise auf dieses Panel aus allen anderen Sammlungen entfernt.

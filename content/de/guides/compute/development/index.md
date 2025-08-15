+++
aliases = ["/en/5/guides/compute/development/", "/en/6/guides/compute/development/", "/en/7/guides/compute/development/", "/en/wip/guides/compute/development/"]
authors = [ "pedro" ]
categories = [ "Getting Started", "Development" ]
description = "Compute für die Produktion bereitstellen"
keywords = [ "developer", "compute", "production" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Lokales Ausführen und Debuggen von Compute"
type = "guides"
weight = 2
override_last_modified = "2024-05-13T15:49:48Z"

[admin]
TODO = "needs editing"
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

Rhino.Compute ermöglicht es Ihnen, die geometrischen Berechnungsfähigkeiten von Rhino in die Cloud zu bringen. Bevor Sie Ihre Anwendung in einer Produktionsumgebung einsetzen, sollten Sie sicherstellen, dass alle perfekt in einer kontrollierten Umgebung funktioniert.

Diese Anleitung richtet sich an Entwickler, die mit Windows vertraut sind und über Grundkenntnisse in [Visual Studio](https://visualstudio.microsoft.com/downloads/) und [Git](https://git-scm.com/downloads) verfügen. Egal, ob Sie ein erfahrener Rhino-Benutzer oder neu in Rhino.Compute sind, diese Dokumentation wird Ihnen die notwendigen Schritte zum Einrichten Ihrer Entwicklungsumgebung und zum effektiven Debuggen zeigen.

## Voraussetzungen

Bevor Sie mit der Einrichtung von Rhino.Compute auf Ihrem lokalen Rechner beginnen, müssen Sie sicherstellen, dass Sie die richtigen Werkzeuge haben. Das brauchen Sie dazu:

- Windows-Betriebssystem. Rhino.Compute läuft nur auf Windows.
- Entwicklungsumgebung. Sie benötigen [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/), um den Code zu kompilieren.
- Versionskontrolle. [Git](https://git-scm.com/downloads) ist notwendig, um das compute.rhino3d-Repository zu klonen und Branches entsprechend Ihrer Rhino-Version zu verwalten.
- Rhino, Besuchen Sie unsere Download-Seite, um die neuesten Builds von [Rhino 8](https://www.rhino3d.com/download/rhino-for-windows/8/latest) oder [Rhino 7](https://www.rhino3d.com/download/rhino-for-windows/7/latest) zu erhalten. Nach dem Herunterladen und der Installation starten Sie bitte Rhino und folgen Sie den Anweisungen beim Start, um Ihre Lizenz auf Ihrem Computer oder über den Cloud Zoo zu validieren.

{{< call-out "note" "Anmerkung" >}}
Sie müssen die spezifische Version von Rhino.Compute entsprechend der von Ihnen installierten Rhino-Version ausführen. Im nächsten Abschnitt werden Sie den Quellcode aus dem compute.rhino3d-Repository klonen. Wenn Sie Rhino 8 auf Ihrem Rechner installiert haben, müssen Sie sicherstellen, dass Sie den 8.x-Branch klonen. Wenn Sie Rhino 7 installiert haben, stellen Sie sicher, dass Sie den 7.x-Branch klonen.
{{< /call-out >}}

## Klonen Sie das Repository

Um die neueste Version von Rhino.Compute zu erhalten, müssen Sie das [Repository](https://github.com/mcneel/compute.rhino3d) von unserem offiziellen Konto in Github klonen.

1. Gehen Sie zu [https://github.com/mcneel/compute.rhino3d](https://github.com/mcneel/compute.rhino3d)

1. Vergewissern Sie sich, dass Sie im Dropdown-Menü Branch entweder den 8.x- oder den 7.x-Branch zum Klonen auswählen.

1. Klicken Sie dort auf die grüne Schaltfläche "<> Code" und kopieren Sie die URL für das Repository.
![compute_geometry_clone](/images/compute_geometry_clone.png)

1. Erstellen Sie auf Ihrem lokalen Computer einen Ordner, in den Sie das Repository klonen möchten.

1. Navigieren Sie über Ihre bevorzugte Eingabeaufforderung zu diesem Verzeichnis, geben Sie "git clone" ein und fügen Sie die URL ein, die Sie zuvor kopiert haben.
    ```python
    git clone https://github.com/mcneel/compute.rhino3d.git
    ```
1. Nachdem der Klonvorgang abgeschlossen ist, sollten Sie eine Reihe von Dateien und Verzeichnissen sehen, die aus dem compute.rhino3d-Repository in den von Ihnen erstellten Ordner heruntergeladen wurden.

## Anatomie der Lösung

Das Rhino.Compute-Repository besteht aus zwei Hauptprojekten, die jeweils unterschiedlichen Zwecken innerhalb des Frameworks dienen. Diese zu verstehen, kann helfen, die Funktionsweise von Rhino.Compute zu klären, insbesondere wenn Sie mit dem Programm arbeiten oder zu seiner Entwicklung beitragen möchten. Hier ist eine Aufschlüsselung der beiden Projekte:

- **compute.geometry**. Dieses Projekt konzentriert sich in erster Linie auf die Aspekte der geometrischen Berechnung. Im Wesentlichen bietet compute.geometry eine REST-API, die die Geometrie-Engine von Rhino für die Verwendung über das Web zugänglich macht. Das bedeutet, dass geometrische Operationen auf einem Server durchgeführt und die Ergebnisse remote abgerufen werden können. Dies ist sehr nützlich für webbasierte Anwendungen oder Dienste, die eine komplexe geometrische Verarbeitung erfordern.

- **rhino.compute**. Dieses Projekt kann als übergeordnete Service-Ebene betrachtet werden, die die Aufrufe der compute.geometry-API verwaltet und orchestriert und Aufgaben wie Authentifizierung, das Erzeugen von Untergeordneten-Prozessen und das Einrichten von Zeitlimits für das Herunterfahren des Prozesses übernimmt.

## Kompilieren Sie die Lösung

Nun, da Sie den Code haben, ist es an der Zeit, das Projekt in Visual Studio 2022 zu öffnen und es für das Debugging vorzubereiten.

1. Navigieren Sie zu dem Verzeichnis, in das Sie das Repository geklont haben, und suchen Sie die Datei **compute.sln**. Doppelklicken Sie darauf, um das Projekt in Visual Studio 2022 zu öffnen.

1. Setzen Sie die Lösungskonfiguration in den **Debug**-Modus. Dadurch können Sie den Code mit allen Debugging-Funktionen ausführen, was es einfacher macht, den Code zu durchsuchen und Fehler zu finden.
![compute_geometry_vs_debug](/images/compute_geometry_vs_debug.png)

1. Klicken Sie im Menü File auf Build -> Build Solution (Strg + Umschalt + B). Dadurch werden alle Projektdateien kompiliert.
![compute_geometry_vs_build](/images/compute_geometry_vs_build.png)

1. Klicken Sie im Panel Solution Explorer mit der rechten Maustaste auf das Projekt **rhino.compute** und wählen Sie **Set as Startup Project**. Dadurch wird sichergestellt, dass Visual Studio beim Ausführen des Debuggers genau dieses Projekt startet.
![compute_geometry_vs_startup](/images/compute_geometry_vs_startup.png)

1. Klicken Sie auf **rhino.compute**, um die Anwendung im Debugger zu starten. Eine Konsolenanwendung sollte in Ihrer Taskleiste erscheinen und den Status des Rhino.Compute-Ladevorgangs anzeigen.
![compute_geometry_vs_run](/images/compute_geometry_vs_run.png)

1. Jetzt müssen Sie nur noch ein paar Sekunden warten, bis Rhino.Compute geladen ist. Bitte beachten Sie, dass die protokollierten Informationen von der Rhino-Version abhängen, die Sie zuvor ausgewählt hatten.
![compute.geometry.exe](/images/compute_geometry_screenshot.png)

## Einen Endpunkt testen

Wenn die Rhino.Compute-Konsolenanwendung läuft, navigieren Sie zu einem dieser Endpunkte, um zu überprüfen, ob alles funktioniert!
- [http://localhost:6500/version](http://localhost:6500/version)
- [http://localhost:6500/healthcheck](http://localhost:6500/healthcheck)
- [http://localhost:6500/activechildren](http://localhost:6500/activechildren)
- [http://localhost:6500/sdk](http://localhost:6500/sdk)
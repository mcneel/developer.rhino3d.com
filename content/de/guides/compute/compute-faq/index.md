+++
aliases = ["/en/5/guides/compute/compute-faq/", "/en/6/guides/compute/compute-faq/", "/en/7/guides/compute/compute-faq/", "/en/wip/guides/compute/compute-faq/", "/en/guides/compute/faq/"]
authors = [ "andy.payne" ]
categories = [ "Getting Started" ]
description = "Dieser Leitfaden ist eine Liste häufig gestellter Fragen (FAQ)) für Rhino.Compute."
keywords = [ "developer", "compute", "faq" ]
languages = []
sdk = [ "Compute" ]
title = "Häufig gestellte Fragen"
type = "guides"
weight = 1
override_last_modified = "2025-05-07T09:45:21Z"

[admin]
TODO = ""
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

## Allgemein

### Was ist Rhino.Compute?

In seiner einfachsten Definition ist Rhino.Compute ein Webserver, der Geometrieberechnungen unter Verwendung der Geometriebibliothek von Rhino (d.h. [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/)) durchführen kann. Es empfängt Anfragen über das Internet (mittels [HTTP](https://en.wikipedia.org/wiki/HTTP) oder [HTTPS](https://en.wikipedia.org/wiki/HTTPS)), verarbeitet sie mit der Geometrie-Engine von Rhino und sendet dann die Ergebnisse zurück. Jede Anwendung, die Webanfragen senden kann, kann mit Rhino.Compute interagieren, weswegen es leicht in verschiedene Arbeitsabläufe integrierbar ist.

### Warum sollte ich es benutzen?

Mit Rhino.Compute können Sie die leistungsstarken Werkzeuge und Funktionen von Rhino außerhalb der regulären Rhino- oder Grasshopper-Benutzeroberfläche verwenden. Es ist ideal für Teams, da Sie Grasshopper-Definitionen oder Rhino-Funktionen von einem zentralen Ort aus ausführen können, was die Zusammenarbeit erleichtert. Außerdem können mehrere Aufgaben gleichzeitig (parallel) bearbeitet werden, was zur Beschleunigung großer Projekte beiträgt. Und bei längeren Berechnungen läuft es im Hintergrund (asynchron), so dass es nicht einfriert oder Ihre Hauptschnittstelle verlangsamt.

### Funktioniert es auch unter macOS?

Nein. Rhino.Compute ist auf [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/) angewiesen, das die Ausführung von Rhino und Grasshopper *innerhalb* anderer 64-Bit-Anwendungen ermöglicht. Derzeit ist Rhino.Inside nur mit dem Windows-Betriebssystem kompatibel.

### Kostet es Geld?

Die kurze Antwort lautet: es hängt davon ab, *wo* Sie Rhino.Compute ausführen. Wenn Sie es auf einem normalen Windows-Computer, z. B. Ihrem privaten PC, verwenden, fallen keine zusätzlichen Kosten an. Rhino.Compute überprüft beim Start Ihre Standard-Rhino-Lizenz (beachten Sie: [Rhino-Testversionen](https://www.rhino3d.com/download/) funktionieren einwandfrei). Wenn Sie es jedoch auf einem Windows Server (z. B. einer virtuellen Maschine in der Cloud) ausführen, wird es nach unserem [Kernstunden-Berechnungsmodell](../core-hour-billing/) abgerechnet.

### Worin liegt der Unterschied zu Hops?

[Hops](../what-is-hops/) ist ein Grasshopper-Plugin (verfügbar im [Paketmanager](../../yak/what-is-yak/)), das es einfach macht, Grasshopper-Definitionen mit Rhino.Compute zu lösen. Ist Hops installiert, startet es automatisch eine Instanz von Rhino.Compute im Hintergrund, sobald Sie Grasshopper öffnen. Sie können dann die Komponente Hops verwenden, um Ihre Grasshopper-Definition an Rhino.Compute zu senden, das sie löst und die Ergebnisse zurücksendet. In diesem Zusammenhang ist Hops der "Client" und Rhino.Compute ist der "Server".

### Kann ich meine eigene Schnittstelle für die Arbeit mit Rhino.Compute erstellen?

Ja. Wie bereits erwähnt, kann jede Anwendung, die Webanfragen senden kann, mit Rhino.Compute arbeiten. Um die Arbeit zu erleichtern, bieten wir drei Bibliotheken an, die Sie je nach der von Ihnen bevorzugten Sprache verwenden können:
1. [Python Rhino.Compute Bibliothek](https://pypi.org/project/compute-rhino3d/)
1. [Javascript Rhino.Compute Bibliothek](https://www.npmjs.com/package/compute-rhino3d)
1. [.NET (C#) Rhino.Compute Bibliothek](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs)

Wir haben auch Schritt-für-Schritt-Anleitungen, die Ihnen den Einstieg in die oben genannten Bibliotheken erleichtern:
1. [Aufrufen von Compute mit Python](../compute-python-getting-started/)
1. [Aufrufen von Compute mit Javascript](../compute-javascript-getting-started/)
1. [Aufrufen von Compute mit .NET](../compute-net-getting-started/)

Schließlich haben wir ein [GitHub-Repository](https://github.com/mcneel/rhino-developer-samples/tree/8/compute) mit vielen Beispielprojekten und Beispielen, die zeigen, wie man Rhino.Compute für verschiedene Geometrieaufgaben verwendet.

### Kann ich Rhino.Compute in einer Produktionsumgebung verwenden?

Ja. Wir bieten eine [Schritt-für-Schritt-Anleitung](../deploy-to-iis/), um Ihnen bei der Einrichtung von Rhino.Compute in einer Produktionsumgebung zu helfen, zum Beispiel auf einer virtuellen Maschine (VM). Die Einrichtung ist unkompliziert - führen Sie einfach ein einfaches PowerShell-Skript aus, und Rhino.Compute ist einsatzbereit, um Anfragen zu bearbeiten.

## Fehlersuche und -behebung

Wir haben hart daran gearbeitet, Rhino.Compute so benutzerfreundlich wie möglich zu machen. Aber manchmal laufen die Dinge nicht wie geplant. Dieser Abschnitt soll Ihnen bei der Fehlersuche und -behebung helfen, wenn Sie auf Probleme stoßen.

### Wo finde ich die Protokolldateien?

Wenn Sie Rhino.Compute mit Hops ausführen, müssen Sie sicherstellen, dass die Rhino.Compute-Konsolenanwendung sichtbar ist, wenn sie gestartet wird. Hierfür führen Sie folgende Schritte aus:
1. Grasshopper starten
1. Klicken Sie auf **File -> Preferences**, um den Grasshopper-Einstellungsdialog zu öffnen
1. Klicken Sie auf den Reiter **Solver** im linken Menü
1. **Deaktivieren Sie** den Menüpunkt Hide Rhino.Compute Console Window
1. Rhino und Grasshopper neu starten 

{{< image url="/images/hops-preferences-1.png" alt="/images/hops-preferences-1.png" class="image_center" width="75%" >}}

Wenn Sie Grasshopper starten, sollten Sie nun eine neue Anwendung in Ihrer Taskleiste sehen (wenn Sie Windows verwenden). Dies ist die Rhino.Compute-Konsolenanwendung. Nützliche Informationen zur Fehlersuche werden hier angezeigt, während Sie mit Rhino.Compute arbeiten.

{{< image url="/images/hops-console-2.png" alt="/images/hops-console-2.png" class="image_center" width="100%" >}}

<br>
Wenn Sie Rhino.Compute auf einer VM ausführen, werden die Protokolldateien als Textdateien gespeichert. Es werden täglich neue Protokolldateien erstellt. Standardmäßig werden die Protokolldateien an folgendem Ort gespeichert: 

```cs
C:\inetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute\logs\
```

### Kann ich ausführliche Protokollierungsinformationen aktivieren?

Standardmäßig gibt Rhino.Compute einen minimalen Satz an Informationen in den Protokollen aus. Um eine ausführlichere Protokollierung zu ermöglichen, müssen Sie eine Umgebungsvariable auf Ihrer Maschine erstellen.

1. Klicken Sie mit der rechten Maustaste auf das Symbol **Dieser PC** im Datei-Explorer und wählen Sie dann **Eigenschaften** oder **System** in der Systemsteuerung
1. Klicken Sie im Fenster der Systemeigenschaften auf **Erweiterte Systemeinstellungen**
1. Auf dem Reiter **Erweitert** klicken Sie auf **Umgebungsvariablen**
1. Klicken Sie auf die Schaltfläche **Neu**, um eine neue Systemvariable zu erstellen
1. Im Feld **Variablenname** geben Sie "RHINO_COMPUTE_DEBUG" ein.
1. Im Feld **Variablenwert** geben Sie "wahr" ein.
1. Klicken Sie auf OK, um die Systemumgebungsvariable zu speichern, und dann erneut auf OK, um das Dialogfeld Umgebungsvariablen und das Fenster Systemeigenschaften zu schließen.

### Was kann ich tun, wenn ich den Fehler HRESULT E_FAIL erhalte?

Wenn Rhino.Compute den folgenden Fehler zurückgibt:

```cs
Application startup exception
System.Runtime.InteropServices.COMException (0x80004005): Error HRESULT E_FAIL has been returned from a call to a COM component.
   at Rhino.Runtime.InProcess.RhinoCore.InternalStartup(Int32 argc, String[] argv, StartupInfo& info, IntPtr hostWnd)
```

Dies wird höchstwahrscheinlich dadurch verursacht, dass Rhino.Compute beim Starten keine gültige Lizenz finden kann. Wenn Sie eine Windows-Server-basierte Maschine (d.h. eine virtuelle Maschine) verwenden, gehen Sie wie folgt vor:

1. Gehen Sie zum [Lizenzportal](https://www.rhino3d.com/licenses?_forceEmpty=true) und wählen Sie das Team aus, das Sie mit der Kernzeitabrechnung eingerichtet haben.
1. Klicken Sie auf **Team verwalten -> Kernstundenabrechnung verwalten**.
1. Klicken Sie auf **Aktion -> Token zur Authentisierung erhalten**, um ein Token zu erhalten.
1. Erstellen Sie eine neue Umgebungsvariable mit dem Namen `RHINO_TOKEN` und verwenden Sie das Token als Wert. Da das Token zu lang für das Dialogfeld Umgebungsvariablen von Windows ist, ist es am einfachsten, dies über einen PowerShell-Befehl zu tun.

```ps
[System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'your token here', 'Machine')
```

Wenn Sie Rhino auf diesem Computer starten, wird es von nun an Ihr Kernstunden-Abrechnungsteam verwenden.

{{< call-out "warning" "Wichtig" >}}
<strong>Wichtig!</strong> Ihr Kernstunden-Abrechnungstoken erlaubt es jedem, der es besitzt, Ihr Team nach Belieben zu belasten. Geben Sie dieses Token <strong>NICHT</strong> an andere weiter.
{{< /call-out >}}

### Ich erhalte eine 401-Fehlermeldung. Was bedeutet das?

Wenn Rhino.Compute eine 401-Fehlermeldung ausgibt, bedeutet dies, dass die Anfrage nicht autorisiert wurde. Dies geschieht in der Regel, wenn der Anfrage ein API-Schlüssel fehlt. Rhino.Compute sucht nach diesem Schlüssel - der als Umgebungsvariable auf der Maschine, auf der es läuft, gespeichert ist - um sicherzustellen, dass nur zugelassene Clients eine Verbindung herstellen können.

Wenn Sie Hops verwenden, können Sie den API-Schlüssel im Bereich Einstellungen festlegen.

1. Grasshopper starten
1. Klicken Sie auf **File -> Preferences**, um den Grasshopper-Einstellungsdialog zu öffnen
1. Klicken Sie auf den Reiter **Solver** im linken Menü
1. Nehmen Sie die **Eingabe des API-Schlüssels** im Eingabedialog vor
1. Rhino und Grasshopper neu starten

{{< image url="/images/hops-api-key.png" alt="/images/hops-api-key.png" class="image_center" width="75%" >}}

<br>
Wenn Sie mit einer anderen Methode eine Webanfrage an Rhino.Compute senden, stellen Sie sicher, dass Sie ein Schlüssel/Wert-Paar in die Kopfzeile der Anfrage aufnehmen. Der Schlüssel sollte "RhinoComputeKey" heißen und sein Wert muss mit dem API-Schlüssel übereinstimmen, der auf der Maschine festgelegt wurde, auf der Rhino.Compute läuft.

### Was bedeutet ein 500-Fehlercode?

Wenn Sie eine Antwort von Rhino.Compute mit einem 500-Fehlercode erhalten, bedeutet dies, dass der Server nicht richtig funktioniert und die Anfrage nicht korrekt bearbeiten kann. In diesem Fall sollten Sie Rhino.Compute im Debug-Modus ausführen, um weitere Informationen zu erhalten, warum der Server fehlschlägt. [Befolgen Sie diese Anleitung](../development/) um zu lernen, wie man Rhino.Compute im Debug-Modus ausführt.

### Was tue ich, wenn ich Zeitüberschreitung-Ausnahme erhalte?

Wenn Rhino.Compute den folgenden Fehler zurückgibt:

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Connection id "...", Request id "...": An unhandled exception was thrown by the application.
      System.Threading.Tasks.TaskCanceledException: The request was canceled due to the configured HttpClient.Timeout of 100 seconds elapsing.
```

Ein HTTP-Anfrage-Zeitüberschreitung tritt auf, wenn ein Client (wie Hops) innerhalb einer bestimmten Zeitspanne keine Antwort von einem Server (wie Rhino.Compute) erhält. Es gibt also zwei Werte der Zeitüberschreitung, die wir beachten sollten: 1) die Client-Zeitüberschreitung und 2) die Server-Zeitüberschreitung.

Die Einstellung der Zeitüberschreitung, die Sie in den Hops-Einstellungen sehen, steuert die clientseitige Zeitüberschreitung. Der Standardwert ist 100 Sekunden, kann aber erweitert werden, um diesen Fehler zu beheben.

{{< image url="/images/hops-timeout.png" alt="/images/hops-timeout.png" class="image_center" width="75%" >}}

Die serverseitige Zeitüberschreitung wird separat verwaltet - sie wird durch eine Umgebungsvariable auf der Maschine festgelegt, auf der der Server läuft. Gehen Sie wie folgt vor, um die Umgebungsvariable zu setzen:

1. Klicken Sie mit der rechten Maustaste auf das Symbol **Dieser PC** im Datei-Explorer und wählen Sie dann **Eigenschaften** oder **System** in der Systemsteuerung
1. Klicken Sie im Fenster der Systemeigenschaften auf **Erweiterte Systemeinstellungen**
1. Auf dem Reiter **Erweitert** klicken Sie auf **Umgebungsvariablen**
1. Klicken Sie auf die Schaltfläche **Neu**, um eine neue Systemvariable zu erstellen
1. In der Eingabe **Variablenname** geben Sie "RHINO_COMPUTE_TIMEOUT“ ein
1. Geben Sie in die Eingabe **Variablenwert** die **Sekundenzahl** ein, die Sie als serverseitigen Zeitüberschreitung-Wert verwenden möchten
1. Klicken Sie auf OK, um die Systemumgebungsvariable zu speichern, und dann erneut auf OK, um das Dialogfeld Umgebungsvariablen und das Fenster Systemeigenschaften zu schließen.

### Ich erhalte eine Fehlermeldung, die besagt, dass der Anfragekörper zu groß ist. Was soll ich tun?

Wenn Rhino.Compute den folgenden Fehler zurückgibt:

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Connection id "...", Request id "...": An unhandled exception was thrown by the application.
      Microsoft.AspNetCore.Server.Kestrel.Core.BadHttpRequestException: Request body too large.
```

Dieser Fehler kann auftreten, wenn Sie versuchen, eine große Menge an Daten im Hauptteil einer Anfrage an Rhino.Compute zu senden. Die Standardgrenze für die Größe einer Anfrage liegt bei etwa 50 MB. Um diesen Grenzwert zu erhöhen, gehen Sie folgendermaßen vor:

1. Klicken Sie mit der rechten Maustaste auf das Symbol **Dieser PC** im Datei-Explorer und wählen Sie dann **Eigenschaften** oder **System** in der Systemsteuerung
1. Klicken Sie im Fenster der Systemeigenschaften auf **Erweiterte Systemeinstellungen**
1. Auf dem Reiter **Erweitert** klicken Sie auf **Umgebungsvariablen**
1. Klicken Sie auf die Schaltfläche **Neu**, um eine neue Systemvariable zu erstellen
1. In der Eingabe **Variablenname** geben Sie "RHINO_COMPUTE_MAX_REQUEST_SIZE" ein.
1. Geben Sie in die Eingabe **Variablenwert** die **maximale Anzahl von Bytes** ein, die in einem HTTP-Anfragekörper zulässig sind. Der Standardwert ist 52.428.800 Bytes (etwa 50 MB). Erhöhen Sie diesen Wert, um größere Anfragen zuzulassen.
1. Klicken Sie auf OK, um die Systemumgebungsvariable zu speichern, und dann erneut auf OK, um das Dialogfeld Umgebungsvariablen und das Fenster Systemeigenschaften zu schließen.

<br></br>
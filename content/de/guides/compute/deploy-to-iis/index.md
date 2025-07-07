+++
aliases = ["/en/5/guides/compute/deploy-to-iis/", "/en/6/guides/compute/deploy-to-iis/", "/en/7/guides/compute/deploy-to-iis/", "/en/wip/guides/compute/deploy-to-iis/", "/en/guides/compute/deploy/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
description = "Wie man Rhino.Compute für die Produktion auf einem Rechner mit Internet Information Services (IIS) bereitstellt."
keywords = [ "developer", "compute", "production", "IIS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Verteilung auf Produktionsservern"
type = "guides"
weight = 4
override_last_modified = "2022-05-18T09:45:21Z"

[admin]
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

## Übersicht

Diese Anleitung führt Sie durch die Einrichtung einer Instanz von Rhino.Compute auf einer virtuellen Maschine mit Internet Information Services (IIS). [IIS](https://www.iis.net/) ist ein flexibler, von Microsoft entwickelter Allzweck-Webserver, der so konfiguriert werden kann, dass er angeforderte HTML-Seiten oder Dateien bereitstellt. Wir können IIS so einrichten, dass es eingehende Anfragen (entweder von Hops oder einem anderen Client) verarbeitet und diese Anfragen an die Rhino.Compute-Instanz weiterleitet. 

Sie fragen sich vielleicht: "Warum brauche ich überhaupt IIS? Warum kann ich nicht einfach den Rhino.Compute-Server starten und API-Anfragen direkt an diese Instanz senden?". In technischer Hinsicht brauchen Sie keinen IIS. Allerdings müssen Sie sich überlegen, wie Sie den Compute-Server im Falle eines Absturzes oder einer Störung neu starten können. Sie müssen Rhino.Compute auch so konfigurieren, dass es immer dann startet, wenn die virtuelle Maschine gestartet wird. 

Einer der Hauptvorteile der Verwendung von IIS als Middleware ist, dass es automatisch eine Instanz des Rhino.Compute-Servers beschleunigen kann, sobald eine Anfrage eingeht. Bei dieser Konfiguration müssen Sie den Rechner nicht ständig laufen lassen. Stattdessen kann IIS bei Bedarf eine Instanz von Compute starten, die ihrerseits einen oder mehrere untergeordnete Prozesse startet. Diese untergeordneten Prozesse führen die eigentlichen Berechnungen durch und benötigen auch Ihre Lizenzberechtigung. 

Wenn Rhino.Compute.exe über einen Zeitraum von Sekunden keine Lösungsanfragen erhält (dies wird als Idlepans bezeichnet und ist standardmäßig auf 1 Stunde eingestellt), werden die untergeordneten compute.geometry.exe-Prozesse heruntergefahren und verursachen keine Kernstundenabrechnung mehr. Irgendwann in der Zukunft, wenn eine neue Anforderung eingeht, sorgt IIS dafür, dass Rhino.Compute.exe läuft und startet dann die untergeordneten Prozesse neu. Beachten Sie, dass es zu einer kleinen Verzögerung bei der Antwort kommen kann, während die untergeordneten Prozesse gestartet werden.

{{< image url="/images/IIS_Request.png" alt="/images/IIS_Request.png" class="image_center" width="100%" >}}
<figcaption align = "left"><b>Abb.1 - Ein Flussdiagramm, das zeigt, wie IIS eine eingehende Anfrage empfängt und Rhino.Compute.exe startet, das wiederum untergeordnete Prozesse in Gang setzt.</b></figcaption>

## Voraussetzungen

Bevor Sie das Bootstrap-Skript auf Ihrem Server oder Ihrer virtuellen Maschine ausführen, benötigen Sie die folgenden Informationen.

* **`EmailAddress`** - Das Script wird diese E-Mail-Adressen verwenden, um eine Kopie von Rhino zur Installation herunterzuladen. Dies ist ähnlich wie das Verhalten der Rhino-Download-Seite.
* **`ApiKey`** - Der API-Schlüssel ist eine für Ihren Compute-Server und Ihre Anwendungen, welche die Compute API verwenden, geheime Zeichenfolge, z.B. `b8f91f04-3782-4f1c-87ac-8682f865bf1b`. Auf diese Weise stellt der Compute-Server sicher, dass die API-Aufrufe nur von Ihren Anwendungen kommen. Sie können eine beliebige Zeichenfolge eingeben, die für Sie und Ihre Computeranwendungen eindeutig und geheim ist. Bewahren Sie diese an einem sicheren Ort auf.
* **`RhinoToken`** – Dies ist ein langes Token, das Ihre Instanz von Rhino Compute für das Kernstunden-Abrechnungssystem identifiziert. Rufen Sie das [Lizenzportal](https://www.rhino3d.com/licenses?_forceEmpty=true) auf, um diese eindeutige ID auf der Grundlage Ihrer Lizenz zu erstellen. Weitere Informationen finden Sie im [Leitfaden "Abrechnung von Kernzeiten"](../core-hour-billing/) .

{{< call-out "note" "Anmerkung" >}}
Der lokale Betrieb von Rhino.Compute nutzt Ihre bestehende Rhino-Lizenz und kostet kein zusätzliches Geld (außer Ihrer ursprünglichen Investition in die Rhino-Lizenz). Das lokale Ausführen von Compute ist die beste Option für die Entwicklung und das Testen. Um mehr darüber zu erfahren, lesen Sie <a href="../development"><u>Lokales Ausführen und Debuggen von Compute</u></a>.<br><br>

Wenn Sie jedoch eine Produktionsumgebung einrichten, benötigen Sie einen Server oder eine mit dem Windows Server 2019 (oder neuer) vorinstallierte virtuelle Maschine. Die Lizenzierung funktioniert anders, wenn Rhino (d.h. über Compute) in einer Produktionsumgebung (d.h. Server-Einstellung) ausgeführt wird, und Sie werden mit einem Satz von <strong>0,10 $ pro Kern pro Stunde</strong> berechnet. <br></br>

Folgen Sie dem <a href="../core-hour-billing"><u>Leitfaden zur "Kernzeit-Fakturierung"</u></a>, um sich einzurichten. <b>Dies ist wichtig und sollte nicht übersprungen werden.</b>
{{< /call-out >}}

## Erstellen Sie die VM

Der erste Schritt im Prozess der Bereitstellung von **Rhino.Compute** für die Produktion besteht darin, entweder eine physische Maschine als Server einzurichten oder eine virtuelle Maschine (VM) zu erstellen. In dieser Anleitung verwenden wir eine virtuelle Maschine. Es gibt mehrere beliebte Dienste, die je nach Ressourcenbedarf für die Einrichtung einer Vielzahl von virtuellen Maschinen konfiguriert werden können. Zwei der bekanntesten Anbieter sind [Azure](https://azure.microsoft.com/en-us/free/virtual-machines/) und [AWS](https://aws.amazon.com/ec2/instance-types/).  

Je nach Ihren Präferenzen empfehlen wir, mit einer Azure- oder AWS-VM zu beginnen. Verwenden Sie die folgenden Anleitungen, um diesen Prozess zu durchlaufen.

* * [Erstellen einer virtuellen Maschine auf Azure](../creating-an-Azure-VM).

* * [Erstellen einer virtuellen Maschine auf AWS](../creating-an-aws-vm).

### Verbindung über RDP

Nun, da wir die virtuelle Maschine konfiguriert haben, müssen wir in der Lage sein, uns bei ihr anzumelden, damit wir IIS und die Rhino.Compute-Instanz einrichten können. Dazu verwenden wir ein Remote-Desktop-Protokoll (RDP), das zwei Computer über ein Netzwerk miteinander verbindet.

Lassen Sie uns zunächst die RDP-Datei herunterladen. Wir verwenden das Azure VM Portal, aber ein ähnlicher Prozess wird für AWS verwendet.

1. Stellen Sie zunächst sicher, dass die virtuelle Maschine in Betrieb ist. Klicken Sie auf den Reiter **Übersicht** im linken Menü. Vorausgesetzt, der *Status* lautet *Angehalten (Freigegeben)*, klicken Sie oben auf die Schaltfläche **Start**, um den remoten Rechner zu starten. Nach einigen Sekunden sollte *Läuft* als Status angezeigt werden.

1. Klicken Sie auf den Menüpunkt **Verbinden** im linken Menü, um das Einstellungsblatt für die Verbindung aufzurufen.

1. Klicken Sie auf die Schaltfläche **RDP-Datei herunterladen** und speichern Sie die Datei irgendwo auf Ihrem Computer.
{{< image url="/images/Azure_VM_Connect1.png" alt="/images/Azure_VM_Connect1.png" class="image_center" width="100%" >}}

1. Klicken Sie auf das **Start**-Menü von Windows und geben Sie *Remotedesktopverbindung* in die Suchleiste ein. Klicken Sie auf den Link, um die App zu starten.

1. Klicken Sie auf die Schaltfläche **Optionen anzeigen** am unteren Rand der Anwendung.

1. Im Bereich *Verbindungseinstellungen* wählen Sie **Öffnen** und navigieren Sie zu dem Verzeichnis, in dem Sie Ihre RDP-Datei gespeichert haben. Wählen Sie diese Datei aus und klicken Sie auf Öffnen.

1. Aktivieren Sie das Kontrollkästchen, um **Zugangsdaten speichern** zu können.

1. Klicken Sie auf **Verbinden**.
{{< image url="/images/Azure_VM_Connect2.png" alt="/images/Azure_VM_Connect2.png" class="image_center" width="60%" >}}

1. Ein Sicherheits-Pop-up wird geöffnet. Klicken Sie auf das Kontrollkästchen **Nicht mehr nach Verbindungen zu diesem Computer fragen** und dann auf **Verbinden**.

1. Geben Sie die Administrator-Anmeldedaten ein, die Sie in Schritt 7 von [Erstellen einer virtuellen Maschine](../deploy-to-iis/#setting-up-a-virtual-machine) eingegeben haben.

1. Möglicherweise wird ein weiteres Sicherheits-Pop-up angezeigt. Wählen Sie erneut **Nicht erneut nach Verbindungen zu diesem Computer fragen** und klicken Sie auf **Ja**.

Herzlichen Glückwunsch. Sie sollten nun Zugriff auf den Desktop des Remotecomputers mit Windows Server 2019 oder neuer haben.

## Ausführen des Bootstrap-Skripts
Angenommen, Sie sind jetzt in der virtuellen Maschine angemeldet (mit RDP), befolgen Sie die folgenden Schritte, um Rhino.Compute hinter IIS zu installieren. Hinweis: Für die folgenden Schritte wird davon ausgegangen, dass es sich um eine Installation auf einer neuen virtuellen Maschine oder einem neuen Server handelt (d.h. Rhino.Compute wurde vorher noch nicht auf dieser Maschine installiert). Wenn Sie Rhino.Compute und IIS bereits auf dieser Maschine eingerichtet haben und Rhino und/oder Rhino.Compute auf dieser VM aktualisieren müssen, fahren Sie bitte mit dem Abschnitt [Aktualisierung von Rhino Compute](../deploy-to-iis/#updating-the-deployment) fort.

### Schritt 1

1. Klicken Sie auf das Windows-Startmenü und geben Sie "Powershell" ein. Klicken Sie im angezeigten Menü mit der rechten Maustaste auf die Anwendung **Windows Powershell** und wählen Sie **Als Administrator ausführen**.
{{< image url="/images/powershell_1.png" alt="/images/powershell_1.png" class="image_center" width="50%" >}}

1. Nach dem **Kopieren und Einfügen** des untenstehenden Befehls in den Powershell-Prompt betätigen Sie die **Eingabetaste**. Durch diesen Befehl wird das neueste Bootstrap-Skript für Schritt 1 heruntergeladen und Rhino und IIS auf Ihrer VM installiert. Hinweis: Sie werden aufgefordert, Ihre **E-Mail-Adresse**, Ihren **API-Schlüssel** und Ihr **Rhino-Token** einzugeben, halten Sie diese Informationen also bitte bereit.
    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-1')">Rhino 7: Schritt 1</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-1')" id="defaultOpen1">Rhino 8: Schritt 1</button>
    </div>

    <div class="tab-content">
    <div class="codetab-content1" id="r7-1">

    ```powershell
    $F="/bootstrap_step-1.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/bootstrap_step-1.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-1\boostrap_step-1.ps1" 
    ```

    </div>

    <div class="codetab-content1" id="r8-1">

    ```powershell
    $F="/bootstrap_step-1.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/bootstrap_step-1.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-1\boostrap_step-1.ps1" 
    ```

    </div>
    </div>

1. Am Ende von Schritt 1 wird Ihre VM automatisch neu gestartet (Sie werden bei Remote Desktop abgemeldet).

### Schritt 2

1. Melden Sie sich mit Remote Desktop wieder bei Ihrer VM an.

1. Öffnen Sie eine neue Instanz von **Windows Powershell**. Versichern Sie sich, mit der rechten Maustaste auf die Datei zu klicken und **Als Administrator ausführen** auszuwählen.

1. Nach dem **Kopieren und Einfügen** des untenstehenden Befehls in den Powershell-Prompt betätigen Sie die **Eingabetaste**. Durch diesen Befehl wird das neueste Bootstrap-Skript für Schritt 2 heruntergeladen und IIS für die Funktion mit Rhino.Compute konfiguriert.
    <div class="codetab">
      <button class="tablinks2" onclick="openCodeTab(event, 'r7-2')">Rhino 7: Schritt 2</button>
      <button class="tablinks2" onclick="openCodeTab(event, 'r8-2')" id="defaultOpen2">Rhino 8: Schritt 2</button>
    </div>

    <div class="tab-content">
    <div class="codetab-content2" id="r7-2">

    ```powershell
    $F="/bootstrap_step-2.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/bootstrap_step-2.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-2\boostrap_step-2.ps1"
    ```

    </div>

    <div class="codetab-content2" id="r8-2">

    ```powershell
    $F="/bootstrap_step-2.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/bootstrap_step-2.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\bootstrap_step-2\boostrap_step-2.ps1"
    ```

    </div>
    </div>

1. Am Ende des Installationsskripts von Schritt 2 erscheint jetzt normalerweise die Meldung *Glückwunsch! Alle Komponenten sind nun installiert.* Danach folgen einige Anweisungen zur Installation von Plug-ins von Drittanbietern, damit diese mit Rhino.Compute richtig funktionieren. Bitte beachten Sie den neuen **Benutzernamen** und das **Passwort**, die beim erneuten Einloggen zur Installation eines zusätzlichen Plug-ins benötigt werden.

## Testen der App

Zu diesem Zeitpunkt sollte IIS so konfiguriert sein, dass die Rhino.Compute-Instanz gestartet wird, wenn eine API-Anfrage gestellt wird. Versuchen wir nun, Hops dazu zu bringen, eine Definition an die URL unserer virtuellen Maschine zu senden. 

1. Starten Sie **Rhino** auf Ihrem lokalen Rechner.

1. Wenn Sie Hops noch nicht auf diesem Rechner installiert haben, tun Sie dies bitte, indem Sie im Rhino-**Paketmanager** danach suchen.

1. Starten Sie **Grasshopper**, indem Sie das Wort *Grasshopper* in die Befehlseingabeaufforderung eingeben und die Eingabetaste drücken.

1. Gehen Sie auf **File** und dann **Preferences**, um den Einstellungsdialog zu öffnen. 

1. Klicken Sie auf den Reiter **Solver** im linken Menü 

1. Geben Sie im Abschnitt **Hops - Compute server URLs** die Webadresse Ihrer virtuellen Maschine ein. Beginnen Sie mit der Eingabe von `http://`, gefolgt von der IP-Adresse des virtuellen Rechners, gefolgt von einem `:` und der Portnummer `80`. Die vollständige Adresse würde also etwa so aussehen:
            
        http://52.168.38.105:80/

1. Geben Sie im Abschnitt **API-Schlüssel** den API-Schlüssel ein, den Sie im Abschnitt [Voraussetzungen](../deploy-to-iis/#prerequisites) gespeichert haben.
{{< image url="/images/Hops_To_IIS_4.png" alt="/images/Hops_To_IIS_4.png" class="image_center" width="80%" >}}

1. Fügen Sie eine **Hops**-Komponente auf der **Grasshopper-Arbeitsfläche** (Params/Util) hinzu.

1. Klicken Sie mit der rechten Maustaste auf die Komponente **Hops** und setzen Sie den **Pfad** auf eine gültige Hops/Grasshopper-Definition. Um mehr darüber zu erfahren, wie man eine Grasshopper-Definition einrichtet, die korrekt mit Hops funktioniert, [befolgen Sie diese Anleitung](../hops-component/).
{{< image url="/images/Hops_To_IIS_2.png" alt="/images/Hops_To_IIS_2.png" class="image_center" width="50%" >}}

Sobald der Pfad festgelegt ist, erstellt die Hops-Komponente die entsprechende API-Anfrage und sendet sie an die URL, die wir in Schritt 6 angegeben haben (den Rhino.Compute-Server, der auf IIS läuft). Der Compute-Server verarbeitet die Anfrage und sendet eine Antwort zurück an Hops, der das Ergebnis zurückgibt.
{{< image url="/images/Hops_To_IIS_3.png" alt="/images/Hops_To_IIS_3.png" class="image_center" width="70%" >}}

Herzlichen Glückwunsch! Sie haben erfolgreich eine Instanz von Rhino.Compute eingerichtet, die hinter IIS auf einer virtuellen Maschine läuft. 

## Ändern von Compute-Parametern nach der Bereitstellung

Es gibt eine Reihe von Befehlszeilenargumenten, die verwendet werden können, um das Verhalten von Rhino.Compute zu ändern. Dieser Abschnitt beschreibt, wie Sie diese Parameter nach der Bereitstellung von Rhino.Compute ändern können.

1. Melden Sie sich bei Ihrer VM an (über RDP). Weitere Einzelheiten finden Sie im Abschnitt [Verbindung über RDP](#connect-via-rdp) .

1. Klicken Sie im Menü **Start** in das Suchfeld und geben Sie *Internet Information Services (IIS) Manager* ein. Klicken Sie, um die App zu starten.

1. Im IIS Manager, **klicken Sie** auf den Webserverknoten im Panel **Verbindungen** auf der linken Seite. Beachten Sie, dass dieser Webservername derselbe sein sollte, den Sie beim Einrichten des Namens Ihrer virtuellen Maschine verwendet haben. 

1. Klicken Sie im Bereich **Aktionen** auf der rechten Seite auf **Anhalten**, um den Webserver anzuhalten.
{{< image url="/images/iis_manager.png" alt="/images/iis_manager.png" class="image_center" width="100%" >}}

Nun, da der IIS-Webserver gestoppt wurde, müssen wir die Datei **web.config* für Rhino.Compute ändern. Die Datei [web.config](https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/web-config?view=aspnetcore-6.0) ist eine Datei, die von IIS und dem ASP.NET Core-Modul gelesen wird, um einen von IIS gehosteten Server zu konfigurieren. 

1. Öffnen Sie ein **Dateiexplorer**-Fenster und navigieren Sie zu *C:\inetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute*. Am Ende dieses Verzeichnisses sollten Sie eine Datei mit dem Namen **web.config** finden. Beachten Sie, dass Sie möglicherweise auf die Registerkarte **Ansicht** klicken und das Kontrollkästchen **Dateinamenerweiterungen** aktivieren müssen. Öffnen Sie die Datei web.config mit **Notepad** oder einem anderen Texteditor Ihrer Wahl.

Die vollständige web.config-Datei sollte ungefähr so aussehen:

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.webServer>
    <handlers>
      <add name="aspNetCore" path="*" verb="*" modules="AspNetCoreModuleV2" resourceType="Unspecified"/>
    </handlers>
    <aspNetCore processPath=".\rhino.compute.exe" arguments="--port 80" stdoutLogEnabled="true" stdoutLogFile="..\..\..\..\..\logs\LogFiles\W3SVC1\" forwardWindowsAuthToken="true" hostingModel="InProcess"/>
  </system.webServer>
</configuration>
```
Die Zeile, an deren Änderung wir am meisten interessiert sind, ist diejenige, die mit der Beschriftung **`<aspNetCore>`** beginnt. Wie Sie sehen, wird der zweite Parameter in dieser Zeile **`arguments`** genannt. Dies ist der Abschnitt, den Sie bearbeiten würden, um andere Befehlszeilenargumente zum Ändern von Rhino.Compute hinzuzufügen. 

Nachfolgend finden Sie eine Beschreibung der einzelnen Befehlszeilenargumente, die geändert werden können.

- **port** - Dies ist die Portnummer, unter der Rhino.Compute ausgeführt wird. Die Portnummer 80 ist normalerweise für die HTTP-Kommunikation reserviert, während Portnummer 443 für das HTTPS-Protokoll verwendet wird. Wir haben Rhino.Compute so eingerichtet, dass es im Bootstrap-Skript an Port 80 gebunden ist, also ändern Sie diesen Wert nicht, wenn Sie sich Ihrer Sache nicht hunderprozentig sicher sind. Beispiel für die Verwendung: `--port 80`.

- **childcount** - Dieser Parameter steuert die Anzahl der zu verwaltenden Untergeordneten-Prozesse von compute.geometry. Der *Standardwert ist 4*, was bedeutet, dass Rhino.Compute vier Untergeordneten-Prozesse erzeugen wird, von denen jeder eingehende Anfragen bearbeiten kann. Beispiel für die Verwendung: `--childcount 8` würde Rhino.Compute anweisen, acht Untergeordneten-Prozesse zu starten.

- **childof** - Dies ist die Handhabe des Übergeordneten-Prozesses. Compute überprüft das Vorhandensein 
dieser Handhabe und wird beendet, wenn dieser Prozess beendet ist. Da wir uns darauf verlassen, dass IIS Rhino.Compute startet und anhält, benötigen Sie diesen Parameter nicht, wenn Sie in einer Produktionsumgebung arbeiten.

- **spawn-on-startup** - Dieses Flag bestimmt, ob ein untergeordneter compute.geometry-Prozess gestartet werden soll, wenn Rhino.Compute gestartet wird. Der *Standardwert ist False*. Bei diesem Parameter handelt es sich um ein Flag, d. h. wenn er nicht in der Argumentliste enthalten ist, ist der Wert falsch. Wenn Sie diesen Parameter angeben, ist sein Wert True. In Produktionsumgebungen sollte dieser Wert False bleiben.

- **idlespan** - Dies ist die Anzahl der Sekunden, die ein untergeordneter compute.geometry-Prozess zwischen Anfragen offen bleiben soll. Der *Standardwert ist 1 Stunde*. Wenn Rhino.Compute.exe über einen Zeitraum von `idlespan` Sekunden keine Lösungsanfragen erhält, werden die untergeordneten compute.geometry.exe-Prozesse heruntergefahren und stellen die Abrechnung der Kernstunden ein. Wenn irgendwann in der Zukunft eine neue Anforderung eingeht, werden die untergeordneten Prozesse neu gestartet, was zu einer kleinen Verzögerung bei den Anforderungen führt, während die untergeordneten Prozesse gestartet werden. Beispiel für die Verwendung: `--idlespan 1800` würde Rhino.Compute anweisen, die Untergeordnetenprozesse nach 30 Minuten abzuschalten (30 Minuten x 60 Sekunden = 1800).

    Wenn Sie den Wert `idlespan` in den Befehlszeilenargumenten für Rhino.Compute ändern, müssen Sie auch eine Änderung an der IIS-Konfiguration vornehmen. Das liegt daran, dass IIS auch eine Einstellung enthält, die Rhino.Compute herunterfährt, wenn nach einer gewissen Zeit keine neuen Anfragen eingehen. Wenn Rhino.Compute heruntergefahren wird, werden auch alle untergeordneten Prozesse heruntergefahren. 

    Angenommen, Sie ändern den Wert für `idlespan` auf 7.200 (2 Stunden). Das Bootstrap-Skript setzt den IIS-"IdleTimeout"-Wert auf 65 Minuten (etwas länger als der `idlespan`-Standardwert). Nach 65 Minuten würde IIS Rhino.Compute herunterfahren, das dann alle seine untergeordneten Prozesse viel früher als die erwartete 2-Stunden-Frist herunterfahren würde. Wenn Sie also den `idlespan`-Wert ändern, sollten Sie auch den Wert `IdleTimeout`" in den IIS-Einstellungen ändern.

    1. Gehen Sie dazu zurück zum IIS-Manager und klicken Sie auf den Eintrag **Application Pools** im Bereich **Connections** auf der linken Seite. 
    
    1. Klicken Sie im mittleren Fenster auf den **RhinoComputeAppPool**.

    1. Klicken Sie im Bereich **Actions** auf der rechten Seite auf **Advanced Settings**.

    1. Suchen Sie die Zeile **Idle Time-out** unter dem Abschnitt **Process Model** und ändern Sie den Wert für die Leerlaufzeit so, dass er etwas länger ist als der in den Befehlszeilenargumenten angegebene Wert für `idlespan`. Hinweis: Der Wert `idlespan` wird in Sekunden und der Wert `Idle Timeout` in Minuten angegeben.
    {{< image url="/images/iis_idletimout.png" alt="/images/iis_idletimout.png" class="image_center" width="60%" >}}

Sobald Sie die Datei web.config geändert haben, **speichern** Sie sie und schließen Sie die Datei. Sie können dann zum IIS-Manager zurückkehren und den Webserver **starten**, indem Sie auf den Webserverknoten im Bereich **Connections** auf der linken Seite und auf **Start** im Bereich **Actions** auf der rechten Seite klicken.

## Aktualisierung der Verteilung
Wenn Sie Rhino.Compute bereits auf diesem Rechner eingerichtet haben, kann es sein, dass Sie Rhino und/oder die Rhino.Compute-Build-Dateien regelmäßig auf die neueste Version aktualisieren müssen. Führen Sie die folgenden Schritte aus, um diese Anwendungen zu aktualisieren.

### Rhino aktualisieren

1. Klicken Sie auf das Windows-Startmenü und geben Sie "Powershell" ein. Klicken Sie im angezeigten Menü mit der rechten Maustaste auf die Anwendung **Windows Powershell** und wählen Sie **Als Administrator ausführen**.

1. Nach dem **Kopieren und Einfügen** des untenstehenden Befehls in den Powershell-Prompt betätigen Sie die **Eingabetaste**. Mit diesem Befehl wird die neueste Version von Rhino für Windows heruntergeladen. Hinweis: Sie werden aufgefordert, Ihre **E-Mail-Adresse** einzugeben, halten Sie diese Information also bitte bereit.

    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-3')">Update auf die neueste Rhino-7-Installation</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-3')" id="defaultOpen3">Update auf die neueste Rhino-8-Installation</button>
    </div>

    <div class="tab-content">
    <div class="codetab-content1" id="r7-3">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/module_update_rhino.ps1 -outfile update_rhino.ps1; .\update_rhino.ps1 
    ```

    </div>

    <div class="codetab-content1" id="r8-3">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/module_update_rhino.ps1 -outfile update_rhino.ps1; .\update_rhino.ps1 
    ```

    </div>
    </div>

### Compute aktualisieren

1. Klicken Sie auf das Windows-Startmenü und geben Sie "Powershell" ein. Klicken Sie im angezeigten Menü mit der rechten Maustaste auf die Anwendung **Windows Powershell** und wählen Sie **Als Administrator ausführen**.

1. Nach dem **Kopieren und Einfügen** des untenstehenden Befehls in den Powershell-Prompt betätigen Sie die **Eingabetaste**. Mit diesem Befehl wird die neueste Version von Rhino.Compute heruntergeladen.

    <div class="codetab">
      <button class="tablinks1" onclick="openCodeTab(event, 'r7-4')">Rhino.Compute für Rhino 7 aktualisieren</button>
      <button class="tablinks1" onclick="openCodeTab(event, 'r8-4')" id="defaultOpen4">Rhino.Compute für Rhino 8 aktualisieren</button>
    </div>

    <div class="tab-content">
    <div class="codetab-content1" id="r7-4">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/7.x/script/production/module_update_compute.ps1 -outfile update_compute.ps1; .\update_compute.ps1 
    ```

    </div>

    <div class="codetab-content1" id="r8-4">

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/8.x/script/production/module_update_compute.ps1 -outfile update_compute.ps1; .\update_compute.ps1 
    ```

    </div>
    </div>

 
## Quick Links

 - [Was ist Hops?](../what-is-hops)
 - [Wie funktioniert Hops?](../how-hops-works)
 - [Die Hops-Komponente](../hops-component)

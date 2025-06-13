+++
aliases = ["/en/5/guides/compute/configure-https/", "/en/6/guides/compute/configure-https/", "/en/7/guides/compute/configure-https/", "/en/wip/guides/compute/configure-https/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "AWS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Compute für die Verwendung von HTTPS konfigurieren"
type = "guides"
weight = 5
override_last_modified = "2025-02-25T08:16:19Z"

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

In dieser Anleitung werden wir den Prozess der Erstellung eines gültigen SSL-Zertifikats durchlaufen, damit Rhino.Compute mit Clients über das HTTPS-Protokoll kommunizieren kann.

## Voraussetzungen

Die folgenden Angaben müssen ausgefüllt werden:

1. Sie müssen über eine aktive Instanz einer virtuellen Maschine (VM) verfügen. Verwenden Sie die folgenden Anleitungen, um die Einrichtung einer VM zu erläutern.

    * [Erstellen einer virtuellen Maschine auf Azure](../creating-an-Azure-VM).
    * [Erstellen einer virtuellen Maschine auf AWS](../creating-an-aws-vm).

1. Die VM muss für das Web zugänglich sein (Port 80 und 443 öffnen).

1. Eine statische öffentliche IPv4-Adresse muss mit Ihrer virtuellen Maschine verknüpft sein. Weitere Informationen zur Konfiguration statischer IP-Adressen finden Sie unter den folgenden Links:
    * [Konfigurieren von IP-Adressen für eine Azure-Netzwerkschnittstelle](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/virtual-network-network-interface-addresses?tabs=nic-address-portal#add-ip-addresses)
    * [Zuordnen einer elastischen IP-Adresse zu einer EC2-Instanz](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)

1. Sie müssen über eine bestehende Domäne verfügen und Zugriff auf deren DNS-Einstellungen haben. Ein **A-Eintrag** in Ihren DNS-Einstellungen muss auf die öffentliche IPv4-Adresse Ihrer virtuellen Maschine zeigen.

{{< call-out "note" "Anmerkung" >}}
Für diese Anleitung habe ich eine elastische IP-Adresse mit meiner virtuellen Maschineninstanz verknüpft. Ich habe auch einen A-Eintrag in meinen DNS-Einstellungen eingerichtet, um *rhino.compute.rhino3d.com* auf die IP-Adresse meiner virtuellen Maschine zu verweisen.
{{< /call-out >}}

## Ändern Sie den Hostnamen

Bevor wir den Prozess der Erstellung eines SSL-Zertifikats durchlaufen, müssen wir eine Änderung an unserer bestehenden IIS-Konfiguration für Rhino.Compute vornehmen.

1. Falls Sie dies noch nicht getan haben, melden Sie sich bei Ihrer VM an (über RDP). Weitere Einzelheiten finden Sie im Abschnitt [Verbindung über RDP](../deploy-to-iis/#connect-via-rdp) .

1. Klicken Sie im Menü **Start** in das Suchfeld und geben Sie *Internet Information Services (IIS) Manager* ein. Klicken Sie, um die App zu starten.

1. Im IIS Manager, **klicken Sie** auf den Webserverknoten im Panel **Connections** auf der linken Seite, um den Menübaum zu erweitern. Dann **klicken Sie** auf den Knoten **Sites**, um das Untermenü zu erweitern. Wählen Sie schließlich den Knoten **Rhino.Compute** aus dem Menübaum, um seine Einstellungen anzupassen.

1. Klicken Sie im Bereich **Actions** auf der rechten Seite auf **Bindings**. {{< image url="/images/Site_Binding_2.png" alt="/images/Site_Binding_2.png" class="image_center" width="100%" >}}

1. Wählen Sie im Bereich **Site Bindings** die Schaltfläche **Add** . {{< image url="/images/Site_Binding_3.png" alt="/images/Site_Binding_3.png" class="image_center" width="100%" >}}

1. Geben Sie in das Textfeld **Host name** den Namen der Subdomain ein, die Sie beim Einrichten des A-Records erstellt haben. Klicken Sie auf **OK**, wenn Sie fertig sind.
{{< image url="/images/Site_Binding_1.png" alt="/images/Site_Binding_1.png" class="image_center" width="80%" >}}

1. Hier angekommen, sollten Sie zwei Website-Bindungen aufgelistet haben. Klicken Sie auf **Close**, wenn Sie fertig sind. {{< image url="/images/Site_Binding_4.png" alt="/images/Site_Binding_4.png" class="image_center" width="100%" >}}

## Erzeugen des Zertifikats

Der nächste Schritt im Prozess ist die Erstellung und Installation eines SSL-Zertifikats für den lokalen IIS-Server. Ein SSL-Zertifikat ist ein digitales Zertifikat, das die Identität einer Website bestätigt und eine verschlüsselte Verbindung ermöglicht. Sie ist erforderlich, um das HTTPS-Protokoll zu verwenden.

Zur Erstellung des Zertifikats empfehlen wir [Win-ACME](https://www.win-acme.com/). Win-ACME ist ein einfacher interaktiver Client, der das Zertifikat erstellen und installieren kann und bei Bedarf die Erneuerung des Zertifikats übernimmt.

1. [Laden Sie den Win-ACME Client](https://github.com/win-acme/win-acme/releases/download/v2.2.2.1449/win-acme.v2.2.2.1449.x64.pluggable.zip) auf die virtuelle Maschine herunter. Hinweis: Win-ACME wird als .zip-Datei verteilt.

1. Klicken Sie mit der rechten Maustaste auf die heruntergeladene .zip-Datei und wählen Sie **Alles extrahieren**. Es spielt keine Rolle, in welches Verzeichnis Sie die Dateien extrahieren, da wir sie im nächsten Schritt manuell verschieben/umbenennen werden. Klicken Sie auf **Extrahieren**.

1. Wählen Sie das neu extrahierte Verzeichnis aus und drücken Sie **Strg+X** zum **Ausschneiden**, und dann **Strg+V** zum **Einfügen** dieses Ordners in das Stammlaufwerk <i>C:\</i>. 

1. Klicken Sie nun mit der rechten Maustaste auf das Verzeichnis, das Sie gerade auf das Laufwerk <i>C:\\</i> kopiert haben, und wählen Sie **Umbenennen** aus dem Menü. Kürzen Sie den Ordnernamen auf *"win-acme"*. 
{{< image url="/images/win_acme_1.png" alt="/images/win_acme_1.png" class="image_center" width="100%" >}}

1. Klicken Sie auf das Windows-Startmenü und geben Sie "Powershell" ein. Klicken Sie im angezeigten Menü mit der rechten Maustaste auf die Anwendung **Windows Powershell** und wählen Sie **Als Administrator ausführen**.

1. Geben Sie den folgenden Befehl ein und drücken Sie die **Eingabetaste**, um die Anwendung Win-ACME zu starten.
```powershell
    C:\win-acme\wacs.exe
```
1. Es sollte ein interaktives Menü mit einer Reihe von Anweisungen erscheinen, die durch Eingabe eines bestimmten Buchstabens ausgeführt werden können.
{{< image url="/images/win_acme_7.png" alt="/images/win_acme_7.png" class="image_center" width="100%" >}} 

1. Geben Sie den Buchstaben **N** ein und drücken Sie die **Eingabetaste**, um ein Zertifikat mit den Standardeinstellungen zu erstellen. Sie sollten eine Liste der verfügbaren IIS-Sites sehen, die verfügbar sind. Wenn Sie keinen Eintrag für **Rhino.Compute (1 Binding)** sehen, dann haben Sie wahrscheinlich den Hostnamen im vorherigen Schritt nicht richtig gesetzt. Siehe den Abschnitt [Ändern des Hostnamens](#modify-the-host-name).
{{< image url="/images/win_acme_8.png" alt="/images/win_acme_8.png" class="image_center" width="100%" >}} 

1. Geben Sie die Nummer der Zeile für **Rhino.Compute (1 Binding)** ein und drücken Sie die **Eingabetaste**.
{{< image url="/images/win_acme_9.png" alt="/images/win_acme_9.png" class="image_center" width="100%" >}} 

1. Drücken Sie die **Eingabetaste** erneut, um die Standardeinstellung **Pick all bindings** zu akzeptieren.

1. Wenn die Frage *Mit dieser Auswahl fortzufahren?* Erscheint, drücken Sie die **Eingabetaste** oder geben Sie **J** für Ja ein.
{{< image url="/images/win_acme_10.png" alt="/images/win_acme_10.png" class="image_center" width="100%" >}} 

1. Während das SSL-Zertifikat generiert wird, sollten Sie einige Informationen auf der Konsole sehen.
{{< image url="/images/win_acme_11.png" alt="/images/win_acme_11.png" class="image_center" width="100%" >}} 

Herzlichen Glückwunsch. Bei Erfolg führt die Anwendung dann eine Reihe von Autorisierungs- und Validierungstests durch, um zu bestätigen, dass der Host sicher ist. Win-ACME generiert dann das SSL-Zertifikat und installiert es mit IIS und fügt eine neue Bindung **(*:443)** zur Rhino.Compute-Site hinzu. Das SSL-Zertifikat hat eine Gültigkeit von 90 Tagen. Die Win-ACME-Anwendung wird jedoch einen Aufgabenplaner erstellen, der versucht, das Zertifikat nach 60 Tagen zu erneuern. Sie sollten jetzt in der Lage sein, eine HTTPS-Anfrage an Ihren Rhino.Compute-Server zu senden und eine gültige Antwort zurückzuerhalten.

<br>

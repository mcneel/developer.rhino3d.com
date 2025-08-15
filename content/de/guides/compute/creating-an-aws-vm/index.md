+++
aliases = ["/en/5/guides/compute/creating-an-aws-vm/", "/en/6/guides/compute/creating-an-aws-vm/", "/en/7/guides/compute/creating-an-aws-vm/", "/en/wip/guides/compute/creating-an-aws-vm/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "AWS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Wie man eine virtuelle Maschine (VM) auf Amazon Web Service erstellt"
type = "guides"
weight = 3
override_last_modified = "2021-12-14T13:16:19Z"

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

In diesem Leitfaden werden wir den Prozess der Einrichtung einer virtuellen Maschine mit Amazon Elastic Compute Cloud (Amazon EC2) erläutern. 

Um zu beginnen, müssen Sie Ihr AWS-Abonnement bestätigen. Wenn Sie neu bei AWS sind, können Sie mit Amazon EC2 unter Verwendung des [AWS Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all) beginnen. 

{{< call-out "note" "Anmerkung" >}}
Wenn Sie Ihr AWS-Konto vor weniger als 12 Monaten erstellt und die Vorteile der kostenlosen Stufe für Amazon EC2 noch nicht überschritten haben, kostet Sie die Teilnahme an diesem Tutorial nichts. Andernfalls fallen die üblichen Amazon EC2-Nutzungsgebühren ab dem Zeitpunkt an, an dem Sie die Instanz starten, bis Sie die Instanz beenden, auch wenn sie im Leerlauf bleibt.
{{< /call-out >}}

## Voraussetzungen

1. [Erstellen Sie ein Konto für AWS](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#sign-up-for-aws)

1. [Erstellen Sie ein Schlüsselpaar](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-key-pair). Hinweis: Wir empfehlen, die **private Schlüsseldatei** im **.pem**-Format mit **RSA**-Verschlüsselung zu speichern.

1. [Eine Sicherheitsgruppe anlegen](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-base-security-group). Wir empfehlen, eine Regel für **HTTP**, **HTTPS**, **RDP** und **Alle ICMP - IPv4** hinzuzufügen.

## Starten Sie die Instanz

Gehen Sie folgendermaßen vor, um eine neue Instanz einer virtuellen Maschine auf AWS zu erstellen:

1. Öffnen Sie die [Amazon-EC2-Konsole](https://console.aws.amazon.com/ec2/).

1. Wählen Sie auf dem Dashboard der EC2-Konsole **Instanz starten**.

1. Geben Sie einen Namen für die VM-Instanz ein. Für dieses Tutorial werden wir den Namen **"RhinoComputeVM“** verwenden.

1. Klicken Sie im Abschnitt Anwendungs- und Betriebssystem-Images unter dem Reiter "Schnellstart" auf die Schaltfläche **Windows**. Unter dem Abschnitt Amazon Machine Image (AMI) sollte sich ein Dropdown-Menü befinden, in dem alle verfügbaren Machine Images aufgelistet sind. Wählen Sie das AMI für **Microsoft Windows Server 2022 Base**.</p>
{{< image url="/images/AWS_Setup_11.png" alt="/images/AWS_Setup_11.png" class="image_left" width="90%" >}}

1. Im Abschnitt **Instanztyp** wählen Sie den Instanztyp **t2.micro** (Standard), oder einen größeren Instanztyp falls erforderlich. Hinweis: Der Instanztyp *t2.micro* ist für den kostenlosen Tier geeignet. In Regionen, in denen *t2.micro* nicht verfügbar ist, können Sie eine *t3.micro**-Instanz im Rahmen des kostenlosen Tiers verwenden.</p>
{{< image url="/images/AWS_Setup_12.png" alt="/images/AWS_Setup_12.png" class="image_left" width="90%" >}}

1. Wählen Sie im Abschnitt **Schlüsselpaar (Anmeldung)** den Namen des Schlüsselpaars, das Sie in Schritt 2 des Abschnitts [Voraussetzungen](../creating-an-aws-vm/#prerequisites) erstellt haben, aus der Dropdown-Liste.</p>
{{< image url="/images/AWS_Setup_13.png" alt="/images/AWS_Setup_13.png" class="image_left" width="90%" >}}

1. Wählen Sie im Abschnitt **Netzwerkeinstellungen** unter **Firewall (Sicherheitsgruppen)** das Optionsfeld **Vorhandene Sicherheitsgruppe auswählen**. Wählen Sie dann unter der Dropdown-Liste **Gemeinsame Sicherheitsgruppen** die Sicherheitsgruppe aus, die Sie in Schritt 3 des Abschnitts [Voraussetzungen](../creating-an-aws-vm/#prerequisites) erstellt haben.{{< call-out "warning" "Wichtig" >}}Wenn die Einstellung **Öffentliche IP automatisch zuweisen** auf **Deaktiviert** gesetzt ist, klicken Sie auf die Schaltfläche **Bearbeiten** oben rechts in diesem Abschnitt und ändern Sie diese Einstellung auf **Aktiviert**.{{< /call-out >}}
{{< image url="/images/AWS_Setup_14.png" alt="/images/AWS_Setup_14.png" class="image_left" width="90%" >}}

1. Wählen Sie im Abschnitt **Speicher konfigurieren** die Standardmenge an Speicherplatz für diese Instanz.

1. Wählen Sie nun ganz rechts die Schaltfläche **Instanz starten**.

1. Eine Bestätigungsseite informiert Sie darüber, dass Ihre Instanz erfolgreich gestartet wurde. Wählen Sie im obersten Menü **EC2 > Instanzen > Eine Instanz starten** den Menüpunkt **Instanzen**, um das Konsolenfenster der Instanzen anzuzeigen.</p>
{{< image url="/images/AWS_Setup_15.png" alt="/images/AWS_Setup_15.png" class="image_left" width="90%" >}}

1. Auf dem Bildschirm **Instanzen** können Sie den Status der gestarteten Instanz einsehen. Die Instanz sollte nach dem Start automatisch laufen; falls nicht, aktivieren Sie das Kontrollkästchen Instanzreihe und wählen Sie dann den Menüpunkt **Instanzstatus** ganz oben. Wählen Sie **Instanz starten**, um die virtuelle Maschine zu starten.

1. Klicken Sie bei ausgewählter Instanzzeile im oberen Menü auf die Schaltfläche **Verbinden**.

1. Wählen Sie auf der Seite **Mit Instanz verbinden** den Reiter **RDP-Client** .

1. Wählen Sie dann die Schaltfläche **Kennwort anfordern** .

1. Wählen Sie **Private Schlüsseldatei hochladen** und navigieren Sie zu der privaten Schlüsseldatei (.pem), die Sie beim Start der Instanz erstellt haben.

1. Wählen Sie **Passwort entschlüsseln**. Die Konsole zeigt das Standard-Administratorkennwort für die Instanz unter **Kennwort** an und ersetzt damit den zuvor angezeigten Link **Kennwort abfragen**. **Speichern Sie dieses Passwort an einem sicheren Ort**. Dieses Kennwort ist erforderlich, um eine Verbindung zur Instanz herzustellen.

1. Wählen Sie **Remote-Desktop-Datei herunterladen**, um die .rdp-Datei auf Ihrem lokalen Computer zu speichern. Sie benötigen diese Datei, wenn Sie eine Verbindung zu Ihrer Instanz mit der App Remote Desktop Connect herstellen.

Herzlichen Glückwunsch! In diesem Lernprogramm haben Sie erfolgreich eine virtuelle Maschine auf AWS gestartet und die RDP-Datei heruntergeladen, mit der Sie die Verbindung mit dieser Instanz herstellen können.
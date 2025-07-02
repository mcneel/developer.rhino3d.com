+++
aliases = ["/en/5/guides/compute/creating-an-Azure-VM/", "/en/6/guides/compute/creating-an-Azure-VM/", "/en/7/guides/compute/creating-an-Azure-VM/", "/en/wip/guides/compute/creating-an-Azure-VM/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "Azure" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Wie man eine virtuelle Maschine (VM) auf Azure erstellt"
type = "guides"
weight = 2
override_last_modified = "2022-02-14T14:13:06Z"

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

## Erstellen der Virtuellen Maschine

In diesem Leitfaden werden wir den Prozess der Einrichtung einer virtuellen Maschine mit Azure Services erläutern.

Stellen Sie zunächst sicher, dass Sie über ein gültiges Azure-Abonnement verfügen und dass Sie bereits eine Ressourcengruppe für die verschiedenen Ressourcen dieser Instanz eingerichtet haben. Um mehr über die Einrichtung einer Ressourcengruppe in Azure zu erfahren, [besuchen Sie diese Seite](https://docs.microsoft.com/de-de/azure/azure-resource-manager/management/manage-resource-groups-portal).

1. Melden Sie sich beim Azure-[Portal](https://portal.azure.com/#home) an.

1. Geben Sie **Virtuelle Computer** in die Suchleiste ein.

1. Unter **Dienste** wählen Sie **Virtuelle Computer**.

1. Auf der Seite **Virtuelle Computer** wählen Sie **Erstellen** und dann **Virtueller Computer**

1. Vergewissern Sie sich auf der Registerkarte **Grundeinstellungen** unter **Projektdetails**, dass die richtige Abonnement- und Ressourcengruppe ausgewählt ist.

1. Erstellen Sie unter **Instanzendetails** einen eindeutigen Namen für den virutellen Rechner. Wir verwenden *Rhino-Compute-VM* für unseren VM-Namen. Wählen Sie eine Region in Ihrer Nähe und wählen Sie dann *Windows Server 2022 Datacenter - Azure Edition Gen2* für das **Image**. Sie können jede **Größe** für die Virtuelle Maschine wählen, die Ihren Bedürfnissen entspricht. Wir verwenden *Standard DS2_v2* für dieses Beispiel. Belassen Sie die anderen Standardeinstellungen.
{{< image url="/images/Azure_VM_Create3.png" alt="/images/Azure_VM_Create3.png" class="image_center" width="100%" >}}

1. Geben Sie unter **Administratorkonto** einen Benutzernamen und ein Passwort ein. Notieren Sie sich diese Anmeldedaten, da wir sie verwenden werden, wenn wir uns bei dem remoten Computer anmelden.

1. Unter **Regeln für eingehende Ports** wählen Sie **Ausgewählte Ports zulassen** und dann **RDP (3389)**, **HTTPS (443)**und **HTTP (80)**.
{{< image url="/images/Azure_VM_Create4.png" alt="/images/Azure_VM_Create4.png" class="image_center" width="100%" >}}

1. Wählen Sie **Weiter: Datenträger >**.

1. Wählen Sie **Weiter: Netzwerk >**.

1. Klicken Sie im Abschnitt **Netzwerkschnittstelle** auf die Schaltfläche *Neu erstellen* unter dem Unterabschnitt **Öffentliche IP**.

1. Wenn sich das Pop-Out-Blade öffnet, wählen Sie **Statisch** unter der Registerkarte Zuweisung. Klicken Sie auf **OK** um diese Einstellung zu speichern.
{{< image url="/images/Azure_VM_Create5.png" alt="/images/Azure_VM_Create5.png" class="image_center" width="100%" >}}

1. Belassen Sie alle anderen Standardeinstellungen. Wählen Sie **Überprüfen + Erstellen**.

1. Sobald Ihre Konfiguration die Validierungsprüfung bestanden hat, wählen Sie **Erstellen** um Ihre virtuelle Maschine bereitzustellen.

1. Nachdem die Bereitstellung abgeschlossen ist, wählen Sie **Zur Ressource gehen**.

### Hinzufügen einer Regel für eingehende Ports

Sobald Ihre Virtuelle Maschine bereitgestellt wurde, sollten Sie die Ressourcen-Homepage aufrufen können. Hier können Sie verschiedene Einstellungen und Konfigurationen ändern. Wir fügen eine Regel für den eingehenden Port hinzu, damit wir API-Anfragen an einen bestimmten Port senden können.

Standardmäßig verweigert und blockiert Azure den gesamten öffentlichen eingehenden Datenverkehr, was auch ICMP-Datenverkehr einschließt. Dies ist eine gute Sache, da es durch Verringerung der Angriffsfläche die Sicherheit verbessert. Das [Internet Control Message Protocol (ICMP)](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) wird in der Regel für Diagnosen und zur Behebung von Netzwerkproblemen verwendet. 

Wir wollen den ICMP-Verkehr für unsere VM einschalten, damit wir versuchen können, die IP-Adresse anzupingen und eine Antwort zu erhalten. Als erstes müssen wir eine Regel für den eingehenden Port für ICMP-Verkehr hinzufügen. 

1. Wählen Sie im Menü auf der linken Seite den Menüpunkt **Netzwerk**. Dadurch wird das Netzwerk-Blade geöffnet.

1. Klicken Sie auf die Schaltfläche **Regel für eingehende Ports hinzufügen** .
{{< image url="/images/Azure_VM_Create6.png" alt="/images/Azure_VM_Create6.png" class="image_center" width="100%" >}}

1. Setzen Sie im Bereich **Eingehende Sicherheitsregel hinzufügen** den **Zielportbereiche** auf *, ändern Sie das **Protokoll** auf **ICMP**, setzen Sie die **Priorität** auf **100** und geben Sie **ICMP** in das Eingabefeld **Name** ein.
{{< image url="/images/Azure_VM_Create8.png" alt="/images/Azure_VM_Create8.png" class="image_center" width="75%" >}}

1. Klicken Sie auf **Hinzufügen**, um die neue Regel für eingehende Ports zu erstellen.

Herzlichen Glückwunsch! In dieser Anleitung haben Sie eine einfache virtuelle Maschine auf Azure bereitgestellt.
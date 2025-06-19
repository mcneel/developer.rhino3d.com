+++
aliases = ["/en/5/guides/compute/core-hour-billing/", "/en/6/guides/compute/core-hour-billing/", "/en/7/guides/compute/core-hour-billing/", "/en/wip/guides/compute/core-hour-billing/"]
authors = [ "brian" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "core-hour" ]
languages = []
sdk = [ "Compute" ]
title = "Lizenzierung und Abrechnung"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://www.grasshopper3d.com/forum/topics/how-do-i-install-a-custom-ghx"
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


## Info zur Kernzeit-Fakturierung

Wenn Rhino in einem Dienstkonto angemeldet ist und auf einem Windows-Server-basierten Betriebssystem läuft, werden Ihnen **0,10 $ pro Kern pro Stunde**, in der Rhino läuft, in Rechnung gestellt (anteilig pro Minute).

***Beispiel 1:** Rhino läuft eine Stunde lang auf einem 32-Kern-Server:*

  * 1 Computer * 32 Kerne * 1 Stunde * 0,10 $/Kernstunde = 3,20 $

***Beispiel 2:** Rhino läuft auf 200 4-Kern-Servern für 6 Minuten:*

  * 200 Computer * 4 Kerne * 0,1 Stunde * 0,10 $/Kernstunde = 8,00 $

***Beispiel 3:** 1 Rhino-Instanz läuft auf einem 2-Kern-Server 8 Stunden pro Tag für 30 Tage:*
  * 1 Computer * 2 Kerne * 8 Stunden/Tag * 30 Tage/Monat * 0,10 $/Kernstunde = 48 $/Monat

***Beispiel 4:** 10 Rhino-Instanzen laufen auf einem 2-Kern-Server 8 Stunden pro Tag für 30 Tage:*
  * 1 Computer * 2 Kerne * 8 Stunden/Tag * 30 Tage/Monat * 0,10 $/Kernstunde = 48 $/Monat
  * (Beachten Sie, dass die Anzahl der Instanzen von Rhino keinen Einfluss auf Ihre Rechnung hat)

**Die Abrechnung basiert auf der Betriebszeit**, nicht auf der Nutzung - wir verfolgen nicht die Aktivität jedes Kerns, sondern nur, dass Sie einen mit Rhino in Betrieb haben. Sie können Ihre Arbeitslasten nach oben und unten skalieren, um die Leistung und die Kosten für Sie zu optimieren.

**Mehrere Instanzen sind erlaubt** - Sie können so viele Instanzen von Rhino auf demselben Rechner laufen lassen, wie Sie wollen, und die Kosten sind dieselben wie für eine Instanz.

## Kernzeit-Fakturierung einrichten

Kernzeit-Fakturierung ist erforderlich, wenn Rhino auf einem Windows-Server-basierten Betriebssystem ausgeführt wird.

1. Gehen Sie zum [Lizenzportal](https://www.rhino3d.com/licenses?_forceEmpty=true) (melden Sie sich bei Ihrem Rhino-Konto an, wenn Sie dazu aufgefordert werden).
2. Klicken Sie auf _Neues Team anlegen_ und erstellen Sie ein Team, das Sie für Ihr Rechenprojekt verwenden möchten. {{< call-out "note" "Anmerkung" >}}
Das Anlegen eines neuen Teams ist nicht unbedingt erforderlich, aber die Abrechnung von Kernstunden ist *nicht kompatibel* mit im Team vorhandenen Lizenzen. Wenn Ihr Team also Lizenzen enthält, ist die Abrechnung von Kernstunden nicht zulässig.
{{< /call-out >}}

3. Klicken Sie auf _Team verwalten_ -> _Kernzeit-Fakturierung verwalten_.
4. Klicken Sie das Kontrollkästchen neben den Produkten an, die Sie aktivieren möchten. \
**Bitte beachten Sie: wenn Sie ein Team seit Jahren betreiben, müssen Sie möglicherweise neuere Versionen von Rhino aktivieren.**
5. Klicken Sie auf _Speichern_ und geben Sie die Zahlungsinformationen für Ihr neues Team ein, wenn Sie dazu aufgefordert werden.

## Kernzeit-Fakturierung verwenden…

1. Gehen Sie zum [Lizenzportal](https://www.rhino3d.com/licenses?_forceEmpty=true) und wählen Sie das Team aus, das Sie mit der Kernzeit-Fakturierung eingerichtet haben.
1. Klicken Sie auf _Team verwalten_ -> _Kernzeit-Fakturierung verwalten_.
2. Klicken Sie auf _Aktion_ -> _Token zur Authentisierung erhalten_, um ein Token zu erhalten.
3. Erstellen Sie eine neue Umgebungsvariable mit dem Namen `RHINO_TOKEN` und verwenden Sie das Token als Wert. Da das Token zu lang für das Dialogfeld Umgebungsvariablen von Windows ist, ist es am einfachsten, dies über einen PowerShell-Befehl zu tun.

    ```ps
    [System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'your token here', 'Machine')
    ```

Wenn Sie Rhino auf diesem Computer starten, wird es von nun an Ihr Kernstunden-Abrechnungsteam verwenden.

{{< call-out "warning" "Wichtig" >}}
<strong>Wichtig!</strong> Dieses Token erlaubt es jedem, der es besitzt, Ihr Team nach Belieben zu belasten. Geben Sie dieses Token <strong>NICHT</strong> an andere weiter.
{{< /call-out >}}

## Einzelcomputer-Lizenzierung wird nicht unterstützt

Wenn Rhino auf einem Windows-Server läuft, ist es nicht möglich, einen Lizenzschlüssel für den Betrieb als Einzelplatzlizenz einzugeben, da Rhino eine Lizenz pro Kern benötigt.

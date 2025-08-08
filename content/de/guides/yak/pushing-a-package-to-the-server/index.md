+++
aliases = ["/en/5/guides/yak/pushing-a-package-to-the-server/", "/en/6/guides/yak/pushing-a-package-to-the-server/", "/en/7/guides/yak/pushing-a-package-to-the-server/", "/en/wip/guides/yak/pushing-a-package-to-the-server/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "Dies ist eine Schritt-für-Schritt-Anleitung, um ein Paket auf den Paketserver zu schieben."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Ein Paket auf den Server schieben"
type = "guides"
weight = 20
override_last_modified = "2020-11-12T12:17:36Z"

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

Siehe den Leitfaden [Paketserver](/guides/yak/the-package-server/) für weitere Informationen über den öffentlichen Paketserver von McNeel.

{{< call-out "note" "Anmerkung" >}}
Yak ist plattformübergreifend. Die folgenden Beispiele sind für Windows. Für Mac ersetzen Sie den Pfad zum Yak CLI-Tool durch <code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.
{{< /call-out >}}



## Authentifizierung

Bevor Sie ein Paket auf den Server schieben können, müssen Sie das Yak CLI Tool mit Ihrem Rhino-Konto autorisieren.

```commandline
> "C:\Programme\Rhino {{< latest-rhino-version >}}\System\Yak.exe" login
```

Es sollte sich eine Browser-Registerkarte öffnen, in der Sie aufgefordert werden, sich bei Rhino Accounts anzumelden (vorausgesetzt, Sie sind noch nicht angemeldet). Im nächsten Fenster werden Sie aufgefordert, "Yak" Zugriff auf Ihr Konto zu gewähren.

- **Allgemeine Profilinformationen abrufen**: Dieser Bereich wird verwendet, um Ihren Namen, Ihren Standort und Ihr Profilbild abzurufen. Diese Informationen werden in Zukunft verwendet, wenn die Paketdatenbank über eine grafische Schnittstelle verfügt.
- **Ihre Identität überprüfen**: Wird für die Authentifizierung bei der Abfrage des Paketeigentums verwendet.
- **Ihre E-Mail-Adresse abrufen**: Ihre primäre E-Mail-Adresse wird gespeichert, damit Sie als [Besitzer von Paketen hinzugefügt](../yak-cli-reference/#owner) werden können, die andere veröffentlicht haben.

Sobald Sie akzeptiert haben, schließt sich das Browserfenster von selbst. Yak hat ein OAuth-Token von Rhino Accounts abgerufen und dieses auf Ihrem Computer gespeichert.

- Mac - `~/.mcneel/yak.yml`
- Windows - `%APPDATA%\McNeel\yak.yml`

{{< call-out "note" "Anmerkung" >}}
Zur Sicherheit ist das OAuth-Token nur für eine begrenzte Zeit gültig. Wundern Sie sich nicht, wenn das Yak CLI-Tool Sie nach etwa 30 Tagen dazu auffordert, sich erneut anzumelden.
{{< /call-out >}}

## Verschieben!

Jetzt, wo Sie eingeloggt sind, können Sie ein Paket auf den Server übertragen. Ich werde das Paket aus dem [vorherigen Leitfaden](../creating-a-grasshopper-plugin-package) als Beispiel verwenden.

```commandline
> "C:\Programme\Rhino {{< latest-rhino-version >}}\System\Yak.exe" push marmoset-1.0.0-rh6_18-any.yak
```

Dieser Befehl erstellt bei Erfolg keine Ausgabe.

Sie können überprüfen, ob Ihr Paket erfolgreich veröffentlicht wurde, indem Sie danach suchen. Sie sollten den Namen und die Versionsnummer des Pakets sehen, das Sie gerade verschoben haben. 🤞

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" search --all --prerelease marmoset

marmoset (1.0.0)
```

{{< call-out "note" "Anmerkung" >}}
Wenn Sie dies zum ersten Mal tun, sollten Sie zunächst versuchen, die Daten auf den Testserver zu verschieben.
```cmd
"C:\Programme\Rhino {{< latest-rhino-version >}}\System\Yak.exe" push --source https://test.yak.rhino3d.com marmoset-1.0.0-rh6_18-any.yak

"C:\Programme\Rhino {{< latest-rhino-version >}}\System\Yak.exe" search --source https://test.yak.rhino3d.com --all --prerelease marmoset

marmoset (1.0.0)
```
Dieser Server wird jede Nacht gereinigt.
{{< /call-out >}}

## Fehlersuche und -behebung

Es gibt einige Gründe, warum das Verschieben eines Pakets möglicherweise nicht funktioniert.

- Ungültige `manifest.yml`

  _Fehlermeldung sollte selbsterklärend sein. Beheben Sie das Problem und versuchen Sie es erneut! Sie können auch versuchen, die YAML-Syntax selbst mit einem [Linter](http://www.yamllint.com) zu validieren._

- Der Paketname existiert bereits, aber Sie sind kein **Besitzer**.

  _Nur Paket-**Besitzer** sind berechtigt, neue Versionen ihrer Pakete zu veröffentlichen. Wenn ein Benutzer die erste Version eines Pakets veröffentlicht, wird er dessen **Besitzer**. Zusätzliche Besitzer können mit dem Befehl [`owner`](../yak-cli-reference/#owner) hinzugefügt werden._

- Die Paketversion existiert bereits.

  _Um anderen, die eines Ihrer Pakete verwenden, keine Störungen zu verursachen, ist es nicht möglich, Versionen zu löschen oder zu überschreiben. Geben Sie die Versionsnummer an und lassen Sie Ihre Nutzer wissen, dass es etwas Neues gibt, das sie ausprobieren können!_

- Sie haben unbeabsichtigterweise etwas verschoben?

  _Verwenden Sie den [Befehl `yank`](../yak-cli-reference/#yank) um eine bestimmte Version aus der Liste zu nehmen._

## Verwandte Themen

- [Der Paketserver](/guides/yak/the-package-server/)
- [Erstellen eines Grasshopper-Plug-in-Pakets](/guides/yak/creating-a-grasshopper-plugin-package/)
- [Erstellen eines Rhino-Plug-in-Pakets](/guides/yak/creating-a-rhino-plugin-package/)

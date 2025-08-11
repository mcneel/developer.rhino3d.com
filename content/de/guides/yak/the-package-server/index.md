+++
aliases = ["/en/5/guides/yak/the-package-server/", "/en/6/guides/yak/the-package-server/", "/en/7/guides/yak/the-package-server/", "/en/wip/guides/yak/the-package-server/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Diese Anleitung stellt den Rhino Package Manager Server vor - https://yak.rhino3d.com"
keywords = [ "yak" ]
sdk = [ "Yak" ]
title = "Der Paketserver"
type = "guides"
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

Wir betreiben einen öffentlichen Paketserver, den jeder nutzen kann. Sie brauchen nichts zu konfigurieren. Sowohl das Yak CLI-Tool als auch Rhino wissen bereits, wo sie suchen müssen.

Die auf dem öffentlichen Paketserver freigegebenen Pakete können kostenlos heruntergeladen und installiert werden. Sie können kostenlos oder lizenzpflichtig sein - siehe die Anleitungen [Cloud Zoo](/guides/rhinocommon/cloudzoo/cloudzoo-overview/) und [Zoo](/guides/rhinocommon/rhinocommon-zoo-plugins/) für Möglichkeiten, die Lizenzierung in Ihrem Plug-in mit unseren Tools zu implementieren.

Nachfolgend finden Sie einige nützliche Informationen über unseren Paketserver.

## Authentifizierung und Autorisierung

Die Authentifizierung, die von [Rhino Accounts](https://accounts.rhino3d.com)bereitgestellt wird, ist nur für [Veröffentlichung von Paketen](../pushing-a-package-to-the-server) erforderlich, nicht für das Herunterladen bzw. Installieren.

Sobald ein Paketautor ein Paket veröffentlicht hat, kann nur er zukünftige Versionen unter demselben Paketnamen veröffentlichen.

{{< call-out "note" "Anmerkung" >}}
Die Funktion zum Hinzufügen von "Mitwirkenden" wird in Zukunft hinzugefügt werden.
{{< /call-out >}}

## Richtlinien

Der Paketserver hat einige Richtlinien, die eingehalten werden müssen.

### Benennung

Paketnamen sind ziemlich streng. Sie erlauben nur Buchstaben, Zahlen, Bindestriche und Unterstriche, z. B. `Hello_World` oder `hello-world1`.

Die Paketnamen übernehmen die Groß-/Kleinschreibung, die in der allerersten hochgeladenen Version verwendet wurde. Künftige Uploads ignorieren die Schreibweise des Paketnamens und alle Abfragen sind unabhängig von der Groß- und Kleinschreibung.

### Versionen

Paketversionsnummern müssen entweder [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) (z.B. `1.1.0-beta`) oder `System.Version`, auch bekannt als Microsofts vierstelliger Standard (z.B. `1.2.3.4`), folgen.

Es wird empfohlen, Semantic Versioning zu verwenden, da es Paketautoren erlaubt, Vorabversionen anzugeben. Diese sind praktisch für begrenzte Tests, da standardmäßig die neueste _stabile_ Version installiert ist.

Vierstellige Versionsnummern wurden in Version 0.8 (August 2019) hinzugefügt, um bestehende Plug-ins zu unterstützen, die Versionsnummern im Stil von `System.Version` verwenden. Sie unterstützen keine Vorabversionen oder Build-Metadaten.

#### Partielle Versionsnummern und Normalisierung

Wenn ein Paket erstellt wird, werden Sie vielleicht feststellen, dass die Versionsnummer im Dateinamen anders ist als in der Datei `manifest.yml`. Dies ist auf die Normalisierung der Versionsnummern zurückzuführen. Derselbe Prozess läuft hinter den Kulissen auf dem Paketserver ab und dient dazu, Mehrdeutigkeiten zwischen semantisch gleichwertigen Versionen zu vermeiden.

Es gibt zwei Fälle, in denen Versionsnummern semantisch äquivalent sein können.

* Semantische Versionen, die sich nur in den Build-Metadaten[^1] unterscheiden, d.h. `1.0.0+build.1` und `1.0.0+build.2`
* Eine vierstellige Version und eine semantische Version, die bis auf die vierte Ziffer "0" identisch sind (keine Vorabversion oder Build-Metadaten), z. B. "1.2.3" und "1.2.3.0".

Die Normalisierung unterscheidet sich von der Expansion von Teilversionsnummern (z.B. `1.0`). Die Nummern von Teilversionen werden erweitert und in ihrer vollständigen Form gespeichert. Wenn Sie zum Beispiel ein Paket als `1.0` hochladen, wird es tatsächlich als `1.0.0` gespeichert. Anschließend werden alle Anfragen (REST, CLI usw.) für Version "1.0" automatisch umgeleitet.

[^1]: ["Build-Metadaten MÜSSEN bei der Bestimmung des Versionsvorrangs ignoriert werden. So haben zwei Versionen, die sich nur in den Build-Metadaten unterscheiden, den gleichen Vorrang."](https://semver.org/#spec-item-10)
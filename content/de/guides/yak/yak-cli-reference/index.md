+++
aliases = ["/en/5/guides/yak/yak-cli-reference/", "/en/6/guides/yak/yak-cli-reference/", "/en/7/guides/yak/yak-cli-reference/", "/en/wip/guides/yak/yak-cli-reference/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Eine Referenz für das Yak-Befehlszeilenwerkzeug."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Befehlszeilenwerkzeug-Referenz in Yak"
type = "guides"
weight = 1

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

Das Yak-Befehlszeilenwerkzeug ist in Rhino 7 WIP enthalten. Auf Windows finden Sie das Tool unter `"C:\Programme\Rhino {{< latest-rhino-version >}}\System\yak.exe"`. Auf dem Mac gibt es das Convenience-Script auf `"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"`.

## Befehle

### Erstellen

* _Seit 0.2: Befehl hinzugefügt_
* _Seit 0.4: Unterstützt mehrere .gha-Dateien, .rhp-Dateien oder andere_
* _Seit 0.9: Hängt den Distribution-Tag an den Dateinamen an und erweitert den Platzhalter $version_
* _Seit 0.10.1: Das Argument `--platform` wird hinzugefügt_

Wenn es in einem Verzeichnis ausgeführt wird, das eine gültige Datei "manifest.yaml" enthält, wird ein Paket erstellt, das alle Dateien in diesem Verzeichnis enthält.

```commandline
Verwendung: yak build [Optionen]

Optionen:
    --platform PLATFORM Die Plattform, auf der das Paket laufen soll ('win', 'mac' oder 'any')
    -h, --help           Hilfe erhalten (entspricht `yak help build`)
```

{{< call-out "note" "Hinweis" >}}
  Ein <a class="alert-link" href="../the-anatomy-of-a-package#distributions">Distribution Tag</a> (z.B.<code>rh7-win</code>) wird an den Dateinamen des erstellten Pakets angehängt. Die Kennzeichnung wird während der Erstellung durch die Überprüfung des Inhalts des Pakets bestimmt. Das Argument <code>&#45;&#45;platform=any</code> kann verwendet werden, wenn der Autor eine plattformübergreifende Distribution veröffentlichen möchte, z.B. <code>rh7-any</code>. Derzeit können nur .rhp- und .gha-Dateien eingesehen werden. Wenn ein Paket keines dieser Elemente enthält, wird es mit dem Distribution Tag <code>any-any</code> versehen.
{{< /call-out >}}

<!-- Während des Builds wird die GUID der Komponente extrahiert, um später die Suche nach dem Paket zu erleichtern. -->

### Installation

* _Seit 0.1: Befehl hinzugefügt_
* _Seit 0.13.0: Unterstützt die Installation von lokalen .yak-Dateien_

Installiert ein Paket (optional mit einer bestimmten Version).

```commandline
Verwendung:
    yak install [--source=URL] <package> [<version>]
    yak install <package>
```

Wobei `<package>` entweder der Name eines Pakets oder der Pfad zu einer lokalen .yak-Datei ist.

### Liste

_Seit 0.2_

Listet die auf dem Rechner installierten Pakete auf.

```commandline
yak list
```

### Log-in

* _Seit 0.2: Befehl hinzugefügt_
* _Seit 0.10: Bei der Anmeldung registrierter Benutzer_

Authentifiziert sich mit Rhino-Konten und speichert ein zeitlich begrenztes OAuth2-Zugangs-Token, damit der Benutzer Befehle verwenden kann, die eine Authentifizierung erfordern.

```commandline
Usage: yak login [options]

Optionen:
    --ci              Erzeugt einen nicht ablaufenden API-Schlüssel und zeigt hn an
    -s, --source URL  Speicherort des Paket-Repositorys [Standard: https://yak.rhino3d.com/].
    -h, --help        Hilfe erhalten (entspricht `yak help login`)
```

Auf Windows wird das Token in `%appdata%\McNeel\yak.yml` gespeichert. Auf macOS wird sie in `~/.mcneel/yak.yml` gespeichert.

Bei der ersten Anmeldung wird der Benutzer auf dem Server registriert.

{{< call-out "note" "Hinweis" >}}
  In einer automatisierten Build-Umgebung - z.B. einer Build-Maschine, GitHub Actions, etc. - kann das CLI-Tool `yak` das Zugriffstoken aus der Umgebungsvariablen `YAK_TOKEN` lesen. Benutzen Sie das `--ci`-Flag, um sich anzumelden und ein Token für diesen Zweck zu erzeugen!
{{< /call-out >}}

### Verschieben

_Seit 0.1_

Verschiebt ein Paket auf den Server.

```commandline
yak push [--source=URL] <filename>
```

{{< call-out "note" "Hinweis" >}}
  Erfordert <a class="alert-link" href="#login">Authentifizierung</a>.
{{< /call-out >}}

### Suchen

* _Seit 0.1: Befehl hinzugefügt_
* _Seit 0.5: Fügt die Flags `--all` und `--prerelease` hinzu_

Durchsucht den Server nach Paketen, die `query` entsprechen.

```commandline
Verwendung: yak search [options] <query>

  Optionen:
    --prerelease      Paketversionen der Vorabversion anzeigen
    -a, --all         Alle Paketversionen anzeigen
    -s, --source URL  Ort des Paket-Repositorys
    -h, --help        Hilfe erhalten (entspricht `yak help search`)
```

### Spec

* _Seit 0.2: Befehl hinzugefügt_
* _Seit 0.4: Fügt Unterstützung für die Inspektion von .rhp-Dateien hinzu (nur RhinoCommon)_

Erzeugt eine Skelettdatei `manifest.yml` auf der Grundlage des Inhalts des aktuellen Verzeichnisses. Wenn sie in einem Verzeichnis ausgeführt wird, das eine Grasshopper-Baugruppe (`.gha`) oder ein RhinoCommon-Plugin (`.rhp`) enthält, wird die Datei inspiziert und zum Vorbefüllen der Datei `manifest.yml` verwendet.

```commandline
yak spec
```

### Deinstallieren

_Seit 0.1_

Deinstalliert ein Paket.

```commandline
yak uninstall <package>
```
<!-- Deaktivierungs-Rückgriff wurde entfernt in v0.6-->
<!-- {{< call-out "note" "Hinweis" >}}
  Seit 0.3 versucht Yak, das Paket aus dem Rechner zu entfernen. Wenn dies nicht möglich ist - wahrscheinlich, weil Rhino läuft - dann wird das Paket stattdessen <em>deaktiviert</em>.
{{< /call-out >}} -->

### Yank

_Seit 0.6_

Entfernt eine Version aus dem Paketindex.

```commandline
yak yank <package> <version>
```

{{< call-out "note" "Hinweis" >}}
  Erfordert <a class="alert-link" href="#login">Authentifizierung</a>.
{{< /call-out >}}

Veraltete Versionen erscheinen nicht in der Suche, können aber trotzdem installiert werden, wenn die genaue Paketversion bekannt ist. Sie sind sozusagen versteckt.

Es ist nicht möglich, eine Paketversion, die zurückgezogen wurde, erneut zu veröffentlichen. Wenn Sie sich in dieser Situation befinden, ändern Sie einfach die Versionsnummer Ihres Pakets und führen Sie den Push-Vorgang erneut durch.

Wenn alle Versionen eines Pakets entfernt werden, wird es nicht mehr im Paketindex angezeigt.

{{< call-out "danger" "Gefahr" >}}
  <p><strong>Löschen eines Pakets vom McNeel-Server</strong></p>
  <p>Wenn Sie Ihr Paket unbedingt vom öffentlichen Server löschen müssen, senden Sie bitte eine E-Mail an <a href="mailto:support@mcneel.com">support@mcneel.com</a>. Sobald ein Paket gelöscht wurde, kann der Name nicht mehr verwendet werden.</p>
{{< /call-out >}}

### Unyank

Funktioniert genauso wie der Befehl yank, aber umgekehrt!

### Eigentümer

_Seit 0.10_

Fügt die Eigentümer eines Pakets hinzu, entfernt sie oder listet sie auf. Paketbesitzer können neue Versionen des Pakets veröffentlichen und bestehende Versionen veröffentlichen bzw. zurücknehmen.

```commandline
Verwendung:
    yak owner add [--source=URL] <package> <email>
    yak owner remove [--source=URL] <package> <email>
    yak owner list [--source=URL] <package>
    
Optionen:
    -h, --help
    -s, --source URL  Speicherort des Paket-Repositorys [Standard: https://yak.rhino3d.com/].
```

Der neue Eigentümer kann alles tun, was der ursprüngliche Eigentümer tun kann. Bitte beachten Sie dies!

Neue Eigentümer müssen auf dem Server registriert werden, bevor sie zu einem Paket hinzugefügt werden können. Sie können dies selbst mit dem Befehl [`login`](#login) tun.

## Downloads

Die `yak` CLI ist als eigenständige ausführbare Datei für die Verwendung in Umgebungen verfügbar, in denen Rhino nicht installiert ist, wie z.B. auf automatischen Build-Maschinen.

* https://files.mcneel.com/yak/tools/0.13.0/yak.exe
* https://files.mcneel.com/yak/tools/0.13.0/win-arm64/yak.exe
* https://files.mcneel.com/yak/tools/0.13.0/mac/yak
* https://files.mcneel.com/yak/tools/0.13.0/linux-x64/yak
* https://files.mcneel.com/yak/tools/0.13.0/linux-arm64/yak


## Verwandte Themen

- [Yak-Anleitungen und Tutorials](/guides/yak/)
- [Anatomie eines Pakets](/guides/yak/the-anatomy-of-a-package/)
- [Das Paketmanifest](/guides/yak/the-package-manifest/)

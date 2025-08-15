+++
aliases = ["/en/5/guides/yak/the-package-manifest/", "/en/6/guides/yak/the-package-manifest/", "/en/7/guides/yak/the-package-manifest/", "/en/wip/guides/yak/the-package-manifest/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "Was ist ein 'Paketmanifest' und was sollte es enthalten?"
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Das Paketmanifest"
type = "guides"
weight = 1
override_last_modified = "2021-07-21T10:09:56Z"

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

## Übersicht

Jedes Paket sollte eine Manifestdatei mit einer Spezifikation haben, die in die Datenbank destilliert werden kann, wenn das Paket auf den Server übertragen wird. Das Manifest sollte in [YAML](http://www.yaml.org)geschrieben sein und der Struktur des untenstehenden Beispiels folgen.

Die Manifestdatei sollte den Namen `manifest.yml` tragen und sich im Stammverzeichnis des Pakets befinden. (Keine Sorge, der [`build`-Befehl](/guides/yak/yak-cli-reference#build) des Yak-CLI-Tools erledigt das für Sie!)

Der Zweck des Manifests besteht darin, den Prozess der Veröffentlichung von Paketen zu rationalisieren (und möglicherweise zu automatisieren), so dass bei der Veröffentlichung von Paketen keine Webformulare mehr erforderlich sind.

**Erforderliche Attribute**
 - [Name](#name)
 - [Version](#version)
 - [Autoren](#authors)
 - [Beschreibung](#description)

**Empfohlene Attribute**
 <!-- - [`license`](#license) -->
 - [URL](#url)
 - [Stichwörter](#keywords)
 - [Symbol](#icon)

<!-- ### Optionale Attribute
 - [`dependencies`](#dependencies) -->

## Beispiel

Hier ist ein Beispiel für ein Grasshopper-Plug-in.

```yaml
name: plankton
version: 0.3.4
authors:
  - Daniel Piker
  - Will Pearson
description: >
  Plankton is a flexible and efficient library for handling n-gonal meshes.
  Plankton is written in C# and implements the halfedge data structure. The
  structure of the library is loosely based on Rhinocommon's mesh classes and
  was originally created for use within C#/VB scripting components in
  Grasshopper.
url: "https://github.com/meshmash/Plankton"
```

## Erforderliche Attribute

### Name

Der Kurzname, der das Paket beschreibt. Vorzugsweise ein Wort, wobei mehrere Wörter durch Unterstriche oder Bindestriche getrennt werden können.

_**Hinweis:** Der Paketname darf nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten_

_**Hinweis 2:** Die Paketnamen übernehmen die Groß-/Kleinschreibung, die in der allerersten hochgeladenen Version verwendet wurde. Künftige Uploads ignorieren die Schreibweise des Paketnamens und alle Abfragen sind unabhängig von der Groß- und Kleinschreibung.

```yaml
name: plankton
```

### Version

_Seit 0.8: vierstellige Versionsnummern erlaubt_
_Seit 0.9: `$version` Platzhalter_

Die Versionsnummer, die dem Paket gegeben wurde.

Paketversionsnummern **müssen** entweder [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) (z.B. `1.1.0-beta`) oder `System.Version`, auch bekannt als Microsofts vierstelliger Standard (z.B. `1.2.3.4`), folgen. Es wird empfohlen, Semantic Versioning zu verwenden, da es Paketautoren erlaubt, Vorabversionen anzugeben. Diese sind praktisch für begrenzte Tests, da standardmäßig die neueste _stabile_ Version installiert ist.

Um den Erstellungsprozess zu vereinfachen, ist es möglich, die Versionsnummer durch `$version` zu ersetzen - die Versionsnummer wird aus dem Inhalt des Pakets abgeleitet und während `yak build` ersetzt.

```yaml
version: 0.3.4
```

### Autoren

Eine Liste der Autoren des Pakets.

```yaml
authors:
  - Daniel Piker
  # list additional package authors below
  - Will Pearson
```

### Beschreibung

Beschreiben Sie das Paket. Seien Sie so ausführlich oder so kurz, wie Sie es für richtig halten.

```yaml
description: This is an awesome package.
```

Wenn Sie mehr schreiben wollen, können Sie den [folded style](http://www.yaml.org/spec/1.2/spec.html#id2796251) von YAML verwenden.

```yaml
description: >
  This is such an awesome package
  that I'm going to write a whole
  bunch of text describing it!

  This sentence will be on a new line.
```

<!-- Oder, wenn Sie Zeilenumbrüche beibehalten wollen, verwenden Sie den [literal style](https://yaml.org/spec/1.2-old/spec.html#id2795688)

```yaml
description: |
  This is the first line of the description.
  This sentence is (and will be) on a new line!
``` -->


## Empfohlene Attribute

<!-- ### License

Die Lizenz für dieses Paket. Diese sollte nicht mehr als 64 Zeichen lang sein und einer der standardmäßigen [SPDX-Bezeichner](spdx.org/licenses/) sein.

```yaml
license: MIT
```

Wenn das Paket quelloffen sein soll, sollten Sie idealerweise ein Paket wählen, das von der [OSI (Open Source Initiative)](opensource.org/licenses/alphabetical) anerkannt ist. Die am häufigsten verwendeten, von der OSI genehmigten Lizenzen sind BSD-3-Clause und MIT. GitHub bietet auch eine Lizenzauswahl unter http://choosealicense.com.

Dies sollte nur der Name Ihrer Lizenz sein. Der vollständige Text der Lizenz sollte als `LICENSE[.ext]` (auf oberster Ebene) in das Paket aufgenommen werden, wenn Sie es erstellen.

Sie sollten eine Lizenz für Ihr Paket angeben, damit andere wissen, wie sie es verwenden dürfen und welche Einschränkungen Sie ihm auferlegen. Keine Lizenz anzugeben bedeutet, dass alle Rechte vorbehalten sind; andere haben keine Rechte, den Code für irgendeinen Zweck zu verwenden. -->

### URL

Eine Webseite für das Paket. Dies kann eine beliebige URL sein, z.B. Kontaktinformationen des Autors, Foren, Tutorials oder andere Informationen über das Plug-in.

<!-- HINWEIS: Ich denke, dass, wenn es sich um ein Github-Repository handelt, die Möglichkeit besteht, direkt aus HEAD zu bauen. -->

```yaml
url: "https://github.com/meshmash/Plankton"
```

### Stichwörter

Eine Liste von Schlüsselwörtern, die den Nutzern helfen, das Paket zu finden.

```yaml
keywords:
- one
- two
```

### Symbol

Eine Bilddatei im Paket. Sie sollte klein sein (z.B. 64x64) und muss entweder ein PNG oder ein JPEG sein.

```yaml
icon: icon.png
```


<!-- ## Optionale Attribute -->

<!-- ### Abhängigkeiten

Eine Liste der Pakete, von denen dieses Paket abhängt. Kann auch optionale Versionsangaben enthalten, die wiederum der Semantischen Versionierung entsprechen.

_Wird derzeit nicht verwendet, aber der Server ist in der Lage, Abhängigkeiten zu speichern, so dass dies angeschlossen werden muss!_

```yaml
dependencies:
  - name: plankton
    spec: "< 0.4.0, >= 0.3.0"
  - name: package_without_spec
​``` -->


<!--## Alternative (JSON)

​```json
{
  "name": "plankton",
  "version": "0.3.4",
  "author": [
    "Daniel Piker",
    "Will Pearson"
  ],
  "dependencies": [

  ],
  "description": "Plankton is a flexible and efficient library for handling n-gonal meshes. Plankton is written in C# and implements the halfedge data structure. The structure of the library is loosely based on Rhinocommon's mesh classes and was originally created for use within C#/VB scripting components in Grasshopper.",
  "license": "LGPL-3",
  "url": "https://github.com/meshmash/Plankton",
  "type": "gh-plugin"
}
``` -->

## Veraltete Attribute

### Symbol-URL

{{< call-out "warning" "Wichtig" >}}
⚠️ Ersetzt durch das Attribut <a href="#icon" class="alert-link">icon</a> .
{{< /call-out >}}

Geben Sie einen **direkten** Link zu einem Symbol an, das vom Paketmanager in Rhino verwendet werden soll. Es sollte klein sein (32x32 ist ideal) und muss entweder ein PNG- oder ein JPEG-Format sein.

```yaml
icon_url: "https://example.com/path/to/icon.png"
```

## Verwandte Themen

- [Yak-Anleitungen und Tutorials](/guides/yak/)
- [Anatomie eines Pakets](/guides/yak/the-anatomy-of-a-package/)
- [Yak CLI-Referenz](/guides/yak/yak-cli-reference)


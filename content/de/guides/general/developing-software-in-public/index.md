+++
aliases = ["/en/5/guides/general/developing-software-in-public/", "/en/6/guides/general/developing-software-in-public/", "/en/7/guides/general/developing-software-in-public/", "/en/wip/guides/general/developing-software-in-public/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "An overview of the McNeel Development Process."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Öffentliche Software-Entwicklung"
type = "guides"
weight = 0
override_last_modified = "2018-12-05T14:59:06Z"

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

Während der letzten 20 haben wir einen Prozess erarbeitet, der uns dabei hilft, die Zufriedenheit unserer Kunden zu erhalten.  Dieser Prozess gliedert sich in acht Teile, die alle gleich wichtig sind.  Jahrelang haben wir unsere eigenen Werkzeuge erstellt, um die meisten Teile dieses Prozesses bewältigen zu können.  Doch jetzt gibt es hervorragende Werkzeuge im öffentlichen Handel - Werkzeuge, die wir Ihnen ebenfalls für den Gebrauch empfehlen.

Unser Software-Entwicklungsprozess ist, wie schon der andere Prozesses, ein Kreislauf.  Wie können also an jeder beliebigen Stelle beginnen.

![Rhino Development Cycle](/images/developing-software-in-public-01.png)

## Der Kreislauf

Da es sich hier um einen Entwickler-Leitfaden handelt, beginnen wir mit dem Schreiben eines Codes.

### Code

Das ist etwas, womit wir als Software-Entwickler eine Menge Zeit verbringen.  Wir lassen unsere bevorzugte IDE offen, wir schreiben Code, wir prüfen aus, wir lösen Probleme.  Wir kennen keinen Software-Entwickler, der es nicht liebt, Probleme zu lösen.

Wenn wir ein Resultat haben, erfolgt das *Einchecken* in unsere Versionsverwaltung...

### Einchecken

Wir checken Code in ein [Versionsverwaltungs-System](https://en.wikipedia.org/wiki/Version_control) ein.  In unserem Fall verwenden wir [git](https://git-scm.com/) mit [GitHub](https://github.com/).  Es sind aber auch viele andere Verionsverwaltungs-System verbreitet.  Früher verwendeten wir [Subversion](https://subversion.apache.org/), heute verwenden wir [GitHub](https://github.com/).  [GitHub](https://github.com/) harmoniert hervorragend mit zahlreichen anderen Werkzeugen und verfügt über eine vielfältige API.  Es kommen aber auch andere in Frage: [BitBucket](https://bitbucket.org), [Mercurial](https://www.mercurial-scm.org/) usw.

Falls Sie noch keine Versionsverwaltung verwenden, raten wir Ihnen eindringlich: tun Sie es.  Es ist jetzt ganz einfach.  Sie ermöglicht Ihnen, zu älteren Versionen Ihrer Software zurückzukehren, bevor ein Problem auftrat.  Sie fördert Ihre Zusammenarbeit als Team.  Sie wird für jegliche Art von Build-Automatisierung benötigt.  Und wie gesagt: sie ist einfach

Als Entwickler verwenden wir eine abgeänderte Version von [GitHub Flow](https://guides.github.com/introduction/flow/), um Pull Requests zu erstellen und in unsere Haupt-Branch zusammenzuführen.

Nachdem wir unseren Code eingecheckt haben, kompilieren wir ihn...

### Kompilieren

Zusätzlich zum Kompilieren auf unseren Desks haben wir eigens [TeamCity](https://www.jetbrains.com/teamcity/)-Server, die ständig unseren Code erstellen und überprüfen, dass er mit unserer Hauptbranch auf [GitHub](https://github.com/) funktioniert.  Somit wird garantiert, dass wir einander nicht die Möglichkeit nehmen, den neuesten Code zu erhalten und zu kompilieren.

Diese [TeamCity](https://www.jetbrains.com/teamcity/)-Server überprüfen das Einchecken und erstellen auch unsere täglichen Veröffentlichungen - viele davon - und zwar alle vier Stunden.  Sie erstellen auch unsere öffentliche WIP- und Service-Release-Builds.

Mit jedem neuen Build testen wir...

### Testen

Wenn Entwickler Fehler beheben und Probleme beenden, stellt unser internes Tespersonal sicher, dass der öffentliche Build korrekt funktioniert.  Beim Testen der WIP- und Release-Candidate-Builds sind wir auch auf unsere Kunden angewiesen.

Das Testen geschieht vor und nach dem folgenden Schritt: Veröffentlichung...

### Veröffentlichen

Wann immer wir über einen auslieferungsbereiten Build verfügen, stellen wir ihn bereit (oder veröffentlichen ihn).

Dazu gehört auch die Veröffentlichung von...

- [Installern zum Herunterladen](http://www.rhino3d.com/download)
- [SDKs](http://developer.mcneel.com)
- Dokumentation (diese Website hier)

...sowie die Veröffentlichung von Bekanntgaben per E-Mail, in Blogs und in den Sozialen Medien.

### Feedback

Feedback nehmen wir auf allen möglichen Kommunikationswegen entgegen.

- [Chat](http://www.rhino3d.com/support#)
- [E-Mail](mailto:tech@mcneel.com)
- Telefonischer Support +34 933 199 002
- [Forum (Discourse)](https://discourse.mcneel.com/)

Dank der Rückmeldungen stoßen wir oft auf Probleme, die einer Lösung bedürfen.  Manchmal handelt es sich um kleine, manchmal aber auch um BEDEUTENDE Probleme.  Immer erstellen wir einen Problembericht...

### Verfolgen

Die Problemberichte erstellen wir in [YouTrack](https://mcneel.myjetbrains.com).

[YouTrack](https://mcneel.myjetbrains.com) funktioniert gut für uns, da es eine große Hilfe dabei ist, jeden Fehler zu testen und zu dokumentieren.

### Priorisieren

Herauszufinden, was gerade am wichtigsten ist, ist SCHWER:.  Wir sprechen mit unseren Kunden.  Wir sprechen miteinander.  We benutzen Gmail, Google Drive und Google Docs, um mitenander zu kommunizieren.  24 Stunden am Tag chatten wir auf [Slack](https://slack.com/).

Jeden Dienstag haben wir eine gemeinsame Besprechung.  Davor teilen wir alles, was anliegt, in einem Google Doc. In diesem Dokument teilen wir die Ziele unserer demnächst zur Veröffentlichung anstehenden Produkte sowie alle Funktionsgruppen, an denen wir arbeiten - einschließlich grafischer Darstellungen unserer Fortschritte -; zudem enthält es Links zu unseren Fehlerberichten in [YouTrack](https://mcneel.myjetbrains.com) und wir erhalten verbale Rückmeldung aller Leute, die an diesen Funktionen arbeiten.

Auch schreiben alle Entwickler auf, woran sie gerade arbeiten, was als nächste für sie auf dem Plan steht und auf welche Hindernisse sie bei ihrer Arbeit stoßen.

### Automatisierung

Und nicht zuletzt wird auch VIEL automatisiert.

Hier sind einige der Dinge, die wir automatisieren:

- Erstellung aller Check-ins von allen Entwicklern, bevor sie Teil der Haupt-Branch unserer Enwicklung werden.
- Schließen der Problemberichte in [YouTrack](https://mcneel.myjetbrains.com), wenn Fehlerbehebungen durch die [TeamCity](https://www.jetbrains.com/teamcity/)-Server in unsere Haupt-Entwicklungsbranch eingeführt werden.
- Erstellung interner und auslieferbarer Veröffentlichungen auf unseren [TeamCity](https://www.jetbrains.com/teamcity/)-Servern.
- Herausgabe neuer WIP-Veröffentlichungen durch Befehlseingabe in [Slack](https://slack.com/).
- Hochladen lieferbarer Veröffentlichungen auf unsere Download-Server.

## Publik

Bis vor Kurzem waren dies die Teile unseres Prozesses, die wir öffentlich gemacht haben:

- Testen
- Veröffentlichen
- Erhaltenes Feedback

Und während der letzten zwei Jahre haben wir unseren Bugtracker öffentlich zugänglich gemacht, indem wir zu YouTrack gewechselt sind.  Einige Probleme sind aus Sicherheits- oder Datenschutzgründen nicht öffentlich einsehbar.

Das nächste was wir tun möchten, ist noch mehr von all dem publik zu machen, und zwar durch:

- Teilweises Code-Sharing auf öffentlichen Repos auf GitHub, so dass Sie über echte, produkterprobte Code-Beispiele als Arbeitsgrundlage verfügen können.
- Die Möglichkeit für Sie, Fehlerbehebungen und Verbesserungen unseres Codes zu teilen.
- Leichtere Erstellung von Plug-in-Projekten durch die Veröffentlichung von RhinoCommon als NuGet-Paket.
- Hilfe bei der Build-Automatisierung, falls erforderlich.

## Verwandte Themen

- [Rhino-Technologie in der Übersicht](/guides/general/rhino-technology-overview)
- [Beiträge](/guides/general/contributing)
- [Voraussetzungen für Entwickler](/guides/general/rhino-developer-prerequisites)

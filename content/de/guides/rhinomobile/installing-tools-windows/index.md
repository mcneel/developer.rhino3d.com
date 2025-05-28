+++
aliases = ["/en/5/guides/rhinomobile/installing-tools-windows/", "/en/6/guides/rhinomobile/installing-tools-windows/", "/en/7/guides/rhinomobile/installing-tools-windows/", "/en/wip/guides/rhinomobile/installing-tools-windows/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "Diese Anleitung behandelt alle notwendigen Werkzeuge, die für RhinoMobile auf Windows benötigt werden."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Installation von Werkzeugen (Windows)"
type = "guides"
weight = 3

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/getting-started"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac" ]
since = 5
until = 7

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true

[_build]
list = "never"
+++

{{< call-out "warning" "RhinoMobile: Deprecated" >}}
RhinoMobile wird nicht mehr unterstützt. Rhino 3dm File I/O ist weiterhin auf iOS und Android über die [rhino3dm Bibliothek](https://github.com/mcneel/rhino3dm) verfügbar.
{{< /call-out >}}

Am Ende dieses Leitfadens sollten Sie alle Tools installiert haben, die für das Verfassen, Erstellen und Debuggen von mobilen C#-Anwendungen mit RhinoMobile erforderlich sind.

## Voraussetzungen

Falls Sie dies noch nicht getan haben, lesen Sie bitte den Leitfaden [Was ist RhinoMobile?](/guides/rhinomobile/what-is-rhinomobile/)

Dieser Leitfaden wurde konzipiert für die Verwendung eines:

- PC mit [Microsoft Windows](http://www.microsoft.com/en-us/windows) 8.1 oder neuer.

## Visual Studio installieren

[Visual Studio](https://www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx) ist das Leuchtturmprojekt von Microsofts Entwicklungsplattform und integrierter Entwicklungsumgebung (IDE).  Visual Studio gibt es jetzt in drei "Geschmacksrichtungen": Visual Studio Code[^1], Visual Studio Online[^2], und das „eigentliche“ Visual Studio[^3].  Um RhinoMobile-Anwendungen zu erstellen, benötigen Sie das „eigentliche“ Visual Studio (Visual Studio Code und Visual Studio Online werden nicht unterstützt).

Zum Zeitpunkt der Erstellung dieses Dokuments ist das „eigentliche“ Visual Studio in [drei Editionen](https://www.visualstudio.com/vs-2015-product-editions) erhältlich: Gemeinschaft, Beruf und Unternehmen.  Jede dieser Editionen ist geeignet.

Für die Zwecke dieser Anleitung gehen wir davon aus, dass Sie Visual Studio 2017 Community Edition verwenden.

#### Schrittweise Anleitung

1. *[Visual Studio 2017 Community Edition](https://www.visualstudio.com/vs-2015-product-editions)* ist von Microsoft kostenlos für Studenten, Open-Source-Mitarbeiter und kleine Teams erhältlich. [Weitere Infos finden Sie hier](https://www.visualstudio.com/en-us/support/legal/mt171547).  Klicken Sie auf die Schaltfläche *Community*, um das Installationsprogramm herunterzuladen.
1. Führen Sie das *Visual Studio Installationsprogramm* aus, das Sie von Microsoft heruntergeladen haben, in diesem Fall *vs_community.exe*.
1. Folgen Sie den Anweisungen auf dem Bildschirm, um Visual Studio zu installieren.  Es wird empfohlen, die *Typische* Installation auszuführen.  Je nach Ihrer Internetverbindung kann dies Minuten oder Stunden dauern.  Wenn die Installation erfolgreich war, klicken Sie auf die Schaltfläche *Starten* , um zu überprüfen, ob sie ordnungsgemäß installiert wurde.

## Xcode installieren (optional)

[Xcode](https://developer.apple.com/xcode/) ist die Entwicklungsplattform und IDE von Apple. Dieser Schritt ist optional und nur erforderlich, wenn Sie für iOS erstellen möchten. Sie müssen diesen Schritt auf Ihrem Mac-Baukasten mit macOS durchführen.

#### Schrittweise Anleitung

1. *[Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)* ist kostenlos im [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12) verfügbar.  Klicken Sie auf die Schaltfläche *Anzeigen in Mac App Store* .
1. Klicken Sie auf die Schaltfläche *Get* > *Install App* unterhalb des Xcode-Symbols.
1. Sie werden aufgefordert, Ihre [Apple ID](https://appleid.apple.com/) einzugeben (erforderlich zum Herunterladen von Anwendungen aus dem App Store).
1. Xcode ist ein umfangreicher Download - fast 2,6 GB.  Sie können den Fortschritt des Downloads in Launchpad überwachen.  Wenn Xcode den Download und die Installation beendet hat, wird es in Ihrem */Programme*-Ordner zu finden sein.
1. *Starten Sie* Xcode.  Beim ersten Start wird Xcode einige zusätzliche Komponenten installieren.
1. *Beenden Sie* Xcode.

## Xamarin installieren

Die Plattform von Xamarin ist derzeit erforderlich, um RhinoMobile-Anwendungen zu erstellen.  Werfen Sie einen Blick in den Leitfaden [Was sind Mono und Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/) um mehr zu erfahren.

#### Schrittweise Anleitung

1. *[Laden Sie die Xamarin-Plattform herunter](http://xamarin.com/download)*.
1. Xamarin verwendet eine Installationsanwendung, die die von Ihnen ausgewählten Komponenten herunterlädt und installiert.  Sobald Sie die Datei *XamarinInstaller.dmg* heruntergeladen haben, doppelklicken Sie darauf, um die Image-Datei zu mounten.  Doppelklicken Sie auf das große Symbol *Install Xamarin* , um das Installationsprogramm einzuhängen.
1. Sie müssen die Xamarin-Software-Lizenzvereinbarung akzeptieren, um die Xamarin-Plattform nutzen zu können.
1. Die *Xamarin-Plattform* besteht aus folgenden Teilen:
   - Xamarin Studio
   - Xamarin.Android
   - Xamarin.iOS
   - Xamarin.Mac
...stellen Sie sicher, dass *Xamarin.Android* und *Xamarin.iOS* markiert sind und klicken Sie auf *Fortfahren*.
1. Xamarin installiert: *Xamarin Studio*, *Xamarin.Android* und *Xamarin.iOS*.  Klicken Sie auf *Fortfahren*.
1. Xamarin wird nun heruntergeladen und installiert.  Je nachdem, welche Produkte Sie in Schritt 4 oben ausgewählt haben, kann dies eine Weile dauern.
1. *Starten Sie Xamarin Studio*.
1. Navigieren Sie zu *Hilfe* > *Nach Updates suchen*. Aktualisieren Sie Xamarin Studio und starten Sie es neu, falls erforderlich.
1. *Xamarin Studio* - sowie Xamarin.Android und Xamarin.iOS - sind nun installiert.

## Aktualisieren Sie das Android-SDK

Sobald Xamarin Studio selbst aktualisiert wurde, müssen Sie die Updates für das Android-SDK abrufen.

#### Schrittweise Anleitung

1. Navigieren Sie in *Xamarin Studio* zu *Tools* > *Open Android SDK Manager...*.
1. Warten Sie im Fenster *Android SDK Manager*, bis der Manager den Abruf des Update-Manifests beendet hat.
1. *Hinweis*: Sie müssen den SDK-Manager möglicherweise als Administrator ausführen. Der Standardpfad zum Android-SDK lautet: *C:\Benutzer\Ihr_Name\AppData\Local\Android\android-sdk*.
1. Je nachdem, wann Sie die Xamarin-Tools heruntergeladen haben, sollten Sie aus Gründen der Abwärtskompatibilität sowohl die neueste API (21 zum Zeitpunkt des Schreibens) als auch die letzten beiden (20 und 19) installieren. Aktivieren Sie die kleinen Kontrollkästchen neben den Namen und klicken Sie dann auf die Schaltfläche *Install N packages...*.
1. Daraufhin wird ein (sehr fehlerhaftes) Fenster angezeigt, in dem Sie alle Lizenzen für jeden Artikel akzeptieren müssen, bevor Sie fortfahren. Wenn die Schaltfläche *Installieren* nicht funktioniert, verlassen Sie das Fenster, öffnen Sie es erneut und klicken Sie einzeln auf das Optionsfeld Accept auf der linken Seite, bis es funktioniert.
![android sdk](/images/rhinomobile-installing-tools-windows-01.png)
1. *Hinweis* Das Herunterladen kann je nach Ihrer Internetverbindung eine Weile dauern.

## Installieren Sie den Intel-HAXM

Der [Intel-HAXM ist der Intel Hardware Acceleration Execution Manager](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/).  HAXM bietet eine hardwarebeschleunigte Engine für die x86-Android-Emulatoren. Ohne HAXM sind die Emulatoren fast unbrauchbar, da ihre Leistung so stark nachlässt. Mit HAXM sind die x86-Emulatoren jedoch reaktionsschnell und brauchbar. Nicht so schnell wie ein echtes Gerät, aber zumindest passabel. Es kann über den Android-SDK-Manager installiert werden, aber die dortige Version ist unwirksam. Rufen Sie es stattdessen über den obigen Link ab.  HAXM funktioniert nicht in einer virtualisierten Umgebung, z. B. einer VM. Wenn Sie also Ihre Android-Entwicklung in einer Windows-VM durchführen, müssen Sie ein Gerät verwenden.

#### Schrittweise Anleitung

1. Besuchen Sie die [Website für beschleunigte Ausführung von Intel Hardware](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/).
1. Suchen Sie den Abschnitt *Microsoft Windows* auf der Seite.
1. Laden Sie die Datei *haxm-windows_rxx.zip* herunter.  Möglicherweise werden Sie aufgefordert, eine Lizenzvereinbarung zu akzeptieren, bevor das Herunterladen beginnen kann.
1. Entpacken Sie *haxm-windows_rxx.zip*.
1. Installieren Sie den HAXM, indem Sie die ausführbare Datei *intelhaxm-android.exe* ausführen.

## RhinoCommon klonen

RhinoMobile basiert auf [RhinoCommons rhino3dmio-Verzweigung](https://github.com/mcneel/rhinocommon/tree/rhino3dmio). Sie können RhinoCommon entweder als Zip-Datei herunterladen oder das Repository mit Git klonen (empfohlen). (Wenn Sie neu bei GitHub sind, gibt es eine [GitHub Windows Desktop](https://desktop.github.com/) App für den Einstieg).

#### Schrittweise Anleitung

1. Entpacken oder klonen Sie *[rhinocommon (rhino3dmio branch)](https://github.com/mcneel/rhinocommon/tree/rhino3dmio)* in einen geeigneten Ordner, z.B. *C:\Benutzer\Ihr_Name\Entwicklung\Repos\rhinocommon*:
![clone rhinocommon](/images/rhinomobile-installing-tools-windows-02.png)
1. *[Laden Sie openNURBS herunter](http://www.rhino3d.com/download/opennurbs/5.0/commercial)*. RhinoMobile benötigt das C++ openNURBS SDK.
1. Entpacken Sie openNURBS und legen Sie den Inhalt in den Ordner *rhinocommon\c\opennurbs* (der Ordner, der nur die *readme.md* -Datei enthält):
![opennurbs](/images/rhinomobile-installing-tools-windows-03.png)
1. Es ist nicht möglich, die native openNURBS-Mobile-Library für iOS unter Windows zu erstellen - dazu ist ein Mac erforderlich. Der Einfachheit halber haben wir [vorgefertigte Binärdateien für iOS](http://files.na.mcneel.com/opennurbs/5.0/sdk/RhinoMobile-ONBinaries.zip) bereitgestellt, die Sie in Ihrem Projekt auf der Windows-Seite verwenden können. Sobald diese Binärdateien heruntergeladen wurden, verschieben Sie den Ordner *Release-ios* in den Ordner *rhinocommon\c\build\* .
![opennurbs](/images/rhinomobile-installing-tools-windows-04.png)

## RhinoMobile klonen

Sie müssen [RhinoMobile](http://github.com/mcneel/RhinoMobile) und die [RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples)-Repos herunterladen oder klonen. (Wenn Sie neu bei GitHub sind, gibt es eine [GitHub Windows Desktop](https://desktop.github.com/) App für den Einstieg).

#### Schrittweise Anleitung

1. Entpacken oder klonen Sie *[RhinoMobile](http://github.com/mcneel/RhinoMobile)* in einen Ordner *parallel zu rhinocommon* (oben geklont). Wenn sich zum Beispiel *rhinocommon* im Ordner     *C:\Benutzer\Ihr_Name\Entwicklung\Repos\rhinocommon* befindet, dann sollte sich RhinoMobile im Ordner *C:\Benutzer\Ihr_Name\Entwicklung\Repos\RhinoMobile* befinden:
![rhinomobile](/images/rhinomobile-installing-tools-windows-05.png)
1. Entpacken oder klonen Sie *[RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples)* in einen Ordner *parallel zu rhinocommon* und *RhinoMobile*:
![rhinomobilesamples](/images/rhinomobile-installing-tools-windows-06.png)

## Weitere Schritte:

*Herzlichen Glückwunsch!*  Sie haben alle notwendigen Werkzeuge, um eine mobile Anwendung zu erstellen, die RhinoMobile verwendet.  *Was nun?*

Im Leitfaden [Ihre erste App (Windows)](/guides/rhinomobile/your-first-app-windows) finden Sie eine Anleitung, um genau das zu ertellen: Ihre erste App.

## Verwandte Themen

- [Was ist RhinoMobile?](/guides/rhinomobile/what-is-rhinomobile/)
- [Was ist RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon/)
- [Was sind Mono und Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Installation von Werkzeugen (Mac)](/guides/rhinomobile/installing-tools-mac/)
- [Ihre erste App (Windows)](/guides/rhinomobile/your-first-app-windows)

**Fußnoten**

[^1]: Visual Studio Code is Microsoft's cross-platform source code editor for Windows, Linux, and macOS.  At the time of this writing, Visual Studio code does not yet support the features required to author RhinoMobile apps.

[^2]: Visual Studio Online is Microsoft's online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio "eigentlich" oben).  Wir haben die Verwendung von Visual Studio Online nicht zum Debuggen von RhinoMobile-Anwendungen getestet.

[^3]: Visual Studio "eigentlich" ist die Desktop-Version von Visual Studio... wir fügen den Beinamen "eigentlich" nur hinzu, um sie von Visual Studio Code und Visual Studio Online zu unterscheiden.  In den folgenden Handbüchern wird dies einfach als "Visual Studio" bezeichnet.

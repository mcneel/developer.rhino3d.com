+++
aliases = ["/en/5/guides/rhinomobile/installing-tools-mac/", "/en/6/guides/rhinomobile/installing-tools-mac/", "/en/7/guides/rhinomobile/installing-tools-mac/", "/en/wip/guides/rhinomobile/installing-tools-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "Diese Anleitung behandelt alle notwendigen Werkzeuge, die für RhinoMobile auf dem Mac benötigt werden."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Installation von Werkzeugen (Mac)"
type = "guides"
weight = 2

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
RhinoMobile wird nicht mehr unterstützt. Rhino 3dm File I/O ist weiterhin auf iOS und Android über die [rhino3dm Bibliothek](https://github.com/mcneel/rhino3dm)verfügbar.
{{< /call-out >}}
 
Am Ende dieses Leitfadens sollten Sie alle Tools installiert haben, die für das Verfassen, Erstellen und Debuggen von mobilen C#-Anwendungen mit RhinoMobile in Xamarin Studio erforderlich sind.

## Voraussetzungen

Falls Sie dies noch nicht getan haben, lesen Sie bitte den Leitfaden [Was ist RhinoMobile?](/guides/rhinomobile/what-is-rhinomobile/)

Dieser Leitfaden wurde konzipiert für die Verwendung eines:

- [Apple Mac](http://store.apple.com/) mit [OS X Yosemite](https://www.apple.com/osx/) (10.10) oder neuer.

## Xcode installieren

[Xcode](https://developer.apple.com/xcode/) ist die Entwicklungsplattform und IDE von Apple.

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
1. Xamarin verwendet eine Installationsanwendung, die die von Ihnen ausgewählten Komponenten herunterlädt und installiert.  Sobald Sie die Datei *XamarinInstaller.dmg*heruntergeladen haben, doppelklicken Sie darauf, um die Image-Datei zu mounten.  Doppelklicken Sie auf das große Symbol *Install Xamarin* , um das Installationsprogramm einzuhängen.
1. Sie müssen die Xamarin-Software-Lizenzvereinbarung akzeptieren, um die Xamarin-Plattform nutzen zu können.
1. Die *Xamarin-Plattform* besteht aus folgenden Teilen:
   - Xamarin Studio
   - Xamarin.Android[^1]
   - Xamarin.iOS[^2]
   - Xamarin.Mac[^3]
...stellen Sie sicher, dass *Xamarin.Android* und *Xamarin.iOS* markiert sind und klicken Sie auf *Fortfahren*.
1. Wenn Sie Xcode nicht installiert haben, werden Sie von Xamarin dazu aufgefordert.  Siehe [Installation von Xcode](#install-xcode) oben.
1. Xamarin installiert: *Mono Framework*, *Xamarin Studio*, *Xamarin.Android* und *Xamarin.iOS*.  Klicken Sie auf *Fortfahren*.
1. Xamarin wird nun heruntergeladen und installiert.  Je nachdem, welche Produkte Sie in Schritt 4 oben ausgewählt haben, kann dies eine Weile dauern.
1. Wenn das Installationsprogramm abgeschlossen ist, klicken Sie auf die Schaltfläche *Launch Xamarin Studio* .
1. *Xamarin Studio* - sowie das Mono Framework, Xamarin.Android und Xamarin.iOS - sind nun installiert.
1. Xamarin Studio wird in Ihrem Ordner */Programme* installiert. Sie sollten *das Symbol in Ihr Dock* ziehen, um es später zu verwenden, oder - wenn es läuft - mit der rechten Maustaste auf das Symbol im Dock klicken und *Im Dock behalten*wählen.

## Aktualisieren Sie das Android-SDK

Sobald Xamarin Studio selbst aktualisiert wurde, müssen Sie die Updates für das Android-SDK abrufen.

#### Schrittweise Anleitung

1. Navigieren Sie in *Xamarin Studio* zu *Tools* > *Open Android SDK Manager...*.
1. Warten Sie im Fenster *Android SDK Manager*, bis der Manager den Abruf des Update-Manifests beendet hat.
1. Je nachdem, wann Sie die Xamarin-Tools heruntergeladen haben, sollten Sie aus Gründen der Abwärtskompatibilität sowohl die neueste API (21 zum Zeitpunkt des Schreibens) als auch die letzten beiden (20 und 19) installieren. Aktivieren Sie die kleinen Kontrollkästchen neben den Namen und klicken Sie dann auf die Schaltfläche *Install N packages...*.
1. Daraufhin wird ein (sehr fehlerhaftes) Fenster angezeigt, in dem Sie alle Lizenzen für jeden Artikel akzeptieren müssen, bevor Sie fortfahren. Wenn die Schaltfläche *Installieren* nicht funktioniert, verlassen Sie das Fenster, öffnen Sie es erneut und klicken Sie einzeln auf das Optionsfeld Accept auf der linken Seite, bis es funktioniert.
![android sdk](/images/rhinomobile-installing-tools-mac-01.png)
1. *Hinweis:* Das Herunterladen kann je nach Ihrer Internetverbindung eine Weile dauern.

## Installieren Sie den Intel-HAXM

Der [Intel-HAXM ist der Intel Hardware Acceleration Execution Manager](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/).  HAXM bietet eine hardwarebeschleunigte Engine für die x86-Android-Emulatoren. Ohne HAXM sind die Emulatoren fast unbrauchbar, da ihre Leistung so stark nachlässt. Mit HAXM sind die x86-Emulatoren jedoch reaktionsschnell und brauchbar. Nicht so schnell wie ein echtes Gerät, aber zumindest passabel. Es kann über den Android-SDK-Manager installiert werden, aber die dortige Version ist unwirksam. Rufen Sie es stattdessen über den obigen Link ab.  HAXM funktioniert nicht in einer virtualisierten Umgebung, z. B. einer VM. Wenn Sie also Ihre Android-Entwicklung in einer Windows-VM durchführen, müssen Sie ein Gerät verwenden.

#### Schrittweise Anleitung

1. Besuchen Sie die [Website für beschleunigte Ausführung von Intel Hardware](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/).
1. Suchen Sie den Abschnitt *macOS* auf der Seite.
1. Laden Sie die Datei *haxm-macosx_rxx.zip*herunter.  Möglicherweise werden Sie aufgefordert, eine Lizenzvereinbarung zu akzeptieren, bevor das Herunterladen beginnen kann.
1. Entpacken Sie *haxm-macosx_rxx.zip*.
1. Hängen Sie die *IntelHAXM_x.x.x.dmg* ein, indem Sie darauf doppelklicken.
1. Installieren Sie HAXM durch Doppelklick auf die Datei *IntelHAXM_x.x.x.mpkg* .

## RhinoCommon klonen

RhinoMobile basiert auf [RhinoCommons rhino3dmio-Verzweigung](https://github.com/mcneel/rhinocommon/tree/rhino3dmio). Sie können RhinoCommon entweder als Zip-Datei herunterladen oder das Repository mit Git klonen (empfohlen). (Wenn Sie neu bei GitHub sind, gibt es eine [GitHub Mac Desktop](https://desktop.github.com/) App für den Einstieg).

#### Schrittweise Anleitung

1. Entpacken oder klonen Sie *[rhinocommon (rhino3dmio-Verzweigung)](https://github.com/mcneel/rhinocommon/tree/rhino3dmio)*  in einen geeigneten Ordner, z.B. den Ordner */Benutzer/Ihr_Name/Entwicklung/Repos/rhinocommon* :
![clone rhinocommon](/images/rhinomobile-installing-tools-mac-02.png)
1. *[Laden Sie openNURBS herunter](http://www.rhino3d.com/download/opennurbs/5.0/commercial)*. RhinoMobile benötigt das C++ openNURBS SDK.
1. Entpacken Sie openNURBS und legen Sie den Inhalt in den Ordner *rhinocommon/c/opennurbs/* (der Ordner, der nur die *readme.md* -Datei enthält):
![opennurbs](/images/rhinomobile-installing-tools-mac-03.png)

## RhinoMobile klonen

Sie müssen [RhinoMobile](http://github.com/mcneel/RhinoMobile) und die [RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples)-Repos herunterladen oder klonen. (Wenn Sie neu bei GitHub sind, gibt es eine [GitHub Mac Desktop](https://desktop.github.com/) App für den Einstieg).

#### Schrittweise Anleitung

1. Entpacken oder klonen Sie *[RhinoMobile](http://github.com/mcneel/RhinoMobile)* in einen Ordner *parallel zu rhinocommon* (oben geklont). Wenn sich zum Beispiel *rhinocommon* im Ordner     */Benutzer/Ihr_Name/Entwicklung/Repos/rhinocommon* befindet, dann sollte sich RhinoMobile im Ordner */Benutzer/Ihr_Name/Entwicklung/Repos/RhinoMobile* befinden:
![rhinomobile](/images/rhinomobile-installing-tools-mac-04.png)
1. Entpacken oder klonen Sie *[RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples)* in einen Ordner *parallel zu rhinocommon* und *RhinoMobile*:
![rhinomobilesamples](/images/rhinomobile-installing-tools-mac-05.png)

## Weitere Schritte:

*Herzlichen Glückwunsch!*  Sie haben alle notwendigen Werkzeuge, um eine mobile Anwendung zu erstellen, die RhinoMobile verwendet.  *Was nun?*

Im Leitfaden [Ihre erste App (Mac)](/guides/rhinomobile/your-first-app-mac) finden Sie eine Anleitung, um genau das zu ertellen: Ihre erste App.

## Verwandte Themen

- [Was ist RhinoMobile?](/guides/rhinomobile/what-is-rhinomobile/)
- [Was ist RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon/)
- [Was sind Mono und Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Installieren von Tools (Windows)](/guides/rhinomobile/installing-tools-windows/)
- [Ihre erste App (Mac)](/guides/rhinomobile/your-first-app-mac)

**Fußnoten**

[^1]: Xamarin.Android is used to build C# .NET applications for Android devices.

[^2]: Xamarin.iOS is used to build C# .NET applications for Apple iOS devices.

[^3]: Xamarin.Mac is Xamarin's proprietary closed-source toolkit build on the open-source MonoMac (aka Mono for macOS).  Xamarin.Mac provides a commercial license of Mono, bindings to additional frameworks, and the ability to create self-contained application bundles that do not require mono.  RhinoMobile does not currently use Xamarin.Mac.

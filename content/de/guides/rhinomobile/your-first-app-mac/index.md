+++
aliases = ["/en/5/guides/rhinomobile/your-first-app-mac/", "/en/6/guides/rhinomobile/your-first-app-mac/", "/en/7/guides/rhinomobile/your-first-app-mac/", "/en/wip/guides/rhinomobile/your-first-app-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "Diese Anleitung führt Sie durch Ihre erste mobile App mit RhinoMobile und Xamarin Studio auf dem Mac."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Ihre erste App (Mac)"
type = "guides"
weight = 4

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/hellorhinomobile"
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

{{< call-out "warning" "RhinoMobile: Veraltet" >}}
RhinoMobile wird nicht mehr unterstützt. Rhino 3dm File I/O ist weiterhin auf iOS und Android über die [rhino3dm-Bibliothek](https://github.com/mcneel/rhino3dm) verfügbar.
{{< /call-out >}}
 
In dieser Anleitung wird davon ausgegangen, dass Sie die Anleitung [Installation von Werkzeugen (Mac)](/guides/rhinomobile/installing-tools-mac) durchgearbeitet und Xamarin Studio, Xcode und alle erforderlichen Bibliotheken erfolgreich installiert haben.

## HelloRhinoMobile

Wir gehen davon aus, dass Sie Xamarin Studio noch nie verwendet haben, also gehen wir Schritt für Schritt vor.  Zum Zeitpunkt der Erstellung dieses Artikels verwenden wir Xamarin Studio 5.9.7.

### iOS Boilerplate erstellen

1. *Starten Sie Xamarin Studio* und öffnen Sie die *HelloRhinoMobile*-Lösung.
1. *Klicken Sie mit der rechten Maustaste* auf das *HelloRhino.iOS*-Projekt und wählen Sie *Set As Startup Project* aus dem Dropdown-Menü. So wird *HelloRhino.iOS* zum aktiven Projekt für den Build gemacht. (HelloRhino.Touch ist das iOS-Zielprojekt.  Die HelloRhino.Touch-Projekte verwenden monotouch.dll - die ältere Version von Xamarin.iOS).
![hellorhinomobile solution](/images/your-first-app-mac-01.png)
1. Stellen Sie sicher, dass der Build auf *Debug* und das Gerät auf *iPhone Simulator* > *iPhone iOS 5 iOS 9* eingestellt ist. Klicken Sie auf die Schaltfläche *Play/Run*.
1. [Aktivieren Sie eine Xamarin-Testversion](http://docs.xamarin.com/guides/cross-platform/getting-started/beginning_a_xamarin_trial). Mit der Xamarin Business Edition können Sie eine 30tägige Testversion freischalten, die für die Erstellung und Verwendung von RhinoMobile erforderlich ist. Sie müssen [ein Xamarin-Login erstellen](https://auth.xamarin.com/account/register). Wenn Sie nicht in der Lage sind, eine Testversion zu starten, nachdem Sie ein Login erstellt haben, machen Sie sich keine Sorgen; Xamarin Studio wird Sie dazu auffordern, wenn Sie versuchen, RhinoMobile-Projekte zu erstellen. Möglicherweise müssen Sie das Projekt löschen und neu erstellen, wenn Sie weiterhin Fehler bei der Auswertung erhalten.
1. *Beenden* Sie Xamarin Studio und führen Sie einen *Neustart* aus.
1. Öffnen Sie auf dem Xamarin Studio-Startbildschirm erneut die *HelloRhinoMobile* -Lösung.
1. Überprüfen Sie, ob die Vollversion von Xamarin Studio aktiviert wurde. Navigieren Sie zu *Xamarin Studio* > *About Xamarin Studio* > *Show Details*. Scrollen Sie nach unten und vergewissern Sie sich, dass *Xamarin.iOS* und *Xamarin.Android* auf *Trial Edition* eingestellt sind.
1. Schließen Sie das Fenster *About Xamarin Studio*.
1. Klicken Sie erneut auf die Schaltfläche *Play/Run*. Diesmal sollte der Build fehlerfrei gelingen. (HINWEIS: Wenn Sie RhinoMobile.iOS zum ersten Mal erstellen, muss die libopennurbs-Bibliothek kompiliert werden. Nachfolgende Builds werden sehr viel schneller sein). Nach dem Hochladen des Anwendungspakets in den Simulator sollten Sie folgendes sehen:
![hellorhinomobile on ios](/images/your-first-app-mac-02.png)
1. Wenn Sie mit dem HelloRhino-Beispiel im iOS-Simulator fertig sind, klicken Sie in Xamarin Studio auf die Schaltfläche *Stop*, um die Debug-Sitzung zu beenden.  Jetzt wollen wir einen...

### Android-Boilerplate-Build erstellen

1. Klicken Sie mit der rechten Maustaste auf das Projekt *HelloRhino.Droid* und wählen Sie *Set As Startup Project* aus dem Dropdown-Menü. Wie erwartet, wird so das Android-Projekt zum Standardprojekt für den Build...
![hellorhinomobile solution with android](/images/your-first-app-mac-03.png)
1. *Vergewissern Sie sich, dass der Build auf Debug eingestellt ist.*  Dieses Mal sollte das Dropdown-Menü für die Geräteauswahl deaktiviert werden. Das liegt daran, dass Sie noch keinen Emulator eingerichtet haben, was wir jetzt nachholen.
1. Klicken Sie auf die Schaltfläche *Play/Run*, um den *HelloRhino.Droid*-Debug-Build zu starten. (HINWEIS: Wenn Sie RhinoMobile.Droid zum ersten Mal erstellen, muss die libopennurbs-Bibliothek kompiliert werden... dies kann bis zu 20 Minuten dauern. Nachfolgende Builds werden sehr viel schneller sein).
1. Das Fenster *Gerät auswählen** sollte erscheinen. In diesem Fenster teilen Sie dem Android SDK mit, welchen Emulator oder welches Gerät Sie für die Tests verwenden möchten. Keine der Standardeinstellungen reicht aus, also müssen wir einen schnelleren Emulator erstellen...
1. Klicken Sie auf die Schaltfläche *Emulator erstellen*.
1. Der *Android Virtual Device Manager* sollte starten. Er ist Teil des Android-SDK und wird Ihnen vertraut sein, wenn Sie schon einmal Android entwickelt haben. Hier definieren Sie Ihre virtuellen Android-Geräte (AVDs), die im Emulator laufen.
1. *Heben Sie jede der vorhandenen AVDs hervor* und klicken Sie auf die Schaltfläche *Löschen*. Diese AVDs sind viel zu langsam für die Entwicklung.
1. Um eine neue AVD zu erstellen, klicken Sie auf die Schaltfläche *Create*. Das Fenster Create new Android Virtual Device (AVD)  wird angezeigt. Erstellen Sie einen neuen AVD mit den folgenden Parametern: *AVD-Name*: Nexus7-API17-IntelHAXM; *Device*: Nexus 7; *Target*: Android 4.2.2 - API Level 17; *CPU/ABI*: Intel Atom (x86); *Front Camera*: Webcam0; *VM Heap*: 64 *Emulation Options*: Use Host GPU enabled...
![create new android virtual device](/images/your-first-app-mac-04.png)
1. Sie sollten Ihr neues AVD in der Liste sehen. Sie haben gerade Ihr erstes AVD erstellt.  Weitere Informationen zur Erstellung von Emulatoren finden Sie in der [Android-Dokumentation zur Verwaltung von Geräten](http://developer.android.com/tools/devices/index.html). Sie können so viele erstellen, wie Sie benötigen. Tipps zur Verwendung des Emulators finden Sie im Leitfaden [Einsatz von Simulatoren](/guides/rhinomobile/using-simulators/).  Zunächst *beenden Sie den Android Virtual Device Manager* und kehren Sie zu Xamarin Studio zurück.
1. Sie sollten das Fenster *Gerät auswählen* erneut sehen, diesmal mit Ihrem neuen AVD in der Liste. Markieren Sie das AVD und klicken Sie auf die Schaltfläche *Start Emulator* . Wenn alles gut verlaufen ist, sollten Sie nach einer kurzen Startphase sehen, wie Android startet (seien Sie versichert, es geht viel schneller als bei den Standard-Emulatoren). Beim ersten Start kann es etwas länger dauern, und es wird dringend empfohlen, dieses Fenster während Ihrer Entwicklungssitzung geöffnet zu lassen. Sobald Android gebootet ist, können Sie loslegen... Sie müssen das Gerät nur noch entsperren, indem Sie das Schloss nach rechts schieben.
1. Schließen Sie den Android-Emulator nicht. *Wechseln Sie zurück zu Xamarin Studio*. Klicken Sie im Fenster *Select Device*, falls das Label *not started* noch nicht verschwunden ist, auf die Schaltfläche *Refresh*. Sobald Sie das AVD in schwarzer, auswählbarer Schrift sehen, wissen Sie, dass Xamarin Studio bereit ist, die App auf dem Emulator zu starten.  Heben Sie das AVD hervor und klicken Sie auf *OK*.
1. Wenn alles gut geht, sollten Sie, ähnlich wie bei iOS, folgendes sehen:
![hellorhino android](/images/your-first-app-mac-05.png)
1. Wenn Sie mit dem HelloRhino.Droid-Build fertig sind, klicken Sie zurück in Xamarin Studio auf die Schaltfläche *Stop*, um die Debug-Sitzung zu beenden.

*Herzlichen Glückwunsch!*  Sie haben eine RhinoMobile-Anwendung für zwei Plattformen mit gemeinsamem Code erstellt.

## Verwandte Themen

- [Installation von Werkzeugen (Mac)](/guides/rhinomobile/installing-tools-mac)
- [Ihre erste App (Windows)](/guides/rhinomobile/your-first-app-windows)
- [Verwendung von Simulatoren](/guides/rhinomobile/using-simulators)
- [Prüfung auf Geräten](/guides/rhinomobile/testing-on-devices)
- [Geräte verwalten (Android-Dokumentation)](http://developer.android.com/tools/devices/index.html)

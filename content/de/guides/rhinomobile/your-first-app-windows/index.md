+++
aliases = ["/en/5/guides/rhinomobile/your-first-app-windows/", "/en/6/guides/rhinomobile/your-first-app-windows/", "/en/7/guides/rhinomobile/your-first-app-windows/", "/en/wip/guides/rhinomobile/your-first-app-windows/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "Diese Anleitung führt Sie durch Ihre erste mobile App mit RhinoMobile und Visual Studio Studio auf Windows."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Ihre erste App (Windows)"
type = "guides"
weight = 5

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

In dieser Anleitung wird davon ausgegangen, dass Sie die Anleitung [Installation von Werkzeugen (Windows)](/guides/rhinomobile/installing-tools-windows) durchgearbeitet und Xamarin und alle erforderlichen Bibliotheken erfolgreich installiert haben.  Diese Anweisungen setzen voraus, dass Sie Visual Studio 2017 Professional verwenden.

## HelloRhinoMobile

In dieser Anleitung wird davon ausgegangen, dass Sie Visual Studio 2017 Professional verwenden, obwohl dieser Prozess auch mit Visual Studio 2013 funktionieren sollte.

### Android-Boilerplate-Build erstellen

1. *Starten Sie Visual Studio* und öffnen Sie die *HelloRhinoMobile*-Lösung.
1. *Klicken Sie mit der rechten Maustaste* auf das Projekt *HelloRhino.Droid* und wählen Sie *Set As StartUp Project* aus dem Dropdown-Menü. So wird *HelloRhino.Droid*  zum aktiven Projekt für den Build gemacht. (HelloRhino.Droid ist das Android-Zielprojekt. Das Suffix .Droid ist eine Namenskonvention von Mono, die Namenskollisionen mit den wichtigsten Android-Bibliotheken vermeidet).
![hellorhinomobile solution](/images/your-first-app-windows-01.png)
1. Öffnen Sie den *Android Emulator Manager*: Navigieren Sie zu *Tools* > *Open Android Emulator Manager*. Ein Fenster namens *Android Virtual Device (AVD) Manager* sollte erscheinen. Dies ist Teil des Android-SDK und wird Ihnen vertraut sein, wenn Sie schon einmal Android entwickelt haben. Hier definieren Sie Ihre virtuellen Android-Geräte (AVDs), die im Emulator laufen.
![avd manager](/images/your-first-app-windows-02.png)
1. Die Standard-AVDs sind für die Entwicklung viel zu langsam. *Heben Sie jede der vorhandenen AVDs hervor* und klicken Sie auf die Schaltfläche *Delete* .
1. Um eine neue AVD zu erstellen: Klicken Sie auf die Schaltfläche *Neu*. Das Fenster Create new Android Virtual Device (AVD)  wird angezeigt. Erstellen Sie einen neuen AVD mit den folgenden Parametern: *AVD-Name*: Nexus7-API17; *Device*: Nexus 7 (7.02“, 1200 x 1920:xhdpi); *Target*: Android 4.3 - API Level 18; *CPU/ABI*: Intel Atom (x86); *Skin*: Skin with dynamic hardware controls; *Front Camera*: Webcam0; *VM Heap*: 64 *Emulation Options*: Use Host GPU enabled ...
![create new avd](/images/your-first-app-windows-03.png)
1. Sie sollten Ihr neues AVD in der Liste sehen. Sie haben gerade Ihr erstes AVD erstellt. Weitere Informationen zur Erstellung von Emulatoren finden Sie in der [Android-Dokumentation zur Verwaltung von Geräten](http://developer.android.com/tools/devices/index.html). Sie können so viele erstellen, wie Sie benötigen. Tipps zur Verwendung des Emulators finden Sie im Leitfaden [Einsatz von Simulatoren](/guides/rhinomobile/using-simulators/).
1. *Schließen Sie* den *AVD-Manager*. Wechseln Sie zurück zu *Visual Studio*.
1. Klicken Sie auf die Schaltfläche *Info* in der Xamarin.Android-Werkzeugleiste.
![info button](/images/your-first-app-windows-04.png)
1. Daraufhin erscheint das Fenster *Android Device Logging*. Klicken Sie auf die Schaltfläche *Change Device* ...
![select device window](/images/your-first-app-windows-05.png)
1. Daraufhin erscheint das Fenster *Select Device*, in dem alle laufenden Geräte (Emulatoren und physische Geräte) aufgelistet sind. Klicken Sie auf die Schaltfläche *Start emulator image*.
![start emulator](/images/your-first-app-windows-06.png)
1. Daraufhin wird dieselbe Liste verfügbarer AVD-Images angezeigt, die Sie im Fenster Android Virtual Device (AVD) Manager gesehen haben. Wählen Sie das *Nexus7-API18 AVD*, das Sie oben erstellt haben. Klicken Sie auf *OK*.
![select device](/images/your-first-app-windows-07.png)
1. Wenn alles gut verlaufen ist, sollten Sie nach einer kurzen Startphase sehen, wie Android startet (seien Sie versichert, es geht viel schneller als bei den Standard-Emulatoren). Beim ersten Start kann es etwas länger dauern, und es wird dringend empfohlen, dieses Fenster während Ihrer Entwicklungssitzung geöffnet zu lassen. Sobald Android gebootet ist, können Sie loslegen... Sie müssen das Gerät nur noch entsperren, indem Sie das Schloss nach rechts schieben. Wir sind nun bereit, die Anwendung an den Emulator zu senden.
1. Im *Solution Explorer* *klicken Sie mit der rechten Maustaste* auf das *HelloRhino.Droid*-Projekt und wählen Sie *Deploy*. HelloRhino.Droid wird zusammen mit seiner Kopplung, RhinoMobile.Droid, erstellt. (HINWEIS: Wenn Sie RhinoMobile.Droid zum ersten Mal erstellen, muss die libopennurbs-Bibliothek kompiliert werden... dies kann bis zu 20 Minuten dauern. Nachfolgende Builds werden sehr viel schneller sein).
1. Sobald die Anwendung auf dem laufenden Emulator bereitgestellt wurde, können Sie die Anwendung ausführen. Klicken Sie in *Visual Studio* auf die Schaltfläche *Start*. Wenn alles gut geht, sollten Sie etwas wie das hier sehen...
![hellorhinomobile android](/images/your-first-app-windows-08.png)

*Herzlichen Glückwunsch!*  Sie haben eine RhinoMobile-App für Android erstellt.

### iOS Boilerplate erstellen

IN VORBEREITUNG

## Verwandte Themen

- [Installation von Werkzeugen (Windows)](/guides/rhinomobile/installing-tools-windows)
- [Ihre erste App (Mac)](/guides/rhinomobile/your-first-app-mac)
- [Verwendung von Simulatoren](/guides/rhinomobile/using-simulators)
- [Prüfung auf Geräten](/guides/rhinomobile/testing-on-devices)
- [Geräte verwalten (Android-Dokumentation)](http://developer.android.com/tools/devices/index.html)

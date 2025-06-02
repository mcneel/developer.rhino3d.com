+++
aliases = ["/en/5/guides/rhinomobile/using-simulators/", "/en/6/guides/rhinomobile/using-simulators/", "/en/7/guides/rhinomobile/using-simulators/", "/en/wip/guides/rhinomobile/using-simulators/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "Dieser Leitfaden behandelt die Grundlagen der Verwendung von Emulatoren oder Simulatoren zum Debuggen Ihrer mobilen Anwendung."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Einsatz von Simulatoren"
type = "guides"
weight = 6

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/simulators_and_emulators"
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
RhinoMobile wird nicht mehr unterstützt. Rhino 3dm File I/O ist weiterhin auf iOS und Android über die [rhino3dm Bibliothek](https://github.com/mcneel/rhino3dm) verfügbar.
{{< /call-out >}}
 
Android bietet Emulatoren und iOS bietet Simulatoren, beide mit ihren Vorteilen und Schwächen.

## Android-Emulatoren

<img align="right" src="/images/using-simulators-01.png" width="121">

Android-Emulatoren sind eine gute Annäherung an die tatsächlichen Geräte selbst, obwohl die Leistung leicht variieren kann. Der Android-Emulator leistet gute Dienste bei der Virtualisierung von Hardwarekonfigurationen und ihre Schwachstellen, wenn es nötig ist (Sie können z. B. den Arbeitsspeicher in einer Weise begrenzen, die mit dem iOS-Simulator nicht möglich ist). Dennoch ist es wichtig, auf realen Geräten zu testen, insbesondere angesichts der funktionalen Einschränkungen des Emulators (z. B. kein Multitouch) und der großen Vielfalt an Android-Geräten auf dem Markt mit ihren unterschiedlichen Hardwarekonfigurationen und -fähigkeiten. Wenn die Emulatoren einmal richtig eingerichtet sind, können sie Sie im Entwicklungsprozess ein gutes Stück voranbringen, bevor Sie auf echten Geräten testen.

### Drehung und Multi-Touch

Die folgenden Tastenkombinationen können verwendet werden, um Emulatoren zu drehen:

- <kbd>fn</kbd> + <kbd>Strg</kbd> + <kbd>F12</kbd> = Emulator drehen (macOS)
- <kbd>Links-Strg</kbd> + <kbd>F12</kbd> = Emulator drehen (Windows)

*Hinweis*: Sie können nicht mehrere Berührungen auf dem Android-Emulator simulieren.

### Dateisystem des Emulators

Der beste Weg, um auf die Einbauten eines Android-Geräts oder eines Emulators zuzugreifen, ist die Verwendung der [Android Debug Bridge](http://developer.android.com/tools/help/adb.html) (ADB), die mit dem Android SDK als Teil des Xamarin Toolkits geliefert wird. ADB wird mit einem Shell-Dienstprogramm geliefert, mit dem Sie das Android-Dateisystem wie ein Standard-Linux-Dateisystem durchsuchen können - was es auch ist. Die Ausführung der ADB-Shell auf einem Mac unterscheidet sich geringfügig von der Ausführung unter Windows, aber hier sind die Grundlagen.

**macOS**

Bevor wir die ADB-Tools starten, müssen wir sicherstellen, dass das Android SDK und NDK Teil unserer Bash-Terminal-Umgebung sind. Öffnen Sie Ihr *.bash_profile* (in Ihrem *~* oder Home-Ordner) mit einem vertrauten Texteditor (wir empfehlen [TextWrangler](http://www.barebones.com/products/textwrangler/) oder [BBEdit](http://www.barebones.com/products/bbedit/)). Fügen Sie die folgenden Zeilen in Ihr Profil ein, falls sie noch nicht vorhanden sind:

```
export ANDROID_SDK="/Benutzer/Ihr_Name/Library/Developer/Xamarin/android-sdk-mac_x86/"
export ANDROID_NDK="/Benutzer/Ihr_Name/Library/Developer/Xamarin/android-ndk/android-ndk-r8d/"
export PATH="$PATH:$ANDROID_SDK/tools:$ANDROID_SDK/platform-tools:$ANDROID_NDK"
export _JAVA_OPTIONS="-Xmx1g"
```

Die ersten beiden Zeilen teilen Ihrer Bash-Umgebung mit, wo sie nach dem Android SDK und NDK suchen soll. Die Option `_JAVA_OPTIONS="-Xmx1g"` erhöht die Heap-Größe, die Xamarin Studio für native Java-Binärdateien verwenden kann.

Speichern Sie Ihr Profil und öffnen Sie ein Terminal-Fenster. Sie sollten nun in der Lage sein, adb shell einzugeben. Wenn Sie keinen Emulator laufen haben oder kein Gerät angeschlossen ist, erhalten Sie die Fehlermeldung: Gerät nicht gefunden. Das ist in Ordnung, es bedeutet, dass die adb-Shell eingerichtet ist. Schließen Sie ein Gerät an oder starten Sie einen Emulator und versuchen Sie den Befehl "adb shell" erneut. Jetzt sollten Sie in Ihrem Terminal etwa Folgendes sehen:

![adb shell](/images/using-simulators-02.png)

Sie können viele Standard-Linux-Befehle verwenden, um Dateien zu meiden und durcheinander zu bringen. Beachten Sie, dass es eine Reihe spezieller Befehle gibt, um Dateien auf das Gerät/den Emulator zu schieben und von dort zu entfernen. In der [Android-ADB-Dokumentation](http://developer.android.com/tools/help/adb.html) finden Sie eine praktische Liste. Die Daten für viele Anwendungen werden im Ordner *data/data/AppName/* gespeichert.

**Windows**

Bevor wir die ADB-Tools starten, müssen wir sicherstellen, dass das Android-SDK und -NDK Teil der Umgebungsvariablen sind. Gehen Sie hierfür folgendermaßen vor:

1. Navigieren Sie zu den *Systemsteuerungen* in der Systemsteuerung (*Start* > *Systemsteuerung* > *System*)
1. Klicken Sie auf die Schaltfläche *Erweiterte Systemeinstellungen* auf der linken Seite.
1. Sie sollten nun das Fenster *Systemeigenschaften* sehen. Klicken Sie auf die Schaltfläche *Umgebungsvariablen...* auf der Registerkarte Erweitert.
1. Im Feld *Systemvariablen* (das untere Feld) scrollen Sie durch die Liste, bis Sie *Pfad* unter der Spalte Variable sehen.
1. Klicken Sie auf *Pfad* , um ihn zu markieren, und dann auf die Schaltfläche *Bearbeiten...*.
1. Wir werden unseren Pfad zu adb hinzufügen, wo Xamarin das android-sdk installiert hat. Vergewissern Sie sich, dass sich Ihr Mauszeiger am Ende des letzten Eintrags befindet, und geben Sie dann ein: *;C:\Benutzer\Ihr_Name\AppData\Local\Android\android-sdk\platform-tools\* ersetzen Sie *you* durch den Namen Ihres Kontos. Achten Sie darauf, dass dieser Pfad keine Leerzeichen enthält. Wenn der Pfad zu Ihrem android-sdk an einer benutzerdefinierten Stelle liegt, ersetzen Sie ihn durch diesen Pfad.
1. Klicken Sie bei allem auf *OK* und *schließen Sie die Systemsteuerung* , falls sie noch geöffnet ist.

Öffnen Sie eine Eingabeaufforderung "cmd.exe". Geben Sie nun `adb shell` ein. Vergewissern Sie sich, dass ein Emulator gestartet oder ein Gerät angeschlossen ist, so sollten Sie ein adb-Shell-Tool sehen, das dem oben in der Mac-Anleitung gezeigten ähnelt. Sie können viele Standard-Linux-Befehle verwenden, um Dateien zu meiden und durcheinander zu bringen. Beachten Sie, dass es eine Reihe spezieller Befehle gibt, um Dateien auf das Gerät/den Emulator zu schieben und von dort zu entfernen. In der [Android-ADB-Dokumentation](http://developer.android.com/tools/help/adb.html) finden Sie eine praktische Liste. Die Daten für viele Anwendungen werden im Ordner *data/data/AppName/* gespeichert.

### Zurücksetzen von Emulatoren

Es ist selten notwendig, die Android-Emulatoren zurückzusetzen, da die gesamte App zwischen den Builds entfernt wird. Wenn Sie sie zurücksetzen müssen, ist es am besten, das gesamte AVD zu löschen und ein neues zu erstellen. Öffnen Sie den Android Virtual Device Manager (navigieren Sie in Xamarin Studio zu *Tools* > *Open Android Emulator Manager...* in der Anwendungs-Werkzeugleiste), wählen Sie auf der Registerkarte *Android Virtual Devices* den Emulator aus der Liste der AVDs und klicken Sie auf die Schaltfläche *Delete*.

## iOS-Simulatoren

<img align="right" src="/images/using-simulators-03.png" width="121">

Die iOS-Simulatoren sind eine bequeme Möglichkeit, Ihre App schnell mit verschiedenen Bildschirmgrößen, iOS-Versionen und auf verschiedenen Geräten zu testen. Sie können auf den Simulator zugreifen, indem Sie Ihre Anwendung im Debug- oder Freigabemodus ausführen und einen Simulator und Geräte aus dem Dropdown-Menü rechts neben den Steuerelementen Ausführen und Konfiguration auswählen.

<div class="bs-callout bs-callout-danger">
  <h4>ACHTUNG:</h4>
  <p>Simulatoren sind KEIN guter Ersatz für Tests auf echter iOS-Hardware. Das Verhalten bzw. die Leistung einer Anwendung auf einem Gerät kann erheblich vom Simulator abweichen, insbesondere bei OpenGL ES 2.0-Code.</p>
</div>

Um ältere Versionen des iOS Simulators zu installieren, starten Sie Xcode und navigieren Sie zu *Xcode* > *Preferences* > *Downloads* Registerkarte > *Components* Abschnitt > *click small download arrows* rechts neben der Simulator-Version, die Sie installieren möchten.

### Drehung und Multi-Touch

Die folgenden Tastenkombinationen können verwendet werden, um mehrere Berührungen zu drehen und zu simulieren:

- <kbd>Cmd</kbd> + <kbd>Pfeiltasten links/rechts</kbd> = Drehen des Simulators
- <kbd>Option</kbd> + *Den Cursor herumverschieben* = Zweifingergeste simulieren
- <kbd>Option</kbd> + <kbd>Umschalttaste</kbd> + *Den Cursor herumbewegen* = Schwenken mit zwei Fingern

### Dateisystem des Simulators

Der beste Weg, um auf den Inhalt des Dateisystems des Simulators zuzugreifen, ist die Verwendung eines Terminals. Öffnen Sie unter macOS ein Terminalfenster und navigieren Sie zu:

`~/Entwickler/CoreSimulator/Geräte/<code>/data/Containers/Data/Application/<app UDID number>/`

(Denken Sie daran, dass Sie die Tabulatortaste verwenden können, um Pfade automatisch zu vervollständigen, während Sie Verzeichnisse wechseln - was für die automatische Vervollständigung längerer UDIDs von Anwendungen nützlich ist).

Alternativ können Sie auch den Finder verwenden, um zu demselben Ordner zu navigieren, aber Sie müssen Ihre Finder-Einstellungen so ändern, dass versteckte Dateien angezeigt werden, falls Sie dies nicht bereits getan haben.

Weitere Informationen darüber, wo temporäre oder bleibende Ressourcen gespeichert werden können, finden Sie in der folgenden [Xamarin-Dokumentation](http://docs.xamarin.com/guides/ios/application_fundamentals/working_with_the_file_system/).

### Simulatoren zurücksetzen

Oft ist es notwendig, den gesamten Inhalt des Simulators zwischen zwei Builds zu löschen, insbesondere wenn Sie Ressourcen geändert oder entfernt haben, die im Simulator zwischengespeichert werden können. Wenn Sie einen Neustart wünschen, können Sie den Simulator auf die virtuellen "Werkseinstellungen" zurücksetzen, indem Sie im Menü *Programme* zum Menüpunkt *iOS Simulator* > *Inhalt und Einstellungen zurücksetzen...* navigieren. Beachten Sie, dass dadurch alle App-Daten gelöscht und die UDID-Nummer der App zurückgesetzt wird.

## Verwandte Themen

- [Prüfung auf Geräten](/guides/rhinomobile/testing-on-devices/)

+++
aliases = ["/en/5/guides/rhinomobile/testing-on-devices/", "/en/6/guides/rhinomobile/testing-on-devices/", "/en/7/guides/rhinomobile/testing-on-devices/", "/en/wip/guides/rhinomobile/testing-on-devices/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "Dieser Leitfaden führt Sie durch die Einrichtung von Geräten zum Testen mobiler Anwendungen."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Prüfung auf Geräten"
type = "guides"
weight = 7

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/devices_and_testing"
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
 
## Android-Geräte

Um Ihren Code auf einem Android-Gerät zu debuggen, müssen Sie das USB-Debugging auf dem Gerät aktivieren. Dieser Modus macht Ihr Gerät etwas anfälliger für Beschädigungen - durch Sie selbst und durch andere - und sollte daher mit Vorsicht verwendet werden. Sie können sie zwischen den Entwicklungssitzungen aktivieren und deaktivieren, wenn Sie möchten.

#### Geräte mit Android 4.0 (JellyBean - API 14) oder neuer

Aktivieren Sie die Option *USB-Debugging* unter *Einstellungen* > *Entwickleroptionen*.

Bei Android 4.2 und neuer sind die *Entwickleroptionen standardmäßig ausgeblendet*; gehen Sie wie folgt vor:

1. Gehen Sie auf dem Gerät zu *Einstellungen* > *Informationen* <Gerät>.
1. Tippen Sie sieben Mal auf die *Build-Nummer*, um die *Einstellungen* > *Entwickler*-Optionen verfügbar zu machen.
1. Aktivieren Sie dann die Option *USB-Debugging* .

Unter Windows ist es manchmal erforderlich, das Gerät in den Kameramodus (PTP) und nicht in den Mediengerätemodus (MTP) zu schalten. Um diesen Modus zu ändern, gehen Sie wie folgt vor:

1. Gehen Sie auf dem Gerät zu *Einstellungen* > *Speicher* > *Weitere Optionen (...)* > *USB-Computeranschluss*
1. Wechseln Sie von *Mediengerät (MTP)* zu *Kamera (PTP)*.

#### Kindle-Fire-Geräte

Wählen Sie auf dem Gerät *Einstellungen* > *Sicherheit* und setzen Sie ADB aktivieren auf Ein.

Weitere Informationen finden Sie in der [Amazon-Entwicklerdokumentation](https://developer.amazon.com/sdk/fire/connect-adb.html#Connecting).

Sie können auch die Option "Wach bleiben" aktivieren, um zu verhindern, dass Ihr Android-Gerät schläft, während es an den USB-Anschluss angeschlossen ist.

## iOS-Geräte

iOS-Geräte müssen bei Apple registriert werden, bevor Sie sie für die Entwicklung oder für Tests verwenden können. Dieser Prozess ist auch als *Provisionierung* bekannt. Befolgen Sie diese Anweisungen von Xamarin, um Ihr iOS-Gerät einsatzbereit zu machen.

Sobald Sie Ihr Gerät provisioniert und über USB angeschlossen haben, können Sie Ihre Anwendung in Xamarin Studio oder Visual Studio (über den Mac Build-Host) ausführen und debuggen.

Geräte sind der beste Ort, um Ihre Anwendung zu testen. Die vier Bereiche, in denen sich die Geräte am meisten vom Simulator unterscheiden, sind:

1. Netzwerke und Konnektivität
1. Standortbezogene Dienste
1. *Speicher*
1. *OpenGL ES*

Die letzten beiden sind für RhinoMobile-Anwendungen am wichtigsten. Große Polygonnetze in .3dm-Dateien können viel Speicher verbrauchen; der Simulator wird versuchen, OutOfMemory-Warnungen auszulösen, aber das ist nicht so konsistent (oder realistisch) wie das Ausführen und Debuggen auf dem Gerät. Schließlich werden OpenGL ES-Aufrufe auf dem Simulator anders interpretiert als auf dem Gerät... es ist möglich, dass Code, der auf dem Simulator funktioniert, nicht auf allen Geräten funktioniert.

## Verwandte Themen

- [Verwendung von Simulatoren](/guides/rhinomobile/using-simulators/)

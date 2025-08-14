+++
title = "Asynchrone Ausführung"
description = "Bietet Informationen zur Ausführung von Skripten im asynchronen Modus, um zu vermeiden, dass die Rhino-Benutzeroberfläche durch lange laufende Aufgaben blockiert wird"
authors = ["ehsan"]

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

<style>
    .main-content img { zoom: 50%; }
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
    }
</style>

## Was bedeutet asynchron?

Normalerweise laufen die meisten Operationen in einer Anwendung mit einer grafischen Benutzeroberfläche (GUI) auf dem *UI Thread*. Dies ist der Thread, der die Benutzeroberfläche startet und auf Betätigungen wie das Klicken von Schaltflächen und das Bewegen der Maus reagiert. Wenn Sie auf eine Schaltfläche klicken, wird der Code hinter dieser Schaltfläche im UI-Thread ausgeführt.

**Asynchrone (kurz Async) Operationen laufen auf Nicht-UI-Threads und frieren die Benutzeroberfläche nicht ein.**

Wenn die Aufgabe zeitaufwändig ist, kann der UI-Thread (der die Aufgabe jetzt nach dem Klicken auf die Schaltfläche ausführt) nicht auf andere Ereignisse reagieren. Somit ist die Benutzeroberfläche *"Eingefroren"* und nicht reaktionsfähig. Normalerweise ist dies in Ordnung, da Sie nicht möchten, dass der Benutzer das Dokument ändert, während die Aufgabe ausgeführt wird. Es ist eine gute Idee, Nicht-UI-Threads für zeitaufwändige Aufgaben zu verwenden und sie *Asynchron* auszuführen.

## Async im Skript-Editor
Wenn ein Skript im Rhino-Skript-Editor eine zeitaufwändige Aufgabe ausführt, würde das Klicken auf die Schaltfläche *Ausführen* die Rhino-Benutzeroberfläche für die Dauer des Skripts einfrieren lassen. Wie wir bereits erwähnt haben, ist das in Ordnung. Wenn Ihre Aufgabe jedoch nicht mit dem Rhino-Dokument zu tun hat (könnte vom Rhino-Benutzer geändert werden, während Ihr Skript läuft), könnte sie Async gemacht werden. Dies würde Rhino UI während der Ausführung Ihres Skripts reaktionsfähig machen. Es ist auch eine gute Angewohnheit, den Fortschritt anzuzeigen, während die Aufgabe im Hintergrund läuft:

- In C# fügen Sie am Anfang Ihres Skripts `// async:true` hinzu. 
- In Python setzen Sie `# async:true` an den Anfang Ihres Skripts.

Wenn das Skript als `async: true` markiert ist, führt der Skript-Editor das gesamte Skript in einem Nicht-UI-Thread aus. Dies ist eine Funktion von Rhino Script Editor und nicht der Skriptsprache. Sie können diese Zeile entfernen oder sie auf `false` setzen, um das Skript wieder synchron zu machen.

## Asynchrones C#

Das folgende Beispiel-C#-Skript friert die Rhino-Benutzeroberfläche für etwa 2 Sekunden vollständig ein. Das ist die Zeitspanne, die wir in `Thread.Sleep` angeben, um Arbeit zu simulieren. Das kann eine lange laufende Berechnung sein oder das Warten auf den Empfang von Daten aus dem Internet:

```csharp
// #! csharp
using System;
using System.Threading;

using Rhino;

RhinoApp.WriteLine("Start Task");
Thread.Sleep(2000); // simulate work
RhinoApp.WriteLine("End Task");
```

Durch Hinzufügen der Zeile `// async:true` können wir dieses komplette Skript dazu zwingen, auf einem Nicht-UI-Thread zu laufen, so dass Rhino UI aktiv bleibt und wir weiterarbeiten können, während das Skript läuft:

```csharp
// #! csharp
// async:true
using System;
using System.Threading;

using Rhino;

RhinoApp.WriteLine("Start Task");
Thread.Sleep(2000); // simulate work
RhinoApp.WriteLine("End Task");
```

Beachten Sie, dass dies die einzige Änderung ist, die wir am Skript vorgenommen haben. Beachten Sie auch, dass die Schaltfläche *Ausführen* im Dashboard des Skripteditors jetzt einen roten Pfeil anzeigt, um die asynchrone Ausführung dieses Skripts darzustellen:

![](editor-csharp-async.png)

## Asynchrones Python

Das folgende Python-Beispielskript friert die Rhino-Benutzeroberfläche für etwa 2 Sekunden vollständig ein. Das ist die Zeitspanne, die wir in `time.sleep` angeben, um die Arbeit zu simulieren. Das kann eine lange laufende Berechnung sein oder das Warten auf den Empfang von Daten aus dem Internet:

```python
#! python3
import threading
import time

class Job(threading.Thread):
    def __init__(self, id, name, wait):
        super().__init__()
        self.id = id
        self.name = name
        self.wait = wait

    def run(self):
        print("Starting " + self.name)
        time.sleep(self.wait) # wait to simulate work
        print(f"Done {self.name}: {time.ctime(time.time())}")


job1 = Job(1, "Job-1", 2)
job1.start()
job1.join()

print("Complete")
```

Durch Hinzufügen der Zeile `# async:true` können wir dieses komplette Skript dazu zwingen, auf einem Nicht-UI-Thread zu laufen, so dass die Rhino-Benutzeroberfläche aktiv bleibt und wir weiterarbeiten können, während das Skript läuft (dies ist eine Funktion des Rhino-Skripteditors und nicht der Python-Sprache):

```python
#! python3
# async: true
import threading
import time

class Job(threading.Thread):
    def __init__(self, id, name, wait):
        super().__init__()
        self.id = id
        self.name = name
        self.wait = wait

    def run(self):
        print("Starting " + self.name)
        time.sleep(self.wait) # wait to simulate work
        print(f"Done {self.name}: {time.ctime(time.time())}")


job1 = Job(1, "Job-1", 2)
job1.start()
job1.join()

print("Complete")
```

Beachten Sie, dass dies die einzige Änderung ist, die wir am Skript vorgenommen haben. Beachten Sie auch, dass die Schaltfläche *Ausführen* im Dashboard des Skripteditors jetzt einen roten Pfeil anzeigt, um die asynchrone Ausführung dieses Skripts darzustellen:

![](editor-python-async.png)


## Fortschritt anzeigen

Es ist eine gute Praxis, Rückmeldungen über den Fortschritt von Hintergrundaufgaben zu geben. Rhino UI hat eine Fortschrittsanzeige in der Statusleiste. Dies ist ein Beispiel dafür, wie Sie diesen Fortschrittsbalken in Ihren Skripten verwenden können. Im Folgenden wird `Thread.Sleep` verwendet, um die Arbeit zu simulieren:

```csharp
// #! csharp
using System;
using System.Threading;

using Rhino;
using Rhino.UI;
using Eto.Forms;

// setup the progress indicator with expected range, and a message
StatusBar.ShowProgressMeter(0, 5, "Progress", embedLabel: true, showPercentComplete: false);
RhinoApp.WriteLine("Start Task");
for (int i = 0; i < 5; i++)
{
    Thread.Sleep(1000); // simulate work

    // update progress
    StatusBar.UpdateProgressMeter("Progress", i, true);
    // since we are on the main thread here,
    // call this method to force Rhino UI to update
    Application.Instance.RunIteration();
}

// do not forget to hide the progress when done
StatusBar.HideProgressMeter();
RhinoApp.WriteLine("End Task");
```

![](editor-csharp-progress-sync.png)

### Python-Fortschritt

In Python können Sie das Modul `rhinoscriptsyntax` verwenden, um den Zugriff auf die Fortschrittsanzeige zu erleichtern:

```python
import rhinoscriptsyntax as rs
from Rhino import RhinoApp

MAX = 1000
rs.StatusBarProgressMeterShow("Progress", 0, MAX)

for i in range(0, MAX):
    rs.StatusBarProgressMeterUpdate(i)

rs.StatusBarProgressMeterHide()
```

## Async in Grasshopper

{{< call-out "note" "Hinweis" >}}
Das Muster `async: true` wird in Grasshopper NICHT UNTERSTÜTZT, da es warten muss, bis das Skript vollständig ausgeführt ist und die Ausgabedaten gesetzt sind, bevor der Rest des Komponentendiagramms ausgeführt wird. Wir können jedoch Hintergrund-Threads haben, die Berechnungen durchführen und kontinuierlich eine Grasshopper-Lösung auslösen, um die Ergebnisse zu aktualisieren.
{{< /call-out >}}

Dies ist ein Beispiel für eine Python-Skriptkomponente, die Berechnungen im Hintergrund durchführt. Wir verwenden die *Trigger* Komponente in Grasshopper, um diese Komponente in Intervallen neu zu berechnen und somit die Geometrievorschau in Rhino zu aktualisieren:

- `RunScript` richtet beim ersten Durchlauf den Arbeitsfaden ein. Bei späteren Durchläufen wird nichts unternommen, außer der Ausgabe von `"Training in Progress"` und dem aktuellen Zustand des Berechnungsnetzes
- `main_solve` ist die Solver-Funktion, die von dem Worker-Thread ausgeführt wird.. Sie aktualisiert die Klassenvariable `MyComponent.CURRENT_MESH` während der Ausführung
- `DrawViewportMeshes` wird von Grasshopper nach jedem Trigger aufgerufen und zeigt den aktuellen Zustand des berechneten Netzes in `MyComponent.CURRENT_MESH` an

```python
import System
import System.Drawing as SD
import Rhino
import Rhino.Geometry as G
import Grasshopper
import Grasshopper.Kernel as GHK
import threading
import time


def main_solve():
    for r in range(10, 20):
        # wait represents compute work
        Rhino.RhinoApp.WriteLine("computing mesh")
        time.sleep(1)

        sphere = G.Sphere(G.Point3d.Origin, r)
        MyComponent.CURRENT_MESH = G.Mesh.CreateFromSphere(sphere, 10, 10)
        Rhino.RhinoApp.WriteLine("computed mesh")

    Rhino.RhinoApp.WriteLine("computed completed")


class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    SOVLE_STARTED = False
    CURRENT_MESH = None

    def RunScript(self):
        if MyComponent.SOVLE_STARTED:
            return ("Training in Progress", MyComponent.CURRENT_MESH)
        
        MyComponent.SOVLE_STARTED = True
        threading.Thread(target=main_solve).start()
        return ("Training in Progress", None)
        
    @property
    def ClippingBox(self):
        return G.BoundingBox(-30, -30, -30, 30, 30, 30)

    def DrawViewportMeshes(self, args: GHK.IGH_PreviewArgs):
        if d := getattr(args, "Display", None):
            if MyComponent.CURRENT_MESH:
                d.DrawMeshWires(MyComponent.CURRENT_MESH, SD.Color.Blue, 2)
```

Beachten Sie, dass Rhino UI während dieser Hintergrundberechnung aktiv bleibt:

{{< vimeo id="999893058" autoplay="1" loop="1" autopause="0" >}}

## Erweiterte Async

Manchmal ist es notwendig, Operationen auf dem UI-Thread auszuführen, bevor oder nachdem eine zeitaufwändige Operation abgeschlossen wurde. Denken Sie daran, dass der oben erwähnte `async:true`-Mechanismus der Bequemlichkeit dient und das gesamte Skript auf einem Nicht-UI-Thread ausführt. Je nach Skriptsprache können Sie die Threading- oder Async-Funktionen der Sprache nutzen, um kompliziertere Sync/Async-Operationen durchzuführen.

Dies ist ein Beispiel für ein C#-Skript, das auf einem UI-Thread in den Teilen **A** und **C** des Skripts (blockierend) läuft und eine zeitaufwändige Operation in Teil **B**hat. Rhino UI wird während der blockierenden Teile eingefroren, ist aber ansonsten voll verfügbar. Beachten Sie Folgendes:

- Das Skript gibt `// async: true` an. **Dies bedeutet, dass das gesamte Skript auf einem Nicht-UI-Thread läuft.**

- Um sicherzustellen, dass **Teil A und C auf dem UI-Thread laufen** und Änderungen in Rhino vornehmen können, verwenden wir `Application.Instance.Invoke`. Diese Methode wird von Eto bereitgestellt, dem UI-Framework, das Rhino >=8 verwendet, und stellt sicher, dass die angegebene Aktion auf dem UI-Thread läuft.

- In Teil B ruft das Skript `.GetAwaiter().GetResult()` für das Objekt `Task<int>` auf, das durch den Aufruf `Task.Run` erstellt wurde. Damit soll sichergestellt werden, dass **die Ausführung auf den Abschluss der Aufgabe wartet** und wir das Ergebnis haben, bevor wir mit Teil C fortfahren. Beachten Sie auch, dass der Aufruf von `Application.Instance.RunIteration` hier nicht notwendig ist und einen Absturz verursacht, wenn er aufgerufen wird.

```csharp
// #! csharp
// async: true
using System;
using System.Threading;
using System.Threading.Tasks;

using Rhino;
using Rhino.UI;
using Eto.Forms;

// Part A: runs on UI thread (blocking)
Application.Instance.Invoke(() => {
    // KANN HIER ÄNDERUNGEN AN RHINO oder DOKUMENT VORNEHMEN
    StatusBar.ShowProgressMeter(0, 5, "Progress", true, false);
});

// Part B: runs on Non-UI thread
int result = Task.Run(() => {
    for (int i = 0; i < 5; i++)
    {
        Thread.Sleep(1 * 1000);
        StatusBar.UpdateProgressMeter("Progress", i, true);
        // DO NOT CALL THIS SINCE WE ARE NOT ON UI THREAD
        // Application.Instance.RunIteration();
    }

    return 42;
}).GetAwaiter().GetResult();

// Part C: runs on UI thread (blocking)
Application.Instance.Invoke(() => {
    // KANN HIER ÄNDERUNGEN AN RHINO oder DOKUMENT VORNEHMEN
    RhinoApp.WriteLine($"Result: {result}");
    StatusBar.HideProgressMeter();
});
```

Sie können dieses Skript auch debuggen, indem Sie Haltepunkte innerhalb des Geltungsbereichs der einzelnen Teile setzen. Beachten Sie, dass der erste und der letzte Haltepunkt auf `Thread 1` (Haupt- und UI-Thread in Rhino) angehalten werden, aber der Haltepunkt in Zeile 19 wird auf `Thread 15` angehalten, der zufällig der Thread ist, der zur Ausführung der Aufgabe durch die Dotnet-Laufzeit verwendet wird:

![](editor-csharp-mixed-debug.png)


Hier ist ein ähnliches Beispiel in Python. Beachten Sie, dass wir `rhinoscriptsyntax` verwenden, um die Fortschrittsanzeige zu behandeln. Die Funktionen `part_a` und `part_c` werden auf dem Haupt-Thread der Benutzeroberfläche ausgeführt, und der mittlere Teil wird auf dem im Skript erstellten neuen Thread ausgeführt:

```python
#! python3
# async: true
import threading
import time
import rhinoscriptsyntax as rs

from Rhino import RhinoApp
from Eto.Forms import Application


class Job(threading.Thread):
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
        self.result = 0

    def run(self):
        thread_id = threading.current_thread().ident
        print(f"Starting {self.name} on Thread: {thread_id}")
        for i in range(5):
            time.sleep(1) # wait to simulate work
            rs.StatusBarProgressMeterUpdate(i)
        self.result = 42
        print(f"Done {self.name}: {time.ctime(time.time())}")


def part_a():
    # CAN MAKE CHANGES TO RHINO or DOCUMENT HERE
    thread_id = threading.current_thread().ident
    print(f"Thread: {thread_id}")
    rs.StatusBarProgressMeterShow("Progress", 0, 5)

def part_c(result):
    # CAN MAKE CHANGES TO RHINO or DOCUMENT HERE
    thread_id = threading.current_thread().ident
    print(f"Thread: {thread_id}")
    print(f"Result: {result}")
    rs.StatusBarProgressMeterHide()


RhinoApp.ClearCommandHistoryWindow()
Application.Instance.Invoke(part_a)

job1 = Job(1, "Job-1")
job1.start()
job1.join()

result = job1.result

Application.Instance.Invoke(lambda: part_c(result))

print("Complete")
```

Beachten Sie, dass die Thread-ID für `part_a` und `part_c` übereinstimmt, aber der mittlere Abschnitt von einem Thread mit einer anderen ID ausgeführt wird. Beachten Sie auch, dass sich die Thread-Identifikatoren bei der Verwendung von C# von den Dotnet-Thread-IDs unterscheiden:

![](editor-python-mixed-threadids.png)


### C# Async/Await

In C# (Rhino >= 8.12) können Sie [async/await](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/) für asynchrone Programmierung verwenden. Hier ist ein Beispiel für die Erstellung einer asynchronen Funktion im Skript-Editor:

```csharp
// #! csharp
// async: true
using System;
using System.Threading;
using System.Threading.Tasks;

async Task<int> Berechnen()
{
    await Task.Delay(TimeSpan.FromMilliseconds(2000));
    return 42;
}

int result = await Compute();

Console.WriteLine($"Result: {result}");
```

Wenn wir die Zeile `// async: true` entfernen oder sie auf `false` setzen, zeigt der Editor einen Fehler beim Aufruf von `await` im globalen Bereich an:

![](editor-csharp-await-error.png)

Bei der Ausführung von C#-Skripten setzt der Editor das Skript in etwas um, das wie das folgende Beispiel aussieht. Auf diese Weise können mehrere Instanzen desselben Skripts erstellt werden, die ihre eigenen internen Zustände beibehalten und in unterschiedlichen Kontexten ausgeführt werden. Beachten Sie, dass die Hauptmethode `__RunScript__` NICHT als *async*markiert ist:

```csharp
sealed class __RhinoCodeScript__ {
public void __RunScript__(Rhino.Runtime.Code.Execution.RunContext __context__)
{
        // YOUR SCRIPT IS EMBEDDED HERE
}}
```

Wenn wir `await` im globalen Bereich verwenden, müssen wir das Skript als `// async: true` kennzeichnen, um sicherzustellen, dass `__RunScript__` als `async` gekennzeichnet ist und eine `Task`-Instanz zurückgibt, damit der Editor die Ausführung abwarten kann:

```csharp
sealed class __RhinoCodeScript__ {
public async Task __RunScript__(Rhino.Runtime.Code.Execution.RunContext __context__)
{
        async Task<int> Berechnen()
        {
            await Task.Delay(TimeSpan.FromMilliseconds(2000));
            return 42;
        }

        int result = await Compute();

        Console.WriteLine($"Result: {result}");
}}
```
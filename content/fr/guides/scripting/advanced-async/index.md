+++
title = "Exécution asynchrone"
description = "Ce guide porte sur l’exécution de scripts en mode asynchrone permettant d’éviter de bloquer l’interface utilisateur de Rhino avec des tâches de longue durée"
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

## Que signifie « asynchrone » ?

Normalement, la plupart des opérations d’une application dotée d’une interface utilisateur graphique (GUI) s’exécutent sur le *thread de l’UI*. C’est le thread qui démarre l’interface utilisateur et écoute les événements tels que les clics sur les boutons et les déplacements de la souris. Lorsque vous cliquez sur un bouton, le code qui se trouve derrière ce bouton s’exécute sur le thread de l’UI.

**Les opérations asynchrones (que l’on appelle parfois tout simplement « Async ») s’exécutent sur des threads non liés à l’interface utilisateur, évitant ainsi que l’interface utilisateur ne se bloque.**

Si une tâche prend du temps, le thread de l’UI (qui est en train d’exécuter la tâche parce que l’utilisateur a cliqué sur un bouton) ne peut pas répondre à d’autres événements. L’interface utilisateur est donc *figée* et ne répond pas. En temps normal, cela ne pose pas de problème car vous ne voulez pas que l’utilisateur modifie le document pendant que la tâche est en cours d’exécution. C’est une bonne idée d’utiliser des threads non-UI pour les tâches qui prennent du temps et de les exécuter de manière *asynchrone*.

## Async dans l’éditeur de scripts
Dans l’éditeur de scripts de Rhino, si un script exécute une tâche longue, le fait de cliquer sur le bouton *Exécuter* va figer l’interface utilisateur de Rhino pendant la durée du script. Comme nous l’avons indiqué, cela ne pose pas de problème. Cependant, si votre tâche ne concerne pas le document de Rhino (et que celui-ci pourrait être modifié par l’utilisateur pendant que votre script est en cours d’exécution), elle peut être rendue asynchrone. Ainsi, l’interface utilisateur de Rhino sera réactive pendant l’exécution du script. C’est également une bonne habitude d’indiquer la progression lorsque la tâche s’exécute en arrière-plan :

- En C#, ajoutez `// async:true` au début de votre script. 
- En Python, ajoutez `# async:true` au début de votre script.

Lorsque le script est marqué comme `async:true`, l’éditeur de scripts exécute le script complet sur un thread non-UI. Il s’agit d’une fonctionnalité de l’éditeur de scripts de Rhino et non pas du langage de script. Vous pouvez supprimer cette ligne ou changer `true` par `false` pour rendre le script à nouveau synchrone.

## C# asynchrone

L’exemple de script C# ci-dessous fige complètement l’interface utilisateur de Rhino pendant environ 2 secondes. C’est la durée que nous spécifions dans `Thread.Sleep` pour simuler le travail. Il peut s’agir d’un calcul long ou de l’attente de données provenant d’Internet :

```csharp
// #! csharp
using System;
using System.Threading;

using Rhino;

RhinoApp.WriteLine("Start Task");
Thread.Sleep(2000); // Simulation du travail.
RhinoApp.WriteLine("End Task");
```

En ajoutant la ligne `// async:true`, nous pouvons forcer tout ce script à s’exécuter sur un thread Non-UI, en gardant l’interface utilisateur de Rhino active afin de pouvoir continuer à travailler pendant que le script s’exécute :

```csharp
// #! csharp
// async:true
using System;
using System.Threading;

using Rhino;

RhinoApp.WriteLine("Start Task");
Thread.Sleep(2000); // Simulation du travail.
RhinoApp.WriteLine("End Task");
```

Remarquez que c’est la seule modification que nous ayons apportée au script. Notez également que le bouton *Exécuter* dans le tableau de bord de l’éditeur de scripts est à présent accompagné d’une flèche rouge qui symbolise l’exécution asynchrone de ce script :

![](editor-csharp-async.png)

## Python asynchrone

L’exemple de script Python ci-dessous fige complètement l’interface utilisateur de Rhino pendant environ 2 secondes. C’est la durée que nous spécifions dans `time.sleep` pour simuler le travail. Il peut s’agir d’un calcul long ou de l’attente de données provenant d’Internet :

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
        time.sleep(self.wait) # Attente pour simuler le travail.
        print(f"Done {self.name}: {time.ctime(time.time())}")


job1 = Job(1, "Job-1", 2)
job1.start()
job1.join()

print("Complete")
```

En ajoutant la ligne `# async:true`, nous pouvons forcer tout ce script à s’exécuter sur un thread Non-UI, en gardant l’interface utilisateur de Rhino active afin de pouvoir continuer à travailler pendant que le script s’exécute (c’est une fonctionnalité de l’éditeur de scripts de Rhino et non pas du langage Python) :

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
        time.sleep(self.wait) # Attente pour simuler le travail.
        print(f"Done {self.name}: {time.ctime(time.time())}")


job1 = Job(1, "Job-1", 2)
job1.start()
job1.join()

print("Complete")
```

Remarquez que c’est la seule modification que nous ayons apportée au script. Notez également que le bouton *Exécuter* dans le tableau de bord de l’éditeur de scripts est à présent accompagné d’une flèche rouge qui symbolise l’exécution asynchrone de ce script :

![](editor-python-async.png)


## Afficher la progression

Il est recommandé d’informer sur la progression des tâches en arrière-plan. L’interface utilisateur de Rhino dispose d’un indicateur de progression dans la barre d’état. Voici un exemple de la façon dont vous pouvez utiliser cette barre de progression dans vos scripts. `Thread.Sleep` est utilisé ci-dessous pour simuler le travail :

```csharp
// #! csharp
using System;
using System.Threading;

using Rhino;
using Rhino.UI;
using Eto.Forms;

// Configurez l’indicateur de progression avec une fourchette attendue et un message.
StatusBar.ShowProgressMeter(0, 5, "Progress", embedLabel: true, showPercentComplete: false);
RhinoApp.WriteLine("Start Task");
for (int i = 0; i < 5; i++)
{
    Thread.Sleep(1000); // Simulation du travail.

    // Mise à jour de la progression.
    StatusBar.UpdateProgressMeter("Progress", i, true);
    // Comme nous sommes sur le thread principal ici,
    // appelez cette méthode pour obliger l’UI de Rhino à s’actualiser.
    Application.Instance.RunIteration();
}

// N’oubliez pas de cacher la progression une fois le processus terminé.
StatusBar.HideProgressMeter();
RhinoApp.WriteLine("End Task");
```

![](editor-csharp-progress-sync.png)

### Progression avec Python

En Python, vous pouvez utiliser le module `rhinoscriptsyntax` pour accéder plus facilement à l’indicateur de progression :

```python
import rhinoscriptsyntax as rs
from Rhino import RhinoApp

MAX = 1000
rs.StatusBarProgressMeterShow("Progress", 0, MAX)

for i in range(0, MAX):
    rs.StatusBarProgressMeterUpdate(i)

rs.StatusBarProgressMeterHide()
```

## Async dans Grasshopper

{{< call-out "note" "Remarque" >}}
Le schéma `async:true` n’est PAS PRIS EN CHARGE par Grasshopper, car il doit attendre que le script s’exécute complètement et produise les données de sortie avant d’exécuter le reste des graphiques des composants. Vous pouvez toutefois avoir des threads en arrière-plan qui exécutent des calculs et déclenchent en permanence une opération de résolution de Grasshopper pour actualiser les résultats.
{{< /call-out >}}

Voici un exemple de composant de script Python qui exécute des calculs sur un thread en arrière-plan. Nous utilisons le composant *Trigger* de Grasshopper pour recalculer ce composant à intervalles réguliers et ainsi actualiser les prévisualisations de la géométrie dans Rhino :

- `RunScript` met en place le thread de travail à la première exécution. Il ne fait rien lors des exécutions ultérieures, si ce n’est générer `"Training in Progress"` et l’état actuel du maillage calculé.
- `main_solve` est la fonction du solveur qui est exécutée par le thread de travail. Il actualise la variable de classe `MyComponent.CURRENT_MESH` pendant l’exécution.
- `DrawViewportMeshes` est appelé par Grasshopper après chaque déclenchement et affiche l’état actuel du maillage calculé dans `MyComponent.CURRENT_MESH`.

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
        # L’attente représente le travail de calcul.
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

Remarquez que l’interface utilisateur de Rhino reste active pendant ce calcul en arrière-plan :

{{< vimeo id="999893058" autoplay="1" loop="1" autopause="0" >}}

## Exécution asynchrone avancée

Il est parfois nécessaire d’exécuter des opérations sur le thread de l’UI avant ou après une opération longue. Rappelez-vous que le mécanisme `async:true` que nous avons mentionné précédemment est utilisé pour des raisons de commodité et qu’il exécute le script complet sur un thread non-UI. En fonction du langage de script, vous pouvez utiliser les fonctions de threading ou d’asynchronisme du langage pour effectuer des opérations synchrones/asynchrones plus complexes.

Vous trouverez ci-dessous un exemple de script C# qui s’exécute sur le thread de l’UI sur les parties **A** et **C** du script (blocage), et qui comporte une opération longue sur la partie **B**. L’interface utilisateur de Rhino est figée pendant les parties de blocage, mais est entièrement disponible par ailleurs. Remarquez que :

- Le script spécifie `// async:true`. **Cela signifie que tout le script s’exécute sur un thread non-UI.**

- Pour s’assurer que **les parties A et C s’exécutent sur le thread de l’UI** et peuvent apporter des modifications à Rhino, nous utilisons `Application.Instance.Invoke`. Cette méthode est fournie par Eto, qui est le cadre d’interface utilisateur que Rhino >=8 utilise, et garantit que l’action concernée s’exécute sur le thread de l’interface utilisateur.

- Dans la partie B, le script appelle `.GetAwaiter().GetResult()` sur l’objet `Task<int>` créé par l’appel `Task.Run`. Cela permet de s’assurer que **l’exécution attend que la tâche se termine** et que nous obtenons le résultat avant de passer à la partie C. Notez également qu’il n’est pas nécessaire d’appeler `Application.Instance.RunIteration` ici et qu’il provoquerait une erreur s’il était appelé.

```csharp
// #! csharp
// async: true
using System;
using System.Threading;
using System.Threading.Tasks;

using Rhino;
using Rhino.UI;
using Eto.Forms;

// La partie A s’exécute sur le thread de l’interface utilisateur (blocage)
Application.Instance.Invoke(() => {
    // POSSIBILITÉ DE MODIFIER RHINO ou LE DOCUMENT ICI
    StatusBar.ShowProgressMeter(0, 5, "Progress", true, false);
});

// La partie B s’exécute sur un thread non-UI
int result = Task.Run(() => {
    for (int i = 0; i < 5; i++)
    {
        Thread.Sleep(1 * 1000);
        StatusBar.UpdateProgressMeter("Progress", i, true);
        // ÉTANT DONNÉ QUE NOUS NE SOMMES PAS DANS LE THREAD DE L’INTERFACE UTILISATEUR, NE PAS APPELER
        // Application.Instance.RunIteration();
    }

    return 42;
}).GetAwaiter().GetResult();

// La partie C s’exécute sur le thread de l’interface utilisateur (blocage)
Application.Instance.Invoke(() => {
    // POSSIBILITÉ DE MODIFIER RHINO ou LE DOCUMENT ICI
    RhinoApp.WriteLine($"Result: {result}");
    StatusBar.HideProgressMeter();
});
```

Vous pouvez également déboguer ce script en plaçant des points de rupture dans la portée de chaque partie. Remarquez que le premier et le dernier point de rupture sont mis en pause sur `Thread 1` (thread principal et thread de l’UI dans Rhino), mais que le point de rupture de la ligne 19 est mis en pause sur `Thread 15` qui se trouve être le thread utilisé pour exécuter la tâche par le runtime .Net :

![](editor-csharp-mixed-debug.png)


Voici un exemple similaire en Python. Notez que nous utilisons `rhinoscriptsyntax` pour gérer l’indicateur de progression. Les fonctions `part_a` et `part_c` sont exécutées sur le thread principal de l’UI et la partie centrale est exécutée sur le nouveau thread créé dans le script :

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
            time.sleep(1) # Attente pour simuler le travail
            rs.StatusBarProgressMeterUpdate(i)
        self.result = 42
        print(f"Done {self.name}: {time.ctime(time.time())}")


def part_a():
    # POSSIBILITÉ DE MODIFIER RHINO ou LE DOCUMENT ICI
    thread_id = threading.current_thread().ident
    print(f"Thread: {thread_id}")
    rs.StatusBarProgressMeterShow("Progress", 0, 5)

def part_c(result):
    # POSSIBILITÉ DE MODIFIER RHINO ou LE DOCUMENT ICI
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

Remarquez que l’identifiant du thread correspond pour `part_a` et `part_c`, mais que la section du milieu est exécutée sur un thread avec un identifiant différent. Notez également que les identifiants de threads sont différents des identifiants de threads .Net lorsque vous utilisez C# :

![](editor-python-mixed-threadids.png)


### Async/Await en C#

En C# (Rhino >= 8.12), vous pouvez utiliser [async/await](https://learn.microsoft.com/fr-fr/dotnet/csharp/asynchronous-programming/) pour la programmation asynchrone. Voici par exemple comment créer une fonction asynchrone dans l’éditeur de scripts :

```csharp
// #! csharp
// async: true
using System;
using System.Threading;
using System.Threading.Tasks;

async Task<int> Compute()
{
    await Task.Delay(TimeSpan.FromMilliseconds(2000));
    return 42;
}

int result = await Compute();

Console.WriteLine($"Result: {result}");
```

Remarquez que si nous enlevons la ligne `// async: true` ou que nous changeons `true` par `false`, l’éditeur signale une erreur sur l'appel `await` dans la portée globale :

![](editor-csharp-await-error.png)

Lors de l’exécution de scripts C#, l’éditeur recompose le script de façon similaire à l’exemple ci-dessous. Cela permet de créer plusieurs instances du même script, qui conservent leurs propres états internes, et de les exécuter dans des contextes différents. Remarquez que la méthode principale `__RunScript__` n'est PAS marquée comme *async* :

```csharp
sealed class __RhinoCodeScript__ {
public void __RunScript__(Rhino.Runtime.Code.Execution.RunContext __context__)
{
        // VOTRE SCRIPT EST INTÉGRÉ ICI
}}
```

Si vous utilisez `await` dans la portée globale, vous devez marquer le script comme `// async: true` afin d’être sûr que `__RunScript__` est marqué comme `async` et renvoie une instance de `Task` pour que l’éditeur puisse attendre l’exécution :

```csharp
sealed class __RhinoCodeScript__ {
public async Task __RunScript__(Rhino.Runtime.Code.Execution.RunContext __context__)
{
        async Task<int> Compute()
        {
            await Task.Delay(TimeSpan.FromMilliseconds(2000));
            return 42;
        }

        int result = await Compute();

        Console.WriteLine($"Result: {result}");
}}
```
+++
title = "Grasshopper 2 Scripting: C#"
description = "Provides detailed information on C# scripting in Grasshopper 2"
authors = ["ehsan"]

[included_in]
platforms = [ "Windows", "Mac" ]
since = 9

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

<style>
    .main-content img { zoom: 50%; }

    /* instance member table reads as rows, no header needed */
    .main-content table { table-layout: fixed; width: 100%; }
    .main-content table thead { display: none; }
    .main-content table th:first-child,
    .main-content table td:first-child { width: 30%; }
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
        font-size: 14px;
    }
</style>

{{< call-out "note" "Note" >}}
This guide covers the C# script component in Grasshopper 2. For the Grasshopper 1 component, see [Grasshopper Scripting: C#](/guides/scripting/scripting-gh-csharp). For scripting in Rhino itself, see [Scripting: C#](/guides/scripting/scripting-csharp).
{{< /call-out >}}

## C# Component

The C# script component is in the **Maths** tab, **Script** panel. Drop one onto the canvas:

<!-- SCREENSHOT: C# Script component dropped on the GH2 canvas -->
![](gh2-csharp-component.png)

A new component starts with a small script that sets one output:

```csharp
// Grasshopper Script
using System;

A = "Hello C# Scripting!";

Console.WriteLine(A);
```

### Opening Script Editor

Double-click the component to open a script editor. The component draws a cone pointing to the editor associated with it:

<!-- SCREENSHOT: component with the editor open and the cone drawn between them -->
![](gh2-csharp-open.png)

### Component Options

Component options are in the component panel. The **Script** category has:

- **Open** opens the script in the editor
- **Export** saves the script to a file
- **Expire** clears cached compiler results and recomputes

<!-- SCREENSHOT: component panel open showing the Script category buttons -->
![](gh2-csharp-panel.png)

#### Threading

**Threading** sets how the iterations of your script are run:

- **One** runs iterations on a single thread, in order. This is the default
- **Many** runs iterations on different threads, which is faster for scripts that solve many iterations
- **UI** runs iterations on the application UI thread, in order

**One** is the default because scripts that run on many threads at once are harder to reason about. Iterations no longer run in order, and anything your script shares between them has to be written carefully.

**Debug Threading** sets the same choice for debug runs, and is also **One** by default. Stepping through a script while several iterations run at once is confusing, so debug runs stay single-threaded even when the script is set to **Many**:

<!-- SCREENSHOT: component panel showing Threading and Debug Threading option bars -->
![](gh2-csharp-threading.png)

## Inputs, Outputs

A new component has two inputs and one output, plus the **Console** output. Inputs may be left empty, so a script runs even when nothing is connected.

Add, remove, and rename parameters the same way as any other Grasshopper 2 component. Give them meaningful names, since the names are how your script reaches their values:

<!-- SCREENSHOT: component with renamed inputs and outputs -->
![](gh2-csharp-params.png)

### Pick Pears

Grasshopper 2 keeps metadata alongside every value, and the value together with its metadata is a *pear*. Turn on **Pick Pears** in the **Variable** category of an input's panel to receive `IPear` instances instead of naked values:

<!-- SCREENSHOT: input panel of a script parameter with the Pick Pears toggle enabled -->
![](gh2-csharp-pears.png)

This is off by default, and is only offered on inputs. Turn it on when your script needs the metadata of an item, not just its value.

### Standard Output (Console)

The **Console** output captures anything your script prints to the console. Each printed line becomes one item:

<!-- SCREENSHOT: Console output parameter holding printed text -->
![](gh2-csharp-console.png)

#### Toggling Output

Two toggles in the **Parameters** category of the component panel control it:

- **Console** shows or hides the output parameter
- **Break** splits the collected text into one item per line

Hiding the parameter when your script prints nothing saves the component from collecting and splitting output on every run.

### Parameter Converters

Right-click a parameter to choose how its data reaches your script. The list is grouped by kind:

- **System** types like boolean, integer, string, number, `Guid`, `DateTime`, color, and file path
- **Rhino** data types like `Point3d`, `Vector3d`, `Plane`, `Interval`, `Box`, `Transform`
- **Geometry** types like `Line`, `Circle`, `Arc`, `Polyline`, `Rectangle3d`
- **Geometry base** types like `Curve`, `Mesh`, `Surface`, `Brep`, `SubD`, `PointCloud`

<!-- SCREENSHOT: right-click menu on a script input showing the grouped converter list -->
![](gh2-csharp-converters.png)

**No Conversion** is the default, so values reach your script as Grasshopper stores them. Pick a converter and values are converted to that type first.

Converters replace the type hints of the Grasshopper 1 component.

### Parameter Access

Each parameter takes **Item**, **Twig**, or **Tree** access, which sets whether your script is handed one value, a list, or a whole tree:

<!-- SCREENSHOT: access menu open on a script input -->
![](gh2-csharp-access.png)

**Unwrap Data** on an output turns collections your script sets into Grasshopper trees and twigs.

## SDK-Mode

Choose **Convert To Grasshopper2ScriptInstance (Component SDK Mode)** on the editor dashboard to turn the script into a class. The component then calls `RunScript` for every iteration:

```csharp
using System;

using Rhino;
using Rhino.Geometry;

using Grasshopper2.Components;

public class Script_Instance : GH_ScriptInstance
{
  private void RunScript(double X, double Y, ref double A)
  {
    A = X + Y;

    Print($"Iteration {Iteration} of {Iterations}");
  }
}
```

The instance also gives access to what is running the script:

|  |  |
| --- | --- |
| `Component` | The component running the script |
| `Document` | The Grasshopper document holding the component |
| `RhinoDocument` | The active Rhino document |
| `Access` | Data access for the iteration being computed |
| `Solution` | The solution being computed |
| `Callstack` | The callstack leading up to the component |
| `CustomData` | Data shared by all iterations of the solution |
| `Iteration` | Index of the iteration being computed |
| `Iterations` | Number of iterations in the solution |

### RunScript Signature

Inputs are method parameters and outputs are `ref` parameters, so their names and types follow the component parameters. Use `Print` to write to the **Console** output.

Changing the component parameters changes the signature, so keep the method parameters in step with the component.

### Before, After Solve Overrides

Choose **Add Solve Overrides** to add methods that run once per solution, before and after all the iterations:

```csharp
public class Script_Instance : GH_ScriptInstance
{
  int _count;

  // runs once before the first iteration
  public override void BeforeRun()
  {
    _count = 0;
  }

  private void RunScript(double X, double Y, ref double A)
  {
    A = X + Y;
    System.Threading.Interlocked.Increment(ref _count);
  }

  // runs once after the last iteration
  public override void AfterRun()
  {
    Print($"Solved {_count} iterations");
  }
}
```

### Preview Overrides

Choose **Add Preview Overrides** to add `Draw`, the single override where a script draws into the Rhino viewports. Keep whatever you draw on the instance, since `Draw` runs separately from `RunScript`:

```csharp
public class Script_Instance : GH_ScriptInstance
{
  readonly List<Circle> _circles = new List<Circle>();

  public override void BeforeRun()
  {
    _circles.Clear();
  }

  private void RunScript(double X, double Y, ref double A)
  {
    var circle = new Circle(new Point3d(X, Y, 0.0), 1.0);

    // iterations can run in parallel and this field is shared
    lock (_circles)
    {
      _circles.Add(circle);
    }

    A = circle.Circumference;
  }

  public override void Draw(DisplayBag bag, CancellationToken token)
  {
    foreach (Circle circle in _circles)
    {
      bag.AddCurve(Pear<Circle>.Create(circle));
    }
  }
}
```

<!-- SCREENSHOT: circles drawn in the Rhino viewport from a script component preview -->
![](gh2-csharp-preview.png)

### Input Panel

A script instance can add its own items to the component panel. Override `AppendToInputPanel` and the edits land on the instance:

```csharp
public class Script_Instance : GH_ScriptInstance
{
  double _factor = 2.0;

  private void RunScript(double X, double Y, ref double A)
  {
    A = (X + Y) * _factor;
  }

  public override void AppendToInputPanel(InputPanel panel)
  {
    using (panel.BeginCategory("Options"))
    {
      panel.AddLabel($"Factor is {_factor}", italic: true);

      panel.AddText(_factor.ToString(), text =>
      {
        if (double.TryParse(text, out double factor))
        {
          _factor = factor;
        }
      }, "Multiplier applied to the sum.");
    }
  }
}
```

Edits apply on the next solve:

<!-- SCREENSHOT: component panel showing the Options category added by the script -->
![](gh2-csharp-inputpanel.png)

## Script-Mode

A script does not have to be a class. A plain list of statements works too. Inputs arrive as variables named after the input parameters, and outputs are set by assigning to variables named after the output parameters:

```csharp
using System;

// X and Y are inputs, A is an output
A = X + Y;

Console.WriteLine($"A is {A}");
```

## Debugging Scripts

Set a breakpoint and choose **Run > Debug** in the editor to step through your script. See [Debugging Your Scripts](/guides/scripting/editor-debug).

Debug runs are single-threaded by default, so iterations stop in order even when the script itself is set to run on **Many** threads.

<!-- SCREENSHOT: GH2 C# script paused on a breakpoint with the debugging panels open -->
![](gh2-csharp-debug.png)

## NuGet Packages

Scripts can use packages published on [NuGet](https://www.nuget.org). Use **Install Package** on the editor dashboard to search for one, and a reference is added to your script:

```csharp
#r "nuget: RestSharp, 110.2.0"
```

See [NuGet Packages](/guides/scripting/scripting-csharp/#nuget-packages).

## Assembly References

Scripts can also reference .NET assemblies directly, by name if the assembly is already loaded in Rhino, or by path:

```csharp
#r "System.Text.Json.dll"
#r "/path/to/my/assemblies/MySharedAssembly.dll"
```

See [Assembly References](/guides/scripting/scripting-csharp/#assembly-references).

## Template Scripts

The editor **Templates** panel lists starting points for C# scripts:

- **Script**
- **Script (With Nuget Package)**
- **Script Instance**
- **Script Instance (With Preview)**
- **Script Instance (With Input Panel)**

<!-- SCREENSHOT: Templates panel in the component editor listing the C# templates -->
![](gh2-csharp-templates.png)

## Shared State Between Iterations

One script instance is shared by every iteration, so fields you declare on it are shared too.

With the default **One** threading, iterations run one after another and plain fields are safe. With **Many**, several iterations run at the same time and touch the same fields. Two things stop being true:

- Iterations no longer run in order
- Reading and writing a field is no longer safe on its own

This script looks correct and is not:

```csharp
public class Script_Instance : GH_ScriptInstance
{
  int _count;
  readonly List<Circle> _circles = new List<Circle>();

  private void RunScript(double X, double Y, ref double A)
  {
    _count++;                                    // increments get lost
    _circles.Add(new Circle(Point3d.Origin, X)); // list can end up corrupt

    A = _count;
  }
}
```

`_count++` reads the field, adds one, and writes it back. Two threads can read the same value and write back the same result, so one increment disappears. `List<T>` is worse: two threads adding at once can leave the list in a broken state or throw.

### Atomic Operations

For counting, use the `Interlocked` methods. Each one reads and writes in one uninterruptible step, so no increment is lost:

```csharp
using System.Threading;

int _count;

private void RunScript(double X, double Y, ref double A)
{
  // instead of _count++
  Interlocked.Increment(ref _count);

  A = X + Y;
}
```

`Interlocked.Add` adds a whole number in the same way. Adding up decimal numbers needs a lock instead.

### Locking

For anything that takes more than one step, or for collections, guard the field with a lock. Every thread that reaches the `lock` waits its turn:

```csharp
readonly object _sync = new object();
double _total;

private void RunScript(double X, double Y, ref double A)
{
  lock (_sync)
  {
    _total = _total + X;
    A = _total;
  }
}
```

Keep the work inside a lock small. While one iteration holds the lock, the others wait, and a large locked block cancels out the speed you switched to **Many** for.

### Thread-Safe Collections

The collections in `System.Collections.Concurrent` handle the locking for you. A `ConcurrentBag<T>` takes items from any thread, so iterations can collect into it without a lock of your own:

```csharp
using System.Collections.Concurrent;

readonly ConcurrentBag<Circle> _circles = new ConcurrentBag<Circle>();

// empty the bag before the iterations fill it again
public override void BeforeRun()
{
  _circles.Clear();
}

private void RunScript(double X, double Y, ref double A)
{
  var circle = new Circle(new Point3d(X, Y, 0.0), 1.0);

  _circles.Add(circle);

  A = circle.Circumference;
}

public override void AfterRun()
{
  Print($"Collected {_circles.Count} circles");
}
```

A bag does not keep the order items were added in. When order matters, use a `ConcurrentDictionary` keyed by `Iteration`:

```csharp
readonly ConcurrentDictionary<int, Circle> _circles = new ConcurrentDictionary<int, Circle>();

private void RunScript(double X, double Y, ref double A)
{
  var circle = new Circle(new Point3d(X, Y, 0.0), 1.0);

  _circles[Iteration] = circle;

  A = circle.Circumference;
}
```

### Avoiding Shared State

The simplest fix is often to not share anything. Values you only need for one iteration belong in local variables, which every iteration gets its own copy of:

```csharp
private void RunScript(double X, double Y, ref double A)
{
  // local, so no other iteration can see it
  var circle = new Circle(new Point3d(X, Y, 0.0), 1.0);

  A = circle.Circumference;
}
```

`BeforeRun` and `AfterRun` run once per solution, not once per iteration, so setting up and summarizing there needs no lock. `Iteration` and `Iterations` are also safe to read, since each iteration sees its own values.

When a script is hard to make thread safe, set **Threading** to **One** and leave it there.

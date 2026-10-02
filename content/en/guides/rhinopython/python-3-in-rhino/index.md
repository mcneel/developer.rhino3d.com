+++
aliases = []
authors = [ "ehsan" ]
categories = [ "Overview" ]
description = "This guide is an overview of Python 3 in Rhino and Grasshopper, and what it means for existing Python 2 scripts."
keywords = [ "python", "python3", "ironpython", "overview" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Python 3 in Rhino"
type = "guides"
weight = 2
draft = false

[admin]
TODO = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"
+++

<style>
    .main-content img { zoom: 50%; }
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
        font-size: 14px;
    }
</style>

## Python 3 in Rhino

Rhino 8 and newer embed two Python runtimes side by side:

- **Python 3** is [CPython](https://www.python.org), and reaches .NET and RhinoCommon through [Python.NET](https://pythonnet.github.io)
- **Python 2** is [IronPython](https://ironpython.net), which runs on .NET itself

Python 3 is an addition, not a replacement. Your Python 2 scripts keep running on IronPython, and both runtimes are available in Rhino and in Grasshopper.

## Python Versions

Each Rhino release ships with its own version of Python 3. The chart shows that version, and how long [python.org](https://devguide.python.org/versions/) supports it:

<!-- dates from devguide.python.org/versions; x = 170 + (year - 2020) * 48.2 -->
<svg class="python-versions" viewBox="0 0 720 150" role="img" aria-label="Python versions in Rhino: Rhino 8 ships Python 3.9.10, Rhino 9 ships Python 3.13.13">
  <style>
    .python-versions { width: 100%; max-width: 720px; font-family: inherit; }
    .python-versions text { fill: #333; font-size: 12px; }
    .python-versions .grid { stroke: #ddd; stroke-width: 1; }
    .python-versions .year { fill: #777; font-size: 11px; text-anchor: middle; }
    .python-versions .rhino { font-weight: bold; font-size: 13px; }
    .python-versions .py { fill: #666; }
    .python-versions .bar text { fill: #fff; font-size: 11px; text-anchor: middle; }
    .python-versions .bugfix { fill: #3c8d40; }
    .python-versions .security { fill: #e0a526; }
    .python-versions .now line { stroke: #c62828; stroke-width: 1.5; stroke-dasharray: 4 3; }
    .python-versions .now text { fill: #c62828; font-size: 11px; font-weight: bold; }
  </style>
  <g class="grid">
    <line x1="170" y1="22" x2="170" y2="120"/><line x1="218.2" y1="22" x2="218.2" y2="120"/>
    <line x1="266.4" y1="22" x2="266.4" y2="120"/><line x1="314.6" y1="22" x2="314.6" y2="120"/>
    <line x1="362.8" y1="22" x2="362.8" y2="120"/><line x1="411" y1="22" x2="411" y2="120"/>
    <line x1="459.2" y1="22" x2="459.2" y2="120"/><line x1="507.4" y1="22" x2="507.4" y2="120"/>
    <line x1="555.6" y1="22" x2="555.6" y2="120"/><line x1="603.8" y1="22" x2="603.8" y2="120"/>
    <line x1="652" y1="22" x2="652" y2="120"/><line x1="700.2" y1="22" x2="700.2" y2="120"/>
  </g>
  <g>
    <text class="year" x="194.1" y="15">2020</text><text class="year" x="242.3" y="15">2021</text>
    <text class="year" x="290.5" y="15">2022</text><text class="year" x="338.7" y="15">2023</text>
    <text class="year" x="386.9" y="15">2024</text><text class="year" x="435.1" y="15">2025</text>
    <text class="year" x="483.3" y="15">2026</text><text class="year" x="531.5" y="15">2027</text>
    <text class="year" x="579.7" y="15">2028</text><text class="year" x="627.9" y="15">2029</text>
    <text class="year" x="676.1" y="15">2030</text>
  </g>
  <!-- Rhino 8: 3.9 released 2020-10-05, last bugfix 2022-05-17, end of life 2025-10-31 -->
  <text class="rhino" x="0" y="45">Rhino 8</text>
  <text class="py" x="0" y="61">Python 3.9.10</text>
  <g class="bar">
    <rect class="bugfix" x="206.7" y="34" width="77.6" height="26"/>
    <text x="245.5" y="51">bugfix</text>
    <rect class="security" x="284.3" y="34" width="166.6" height="26"/>
    <text x="367.6" y="51">security</text>
  </g>
  <!-- Rhino 9: 3.13 released 2024-10-07, last bugfix 2026-10-01, end of life 2029-10 -->
  <text class="rhino" x="0" y="91">Rhino 9</text>
  <text class="py" x="0" y="107">Python 3.13.13</text>
  <g class="bar">
    <rect class="bugfix" x="399.6" y="80" width="95.6" height="26"/>
    <text x="447.4" y="97">bugfix</text>
    <rect class="security" x="495.2" y="80" width="146.2" height="26"/>
    <text x="568.3" y="97">security</text>
  </g>
  <g class="bar">
    <rect class="bugfix" x="170" y="132" width="12" height="12"/>
    <rect class="security" x="370" y="132" width="12" height="12"/>
  </g>
  <text x="188" y="142">bugfix and security fixes</text>
  <text x="388" y="142">security fixes only</text>
  <g class="now" visibility="hidden">
    <line y1="22" y2="120"/>
    <text y="31"></text>
  </g>
</svg>
<script>
  // placed at view time so the marker never goes stale
  (function () {
    var now = new Date();
    var x = 170 + (now.getFullYear() + now.getMonth() / 12 - 2020) * 48.2;
    if (x < 170 || x > 700) return;
    var g = document.querySelector('.python-versions .now');
    var line = g.querySelector('line'), label = g.querySelector('text');
    line.setAttribute('x1', x); line.setAttribute('x2', x);
    label.setAttribute('x', x + 4);
    label.textContent = now.toLocaleString('en', { month: 'short', year: 'numeric' });
    g.setAttribute('visibility', 'visible');
  })();
</script>

Scripts of either runtime are written in a refreshed Script Editor, and it is the editor that puts the rest of this page within reach: installing packages, and a real debugger with breakpoints, variables, and a call stack. That debugger also works inside Grasshopper components, which the old editor could not do.

## What You Get With Python 3

Python 3 opens up the wider Python world:

- Packages from [PyPI](https://pypi.org) such as `numpy`, declared in the script itself with `#r: numpy`
- Separate package environments, for packages that clash with each other
- Current Python language features, and the libraries that expect them

```python
#r: numpy

import numpy as np
import rhinoscriptsyntax as rs

points = np.random.rand(10, 3) * 100

for point in points:
    rs.AddPoint(*point)
```

## What Python 2 Still Does Better

IronPython runs on .NET with nothing in between, which shows in two places:

- Pure RhinoCommon calls are faster
- Real .NET multithreading is available

So the choice is per script rather than once and for all. Scripts that lean on packages want Python 3. Scripts that hammer RhinoCommon, or that need threads, can be better off staying on Python 2.

## The Script Editor

Scripts of both runtimes are written in the Script Editor, opened with the `ScriptEditor` command. The same command runs scripts from macros, toolbar buttons, and aliases:

```text
_-ScriptEditor _R "C:\path\to\script.py"
```

See [ScriptEditor Command in Macros](/guides/scripting/advanced-scripteditor-macros) for the other command options, and [Scripting: Python](/guides/scripting/scripting-python) for writing and debugging scripts.

{{< call-out "note" "Note" >}}
The `EditPythonScript` command and its editor still exist, but are deprecated. New work belongs in `ScriptEditor`.
{{< /call-out >}}

## Python 3 in Grasshopper

Grasshopper has a Python 3 script component alongside the older GHPython component. `ghpythonlib` works the same under Python 3 as it does under Python 2:

```python
import ghpythonlib.components as ghcomp

a = ghcomp.Circle(x, y)
```

Grasshopper 2 ships its own Python 3 and Python 2 script components. `ghpythonlib` is a Grasshopper 1 library and is not available there.

Details are in the component guides:

- [Grasshopper Scripting: Python](/guides/scripting/scripting-gh-python)
- [Grasshopper 2 Scripting: Python](/guides/scripting/scripting-gh2-python)

## Publishing Scripts as Plugins

Scripts do not have to stay scripts. The Script Editor can gather them into a project and build that project into a Rhino or Grasshopper plugin, so your scripts become Rhino commands and Grasshopper components that others install like any other plugin.

- [Creating Rhino/Grasshopper Script Plugins](/guides/scripting/projects-create) for making a project, and adding commands and components to it
- [Publishing Rhino/Grasshopper Script Plugins](/guides/scripting/projects-publish) for building and sharing the plugin

## Moving a Script to Python 3

Most of the work is ordinary Python 2 to Python 3 work: `print` is a function, `/` on two integers no longer truncates, `range` replaces `xrange`, and `str` replaces `basestring`. The [Python documentation](https://docs.python.org/3/whatsnew/3.0.html) covers the language changes.

Three changes catch Rhino scripts in particular.

**Enum members named `None`.** `None` is a keyword in Python, so Python.NET exposes such members in upper case:

```python
# python 2
value = Rhino.Geometry.Mesh.MeshType.None

# python 3
value = Rhino.Geometry.Mesh.MeshType.NONE
```

**Methods returning collections.** A .NET method returning an `IEnumerable` gives you an iterator in Python 3, not a list. Wrap it when you need indexing or a length:

```python
items = list(some_method())
```

**Subclassing .NET types.** Python.NET expects the base constructor to be called, so a class deriving from a .NET type needs a `super()` call in its `__init__`. IronPython let you leave it out:

```python
import Rhino

class MyConduit(Rhino.Display.DisplayConduit):
    def __init__(self):
        # required in python 3
        super().__init__()

        self.points = []
```

Without it, the object is not fully constructed and calls into it fail.

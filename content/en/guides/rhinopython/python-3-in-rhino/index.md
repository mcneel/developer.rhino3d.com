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

Rhino 8 and newer, embed two Python runtimes side by side:

- **Python 3** is [CPython](https://www.python.org), and reaches .NET and RhinoCommon through [Python.NET](https://pythonnet.github.io)
- **Python 2** is [IronPython](https://ironpython.net), which runs on .NET itself

Python 3 is an addition, not a replacement. Your Python 2 scripts keep running on IronPython, and both runtimes are available in Rhino and in Grasshopper.

Scripts of either runtime are written in a refreshed Script Editor, and it is the editor that puts the rest of this page within reach: installing packages, and a real debugger with breakpoints, variables, and a call stack. That debugger also works inside Grasshopper components, which the old editor could not do.

## What You Get With Python 3

Python 3 opens up the wider Python world:

- Packages from [PyPI](https://pypi.org) such as `numpy`, declared in the script itself with `# r: numpy`
- Separate package environments, for packages that clash with each other
- Current Python language features, and the libraries that expect them

```python
# r: numpy

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

For a script that has to work under either runtime, see [Scripts That Run on Both](/guides/scripting/scripting-python/#scripts-that-run-on-both).

## Where To Go Next

- [Scripting: Python](/guides/scripting/scripting-python) for writing, running, and debugging scripts
- [Python Package Environments](/guides/scripting/advanced-pyvenvs) for packages that clash
- [Python Path Files](/guides/scripting/advanced-pthfiles) for adding module search paths

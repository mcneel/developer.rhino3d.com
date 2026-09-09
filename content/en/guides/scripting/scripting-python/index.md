+++
title = "Scripting: Python"
description = "Provides detailed information on Python scripting in Rhino"
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

    /* directive table reads as rows, no header needed */
    .main-content table { table-layout: fixed; width: 100%; }
    .main-content table thead { display: none; }
    .main-content table th:first-child,
    .main-content table td:first-child { width: 45%; }
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
        font-size: 14px;
    }
</style>

{{< call-out "note" "Note" >}}
This guide covers writing Python scripts in Rhino. For Python scripting in Grasshopper components, see [Grasshopper Scripting: Python](/guides/scripting/scripting-gh-python).
{{< /call-out >}}

## Creating a Python Script

Run the `ScriptEditor` command to open the script editor. Choose **File > New** and pick Python 3 from the list of languages:

<!-- SCREENSHOT: File > New prompt open with the language list, Python 3 highlighted -->
![](python-new.png)

Write your script and choose **Run > Run** to run it. The status bar shows the language and version of the script you are editing:

<!-- SCREENSHOT: editor with a short Python script, status bar showing the language and version -->
![](python-run.png)

Scripts are saved as `.py` files. **File > New From Template** starts a new script from one of your [templates](/guides/scripting/editor-templates).

## Python 3 and Python 2

Rhino embeds two Python runtimes. They are separate implementations rather than two versions of the same thing, and each has its own strengths and its own quirks:

- **Python 3** is [CPython](https://www.python.org). It installs and uses packages from PyPI, so libraries like `numpy` are available to your scripts. It reaches .NET, and therefore RhinoCommon, through [Python.NET](https://pythonnet.github.io)
- **Python 2** is [IronPython](https://ironpython.net), which runs on .NET itself. Pure RhinoCommon calls are faster since nothing sits in between, and it has real .NET multithreading

Python 3 is the better starting point for most scripts, if only for the packages. A script that spends its time calling RhinoCommon, or that needs threads, can do better in Python 2.

Both are listed as separate languages when you create a script, and the editor shows which one the current script uses. A script saved as `.py3` or `.py2` is pinned to that runtime, while a plain `.py` file is opened with the runtime the script asks for.

Choose **Tools > Reload Python 3 (CPython) Engine** or **Tools > Reload Python 2 (IronPython) Engine** to restart an engine without restarting Rhino. This is useful after installing packages or changing modules your script imports:

<!-- SCREENSHOT: Tools menu open showing the two engine reload items -->
![](python-engines.png)

## Scripts That Run on Both

For a script that has to work under either runtime, `rhinocompat` carries the differences:

```python
import rhinocompat as compat
from rhinocompat import PY3, RANGE

for i in RANGE(10):
    pass

value = compat.ENUM_NONE(Rhino.Geometry.Mesh.MeshType)

if PY3:
    pass
```

It also has `STRING_TYPE`, `IS_STRING_INSTANCE()`, and `ITERATOR2LIST()` for the cases above.

## Running Scripts From Rhino

Scripts do not have to be run from the editor. The `ScriptEditor` command can run a script file from the Rhino prompt, a macro, a toolbar button, or an alias:

```text
_-ScriptEditor _R "C:\path\to\script.py"
```

A script written straight into a macro needs a language specifier so Rhino knows which engine to run it with:

```text
_-ScriptEditor _R (
    #! python 3
    print("Hello Rhino")
)
```

See [ScriptEditor Command in Macros](/guides/scripting/advanced-scripteditor-macros) for the rest of the command options.

## Debugging

Click the gutter to the left of a line to add a breakpoint, then choose **Run > Debug** to run the script and stop there:

<!-- SCREENSHOT: Python script paused on a breakpoint, debug panels open below -->
![](python-debug.png)

**Debug** is only available when the script has a breakpoint. While the script is paused you can step through it and inspect your variables in the debugging panels. See [Debugging Your Scripts](/guides/scripting/editor-debug).

## PyPI Packages

Your scripts can use packages published on [PyPI](https://pypi.org). Choose **Install Package** on the editor dashboard, then search for the package or type its name and version:

<!-- SCREENSHOT: Install Package dialog with a PyPI package searched -->
![](python-packages.png)

Leave **Add Package Reference to Script** checked to write the package into the script text. The script then carries the list of packages it needs, and can install them when someone else opens it:

```python
# r: numpy

import numpy as np

print(np.random.rand(7))
```

`# r:` and `# requirements:` are the same thing, and both take more than one package:

```python
# requirements: numpy, requests
```

Packages can also be declared in a [PEP 723](https://peps.python.org/pep-0723/) block, which other Python tools understand too:

```python
# /// script
# dependencies = ["numpy", "requests"]
# ///

import numpy as np
```

For packages that clash with each other, or with what Rhino already loads, see [Python Package Environments](/guides/scripting/advanced-pyvenvs).

## .NET Packages and Assemblies

Python scripts can reach .NET as well. Python 3 does this through [Python.NET](https://pythonnet.github.io), while Python 2 runs on .NET already. Either way, import the namespaces you need:

```python
import System
import Rhino
```

Packages and assemblies are referenced with the same `# r` directive:

|  |  |
| --- | --- |
| `# r "pip: numpy"` | A package from PyPI |
| `# r "nuget: Newtonsoft.Json, 13.0.3"` | A package from NuGet |
| `# r "yak: LunchBox, 2025.5.5"` | A Rhino package from the package server |
| `# r "wheel: /path/to/package.whl"` | A wheel file on disk |
| `# r "/path/to/module.dll"` | An assembly file on disk |

## Sharing Code Between Scripts

Put code you use in more than one script into a module and import it:

```python
import myhelpers

myhelpers.do_the_thing()
```

For Rhino to find the module, its folder has to be on the module search path. **Module Search Paths** in [Options](/guides/scripting/editor-configs) lists the folders that are searched, in order. See [Python Path Files](/guides/scripting/advanced-pthfiles) for adding paths with a `.pth` file instead.

<!-- SCREENSHOT: Module Search Paths in the editor options dialog -->
![](python-searchpaths.png)

## Language Options

Editing features like line numbers, indentation guides, autocomplete, and tab size can be set for Python alone. Choose **Tools > Language Options** while editing a Python script, or right-click the script tab and choose **Language Options**:

<!-- SCREENSHOT: Language Options dialog open for Python -->
![](python-langoptions.png)

Each option can follow the editor-wide setting or be set for Python only. The editor-wide values are in [Options](/guides/scripting/editor-configs).

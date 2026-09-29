+++
title = "Script Package References"
description = "Provides information on referencing packages from scripts"
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

    /* option table reads as rows, no header needed */
    .main-content table { table-layout: fixed; width: 100%; }
    .main-content table thead { display: none; }
    .main-content table th:first-child,
    .main-content table td:first-child { width: 35%; }
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
        font-size: 14px;
    }
</style>

{{< call-out "new" "New in Rhino 9" >}}

Some of the directives on this page are new in Rhino 9 and are not understood by earlier versions.

{{< /call-out >}}

## Package References

A package reference is a line in your script that says which packages the script needs. The script carries its own list, so it installs what it needs when someone else opens it.

References come in two forms:

```python
# short form, python 3 packages
#r: numpy

# full form, any package provider
#r "pip: numpy"
```

Use `#` to start the line in Python. In C# use `#r` or `// r`.

## Python 3 Packages

`#r:` and `#requirements:` are the same thing, and take one or more packages:

```python
#r: numpy
#requirements: numpy, requests
```

Versions are written the way pip writes them:

```python
#r: torch==2.4.1
#r: numpy>=1.2
```

The full form does the same through the `pip` provider. Quote specs that contain spaces:

```python
#r "pip: numpy"
#r "pip: requests[security]"
```

### Your Own Libraries

A library of your own that is not published on PyPI can be installed in place, straight from the folder you develop it in:

```python
#r "pip: --editable /Users/me/dev/mylibrary"
```

This is better than copying the library next to your script, which hides any properly installed copy of it.

### Git Repositories

Packages can come from a repository, optionally pinned to a commit, tag, or branch:

```python
#r "pip: git+https://github.com/user/repo.git"
#r "pip: git+https://github.com/user/repo.git@9e3c1a2"
```

### Other Package Indexes

pip options are accepted alongside the packages, so a package can come from somewhere other than PyPI:

|  |  |
| --- | --- |
| `--index-url` | Use this index instead of PyPI |
| `--extra-index-url` | Also look in this index |
| `--find-links` | Look for packages at this path or url |
| `--no-index` | Do not use an index at all |

```python
#r "pip: mypackage --index-url https://my.company.server/simple"
#r "pip: mypackage --no-index --find-links /Users/me/wheels"
```

### Inline Script Metadata

Packages can also be declared in a [PEP 723](https://peps.python.org/pep-0723/) block, which other Python tools read as well:

```python
# /// script
# dependencies = ["numpy", "requests"]
# ///

import numpy as np
```

Only the `dependencies` list is read. Other fields in the block are ignored.

## NuGet Packages

.NET packages are referenced with the `nuget` provider, from both C# and Python:

```csharp
#r "nuget: RestSharp, 110.2.0"
```

```python
#r "nuget: Newtonsoft.Json, 13.0.3"
```

## Rhino Packages

Packages from the Rhino package server are referenced with the `yak` provider:

```python
#r "yak: LunchBox, 2025.5.5"
```

## Assembly Files

An assembly is referenced by name when it is already loaded in Rhino, or by path:

```csharp
#r "System.Text.Json.dll"
#r "/path/to/my/assemblies/MySharedAssembly.dll"
```

## Python 2 Packages

Python 2 has no pip. Wheel files are the only packages it installs, so a package has to be a `.whl` file on disk:

```python
#wheel: /path/to/package.whl
```

The full form does the same:

```python
#r "wheel: /path/to/package.whl"
```

## Related Topics

- [Python Package Environments](/guides/scripting/advanced-pyvenvs) for keeping packages of one script away from another with `# venv:`
- [Python Path Files](/guides/scripting/advanced-pthfiles) for adding module search paths
- [Scripting: Python](/guides/scripting/scripting-python)
- [Scripting: C#](/guides/scripting/scripting-csharp)

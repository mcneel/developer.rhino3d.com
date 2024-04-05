+++
aliases = ""
authors = [ "scott" ]
categories = [ "Intermediate" ]
description = "This guide covers the various ways to install packages in Python for Rhino."
keywords = [ "Rhino.Python", "Python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Using Python Packages"
type = "guides"
weight = 27
override_last_modified = "2024-04-05T14:59:06Z"
draft = false

[admin]
TODO = ""
origin = ""
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

One of the powers of Python is its ability to use thousands of additional modules in its scripts.
There are 4 main sources of Python packages that may be installed or loaded into Python 3.
* Built-in Modules - Comes with the RHino.Python install.
* Local Modules - These are Libraries made from other Python files.
* Packages on Pypi - 300,000 Python Modules available online.
* Downloaded Packages - For some specialized Packages, it may be necessary to download the models manually.

## Built-in Modules

Rhino comes with many built in modules that add functionality.  To use methods within built-in modules they simply need to be imported first:

```python
import math
```

Here are a list of the most useful to built in modules for Python:

* Date and Time
  * datetime — Basic date and time types
  * time — Time access and conversions
* Numeric and Mathematical Modules
  * math — Mathematical functions
  * fractions — Rational numbers
  * random — Generate pseudo-random numbers
* File and Directory Access
  * System.IO — Common pathname manipulations
  * tempfile — Generate temporary files and directories
  * csv — CSV File Reading and Writing
* String Services
  * string — Common string operations
  * StringIO — Read and write strings as files
  * fpformat — Floating point conversions

A complete list of predefined modules in Python, see the [Python Standard Library modules](https://docs.python.org/3/library/)

## Local Modules

Other Python files can be used to import functions using [Def](https://docs.python.org/3/tutorial/modules.html)

For instance in a `tools.py` file here are two defined functions `print_rhino_version` and `get_python_version`

```python
import Rhino
import sys


def print_rhino_version():
    ver = str(Rhino.RhinoApp.Version)
    versp = ver.split(".")
    print("Major version: " + versp[0])
    print("Service Release: " + versp[1])


def get_python_version():
    ver = sys.version
    print("Python version: " + ver)
```

Those functions then can be imported and called by:

```python
import python_functions as pf

pf.print_rhino_version()
```

Additonal details can be found on [Functions in Python](https://diveintopython.org/learn/functions)

## Python Package Index (PyPI)

PyPI is a repository of software for the Python programming language with over 500,000 packages.  
You can specify the packages required for your scripts inside the script source. This creates self-contained scripts that carry all their requirements with them.
Python 3 will use pip to install packages from PyPI.org
pip does not support Python 2 anymore so only works for Python 3.

Popular PiPy packages are:
* Pandas - data analysis toolkit
* Numpy - popular scientific computing with Python
* Scipy - modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing
* pyyaml - human-readable YAML-serialized data
* Pillow - Python Imaging Library
* openpyxl - library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.

Looking at Python 3 default script, we can specify required packages using this syntax:

```python
# r: numpy
```
or

```python
# requirements: numpy
```

Let’s create a new Python 3 script and add numpy as a package and use that in our script:

```python
# r: numpy

import numpy

print(f"using numpy: {numpy.version.full_version}\n")

for i in numpy.random.rand(10):
   print(i)
```

Click Run, and the script editor will attempt to install the required packages before running the script. This process might take some time and the editor is going to be disabled. Once the packages are installed, editor will continue to execute the script:

Mutiple packages can be install and are reccomended to be listed on the same line:

```python
#r: numpy, scipy
```

Additional PyPI version specifiers can also be used as referenced in [Install PyPI Syntax Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)

The [PyPI website](https://pypi.org/) can be searched for the many packages that are availble. 

## Downloading Python Libraries (Modules)

The last way that packages can be used is tho download the packages and put it into a library on the computer.  This allows a very tight control of the packages available.  This is also a good way to install packages that are not available on Pip the time.

Another method of adding local packages to Python scripts is by adding their path to the `sys.path`. You can simplify this step by using the # env: specifier in your scripts to automatically add a path to the `sys.path` before running your script.  Using a customer folder is recommended as Rhino updated will not overwrite the folder as it will the internal app folders: 

```python
# env: C:/Path/To/Where/My/Library/Is/Located/

import mylibrary

mylibrary.do_something()
```


## Related Topics

- [What are Python and RhinoScriptSyntax?](/guides/rhinopython/what-is-rhinopython)
- [Python Basic Syntax](/guides/rhinopython/python-statements/)
- [Python Procedures](/guides/rhinopython/python-procedures/)
- [Rhinoscript Syntax in Python](/guides/rhinopython/python-rhinoscriptsyntax-introduction/)
- [Rhino.Python Home Page](/guides/rhinopython/)
- [Python (homepage)](https://www.python.org/)

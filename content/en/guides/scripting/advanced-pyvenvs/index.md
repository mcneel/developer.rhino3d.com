+++
title = "Python Package Environments"
description = "Provides information on managing multiple python package environments"
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
        font-size: 14px;
    }

    .language-csharp {
        font-size: .9em;
    }
</style>

## Package Conflicts

Sometimes scripts need different versions of the same package either intentionally or through nested dependencies. Imagine this scenario:

- File *script_a.py* requires *pkg_a* version 1
- File *script_b.py* requires *pkg_b* version 2 which is dependent on *pkg_a* version 2 (newer than pkg_a of *script_a*)
- On a clean Rhino, running *script_a* installs and loads *pkg_a* v1
- On a clean Rhino, running *script_b* installs and loads *pkg_b* + *pkg_a* v2

Here is a few ways that package version conflicts can happen:

### A) PIP Install Failure

Following the scenario above, if *script_a* is executed successfully in a Rhino session, running *script_b* will probably fail when installing *pkg_b*. Script Editor is using *pip* to install packages. Since, by default, all the packages for all the various scripts are installed in the same directory (as python normally does), this creates a conflict when pip is trying to remove *pkg_a* v1 to install *pkg_a* v2. Remember Rhino has already executed *script_a*, therefore *pkg_a* libraries are loaded in memory and at least on Windows, these library files are locked and can not be deleted while Rhino is running.

Any pip install error will mark the environment as *Invalid* and will cleanup after Rhino is restarted.

### B) Runtime Conflicts

Following the scenario above, even if the two version of *pkg_a* can be installed at the same time, *pkg_a* is already loaded in Python 3 runtime and loading another version of this package (that is in the same directory) might lead to runtime errors and unexpected behaviour.

## Virtual Environments

Tools like *pipenv* and other environment managers for Python, normally solve this problem by creating multiple **Virtual Environment**s. Each virtual environment has a dedicated folder with its own `site-packages` (where pip installs packages by default). Python core binaries are then linked into this folder to create a fully functional Python environment. Following the scenario above:

- File *script_a.py* requires *pkg_a* version 1 - installed in *venv_a*
- File *script_b.py* requires *pkg_a* version 2 through *pkg_b* version 2 - installed in *venv_b*

So each script is created inside a unique virtual environment and are run independently of each other:

![](venvs-python.jpg)

### "Virtual" Environments in Rhino

Virtual Environments (vnev) in Rhino are implemented differently. The main reason is that in normal venvs, separate python processes run *script_a* and *script_b* so there is no runtime conflict between these two processes. They each have their own memory and python interpretter state.

In Rhino, however, both *script_a* and *script_b* are executed inside the same process, same memory, and same python interpretter state. So we can not really have true virtual environments unless you are running separate Rhino processes:

![](venvs-rhino-conflict.jpg)

{{< call-out "note" "Environments in Rhino" >}}

Virtual Environments in Rhino are usually helpful in avoiding to reinstall packages. If you are running a script with conflicting packages, pip has to uninstall the existing to install new versions. This means that your scripts keep uninstalling and reinstalling packages and will eventually overwrite each other, corrupting the installed environment.

`venv` tag helps keeping these install packages separate and is great when running scripts in separate Rhino processes:

![](venvs-rhino-noconflict.jpg)

Note that if you are running two scripts with two different versions of torch library in the same Rhino instance you might/will run into runtime conflicts as described above.

{{< /call-out >}}

### Default Environment

By default, all python packages are installed to `site-envs/default-<unique-id>` directory inside Python 3 runtime directory. This path is added to `sys.path` and is the first path to be searched when importing installed modules:

```text
/Users/*/.rhinocode/py39-rh8/site-envs/default-A6YRvqqN
/Users/*/.rhinocode/py39-rh8/site-rhinoghpython
/Users/*/.rhinocode/py39-rh8/site-rhinopython
/Users/*/.rhinocode/py39-rh8/site-interop
/Users/*/.rhinocode/py39-rh8/lib/python39.zip
/Users/*/.rhinocode/py39-rh8/lib/python3.9
```

### Custom Environments

You can configure your script to install required packages in a custom environment using `# venv: <environment-name>` tag. When running this example script, Python 3 will create new folder `site-envs/my-pytorch-tools-<unique-id>` to install pytorch v2.4.1 in that environment. `<unique-id>` is automatically assigned to the environment to avoid conflicts:

```python
#! python 3
# venv: my-pytorch-tools
# r: torch==2.4.1

import pytorch

```

This will ensure that the requirements for your package do not override any existing installed packages for other scripts. If you are fixing the version of a package in your script or use packages that might cause conflicts, it is good practice to specify a unique name for this environment to avoid conflicts.

### Invalid Environments

When a pip install error occurs, the target environment is marked as *Invalid*. Therefore it is necesary to restart Rhino so editor can cleanup the environment and start fresh.

### Site-Packages

As mentioned above, by default, all python packages are installed to `site-envs/default-<unique-id>` directory. Sometimes it is necessary to install packages under the default python `site-packages` folder. Normally this folder is reserved for packages that Python 3 runtime inside of Rhino requires to work e.g. `pip` itself.

There is a special environment id `site-packages`. This id can be used in your scripts to force install packages into `site-packages` directory. 

```python
#! python 3
# venv: site-packages
```

In case any install errors occured, please run *Tools > Advanced > Reset Python 3 (CPython) Runtime* to reset the complete runtime and install a fresh deployment of Python 3 with clean `site-packages` and `site-envs` directories.

### Python 3 Shell

When using Python 3 shell (from *Tools > Advanced > Open Python 3 Shell*), you might want to manually install packages using *pip*. As the notes printed on the shell describe, you would need to specify the `--target` option and point `pip` to a specific environment under `site-envs` that you want to install the packages to.

If `--target` is not specified, `pip` automatically installs packages under `site-packages`.

![](python-shell-target.png)

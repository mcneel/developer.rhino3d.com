+++
title = "Python Path Files"
description = "Provides information on system and user python search path files"
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

## Path Files

Path files are simple ascii files with one search path per line. These files are similar to [Python 3 path configuration files](https://docs.python.org/3/library/site.html) except that they can only contain search paths and no code inside these files will be parsed or executed. First path in the file would be the first path to be search for a module, so the order is important.

Script editor stores search paths configured in the options window, in these files:

- `.rhinocode/python-2.pth`
- `.rhinocode/python-3.pth`

You can edit these files manually and Rhino will use the paths on next launch.

By default, Rhino adds all the paths specified in python path files (*.pth) under these locations to Python 2 and 3 search paths (`sys.path`):

On Windows:

- `%PROGRAMDATA%\McNeel\Rhinoceros\<version>.0\scripts` (if exists)
- `%APPDATA%\McNeel\Rhinoceros\<version>.0\scripts`
- `.rhinocode`

On macOS:

- `/Users/Shared/McNeel/Rhinoceros/<version>.0/scripts` (if exists)
- `~/Library/Application Support/McNeel/Rhinoceros/<version>.0/scripts`
- `.rhinocode`

## Path File Naming

As you might have noticed, the name of the `.pth` file specifies language specification and follows the format below with minor and patch numbers being optional:

`<language>-<major>.<minor>.<patch>`

So `python-3.pth` specifies Python of version 3. The names can be more specific as in `python-3.9.10.pth`. You can also include other text after the language specification as in `python-3_dev.pth`. Any text after the language specification is only for creating unique path file names and will be ignored.

For example, to make sure custom python modules are importable, a Rhino plugin developer can:

- place their python modules under shared `scripts/`

OR

- place a `python-3_pluginname.pth` file under shared `scripts/` and list more that one search path pointing to where the python modules are located
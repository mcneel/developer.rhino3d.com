+++
aliases = ["/5/guides/rhinopython/your-first-python-script-in-rhino-mac/", "/6/guides/rhinopython/your-first-python-script-in-rhino-mac/", "/7/guides/rhinopython/your-first-python-script-in-rhino-mac/", "/wip/guides/rhinopython/your-first-python-script-in-rhino-mac/"]
authors = [ "alain" ]
categories = [ "Getting Started" ]
description = "This guide covers the basics of getting started writing Python in Rhino for Mac."
keywords = [ "Rhino.Python", "Python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Your First Python Script in Rhino (Mac)"
type = "guides"
weight = 2
override_last_modified = "2019-09-13T13:01:12Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/python"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac" ]
since = 0
version = [  "7", "8" ]

[page_options]
byline = true
toc = true
toc_type = "single"

+++

## Running a Python script

To get acquainted with how Python scripts can help you model first run some of the sample scripts that are provided.

  1. In the Command prompt edit box (top left by default) type the RunPythonScript command.
  2. If it's the first time you run this command the dialog box that comes up will show the files in the samples directory.  If it's not then navigate to it.  It should be under:
  ```
  ~/Library/Application Support/McNeel/Rhinoceros/6.0/Scripts/samples
  ```
  (the beginning tilde (~) character is normally in the far upper left of the keyboard).
  3. Experiment by running HelloPython.py

## Editing a Python Script

You can open any of the sample Python scripts in a text editor. From Finder navigate to the samples directory:

```
/Users/HOME/Library/Application Support/McNeel/Rhinoceros/6.0/Scripts/samples
```
(replace HOME with your home directory name).

Or in the Finder, use the Go pulldown > Go To Folder... and type:

```
~/Library/Application Support/McNeel/Rhinoceros/6.0/Scripts/samples
```

Right-click on any of the scripts and from the context menu that pops up select Open With -> TextEdit.app which is the text editor that comes with macOS.  You can try editing and saving the files and then re-run them in Rhino with the `RunPythonScript` command.

When you're ready start writing more complex scripts you can install the [Atom text editor](https://atom.io/packages/rhino-python) that's been specifically enhanced for <a href="https://atom.io/packages/rhino-python" target="_blank">rhino-python</a> package to help with scripts that will be run by Rhino.

After you've followed the above links and setup Atom the next step is to get familiar with the different [application programming interfaces (API)](../apis-for-python/) you'll need to write scripts that interact with Rhino.

## Related Topics

- [What are Python and RhinoScriptSyntax?](/guides/rhinopython/what-is-rhinopython)
- [Using the Atom.io editor with Rhino.Python](https://atom.io/packages/rhino-python)
- [Python Basic Syntax](/guides/rhinopython/python-statements/)
- [Rhinoscript Syntax in Python](/guides/rhinopython/python-rhinoscriptsyntax-introduction/)
- [Rhino.Python Home Page](/guides/rhinopython/)

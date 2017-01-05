---
title: Your First Python Script in Rhino (Mac)
description: This guide covers the basics of getting started writing Python in Rhino for Mac.
authors: ['Alain Cormier']
author_contacts: ['Alain']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac']
categories: [ ]
origin: http://wiki.mcneel.com/developer/python
order: 2
keywords: ['Rhino.Python', 'Python']
layout: toc-guide-page
---

## Running a Python script

To get acquainted with how Python scripts can help you model first run some of the sample scripts that are provided.

  1. In the Command prompt edit box (top left by default) type the RunPythonScript command.
  2. If it's the first time you run this command the dialog box that comes up will show the files in the samples directory.  If it's not then navigate to it.  It should be under:
  ```
  ~/Library/Application/Support/McNeel/Rhinoceros/Scripts/samples
  ```
  (the begining tilde (~) character is normally in the far upper left of the keyboard).
  3. Experiment by running HelloPython.py

## Editing a Python Script

You can open any of the sample Python scripts in a text editor. From Finder navigate to the samples directory:

```
/Users/HOME/Library/Application\ Support/McNeel/Rhinoceros/Scripts/samples
```
(replace HOME with your home directory name).

Or in the Finder, use the Go pulldown > Go To Folder... and type:

```
~/Library/Application/Support/McNeel/Rhinoceros/Scripts/samples
```

Right-click on any of the scripts and from the context menu that pops up select Open With -> TextEdit.app which is the text editor that comes with macOS.  You can try editing and saving the files and then re-run them in Rhino with the `RunPythonScript` command.

When you're ready start writing more complex scripts you can install the [Atom text editor](https://atom.io/packages/rhino-python) that's been specifically enhanced for <a href="https://atom.io/packages/rhino-python" target="_blank">rhino-python</a> package to help with scripts that will be run by Rhino.

After you've followed the above links and setup Atom the next step is to get familiar with the different [application programming interfaces (API)](../apis-for-python/) you'll need to write scripts that interact with Rhino.

---

## Related Topics

- [What are Python and RhinoScriptSyntax?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Using the Atom.io editor with Rhino.Python](https://atom.io/packages/rhino-python)
- [Python Basic Syntax]({{ site.baseurl }}/guides/rhinopython/python-statements/)
- [Rhinoscript Syntax in Python]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-introduction/)
- [Rhino.Python Home Page]({{ site.baseurl }}/guides/rhinopython/)

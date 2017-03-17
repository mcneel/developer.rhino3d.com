---
title: Running a Python script in Rhino
description: This guide demonstrates how to run a Python script in Rhino.
authors: ['Scott Davidson']
author_contacts: ['scottd']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Python Windows']
origin:
order: 4
keywords: ['python', 'commands']
layout: toc-guide-page
---

## Running Scripts

The RunPythonScript command is used to execute script subroutines that were loaded into the Python engine.

## RunPythonScript operation

The RunScript dialog box will display a file dialog box.  Select a Python file (.py) to run in Rhino.  Simply select the python file and hit OK. The Python script will run.

## Scripting the RunPythonScript command

As is the case with most Rhino commands, the RunPythonScript command can be scripted, thus bypassing the interactive dialog box.  To script the RunPythonScript command, simply precede the command name with a hyphen when entering the command on Rhino's command line.  For example:

-RunPythonScript

After entering the command, you will be prompted to enter the name of the script to run.

## Assigning the RunPythonScript command to a button.

The RunPythonScript command can also be assigned to command aliases or to a toolbar button.

<img src="{{ site.baseurl }}/images/runpythonscript.png" alt="RunPythonScript">

<!-- TODO: Does RunPython actually run this way: When assigned to a toolbar button, the RunPythonScript can execute raw Python code.  To embed raw Python code on a button, make sure to surround the code with an opening and closing parenthesis.-->

---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Your First Python Script in Rhino (Windows)]({{ site.baseurl }}/guides/rhinopython/your-first-python-script-in-rhino-windows)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)

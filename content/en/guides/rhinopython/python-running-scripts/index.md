+++
aliases = ["/en/5/guides/rhinopython/python-running-scripts/", "/en/6/guides/rhinopython/python-running-scripts/", "/en/7/guides/rhinopython/python-running-scripts/", "/wip/guides/rhinopython/python-running-scripts/", "/guides/rhinopython/python-loading-scripts/"]
authors = [ "scottd" ]
categories = [ "Python Windows" ]
description = "This guide demonstrates how to run a Python script in Rhino."
keywords = [ "python", "commands" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Running a Python script in Rhino"
type = "guides"
weight = 20
override_last_modified = "2018-12-05T14:59:06Z"
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 7
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"

+++

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

<img src="/images/runpythonscript.png" alt="RunPythonScript">

<!-- TODO: Does RunPython actually run this way: When assigned to a toolbar button, the RunPythonScript can execute raw Python code.  To embed raw Python code on a button, make sure to surround the code with an opening and closing parenthesis.-->

## Related Topics

- [What is RhinoPython?](/guides/rhinopython/what-is-rhinopython)
- [Your First Python Script in Rhino (Windows)](/guides/rhinopython/your-first-python-script-in-rhino-windows)
- [Running Scripts](/guides/rhinopython/python-running-scripts)
- [Canceling Scripts](/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts](/guides/rhinopython/python-editing-scripts)

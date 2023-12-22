+++
aliases = ["/5/guides/rhinopython/your-first-python-script-in-rhino-windows/", "/6/guides/rhinopython/your-first-python-script-in-rhino-windows/", "/7/guides/rhinopython/your-first-python-script-in-rhino-windows/", "/wip/guides/rhinopython/your-first-python-script-in-rhino-windows/"]
authors = [ "scottd" ]
categories = [ "Getting Started" ]
description = "This guide demonstrates how to create Python scripts in Rhino for Windows."
keywords = [ "python", "commands" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Your First Python Script in Rhino 7 (Windows)"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 7
until = 8

[page_options]
block_webcrawlers = true
byline = true
toc = true
toc_type = "single"

+++


You will learn how to display a message box in Rhino that says "Hello World."  It covers the most basic concepts for editing, loading, and running scripts.

## The Complete Script

```python
import rhinoscriptsyntax as rs

rs.MessageBox ("Hello World")
```
To test the Script:

- Start Rhino
- At the command prompt, type EditPythonScript and press Enter.
- The Edit Script dialog box appears.
- In the script Code window, type the code sample above.
- Click the "Run the script" button.
- The Edit Script dialog box disappears, and the message below appears:

## The HelloWorld Function

If you were writing a more complex script, and wanted to display "Hello World" at strategic points throughout the script, you could write this code every time you wanted the message to appear.

But if you changed your mind and wanted it to say "Howdy World" instead, you'd have to search for all the places "Hello World" was used, and replace them.

An easier way to solve this problem is to write a Function (`def` is used to define the function).  At several places throughout your script, you call the function.  The function handles displaying the message, so you only have to change the message in one place.

Here's what the function definition looks like:

```python
import rhinoscriptsyntax as rs

def HelloWorld():
    rs.MessageBox ("Hello World")
```

If you click the run button at this time nothing will happen. Nothing happened? That's because the RhinoScript defined the Subroutine but did not actually call it. To call the subroutine, either add this line of code and click Run.

To call this function, simply add this to the bottom of the script:

```python
HelloWorld()
```

In Python the functions definitions need to come before being called in the code.

#### Testing HelloWorld

- At the command prompt, type EditScript and press Enter.
- The Edit Script dialog box appears.
- In the script Code window, type

```python
import rhinoscriptsyntax as rs

def HelloWorld():
    rs.MessageBox ("Hello World")

HelloWorld()
```
- Click the Run button.

When you do more than write a couple lines of script, it becomes necessary to save the script to a file so that you can run the script without typing it every time.

#### To save your script:

In the Edit Script dialog box, Click the Save button. Save the file as "Hello World.py".

#### Running HelloWorld.py

- At the Command prompt, type RunPythonScript and press Enter.
- In the Run python script dialog box, select "Hello World.py" and click Open.

Your script will run, and display the familiar "Hello World" dialog box.

## Related Topics

- [What is RhinoPython?](/guides/rhinopython/what-is-rhinopython)
- [Running Scripts](/guides/rhinopython/python-running-scripts)
- [Canceling Scripts](/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts](/guides/rhinopython/python-editing-scripts)

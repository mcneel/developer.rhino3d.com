+++
aliases = ["/5/guides/rhinopython/python-editing-scripts/", "/6/guides/rhinopython/python-editing-scripts/", "/7/guides/rhinopython/python-editing-scripts/", "/wip/guides/rhinopython/python-editing-scripts/"]
authors = [ "scottd" ]
categories = [ "Python Windows" ]
description = "This guide demonstrates how to edit a Python script in Rhino."
keywords = [ "python", "commands" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Editing a Python script in Rhino 7"
type = "guides"
weight = 6
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
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"

+++

## Editing Scripts

Any simple plain-text editor, such as Notepad, [Atom](https://atom.io/) or [Notepad++](https://notepad-plus-plus.org/) can be used to create and/or edit script files.  When saving your script file, make sure to give the file the default file extension for Python files, which is `.py`.

You can also create and edit script file from within Rhino by using the EditPythonScript command.  The EditPythonScript command can be accessed from either Rhino's Tools menu, or by entering EditPythonScript on Rhino's command line.

Note, there is no scriptable version of the EditPythonScript command.

## The RhinoPythonScript Editor

The RhinoPythonScript Editor can be used to edit, run, and debug scripts. It contains standard source code editing feature, such as find and replace (with regular expressions), multiple-document interface, method browser, and an integrated help file.

<img src="/images/pythoneditor.png" alt="Windows">

## The Code Editor

The most important item on the RhinoPythonScript Editor is the code editor. It is here that you make your scripts. As you can see, the editor is much more than a simple text editor. It performs automatic syntax parsing meaning you get properly colored keywords, collapsible code groups which encapsulate `def` function blocks, automatic indenting, auto-completion and error highlighting.

<img src="/images/pythoneditor-code-editor.png" alt="Windows">

Auto-completion and parameter tips are grouped under the catch-phrase Intellisense. Since Python is not a strongly typed language. Thus, Intellisense in the RhinoPythonScript Editor is limited to RhinoPythonScriptSyntax methods and script scope procedures.

In the RhinoPythonScript Ediotr, type:

```python
import rhinoscriptsyntax as rs
```

Any line that follows the auto-completion list pops up as soon as `rs.`. is typed. The list updates when you keep typing to reflect the best possible match with your current text. Once the desired method is highlighted in the pop up list, press [Enter] and the complete method name will be inserted into the script. Once the method name is in place, we have to supply the arguments. Intellisense displays a tooltip showing us the required arguments and which one we are currently setting.

Above the code editor you will find the document tab. The RhinoPythonScript Editor is multiple-document capable and you can switch between documents by clicking on the appropriate tab. You can also add existing files quickly by dragging them onto the file tab.

## The Method Browser

The method browser displays a categorized view of all RhinoPythonScript methods. Use the plus and minus tree icons to expand and collapse each category. You can search for methods by typing the method name in the search field and then pressing [Enter]. If you double-click on a method, in the method browser, help on the method will appear. To use the method in your script, just drag the method into the code editor.

<img src="/images/pythoneditor-module-browser.png" alt="Windows">

## The Status Bar

The status bar provides feedback on the location of the insertion caret in the currently active script. It provides both line and column coordinates, as well as procedure scope coordinate. You can jump to a specific line in your script by using the Go To Line dialog box. But you can also scroll the line index field in the status bar. Just click + drag up and down and the currently selected line will be scrolled.

The status bar exposes another quick navigation tool. If you click on the procedure scope field (the last field on the status bar) you will pop up a menu listing all defined Sub and Function procedures. Click on one of the names to jump to that procedure. If the caret is not inside any procedure body, the status bar will read "Global scope".

<img src="/images/pythoneditor-output-window.png" alt="Windows">

## The Toolbar

The toolbar exposes standard functionality, which can also be found in the menus.

<img src="/images/pythoneditor-toolbar.png" alt="Windows">

| Button | | |Shortcut | | |  Description |
|:--------|:-:|:-:|:-|:-:|:-:|:--------|
| New Script| | | Ctrl + N | | | Create a new script file with a custom header.   |
| Open Script  | | | Ctrl + O | | | Open an existing script. Dropdown arrow to access recent scripts |
| Save   | | | Ctrl + S | | | Save the currently active script.   |
| Save All   | | |   | | | Save all changes to all loaded scripts.   |
| Save As   | | | Ctrl + Shift + S | | | Save the active script under another file name.   |
| Find   | | | Ctrl + F| | | Search the active script for a specific string.   |
| Run Script  | | | F5 | | | Run the active script.   |
| Debug Script   | | | Ctrl + F5 | | | Run the active script with breakpoints enabled.  |
| Toggle Breakpoint   | | | F9 | | | Toggle breakpoint flag on the active line in the active script.   |

## The Menu

The menu provides access to all the RhinoPythonScript Editor features.

<img src="/images/pythoneditor-menubar.png" alt="Windows">

## Related Topics

- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Your First Python Script in Rhino (Windows)](/guides/rhinopython/your-first-python-script-in-rhino-windows)
- [Running Scripts](/guides/rhinopython/python-running-scripts)
- [Canceling Scripts](/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts](/guides/rhinopython/python-editing-scripts)
- [Scripting Options](/guides/rhinopython/python-scripting-options)
- [Reinitializing Python](/guides/rhinopython/python-scripting-reinitialize)

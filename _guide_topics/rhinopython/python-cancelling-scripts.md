---
title: Canceling a Python script in Rhino
description: This guide demonstrates how to cancel a Python script in Rhino.
authors: ['Scott Davidson']
author_contacts: ['scott']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Getting Started']
origin:
order: 5
keywords: ['python', 'commands']
layout: toc-guide-page
---

<!-- TODO: This page is nto right yet.  The Sleep function does not seem to help.  I need to check with soemone ont he Rhinocommon calls -->

## Cancelling Scripts

When a script is running, and it is not waiting for user input, it can be cancelled by pressing the ESC key.

Cancelling out of a tight loop

If you have a tight loop that does not call back into Rhino, then it is possible for ESC key processing to be either very slow or not happen at all. This is because the tight loop does not allow Rhino to process the messages, such as keystrokes, sent to it by Windows. For example, the following script is not be cancelled by pressing the ESC key.

```python
def TightLoopEscapeTest():
  for i in range(10000):
  
TightLoopEscapeTest()
```
To work around this situation, you will want to call back into Rhino inside of your tight loop. Using RhinoScriptSyntax's `sleep` function is a good way to do this without slowing down your code. For example:

```python
import rhinoscriptsyntax as rs

def TightLoopEscapeTest():
  for i in range(10000):
      # Do tight loop processing here...
      rs.Sleep(1)

TightLoopEscapeTest()
```

If your loop is relatively fast, you may want to postpone the Sleep call or else it will slow down your script significantly. For example: 

Sub TightLoopEscapeTest

  For i = 0 To 100000

    ' Do tight loop processing here...

    If ((i Mod 25) = 0) Then Call Rhino.Sleep(0)

  Next

End Sub

This will call the Sleep method only once every 25 iterations.

Using OnCancelScript to handle script cancelling

The default behavior when cancelling a script is to halt the script's execution and print a "Script cancelled" message to Rhino's command line. But, there are often times when you might want to know when your script is cancelled. For example, lets say you have a script that: (a) modifies some Rhino parameters, (b) performs an operation and, (c) resets the modified parameters. If your script is cancelled in operation (b), then Rhino can be left in a state unfamiliar to the user.

It is possible for your script to be notified when it has been cancelled. This is done through a special, user-defined subroutine named OnCancelScript. 

When a script is running and the ESC key is pressed, RhinoScript searches for loaded, user-defined subroutine named OnCancelScript. If this subroutine is detected, RhinoScript will automatically run this procedure instead of just printing the "Script cancelled" message. 

In the above script scenario, the user-defined OnCancelScript subroutine could reset the parameters (c) that were modified when the script started (a).

The following is a simple example that demonstrates the OnCancelScript procedure.

Sub TightLoopEscapeTest

  For i = 0 to 100000

    Call Rhino.Print(i)

    Call Rhino.Sleep(0)

  Next

End Sub

' User-defined cancel script handler

Sub OnCancelScript

  ' Do script cancelling operations here...

  Call MsgBox("Script Cancelled!", vbOkOnly + vbExclamation, "RhinoScript")

End Sub

Note, your user-defined OnCancelScript subroutine must not have any arguments. If you define your OnCancelScript subroutine as one that requires one or more arguments, then RhinoScript will not execute it when the ESC key is pressed.


---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [My First Script]({{ site.baseurl }}/guides/rhinopython/first-python-script-in-rhino)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)

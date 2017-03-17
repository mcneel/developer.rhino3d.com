---
title: Cancelling Scripts
description: This guide demonstrates how to allow scripts to be cancelled by the user.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/cancelscript
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Overview

When running a RhinoScript, it often occurs that a user wants to interrupt a running RhinoScript by pressing <kbd>ESC</kbd>.  This most frequently happens when running a script with a tight loop or a recursive function.  In order to cancel the script, we want to allow the user to press <kbd>ESC</kbd>, rather than having to stop Rhino using Task Manager and restart everything.  There are two topics to cover: Sleep and OnCancelScript.

## Sleep

If you have a tight loop that does not call back into Rhino, then it is possible for <kbd>ESC</kbd> key processing to be either very slow or not happen at all. This is because the tight loop does not allow Rhino to process the messages, such as keystrokes, sent to it by Windows.

To work around this situation, you will want to call back into Rhino inside of your tight loop.  Using RhinoScript's **Sleep** function is a good way to do this without slowing down your code...

```vbnet
Sub TightLoopEscapeTest
   For i = 0 To 100000
     '
     ' Do tight loop processing here...
     '
     ' Allow Rhino to "pump" it's message queue
     Call Rhino.Sleep(0)
   Next
 End Sub
```

If your loop is relatively fast, you may want to postpone the Sleep call or else it will slow down your script significantly...

```vbnet
Sub TightLoopEscapeTest
  For i = 0 To 100000
    '
    ' Do tight loop processing here...
    '
    ' Allow Rhino to "pump" it's message queue
    If ((i Mod 25) = 0) Then Call Rhino.Sleep(0)
  Next
End Sub
```

...which will call the Sleep method only once every 25 iterations.

## OnCancelScript

The default behavior when cancelling a script is to halt the script's execution and print a “Script cancelled” message to Rhino's command line.  There are often times when you might want to know when your script is cancelled. For example, lets say you have a script that does the following steps in this order:

1. Modifies some Rhino parameters...
1. Performs an operation and...
1. Resets the modified parameters.

If your script is cancelled in operation (2), then Rhino can be left in a state unfamiliar to the user.

It is possible for your script to be notified when it has been cancelled.  This is done through a special, user-defined subroutine named `OnCancelScript`.

When a script is running and the <kbd>ESC</kbd> key is pressed, RhinoScript searches for loaded, user-defined subroutine named `OnCancelScript`. If this subroutine is detected, RhinoScript will automatically run this procedure instead of just printing the “Script cancelled” message.

In the above script scenario, the user-defined `OnCancelScript` subroutine could reset the parameters (3) that were modified when the script started (1).

The following is a simple example that demonstrates the `OnCancelScript` procedure...

```vbnet
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
```

**NOTE**: your user-defined `OnCancelScript` subroutine must not have any arguments.  If you define your `OnCancelScript` subroutine as one that requires one or more arguments, then RhinoScript will not execute it when <kbd>ESC</kbd> is pressed.

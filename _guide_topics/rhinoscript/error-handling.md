---
title: Error Handling
description: This guide describes the error handling semantics of VBScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/errorhandling
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Overview

There are two statements that affect error handling in VBScript:

```vbnet
On Error Resume Next
On Error Goto 0
```

The meaning of the first statement is this: if you get an error, ignore it and resume execution on the next statement.  As we'll see, there are some subtleties.

The second statement simply turns off "Resume Next" mode if it is on.  The odd syntax is because Visual Basic has an error handling mode which VBScript does not – VB can branch to a labeled or numbered statement.

## Discussion

The subtlety in the "Resume Next" mode is best illustrated with an example...

```vbnet
Const InvalidCall = 5
Rhino.Print "Global code start"
Blah1
Rhino.Print "Global code end"

Sub Blah1()
  On Error Resume Next
  Rhino.Print "Blah1 Start"
  Blah2
  Rhino.Print "Blah1 End"
End Sub
Sub Blah2()
  Rhino.Print "Blah2 Start"       
  Err.Raise InvalidCall
  Rhino.Print "Blah2 End"
End Sub
```

This prints out:

```vbs
Global code start
Blah1 Start
Blah2 Start
Blah1 End
Global code end
```

When the error ocurred, Blah1 had already turned "Resume Next" mode on.  The next statement after the error raise is Print "Blah2 End" but that statement was never executed. This is because the error mode is on a per-procedure basis, not a global basis.

Also, remember that the `Next` in “Resume Next” mode is the next statement.  Consider these two scripts:

```vbnet
On Error Resume Next
Temp = CInt(Foo.Bar(123))
Blah Temp
Rhino.Print "Done"

On Error Resume Next
Blah CInt(Foo.Bar(123))
Rhino.Print "Done"
```

They do not have the same semantics.  If `Foo.Bar` raises an error, then the first script passes `Empty` to `Blah`.  The second one never calls `Blah` at all if an error is raised, because it resumes to the next statement.

You can get into similar trouble with other constructs.  For example, these do have the same semantics:

```vbnet
On Error Resume Next
If Blah Then
  Rhino.Print "Hello"
End If
Rhino.Print "Goodbye"

On Error Resume Next
If Blah Then Rhino.Print "Hello"
Rhino.Print "Goodbye"
```

If `Blah` raises an error then it resumes on the `Rhino.Print "Hello"` in either case.

You can also get into trouble with loops:

```vbnet
On Error Resume Next

For index = 1 to Blah
  Rhino.Print TypeName(index)
Next
Rhino.Print "Goodbye"
```

If Blah raises an error, this resumes into the loop, not after the loop. This prints out:

```vbs
Empty
Goodbye
```

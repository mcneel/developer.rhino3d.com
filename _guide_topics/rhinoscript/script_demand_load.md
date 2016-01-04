---
title: Script Demand Loading
description: unset
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/scriptdemandload
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# Script Demand Loading

This guide demonstrates how to demand load and run RhinoScript routines.

## Overview

The following RhinoScript example presents an organized and efficient method for loading and running all of the script that you have either written or accumulated.

The following example below demonstrates how to write a single startup script that can load and run any of your scripts on demand.

## Details

The *Startup.rvb* sample script, below, defines two special subroutines:

1. `DemandRun` checks for the existence of a user-defined subroutine. If the subroutine is not found, then script file, where the procedure is located, is loaded by running the LoadScript command.  Finally, the specified procedure is called.
1. `DemandRegister` registers command aliases that run macros that utilize the DemandRun subroutine.
At the bottom of the script file, you can “register” one or more command aliases and specify the scripts they will run.

When Rhino starts and this script file is loaded, all of your command aliases are registered.  But, none of your script files are loaded (except for the one and only *Startup.rvb*).  It is not until you run a command alias is the script actually loaded.  If you re-run the command alias, the script is not reloaded, but just run (since it is already loaded).  Since scripts are only loaded as needed, you are not loading up a bunch of scripts that you will never use, thus conserving memory and allowing Rhino to load faster.

```vbnet
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Startup.rvb -- September 2010
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0 and 5.0.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Description:
'   Demand loads and runs a script.
' Parameters:
'   subroutine [in] - The name of the script subroutine to run.
'   filename   [in] - The name of the file were the subroutine
'                     is located.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub DemandRun(ByVal subroutine, ByVal filename)
  Dim macro
  macro = "_-LoadScript " & QuoteString(filename)
  If Not Rhino.IsProcedure(subroutine) Then
    Call Rhino.Command(macro, 0)
  End If
  Call Execute(subroutine)
End Sub

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Description:
'   Registers command aliases that run macros that utilize the
'   DemandRun subroutine defined above.
' Parameters:
'   alias      [in] - The name of the command alias to register.
'   subroutine [in] - The name of the script subroutine the the
'                     alias will run.
'   filename   [in] - The name of the file were the subroutine
'                     is located.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub DemandRegister(ByVal alias, ByVal subroutine, ByVal filename)
  Dim macro, qsub, qfile
  qsub = QuoteString(subroutine)
  qfile = QuoteString(filename)
  macro = "_-NoEcho _-RunScript (DemandRun " & qsub & ", "  & qfile & ")"
  Call Rhino.AddAlias(alias, macro)
End Sub  

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Description:
'   Surrounds a string with double-quote characters.
' Parameters:
'   str [in] - The string to modify.
' Returns:
'   The modified string
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function QuoteString(ByVal str)
  QuoteString = Chr(34) & CStr(str) & Chr(34)
End Function

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' TODO: Register your demand loading and running scripts here!
' In the following section below, register the aliases that you
' want to create and the scripts that you want them to run.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Call DemandRegister("Hello", "Hello", "Hello.rvb")
Call DemandRegister("BoxFrame", "BoxFrame", "C:\Users\Dale\Scripts\BoxFrame.rvb")
```

---

## Related Topics

- [Efficient Script Loading]({{ site.baseurl }}/guides/rhinoscript/efficient_script_loading)

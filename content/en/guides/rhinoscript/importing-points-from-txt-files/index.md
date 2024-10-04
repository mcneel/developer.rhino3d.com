+++
aliases = ["/en/5/guides/rhinoscript/importing-points-from-txt-files/", "/en/6/guides/rhinoscript/importing-points-from-txt-files/", "/en/7/guides/rhinoscript/importing-points-from-txt-files/", "/wip/guides/rhinoscript/importing-points-from-txt-files/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide demonstration of how to open a text file and import data from it into Rhino using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Importing Points from Text Files"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/importingpointsfromtextfiles"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Overview

One common task performed by Rhino users is the importing of point coordinates from some kind of delimited file.  This task is easy if you use the Points File file type when opening or importing files.  But what if the file you are importing does not conform to the traditional delimited file notation.  Or, what if the file contains other information?

The key to understanding how to import data from a text is understanding the File System Object included as part of the Microsoft Scripting Runtime.  The File System Object simplifies the task of dealing with any type of file input or output and for dealing with the system file structure itself.

To access the File System Object model you must first create an instance of the `FileSystemObject` object, the only externally creatable object in the model.  For more information on the `FileSystemObject`, see [Microsoft's VBScript documentation on MSDN](https://msdn.microsoft.com/en-us/library/2z9ffy99(v=vs.84).aspx).

## Example

The following code example demonstrates how to import point coordinates from a text file. This can be easily modified to accommodate other information...

```vbnet
Option Explicit
'---------------------------------------------------------------
' Subroutine: ImportPoints
' Purpose:    Import points from a text file.
'---------------------------------------------------------------
Sub ImportPoints
  ' Prompt the user for a file to import
  Dim strFilter, strFileName
  strFilter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*|"
  strFileName = Rhino.OpenFileName("Open Point File", strFilter)
  If IsNull(strFileName) Then Exit Sub

  ' The the file system object
  Dim objFSO, objFile
  Set objFSO = CreateObject("Scripting.FileSystemObject")
  ' Try opening the text file
  On Error Resume Next
  Set objFile = objFSO.OpenTextFile(strFileName, 1)
  If Err Then
    MsgBox Err.Description
    Exit Sub
  End If

  Rhino.EnableRedraw False

  ' Read each line from the file
  Dim strLine, arrPoint
  Do While objFile.AtEndOfStream <> True
    strLine = objFile.ReadLine
    If Not IsNull(strLine) Then
      ' Remove any double-quote characters
      strLine = Replace(strLine, Chr(34), , 1)
      ' Convert the string to a 3D point
      arrPoint = Rhino.Str2Pt(strLine)
      ' Add the point to Rhino
      If IsArray(arrPoint) Then
        ' AddPoint will add a point object to Rhino
        Rhino.AddPoint arrPoint
      End If
    End If
  Loop

  Rhino.EnableRedraw True
  objFile.Close
  Set objFile = Nothing
  Set objFSO = Nothing
End Sub
```

## Related Topics

- [Microsoft's VBScript documentation on MSDN](https://msdn.microsoft.com/en-us/library/2z9ffy99(v=vs.84).aspx)

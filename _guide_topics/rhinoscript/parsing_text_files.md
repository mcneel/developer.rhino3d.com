---
layout: toc-guide-page
title: Parsing Text Files
author: dale@mcneel.com
categories: ['Miscellaneous', 'Intermediate']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['script', 'Rhino', 'vbscript']
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/parsetextfile
order: 1
---

# Parsing Text Files

This guide discusses how to convert data read from a text file into its proper data type in RhinoScript.

## Problem

A frequent workflow is using a text file - generated outside Rhino - to change a Rhino model.  You may know how to read in a text file and parse it with VBScript, but what about parsing the text file and assigning the values as a variable?

## Solution

Consider the following VBScript subroutine that reads a text file:

```vbnet
Sub ReadTextFile
  Dim objFSO, objFile, strFileName, strLine
  Const ForReading = 1

  strFileName = Rhino.OpenFileName("Open", "Text Files (*.txt)|*.txt|")
  If IsNull(strFileName) Then Exit Sub

  Set objFSO = CreateObject("Scripting.FileSystemObject")
  Set objFile = objFSO.OpenTextFile(strFileName, ForReading)

  While Not objFile.AtEndOfStream
    strLine = objFile.ReadLine
    Rhino.Print strLine
  Wend

  objFile.Close
  Set objFSO = Nothing

End Sub
```

Note how every line read from the text file is assigned to the `strLine` variable before it is printed.

Everything read from a text file using VBScript comes in as a string data type.  If you want something that you have read to be an integer or a floating point number, then you need to convert the string to that data type. For example, if you have a text file:

```
7
3.14159
Hello Rhino!
```

If you use VBScript to read this file, all three lines are read in as strings.  If you want line one read as an integer and line read as a double, then you can use some of VBScript's data conversion functions to convert the string to the proper data type.  For example:

```vbnet
Dim nFirst, dblSecond, strThird
nFirst    = CInt(objFile.ReadLine)
dblSecond = CDbl(objFile.ReadLine)
strThird  = objFile.ReadLine
```

**NOTE**: the above example does have the limitation that you have to know what kind of data is on each line. If you don't know what kind of data is on each line, then consider exporting a data type identifier along with the data from the program that generated the file.  This way, when you read a line from VBScript, you will know what kind of data you have.

VBScript's `VarType` function will return a value indicating the type of variable.  The possible values are:

| Type | | | |  Value | | | | Description |
|:--------|:-:|:-:|:-:|:-------:|:-:|:-:|:-:|:--------|
| `vbEmpty`   | | | | 0   | | | | Uninitialized (default)   |
| `vbNull`   | | | | 1   | | | | Contains no valid data   |
| `vbInteger`   | | | | 2   | | | | Integer subtype   |
| `vbLong`   | | | | 3   | | | | Long subtype   |
| `vbSingle`   | | | | 4   | | | | Single subtype   |
| `vbSingle`   | | | | 5   | | | | Double subtype   |
| `vbCurrency`   | | | | 6   | | | | Currency subtype   |
| `vbDate`   | | | | 7   | | | | Date subtype   |
| `vbString`   | | | | 8   | | | | String subtype   |
| `vbObject`   | | | | 9   | | | | Object   |
| `vbError`   | | | | 10   | | | | Error subtype   |
| `vbBoolean`   | | | | 11   | | | | Boolean subtype   |
| `vbVariant`   | | | | 12   | | | | Variant (used only for arrays of variants)   |
| `vbDataObject`   | | | | 13   | | | | Data access object   |
| `vbDecimal`   | | | | 14   | | | | Decimal subtype   |
| `vbByte`    | | | | 17   | | | | Byte subtype   |
| `vbArray`   | | | | 8192   | | | | Array   |
|=====
|
{: rules="groups"}


The text file above written to include the data's type identifier would look like this:

```
2;7
5;3.14159
8;Hello Rhino!
```

Now each line in the text file contains both the data type and the data.  Using VBScript's `Split` function, we can separate the data type from the data.  Then, it is just a matter of testing for the types of data that our script supports and then performing the proper data conversion.  For example:

```vbnet
Dim strLine, arrLine, nType, vaValue
strLine = objFile.ReadLine
arrLine = Split(strLine, ";")
nType = CInt(arrLine(0))
Select Case nType
  Case  2 vaValue = CInt(arrLine(1))
  Case  3 vaValue = CLng(arrLine(1))
  Case  4 vaValue = CSng(arrLine(1))
  Case  5 vaValue = CDbl(arrLine(1))
  Case  8 vaValue = arrLine(1)
  Case 11 vaValue = CBool(arrLine(1))
  Case Else Rhino.Print "Unsupported data type."
End Select
```

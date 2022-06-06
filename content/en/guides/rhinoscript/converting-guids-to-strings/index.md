+++
aliases = ["/5/guides/rhinoscript/converting-guids-to-strings/", "/6/guides/rhinoscript/converting-guids-to-strings/", "/7/guides/rhinoscript/converting-guids-to-strings/", "/wip/guides/rhinoscript/converting-guids-to-strings/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This guide demonstrates how convert an array of bytes containing a GUID to a string."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Converting GUIDs to Strings"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/guidtostring"
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

 
## Problem

If you have written a RhinoScript function which calls a method on a COM object that return an array of bytes with a GUID, you will likely want to convert this GUID into a string.  Converting GUIDs to strings is possible, but it takes a little work.

## Solution

The logical format of a GUID in memory is not in the same order as the bytes are in the string. A GUID stored in binary format in memory is a sixteen byte structure in the following format:

`DWORD-WORD-WORD-BYTE BYTE-BYTE BYTE BYTE BYTE BYTE BYTE`

Where a WORD consists of two bytes and a DWORD consists of four bytes.  They are stored in memory in order from the least to the most significant, or “little endian”, on Intel-based systems.  So, you need to make sure you decode the array in the correct order

The following example RhinoScript code demonstrates how to convert an array of bytes containing a GUID to a string.

```vbnet
' Returns single digit bytes, like 0, as "00", not "0"
Function HexByte(b)
  HexByte = Right("0" & Hex(b), 2)
End Function

' Converts a GUID to a string
Function GuidToString(ByteArray)
  Dim Binary, S
  Binary = CStr(ByteArray)
  ' Uncomment if you want opening paren
  ' S = "{"
  S = S & HexByte(AscB(MidB(Binary, 4, 1)))
  S = S & HexByte(AscB(MidB(Binary, 3, 1)))
  S = S & HexByte(AscB(MidB(Binary, 2, 1)))
  S = S & HexByte(AscB(MidB(Binary, 1, 1)))
  S = S & "-"  
  S = S & HexByte(AscB(MidB(Binary, 6, 1)))
  S = S & HexByte(AscB(MidB(Binary, 5, 1)))
  S = S & "-"  
  S = S & HexByte(AscB(MidB(Binary, 8, 1)))
  S = S & HexByte(AscB(MidB(Binary, 7, 1)))
  S = S & "-"  
  S = S & HexByte(AscB(MidB(Binary, 9, 1)))
  S = S & HexByte(AscB(MidB(Binary, 10, 1)))
  S = S & "-"  
  S = S & HexByte(AscB(MidB(Binary, 11, 1)))
  S = S & HexByte(AscB(MidB(Binary, 12, 1)))
  S = S & HexByte(AscB(MidB(Binary, 13, 1)))
  S = S & HexByte(AscB(MidB(Binary, 14, 1)))
  S = S & HexByte(AscB(MidB(Binary, 15, 1)))
  S = S & HexByte(AscB(MidB(Binary, 16, 1)))
  ' Uncomment if you want closing paren
  ' S = S & "}"
  GuidToString = S
End Function
```

## Related Topics

- [Creating GUIDs](/guides/rhinoscript/creating-guids)

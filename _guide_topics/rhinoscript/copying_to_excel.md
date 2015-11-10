---
layout: toc-guide-page
title: Copying to Excel
author: dale@mcneel.com
categories: ['Miscellaneous']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['RhinoScript']
keywords: ['script', 'Rhino', 'vbscript']
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/copytoexcel
order: 1
---

# Copying to Excel

This guide demonstrates how to copy from Rhino and paste into Microsoft Excel using RhinoScript.

## Overview

You can copy information from Rhino and then paste it into Excel.  The real question is "what do you want to copy and paste?"

Copying information from Rhino and pasting it into Excel is fairly easy using RhinoScript.  All you have to do is use the `ClipboardText` method to copy a text string into the Windows Clipboard.  Then from Excel, just select the cell and paste.

## Details

If you want to copy the string “Hello from Rhino!” into Excel, your script could be as simple as this:

```vbnet
Call Rhino.ClipboardText("Hello from Rhino!")
```

Easy enough. But, what if you want to copy some delimited data so each "token" appears in a different column in Excel when pasted. Then, simply separate each token with a tab, or `vbTab`, character. For example:

```vbnet
Call Rhino.ClipboardText("A" & vbTab & "B" & vbTab & "C" & vbTab & "1" & vbTab & "2" & vbTab & "3")
```

Likewise, if you want to copy some delimited data so each "token" appears in a different row in Excel when pasted, then separate each token with a line-feed, or `vbLf`, character. For example:

```vbnet
Call Rhino.ClipboardText("A" & vbLf & "B" & vbLf & "C" & vbLf & "1" & vbLf & "2" & vbLf & "3")
```

You can get more elaborate by creating a formatted string that contains both tab and line-feed characters. In this example, we will copy something useful - curve lengths in this example...

```vbnet
Sub CopyClipCrvLength()
  Dim curves, crv, length, str
  curves = Rhino.GetObjects("Select curves to copy length", 4, True, True)
  If IsArray(curves) Then
    str = str & "Id" & vbTab & "Length" & vbLf
    For Each crv In curves
      length = Rhino.CurveLength(crv)
      str = str & crv & vbTab & CStr(length) & vbLf
    Next
    Call Rhino.ClipboardText(str)
  End If    
End Sub
```

Now that you have the basic idea, you should be able to write your own scripts that copy any type of data you want from Rhino into Excel.

---

## Related Topics

- [Reading Excel Files]({{ site.baseurl }}/guides/rhinoscript/reading_excel_files)
- Automating Excel From RhinoScript (Sample)
- Automating Curve Properties to Excel From RhinoScript (Sample)
- Exporting Point Coordinates to Excel (Sample)

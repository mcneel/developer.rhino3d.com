+++
aliases = ["/en/5/guides/rhinoscript/read-write-utf8/", "/en/6/guides/rhinoscript/read-write-utf8/", "/en/7/guides/rhinoscript/read-write-utf8/", "/wip/guides/rhinoscript/read-write-utf8/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This brief guide demonstrates how to read and write UTF-8 encoded text files using VBScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Read & Write UTF-8 Files"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/readutf8"
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

If you have a text file saved as UTF-8, sometimes - when you read the file - it reads in weird characters and not the correct characters.  This happens often when the files contain Chinese characters.  How can you make it read the correct characters?


## Solution

The [File System Object](http://msdn.microsoft.com/en-us/library/aa242706(v=vs.60).aspx), generally used by VBScript developers to read and write text files, can read only ASCII or Unicode text files. You cannot use it to read or write UTF-8 encoded text files.

But, if you can use [Microsoft ActiveX Data Objects (ADO)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms676526%28v=vs.85%29.aspx), you can read UTF-8 encoded text files like this:

```vbnet
Dim objStream, strData
Set objStream = CreateObject("ADODB.Stream")
objStream.CharSet = "utf-8"
objStream.Open
objStream.LoadFromFile("C:\Users\admin\Desktop\test.txt")
strData = objStream.ReadText()
```

If you want to write a UTF-8 encode text file, you can do so like this:

```vbnet
Dim objStream
Set objStream = CreateObject("ADODB.Stream")
objStream.CharSet = "utf-8"
objStream.Open
objStream.WriteText "The data I want in utf-8"
objStream.SaveToFile "C:\Users\admin\Desktop\test.txt", 2
```

## Related Topics

- [File System Object on MSDN](http://msdn.microsoft.com/en-us/library/aa242706(v=vs.60).aspx)
- [Microsoft ActiveX Data Objects (ADO) on MSDN](http://msdn.microsoft.com/en-us/library/windows/desktop/ms676526%28v=vs.85%29.aspx)

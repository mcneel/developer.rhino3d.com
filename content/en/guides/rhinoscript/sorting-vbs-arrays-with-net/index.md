+++
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide demonstrates how to use the .NET Framework to sort arrays in RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Sorting VBS Arrays with .NET"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/dotnetsort"
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

One of the big limitations in VBScript is that there is no easy way to sort a list of items.  To put a list in alphabetical order requires you to either use the pre-canned RhinoScript methods, such as `SortNumbers`, `SortPoints` or `SortStrings`, or write a sorting function of your own, like the following bubble sort code:

```vbnet
For i = (UBound(arrNames) - 1) to 0 Step -1
  For j= 0 to i
    If UCase(arrNames(j)) >
      UCase(arrNames(j+1)) Then
        strHolder = arrNames(j+1)
        arrNames(j+1) = arrNames(j)
        arrNames(j) = strHolder
    End If
  Next
Next
```

## Discussion

There is another option and that is to use the .NET Framework to help.  The majority of .NET Framework classes are unusable in VBScript.  However, there are a large number of .NET classes that have COM-callable wrappers. T his means these classes include a COM interface enabling them to be accessed from VBScript.

For example, consider the following script:

```vbnet
Set DataList = CreateObject("System.Collections.ArrayList")
DataList.Add "B"
DataList.Add "C"
DataList.Add "E"
DataList.Add "D"
DataList.Add "A"
DataList.Sort()
For Each strItem in DataList
  Rhino.Print strItem
Next
```

Notice that we have created an instance of the .NET Framework class `System.Collections.ArrayList`.  We then use the `Add` method to add five items to the list.  To sort the list, all we need to do is call the `ArrayList`'s `Sort` method.

Now, what if you really wanted those values in descending order?  In this case, just call `ArrayList`'s `Sort` method after calling the `Sort` method.

```vbnet
Set DataList = CreateObject("System.Collections.ArrayList")
DataList.Add "B"
DataList.Add "C"
DataList.Add "E"
DataList.Add "D"
DataList.Add "A"
DataList.Sort()
DataList.Reverse()
For Each strItem in DataList
  Rhino.Print strItem
Next
```

Also, have you ever tried to remove an item from a VBScript array?  It is not easy.  But, with the .NET Framework's `ArrayList`, you just need to call the `Remove` method. The following script, an `ArrayList`, sorts it, and then removes the entry for `D`...

```vbnet
Set DataList = CreateObject("System.Collections.ArrayList")
DataList.Add "B"
DataList.Add "C"
DataList.Add "E"
DataList.Add "D"
DataList.Add "A"
DataList.Sort()
DataList.Remove("D")
For Each strItem in DataList
  Rhino.Print strItem
Next
```

Copying items VBScript arrays and an `ArrayList` is just as easy.  In the following script, an `ArrayList` is used to sort a list of layer names...

```vbnet
LayerNames = Rhino.LayerNames
Set DataList = CreateObject("System.Collections.ArrayList")
For i = 0 To UBound(LayerNames)
  DataList.Add LayerNames(i)
Next
DataList.Sort()
For i = 0 To UBound(LayerNames)
  LayerNames(i) = DataList(i)
Next
Layer = Rhino.ListBox(LayerNames, "Layer to set current")
```

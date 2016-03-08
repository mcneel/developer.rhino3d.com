---
title: Disconnected Recordset Sorting
description: This guide demonstrates using a disconnected recordset to sort data.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/recordsets
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# Disconnected Recordset Sorting

{{ page.description }}

## Overview

If you are dealing with data which requires more than just key-value pairs and fits best in 2-D array, and you wanted to perform sorting and filtering on it, then Disconnected Recordsets will be an excellent option.

A disconnected recordset is essentially a database that exists only in memory; it is not tied to a physical database.  You create the recordset, add records to it, and then manipulate the data, just like any other recordset.  The only difference is that the moment the script terminates, the recordset, which is stored only in memory, disappears as well.

To use a disconnected recordset to sort data, you must first create the recordset, adding any fields needed to store the data. After you have created the fields, you then use the `AddNew` method to add new records to the recordset, using the same process used to add new records to a physical database.  After the recordset has been populated, a single line of code can then `Sort` the data on the specified field or fields.

## Example

The following example demonstrates how to sort an array of 3D points in ascending x, y, z order. The code can be quickly modified to sort the point in any order by simply modifying the `Sort` statement...

```vbnet
Sub SortPoints

  ' Local constants
  Const adDouble = 5

  ' Local variables
  Dim arrPoints, arrPoint, x, y, z
  Dim objRecordSet

  ' Get the coordinates of selected point objects
  arrPoints = Rhino.GetPointCoordinates
  If IsNull(arrPoints) Then Exit Sub

  ' Create a disconnected recordset object
  Set objRecordSet = CreateObject("ADODB.Recordset")

  ' Define the fields of the recordset
  Call objRecordSet.Fields.Append("X", adDouble)
  Call objRecordSet.Fields.Append("Y", adDouble)
  Call objRecordSet.Fields.Append("Z", adDouble)

  ' Open the recordset
  objRecordSet.Open

  ' Add the curve data to the recordset
  For Each arrPoint In arrPoints
    objRecordSet.AddNew
    objRecordSet("X").Value = arrPoint(0)
    objRecordSet("Y").Value = arrPoint(1)
    objRecordSet("Z").Value = arrPoint(2)
    objRecordSet.Update
  Next

  ' Sort the recordset by x,y,z in ascending order
  objRecordSet.Sort = "X ASC, Y ASC, Z ASC"

  ' Iterate through the sorted recordset and print each record's values
  objRecordSet.MoveFirst
  Do Until objRecordSet.EOF
    x = objRecordSet("X").Value
    y = objRecordSet("Y").Value
    z = objRecordSet("Z").Value
    Call Rhino.Print(Rhino.Pt2Str(Array(x, y, z)))
    objRecordSet.MoveNext
  Loop

  objRecordSet.Close

End Sub
```

---

## Related Topics

- [Recordset Object (ADO) on MSDN](http://msdn.microsoft.com/en-us/library/windows/desktop/ms681510(v=vs.85).aspx)
- [Use a disconnected recordset to sort large data sets in VBScript on Microsoft Technet](http://technet.microsoft.com/en-us/magazine/2008.09.heyscriptingguy.aspx?pr=PuzzleAnswer)
- [How Can I Delete a Record From a Disconnected Recordset? on Microsoft Technet](http://blogs.technet.com/b/heyscriptingguy/archive/2006/10/11/how-can-i-delete-a-record-from-a-disconnected-recordset.aspx)

---
title: Duplicate Object
description: Demonstrates how to clone (or copy, or duplicate) a Rhino object.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/duplicateobject
order: 1
keywords: ['clone', 'copy,', 'duplicate', 'rhino', 'object']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result DuplicateObject(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select object to duplicate", false, ObjectType.AnyObject, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var rhino_object = obj_ref.Object();

    var geometry_base = rhino_object.DuplicateGeometry();
    if (geometry_base != null)
      if (doc.Objects.Add(geometry_base) != Guid.Empty)
        doc.Views.Redraw();

    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function DuplicateObject(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select object to duplicate", False, ObjectType.AnyObject, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim rhino_object = obj_ref.Object()

	Dim geometry_base = rhino_object.DuplicateGeometry()
	If geometry_base IsNot Nothing Then
	  If doc.Objects.Add(geometry_base) <> Guid.Empty Then
		doc.Views.Redraw()
	  End If
	End If

	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from System import *
from Rhino import *
from Rhino.Commands import *
from Rhino.DocObjects import *
from Rhino.Input import *
from scriptcontext import doc

def RunCommand():

    rc, obj_ref = RhinoGet.GetOneObject("Select object to duplicate", False, ObjectType.AnyObject)
    if rc != Result.Success:
        return rc
    rhino_object = obj_ref.Object()

    geometry_base = rhino_object.DuplicateGeometry()
    if geometry_base != None:
        if doc.Objects.Add(geometry_base) != Guid.Empty:
            doc.Views.Redraw()

    return Result.Success

if __name__ == "__main__":
    RunCommand()
```
{: #py .tab-pane .fade .in}

---
layout: code-sample
title: Modify an Object's Name
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['modify', 'objects', 'name']
order: 125
description:  
---



```cs
public class ObjectNameCommand : Command
{
  public override string EnglishName { get { return "csRenameObject"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select object to change name", true, ObjectType.AnyObject, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var rhino_object = obj_ref.Object();

    var new_object_name = "";
    rc = RhinoGet.GetString("New object name", true, ref new_object_name);
    if (rc != Result.Success)
      return rc;
    if (string.IsNullOrWhiteSpace(new_object_name))
      return Result.Nothing;

    if (rhino_object.Name != new_object_name)
    {
      rhino_object.Attributes.Name = new_object_name;
      rhino_object.CommitChanges();
    }

    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class ObjectNameCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbRenameObject"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim obj_ref As ObjRef = Nothing
    Dim rc = RhinoGet.GetOneObject("Select object to change name", True, ObjectType.AnyObject, obj_ref)
    If rc <> Result.Success Then
      Return rc
    End If
    Dim rhino_object = obj_ref.Object()

    Dim new_object_name = ""
    rc = RhinoGet.GetString("New object name", True, new_object_name)
    If rc <> Result.Success Then
      Return rc
    End If
    If String.IsNullOrWhiteSpace(new_object_name) Then
      Return Result.Nothing
    End If

    If rhino_object.Name <> new_object_name Then
      rhino_object.Attributes.Name = new_object_name
      rhino_object.CommitChanges()
    End If

    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs

obj_id = rs.GetObject("Select object to change name")
object_new_name = rs.GetString("New object name")

rs.ObjectName(obj_id, object_new_name)
```
{: #py .tab-pane .fade .in}



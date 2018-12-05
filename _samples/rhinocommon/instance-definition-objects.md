---
title: Instance Definition Objects
description: Demonstrates how to print (or list) the objects that make up a block definition.
authors: ['steve_baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Blocks']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/instancedefinitionobjects
order: 1
keywords: ['list', 'block', 'definition', 'geometry']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result InstanceDefinitionObjects(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select instance", false, Rhino.DocObjects.ObjectType.InstanceReference, out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    var iref = objref.Object() as Rhino.DocObjects.InstanceObject;
    if (iref != null)
    {
      var idef = iref.InstanceDefinition;
      if (idef != null)
      {
        var rhino_objects = idef.GetObjects();
        for (int i = 0; i < rhino_objects.Length; i++)
          Rhino.RhinoApp.WriteLine("Object {0} = {1}", i, rhino_objects[i].Id);
      }
    }
    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function InstanceDefinitionObjects(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select instance", False, Rhino.DocObjects.ObjectType.InstanceReference, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim iref = TryCast(objref.Object(), Rhino.DocObjects.InstanceObject)
	If iref IsNot Nothing Then
	  Dim idef = iref.InstanceDefinition
	  If idef IsNot Nothing Then
		Dim rhino_objects = idef.GetObjects()
		For i As Integer = 0 To rhino_objects.Length - 1
		  Rhino.RhinoApp.WriteLine("Object {0} = {1}", i, rhino_objects(i).Id)
		Next i
	  End If
	End If
	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext

def InstanceDefinitionObjects():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select instance", False, Rhino.DocObjects.ObjectType.InstanceReference)
    if rc != Rhino.Commands.Result.Success: return

    iref = objref.Object()
    if iref:
        idef = iref.InstanceDefinition
        if idef:
            rhino_objects = idef.GetObjects()
            for i, rhobj in enumerate(rhino_objects):
                print "Object", i, "=", rhobj.Id

if __name__=="__main__":
    InstanceDefinitionObjects()
```
{: #py .tab-pane .fade .in}

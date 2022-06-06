+++
aliases = ["/5/samples/rhinocommon/instance-definition-objects/", "/6/samples/rhinocommon/instance-definition-objects/", "/7/samples/rhinocommon/instance-definition-objects/", "/wip/samples/rhinocommon/instance-definition-objects/"]
authors = [ "steve" ]
categories = [ "Blocks" ]
description = "Demonstrates how to print (or list) the objects that make up a block definition."
keywords = [ "list", "block", "definition", "geometry" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Instance Definition Objects"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/instancedefinitionobjects"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

<div class="codetab-content" id="cs">

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

</div>


<div class="codetab-content" id="vb">

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

</div>


<div class="codetab-content" id="py">

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

</div>

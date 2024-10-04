+++
aliases = ["/en/5/samples/rhinocommon/determine-object-layer/", "/en/6/samples/rhinocommon/determine-object-layer/", "/en/7/samples/rhinocommon/determine-object-layer/", "/wip/samples/rhinocommon/determine-object-layer/"]
authors = [ "steve" ]
categories = [ "Adding Objects", "Layers" ]
description = "Demonstrates how to determine which layer a user-specified object is on and print the name."
keywords = [ "determine", "objects", "layer" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Determine Object Layer"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/objectlayer"
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
  public static Rhino.Commands.Result DetermineObjectLayer(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef obref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select object", true, Rhino.DocObjects.ObjectType.AnyObject, out obref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;
    Rhino.DocObjects.RhinoObject rhobj = obref.Object();
    if (rhobj == null)
      return Rhino.Commands.Result.Failure;
    int index = rhobj.Attributes.LayerIndex;
    string name = doc.Layers[index].Name;
    Rhino.RhinoApp.WriteLine("The selected object's layer is '{0}'", name);
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function DetermineObjectLayer(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim obref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select object", True, Rhino.DocObjects.ObjectType.AnyObject, obref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If
	Dim rhobj As Rhino.DocObjects.RhinoObject = obref.Object()
	If rhobj Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If
	Dim index As Integer = rhobj.Attributes.LayerIndex
	Dim name As String = doc.Layers(index).Name
	Rhino.RhinoApp.WriteLine("The selected object's layer is '{0}'", name)
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Guid

def DetermineObjectLayer():
    rc, obref = Rhino.Input.RhinoGet.GetOneObject("Select object", True, Rhino.DocObjects.ObjectType.AnyObject)
    if rc!=Rhino.Commands.Result.Success: return rc
    rhobj = obref.Object()
    if rhobj is None: return Rhino.Commands.Result.Failure
    index = rhobj.Attributes.LayerIndex
    name = scriptcontext.doc.Layers[index].Name
    print "The selected object's layer is '", name, "'"
    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    DetermineObjectLayer()
```

</div>

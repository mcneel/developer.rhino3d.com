+++
authors = [ "steve" ]
categories = [ "Blocks", "Layers" ]
description = "Demonstrates how to lock a user-specified layer."
keywords = [ "lock", "layer" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Lock Layer"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/locklayer"
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
  public static Result LockLayer(RhinoDoc doc)
  {
    string layer_name = "";
    var rc = RhinoGet.GetString("Name of layer to lock", true, ref layer_name);
    if (rc != Result.Success)
      return rc;
    if (String.IsNullOrWhiteSpace(layer_name))
      return Result.Nothing;

    // because of sublayers it's possible that mone than one layer has the same name
    // so simply calling doc.Layers.Find(layerName) isn't good enough.  If "layerName" returns
    // more than one layer then present them to the user and let him decide.
    var matching_layers = (from layer in doc.Layers
                           where layer.Name == layer_name
                           select layer).ToList<Rhino.DocObjects.Layer>();

    Rhino.DocObjects.Layer layer_to_lock = null;
    if (matching_layers.Count == 0)
    {
      RhinoApp.WriteLine("Layer \"{0}\" does not exist.", layer_name);
      return Result.Nothing;
    }
    else if (matching_layers.Count == 1)
    {
      layer_to_lock = matching_layers[0];
    }
    else if (matching_layers.Count > 1)
    {
      for (int i = 0; i < matching_layers.Count; i++)
      {
        RhinoApp.WriteLine("({0}) {1}", i+1, matching_layers[i].FullPath.Replace("::", "->"));
      }
      int selected_layer = -1;
      rc = RhinoGet.GetInteger("which layer?", true, ref selected_layer);
      if (rc != Result.Success)
        return rc;
      if (selected_layer > 0 && selected_layer <= matching_layers.Count)
        layer_to_lock = matching_layers[selected_layer - 1];
      else return Result.Nothing;
    }

    if (layer_to_lock == null)
      return Result.Nothing;

    if (!layer_to_lock.IsLocked)
    {
      layer_to_lock.IsLocked = true;
      layer_to_lock.CommitChanges();
      return Result.Success;
    }
    else
    {
      RhinoApp.WriteLine("layer {0} is already locked.", layer_to_lock.FullPath);
      return Result.Nothing;
    }
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function LockLayer(ByVal doc As RhinoDoc) As Result
	Dim layer_name As String = ""
	Dim rc = RhinoGet.GetString("Name of layer to lock", True, layer_name)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	If String.IsNullOrWhiteSpace(layer_name) Then
	  Return Result.Nothing
	End If

	' because of sublayers it's possible that mone than one layer has the same name
	' so simply calling doc.Layers.Find(layerName) isn't good enough.  If "layerName" returns
	' more than one layer then present them to the user and let him decide.
	Dim matching_layers = (
	    From layer In doc.Layers
	    Where layer.Name = layer_name
	    Select layer).ToList()

	Dim layer_to_lock As Rhino.DocObjects.Layer = Nothing
	If matching_layers.Count = 0 Then
	  RhinoApp.WriteLine("Layer ""{0}"" does not exist.", layer_name)
	  Return Result.Nothing
	ElseIf matching_layers.Count = 1 Then
	  layer_to_lock = matching_layers(0)
	ElseIf matching_layers.Count > 1 Then
	  For i As Integer = 0 To matching_layers.Count - 1
		RhinoApp.WriteLine("({0}) {1}", i+1, matching_layers(i).FullPath.Replace("::", "->"))
	  Next i
	  Dim selected_layer As Integer = -1
	  rc = RhinoGet.GetInteger("which layer?", True, selected_layer)
	  If rc IsNot Result.Success Then
		Return rc
	  End If
	  If selected_layer > 0 AndAlso selected_layer <= matching_layers.Count Then
		layer_to_lock = matching_layers(selected_layer - 1)
	  Else
		  Return Result.Nothing
	  End If
	End If

	If layer_to_lock Is Nothing Then
	  Return Result.Nothing
	End If

	If Not layer_to_lock.IsLocked Then
	  layer_to_lock.IsLocked = True
	  layer_to_lock.CommitChanges()
	  Return Result.Success
	Else
	  RhinoApp.WriteLine("layer {0} is already locked.", layer_to_lock.FullPath)
	  Return Result.Nothing
	End If
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs
from scriptcontext import doc

def lock():
    layerName = rs.GetString("Name of layer to lock")

    matchingLayers = [layer for layer in doc.Layers if layer.Name == layerName]

    layerToLock = None
    if len(matchingLayers) == 0:
        print "Layer \"{0}\" does not exist.".format(layerName)
    elif len(matchingLayers) == 1:
        layerToLock = matchingLayers[0]
    elif len(matchingLayers) > 1:
        i = 0;
        for layer in matchingLayers:
            print "({0}) {1}".format(i+1, matchingLayers[i].FullPath.replace("::", "->"))
            i += 1

        selectedLayer = rs.GetInteger("which layer?", -1, 1, len(matchingLayers))
        if selectedLayer == None:
            return
        layerToLock = matchingLayers[selectedLayer - 1]

    if layerToLock.IsLocked:
        print "layer {0} is already locked.".format(layerToLock.FullPath)
    else:
        layerToLock.IsLocked = True
        layerToLock.CommitChanges()

if __name__ == "__main__":
    lock()
```

</div>

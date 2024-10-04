+++
aliases = ["/en/5/samples/rhinocommon/add-child-layer/", "/en/6/samples/rhinocommon/add-child-layer/", "/en/7/samples/rhinocommon/add-child-layer/", "/wip/samples/rhinocommon/add-child-layer/"]
authors = [ "steve" ]
categories = [ "Adding Objects", "Layers" ]
description = "Demonstrates how to add a child (or sub) layer to a parent layer in a Rhino model."
keywords = [ "add", "child", "layer" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Child Layer"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addchildlayer"
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
  public static Rhino.Commands.Result AddChildLayer(Rhino.RhinoDoc doc)
  {
    // Get an existing layer
    string default_name = doc.Layers.CurrentLayer.Name;

    // Prompt the user to enter a layer name
    Rhino.Input.Custom.GetString gs = new Rhino.Input.Custom.GetString();
    gs.SetCommandPrompt("Name of existing layer");
    gs.SetDefaultString(default_name);
    gs.AcceptNothing(true);
    gs.Get();
    if (gs.CommandResult() != Rhino.Commands.Result.Success)
      return gs.CommandResult();

    // Was a layer named entered?
    string layer_name = gs.StringResult().Trim();
    int index = doc.Layers.Find(layer_name, true);
    if (index<0)
      return Rhino.Commands.Result.Cancel;

    Rhino.DocObjects.Layer parent_layer = doc.Layers[index];

    // Create a child layer
    string child_name = parent_layer.Name + "_child";
    Rhino.DocObjects.Layer childlayer = new Rhino.DocObjects.Layer();
    childlayer.ParentLayerId = parent_layer.Id;
    childlayer.Name = child_name;
    childlayer.Color = System.Drawing.Color.Red;

    index = doc.Layers.Add(childlayer);
    if (index < 0)
    {
      Rhino.RhinoApp.WriteLine("Unable to add {0} layer.", child_name);
      return Rhino.Commands.Result.Failure;
    }
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddChildLayer(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	' Get an existing layer
	Dim default_name As String = doc.Layers.CurrentLayer.Name

	' Prompt the user to enter a layer name
	Dim gs As New Rhino.Input.Custom.GetString()
	gs.SetCommandPrompt("Name of existing layer")
	gs.SetDefaultString(default_name)
	gs.AcceptNothing(True)
	gs.Get()
	If gs.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gs.CommandResult()
	End If

	' Was a layer named entered?
	Dim layer_name As String = gs.StringResult().Trim()
	Dim index As Integer = doc.Layers.Find(layer_name, True)
	If index<0 Then
	  Return Rhino.Commands.Result.Cancel
	End If

	Dim parent_layer As Rhino.DocObjects.Layer = doc.Layers(index)

	' Create a child layer
	Dim child_name As String = parent_layer.Name & "_child"
	Dim childlayer As New Rhino.DocObjects.Layer()
	childlayer.ParentLayerId = parent_layer.Id
	childlayer.Name = child_name
	childlayer.Color = System.Drawing.Color.Red

	index = doc.Layers.Add(childlayer)
	If index < 0 Then
	  Rhino.RhinoApp.WriteLine("Unable to add {0} layer.", child_name)
	  Return Rhino.Commands.Result.Failure
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
import System.Drawing.Color

def AddChildLayer():
    # Get an existing layer
    default_name = scriptcontext.doc.Layers.CurrentLayer.Name
    # Prompt the user to enter a layer name
    gs = Rhino.Input.Custom.GetString()
    gs.SetCommandPrompt("Name of existing layer")
    gs.SetDefaultString(default_name)
    gs.AcceptNothing(True)
    gs.Get()
    if gs.CommandResult()!=Rhino.Commands.Result.Success:
        return gs.CommandResult()

    # Was a layer named entered?
    layer_name = gs.StringResult().Trim()
    index = scriptcontext.doc.Layers.Find(layer_name, True)
    if index<0: return Rhino.Commands.Result.Cancel

    parent_layer = scriptcontext.doc.Layers[index]

    # Create a child layer
    child_name = parent_layer.Name + "_child"
    childlayer = Rhino.DocObjects.Layer()
    childlayer.ParentLayerId = parent_layer.Id
    childlayer.Name = child_name
    childlayer.Color = System.Drawing.Color.Red

    index = scriptcontext.doc.Layers.Add(childlayer)
    if index<0:
        print "Unable to add", child_name, "layer."
        return Rhino.Commands.Result.Failure
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    AddChildLayer()
```

</div>

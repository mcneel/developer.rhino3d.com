+++
aliases = ["/en/5/samples/rhinocommon/add-layer/", "/en/6/samples/rhinocommon/add-layer/", "/en/7/samples/rhinocommon/add-layer/", "/en/wip/samples/rhinocommon/add-layer/"]
authors = [ "steve" ]
categories = [ "Adding Objects", "Layers" ]
description = "Demonstrates how to add a layer to a Rhino model and validate that it does not already exist."
keywords = [ "add", "layer" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Add Layer"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addlayer"
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
  public static Rhino.Commands.Result AddLayer(Rhino.RhinoDoc doc)
  {
    // Cook up an unused layer name
    string unused_name = doc.Layers.GetUnusedLayerName(false);

    // Prompt the user to enter a layer name
    Rhino.Input.Custom.GetString gs = new Rhino.Input.Custom.GetString();
    gs.SetCommandPrompt("Name of layer to add");
    gs.SetDefaultString(unused_name);
    gs.AcceptNothing(true);
    gs.Get();
    if (gs.CommandResult() != Rhino.Commands.Result.Success)
      return gs.CommandResult();

    // Was a layer named entered?
    string layer_name = gs.StringResult().Trim();
    if (string.IsNullOrEmpty(layer_name))
    {
      Rhino.RhinoApp.WriteLine("Layer name cannot be blank.");
      return Rhino.Commands.Result.Cancel;
    }

    // Is the layer name valid?
    if (!Rhino.DocObjects.Layer.IsValidName(layer_name))
    {
      Rhino.RhinoApp.WriteLine(layer_name + " is not a valid layer name.");
      return Rhino.Commands.Result.Cancel;
    }

    // Does a layer with the same name already exist?
    int layer_index = doc.Layers.Find(layer_name, true);
    if (layer_index >= 0)
    {
      Rhino.RhinoApp.WriteLine("A layer with the name {0} already exists.", layer_name);
      return Rhino.Commands.Result.Cancel;
    }

    // Add a new layer to the document
    layer_index = doc.Layers.Add(layer_name, System.Drawing.Color.Black);
    if (layer_index < 0)
    {
      Rhino.RhinoApp.WriteLine("Unable to add {0} layer.", layer_name);
      return Rhino.Commands.Result.Failure;
    }
    return Rhino.Commands.Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Drawing

def AddLayer():
    # Cook up an unused layer name
    unused_name = scriptcontext.doc.Layers.GetUnusedLayerName(False)

    # Prompt the user to enter a layer name
    gs = Rhino.Input.Custom.GetString()
    gs.SetCommandPrompt("Name of layer to add")
    gs.SetDefaultString(unused_name)
    gs.AcceptNothing(True)
    gs.Get()
    if gs.CommandResult()!=Rhino.Commands.Result.Success:
        return gs.CommandResult()

    # Was a layer named entered?
    layer_name = gs.StringResult().strip()
    if not layer_name:
        print("Layer name cannot be blank.")
        return Rhino.Commands.Result.Cancel

    # Is the layer name valid?
    if not Rhino.DocObjects.Layer.IsValidName(layer_name):
        print(layer_name, "is not a valid layer name.")
        return Rhino.Commands.Result.Cancel

    # Does a layer with the same name already exist?
    layer_index = scriptcontext.doc.Layers.FindByFullPath(layer_name, -1)
    if layer_index>=0:
        print("A layer with the name", layer_name, "already exists.")
        return Rhino.Commands.Result.Cancel

    # Add a new layer to the document
    layer_index = scriptcontext.doc.Layers.Add(layer_name, System.Drawing.Color.Black)
    if layer_index<0:
        print("Unable to add", layer_name, "layer.")
        return Rhino.Commands.Result.Failure

    return Rhino.Commands.Result.Success

if __name__=="__main__":
    AddLayer()
```

</div>

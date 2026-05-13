+++
aliases = ["/en/5/samples/rhinocommon/object-display-mode/", "/en/6/samples/rhinocommon/object-display-mode/", "/en/7/samples/rhinocommon/object-display-mode/", "/en/wip/samples/rhinocommon/object-display-mode/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to set the object display mode of a user-specified mesh or surface."
keywords = [ "object", "display", "mode" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Object Display Mode"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/objectdisplaymode"
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
  public static Rhino.Commands.Result ObjectDisplayMode(Rhino.RhinoDoc doc)
  {
    const ObjectType filter = ObjectType.Mesh | ObjectType.Brep;
    ObjRef objref;
    Result rc = Rhino.Input.RhinoGet.GetOneObject("Select mesh or surface", true, filter, out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;
    Guid viewportId = doc.Views.ActiveView.ActiveViewportID;

    ObjectAttributes attr = objref.Object().Attributes;
    if (attr.HasDisplayModeOverride(viewportId))
    {
      RhinoApp.WriteLine("Removing display mode override from object");
      attr.RemoveDisplayModeOverride(viewportId);
    }
    else
    {
      Rhino.Display.DisplayModeDescription[] modes = Rhino.Display.DisplayModeDescription.GetDisplayModes();
      Rhino.Display.DisplayModeDescription mode = null;
      if (modes.Length == 1)
        mode = modes[0];
      else
      {
        Rhino.Input.Custom.GetOption go = new Rhino.Input.Custom.GetOption();
        go.SetCommandPrompt("Select display mode");
        string[] str_modes = new string[modes.Length];
        for (int i = 0; i < modes.Length; i++)
          str_modes[i] = modes[i].EnglishName.Replace(" ", "").Replace("-", "");
        go.AddOptionList("DisplayMode", str_modes, 0);
        if (go.Get() == Rhino.Input.GetResult.Option)
          mode = modes[go.Option().CurrentListOptionIndex];
      }
      if (mode == null)
        return Rhino.Commands.Result.Cancel;
      attr.SetDisplayModeOverride(mode, viewportId);
    }
    doc.Objects.ModifyAttributes(objref, attr, false);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def ObjectDisplayMode():
    filter = Rhino.DocObjects.ObjectType.Brep | Rhino.DocObjects.ObjectType.Mesh
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select mesh or surface", True, filter)
    if rc != Rhino.Commands.Result.Success: return rc;
    viewportId = scriptcontext.doc.Views.ActiveView.ActiveViewportID

    attr = objref.Object().Attributes
    if attr.HasDisplayModeOverride(viewportId):
        print "Removing display mode override from object"
        attr.RemoveDisplayModeOverride(viewportId)
    else:
        modes = Rhino.Display.DisplayModeDescription.GetDisplayModes()
        mode = None
        if len(modes) == 1:
            mode = modes[0]
        else:
            go = Rhino.Input.Custom.GetOption()
            go.SetCommandPrompt("Select display mode")
            str_modes = []
            for m in modes:
                s = m.EnglishName.replace(" ","").replace("-","")
                str_modes.append(s)
            go.AddOptionList("DisplayMode", str_modes, 0)
            if go.Get()==Rhino.Input.GetResult.Option:
                mode = modes[go.Option().CurrentListOptionIndex]
        if not mode: return Rhino.Commands.Result.Cancel
        attr.SetDisplayModeOverride(mode, viewportId)
    scriptcontext.doc.Objects.ModifyAttributes(objref, attr, False)
    scriptcontext.doc.Views.Redraw()

if __name__=="__main__":
    ObjectDisplayMode()
```

</div>

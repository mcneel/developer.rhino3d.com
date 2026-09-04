+++
aliases = ["/en/5/samples/rhinocommon/custom-undo/", "/en/6/samples/rhinocommon/custom-undo/", "/en/7/samples/rhinocommon/custom-undo/", "/en/wip/samples/rhinocommon/custom-undo/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to set up a custom set of actions when the Undo command is called."
keywords = [ "custom", "undo" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Custom Undo"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/customundo"
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
  static double MyFavoriteNumber = 0;

  public static Rhino.Commands.Result CustomUndo(RhinoDoc doc)
  {
    // Rhino automatically sets up an undo record when a command is run,
    // but... the undo record is not saved if nothing changes in the
    // document (objects added/deleted, layers changed,...)
    //
    // If we have a command that doesn't change things in the document,
    // but we want to have our own custom undo called then we need to do
    // a little extra work

    double d = MyFavoriteNumber;
    if (Rhino.Input.RhinoGet.GetNumber("Favorite number", true, ref d) == Rhino.Commands.Result.Success)
    {
      double current_value = MyFavoriteNumber;
      doc.AddCustomUndoEvent("Favorite Number", OnUndoFavoriteNumber, current_value);
      MyFavoriteNumber = d;
    }
    return Rhino.Commands.Result.Success;
  }

  // event handler for custom undo
  static void OnUndoFavoriteNumber(object sender, Rhino.Commands.CustomUndoEventArgs e)
  {
    // !!!!!!!!!!
    // NEVER change any setting in the Rhino document or application.  Rhino
    // handles ALL changes to the application and document and you will break
    // the Undo/Redo commands if you make any changes to the application or
    // document. This is meant only for your own private plugin data
    // !!!!!!!!!!

    // This function can be called either by undo or redo
    // In order to get redo to work, add another custom undo event with the
    // current value.  If you don't want redo to work, just skip adding
    // a custom undo event here
    double current_value = MyFavoriteNumber;
    e.Document.AddCustomUndoEvent("Favorite Number", OnUndoFavoriteNumber, current_value);

    double old_value = (double)e.Tag;
    RhinoApp.WriteLine("Going back to your favorite = {0}", old_value);
    MyFavoriteNumber = old_value;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def OnUndoFavoriteNumber(sender, e):
    """!!!!!!!!!!
    NEVER change any setting in the Rhino document or application.  Rhino
    handles ALL changes to the application and document and you will break
    the Undo/Redo commands if you make any changes to the application or
    document. This is meant only for your own private plugin data
    !!!!!!!!!!

    This function can be called either by undo or redo
    In order to get redo to work, add another custom undo event with the
    current value.  If you don't want redo to work, just skip adding
    a custom undo event here
    """
    current_value = scriptcontext.sticky["FavoriteNumber"]
    e.Document.AddCustomUndoEvent("Favorite Number", OnUndoFavoriteNumber, current_value)

    old_value = e.Tag
    print("Going back to your favorite =", old_value)
    scriptcontext.sticky["FavoriteNumber"]= old_value;

def TestCustomUndo():
    """
    Rhino automatically sets up an undo record when a command is run,
    but... the undo record is not saved if nothing changes in the
    document (objects added/deleted, layers changed,...)

    If we have a command that doesn't change things in the document,
    but we want to have our own custom undo called then we need to do
    a little extra work
    """
    current_value = 0
    if "FavoriteNumber" in scriptcontext.sticky:
        current_value = scriptcontext.sticky["FavoriteNumber"]
    rc, new_value = Rhino.Input.RhinoGet.GetNumber("Favorite number", True, current_value)
    if rc!=Rhino.Commands.Result.Success: return

    scriptcontext.doc.AddCustomUndoEvent("Favorite Number", OnUndoFavoriteNumber, current_value);
    scriptcontext.sticky["FavoriteNumber"] = new_value

if __name__=="__main__":
    TestCustomUndo()
```

</div>

+++
aliases = ["/en/5/samples/rhinocommon/edit-text/", "/en/6/samples/rhinocommon/edit-text/", "/en/7/samples/rhinocommon/edit-text/", "/en/wip/samples/rhinocommon/edit-text/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to edit selected text, replacing it with new text."
keywords = [ "edit", "text" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Edit Text"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/edittext"
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
  public static Rhino.Commands.Result EditText(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select text", false, Rhino.DocObjects.ObjectType.Annotation, out objref);
    if (rc != Rhino.Commands.Result.Success || objref == null)
      return rc;

    Rhino.DocObjects.TextObject textobj = objref.Object() as Rhino.DocObjects.TextObject;
    if (textobj == null)
      return Rhino.Commands.Result.Failure;

    Rhino.Geometry.TextEntity textentity = textobj.Geometry as Rhino.Geometry.TextEntity;
    if (textentity == null)
      return Rhino.Commands.Result.Failure;
    string str = textentity.Text;
    rc = Rhino.Input.RhinoGet.GetString("New text", false, ref str);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    textentity.Text = str;
    textobj.CommitChanges();
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

def EditText():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select text", False, Rhino.DocObjects.ObjectType.Annotation)
    if rc!=Rhino.Commands.Result.Success: return

    textobj = objref.Object()
    if not textobj: return

    str = textobj.Geometry.Text
    rc, str = Rhino.Input.RhinoGet.GetString("New text", False, str)
    if rc!=Rhino.Commands.Result.Success: return

    textobj.Geometry.Text = str;
    textobj.CommitChanges();
    scriptcontext.doc.Views.Redraw();

if __name__=="__main__":
    EditText()
```

</div>

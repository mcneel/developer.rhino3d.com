+++
aliases = ["/en/5/samples/rhinocommon/box-shell/", "/en/6/samples/rhinocommon/box-shell/", "/en/7/samples/rhinocommon/box-shell/", "/en/wip/samples/rhinocommon/box-shell/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to give thickness to (or shell) a Brep box."
keywords = [ "shell" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Box Shell"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
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
  public static Rhino.Commands.Result BoxShell(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Box box;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetBox(out box);
    if (rc == Rhino.Commands.Result.Success)
    {
      Rhino.Geometry.Brep brep = Rhino.Geometry.Brep.CreateFromBox(box);
      if (null != brep)
      {
        System.Collections.Generic.List<int> facesToRemove = new System.Collections.Generic.List<int>(1);
        facesToRemove.Add(0);
        Rhino.Geometry.Brep[] shells = Rhino.Geometry.Brep.CreateShell(brep, facesToRemove, 1.0, doc.ModelAbsoluteTolerance);
        if (null != shells)
        {
          for (int i = 0; i < shells.Length; i++)
            doc.Objects.AddBrep(shells[i]);
          doc.Views.Redraw();
        }
      }
    }
    return rc;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>

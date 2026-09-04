+++
aliases = ["/en/5/samples/rhinocommon/read-dimension-text/", "/en/6/samples/rhinocommon/read-dimension-text/", "/en/7/samples/rhinocommon/read-dimension-text/", "/en/wip/samples/rhinocommon/read-dimension-text/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to read dimension text from an annotation object."
keywords = [ "read", "dimension", "text" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Read Dimension Text"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/gettext"
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
  public static Result ReadDimensionText(RhinoDoc doc)
  {
    var go = new GetObject();
    go.SetCommandPrompt("Select annotation");
    go.GeometryFilter = ObjectType.Annotation;
    go.Get();
    if (go.CommandResult() != Result.Success)
      return Result.Failure;
    var annotation = go.Object(0).Object() as AnnotationObjectBase;
    if (annotation == null)
      return Result.Failure;

    RhinoApp.WriteLine("Annotation text = {0}", annotation.DisplayText);

    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>

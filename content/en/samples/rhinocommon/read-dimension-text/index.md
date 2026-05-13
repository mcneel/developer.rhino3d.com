+++
aliases = ["/en/5/samples/rhinocommon/read-dimension-text/", "/en/6/samples/rhinocommon/read-dimension-text/", "/en/7/samples/rhinocommon/read-dimension-text/", "/en/wip/samples/rhinocommon/read-dimension-text/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to read dimension text from an annotation object."
keywords = [ "read", "dimension", "text" ]
languages = [ "C#", "Python", "VB" ]
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


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function ReadDimensionText(ByVal doc As RhinoDoc) As Result
	Dim go = New GetObject()
	go.SetCommandPrompt("Select annotation")
	go.GeometryFilter = ObjectType.Annotation
	go.Get()
	If go.CommandResult() <> Result.Success Then
	  Return Result.Failure
	End If
	Dim annotation = TryCast(go.Object(0).Object(), AnnotationObjectBase)
	If annotation Is Nothing Then
	  Return Result.Failure
	End If

	RhinoApp.WriteLine("Annotation text = {0}", annotation.DisplayText)

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
#! python 3
import Rhino

def RunCommand():
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select annotation")
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Annotation
    go.Get()
    if go.CommandResult() != Rhino.Commands.Result.Success:
        return Rhino.Commands.Result.Failure
    annotation = go.Object(0).Object()
    if not isinstance(annotation, Rhino.DocObjects.AnnotationObjectBase):
        return Rhino.Commands.Result.Failure

    Rhino.RhinoApp.WriteLine("Annotation text = {0}", annotation.DisplayText)

    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>

+++
aliases = ["/en/5/samples/rhinocommon/add-linear-dimension/", "/en/6/samples/rhinocommon/add-linear-dimension/", "/en/7/samples/rhinocommon/add-linear-dimension/", "/wip/samples/rhinocommon/add-linear-dimension/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add a linear dimension to a Rhino model."
keywords = [ "add", "linear", "dimension" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Linear Dimension"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addlineardimension"
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
  public static Rhino.Commands.Result AddLinearDimension(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.LinearDimension dimension;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetLinearDimension(out dimension);
    if (rc == Rhino.Commands.Result.Success && dimension != null)
    {
      if (doc.Objects.AddLinearDimension(dimension) == Guid.Empty)
        rc = Rhino.Commands.Result.Failure;
      else
        doc.Views.Redraw();
    }
    return rc;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddLinearDimension(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim dimension As Rhino.Geometry.LinearDimension = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetLinearDimension(dimension)
	If rc Is Rhino.Commands.Result.Success AndAlso dimension IsNot Nothing Then
	  If doc.Objects.AddLinearDimension(dimension) = Guid.Empty Then
		rc = Rhino.Commands.Result.Failure
	  Else
		doc.Views.Redraw()
	  End If
	End If
	Return rc
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Guid

def AddLinearDimension():
    rc, dimension = Rhino.Input.RhinoGet.GetLinearDimension()
    if rc==Rhino.Commands.Result.Success:
        if scriptcontext.doc.Objects.AddLinearDimension(dimension)==System.Guid.Empty:
            rc = Rhino.Commands.Result.Failure
        else:
            scriptcontext.doc.Views.Redraw()
    return rc


if __name__=="__main__":
    AddLinearDimension()
```

</div>

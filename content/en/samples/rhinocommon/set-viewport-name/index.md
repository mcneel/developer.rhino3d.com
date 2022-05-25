+++
authors = [ "steve" ]
categories = [ "Viewports and Views" ]
description = "Demonstrates how to set a viewport's name or title."
keywords = [ "setting", "viewports", "title" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Set Viewport Name"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/setviewname"
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
  public static Result SetViewName(RhinoDoc doc)
  {
    var view = doc.Views.ActiveView;
    if (view == null)
      return Result.Failure;

    view.MainViewport.Name = "Facade";
    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function SetViewName(ByVal doc As RhinoDoc) As Result
	Dim view = doc.Views.ActiveView
	If view Is Nothing Then
	  Return Result.Failure
	End If

	view.MainViewport.Name = "Facade"
	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino.Commands import *
import rhinoscriptsyntax as rs
from scriptcontext import doc

def RunCommand():
    view = doc.Views.ActiveView
    if view == None:
        return Result.Failure

    view.MainViewport.Name = "Facade"
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>

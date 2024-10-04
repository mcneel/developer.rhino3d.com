+++
aliases = ["/en/5/samples/rhinocommon/viewport-resolution/", "/en/6/samples/rhinocommon/viewport-resolution/", "/en/7/samples/rhinocommon/viewport-resolution/", "/wip/samples/rhinocommon/viewport-resolution/"]
authors = [ "steve" ]
categories = [ "Viewports and Views" ]
description = "Print Active Viewport Resolution"
keywords = [ "print", "active", "viewport", "resolution" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Viewport Resolution"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/viewportresolution"
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
  public static Result ViewportResolution(RhinoDoc doc)
  {
    var active_viewport = doc.Views.ActiveView.ActiveViewport;
    RhinoApp.WriteLine("Name = {0}: Width = {1}, Height = {2}",
      active_viewport.Name, active_viewport.Size.Width, active_viewport.Size.Height);
    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function ViewportResolution(ByVal doc As RhinoDoc) As Result
	Dim active_viewport = doc.Views.ActiveView.ActiveViewport
	RhinoApp.WriteLine("Name = {0}: Width = {1}, Height = {2}", active_viewport.Name, active_viewport.Size.Width, active_viewport.Size.Height)
	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from scriptcontext import doc

activeViewport = doc.Views.ActiveView.ActiveViewport
print "Name = {0}: Width = {1}, Height = {2}".format(
    activeViewport.Name, activeViewport.Size.Width, activeViewport.Size.Height)
```

</div>

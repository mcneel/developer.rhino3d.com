+++
aliases = ["/en/5/samples/rhinocommon/set-rhinopageview-width-and-height/", "/en/6/samples/rhinocommon/set-rhinopageview-width-and-height/", "/en/7/samples/rhinocommon/set-rhinopageview-width-and-height/", "/en/wip/samples/rhinocommon/set-rhinopageview-width-and-height/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to set the RhinoPageView width and height dimensions."
keywords = [ "rhinopageview", "width", "height" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Set RhinoPageView Width and Height"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/rhinopageviewwidthheight"
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
  public static Result SetRhinoPageViewWidthAndHeight(RhinoDoc doc)
  {
    var width = 1189;
    var height = 841;
    var page_views = doc.Views.GetPageViews();
    int page_number = (page_views==null) ? 1 : page_views.Length + 1;
    var pageview = doc.Views.AddPageView(string.Format("A0_{0}",page_number), width, height);

    int new_width = width;
    var rc = RhinoGet.GetInteger("new width", false, ref new_width);
    if (rc != Result.Success || new_width <= 0) return rc;

    int new_height = height;
    rc = RhinoGet.GetInteger("new height", false, ref new_height);
    if (rc != Result.Success || new_height <= 0) return rc;

    pageview.PageWidth = new_width;
    pageview.PageHeight = new_height;
    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import scriptcontext as sc

def RunCommand():
    width = 1189
    height = 841
    page_views = sc.doc.Views.GetPageViews()
    page_number = 1 if page_views is None else len(page_views) + 1
    pageview = sc.doc.Views.AddPageView("A0_{0}".format(page_number), width, height)

    new_width = width
    rc, new_width = Rhino.Input.RhinoGet.GetInteger("new width", False, new_width)
    if rc != Rhino.Commands.Result.Success or new_width <= 0:
        return rc

    new_height = height
    rc, new_height = Rhino.Input.RhinoGet.GetInteger("new height", False, new_height)
    if rc != Rhino.Commands.Result.Success or new_height <= 0:
        return rc

    pageview.PageWidth = new_width
    pageview.PageHeight = new_height
    sc.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>

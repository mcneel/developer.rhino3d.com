+++
aliases = ["/en/5/samples/rhinocommon/add-layout/", "/en/6/samples/rhinocommon/add-layout/", "/en/7/samples/rhinocommon/add-layout/", "/en/wip/samples/rhinocommon/add-layout/"]
authors = [ "steve" ]
categories = [ "Adding Objects", "Viewports and Views" ]
description = "Demonstrates how to generate a layout with a single detail view that zooms to a list of objects."
keywords = [ "add", "layout", "with", "detail", "view" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Add Layout"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addlayout"
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
  /// <summary>
  /// Generate a layout with a single detail view that zooms to a list of objects
  /// </summary>
  /// <param name="doc"></param>
  /// <returns></returns>
  public static Rhino.Commands.Result AddLayout(Rhino.RhinoDoc doc)
  {
    doc.PageUnitSystem = Rhino.UnitSystem.Millimeters;
    var page_views = doc.Views.GetPageViews();
    int page_number = (page_views==null) ? 1 : page_views.Length + 1;
    var pageview = doc.Views.AddPageView(string.Format("A0_{0}",page_number), 1189, 841);
    if( pageview!=null )
    {
      Rhino.Geometry.Point2d top_left = new Rhino.Geometry.Point2d(20,821);
      Rhino.Geometry.Point2d bottom_right = new Rhino.Geometry.Point2d(1169, 20);
      var detail = pageview.AddDetailView("ModelView", top_left, bottom_right, Rhino.Display.DefinedViewportProjection.Top);
      if (detail != null)
      {
        pageview.SetActiveDetail(detail.Id);
        detail.Viewport.ZoomExtents();
        detail.DetailGeometry.IsProjectionLocked = true;
        detail.DetailGeometry.SetScale(1, doc.ModelUnitSystem, 10, doc.PageUnitSystem);
        // Commit changes tells the document to replace the document's detail object
        // with the modified one that we just adjusted
        detail.CommitChanges();
      }
      pageview.SetPageAsActive();
      doc.Views.ActiveView = pageview;
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
    return Rhino.Commands.Result.Failure;
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
    sc.doc.PageUnitSystem = Rhino.UnitSystem.Millimeters
    page_views = sc.doc.Views.GetPageViews()
    page_number = 1 if page_views is None else len(page_views) + 1
    pageview = sc.doc.Views.AddPageView("A0_{0}".format(page_number), 1189, 841)
    if pageview is not None:
        top_left = Rhino.Geometry.Point2d(20, 821)
        bottom_right = Rhino.Geometry.Point2d(1169, 20)
        detail = pageview.AddDetailView("ModelView", top_left, bottom_right, Rhino.Display.DefinedViewportProjection.Top)
        if detail is not None:
            pageview.SetActiveDetail(detail.Id)
            detail.Viewport.ZoomExtents()
            detail.DetailGeometry.IsProjectionLocked = True
            detail.DetailGeometry.SetScale(1, sc.doc.ModelUnitSystem, 10, sc.doc.PageUnitSystem)
            # Commit changes tells the document to replace the document's detail object
            # with the modified one that we just adjusted
            detail.CommitChanges()
        pageview.SetPageAsActive()
        sc.doc.Views.ActiveView = pageview
        sc.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

if __name__ == "__main__":
    RunCommand()
```

</div>

---
title: Add Layout
description: Demonstrates how to generate a layout with a single detail view that zooms to a list of objects.
author: ['Steve Baer', '@stevebaer']
apis: ['RhinoCommon']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Adding Objects', 'Viewports and Views']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/addlayout
order: 1
keywords: ['add', 'layout', 'with', 'detail', 'view']
layout: code-sample-rhinocommon
---

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
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  ''' <summary>
  ''' Generate a layout with a single detail view that zooms to a list of objects
  ''' </summary>
  ''' <param name="doc"></param>
  ''' <returns></returns>
  Public Shared Function AddLayout(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	doc.PageUnitSystem = Rhino.UnitSystem.Millimeters
	Dim page_views = doc.Views.GetPageViews()
	Dim page_number As Integer = If(page_views Is Nothing, 1, page_views.Length + 1)
	Dim pageview = doc.Views.AddPageView(String.Format("A0_{0}",page_number), 1189, 841)
	If pageview IsNot Nothing Then
	  Dim top_left As New Rhino.Geometry.Point2d(20,821)
	  Dim bottom_right As New Rhino.Geometry.Point2d(1169, 20)
	  Dim detail = pageview.AddDetailView("ModelView", top_left, bottom_right, Rhino.Display.DefinedViewportProjection.Top)
	  If detail IsNot Nothing Then
		pageview.SetActiveDetail(detail.Id)
		detail.Viewport.ZoomExtents()
		detail.DetailGeometry.IsProjectionLocked = True
		detail.DetailGeometry.SetScale(1, doc.ModelUnitSystem, 10, doc.PageUnitSystem)
		' Commit changes tells the document to replace the document's detail object
		' with the modified one that we just adjusted
		detail.CommitChanges()
	  End If
	  pageview.SetPageAsActive()
	  doc.Views.ActiveView = pageview
	  doc.Views.Redraw()
	  Return Rhino.Commands.Result.Success
	End If
	Return Rhino.Commands.Result.Failure
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}

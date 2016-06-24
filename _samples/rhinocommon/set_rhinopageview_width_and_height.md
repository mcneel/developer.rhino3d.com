---
title: Set RhinoPageView Width and Height
description:
author:
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/rhinopageviewwidthheight
order: 1
keywords: ['rhinopageview', 'width', 'height']
layout: code-sample-rhinocommon
---

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
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function SetRhinoPageViewWidthAndHeight(ByVal doc As RhinoDoc) As Result
	Dim width = 1189
	Dim height = 841
	Dim page_views = doc.Views.GetPageViews()
	Dim page_number As Integer = If(page_views Is Nothing, 1, page_views.Length + 1)
	Dim pageview = doc.Views.AddPageView(String.Format("A0_{0}",page_number), width, height)

	Dim new_width As Integer = width
	Dim rc = RhinoGet.GetInteger("new width", False, new_width)
	If rc IsNot Result.Success OrElse new_width <= 0 Then
		Return rc
	End If

	Dim new_height As Integer = height
	rc = RhinoGet.GetInteger("new height", False, new_height)
	If rc IsNot Result.Success OrElse new_height <= 0 Then
		Return rc
	End If

	pageview.PageWidth = new_width
	pageview.PageHeight = new_height
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}

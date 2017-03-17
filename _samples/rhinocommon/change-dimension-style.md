---
title: Change Dimension Style
description: Demonstrates how to change the dimension style on all objects in a Rhino document.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/dimstyle
order: 1
keywords: ['change', 'dimension', 'style']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result ChangeDimensionStyle(RhinoDoc doc)
  {
    foreach (var rhino_object in doc.Objects.GetObjectList(ObjectType.Annotation))
    {
      var annotation_object = rhino_object as AnnotationObjectBase;
      if (annotation_object == null) continue;

      var annotation = annotation_object.Geometry as AnnotationBase;
      if (annotation == null) continue;

      if (annotation.Index == doc.DimStyles.CurrentDimensionStyleIndex) continue;

      annotation.Index = doc.DimStyles.CurrentDimensionStyleIndex;
      annotation_object.CommitChanges();
    }

    doc.Views.Redraw();

    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ChangeDimensionStyle(ByVal doc As RhinoDoc) As Result
	For Each rhino_object In doc.Objects.GetObjectList(ObjectType.Annotation)
	  Dim annotation_object = TryCast(rhino_object, AnnotationObjectBase)
	  If annotation_object Is Nothing Then
		  Continue For
	  End If

	  Dim annotation = TryCast(annotation_object.Geometry, AnnotationBase)
	  If annotation Is Nothing Then
		  Continue For
	  End If

	  If annotation.Index = doc.DimStyles.CurrentDimensionStyleIndex Then
		  Continue For
	  End If

	  annotation.Index = doc.DimStyles.CurrentDimensionStyleIndex
	  annotation_object.CommitChanges()
	Next rhino_object

	doc.Views.Redraw()

	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from Rhino.Geometry import *
from scriptcontext import doc

def RunCommand():
  for annotation_object in doc.Objects.GetObjectList(ObjectType.Annotation):
    if not isinstance (annotation_object, AnnotationObjectBase):
      continue

    annotation = annotation_object.Geometry

    if annotation.Index == doc.DimStyles.CurrentDimensionStyleIndex:
      continue

    annotation.Index = doc.DimStyles.CurrentDimensionStyleIndex
    annotation_object.CommitChanges()

  doc.Views.Redraw()
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}

---
layout: code-sample
title: Box Shell
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['shell']
order: 33
description:  
---



```cs
public static Rhino.Commands.Result BoxShell(Rhino.RhinoDoc doc)
{
  Rhino.Geometry.Box box;
  Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetBox(out box);
  if (rc == Rhino.Commands.Result.Success)
  {
    Rhino.Geometry.Brep brep = Rhino.Geometry.Brep.CreateFromBox(box);
    if (null != brep)
    {
      System.Collections.Generic.List<int> facesToRemove = new System.Collections.Generic.List<int>(1);
      facesToRemove.Add(0);
      Rhino.Geometry.Brep[] shells = Rhino.Geometry.Brep.CreateShell(brep, facesToRemove, 1.0, doc.ModelAbsoluteTolerance);
      if (null != shells)
      {
        for (int i = 0; i < shells.Length; i++)
          doc.Objects.AddBrep(shells[i]);
        doc.Views.Redraw();
      }
    }
  }
  return rc;
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
no vb code sample available
```
{: #vb .tab-pane .fade .in}


```python
no python code sample available
```
{: #py .tab-pane .fade .in}



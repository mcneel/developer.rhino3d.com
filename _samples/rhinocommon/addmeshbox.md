---
layout: code-sample
title: Add Mesh Box
author: 
categories: ['Adding Objects'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['mesh']
order: 16
description:  
---



```cs
public static Rhino.Commands.Result AddMeshBox(Rhino.RhinoDoc doc)
{
  Rhino.Geometry.Box box;
  Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetBox(out box);
  if (rc == Rhino.Commands.Result.Success)
  {
    Rhino.Geometry.Mesh mesh = Rhino.Geometry.Mesh.CreateFromBox(box, 2, 2, 2);
    if (null != mesh)
    {
      doc.Objects.AddMesh(mesh);
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
  }

  return Rhino.Commands.Result.Failure;
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



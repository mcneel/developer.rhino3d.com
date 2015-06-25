---
layout: code-sample
title: conduitdrawshadedmesh
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['conduitdrawshadedmesh']
order: 39
description:  
---



```cs
public Rhino.Geometry.Mesh Mesh { get; set; }

protected override void CalculateBoundingBox(Rhino.Display.CalculateBoundingBoxEventArgs e)
{
  if (null != Mesh)
  {
    Rhino.Geometry.BoundingBox bbox = Mesh.GetBoundingBox(false);
    // Unites a bounding box with the current display bounding box in
    // order to ensure dynamic objects in "box" are drawn.
    e.IncludeBoundingBox(bbox);
  }
}

protected override void PostDrawObjects(Rhino.Display.DrawEventArgs e)
{
  if (null != Mesh)
  {
    Rhino.Display.DisplayMaterial material = new Rhino.Display.DisplayMaterial();
    material.Diffuse = System.Drawing.Color.Blue;
    e.Display.DrawMeshShaded(Mesh, material);
  }
}
```
{: #cs .tab-pane .fade .in .active}



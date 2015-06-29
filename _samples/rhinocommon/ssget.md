---
layout: code-sample
title: ssget
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['ssget']
order: 158
description:  
---



```cs
public class NonInteractObjSelectionCommand : Rhino.Commands.Command
{
  private readonly List<ConduitPoint> m_conduit_points = new List<ConduitPoint>();

  public override string EnglishName
  {
    get { return "csNonInteracPickPoints"; }
  }

  private List<ObjRef> ssget_point(RhinoDoc doc, RhinoView view, Point3d point)
  {
    var world_to_screen = view.ActiveViewport.GetTransform(CoordinateSystem.World, CoordinateSystem.Screen);
    point.Transform(world_to_screen);

    var pick_context = new PickContext();
    pick_context.View = view;
    pick_context.PickStyle = PickStyle.PointPick;
    pick_context.PickGroupsEnabled = true;

    var xform = view.ActiveViewport.GetPickTransform(Convert.ToInt32(point.X), Convert.ToInt32(point.Y));
    pick_context.SetPickTransform(xform);
    double depth, distance;

    foreach (var rhino_object in doc.Objects)
    {
      //rhino_object.OnPicked(pick_context, )
    }
    if (pick_context.PickFrustumTest(point, out depth, out distance))
      pick_context.UpdateClippingPlanes();
    return null;
  }

  protected override Rhino.Commands.Result RunCommand(RhinoDoc doc, Rhino.Commands.RunMode mode)
  {
    //var conduit = new PointsConduit(m_conduit_points);
    //conduit.Enabled = true;

    //var gp = new Rhino.Input.Custom.GetPoint();
    //while (true)
    //{
    //  gp.SetCommandPrompt("click location to create point. (<ESC> exit)");
    //  gp.AcceptNothing(true);
    //  gp.Get();
    //  if (gp.CommandResult() != Rhino.Commands.Result.Success)
    //    break;
    //  m_conduit_points.Add(new ConduitPoint(gp.Point()));
    //  doc.Views.Redraw();
    //}

    //var gcp = new GetConduitPoint(m_conduit_points);
    //while (true)
    //{
    //  gcp.SetCommandPrompt("select conduit point. (<ESC> to exit)");
    //  gcp.AcceptNothing(true);
    //  gcp.Get(true);
    //  doc.Views.Redraw();
    //  if (gcp.CommandResult() != Rhino.Commands.Result.Success)
    //    break;
    //}

    return Rhino.Commands.Result.Success;
  }
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



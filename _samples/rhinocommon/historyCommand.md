---
layout: code-sample
title: History Command
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['history', 'command']
order: 93
description:  
---



```cs
[System.Runtime.InteropServices.Guid("612cf825-844e-4b12-9c0a-1154928c7911")]
public class ex_historyCommand : Command
{
  static ex_historyCommand _instance;
  static int _historyVersion = 20121101; 

  /// <summary>
  /// Public command constructor
  /// </summary>
  public ex_historyCommand()
  {
    _instance = this;
  }

  /// <summary>
  /// The only instance of the ex_historycommand command.
  /// </summary>
  public static ex_historyCommand Instance
  {
    get { return _instance; }
  }

  /// <summary>
  /// The name of this command.
  /// </summary>
  public override string EnglishName
  {
    get { return "ex_historyCommand"; }
  }

  /// <summary>
  /// Rhino calls this function to run the command.
  /// </summary>
  protected override Rhino.Commands.Result RunCommand(Rhino.RhinoDoc doc, Rhino.Commands.RunMode mode)
  {
    const Rhino.DocObjects.ObjectType filter = Rhino.DocObjects.ObjectType.Curve;
    Rhino.DocObjects.ObjRef objref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select curve to divide", false, filter, out objref);
    if (rc != Rhino.Commands.Result.Success || objref == null)
      return rc;

    Rhino.Geometry.Curve curve = objref.Curve();
    if (null == curve || curve.IsShort(Rhino.RhinoMath.ZeroTolerance))
      return Rhino.Commands.Result.Failure;

    int segmentCount = 2;
    rc = Rhino.Input.RhinoGet.GetInteger("Number of segments", false, ref segmentCount, 2, 100);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    Rhino.Geometry.Point3d[] points;
    curve.DivideByCount(segmentCount, true, out points);
    if (null == points)
      return Rhino.Commands.Result.Failure;

    // Create a history record
    Rhino.DocObjects.HistoryRecord history = new Rhino.DocObjects.HistoryRecord(this, _historyVersion);
    WriteHistory(history, objref, segmentCount, points.Length);

    for (int i = 0; i < points.Length; i++)
      doc.Objects.AddPoint(points[i], null, history, false);

    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }

  /// <summary>
  /// Rhino calls this function to remake objects when inputs have changed.  
  /// </summary>
  protected override bool ReplayHistory(Rhino.DocObjects.ReplayHistoryData replay)
  {
    Rhino.DocObjects.ObjRef objref = null;
    int segmentCount = 0;
    int pointCount = 0;

    if (!ReadHistory(replay, ref objref, ref segmentCount, ref pointCount))
      return false;

    Rhino.Geometry.Curve curve = objref.Curve();
    if (null == curve)
      return false;

    if (pointCount != replay.Results.Length)
      return false;

    Rhino.Geometry.Point3d[] points;
    curve.DivideByCount(segmentCount, true, out points);
    if (null == points)
      return false;

    for (int i = 0; i < points.Length; i++)
      replay.Results[i].UpdateToPoint(points[i], null);

    return true;
  }

  private bool ReadHistory(Rhino.DocObjects.ReplayHistoryData replay, ref Rhino.DocObjects.ObjRef objref, ref int segmentCount, ref int pointCount)
  {
    if (_historyVersion != replay.HistoryVersion)
      return false;

    objref = replay.GetRhinoObjRef(0);
    if (null == objref)
      return false;

    if (!replay.TryGetInt(1, out segmentCount))
      return false;

    if (!replay.TryGetInt(2, out pointCount))
      return false;

    return true;
  }

  private bool WriteHistory(Rhino.DocObjects.HistoryRecord history, Rhino.DocObjects.ObjRef objref, int segmentCount, int pointCount)
  {
    if (!history.SetObjRef(0, objref))
      return false;

    if (!history.SetInt(1, segmentCount))
      return false;

    if (!history.SetInt(2, pointCount))
      return false;

    return true;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
<System.Runtime.InteropServices.Guid("2eb9836e-21cd-4b6e-8de0-654ded606ef8")> _
Public Class ex_historyCommand
  Inherits Command

  Shared _instance As ex_historyCommand
  Shared _historyVersion As Integer = 20121101


  Public Sub New()
    ' Rhino only creates one instance of each command class defined in a
    ' plug-in, so it is safe to store a refence in a static field.
    _instance = Me
  End Sub

  '''<summary>The only instance of this command.</summary>
  Public Shared ReadOnly Property Instance() As ex_historyCommand
    Get
      Return _instance
    End Get
  End Property

  '''<returns>The command name as it appears on the Rhino command line.</returns>
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "ex_historyCommand"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As Rhino.RhinoDoc, mode As Rhino.Commands.RunMode) As Rhino.Commands.Result
    Const filter As Rhino.DocObjects.ObjectType = Rhino.DocObjects.ObjectType.Curve
    Dim objref As Rhino.DocObjects.ObjRef = Nothing
    Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select curve to divide", False, filter, objref)
    If rc <> Rhino.Commands.Result.Success OrElse objref Is Nothing Then
      Return rc
    End If

    Dim curve As Rhino.Geometry.Curve = objref.Curve()
    If curve Is Nothing OrElse curve.IsShort(Rhino.RhinoMath.ZeroTolerance) Then
      Return Rhino.Commands.Result.Failure
    End If

    Dim segmentCount As Integer = 2
    rc = Rhino.Input.RhinoGet.GetInteger("Number of segments", False, segmentCount, 2, 100)
    If rc <> Rhino.Commands.Result.Success Then
      Return rc
    End If

    Dim points As Rhino.Geometry.Point3d() = Nothing
    curve.DivideByCount(segmentCount, True, points)
    If points Is Nothing Then
      Return Rhino.Commands.Result.Failure
    End If

    ' Create a history record
    Dim history As New Rhino.DocObjects.HistoryRecord(Me, _historyVersion)
    WriteHistory(history, objref, segmentCount, points.Length)

    For i As Integer = 0 To points.Length - 1
      doc.Objects.AddPoint(points(i), Nothing, history, False)
    Next

    doc.Views.Redraw()

    Return Rhino.Commands.Result.Success
  End Function

  Protected Overrides Function ReplayHistory(replay As Rhino.DocObjects.ReplayHistoryData) As Boolean
    Dim objref As Rhino.DocObjects.ObjRef = Nothing
    Dim segmentCount As Integer = 0
    Dim pointCount As Integer = 0

    If Not ReadHistory(replay, objref, segmentCount, pointCount) Then
      Return False
    End If

    Dim curve As Rhino.Geometry.Curve = objref.Curve()
    If curve Is Nothing Then
      Return False
    End If

    If pointCount <> replay.Results.Length Then
      Return False
    End If

    Dim points As Rhino.Geometry.Point3d() = Nothing
    curve.DivideByCount(segmentCount, True, points)
    If points Is Nothing Then
      Return False
    End If

    For i As Integer = 0 To points.Length - 1
      replay.Results(i).UpdateToPoint(points(i), Nothing)
    Next

    Return True
  End Function

  Private Function ReadHistory(replay As Rhino.DocObjects.ReplayHistoryData, ByRef objref As Rhino.DocObjects.ObjRef, ByRef segmentCount As Integer, ByRef pointCount As Integer) As Boolean
    If _historyVersion <> replay.HistoryVersion Then
      Return False
    End If

    objref = replay.GetRhinoObjRef(0)
    If objref Is Nothing Then
      Return False
    End If

    If Not replay.TryGetInt(1, segmentCount) Then
      Return False
    End If

    If Not replay.TryGetInt(2, pointCount) Then
      Return False
    End If

    Return True
  End Function

  Private Function WriteHistory(history As Rhino.DocObjects.HistoryRecord, objref As Rhino.DocObjects.ObjRef, segmentCount As Integer, pointCount As Integer) As Boolean
    If Not history.SetObjRef(0, objref) Then
      Return False
    End If

    If Not history.SetInt(1, segmentCount) Then
      Return False
    End If

    If Not history.SetInt(2, pointCount) Then
      Return False
    End If

    Return True
  End Function

End Class
```
{: #vb .tab-pane .fade .in}


```python
no python code sample available
```
{: #py .tab-pane .fade .in}



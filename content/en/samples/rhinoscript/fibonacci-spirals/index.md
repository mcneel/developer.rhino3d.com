+++
aliases = ["/en/5/samples/rhinoscript/fibonacci-spirals/", "/en/6/samples/rhinoscript/fibonacci-spirals/", "/en/7/samples/rhinoscript/fibonacci-spirals/", "/wip/samples/rhinoscript/fibonacci-spirals/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to create a Fibonacci Spiral with RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Fibonacci Spirals"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/fibonaccispiral"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' FibonacciSpiral.rvb -- June 2009
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

Call FibonacciSpiral()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Computes Fibonacci Spiral
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub FibonacciSpiral()

  ' Local variables
  Dim steps, scale, plane, xform
  Dim origin, pt0, pt1, pt2, pt3
  Dim n, cmd

  ' Get number of Fibonacci numbers to calculate
  steps = Rhino.GetInteger("Number of steps", 10, 1, 50)
  If IsNull(steps) Then Exit Sub

  ' Original origin point
  origin = Array(0,0,0)

  ' Process every step...
  For n = 1 To steps

    ' Compute Fibonacci number using Binet's formula      
    scale = Round(((Sqr(5) + 1) / 2) ^ n / Sqr(5))

    ' Determine x and y axes based on where we are
    plane = Rhino.WorldXYPlane()
    xform = Rhino.XformRotation(90.0 * (n Mod 4), plane(3), plane(0))
    plane = Rhino.PlaneTransform(plane, xform)

    ' Calculate arc points
    pt0 = origin
    ' Offset pt0 in the xaxis direction by scale
    pt1 = Rhino.PointAdd(pt0, Rhino.VectorScale(plane(1), scale))
    ' Offset pt1 in the yaxis direction by scale
    pt2 = Rhino.PointAdd(pt1, Rhino.VectorScale(plane(2), scale))
    ' Offset origin in the yaxis direction by scale
    pt3 = Rhino.PointAdd(pt0, Rhino.VectorScale(plane(2), scale))

    ' Add a closed polyline
    Call Rhino.AddPolyline(Array(pt0, pt1, pt2, pt3, pt0))

    ' Build a command script that will create an arc from
    ' start, end, and direction
    cmd = "_-Arc _StartPoint " & _
          Rhino.Pt2Str(pt0)    & _
          " "                  & _
          Rhino.Pt2Str(pt2)    & _
          " _Direction "       & _
          Rhino.Pt2Str(pt1)

    ' Run the command script to create the arc          
    Call Rhino.Command(cmd, 0)

    ' Update the origin point
    origin = pt2

  Next

End Sub
```

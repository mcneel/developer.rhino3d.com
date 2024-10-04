+++
aliases = ["/en/5/samples/rhinoscript/create-square-pipes/", "/en/6/samples/rhinoscript/create-square-pipes/", "/en/7/samples/rhinoscript/create-square-pipes/", "/wip/samples/rhinoscript/create-square-pipes/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to create square pipes using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Create Square Pipes"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/squarepipe"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Sub SquarePipe

	' Declare local variables
	Dim arrCrvs, strCrv, dblLength
	Dim arrStart, dblParam, arrPlane
	Dim x0, x1, y0, y1, arrX, arrY
	Dim arrPoints(4), strSqr

	' Pick the input, or path, curves
	arrCrvs = Rhino.GetObjects("Select curves", 4)
	If IsNull(strCrv) Then Exit Sub

	' Specify the lengths of the sides of the square    
	dblLength = Rhino.GetReal("Length of sides", 1.0, 0.0)
	If Not IsNumeric(dblLength) Or dblLength <= 0 Then Exit Sub

	Call Rhino.EnableRedraw(False)

	For Each strCrv In arrCrvs

		' Determine the curve's starting point    
		arrStart = Rhino.CurveStartPoint(strCrv)

		' Determine the parameter at the starting point  
		dblParam = Rhino.CurveClosestPoint(strCrv, arrStart)

		' Detemine the curve's perpendicular plane at its starting point.
		' We can use this plane to cook up the coordinates of the square.
		arrPlane = Rhino.CurvePerpFrame(strCrv, dblParam)

		' Scale the vectors based on the user input
		arrX = Rhino.VectorScale(arrPlane(1), dblLength * 0.5)
		arrY = Rhino.VectorScale(arrPlane(2), dblLength * 0.5)

		' Cook up some temporary points
		x0 = Rhino.PointAdd(arrStart, arrX)
		x1 = Rhino.PointAdd(arrStart, Rhino.VectorReverse(arrX))
		y0 = Rhino.PointAdd(arrStart, arrY)
		y1 = Rhino.PointAdd(arrStart, Rhino.VectorReverse(arrY))

		' Define the points of the square  
		arrPoints(0) = Rhino.PointAdd(x0, Rhino.VectorReverse(arrY))
		arrPoints(1) = Rhino.PointAdd(y1, Rhino.VectorReverse(arrX))
		arrPoints(2) = Rhino.PointAdd(x1, arrY)
		arrPoints(3) = Rhino.PointAdd(y0, arrX)
		arrPoints(4) = arrPoints(0)

		' Create the square
		strSqr = Rhino.AddPolyline(arrPoints)

		' Extrude the polyline along the input curve
		Call Rhino.ExtrudeCurve(strSqr, strCrv)

		' Delete polyline
		Call Rhino.DeleteObject(strSqr)

	Next

	Call Rhino.EnableRedraw(True)

End Sub
```

---
title: Joining the Dots
description: Demonstrates joining points into polylines in RhinoScript.
author: Steven Janssen
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/jointhedots
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit
'Script written by Steven Janssen
'Script version Monday, 9 July 2007 5:23:12 PM

Call Main()
Sub Main()
	Dim arrPoints, arrPoint1, arrPoint2, arrVirtual, arrClosestPt, arrExtractedCoords
	Dim arrVecBetweenPts, arrJoin
	Dim intTolerance, intCurrentDist, intMinDist
	Dim k, i
	i = 0

	arrPoint1 = Rhino.GetPoint("Choose starting point")
	arrPoint2 = Rhino.GetPoint("Choose second point")
	intTolerance = 2 * rhino.Distance(arrPoint1, arrPoint2)
	'intTolerance = Rhino.GetReal("Maximum Distance?",intTolerance)
	arrPoints = Rhino.GetObjects("Select other Points", 1)

	Rhino.EnableRedraw vbFalse
	Do
		'add line between Point1 and Point2
		i = i + 1
		rhino.Print i
		rhino.addline arrPoint1, arrPoint2

		'create the virtual point
		arrVecBetweenPts = rhino.VectorCreate(arrPoint2,arrPoint1)
		arrVecBetweenPts = rhino.VectorScale(arrVecBetweenPts,2)
		arrVirtual = rhino.VectorAdd(arrVecBetweenPts,arrPoint1)

		'find closest point to the virtual point by sifting through all the other points
		intMinDist = 10 * intTolerance 'starting distance
		For k = 0 To Ubound(arrPoints)
			arrExtractedCoords = rhino.PointCoordinates(arrPoints(k))
			If rhino.Pointcompare(arrExtractedCoords,arrPoint2) = vbFalse Then

				intCurrentDist = rhino.Distance(arrExtractedCoords,arrVirtual)

				If intCurrentDist < intMinDist Then
					intMinDist = intCurrentDist
					arrClosestPt = arrExtractedCoords
				End If
			End If
		Next

		'adaptive Tolerance
		'If (2 * intMinDist) > intTolerance Then
		'	intTolerance = (2 * intMinDist)
		'End If

		'check if distance is greater than tolerance and exit if it is
		'rhino.print intMinDist & ", "
		If intMinDist > intTolerance Then
			Exit Do
		End If

		'move the points so that Point2 is Point1 and the newly found point is Point2
		arrPoint1 = arrPoint2
		arrPoint2 = arrClosestPt

		'the following prevents endless loops when there are two points close together at the end
		If rhino.distance(arrPoint1, arrPoint2) < (intTolerance/50) Then
			Exit Do
		End If

	Loop
	Rhino.EnableRedraw vbTrue

End Sub
```

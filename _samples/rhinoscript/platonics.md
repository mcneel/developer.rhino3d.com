---
layout: code-sample-rhinoscript
title: Generating Platonic and Archimedean Solids
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to generate platonic and archimedean solids with RhinoScript.
origin: http://wiki.mcneel.com/developer/scriptsamples/platonics
order: 1
---

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Define geometry for rhombitruncated icosidodecahedron
'''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub RhombitruncatedIcosidodecahedron()

   ' Define the vertices
   Dim arrVertices(119)
   arrVertices(0)   = Array( 0.519,  0.280, -0.560)
   arrVertices(1)   = Array( 0.214, -0.733,  0.280)
   arrVertices(2)   = Array( 0.280, -0.214, -0.733)
   arrVertices(3)   = Array( 0.107,  0.107,  0.799)
   arrVertices(4)   = Array( 0.280,  0.214,  0.733)
   arrVertices(5)   = Array( 0.453,  0.107, -0.667)
   arrVertices(6)   = Array( 0.733, -0.280,  0.214)
   arrVertices(7)   = Array( 0.280, -0.214,  0.733)
   arrVertices(8)   = Array(-0.280, -0.560,  0.519)
   arrVertices(9)   = Array( 0.107, -0.107,  0.799)
   arrVertices(10)  = Array(-0.560, -0.519,  0.280)
   arrVertices(11)  = Array(-0.280,  0.560, -0.519)
   arrVertices(12)  = Array( 0.214,  0.733, -0.280)
   arrVertices(13)  = Array( 0.519, -0.280,  0.560)
   arrVertices(14)  = Array(-0.667,  0.453, -0.107)
   arrVertices(15)  = Array( 0.799, -0.107,  0.107)
   arrVertices(16)  = Array(-0.107, -0.667,  0.453)
   arrVertices(17)  = Array(-0.107,  0.107,  0.799)
   arrVertices(18)  = Array( 0.107,  0.799,  0.107)
   arrVertices(19)  = Array(-0.453,  0.107, -0.667)
   arrVertices(20)  = Array(-0.280, -0.560, -0.519)
   arrVertices(21)  = Array( 0.214, -0.733, -0.280)
   arrVertices(22)  = Array( 0.346,  0.387,  0.626)
   arrVertices(23)  = Array( 0.560, -0.519, -0.280)
   arrVertices(24)  = Array(-0.107, -0.107,  0.799)
   arrVertices(25)  = Array( 0.280, -0.560,  0.519)
   arrVertices(26)  = Array(-0.107, -0.799,  0.107)
   arrVertices(27)  = Array( 0.280,  0.560,  0.519)
   arrVertices(28)  = Array(-0.799, -0.107,  0.107)
   arrVertices(29)  = Array( 0.626, -0.346, -0.387)
   arrVertices(30)  = Array(-0.667, -0.453, -0.107)
   arrVertices(31)  = Array( 0.519,  0.280,  0.560)
   arrVertices(32)  = Array( 0.560, -0.519,  0.280)
   arrVertices(33)  = Array(-0.346,  0.387,  0.626)
   arrVertices(34)  = Array(-0.346,  0.387, -0.626)
   arrVertices(35)  = Array(-0.453, -0.107, -0.667)
   arrVertices(36)  = Array(-0.560,  0.519,  0.280)
   arrVertices(37)  = Array(-0.107,  0.799, -0.107)
   arrVertices(38)  = Array(-0.519,  0.280,  0.560)
   arrVertices(39)  = Array(-0.519, -0.280, -0.560)
   arrVertices(40)  = Array(-0.453,  0.107,  0.667)
   arrVertices(41)  = Array(-0.387,  0.626,  0.346)
   arrVertices(42)  = Array(-0.346, -0.387,  0.626)
   arrVertices(43)  = Array(-0.107,  0.667,  0.453)
   arrVertices(44)  = Array(-0.733,  0.280, -0.214)
   arrVertices(45)  = Array(-0.519, -0.280,  0.560)
   arrVertices(46)  = Array(-0.107, -0.799, -0.107)
   arrVertices(47)  = Array( 0.387, -0.626, -0.346)
   arrVertices(48)  = Array( 0.733,  0.280, -0.214)
   arrVertices(49)  = Array(-0.214,  0.733, -0.280)
   arrVertices(50)  = Array(-0.107,  0.107, -0.799)
   arrVertices(51)  = Array( 0.733,  0.280,  0.214)
   arrVertices(52)  = Array( 0.667,  0.453,  0.107)
   arrVertices(53)  = Array( 0.107, -0.799, -0.107)
   arrVertices(54)  = Array( 0.667, -0.453,  0.107)
   arrVertices(55)  = Array( 0.107,  0.799, -0.107)
   arrVertices(56)  = Array(-0.346, -0.387, -0.626)
   arrVertices(57)  = Array( 0.733, -0.280, -0.214)
   arrVertices(58)  = Array(-0.280, -0.214,  0.733)
   arrVertices(59)  = Array(-0.667,  0.453,  0.107)
   arrVertices(60)  = Array( 0.346, -0.387,  0.626)
   arrVertices(61)  = Array(-0.733,  0.280,  0.214)
   arrVertices(62)  = Array( 0.214,  0.733,  0.280)
   arrVertices(63)  = Array( 0.453, -0.107, -0.667)
   arrVertices(64)  = Array( 0.107, -0.667,  0.453)
   arrVertices(65)  = Array(-0.626, -0.346,  0.387)
   arrVertices(66)  = Array(-0.667, -0.453,  0.107)
   arrVertices(67)  = Array( 0.107, -0.107, -0.799)
   arrVertices(68)  = Array(-0.626,  0.346,  0.387)
   arrVertices(69)  = Array( 0.560,  0.519,  0.280)
   arrVertices(70)  = Array(-0.214,  0.733,  0.280)
   arrVertices(71)  = Array(-0.733, -0.280,  0.214)
   arrVertices(72)  = Array(-0.107,  0.667, -0.453)
   arrVertices(73)  = Array( 0.626,  0.346, -0.387)
   arrVertices(74)  = Array( 0.667,  0.453, -0.107)
   arrVertices(75)  = Array(-0.733, -0.280, -0.214)
   arrVertices(76)  = Array( 0.626, -0.346,  0.387)
   arrVertices(77)  = Array( 0.346,  0.387, -0.626)
   arrVertices(78)  = Array(-0.214, -0.733,  0.280)
   arrVertices(79)  = Array(-0.519,  0.280, -0.560)
   arrVertices(80)  = Array(-0.626,  0.346, -0.387)
   arrVertices(81)  = Array( 0.560,  0.519, -0.280)
   arrVertices(82)  = Array(-0.387,  0.626, -0.346)
   arrVertices(83)  = Array( 0.107, -0.799,  0.107)
   arrVertices(84)  = Array( 0.453, -0.107,  0.667)
   arrVertices(85)  = Array(-0.280,  0.560,  0.519)
   arrVertices(86)  = Array( 0.799, -0.107, -0.107)
   arrVertices(87)  = Array(-0.626, -0.346, -0.387)
   arrVertices(88)  = Array( 0.667, -0.453, -0.107)
   arrVertices(89)  = Array( 0.387,  0.626, -0.346)
   arrVertices(90)  = Array(-0.799,  0.107, -0.107)
   arrVertices(91)  = Array(-0.560,  0.519, -0.280)
   arrVertices(92)  = Array(-0.107, -0.667, -0.453)
   arrVertices(93)  = Array( 0.107, -0.667, -0.453)
   arrVertices(94)  = Array( 0.280,  0.214, -0.733)
   arrVertices(95)  = Array(-0.799, -0.107, -0.107)
   arrVertices(96)  = Array( 0.387,  0.626,  0.346)
   arrVertices(97)  = Array( 0.387, -0.626,  0.346)
   arrVertices(98)  = Array( 0.799,  0.107,  0.107)
   arrVertices(99)  = Array( 0.107,  0.667, -0.453)
   arrVertices(100) = Array(-0.280,  0.214,  0.733)
   arrVertices(101) = Array(-0.280,  0.214, -0.733)
   arrVertices(102) = Array(-0.214, -0.733, -0.280)
   arrVertices(103) = Array( 0.280,  0.560, -0.519)
   arrVertices(104) = Array( 0.107,  0.107, -0.799)
   arrVertices(105) = Array( 0.626,  0.346,  0.387)
   arrVertices(106) = Array(-0.560, -0.519, -0.280)
   arrVertices(107) = Array( 0.799,  0.107, -0.107)
   arrVertices(108) = Array(-0.280, -0.214, -0.733)
   arrVertices(109) = Array( 0.346, -0.387, -0.626)
   arrVertices(110) = Array(-0.387, -0.626, -0.346)
   arrVertices(111) = Array( 0.453,  0.107,  0.667)
   arrVertices(112) = Array( 0.280, -0.560, -0.519)
   arrVertices(113) = Array( 0.107,  0.667,  0.453)
   arrVertices(114) = Array(-0.799,  0.107,  0.107)
   arrVertices(115) = Array(-0.107, -0.107, -0.799)
   arrVertices(116) = Array(-0.107,  0.799,  0.107)
   arrVertices(117) = Array(-0.387, -0.626,  0.346)
   arrVertices(118) = Array( 0.519, -0.280, -0.560)
   arrVertices(119) = Array(-0.453, -0.107,  0.667)

   'Define the faces
   Dim arrFaces(61)
   arrFaces(0)  = Array(47,23,88,54,32,97,1,83,53,21)
   arrFaces(1)  = Array(84,111,4,3,9,7)
   arrFaces(2)  = Array(76,6,54,32)
   arrFaces(3)  = Array(24,9,3,17)
   arrFaces(4)  = Array(18,62,96,69,52,74,81,89,12,55)
   arrFaces(5)  = Array(35,39,87,75,95,90,44,80,79,19)
   arrFaces(6)  = Array(8,16,78,117)
   arrFaces(7)  = Array(8,42,45,65,10,117)
   arrFaces(8)  = Array(7,60,13,84)
   arrFaces(9)  = Array(114,90,44,14,59,61)
   arrFaces(10) = Array(5,0,73,48,107,86,57,29,118,63)
   arrFaces(11) = Array(77,94,104,50,101,34,11,72,99,103)
   arrFaces(12) = Array(4,22,31,111)
   arrFaces(13) = Array(49,37,55,12,99,72)
   arrFaces(14) = Array(6,76,13,84,111,31,105,51,98,15)
   arrFaces(15) = Array(100,33,38,40)
   arrFaces(16) = Array(18,55,37,116)
   arrFaces(17) = Array(43,70,41,85)
   arrFaces(18) = Array(58,42,45,119)
   arrFaces(19) = Array(105,31,22,27,96,69)
   arrFaces(20) = Array(21,47,112,93)
   arrFaces(21) = Array(105,51,52,69)
   arrFaces(22) = Array(28,71,65,45,119,40,38,68,61,114)
   arrFaces(23) = Array(15,86,107,98)
   arrFaces(24) = Array(68,61,59,36)
   arrFaces(25) = Array(93,92,102,46,53,21)
   arrFaces(26) = Array(114,28,95,90)
   arrFaces(27) = Array(65,71,66,10)
   arrFaces(28) = Array(28,95,75,30,66,71)
   arrFaces(29) = Array(113,62,96,27)
   arrFaces(30) = Array(74,81,73,48)
   arrFaces(31) = Array(89,103,77,0,73,81)
   arrFaces(32) = Array(76,13,60,25,97,32)
   arrFaces(33) = Array(14,91,80,44)
   arrFaces(34) = Array(16,8,42,58,24,9,7,60,25,64)
   arrFaces(35) = Array(23,29,118,109,112,47)
   arrFaces(36) = Array(30,106,87,75)
   arrFaces(37) = Array(43,85,33,100,17,3,4,22,27,113)
   arrFaces(38) = Array(82,49,37,116,70,41,36,59,14,91)
   arrFaces(39) = Array(0,5,94,77)
   arrFaces(40) = Array(93,112,109,2,67,115,108,56,20,92)
   arrFaces(41) = Array(74,52,51,98,107,48)
   arrFaces(42) = Array(79,19,101,34)
   arrFaces(43) = Array(25,64,1,97)
   arrFaces(44) = Array(12,89,103,99)
   arrFaces(45) = Array(39,35,108,56)
   arrFaces(46) = Array(19,101,50,115,108,35)
   arrFaces(47) = Array(64,1,83,26,78,16)
   arrFaces(48) = Array(104,50,115,67)
   arrFaces(49) = Array(110,102,46,26,78,117,10,66,30,106)
   arrFaces(50) = Array(113,62,18,116,70,43)
   arrFaces(51) = Array(118,63,2,109)
   arrFaces(52) = Array(5,94,104,67,2,63)
   arrFaces(53) = Array(100,17,24,58,119,40)
   arrFaces(54) = Array(49,82,11,72)
   arrFaces(55) = Array(91,80,79,34,11,82)
   arrFaces(56) = Array(83,53,46,26)
   arrFaces(57) = Array(102,110,20,92)
   arrFaces(58) = Array(106,87,39,56,20,110)
   arrFaces(59) = Array(85,41,36,68,38,33)
   arrFaces(60) = Array(88,23,29,57)
   arrFaces(61) = Array(6,54,88,57,86,15)

   ' Create the solid
   CreateSolid arrVertices, arrFaces
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Define geometry for truncated tetrahedron
'''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub TruncatedTetrahedron()
   ' Define the vertices
   Dim arrVertices(11)
   arrVertices(0)  = Array(-0.347, 0.000,-0.735)
   arrVertices(1)  = Array(-0.693,-0.347,-0.245)
   arrVertices(2)  = Array( 0.347, 0.693, 0.245)
   arrVertices(3)  = Array( 0.000, 0.347, 0.735)
   arrVertices(4)  = Array( 0.693, 0.347,-0.245)
   arrVertices(5)  = Array(-0.347,-0.693, 0.245)
   arrVertices(6)  = Array( 0.347, 0.000,-0.735)
   arrVertices(7)  = Array( 0.347,-0.693, 0.245)
   arrVertices(8)  = Array( 0.693,-0.347,-0.245)
   arrVertices(9)  = Array( 0.000,-0.347, 0.735)
   arrVertices(10) = Array(-0.347, 0.693, 0.245)
   arrVertices(11) = Array(-0.693, 0.347,-0.245)

   'Define the faces
   Dim arrFaces(7)
   arrFaces(0) = Array(9,5,7)
   arrFaces(1) = Array(6,4,8)
   arrFaces(2) = Array(10,11,0,6,4,2)
   arrFaces(3) = Array(4,2,3,9,7,8)
   arrFaces(4) = Array(1,11,0)
   arrFaces(5) = Array(10,3,2)
   arrFaces(6) = Array(6,0,1,5,7,8)
   arrFaces(7) = Array(5,1,11,10,3,9)

   ' Create the solid
   CreateSolid arrVertices, arrFaces
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''
' General purpose subroutine to create solids
'''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub CreateSolid(arrVertices, arrFaces)
   Dim arrSurfaces()
   ReDim arrSurfaces(UBound(arrFaces))
   Rhino.EnableRedraw False

   ' Create each face
   Dim i, j, arrFace, arrPoints(), strPolyline, arrPlanarSrf
   For i = 0 To UBound(arrFaces)
     arrFace = arrFaces(i)
     ReDim arrPoints(UBound(arrFace) + 1)
     For j = 0 To UBound(arrFace)
       arrPoints(j) = arrVertices(arrFace(j))
     Next
     arrPoints(UBound(arrFace) + 1) = arrPoints(0)
     strPolyline = Rhino.AddPolyline(arrPoints)
     arrPlanarSrf = Rhino.AddPlanarSrf(Array(strPolyline))
     arrSurfaces(i) = arrPlanarSrf(0)
     Rhino.DeleteObject strPolyline
   Next

   ' Join all of the faces
   Rhino.SelectObjects arrSurfaces
   Rhino.Command "_-Join"
   Rhino.UnselectAllObjects
   Rhino.EnableRedraw True
 End Sub
```

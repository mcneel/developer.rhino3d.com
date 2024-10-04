+++
aliases = ["/en/5/samples/rhinoscript/drawing-steel-shapes/", "/en/6/samples/rhinoscript/drawing-steel-shapes/", "/en/7/samples/rhinoscript/drawing-steel-shapes/", "/wip/samples/rhinoscript/drawing-steel-shapes/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to draw steel shapes using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Drawing Steel Shapes"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/steelshapes"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Steel.rvb -- September 2008
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.

Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
' Draws Steel Wide Flanges
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
Sub SteelWideFlange

  Dim cmdname, configfile, section
  Dim filename, entries, entry, value, data, bname
  Dim ip, d, b, tf, tw, c
  Dim p0, p1, p2, p3
  Dim e0, e1, e2, e3, a0

  cmdname = "Steel Wide Flange"
  configfile = "STEEL.INI"
  section = "STEEL_WIDE_FLANGE"

  filename = Rhino.FindFile(configfile)
  If IsNull(filename) Then
    Call MsgBox("Unable to locate " & configfile & ".", 17, cmdname)
    Exit Sub
  End If

  entries = Rhino.GetSettings(filename, section)
  If IsNull(entries) Then Exit Sub

  entry = Rhino.ListBox(entries, "Select a wide flange", cmdname)
  If IsNull(entry) Then Exit Sub

  bname = Replace(entry, ".", "_")

  If Rhino.IsBlock(bname) = False Then

    value = Rhino.GetSettings(filename, section, entry)
    If IsNull(value) Then Exit Sub

    data = Rhino.Strtok(value, ", ;")
    If IsNull(data) Or (UBound(data) <> 3) Then Exit Sub

    ' Hide the dirty work      
    Call Rhino.EnableRedraw(False)

    ip = Array(0,0,0)
    d = CDbl(data(0))
    b = CDbl(data(1))
    tf = CDbl(data(2))
    tw = CDbl(data(3))

    ' Top
    p0 = Rhino.Polar(Rhino.Polar(ip, 0, b/2), 270, tf)
    p1 = Rhino.Polar(ip, 0, b/2)
    p2 = Rhino.Polar(ip, 180, b/2)
    p3 = Rhino.Polar(p0, 180, b)
    e0 = Rhino.AddPolyline(Array(p0, p1, p2, p3))

    ' Bottom
    c = Rhino.Polar(ip, 270, d/2)
    e1 = Rhino.MirrorObject(e0, c, Rhino.Polar(c, 0, 1), True)

    ' Right side
    p1 = Rhino.Polar(p0, 180, (b-tw)/2)
    p2 = Rhino.Polar(p1, 270, (d-(tf*2)))
    p3 = Rhino.Polar(p2, 0, (b-tw)/2)
    e2 = Rhino.AddPolyline(Array(p0, p1, p2, p3))
    Call Rhino.Command("_-FilletCorners _SelID " & e2 & " _Enter " & CStr(0.9*tf), 0)

    ' Left side
    e3 = Rhino.MirrorObject(e2, c, ip, True)

    ' Join
    a0 = Rhino.JoinCurves(Array(e0, e1, e2, e3), True)

    ' Create the block
    Call Rhino.SelectObjects(a0)
    Call Rhino.Command("_-Block 0 " & Chr(34) & bname & Chr(34) & " _Enter _Enter _Enter", 0)

    ' Delete the block inserted by the Block command
    Call Rhino.DeleteObjects(Rhino.LastCreatedObjects)

    ' Enable redrawing
    Call Rhino.EnableRedraw(True)

  End If

  ' Insert the block
  Call Rhino.Command("_-Insert " & Chr(34) & bname & Chr(34) & " _Block", 0)

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
' Draws Steel Channels
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
Sub SteelChannel

  Dim cmdname, configfile, section
  Dim filename, entries, entry, value, data, bname
  Dim ip, d, b, tf, tw, tip
  Dim p0, p1, p2, p3, p4, p5
  Dim e0, e1, a0

  cmdname = "Steel Channel"
  configfile = "STEEL.INI"
  section = "STEEL_CHANNEL"

  filename = Rhino.FindFile(configfile)
  If IsNull(filename) Then
    Call MsgBox("Unable to locate " & configfile & ".", 17, cmdname)
    Exit Sub
  End If

  entries = Rhino.GetSettings(filename, section)
  If IsNull(entries) Then Exit Sub

  entry = Rhino.ListBox(entries, "Select a channel", cmdname)
  If IsNull(entry) Then Exit Sub

  bname = Replace(entry, ".", "_")

  If Rhino.IsBlock(bname) = False Then

    value = Rhino.GetSettings(filename, section, entry)
    If IsNull(value) Then Exit Sub

    data = Rhino.Strtok(value, ", ;")
    If IsNull(data) Or (UBound(data) <> 3) Then Exit Sub

    ' Hide the dirty work      
    Call Rhino.EnableRedraw(False)

    ip = Array(0,0,0)
    d = CDbl(data(0))
    b = CDbl(data(1))
    tf = CDbl(data(2))
    tw = CDbl(data(3))
    tip = tf * 0.7

    ' Top
    p0 = Rhino.Polar(Rhino.Polar(ip, 90, d/2), 0, b)
    p1 = Rhino.Polar(ip, 90, d/2)
    p2 = Rhino.Polar(ip, 270, d/2)
    p3 = Rhino.Polar(p0, 270, d)
    e0 = Rhino.AddPolyline(Array(p0, p1, p2, p3))

    ' Right
    p1 = Rhino.Polar(p0, 270, tip)
    p2 = Rhino.Polar(Rhino.Polar(p0, 180, b-tw), 270, tf)
    p3 = Rhino.Polar(p2, 270, d-(tf*2))
    p4 = Rhino.Polar(Rhino.Polar(p0, 270, d), 90, tip)
    p5 = Rhino.Polar(p0, 270, d)
    e1 = Rhino.AddPolyline(Array(p0, p1, p2, p3, p4, p5))
    Call Rhino.Command("_-FilletCorners _SelID " & e1 & " _Enter " & CStr(0.9*tip), 0)

    ' Join
    a0 = Rhino.JoinCurves(Array(e0, e1), True)

    ' Create the block
    Call Rhino.SelectObjects(a0)
    Call Rhino.Command("_-Block 0 " & Chr(34) & bname & Chr(34) & " _Enter _Enter _Enter", 0)

    ' Delete the block inserted by the Block command
    Call Rhino.DeleteObjects(Rhino.LastCreatedObjects)

    ' Enable redrawing
    Call Rhino.EnableRedraw(True)

  End If

  ' Insert the block
  Call Rhino.Command("_-Insert " & Chr(34) & bname & Chr(34) & " _Block", 0 )

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
' Draws Steel Angles
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
Sub SteelAngle

  Dim cmdname, configfile, section, tsection
  Dim filename, entries, entry, value, data, bname
  Dim tentries, tentry, tvalue
  Dim ip, xl, yl, thk
  Dim p0, p1, p2, p3, p4
  Dim e0, e1, a0

  cmdname = "Steel Angle"
  configfile = "STEEL.INI"
  section = "STEEL_ANGLE"
  tsection = "STEEL_ANGLE_THICKNESS"

  filename = Rhino.FindFile(configfile)
  If IsNull(filename) Then
    Call MsgBox("Unable to locate " & configfile & ".", 17, cmdname)
    Exit Sub
  End If

  entries = Rhino.GetSettings(filename, section)
  If IsNull(entries) Then Exit Sub

  entry = Rhino.ListBox(entries, "Select an angle", cmdname)
  If IsNull(entry) Then Exit Sub

  tentries = Rhino.GetSettings(filename, tsection)
  If IsNull(tentries) Then Exit Sub

  tentry = Rhino.ListBox(tentries, "Select an angle thickness", cmdname)
  If IsNull(tentry) Then Exit Sub

  tvalue = Rhino.GetSettings(filename, tsection, tentry)
  If IsNull(value) Then Exit Sub

  bname = Replace(entry, ".", "_") & Replace(tvalue, ".", "_")

  If Rhino.IsBlock(bname) = False Then

    value = Rhino.GetSettings(filename, section, entry)
    If IsNull(value) Then Exit Sub

    data = Rhino.Strtok(value, ", ;")
    If IsNull(data) Or (UBound(data) <> 1) Then Exit Sub

    ' Hide the dirty work      
    Call Rhino.EnableRedraw(False)

    ip = Array(0,0,0)
    xl = CDbl(data(0))
    yl = CDbl(data(1))
    thk = CDbl(tvalue)

    ' Top
    p0 = Rhino.Polar(ip, 90, yl)
    p1 = Rhino.Polar(ip, 0, xl)
    e0 = Rhino.AddPolyline(Array(ip, p0, ip, p1))

    ' Right
    p1 = Rhino.Polar(p0, 0, thk)
    p2 = Rhino.Polar(p1, 270, yl - thk)
    p3 = Rhino.Polar(p2, 0, xl - thk)
    p4 = Rhino.Polar(p3, 270, thk)
    e1 = Rhino.AddPolyline(Array(p0, p1, p2, p3, p4))
    Call Rhino.Command("_-FilletCorners _SelID " & e1 & " _Enter " & CStr(0.9*thk), 0 )

    ' Join
    a0 = Rhino.JoinCurves(Array(e0, e1), True)

    ' Create the block
    Call Rhino.SelectObjects(a0)
    Call Rhino.Command("_-Block 0 " & Chr(34) & bname & Chr(34) & " _Enter _Enter _Enter", 0)

    ' Delete the block inserted by the Block command
    Call Rhino.DeleteObjects(Rhino.LastCreatedObjects)

    ' Enable redrawing
    Call Rhino.EnableRedraw(True)

  End If

  ' Insert the block
  Call Rhino.Command("_-Insert " & Chr(34) & bname & Chr(34) & " _Block", 0 )

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
' Draws Steel T-Sections
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
Sub SteelTSection

  Dim cmdname, configfile, section
  Dim filename, entries, entry, value, data, bname
  Dim ip, d, b, tf, tw, tip
  Dim p0, p1, p2, p3, p4, p5
  Dim e0, e1, e2, e3, a0

  cmdname = "Steel T-Sections"
  configfile = "STEEL.INI"
  section = "STEEL_TSECTION"

  filename = Rhino.FindFile(configfile)
  If IsNull(filename) Then
    Call MsgBox("Unable to locate " & configfile & ".", 17, cmdname)
    Exit Sub
  End If

  entries = Rhino.GetSettings(filename, section)
  If IsNull(entries) Then Exit Sub

  entry = Rhino.ListBox(entries, "Select a channel", cmdname)
  If IsNull(entry) Then Exit Sub

  bname = Replace(entry, ".", "_")

  If Rhino.IsBlock(bname) = False Then

    value = Rhino.GetSettings(filename, section, entry)
    If IsNull(value) Then Exit Sub

    data = Rhino.Strtok(value, ", ;")
    If IsNull(data) Or (UBound(data) <> 3) Then Exit Sub

    ' Hide the dirty work      
    Call Rhino.EnableRedraw(False)

    ip = Array(0,0,0)
    d = CDbl(data(0))
    b = CDbl(data(1))
    tf = CDbl(data(2))
    tw = CDbl(data(3))

    ' Top
    p0 = Rhino.Polar(Rhino.Polar(ip, 0, b/2), 270, tf)
    p1 = Rhino.Polar(ip, 0, b/2)
    p2 = Rhino.Polar(ip, 180, b/2)
    p3 = Rhino.Polar(p0, 180, b)
    e0 = Rhino.AddPolyline(Array(p0, p1, p2, p3))

    ' Right
    p1 = Rhino.Polar(p0, 180, (b-tw)/2)
    p2 = Rhino.Polar(p1, 270, d-tf)
    p3 = Rhino.Polar(p2, 270, d-(tf*2))
    e1 = Rhino.AddPolyline(Array(p0, p1, p2, p3))
    Call Rhino.Command("_-FilletCorners _SelID " & e1 & " _Enter " & CStr(0.9*tf), 0)

    ' Mirror left
    e2 = Rhino.MirrorObject(e1, ip, Rhino.Polar(ip, 270, 1), True)

    ' Bottom
    e3 = Rhino.AddPolyline(Array(p3, Rhino.Polar(p3, 180, tw)))

    ' Join
    a0 = Rhino.JoinCurves(Array(e0, e1, e2, e3), True)

    ' Create the block
    Call Rhino.SelectObjects(a0)
    Call Rhino.Command("_-Block 0 " & Chr(34) & bname & Chr(34) & " _Enter _Enter _Enter", 0)

    ' Delete the block inserted by the Block command
    Call Rhino.DeleteObjects(Rhino.LastCreatedObjects)

    ' Enable redrawing
    Call Rhino.EnableRedraw(True)

  End If

  ' Insert the block
  Call Rhino.Command("_-Insert " & Chr(34) & bname & Chr(34) & " _Block", 0 )

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
' Startup and Aliases
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "SteelWideFlange", "_NoEcho _-RunScript (SteelWideFlange)"
Rhino.AddAlias "SteelChannel", "_NoEcho _-RunScript (SteelChannel)"
Rhino.AddAlias "SteelAngle", "_NoEcho _-RunScript (SteelAngle)"
Rhino.AddAlias "SteelTSection", "_NoEcho _-RunScript (SteelTSection)"
```

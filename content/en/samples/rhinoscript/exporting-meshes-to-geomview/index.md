+++
aliases = ["/en/5/samples/rhinoscript/exporting-meshes-to-geomview/", "/en/6/samples/rhinoscript/exporting-meshes-to-geomview/", "/en/7/samples/rhinoscript/exporting-meshes-to-geomview/", "/wip/samples/rhinoscript/exporting-meshes-to-geomview/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to export a mesh object to Geomview's OFF file format using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Exporting Meshes to Geomview"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/geomview"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ExportOff.rvb -- February 2009
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exports a mesh object to a Geomview .OFF file
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub ExportOff

  ' Local variables
  Dim strMesh, strFilter, strFileName
  Dim objFSO, objStream, i
  Dim v_count, v_list, v
  Dim f_count, f_list, f

  ' Pick a mesh object
  strMesh = Rhino.GetObject("Select mesh", 32)
  If IsNull(strMesh) Then Exit Sub

  ' Prompt the user to specify a file name    
  strFilter = "Geomview OFF (*.off)|*.off|"
  strFileName = Rhino.SaveFileName("Save As", strFilter)
  If IsNull(strFileName) Then Exit Sub

  ' Get the file system object
  Set objFSO = CreateObject("Scripting.FileSystemObject")

  ' Open a text file to write to
  On Error Resume Next
  Set objStream = objFSO.CreateTextFile(strFileName, True)
  If Err Then
    MsgBox Err.Description
    Exit Sub
  End If

  ' Write the header
  objStream.WriteLine("OFF")
  objStream.WriteLine("#")
  objStream.WriteLine("# " & strFileName)
  objStream.WriteLine("#")

  ' Write the vertex, face, and edge counts
  v_count = Rhino.MeshVertexCount(strMesh)
  f_count = Rhino.MeshFaceCount(strMesh)
  objStream.WriteLine(CStr(v_count) & " " & CStr(f_count) & " " & CStr(v_count*f_count))

  ' Write the vertices
  v_list = Rhino.MeshVertices(strMesh)
  For Each v In v_list
    objStream.WriteLine(CStr(v(0)) & " " & CStr(v(1)) & " " & CStr(v(2)))
  Next

  ' Write the faces
  f_list = Rhino.MeshFaceVertices(strMesh)
  For Each f In f_list
    If f(2) = f(3) Then
      objStream.WriteLine(CStr(3) & " " & CStr(f(0)) & " " & CStr(f(1)) & " " & CStr(f(2)))
    Else
      objStream.WriteLine(CStr(4) & " " & CStr(f(0)) & " " & CStr(f(1)) & " " & CStr(f(2)) & " " & CStr(f(3)))
    End If
  Next

  ' Close the file
  objStream.Close

  End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "ExportOff", "_NoEcho _-RunScript (ExportOff)"
```

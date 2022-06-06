+++
aliases = ["/5/samples/rhinoscript/save-video-card-info/", "/6/samples/rhinoscript/save-video-card-info/", "/7/samples/rhinoscript/save-video-card-info/", "/wip/samples/rhinoscript/save-video-card-info/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to save information about your system's video card to a text file using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Save Video Card Info"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/savevideoinfo"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' SaveVideoInfo.rvb -- April 2008
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.

Option Explicit

Sub SaveVideoInfo()

  Dim objShell, objNetwork, objFSO, objFolder, objStream
  Dim strDesktop, strFile, strName, strMsg

  Set objShell = CreateObject("WScript.Shell")
  Set objNetwork = CreateObject("WScript.Network")
  Set objFSO = CreateObject("Scripting.FileSystemObject")

  strName = "RhinoVideoInfo.txt"
  strDesktop = objShell.SpecialFolders("Desktop")
  strFile = strDeskTop & "\" & strName

  On Error Resume Next
  Set objStream = objFSO.CreateTextFile(strFile, True)
  If Err Then
    MsgBox Err.Description
    Exit Sub
  End If

  objStream.WriteLine "**************************"
  objStream.WriteLine "Rhino Video Info"
  objStream.WriteLine
  objStream.WriteLine "Computer Name = " & objNetwork.ComputerName
  objStream.WriteLine "Date and Time = " & CStr(Now)
  objStream.WriteLine "Rhino Build Date = " & CStr(Rhino.BuildDate)
  objStream.WriteLine "Rhino SDK Version = " & CStr(Rhino.SdkVersion)
  objStream.WriteLine "**************************"
  objStream.WriteLine

  Call DisplayConfiguration(objStream)
  Call VideoAdapterInformation(objStream)
  Call VideoControllerProperties(objStream)
  Call MonitorProperties(objStream)
  ' Uncomment the following line if you want the report to include
  ' all possible video card resolutions.
  ' Call VideoResolutions(objStream)

  objStream.Close

  strMsg = "A file named " & Chr(34) & strName & Chr(34) & VbCrLf
  strMsg = strMsg & "has been saved to your desktop." & VbCrLf & VbCrLf
  strMsg = strMsg & "If you are experiencing problems with Rhino," & VbCrLf
  strMsg = strMsg & "email this file to " & Chr(34) & "tech@mcneel.com" & Chr(34) & VbCrLf
  strMsg = strMsg & "along with a detailed description" & VbCrLf
  strMsg = strMsg & "of your problem."
  MsgBox strMsg, 64, "Rhinoceros"

End Sub

' Returns a list of all the possible video display resolutions.
Sub VideoResolutions(ByRef objStream)
  Dim strComputer, objWMIService, colItems, objItem
  objStream.WriteLine "**************************"
  objStream.WriteLine "Video Resolutions"
  objStream.WriteLine "**************************"
  objStream.WriteLine
  On Error Resume Next
  strComputer = "."
  Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
  Set colItems = objWMIService.ExecQuery ("Select * from CIM_VideoControllerResolution")
  For Each objItem In colItems
    objStream.WriteLine "Horizontal Resolution: " & objItem.HorizontalResolution
    objStream.WriteLine "Number Of Colors: " & objItem.NumberOfColors
    objStream.WriteLine "Refresh Rate: " & objItem.RefreshRate
    objStream.WriteLine "Scan Mode: " & objItem.ScanMode
    objStream.WriteLine "Setting ID: " & objItem.SettingID
    objStream.WriteLine "Vertical Resolution: " & objItem.VerticalResolution
    objStream.WriteLine
  Next
End Sub  

' Returns information about the current display settings.
Sub DisplayConfiguration(ByRef objStream)
  Dim strComputer, objWMIService, colItems, objItem
  objStream.WriteLine "**************************"
  objStream.WriteLine "Display Configuration"
  objStream.WriteLine "**************************"
  objStream.WriteLine
  On Error Resume Next
  strComputer = "."
  Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
  Set colItems = objWMIService.ExecQuery ("Select * from Win32_DisplayConfiguration")
  For Each objItem In colItems
    objStream.WriteLine "Bits Per Pel: " & objItem.BitsPerPel
    objStream.WriteLine "Device Name: " & objItem.DeviceName
    objStream.WriteLine "Display Flags: " & objItem.DisplayFlags
    objStream.WriteLine "Display Frequency: " & objItem.DisplayFrequency
    objStream.WriteLine "Driver Version: " & objItem.DriverVersion
    objStream.WriteLine "Log Pixels: " & objItem.LogPixels
    objStream.WriteLine "Pels Height: " & objItem.PelsHeight
    objStream.WriteLine "Pels Width: " & objItem.PelsWidth
    objStream.WriteLine "Setting ID: " & objItem.SettingID
    objStream.WriteLine "Specification Version: " & objItem.SpecificationVersion
    objStream.WriteLine
  Next
End Sub

' Returns information about the desktop monitor.  
Sub MonitorProperties(ByRef objStream)
  Dim strComputer, objWMIService, colItems, objItem
  objStream.WriteLine "**************************"
  objStream.WriteLine "Monitor Properties"
  objStream.WriteLine "**************************"
  objStream.WriteLine
  strComputer = "."
  Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
  Set colItems = objWMIService.ExecQuery("Select * from Win32_DesktopMonitor")
  For Each objItem In colItems
    objStream.WriteLine "Availability: " & objItem.Availability
    objStream.WriteLine "Bandwidth: " & objItem.Bandwidth
    objStream.WriteLine "Description: " & objItem.Description
    objStream.WriteLine "Device ID: " & objItem.DeviceID
    objStream.WriteLine "Display Type: " & objItem.DisplayType
    objStream.WriteLine "Is Locked: " & objItem.IsLocked
    objStream.WriteLine "Monitor Manufacturer: " & objItem.MonitorManufacturer
    objStream.WriteLine "Monitor Type: " & objItem.MonitorType
    objStream.WriteLine "Name: " & objItem.Name
    objStream.WriteLine "Pixels Per X Logical Inch: " & objItem.PixelsPerXLogicalInch
    objStream.WriteLine "Pixels Per Y Logical Inch: " & objItem.PixelsPerYLogicalInch
    objStream.WriteLine "PNP Device ID: " & objItem.PNPDeviceID
    objStream.WriteLine "Screen Height: " & objItem.ScreenHeight
    objStream.WriteLine "Screen Width: " & objItem.ScreenWidth
    objStream.WriteLine
  Next
End Sub

' Returns information about the video adapters.  
Sub VideoAdapterInformation(ByRef objStream)
  Dim strComputer, objWMIService, colItems, objItem
  objStream.WriteLine "**************************"
  objStream.WriteLine "Video Adapter Information"
  objStream.WriteLine "**************************"
  objStream.WriteLine
  On Error Resume Next
  strComputer = "."
  Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
  Set colItems = objWMIService.ExecQuery ("Select * from Win32_DisplayControllerConfiguration")
  For Each objItem In colItems
    objStream.WriteLine "Bits Per Pixel: " & objItem.BitsPerPixel
    objStream.WriteLine "Color Planes: " & objItem.ColorPlanes
    objStream.WriteLine "Device Entries in a Color Table: " & objItem.DeviceEntriesInAColorTable
    objStream.WriteLine "Device Specific Pens: " & objItem.DeviceSpecificPens
    objStream.WriteLine "Horizontal Resolution: " & objItem.HorizontalResolution
    objStream.WriteLine "Name: " & objItem.Name
    objStream.WriteLine "Refresh Rate: " & objItem.RefreshRate
    objStream.WriteLine "Setting ID: " & objItem.SettingID
    objStream.WriteLine "Vertical Resolution: " & objItem.VerticalResolution
    objStream.WriteLine "Video Mode: " & objItem.VideoMode
    objStream.WriteLine
  Next
End Sub

' Retrieves information about the video controller.
Sub VideoControllerProperties(ByRef objStream)
  Dim strComputer, objWMIService, colItems, objItem, strCapability
  objStream.WriteLine "**************************"
  objStream.WriteLine "Video Controller Properties"
  objStream.WriteLine "**************************"
  objStream.WriteLine
  On Error Resume Next
  strComputer = "."
  Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
  Set colItems = objWMIService.ExecQuery ("Select * from Win32_VideoController")
  For Each objItem In colItems
    For Each strCapability In objItem.AcceleratorCapabilities
      objStream.WriteLine "Accelerator Capability: " & strCapability
    Next
    objStream.WriteLine "Adapter Compatibility: " & objItem.AdapterCompatibility
    objStream.WriteLine "Adapter DAC Type: " & objItem.AdapterDACType
    objStream.WriteLine "Adapter RAM: " & objItem.AdapterRAM
    objStream.WriteLine "Availability: " & objItem.Availability
    objStream.WriteLine "Color Table Entries: " & objItem.ColorTableEntries
    objStream.WriteLine "Current Bits Per Pixel: " & objItem.CurrentBitsPerPixel
    objStream.WriteLine "Current Horizontal Resolution: " & objItem.CurrentHorizontalResolution
    objStream.WriteLine "Current Number of Colors: " & objItem.CurrentNumberOfColors
    objStream.WriteLine "Current Number of Columns: " & objItem.CurrentNumberOfColumns
    objStream.WriteLine "Current Number of Rows: " & objItem.CurrentNumberOfRows
    objStream.WriteLine "Current Refresh Rate: " & objItem.CurrentRefreshRate
    objStream.WriteLine "Current Scan Mode: " & objItem.CurrentScanMode
    objStream.WriteLine "Current Vertical Resolution: " & objItem.CurrentVerticalResolution
    objStream.WriteLine "Description: " & objItem.Description
    objStream.WriteLine "Device ID: " & objItem.DeviceID
    objStream.WriteLine "Device Specific Pens: " & objItem.DeviceSpecificPens
    objStream.WriteLine "Dither Type: " & objItem.DitherType
    objStream.WriteLine "Driver Date: " & objItem.DriverDate
    objStream.WriteLine "Driver Version: " & objItem.DriverVersion
    objStream.WriteLine "ICM Intent: " & objItem.ICMIntent
    objStream.WriteLine "ICM Method: " & objItem.ICMMethod
    objStream.WriteLine "INF Filename: " & objItem.InfFilename
    objStream.WriteLine "INF Section: " & objItem.InfSection
    objStream.WriteLine "Installed Display Drivers: " & objItem.InstalledDisplayDrivers
    objStream.WriteLine "Maximum Memory Supported: " & objItem.MaxMemorySupported
    objStream.WriteLine "Maximum Number Controlled: " & objItem.MaxNumberControlled
    objStream.WriteLine "Maximum Refresh Rate: " & objItem.MaxRefreshRate
    objStream.WriteLine "Minimum Refresh Rate: " & objItem.MinRefreshRate
    objStream.WriteLine "Monochrome: " & objItem.Monochrome
    objStream.WriteLine "Name: " & objItem.Name
    objStream.WriteLine "Number of Color Planes: " & objItem.NumberOfColorPlanes
    objStream.WriteLine "Number of Video Pages: " & objItem.NumberOfVideoPages
    objStream.WriteLine "PNP Device ID: " & objItem.PNPDeviceID
    objStream.WriteLine "Reserved System Palette Entries: " & objItem.ReservedSystemPaletteEntries
    objStream.WriteLine "Specification Version: " & objItem.SpecificationVersion
    objStream.WriteLine "System Palette Entries: " & objItem.SystemPaletteEntries
    objStream.WriteLine "Video Architecture: " & objItem.VideoArchitecture
    objStream.WriteLine "Video Memory Type: " & objItem.VideoMemoryType
    objStream.WriteLine "Video Mode: " & objItem.VideoMode
    objStream.WriteLine "Video Mode Description: " & objItem.VideoModeDescription
    objStream.WriteLine "Video Processor: " & objItem.VideoProcessor
    objStream.WriteLine
  Next
End Sub

' Rhino.AddStartUpScript Rhino.LastLoadedScriptFile
' Rhino.AddAlias "SavePlugInList", "_-RunScript (SaveVideoInfo)"

' Run it!
Call SaveVideoInfo
```

+++
aliases = ["/en/5/guides/rhinoscript/converting-to-grayscale/", "/en/6/guides/rhinoscript/converting-to-grayscale/", "/en/7/guides/rhinoscript/converting-to-grayscale/", "/en/wip/guides/rhinoscript/converting-to-grayscale/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide demonstrates how to convert an RGB color value to grayscale."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Converting to Grayscale"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/grayscale"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

 
## Overview

To convert any color to a grayscale representation of its luminance, first one must obtain the values of its red, green, and blue (RGB) primaries in linear intensity encoding, by gamma expansion.  Then, add together 30% of the red value, 59% of the green value, and 11% of the blue value. The resultant number is the desired linear luminance value; it typically needs to be gamma compressed to get back to a conventional grayscale representation.

## Example

The following example demonstrates the above algorithm...

```vbnet
Option Explicit

Sub ConvertLayersToGrayscale()

  ' Declare local variables
  Dim arrLayers, strLayer, lngColor
  Dim nGray, nRed, nGreen, nBlue

  ' Turn off screen redrawing (for performance)
  Call Rhino.EnableRedraw(False)

  ' Get all of the layers in the document
  arrLayers = Rhino.LayerNames

  ' Process each layer one-by-one
  For Each strLayer In arrLayers

    ' Get the layer's color
    lngColor = Rhino.LayerColor(strLayer)

    ' Get the color's red-green-blue components
    nRed = Rhino.ColorRedValue(lngColor)
    nGreen = Rhino.ColorGreenValue(lngColor)
    nBlue = Rhino.ColorBlueValue(lngColor)

    ' Calculate the grayscale based on the NTSC color gamut
    nGray = CByte(nRed * 0.30) + CByte(nGreen * 0.59) + CByte(nBlue * 0.11)

    ' Modify the layer's color
    Call Rhino.LayerColor(strlayer, RGB(nGray, nGray, nGray))

  Next

  ' Turn on screen redrawing
  Call Rhino.EnableRedraw(True)

End Sub
```

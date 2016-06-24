---
title: Determine Language Setting
description: Demonstrates how to determine Rhino's language setting.
author: steve@mcneel.com
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/determinecurrentlanguage
order: 1
keywords: ['determine', 'rhinos', 'language', 'setting']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result DetermineCurrentLanguage(RhinoDoc doc)
  {
    var language_id = Rhino.ApplicationSettings.AppearanceSettings.LanguageIdentifier;
    var culture = new System.Globalization.CultureInfo(language_id);
    RhinoApp.WriteLine("The current language is {0}", culture.EnglishName);
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function DetermineCurrentLanguage(ByVal doc As RhinoDoc) As Result
	Dim language_id = Rhino.ApplicationSettings.AppearanceSettings.LanguageIdentifier
	Dim culture = New System.Globalization.CultureInfo(language_id)
	RhinoApp.WriteLine("The current language is {0}", culture.EnglishName)
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs
import System

locale_id = rs.LocaleID()
culture = System.Globalization.CultureInfo(locale_id)
print culture.EnglishName
```
{: #py .tab-pane .fade .in}

---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Determine Rhino's Language Setting
keywords: ['determine', 'rhinos', 'language', 'setting']
categories: ['Other']
description:
order: 1
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
{: #vb .tab-pane .fade .in .active}


```python
import rhinoscriptsyntax as rs
import System

locale_id = rs.LocaleID()
culture = System.Globalization.CultureInfo(locale_id)
print culture.EnglishName
```
{: #py .tab-pane .fade .in .active}


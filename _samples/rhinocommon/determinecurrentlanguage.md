---
layout: code-sample
title: Determine Rhino's Language Setting
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['determine', 'rhinos', 'language', 'setting']
order: 56
description:  
---



```cs
public class DetermineCurrentLanguageCommand : Command
{
  public override string EnglishName { get { return "csCurrentLanguage"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Public Class DetermineCurrentLanguageCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbCurrentLanguage"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
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



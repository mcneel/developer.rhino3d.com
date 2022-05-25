+++
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to determine Rhino's language setting."
keywords = [ "determine", "rhinos", "language", "setting" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Determine Language Setting"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/determinecurrentlanguage"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

<div class="codetab-content" id="cs">

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

</div>


<div class="codetab-content" id="vb">

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

</div>


<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs
import System

locale_id = rs.LocaleID()
culture = System.Globalization.CultureInfo(locale_id)
print culture.EnglishName
```

</div>

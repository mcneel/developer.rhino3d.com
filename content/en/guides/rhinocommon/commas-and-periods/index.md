+++
aliases = ["/5/guides/rhinocommon/commas-and-periods/", "/6/guides/rhinocommon/commas-and-periods/", "/7/guides/rhinocommon/commas-and-periods/", "/wip/guides/rhinocommon/commas-and-periods/"]
authors = [ "steve" ]
categories = [ "Fundamentals" ]
description = "This guide demonstrates how to consistently read/write numbers to strings."
keywords = [ "RhinoCommon", "Locale", "Threads", "Culture", "Internationalization", "Commas", "Periods" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Commas & Periods"
type = "guides"
weight = 2
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/developer/sdksamples/threadculture"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## English Culture

Depending on the user's culture settings, their computer may be set up to use commas instead of periods for decimal separators. This can cause problems when writing numbers into xml files and reading these xml files on a different culture setting.

An easy way around this problem is to temporarily adjust the application's culture settings when reading/writing files to always use a single culture...

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'vb')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content" id="cs">

```cs
// save current culture
System.Globalization.CultureInfo current_culture = System.Threading.Thread.CurrentThread.CurrentCulture;

// create and set english-us culture
System.Globalization.CultureInfo us_culture = new System.Globalization.CultureInfo("en-us");
System.Threading.Thread.CurrentThread.CurrentCulture = us_culture;

int rc = WriteMyFile( filename );

// restore the saved culture
System.Threading.Thread.CurrentThread.CurrentCulture = current_culture;

```

</div>

<div class="codetab-content" id="vb">

```vbnet
' save current culture
Dim current_culture As System.Globalization.CultureInfo = System.Threading.Thread.CurrentThread.CurrentCulture

' create and set english-us culture
Dim us_culture As new System.Globalization.CultureInfo("en-us")
System.Threading.Thread.CurrentThread.CurrentCulture = us_culture

Dim rc As Integer = WriteMyFile( filename )

' restore the saved culture
System.Threading.Thread.CurrentThread.CurrentCulture = current_culture
```

</div>
</div>

---
title: Commas & Periods
description: This guide demonstrates how to consistently read/write numbers to strings.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: https://wiki.mcneel.com/developer/sdksamples/threadculture
order: 2
keywords: ['RhinoCommon', 'Locale', 'Threads', 'Culture', 'Internationalization', 'Commas', 'Periods']
layout: toc-guide-page
---

 
## English Culture

Depending on the user's culture settings, their computer may be set up to use commas instead of periods for decimal separators. This can cause problems when writing numbers into xml files and reading these xml files on a different culture setting.

An easy way around this problem is to temporarily adjust the application's culture settings when reading/writing files to always use a single culture...

<ul class="nav nav-pills">
  <li class="active"><a href="#cs" data-toggle="pill">C#</a></li>
  <li><a href="#vb" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

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
{: #cs .tab-pane .fade .in .active}

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
{: #vb .tab-pane .fade .in}

</div>

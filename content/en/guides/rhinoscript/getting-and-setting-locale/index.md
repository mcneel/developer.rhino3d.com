+++
aliases = ["/5/guides/rhinoscript/getting-and-setting-locale/", "/6/guides/rhinoscript/getting-and-setting-locale/", "/7/guides/rhinoscript/getting-and-setting-locale/", "/wip/guides/rhinoscript/getting-and-setting-locale/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide demonstrates how to format locale-sensitive numbers using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Getting & Setting Locale"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/getlocale"
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

Formatted numbers are locale-sensitive.  That is, the way numbers are formatted differs depending on which region of the world you are in.

Here are a few examples:

| Culture       |   Format     |
| :------------ | -----------: |
| United States | 1,234,567.89 |
| France        | 1 234 567,89 |
| German        | 1.234.567,89 |
| Switzerland   | 1’234’567.89 |


## Details

VBScript supports the functionality of retrieving and changing the current locale settings of your computer.  The two functions that support this feature are `GetLocale()` and `SetLocale()`.  `GetLocale()` returns the current locale on the client machine.  `SetLocale()` sets the locale to the new specified locale.  These functions can be used accordingly to localize numeric values.

The `SetLocale()` function requires one argument, the LCID, which is a short string, decimal value, or hex value that uniquely identifies a geographic locale.  The various geographic locales are based upon the user's language, country, and culture. For example, the locale "English - United States" can be designated as either "en-us", or "1033", or "0x0409".

This locale information is used to establish user preferences and formats for such things as alphabets, currency, dates, keyboard layout, and numbers.  A list of these locales, and their return values, can be found on the [MSDN Locale ID (LCID) Chart](https://msdn.microsoft.com/en-us/library/0h88fahh(v=vs.85).aspx).

**NOTE**: If the LCID argument is set to zero, the locale will be set by the system.

The following examples demonstrates the use of the `SetLocale()` function:

```vbnet
Sub TestLocale()

  Dim dblValue : dblValue = 1234567.89

  Call SetLocale(1033) 'English - United States
  Rhino.Print "English - United States = " & FormatNumber(dblValue)

  Call SetLocale(1036) 'French - France
  Rhino.Print "French - France = " & FormatNumber(dblValue)

  Call SetLocale(1031) 'German - Germany
  Rhino.Print "German - Germany = " & FormatNumber(dblValue)

  Call SetLocale(2055) 'German - Switzerland
  Rhino.Print "German - Switzerland = " & FormatNumber(dblValue)

  Call SetLocale(0)

End Sub
```

which outputs:

```vbs
English - United States = 1,234,567.89
French - France = 1 234 567,89
German - Germany = 1.234.567,89
German - Switzerland = 1'234'567.89
```

## Related Topics

- [Locale ID (LCID) Chart on MSDN](https://msdn.microsoft.com/en-us/library/0h88fahh(v=vs.85).aspx)

+++
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide demonstrates an easy way to make a plugin expire using C/C++."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Making Plugins That Expire"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/pluginexpire"
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

 
## Problem

You would like to release a work-in-progress, or WIP, version of your plugin so you can get some customer feedback before shipping.  You would like the plugin to expire after a number of days.  Is there something in Rhino that could help with this?

## Solution

Rhino does not have any feature that can help with this.  But, it is not too difficult to compare the compile date of the plugin with the current date to see if you plugin should load or not.  The following example code demonstrates this...

## Sample

```cpp
BOOL CTestPlugIn::OnLoadPlugIn()
{
#if defined(WIP)

  // Easy cheezy way of testing to see if plugin has expired.
  COleDateTime compile_time;
  compile_time.ParseDateTime( ON_wString(__DATE__" "__TIME__), 0, 0x0409 );

  COleDateTime current_time( COleDateTime::GetCurrentTime() );

  COleDateTimeSpan span = current_time - compile_time;
  int elapsed_days = span.GetDays();

  const int warn_after_days = 30;   // or whatever...
  const int expire_after_days = 40; // or whatever...

  if( elapsed_days >= warn_after_days )
  {
    HWND hWnd = RhinoApp().MainWnd();
    if( elapsed_days >= expire_after_days )
    {
      ON_wString str = L"This WIP has expired. Please download the latest and greatest...";
      ::MessageBox( hWnd, str, PlugInName(), MB_OK | MB_ICONERROR );
      return -1; // This will cause the plugin not to load and not display an Rhino error.
    }
    else
    {
      ON_wString str;
      str.Format( L"This WIP will expire in %d days. Please download the latest and greatest...", expire_after_days - elapsed_days );
      ::MessageBox( hWnd, str, PlugInName(), MB_OK | MB_ICONEXCLAMATION );
    }
  }
#endif

  // If we got here, then the WIP was good.
  // So, do other plugin initialization
  // and return TRUE to run.

  return TRUE;
}
```

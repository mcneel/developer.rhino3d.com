+++
aliases = ["/en/5/guides/cpp/saving-persistent-settings/", "/en/6/guides/cpp/saving-persistent-settings/", "/en/7/guides/cpp/saving-persistent-settings/", "/wip/guides/cpp/saving-persistent-settings/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses how to save plugin settings to the Registry using C/C++."
keywords = [ "rhino", "registry", "settings" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Saving Persistent Settings"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/pluginsettings"
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

Your plugin maintains a number of settings that need to be retained between sessions.  Is there an easy way to do this?  Do these setting migrate from one Rhino service release to another?

## Solution

You can load and save persistent plugin setting from and to the Registry using the `CRhinoPlugIn::LoadProfile` and `CRhinoPlugIn::SaveProfile` virtual functions.  For information on these virtual function, see *rhinoSdkPlugIn.h*.

## How To

Lets say we have a sample plugin class declaration that looks something like the following:

```cpp
class CTestPlugIn : public CRhinoUtilityPlugIn
{
public:
  CTestPlugIn();
  ~CTestPlugIn();

  // Required overrides
  const wchar_t* PlugInName() const;
  const wchar_t* PlugInVersion() const;
  GUID PlugInID() const;
  BOOL OnLoadPlugIn();
  void OnUnloadPlugIn();

 private:
  ON_wString m_plugin_version;

  // Persistent data
  bool m_value0;
  int m_value1;
  double m_value2;
  ON_wString m_value3;
};
```

Simply, overload the `CRhinoPlugIn::LoadProfile` and `CRhinoPlugIn::SaveProfile` virtual functions by adding the the following public declarations to our plugin class:

```cpp
void LoadProfile( LPCTSTR lpszSection, CRhinoProfileContext& pc );
void SaveProfile( LPCTSTR lpszSection, CRhinoProfileContext& pc );
```

Then, provide the definition:

```cpp
void CTestPlugIn::LoadProfile( LPCTSTR lpszSection, CRhinoProfileContext& pc )
{
  pc.LoadProfileBool( lpszSection, L"value0", &m_value0 );
  pc.LoadProfileInt( lpszSection, L"value1", &m_value1 );
  pc.LoadProfileDouble( lpszSection, L"value2", &m_value2 );
  pc.LoadProfileString( lpszSection, L"value3", m_value3 );
}

void CTestPlugIn::SaveProfile( LPCTSTR lpszSection, CRhinoProfileContext& pc )
{
  pc.SaveProfileBool( lpszSection, L"value0", m_value0 );
  pc.SaveProfileInt( lpszSection, L"value1", m_value1 );
  pc.SaveProfileDouble( lpszSection, L"value2", m_value2 );
  pc.SaveProfileString( lpszSection, L"value3", m_value3 );
}
```

That's it! Your data is now saved at the following location in the Registry:

```
HKEY_CURRENT_USER\Software\McNeel\Rhinoceros\<version>\<scheme>\Plug-ins\<plugin_id>\Settings
```

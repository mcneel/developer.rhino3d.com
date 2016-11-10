---
title: Determining Language Setting
description: This guide demonstrates how to determine the language setting when developing localized C/C++ plugins.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/determinecurrentlanguage
order: 1
keywords: ['rhino', 'language']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

Rhino provides support for multiple languages.  Rhino's language setting is independent of the operating system's language setting.  Thus, as a plugin developer, knowing Rhino's current language setting is important if you plan on supporting multiple languages.

Rhino stores its current Locale ID (LCID) in a `CRhinoAppAppearanceSettings` object that is held within Rhino applications settings object, or `CRhinoAppSettings`.

## Sample

The following is an example of how to determine Rhino's current language setting.

```cpp
ON_wString wstr;
CRhinoAppSettings settings = ::RhinoApp().AppSettings();
CRhinoAppAppearanceSettings appearance = settings.AppearanceSettings();

switch( appearance.m_language_identifier )
{
case 1028: // zh-tw
  wstr = L"Chinese - Taiwan";
  break;
case 1029: // cs
  wstr = L"Czech";
  break;
case 1031: // de-de
  wstr = L"German - Germany";
  break;
case 1033: // en-us
  wstr = L"English - United States";
  break;
case 1034: // es-es
  wstr = L"Spanish - Spain";
  break;
case 1036: // fr-fr
  wstr = L"French - France";
  break;
case 1040: // it-it
  wstr = L"Italian - Italy";
  break;
case 1041: // ja
  wstr = L"Japanese";
  break;
case 1042: // ko
  wstr = L"Korean";
  break;
case 1045: // pl
  wstr = L"Polish";
  break;
case 2052: // zh-cn
  wstr = L"Chinese - China";
  break;
default:
  wstr = L"unknown";
  break;
}
::RhinoApp().Print( L"The current language is \"%s\ , wstr );
```

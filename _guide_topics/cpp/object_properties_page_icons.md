---
title: Object Properties Page Icons
description: This brief guide discusses how to provide an icon for a custom object properties page using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/objpropicon
order: 1
keywords: ['rhino', 'properties', 'icon']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

In Rhino, the object properties dialog shows a list of icons that allows you to select between the available properties pages.  You would like to add a custom icon to the object properties dialog when your plugin adds a custom page.

## Solution

Derive your custom object properties page from `CRhinoObjectPropertiesDialogPageEx`, which has a virtual `Icon()` member that you must override and implement.  You will want to implement this virtual function as follows:

```cpp
HICON CTestObjectPropertiesPageExDlg::Icon() const
{
  AFX_MANAGE_STATE( AfxGetStaticModuleState() );
  return (HICON)::LoadImage(AfxGetInstanceHandle(), MAKEINTRESOURCE(IDI_OBJPROPPAGE_DIALOG), IMAGE_ICON, 24, 24, LR_SHARED);
}
```

**NOTE**: Make carefully the `AFX_MANAGE_STATE` macro.  See [MFC Technical Notes 33](https://msdn.microsoft.com/en-us/library/hw85e4bb.aspx) and [58](https://msdn.microsoft.com/en-us/library/ft1t4bbc.aspx) for additional details.

## Related Topics

- [TN033: DLL Version of MFC (on MSDN)](https://msdn.microsoft.com/en-us/library/hw85e4bb.aspx)
- [TN058: MFC Module State Implementation (on MSDN)](https://msdn.microsoft.com/en-us/library/ft1t4bbc.aspx)

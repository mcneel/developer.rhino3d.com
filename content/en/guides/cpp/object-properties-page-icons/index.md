+++
aliases = ["/en/5/guides/cpp/object-properties-page-icons/", "/en/6/guides/cpp/object-properties-page-icons/", "/en/7/guides/cpp/object-properties-page-icons/", "/wip/guides/cpp/object-properties-page-icons/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide discusses how to provide an icon for a custom object properties page using C/C++."
keywords = [ "rhino", "properties", "icon" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Object Properties Page Icons"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/objpropicon"
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

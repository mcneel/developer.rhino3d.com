+++
aliases = ["/5/guides/cpp/using-activex-controls/", "/6/guides/cpp/using-activex-controls/", "/7/guides/cpp/using-activex-controls/", "/wip/guides/cpp/using-activex-controls/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide discusses how to use ActiveX controls in C/C++ plugins."
keywords = [ "rhino", "activex" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Using ActiveX Controls"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/activexcontrols"
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

ActiveX controls placed in a simple dialog box will crash Rhino.

## Solution

ActiveX, or OLE, controls work in Rhino plugins, as C/C++ plugin are simply regular MFC DLLs.  For more information on MFC DLLs, read [MFC Technical Note 33](http://msdn.microsoft.com/en-us/library/hw85e4bb(v=VS.80).aspx) and [MFC Technical Note 58](http://msdn.microsoft.com/en-us/library/ft1t4bbc(v=VS.80).aspx) for more information.

Also, you will need to call this function:

```cpp
void AfxEnableControlContainer();
```

in your `CWinApp`-derived object's `InitInstance()` member to enable support for containment of OLE controls.

## Related Topics

- [MFC ActiveX Controls (on MSDN)](https://msdn.microsoft.com/en-us/library/k194shk8(v=VS.80).aspx)
- [MFC Technical Note 33 (on MSDN)](http://msdn.microsoft.com/en-us/library/hw85e4bb(v=VS.80).aspx)
- [MFC Technical Note 58](http://msdn.microsoft.com/en-us/library/ft1t4bbc(v=VS.80).aspx)

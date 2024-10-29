+++
aliases = ["/en/5/guides/cpp/handling-enter-esc-from-modal-dialogs/", "/en/6/guides/cpp/handling-enter-esc-from-modal-dialogs/", "/en/7/guides/cpp/handling-enter-esc-from-modal-dialogs/", "/en/wip/guides/cpp/handling-enter-esc-from-modal-dialogs/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide discusses preventing modal dialogs from closing when the Enter or Escape key is pressed."
keywords = [ "rhino", "escape", "enter" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Handling Enter and Escape from Modal Dialogs"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/escmodaldialog"
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

The problem is simple: how to stop my MFC modal dialog box from closing when the user presses the <kbd>Enter</kbd> or <kbd>Escape</kbd> keys?

## Solution

The first step is to, on your CDialog-drived class, override the `CWnd::PreTranslateMessage` virtual function.  This function is used translate window messages before they are dispatched to the `TranslateMessage` and `DispatchMessage` Windows functions.  Then, add the following block of code:

```cpp
BOOL CMyModalDialog::PreTranslateMessage( MSG* pMsg )
{
  if( pMsg )
  {
    if( pMsg->message == WM_KEYDOWN )
    {
      if( pMsg->wParam == VK_RETURN | pMsg->wParam == VK_ESCAPE )
        pMsg->wParam = NULL;
    }
  }
  // Call the base class PreTranslateMessage. In this example,
  // CRhinoDialog is the base class to CMyModalDialog.
  return CRhinoDialog::PreTranslateMessage( pMsg );
}
```

---
title: Handling Enter and Escape from Modal Dialogs
description: This guide discusses preventing modal dialogs from closing when the Enter or Escape key is pressed.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/escmodaldialog
order: 1
keywords: ['rhino', 'escape', 'enter']
layout: toc-guide-page
---

# Handling Enter and Escape from Modal Dialogs

{{ page.description }}

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

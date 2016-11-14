---
title: Canceling Long Processes with ESC
description: This guide demonstrates two methods for checking the Escape key.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/escape
order: 1
keywords: ['rhino', 'esc', 'commands']
layout: toc-guide-page
---

 
## Overview

When writing commands that contain long, time-consuming tasks, you might want to allow the user to cancel the process or command.  Here are a couple examples of ways this can be achieved...

## Example 1

The following example demonstrates how to periodically test to see if the user pressed the <kbd>ESC</kbd> key by "peeking" in Rhino's message queue...

```cpp
//  -1 = Quit Rhino
//   1 = Escape key pressed
//   0 = Okay to proceed
int EscapeKeyPressed()
{
  AFX_MANAGE_STATE( RhinoApp().RhinoModuleState() );

  MSG msg;
  memset( &msg, 0, sizeof(MSG) );
  while( ::PeekMessage(&msg, 0, 0, 0, PM_NOREMOVE) )
  {
    if( msg.message == WM_KEYDOWN && msg.wParam == VK_ESCAPE )
      return 1;

    if( !RhinoApp().PumpMessage() )
      return -1;
  }

  return 0;
}
```

Using this function is quite simple: in the middle of your loop, call the above function.  If the function returns something other than 0, break out of your loop.

## Example 2

The following sample class demonstrates how to hook the Windows keyboard from a Rhino plugin and check for the <kbd>ESC</kbd> key.

```cpp
//
// rhinoEscapeKey.h
//

class CRhinoEscapeKey
{
public:
  CRhinoEscapeKey( bool bHookNow = false );
  ~CRhinoEscapeKey();
  bool Start();
  void Stop();
  bool EscapeKeyPressed() const;
  void ClearEscapeKeyPressedFlag();
protected:
  static LRESULT CALLBACK HookProc( int code, WPARAM wParam, LPARAM lParam );
  static HHOOK m_KeyboardHookProc;
  static bool m_escape_pressed;
};

//
// rhinoEscapeKey.cpp
//

bool CRhinoEscapeKey::m_escape_pressed = false;
HHOOK CRhinoEscapeKey::m_KeyboardHookProc = NULL;

CRhinoEscapeKey::CRhinoEscapeKey( bool bStartNow )
{
  if( bStartNow )
    Start();
}

CRhinoEscapeKey::~CRhinoEscapeKey()
{
  Stop();
}

bool CRhinoEscapeKey::Start()
{
  if( NULL == m_KeyboardHookProc )
    m_KeyboardHookProc = ::SetWindowsHookEx(
                              WH_KEYBOARD,
                              CRhinoEscapeKey::HookProc,
                              RhinoApp().RhinoInstanceHandle(),
                              ::AfxGetThread()->m_nThreadID
                              );
  ClearEscapeKeyPressedFlag();
  return( NULL != m_KeyboardHookProc );
}

void CRhinoEscapeKey::Stop()
{
  if( m_KeyboardHookProc )
    UnhookWindowsHookEx( m_KeyboardHookProc );
  m_KeyboardHookProc = NULL;
}

bool CRhinoEscapeKey::EscapeKeyPressed() const
{
  RhinoApp().Wait(0);
  return m_escape_pressed;
}

void CRhinoEscapeKey::ClearEscapeKeyPressedFlag()
{
  m_escape_pressed = false;
}

LRESULT CALLBACK CRhinoEscapeKey::HookProc( int code, WPARAM wParam, LPARAM lParam )
{
  // On escape key down....
  if( code == HC_ACTION && wParam == VK_ESCAPE && !(lParam & 0x80000000) )
  {
    m_escape_pressed = true;
    UnhookWindowsHookEx( m_KeyboardHookProc );
    m_KeyboardHookProc = NULL;
    return 0; // Eat the escape key
  }
  // call next hook proc including standard windows proc.
  return CallNextHookEx( m_KeyboardHookProc, code, wParam, lParam );
}
```

## Usage

The following sample code demonstrates using the `CRhinoEscapeKey` class within a Rhino command...

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoEscapeKey escape;
  escape.Start();

  int i = 0;
  while( true )
  {
    if( escape.EscapeKeyPressed() )
    {
      escape.Stop();
      RhinoApp().Print( L"Command canceled.\n" );
      break;
    }
    RhinoApp().Print( L"Count = %d.\n", ++i );
  }

  return success;
}
```

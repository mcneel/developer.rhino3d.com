---
title: Custom Undo Events
description: This guide discusses custom undo events.
author: ['Dale Fugier', '@dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/customundo
order: 1
keywords: ['rhino', 'undo']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

The Rhino C/C++ SDK supports adding custom undo events.  This way plugins can take advantage of Rhino's built in *Undo*, *Redo*, *UndoSelected*, *UndoMultiple*, *RedoMultiple* and *ClearUndo* commands, and any future Rhino commands that deal with undo/redo operations.

## How To

Basically, you create a class derived from `CRhinoUndoEventHandler`, pass it to Rhino, and let Rhino deal with all the details.  Sample 1 below shows how to do this.

In order to have stable plugins, developers must follow the rules for using `CRhinoDoc::AddCustomUndoEvent`...

```cpp
// Description:
//   If you want to your plugin to do something when the Rhino
//   Undo/Redo command runs, the call AddCustomUndoEvent during
//   your command.
//
//   This function is for expert plugin developers.  If you
//   don't do a good job here, you will really break Rhino.
//
// Parameters:
//   undo_event_handler - [in]
//     Pointer to a class allocated with a call to new.
//     Never delete this class.
//     Never pass a pointer to a stack variable.
//
// Returns:
//   If a non zero number is returned, then this is the runtime
//   serial number Rhino has assigned to this undo event.
//   If zero is returned, then the user has disabled undo
//   and undo_event_handler was deleted.

unsigned int AddCustomUndoEvent(
  CRhinoUndoEventHandler* undo_event_handler
  );
```

When you are debugging your code, you may find the *AuditUndo* command useful.  This command lists all the undo information saved in Rhino.

You can also use and event watcher to monitor Rhino undo/redo activity.  Sample 2 (below) is a simple undo event watcher that reports undo activity in the Rhino command windows...

## Samples

### Sample 1

This "plugin" has one piece of data, the account balance, and two commands, *EarnTenEuros* and *SpendFiveEuros*.  The commands use `CUndoEuroTransaction` class to provide integrated Undo/Redo support...

```cpp
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
//
// BEGIN CUndoEuroTransaction class definition
//

static double m_plugin_data_euro_balance = 0.0;

class CUndoEuroTransaction : public CRhinoUndoEventHandler
{
public:
  CUndoEuroTransaction();
  ~CUndoEuroTransaction();

  // virtual CRhinoUndoEventHandler function
  void Undo(
    const CRhinoCommand* cmd,
    const wchar_t* action_description,
    bool bCreatedByRedo,
    unsigned int undo_event_sn
    );

  double m_amount;
};

CUndoEuroTransaction::CUndoEuroTransaction()
{
  m_amount = 0.0;
}

CUndoEuroTransaction::~CUndoEuroTransaction()
{
}

void CUndoEuroTransaction::Undo(
  const CRhinoCommand* cmd,
  const wchar_t* action_description,
  bool bCreatedByRedo,
  unsigned int undo_event_sn
  )
{
  // undo the change to m_plugin_data_euro_balance
  m_plugin_data_euro_balance -= m_amount;
  RhinoApp().Print(L"New balance %g euros.\n",
                  m_plugin_data_euro_balance);
}

//
// END CUndoEuroTransaction class definition
//
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
//
// BEGIN EarnTenEuros command
//

class CCommandEarnTenEuros : public CRhinoCommand
{
public:
  CCommandEarnTenEuros() {}
  ~CCommandEarnTenEuros() {}
  UUID CommandUUID()
  {
    // {658C21B8-221-4887-B4A4-09C39C3E38CA}
    static const GUID EarnTenEurosCommand_UUID =
    { 0x658C21B8, 0x221, 0x4887, { 0xB4, 0xA4, 0x09, 0xC3, 0x9C, 0x3E, 0x38, 0xCA } };
    return EarnTenEurosCommand_UUID;
  }
  const wchar_t* EnglishCommandName() { return L"EarnTenEuros"; }
  CRhinoCommand::result RunCommand( const CRhinoCommandContext& );
};

// The one and only CCommandEarnTenEuros object
static class CCommandEarnTenEuros theEarnTenEurosCommand;

CRhinoCommand::result
CCommandEarnTenEuros::RunCommand( const CRhinoCommandContext& context )
{
  double amount = 10.0;

  CUndoEuroTransaction* pUndoHandler = new CUndoEuroTransaction();
  pUndoHandler->m_amount = amount;
  context.m_doc.AddCustomUndoEvent(pUndoHandler);

  m_plugin_data_euro_balance += amount;
  RhinoApp().Print(L"New balance %g euros.\n", m_plugin_data_euro_balance);
  return CRhinoCommand::success;
}

//
// END EarnTenEuros command
//
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
//
// BEGIN SpendFiveEuros command
//

class CCommandSpendFiveEuros : public CRhinoCommand
{
public:
  CCommandSpendFiveEuros() {}
  ~CCommandSpendFiveEuros() {}
  UUID CommandUUID()
  {
    // {578712DE-D65C-4B9C-9EE6-401C57077057}
    static const GUID SpendFiveEurosCommand_UUID =
    { 0x578712DE, 0xD65C, 0x4B9C, { 0x9E, 0xE6, 0x40, 0x1C, 0x57, 0x07, 0x70, 0x57 } };
    return SpendFiveEurosCommand_UUID;
  }
  const wchar_t* EnglishCommandName() { return L"SpendFiveEuros"; }
  CRhinoCommand::result RunCommand( const CRhinoCommandContext& );
};

// The one and only CCommandSpendFiveEuros object
static class CCommandSpendFiveEuros theSpendFiveEurosCommand;

CRhinoCommand::result
CCommandSpendFiveEuros::RunCommand( const CRhinoCommandContext& context )
{
  double amount = -5.0;

  CUndoEuroTransaction* pUndoHandler = new CUndoEuroTransaction();
  pUndoHandler->m_amount = amount;
  context.m_doc.AddCustomUndoEvent(pUndoHandler);

  m_plugin_data_euro_balance += amount;
  RhinoApp().Print(L"New balance %g euros.\n", m_plugin_data_euro_balance);
  return CRhinoCommand::success;
}

//
// END SpendFiveEuros command
//
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
```

### Sample 2

Using an event watcher to monitor undo events...

```cpp
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
//
// BEGIN CMyUndoSnooper undo event watcher
//

class CMyUndoSnooper : public CRhinoEventWatcher
{
public:
  // virtual
  void UndoEvent(
        CRhinoEventWatcher::undo_event event,
        unsigned int undo_record_serialnumber,
        const CRhinoCommand* cmd
        );
};

void CMyUndoSnooper::UndoEvent(
        CRhinoEventWatcher::undo_event event,
        unsigned int undo_record_serialnumber,
        const CRhinoCommand* cmd
        )
{
  CRhinoApp& app = RhinoApp();

  const wchar_t* cmd_name = cmd
                          ? cmd->LocalCommandName()
                          : 0;

  if( 0 == cmd_name )
    cmd_name = L;

  switch(event)
  {
  case begin_recording:  // Begin recording changes
    app.Print(L"UNDO SNOOP %5d: Begin recording %s changes\n",
                  undo_record_serialnumber,cmd_name);
    break;
  case end_recording:
    app.Print(L"UNDO SNOOP %5d: End recording %s changes\n",
                  undo_record_serialnumber,cmd_name);
    break;

  case begin_undo:       // Begin undoing a changes
    app.Print(L"UNDO SNOOP %5d: Begin undoing %s changes\n",
                  undo_record_serialnumber,cmd_name);
    break;
  case end_undo:
    app.Print(L"UNDO SNOOP %5d: End undoing %s changes\n",
                  undo_record_serialnumber,cmd_name);
    break;

  case begin_redo:       // Begin redoing a changes
    app.Print(L"UNDO SNOOP %5d: Begin redoing %s changes\n",
                  undo_record_serialnumber,cmd_name);
    break;
  case end_redo:
    app.Print(L"UNDO SNOOP %5d: End redoing %s changes\n",
                  undo_record_serialnumber,cmd_name);
    break;

  case purge_record:
    app.Print(L"UNDO SNOOP %5d: Purging %s changes\n",
                  undo_record_serialnumber,cmd_name);
    break;
  }
}

//
// END CMyUndoSnooper undo event watcher
//
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
//
// BEGIN TestUndoSnoop command
//

class CCommandTestUndoSnoop : public CRhinoTestCommand
{
public:
  CCommandTestUndoSnoop() { m_bRegistered = 0; }
  ~CCommandTestUndoSnoop() {}
  UUID CommandUUID()
  {
    // {A7474CED-3C3D-4BCD-9124-4058D619BEA0}
    static const GUID TestUndoSnoopCommand_UUID =
    { 0xA7474CED, 0x3C3D, 0x4BCD, { 0x91, 0x24, 0x40, 0x58, 0xD6, 0x19, 0xBE, 0xA0 } };
    return TestUndoSnoopCommand_UUID;
  }
  const wchar_t* EnglishCommandName() { L"TestUndoSnoop"; }
  CRhinoCommand::result RunCommand( const CRhinoCommandContext& );

  CMyUndoSnooper m_snooper;
  bool m_bRegistered;
};

// The one and only CCommandTestUndoSnoop object
static class CCommandTestUndoSnoop theTestUndoSnoopCommand;

CRhinoCommand::result
CCommandTestUndoSnoop::RunCommand( const CRhinoCommandContext& context )
{
  if( IDYES == RhinoMessageBox( L"Watch undo events?",
                                L"Undo Snooper",
                                MB_YESNO | MB_ICONQUESTION)
                               )
  {
    if( !m_bRegistered )
    {
      m_bRegistered = true;
      m_snooper.Register();
    }
    m_snooper.Enable( true );
  }
  else
  {
    m_snooper.Enable( false );
  }

  return CRhinoCommand::success;
}

//
// END TestUndoSnoop command
//
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
```

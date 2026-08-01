+++
aliases = []
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to call .NET code from a C/C++ plugin using named callbacks."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Calling into .NET from a C++ Plugin"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 9
+++

```cpp
// Demonstrates calling into .NET from C++ using Rhino's named callback
// mechanism. Requires Rhino 9 or later. See the C++ to .NET Interop guide
// for details: https://developer.rhino3d.com/guides/cpp/dotnet-interop/

#include "stdafx.h"

// Queries the .NET side for the runtime hosting this session. There is no
// C++ API for this - the question is only meaningful in managed code.
static bool RhIsRunningNetCore()
{
  CRhinoParameterDictionary args;

  // No inputs for this callback. If no handler is registered, or the
  // handler fails, we report false rather than guessing.
  if (!RhinoExecuteNamedCallback(L"GetDotNetRuntime", args))
    return false;

  // Always initialize outputs - GetBool leaves the value untouched when
  // the key is not present.
  bool running_net_core = false;
  args.GetBool(L"RunningInNetCore", running_net_core);
  return running_net_core;
}

// Displays a modern, cross-platform Eto message dialog with a
// "don't show this again" checkbox. The user's choice is persisted by
// Rhino under the supplied settings key.
//
// Returns true if the user checked "don't show again", either during this
// call or in a previous session (in which case no dialog is displayed).
static bool RhShowInfoMessage(const wchar_t* title, const wchar_t* message, const wchar_t* settings_key)
{
  CRhinoParameterDictionary args;
  args.SetString(L"title", title);
  args.SetString(L"message", message);
  args.SetString(L"dontShowAgainKey", settings_key);

  if (!RhinoExecuteNamedCallback(L"ShowInfoMessageWithDontShowAgain", args))
    return false;

  // The handler writes "dontShowAgain" only when the answer is yes. If the
  // user left the box unchecked, the key is absent and GetBool returns
  // false without touching our variable - hence the initializer.
  bool dont_show_again = false;
  args.GetBool(L"dontShowAgain", dont_show_again);
  return dont_show_again;
}

CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  UNREFERENCED_PARAMETER(context);

  if (RhIsRunningNetCore())
    RhinoApp().Print(L"This session is running .NET Core.\n");
  else
    RhinoApp().Print(L"This session is not running .NET Core.\n");

  // Use a settings key unique to your plugin so it cannot collide with
  // core Rhino or another third-party plugin.
  const bool suppressed = RhShowInfoMessage(
    L"Sample Message",
    L"This message can be suppressed by checking the box below.",
    L"MyPlugIn.SampleCommand.InfoMessage"
  );

  if (suppressed)
    RhinoApp().Print(L"The user chose to suppress this message.\n");

  return CRhinoCommand::success;
}
```

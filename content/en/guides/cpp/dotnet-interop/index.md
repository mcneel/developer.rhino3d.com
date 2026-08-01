+++
aliases = []
authors = [ "steve" ]
categories = [ "Advanced" ]
description = "This guide discusses how to call .NET code from a C/C++ plugin using Rhino's named callback mechanism."
keywords = [ "rhino", "interop", "dotnet", "callback" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "C++ to .NET Interop"
type = "guides"
weight = 10

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = "In Progress"

[included_in]
platforms = [ "Windows", "Mac" ]
since = 9

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true
+++

## Overview

A lot of Rhino's newer functionality - modern dialogs, cross-platform UI, and cloud services - is written in .NET rather than C++. Historically, a C/C++ plugin had no supported way to reach any of it without going through painful measures.

Rhino 9 exposes the mechanism for this since called **named callbacks**. A named callback is an entry in a dictionary of <string,function> elements. .NET code registers a handler under a name; C++ code invokes that name and passes a dictionary of parameters. The dictionary travels in both directions - the caller fills in the inputs, the handler writes results back into the same dictionary, and the caller reads them out after the call returns. This mechanism is heavily used in core Rhino itself and has proven to be a good way to have C++ call .NET code.

## The Two Pieces

Everything lives in *rhinoSdkInterop.h*, which is included by *rhinoSdk.h*. You do not need to include it explicitly.

`CRhinoParameterDictionary` is the property bag that carries values across the boundary. Values are stored by name, and each type has its own `SetXxx` / `GetXxx` pair:

```cpp
class RHINO_SDK_CLASS CRhinoParameterDictionary
{
public:
  CRhinoParameterDictionary();
  virtual ~CRhinoParameterDictionary();

  void SetString(const wchar_t* name, const wchar_t* value);
  bool GetString(const wchar_t* name, ON_wString& value) const;
  // ...one Set/Get pair per supported type
};
```

`RhinoExecuteNamedCallback` performs the call:

```cpp
RHINO_SDK_FUNCTION
bool RhinoExecuteNamedCallback(const wchar_t* name, CRhinoParameterDictionary& p);
```

It returns `true` if a handler was found and reported success, and `false` otherwise. Note that `false` covers two quite different situations - see [Error Handling](#error-handling) below.

## A Simple Example

Rhino registers a handler named `GetDotNetRuntime` that reports which .NET runtime the current session is using.


The pattern is always the same: construct a dictionary, set any inputs, invoke, then read the outputs back out of the same dictionary.

```cpp
bool IsRunningNetCore()
{
  CRhinoParameterDictionary args;

  if (!RhinoExecuteNamedCallback(L"GetDotNetRuntime", args))
    return false;

  bool net_core = false;
  args.GetBool(L"RunningInNetCore", net_core);
  return net_core;
}
```

The matching handler on the .NET side is a two-line method - this is what the other end of every named callback looks like:

```cs
public static void GetDotNetRuntime(object sender, NamedParametersEventArgs args)
{
  args.Set("RunningInNetFramework", HostUtils.RunningInNetFramework);
  args.Set("RunningInNetCore", HostUtils.RunningInNetCore);
}
```

Because the handler wrote both keys, `args` on the C++ side now contains both, whether or not you read them.

## Passing Inputs and Reading Results

Most callbacks take inputs as well. `ShowInfoMessageWithDontShowAgain` displays a modern Eto message dialog with a "don't show this again" checkbox, and persists the user's choice in plugin settings. Writing this dialog in C++ - twice, once per platform - would be a significant amount of work.

```cpp
void ShowStaticOutputWarning()
{
  CRhinoParameterDictionary args;
  args.SetString(L"title", L"Nested Clipping Drawing");
  args.SetString(L"message", L"The output is a static snapshot and does not update with section changes.");

  RhinoExecuteNamedCallback(L"ShowInfoMessageWithDontShowAgain", args);

  bool dont_show_again = false;
  args.GetBool(L"dontShowAgain", dont_show_again);
}
```

Here `title` and `message` are inputs, and `dontShowAgain` is an output. The handler writes `dontShowAgain` only when the answer is yes - when the user leaves the box unchecked, the key is never written at all, and `GetBool` returns `false` without touching the variable.

That behavior is typical. `GetString` and its siblings return `false` when the requested name is not present *in that type's storage*, and leave the out-parameter untouched. Always initialize your output variables before calling `GetXxx`, and treat "not written" as the default rather than an error.

## Naming Conventions

Callback names are global to the Rhino process and are not scoped by plugin. Core Rhino uses a dotted namespace-like form (`Rhino.UI.RuiIo.ToolBarNamedCallbacks.GetGroupList`). Third-party code should prefix names with something unmistakably its own so that a future Rhino version does not collide with it.

Callback names are matched case-insensitively, but **parameter keys are case-sensitive**. `GetBool(L"dontshowagain", ...)` will not find a value stored as `dontShowAgain`. Match the documented spelling of keys exactly.

## Error Handling

`RhinoExecuteNamedCallback` returning `false` means one of three things, and they are not distinguishable from the return value alone:

- No handler is registered under that name.
- A handler is registered but reported failure.
- A handler threw a managed exception. Rhino catches it, reports it through its normal exception reporting, and returns `false`. The one exception to this is `NotLicensedException`, which is deliberately allowed to propagate across the boundary rather than being swallowed.

Because an unregistered name fails silently, a typo in a callback name looks exactly like a callback that ran and declined to do anything. If a call is not behaving, check the spelling first.

If the handler did not run, the dictionary is returned unmodified. This is the practical reason to initialize your output variables: a `false` return plus an untouched `GetXxx` leaves you reading whatever was on the stack.

## Related Topics

- [Calling into .NET from a C++ Plugin (Sample)](/samples/cpp/calling-dotnet-from-cpp)
- [Creating a Rhino-dependent C++ DLL](/guides/cpp/create-dependent-dll)
- [Wrapping Native Libraries](/guides/rhinocommon/wrapping-native-libraries)
- [What is the C/C++ SDK?](/guides/cpp/what-is-the-cpp-sdk)

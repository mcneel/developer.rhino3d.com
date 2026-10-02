+++
aliases = []
authors = [ "andy" ]
categories = [ "Fundamentals" ]
description = "What a C/C++ plugin for Rhino for Mac needs in its code: the declaration block, the plugin and command objects, the Info.plist, and the Windows pieces it does without."
keywords = [ "c", "C/C++", "plugin", "mac" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Anatomy of a C/C++ plugin on the Mac"
type = "guides"
weight = 3

[included_in]
platforms = [ "Mac" ]
since = 9

[page_options]
byline = true
toc = true
toc_type = "single"
+++

A Rhino plugin for Windows is an MFC DLL. A Rhino plugin for the Mac is a *loadable bundle* built as Objective-C++. The SDK is the same, and so is most of your code, but a few things have to be present and correct or Rhino will not load your plugin - sometimes without telling you why.

This page lists those things. It assumes you have been through [Creating your first C/C++ plugin](/guides/cpp/your-first-plugin-crossplatform/).

## The plugin object

Every plugin has exactly one object derived from `CRhinoPlugIn`, and it is created as a static variable in one of your `.cpp` files:

```cpp
static CSamplePlugIn thePlugIn;
```

Static means it is constructed when Rhino loads the bundle, before anything else runs. Rhino looks for it immediately after loading and gives up if it is not there.

Because the order in which static objects are constructed matters - the plugin has to exist before any of its commands - the Windows build uses `#pragma init_seg(lib)` to force it. That pragma is Microsoft-only, so wrap it:

```cpp
#if defined(_MSC_VER)
#pragma warning(push)
#pragma warning(disable : 4073)
#pragma init_seg(lib)
#pragma warning(pop)
#endif
```

## The declaration block

This is the piece most often missing, and the failure is confusing.

One of your `.cpp` files must carry a block like this:

```cpp
#include "SDK/inc/rhinoSdkPlugInDeclare.h"

RHINO_PLUG_IN_DECLARE
RHINO_PLUG_IN_NAME(L"MyPlugin");
RHINO_PLUG_IN_ID(L"use your own uuid here");   // uuidgen
RHINO_PLUG_IN_VERSION(__DATE__ "  " __TIME__)
RHINO_PLUG_IN_DESCRIPTION(L"My plugin");
RHINO_PLUG_IN_DEVELOPER_ORGANIZATION(L"My Company");
RHINO_PLUG_IN_DEVELOPER_ADDRESS(L"My Address");
RHINO_PLUG_IN_DEVELOPER_COUNTRY(L"My Country");
RHINO_PLUG_IN_DEVELOPER_PHONE(L"My Phone");
RHINO_PLUG_IN_DEVELOPER_EMAIL(L"My Email");
RHINO_PLUG_IN_DEVELOPER_WEBSITE(L"My Website");
RHINO_PLUG_IN_UPDATE_URL(L"My Update URL");
```

These macros add small exported functions to your plugin. Before Rhino trusts the plugin, it calls them to get the plugin's name, its ID, and the SDK it was built against.

**The block must be compiled on the Mac too.** In older cross-platform samples it sits inside `#if defined(ON_RUNTIME_WIN)`, because only Windows used to check. Rhino 9 for Mac checks as well, so a plugin whose declaration is compiled out will not load. Only the `init_seg` pragma above is Windows-only.

Two failures come from this block:

- *"Rhino version not specified"* - the block is missing, or compiled out on the Mac.
- *"plug-in not compiled for this version of Rhino"* - the block is there, but the SDK you built against is not the one this Rhino expects. Update your `SDK` submodule.

**The id must be yours.** Do not copy an id out of a sample or out of this page. `RHINO_PLUG_IN_ID` has to match the id your plugin class returns from `PlugInID()`, and no two plugins may share one. If two plugins share an ID, Rhino loads only one of them and shows no warning.

Make your own in Terminal:

```
uuidgen
```

That prints a new id every time you run it. Use one for the plugin and a different one for each command.

## Commands

Each command is a class derived from `CRhinoCommand`, with exactly one static instance, in the same pattern as the plugin:

```cpp
class CCommandSample : public CRhinoCommand
{
public:
  UUID CommandUUID() override { /* a unique id */ }
  const wchar_t* EnglishCommandName() override { return L"MySample"; }
  CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
};

static class CCommandSample theSampleCommand;
```

Rhino collects the commands created during the load and attaches them to the plugin that was loading at the time. This is why the plugin object has to be constructed first.

## stdafx.h

Every source file includes `stdafx.h` first. On Windows it pulls in MFC; on the Mac it pulls in the SDK. Keep both in one file:

```cpp
#pragma once

#if defined(_WIN32) || defined(_MSC_VER)

// ... the MFC includes ...

#elif defined(__APPLE__)

#include "rhinoSdkStdafxPreamble.h"
#include "rhinoSdk.h"
#include "RhRdkHeaders.h"
#include "rhinoSdkChecks.h"

#if !defined(UNREFERENCED_PARAMETER)
#define UNREFERENCED_PARAMETER(p) (void)(p)
#endif

#endif
```

The order of those four headers matters. The preamble sets up things the rest of the SDK expects, so it has to come first, and `rhinoSdkChecks.h` verifies at the end that everything it needs was defined.

`UNREFERENCED_PARAMETER` is a Windows macro. If your code uses it - most Rhino samples do - define it here rather than editing every file that calls it.

## Types that are not the same on both platforms

**`BOOL`.** In MFC, `BOOL` is an `int`. On the Mac, `BOOL` is a single byte. The SDK declares its methods as `int` or `BOOL32`, so an override declared as `BOOL` matches on Windows only by accident, and does not match on the Mac:

```cpp
int OnLoadPlugIn() override;                  // the SDK says int
BOOL32 AddToPlugInHelpMenu() const override;  // the SDK says BOOL32
```

The compiler finds these for you - it reports an override with a different return type. Change them to what the SDK declares, and they still build on Windows.

If you search for `BOOL` parameters by name, you will miss definitions that leave the names out, such as `(CRhinoDoc&, const wchar_t*, BOOL, BOOL)`.

**Microsoft spellings.** `__time64_t` and `_time64` are Microsoft's. Use `time_t` and `time`.

**A few SDK methods differ.** `CRhinoEventWatcher::UndoEvent` takes an extra document argument on the Mac. Where the SDK does this it uses `#ifdef ON_RUNTIME_APPLE`, and your override has to carry the same test. If your override has the Windows arguments, the Mac compiler stops with `non-virtual member function marked 'override' hides virtual member function`. Your method has the same name as the SDK's but different arguments, so it does not override it. Compare it with the SDK's declaration.

## What you do not need on the Mac

**The application file.** A Windows plugin has a `CWinApp` object in `<Name>App.cpp`, which is the DLL entry point. The Mac has no MFC and does not need it. Your plugin object is a static in its own `.cpp`, so leaving the application file out of the Mac build loses nothing.

**The precompiled header source.** `stdafx.cpp` exists to generate the Windows precompiled header. The Mac build does not use it.

**Resource and module definition files.** `.rc`, `.rc2`, `.def` and `Resource.h` are Windows-only. Version information on the Mac comes from the `Info.plist` instead.

## Info.plist

A Mac plugin is a bundle, and every bundle has an `Info.plist` describing it. One key decides whether Rhino will load your plugin at all:

```xml
<key>CFBundlePackageType</key>
<string>BNDL</string>
```

`BNDL` means a loadable bundle. If it says `APPL`, macOS thinks your plugin is an application, and **Rhino refuses it without printing anything** - no error, and no entry in *Settings* > *Plug-ins*. It looks exactly like a plugin that was never loaded.

This catches people because some build tools write `APPL` by default. If your plugin builds and then simply is not there, check this first.

Also set `CFBundleExecutable` to the name of the binary inside the bundle, and `CFBundleIdentifier` to something of your own such as `com.mycompany.myplugin`.

## What a .rhp really is

On Windows a `.rhp` is a DLL - one file. On the Mac it is a folder that Finder shows as a single item:

```
MyPlugin.rhp/
└── Contents/
    ├── Info.plist
    └── MacOS/
        └── MyPlugin      <- the compiled binary
```

If you want to look inside, right-click and choose *Show Package Contents*, or use `ls` in Terminal.

This is also why a Windows `.rhp` cannot be used on the Mac. It is a Windows DLL, not a bundle, and Rhino for Mac will not load it. A plugin has to be built for each platform.

## Checking a plugin before you load it

If your plugin builds but does not appear in Rhino, look at what it exports before looking anywhere else:

```
nm -gU MyPlugin.rhp/Contents/MacOS/MyPlugin | grep RhinoPlugIn
```

A working plugin lists about fifteen `RhinoPlugIn` entries - the functions the declaration block wrote. If you get nothing back, the declaration block was not compiled, and that is the whole problem.

## Objective-C++ and ARC

Your `.cpp` files are compiled as Objective-C++ on the Mac, with Automatic Reference Counting on. Ordinary C++ is unaffected, and you do not have to write any Objective-C.

What it does give you is the option of calling Cocoa directly from the same file when you need something macOS-specific. For user interface work, prefer [Eto](https://github.com/picoe/Eto), which runs on both platforms.

## Related Topics

- [Creating your first C/C++ plugin (Cross-Platform)](/guides/cpp/your-first-plugin-crossplatform/)
- [Installing Tools (Mac)](/guides/cpp/installing-tools-mac/)
- [The Rhino C++ SDK repository](https://github.com/mcneel/rhino_sdk_cpp)

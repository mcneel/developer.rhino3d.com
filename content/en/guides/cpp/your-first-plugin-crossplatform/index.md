+++
aliases = [ "/guides/cpp/your-first-plugin-mac/" ]
authors = [ "andy" ]
categories = [ "Getting Started" ]
description = "Build a Rhino C/C++ plugin that works on both Windows and Mac from one set of sources."
keywords = [ "c", "C/C++", "plugin" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Creating your first C/C++ plugin (Cross-Platform)"
type = "guides"
weight = 2

[included_in]
platforms = [ "Windows", "Mac" ]
since = 9

[page_options]
byline = true
toc = true
toc_type = "single"
+++

Rhino 9 has a C/C++ SDK for Mac as well as for Windows. It is the same SDK, so one set of source files can build a plugin for both.

This guide builds a working sample plugin on whichever platform you are using. It is written for two kinds of readers: someone starting a new plugin who wants it to run on both platforms, and someone who already has a Windows plugin and wants it to run on the Mac as well. If you are the second group, read the whole guide and then the [porting section](#porting-a-windows-plugin) at the end.

You need the tools from [Installing Tools (Windows)](/guides/cpp/installing-tools-windows/) or [Installing Tools (Mac)](/guides/cpp/installing-tools-mac/) before you start.

## Get the code

The sample lives in the Rhino developer samples repository. The SDK is a submodule inside it, so you get both in one go:

```
git clone https://github.com/mcneel/rhino-developer-samples
cd rhino-developer-samples
git submodule update --init cpp/SDK
git -C cpp/SDK lfs pull
```

That last line matters on Windows only. The Windows part of the SDK includes four large library files kept in Git LFS. Without Git LFS, these files arrive as small placeholders, and the Windows build fails at the link step. The Mac does not use them, so on a Mac without Git LFS you can leave the line out.

The sample is in `cpp/SampleEventWatcher`. It watches the Rhino document and prints a line every time something happens - an object added, moved or deleted, a file opened or saved.

## What is in a plugin

| File | Platform | What it is |
| :--- | :--- | :--- |
| `SampleEventWatcherPlugIn.h` / `.cpp` | Both | The plugin itself. One object, created once, that Rhino loads. |
| `cmdSampleEventWatcher.cpp` and the other `cmd*.cpp` files | Both | One Rhino command each. |
| `SampleRhinoEventWatcher.h` / `.cpp` | Both | The part that listens for document events. |
| `stdafx.h` | Both | Included first by every source file. It brings in MFC on Windows and the SDK headers on the Mac. |
| `CMakeLists.txt` | Both | Describes how to build the plugin. |
| `Info.plist.in` | Mac | Describes the plugin bundle to macOS. |
| `SampleEventWatcher.vcxproj` | Windows | A Visual Studio project, as an alternative to CMake. |
| `SampleEventWatcherApp.cpp`, `stdafx.cpp` | Windows | The MFC pieces a Windows plugin needs. Not built on the Mac. |
| `SampleEventWatcher.rc`, `Resource.h`, `SampleEventWatcher.def` | Windows | Version information, icon and exported names. |

The plugin object and the commands are the parts you write. Everything else is scaffolding.

For what each of those pieces has to contain on the Mac - the declaration block, the `Info.plist`, the types that differ, and the Windows files a Mac plugin does without - see [Anatomy of a C/C++ plugin on the Mac](/guides/cpp/anatomy-of-a-mac-cpp-plugin/).

## Build it

### Windows

Open `cpp\SampleEventWatcher\SampleEventWatcher.vcxproj` in Visual Studio. Choose the **Debug** configuration and **x64**, and build.

To run it, press the green arrow marked **Local Windows Debugger**. That starts Rhino with the debugger attached, so you can put a breakpoint in your command and stop on it.

If Rhino does not start, Visual Studio does not know what to run. Open the project's properties, go to *Debugging*, and set **Command** to your Rhino executable - usually `C:\Program Files\Rhino 9\System\Rhino.exe`.

### Mac

The repository does not include an Xcode project. CMake generates one for you. Run this once:

```
cd cpp/SampleEventWatcher
cmake -G Xcode -S . -B build
```

That writes `build/SampleEventWatcher.xcodeproj`. Open it in Xcode and work there from now on. You only need that command again if you add or remove source files - there is more about what it is doing [at the end of this guide](#building-with-cmake).

Build it with *Product > Build*.

To run it under the debugger, tell Xcode what to launch: *Product > Scheme > Edit Scheme*, choose *Run* on the left, and set **Executable** to `Rhino 9.app`. Now the Run button starts Rhino, and your breakpoints work.

## Load it into Rhino

Building the plugin does not tell Rhino about it. There are two ways to load one, and they are for different jobs.

### While you are developing

Use the `TestLoadPlugIn` command. It is a test command, so it does not autocomplete - type the whole name - and it asks you for the `.rhp` you just built.

On Windows the file is under `x64\Debug`; on the Mac it is in `build/Debug`. You can also drag the `.rhp` onto an open Rhino window.

Rhino remembers the plugin, so it loads next time too. This is for trying your own builds and nothing else.

### When you give it to somebody else

Package it with [Yak](/guides/yak/what-is-yak/), Rhino's package manager. A package is what users install, what the Package Manager lists, and what carries your plugin's version and description.

- [Creating a Rhino plugin package](/guides/yak/creating-a-rhino-plugin-package/)
- [Installing and managing packages](/guides/yak/installing-and-managing-packages/)

A C++ plugin has to be built for each platform, so a package containing only your Windows `.rhp` will install on a Mac and then do nothing - the file is a Windows DLL and Rhino for Mac cannot load it. Build on both and put both in the package.

## Try it

Run the `SampleEventWatcher` command and choose **Enable**.

Now draw a point, move it, and delete it. Each time, the command line prints what happened:

```
** EVENT: Add Object **
** EVENT: Replace Object **
** EVENT: Delete Object **
```

The plugin adds three more commands - `SampleIdleWatcher`, `SampleUndoable` and `SampleNotUndoable` - which show other things the SDK can do.

Run `SampleEventWatcher` again and choose **Disable** when you have seen enough.

## Starting your own plugin

Copy the sample folder, rename the files, and change the class names to match. Three things have to be right:

**The plugin declaration.** One of your `.cpp` files carries a block that tells Rhino the plugin's name, its id, and which SDK it was built against. Without it Rhino refuses to load the plugin, saying *"Rhino version not specified"*. The block is the same on both platforms. The SDK's [README](https://github.com/mcneel/rhino_sdk_cpp/blob/main/README.md) gives it in full.

**A new plugin id.** The id in the declaration must be unique to your plugin, and must match the one your plugin class returns from PlugInID(). Generate one with `uuidgen` on the Mac, or *Tools > Create GUID* in Visual Studio. Two plugins with the same id will not both load.

**The SDK and Rhino must be a matching pair.** Your plugin records which SDK it was built against, and Rhino checks it. If you see *"plug-in not compiled for this version of Rhino"*, update the `SDK` submodule:

```
git -C cpp/SDK pull
```

The SDK's README is the reference for everything else - the `CMakeLists.txt` in full, the Windows precompiled header, and how the Mac link stubs work.

## Porting a Windows plugin

If you already have a Windows plugin, most of the work is build files rather than code. A few source changes come up almost every time.

**`stdafx.h` needs a Mac branch.** Put the existing MFC includes inside `#if defined(_WIN32) || defined(_MSC_VER)`, and add an `#elif defined(__APPLE__)` branch that includes `rhinoSdkStdafxPreamble.h`, `rhinoSdk.h`, `RhRdkHeaders.h` and `rhinoSdkChecks.h`, in that order. Rhino for Mac has no MFC.

**`BOOL` is not the same type on both platforms.** In MFC, `BOOL` is an `int`. On the Mac it is a single byte. The SDK declares methods like `OnLoadPlugIn` as `int` and `AddToPlugInHelpMenu` as `BOOL32`, so a method you wrote as `BOOL` matched on Windows by chance and will not match on the Mac. The compiler tells you which ones. Change them to what the SDK says, and they still build on Windows.

**Windows-only pieces do not come across.** The MFC application file, the `.rc` and `.def` files and the precompiled header stay in the Windows build only. The plugin object itself is a static variable in your plugin's `.cpp` file, so nothing is lost by leaving the application file out.

**Some things have no Mac equivalent.** MFC dialogs have to be rewritten - [Eto](https://github.com/picoe/Eto) is the cross-platform way to build user interfaces for Rhino. A few parts of Rhino are Windows-only. Skins are one example. You cannot skin Rhino for Mac.

Again, a C++ plugin for Mac has to be built for the Mac. Shipping your Windows `.rhp` in a package does not make it work there - Rhino will not load it.

## Building with CMake

You can skip this. It explains the file that made the Xcode project, which is worth knowing about if you want your own plugin to build on both platforms or on a build server.

`CMakeLists.txt` describes the plugin once - which files it is built from, and what each platform needs. CMake reads that and writes a real Visual Studio project on Windows and a real Xcode project on the Mac, so you still work in your IDE. Nothing about the plugin is different; only where the project file came from.

The point of it is that the two platforms need quite different settings, and you would otherwise keep them in step by hand in two places. The sample's file, for instance, builds the MFC files on Windows only, compiles as Objective-C++ on the Mac, and links different libraries on each.

To build from a terminal, which is what a build server does:

```
cmake --build build --config Debug
```

To generate a Visual Studio project instead of using the one in the repository:

```
cmake -G "Visual Studio 18 2026" -A x64 -S . -B build
```

If CMake does not recognize this generator name, your CMake is too old. Update it, or use the copy of CMake that comes with Visual Studio.

The SDK's [README](https://github.com/mcneel/rhino_sdk_cpp/blob/main/README.md) gives a complete `CMakeLists.txt` you can start from, with the settings each platform needs and what each one is for.

## Related Topics

- [What is the C/C++ SDK?](/guides/cpp/what-is-the-cpp-sdk/)
- [Installing Tools (Mac)](/guides/cpp/installing-tools-mac/)
- [Installing Tools (Windows)](/guides/cpp/installing-tools-windows/)
- [The Rhino C++ SDK repository](https://github.com/mcneel/rhino_sdk_cpp)
- [Rhino developer samples](https://github.com/mcneel/rhino-developer-samples)

+++
authors = ["curtis", "callum"]
categories = [ "Overview" ]
description = "This guide walks you through making the transition to .NET 7"
keywords = [ ".NET", "RhinoCommon", "Plugin" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Moving to .NET 7"
type = "guides"
weight = 3

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

Rhino 8 now uses the open source [.NET Core Runtime](https://github.com/dotnet/runtime) for running .NET code on both Windows and Mac.
This brings some performance improvements and aligns the .NET runtimes used across platforms. Previously, Rhino 7 and earlier used the [mono runtime](https://www.mono-project.com) on Mac, and .NET Framework exclusively on Windows.

On Windows, you can still optionally run using the .NET Framework runtime in the case of compatibility issues or running inside other software that requires it (e.g. Rhino.Inside Revit).

Most plugins are already compatible when running in .NET Core without any recompilation, but in the case of any incompatibilities you may need to update your plugin.

## Advantages of .NET Core for Rhino

Using .NET Core allows Rhino and plugins to take advantage of many [performance improvements](https://devblogs.microsoft.com/dotnet/performance_improvements_in_net_7/) which will make just about all .NET code execute much faster.  This can potentially provide huge productivity gains with computational libraries or large data sets.

Additionally, using .NET Core on Mac eliminates a lot of compatibility issues between the Mac and Windows versions of Rhino making it easier to make plugins work on both platforms.

## Choosing the .NET Runtime on Windows

There may be reasons to continue to use .NET Framework on Windows, in particular if you need to use 3rd party plugins that aren't compatible with .NET Core yet.  The disadvantage to using .NET Framework is that Rhino may run a little slower in certain use cases.  There are two ways to select the runtime that Rhino uses:

1. Use the `SetDotNetRuntime` command, then restart Rhino.
1. Pass either `/netcore` or `/netfx` as an argument when launching `Rhino.exe`. This overrides the `SetDotNetRuntime` setting.

## Rhino.Inside

When using Rhino.Inside, the runtime Rhino uses is the same as the host application.  For example, since Revit currently uses .NET Framework, Rhino.Inside.Revit will also run using .NET Framework.  Custom Rhino.Inside applications should still work, however migrating to .NET 7+ would allow you to take advantage of the performance improvements offered with .NET Core.

## Checking if your plugin is compatible

Rhino 8 will automatically scan plugins for any known API breakages when running in .NET Core, and will provide a report of the specific assemblies and APIs that are not comatible.

To check manually, you can use the `compat.exe` tool on each of your plugin assemblies:

```
"C:\Program Files\Rhino 8\System\netcore\compat.exe" -q --check-system-assemblies MyPlugin.rhp
```

You can also use Microsoft's [upgrade assistant](https://learn.microsoft.com/en-us/dotnet/core/porting/upgrade-assistant-overview) to analyze your project for compatibility issues.

## Migrating your plugin

It is recommended to keep your plugin(s) targetted at .NET 4.8 so that it can run in either runtime on Windows. Most plugins won't need any changes to run in Rhino 8.

For Mac-specific plugins you can target .NET 7 as that is the only runtime available in Rhino 8. If you want the plugin to be compatible with Rhino 7, keep the target at .NET 4.8.

{{< call-out warning "AnyCPU" >}}

Since Rhino 8 can run natively on Apple Silicon or on Intel, you must compile your .NET assemblies for AnyCPU, and any native binaries need to be compiled as a [Universal Binary](https://developer.apple.com/documentation/apple-silicon/building-a-universal-macos-binary).

{{< /call-out >}}

If your plugin uses any unavailable or non-working APIs when running in .NET Core, some code changes may be necessary. The compat report will show you which APIs you need to avoid.

If you [multi-target your project](https://learn.microsoft.com/en-us/nuget/create-packages/multiple-target-frameworks-project-file) to both .NET 4.8 and .NET 7.0, you can find compatibility issues during compilation. Keep in mind you should only distribute the .NET 4.8 version on Windows.

## Debugging .NET Core on Windows

To debug in .NET Core on Windows you will need to use Visual Studio 2022 or Visual Studio Code.

Visual Studio determines the debugging runtime by the project's target framework, so either you need to [multi-target your project](https://learn.microsoft.com/en-us/nuget/create-packages/multiple-target-frameworks-project-file), or create a separate launcher project used for debugging purposes only.

With Visual Studio Code, use the `coreclr` debugger type from the C# extension. You do not need to multi-target or create a launcher project when using Visual Studio Code.

### How to add a .NET Core launcher project in Visual Studio

This is only required when you want to debug in .NET Core using Visual Studio 2022 on Windows.

1. Right-click on your solution node and select *Add > New Project...*
1. Select the C# **Console App** then click *Next*.
1. Enter a name e.g. `Rhino8Launcher` then click *Next*.
1. Select **.NET 7.0** for the Framework then click *Create*.
1. Right-click the launcher project and select *Properties*.
1. Go to the **Application > General** panel and change the **Output Type** drop down to *Windows Application*.
1. Go to the **Debug > General** panel and click *Open debug launch profiles UI*.
1. Delete the default profile by clicking the *Delete selected profile* button.
2. Create a new **Executable** profile, and enter the path to Rhino.exe. E.g. `C:\Program Files\Rhino 8\System\Rhino.exe`

You may also want to add your plugin project as a dependency of the launcher project so it compiles before launching.

## Debugging on Mac

On Mac, you will need to use [Visual Studio Code](https://code.visualstudio.com/). Follow the [Your First Plugin (Mac)](/guides/rhinocommon/your-first-plugin-mac/#setting-up-debug)

## Discussions

Jump over to our [developer discourse channel](https://discourse.mcneel.com/c/rhino-developer/3) to ask questions regarding the move to .NET Core.

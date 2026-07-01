+++
aliases = ["/en/guides/rhinocommon/moving-to-dotnet-7/"]
authors = ["curtis", "callum"]
categories = [ "Overview" ]
description = "This guide walks you through making the transition to .NET Core in Rhino 8 and Rhino 9"
keywords = [ ".NET", "RhinoCommon", "Plugin" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Moving to .NET Core"
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

Rhino 8 introduced the open source [.NET Core Runtime](https://github.com/dotnet/runtime) for running .NET code on both Windows and Mac, replacing the [mono runtime](https://www.mono-project.com) previously used on Mac and .NET Framework on Windows.

**Rhino 9** continues this transition with .NET 10 as the default runtime, and **.NET Framework is deprecated**. .NET Framework plugins may still load and run in Rhino 9, but support is not guaranteed to continue in future versions. **All plugin developers should migrate to .NET 8 or .NET 10.**

On Windows, Rhino 8 still offered an optional .NET Framework fallback for compatibility with third-party plugins or Rhino.Inside scenarios. That fallback remains available in Rhino 9 but is deprecated and should not be relied upon for new or updated plugins.

Most plugins are already compatible when running in .NET Core without any recompilation, but in the case of any incompatibilities you may need to update your plugin.

## Advantages of .NET Core for Rhino

Using .NET Core allows Rhino and plugins to take advantage of many [performance improvements](https://devblogs.microsoft.com/dotnet/announcing-dotnet-10/) which will make just about all .NET code execute much faster.  This can potentially provide huge productivity gains with computational libraries or large data sets.

Additionally, using .NET Core on Mac eliminates a lot of compatibility issues between the Mac and Windows versions of Rhino making it easier to make plugins work on both platforms.

## Choosing the .NET Runtime on Windows

{{< call-out warning "Rhino 9: .NET Framework Deprecated" >}}

**The .NET Framework runtime is deprecated in Rhino 9.** It still works today, and plugins targeting .NET Framework continue to load and run, but the runtime itself is not guaranteed to remain available in future releases. You should **migrate your plugins to .NET 10** — do not ship new or updated plugins targeting .NET Framework.

{{< /call-out >}}

In **Rhino 8**, there may be reasons to continue using .NET Framework on Windows, such as needing third-party plugins that are not compatible with .NET Core yet. The disadvantages are that Rhino may run a little slower in certain use cases, and that you won't be able to use newer plugins that target .NET Core only.

Rhino 8 initially shipped with the .NET 7.0.0 runtime. Rhino 8.12 or later has the option to use a manually installed .NET 8 runtime, and Rhino 8.20 installs and defaults to using .NET 8.0.14 or later.

In **Rhino 8**, there are a few ways to select the runtime and version:

1. Use the `SetDotNetRuntime` command, then restart Rhino.
1. Pass either `/netcore` or `/netfx` as an argument when launching `Rhino.exe`. This overrides the `SetDotNetRuntime` setting.
1. Pass either `/netcore-8` or `/netcore-7` to specify a particular .NET Core version. This requires that the chosen version is manually installed if it's different from Rhino's default.

In **Rhino 9**, `/netcore` targets .NET 10 and is the default. The `/netfx` flag and `SetDotNetRuntime` command still work but are deprecated — use of .NET Framework in Rhino 9 is strongly discouraged, so migrate to .NET 10 as soon as possible.

## Rhino.Inside

When using Rhino.Inside, the runtime Rhino uses is the same as the host application. The runtime a given host requires depends on its version — for example, Revit has moved through several .NET runtimes over its recent releases:

| Revit Version | .NET Runtime |
| --- | --- |
| Revit 2024 and earlier | .NET Framework 4.8 |
| Revit 2025 (2025.0–2025.4) | .NET 8 |
| Revit 2026 (2026.0–2026.4) | .NET 8 |
| Revit 2025.5, Revit 2026.5, and later | .NET 10 |
| Revit 2027 and later | .NET 10 |

Autodesk migrated Revit 2025 and 2026 from .NET 8 to .NET 10 (starting with the 2025.5 and 2026.5 updates) to follow Microsoft's long-term support lifecycle, since .NET 8 support ends in November 2026.

This means Rhino.Inside.Revit runs on whichever runtime the hosting Revit version requires: .NET Framework when hosted in Revit 2024 or earlier, .NET 8 in Revit 2025/2026 prior to their .5 updates, and .NET 10 in Revit 2025.5/2026.5 and Revit 2027 or later. In Rhino 9, .NET Framework is deprecated but still works, so Rhino.Inside hosts that require .NET Framework can continue to run while you plan a migration to .NET 10. Continued use of .NET Framework in Rhino 9 is strongly discouraged. Custom Rhino.Inside applications should migrate to .NET 10 to take advantage of the performance improvements and to support Rhino 9.

### BinaryFormatter

[`BinaryFormatter`](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization.formatters.binary.binaryformatter) serialization is disabled by default in .NET 9 and later, so any code that relies on it will throw when running under .NET 10 — including when hosted in Revit versions that use .NET 10 (Revit 2025.5/2026.5 and Revit 2027 or later).

When running Rhino standalone, Rhino enables `BinaryFormatter` support so existing plugins that depend on it continue to work. However, when Rhino is hosted inside another application via Rhino.Inside, that support is not enabled by the host — for example, Rhino.Inside.Revit running in a .NET 10 version of Revit will not have `BinaryFormatter` available by default.

`BinaryFormatter` is insecure and its use is discouraged. Ideally, migrate away from it to a safer serializer. If your application still requires it, you can re-enable it in your own process by referencing the [`System.Runtime.Serialization.Formatters` compatibility package](https://learn.microsoft.com/en-ca/dotnet/standard/serialization/binaryformatter-migration-guide/#use-the-compatibility-package).

## Checking if your plugin is compatible

Rhino 8 and Rhino 9 will automatically scan plugins for any known API breakages when running in .NET Core, and will provide a report of the specific assemblies and APIs that are not compatible.

To check manually, you can use the `compat.exe` tool on each of your plugin assemblies:

For Rhino 8:

```
"C:\Program Files\Rhino 8\System\netcore\compat.exe" -q --check-system-assemblies MyPlugin.rhp
```

For Rhino 9:

```
"C:\Program Files\Rhino 9\System\netcore\compat.exe" -q --check-system-assemblies MyPlugin.rhp
```

You can also use Microsoft's [upgrade assistant](https://learn.microsoft.com/en-us/dotnet/core/porting/upgrade-assistant-overview) to analyze your project for compatibility issues.

## Migrating your plugin

Many plugins won't need any changes to run in Rhino 8 with .NET Core, but if they do it is recommended to multi-target your plugin(s) for .NET 4.8, .NET 8.0 and .NET 10.0 so that it can run in either runtime on Windows.

For **Rhino 9**, you should target **.NET 10.0**. Since .NET Framework is deprecated in Rhino 9, multi-targeting .NET 4.8 is only necessary if you also need to support Rhino 8 on Windows with the .NET Framework fallback, or Rhino 7 and earlier.

For Mac-specific plugins you can target .NET 8.0 (Rhino 8) or .NET 10.0 (Rhino 9) as .NET Core is the only runtime available on Mac. If you want the plugin to be compatible with Rhino 7, target .NET 4.8 instead or use multi-targeting.

| Rhino Version | Recommended Target | Notes |
|---|---|---|
| Rhino 7 | `net48` | .NET Framework or Mono |
| Rhino 8 (Windows, .NET Core) | `net8.0` | Default from Rhino 8.20 |
| Rhino 8 (Windows, .NET Framework) | `net48` | Deprecated path, avoid for new work |
| Rhino 9 | `net10.0` | .NET Framework deprecated, but still works |

{{< call-out warning "AnyCPU" >}}

Since Rhino 8 can run natively on Apple Silicon or on Intel, you must compile your .NET assemblies for AnyCPU, and any native binaries need to be compiled as a [Universal Binary](https://developer.apple.com/documentation/apple-silicon/building-a-universal-macos-binary).

Rhino 9 on Mac runs only on Apple Silicon (arm64) — Intel Macs are no longer supported. Even so, targeting AnyCPU is still recommended, especially for code shared across platforms and Rhino versions, so the same assemblies continue to run everywhere without per-architecture builds.

{{< /call-out >}}

If your plugin uses any unavailable or non-working APIs when running in .NET Core, some code changes may be necessary. This is especially true with many 3rd party libraries that have different versions of their library for .NET 4.8 and .NET Core.  The compat report will show you which APIs and libraries you need to avoid or update.

If you [multi-target your project](https://learn.microsoft.com/en-us/nuget/create-packages/multiple-target-frameworks-project-file) to .NET 4.8, .NET 8.0 and .NET 10.0, you can easily find and resolve compatibility issues during compilation.

## Developing on Windows

You can develop Rhino plugins on Windows with either [Visual Studio Code](https://code.visualstudio.com/) or Visual Studio.

- For **Rhino 8**, use **Visual Studio 2022** or Visual Studio Code.
- For **Rhino 9**, use **Visual Studio 2026** or Visual Studio Code. Visual Studio 2026 also works for Rhino 8.

To get started, follow the [Your First Plugin (Windows)](/guides/rhinocommon/your-first-plugin-windows/) guide.

### Debugging .NET Core on Windows

Visual Studio determines the debugging runtime by the project's target framework, so you need to [multi-target your project](https://learn.microsoft.com/en-us/nuget/create-packages/multiple-target-frameworks-project-file) to debug in .NET Core. This is the recommended approach going forward.

With Visual Studio Code, use the `coreclr` debugger type from the C# Dev Kit extension.

Our [project templates](https://github.com/mcneel/RhinoVisualStudioExtensions?tab=readme-ov-file#rhinocommon-visual-studio-extensions) automatically create a multi-targeted plugin, create launch configurations for both VS and VS Code, and have options to include a yak packaging step for multiple Rhino versions.

## Developing on Mac

On Mac, you will need to use [Visual Studio Code](https://code.visualstudio.com/). Follow the [Your First Plugin (Mac)](/guides/rhinocommon/your-first-plugin-mac/#setting-up-debug)

## Discussions

Jump over to our [developer discourse channel](https://discourse.mcneel.com/c/rhino-developer/3) to ask questions regarding the move to .NET Core.

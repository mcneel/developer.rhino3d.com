+++
aliases = []
authors = [ "callum" ]
categories = [ "Plug-in Development" ]
description = "Use Claude Code and RhinoMCP to port a Windows-only WPF plug-in UI to Eto.Forms so it runs on Rhino for Mac."
keywords = [ "developer", "ai", "rhinomcp", "plugins", "WPF", "Eto.Forms", "eto", "cross-platform UI", "mac" ]
languages = [ "C#" ]
sdk = [ "AI", "RhinoCommon", "Eto" ]
title = "Convert a WPF UI to Eto"
type = "guides"
weight = 70
override_last_modified = "2026-11-21T00:00:00Z"
short_description = "Port a WPF plug-in UI to Eto.Forms with an AI agent and RhinoMCP."
thumbnail = ""
tags = ["rhino", "version 8", "version 9", "ai", "rhinomcp", "plugins", "eto", "mac"]

[admin]
TODO = "Source page was draft. Needs a worked example (source had placeholder: https://github.com/dalefugier/SampleCsChromium) and a hero image. The sample prompt targets a WinForms plug-in, not WPF; rewrite it for WPF or note it."
origin = "https://github.com/mcneel/RhinoAI/tree/main/docs/content/docs/developers/wpf-to-eto.md"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = false
toc = true
toc_type = "single"
block_webcrawlers = true
modern_style = true
modern_hero = true

[modern]
eyebrow = "Plug-ins · Tutorial"
lead = "Rewrite XAML as Eto layouts, swap bindings, and re-wire events, with RhinoMCP opening each dialog in a live Rhino to confirm it actually renders."
hero_image = ""
meta = ["45 min", "Rhino 8 / 9 for Windows / Mac", "Advanced"]
+++

If your Rhino plugin's UI is built on WPF, it only runs on Windows. Porting it to [Eto.Forms](https://github.com/picoe/Eto), the cross-platform UI toolkit Rhino itself uses, lets the same plugin run on Rhino for Mac as well. The mechanical parts of that port (rewriting XAML as Eto layouts, swapping bindings, re-wiring event handlers) are a great fit for Claude Code with Rhino MCP, because the assistant can build the plugin, load it into Rhino, and actually open each dialog to see whether it renders.

## What you need

- **Claude Code** with the [Rhino MCP plugin](../MCP/getting-started/cc-plugin/) installed.
- **Rhino** open with Rhino MCP running. If you can run it on both Windows and Mac, even better. The whole point of the port is the Mac side.
- Your plugin's source checked out locally, with Claude Code started in that repo.

## The loop

With Rhino MCP loaded, the assistant can:

- Read your existing `.xaml` and code-behind files and map controls to their Eto equivalents.
- Scaffold an Eto `Dialog` or `Panel` per WPF window, rebuild, and load the `.rhp` into Rhino.
- Run the command that opens each dialog and confirm it actually appears, rather than just compiles.
- Iterate on layout and bindings one panel at a time.

Opening the dialog after each change is what makes this worth doing through the MCP. Eto's layout model isn't WPF's, and "it builds" tells you very little about whether the result is usable.

## A prompt to start with

{{< call-out tip "Prompt" >}}
```text
Convert a legacy Rhino WinForms plug-in to Rhino 8 / net8.0 / Eto.Forms.

SDK-style csproj: net8.0, <TargetExt>.rhp</TargetExt>, <GenerateAssemblyInfo>false</GenerateAssemblyInfo>, single RhinoCommon 8.x PackageReference. Drop packages.config, post-build hacks, per-arch configs.
Replace WinForms controls with Eto.Forms equivalents. Preserve any panel [Guid].
git rm *.Designer.cs, *.resx, Resources.*, packages.config.
Collapse .sln to Any CPU with SDK project type GUID.
Add .vscode/launch.json + tasks.json from the Rhino template.
Verify dotnet build is clean.
```
{{< /call-out >}}

If you have a mix of dialogs and dockable panels, tell the assistant which is which. Eto's `Dialog` and Rhino's panel hosting are different code paths.

## What to review

- **Layout translation.** WPF's `Grid` with star-sizing, `StackPanel`, and `DockPanel` don't map one-for-one to Eto's `TableLayout`, `StackLayout`, and `DynamicLayout`. Open each ported dialog and check spacing, alignment, and what happens when you resize.
- **Data binding.** WPF's `{Binding}` and `INotifyPropertyChanged` flow doesn't exist in Eto the same way. The assistant will often replace bindings with explicit event wiring. Confirm two-way fields still round-trip.
- **Styles and resources.** WPF `Style`, `ResourceDictionary`, and control templates have no direct Eto equivalent. Expect these to collapse into per-control property setters; spot-check the visual result.
- **Platform-specific code-behind.** Anything reaching into `System.Windows.*` (clipboard, dispatcher, message boxes) needs an Eto or RhinoCommon replacement, not a `#if WINDOWS` wrapper.
- **Rhino panel registration.** If a window is hosted as a Rhino panel, the registration attributes and panel GUIDs need to come across too, not just the UI class.

## When the assistant gets stuck

If a control has no clean Eto equivalent (custom-drawn WPF controls, heavy `ItemsControl` templating, third-party WPF libraries), have the assistant stop and surface the list rather than faking it with a `Label` that says "TODO". A short "these need a human" list is more useful than a dialog that opens but does nothing.

For visual diffs, ask the assistant to open the same dialog before and after on the same Rhino session so you can eyeball the difference. The MCP can drive that, but it can't tell you whether the new layout *looks* right.

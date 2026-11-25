+++
aliases = []
authors = [ "callum" ]
categories = [ "Plug-in Development" ]
description = "Use an AI agent and RhinoMCP to upgrade a legacy net45/net48 Rhino plug-in to a modern net8.0 plug-in."
keywords = [ "developer", "ai", "rhinomcp", "plugins", ".NET Core", "net8.0", "plugin upgrade", "net48", "claude code" ]
languages = [ "C#" ]
sdk = [ "AI", "RhinoCommon" ]
title = "Upgrade a Plug-in to .NET Core"
type = "guides"
weight = 50
override_last_modified = "2026-11-21T00:00:00Z"
short_description = "Upgrade a legacy net45/net48 Rhino plug-in to net8.0 with an AI agent and RhinoMCP."
thumbnail = "sel-arc.png"
tags = ["rhino", "version 8", "version 9", "ai", "rhinomcp", "plugins"]

[admin]
TODO = ""
origin = "https://github.com/mcneel/RhinoAI/tree/main/docs/content/docs/developers/upgrade-to-netcore.md"
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
lead = "Move a Rhino plug-in still targeting net45 or net48 onto net8.0 by letting an AI agent do the upgrade and using RhinoMCP to test it in a live Rhino."
hero_image = "sel-arc.png"
meta = ["20 min", "Rhino 8 / 9 for Windows / Mac", "Intermediate"]
+++

If you have a Rhino plugin still targeting `net45` or `net48`, you'll want to move it to `net8.0` (Rhino 8) which will also work for (Rhino 9 WIP/BETA). This page showcases how you can use the RhinoMCP to make this upgrade seamless.

## An Example

As an example we'll upgrade this simple `net45` plugin written by [Steve Baer](https://discourse.mcneel.com/u/stevebaer/summary). Checkout the code, and open your AI agent at the path of the locally cloned repo.

[github.com/sbaer/selcommands](https://github.com/sbaer/selcommands)

## The prompt

{{< call-out tip "Prompt" >}}
```text
Upgrade this legacy RhinoCommon plugin to a modern Rhino 8 plugin per the
McNeel CSRhino template:
https://github.com/mcneel/RhinoVisualStudioExtensions/tree/main/Rhino.Templates/content/CSRhino

- SDK-style csproj, net8.0;net48, EnableDynamicLoading,
  TargetExt=.rhp, RhinoCommon via NuGet (ExcludeAssets="runtime")
- Move Title/Company/Description/Version into the csproj; keep PlugInDescription
  attrs and the original Guid in AssemblyInfo.cs
- Ensure the necessary debug launch profiles exist for vscode and Visual Studio from the template
- Don't touch command sources unless an API changed
- `dotnet build` to verify both target frameworks
```
{{< /call-out >}}

## The AI Agent

With this prompt the AI agent will read through and update all of the necessary files in the repo, mostly `.csproj` and `.cs` files. It will also test using `dotnet build` to ensure the code works. When the code builds the agent will load the `.rhp` into Rhino and can run commands to ensure it worked. If Rhino crashes, the AI Agent should get the crash info and can figure out why it crashed and resolve it.

## What to review

When your AI Assistant is done it is very important to review all of the changes made and make an effort to understand them. Some important items to review.

- **The new `.csproj`.**
- **Directory.Build.Props.**
- **Updated Nuget references**
- **Any updated commands**

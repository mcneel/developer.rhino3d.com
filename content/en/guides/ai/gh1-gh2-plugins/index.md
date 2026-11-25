+++
aliases = ["/en/wip/guides/ai/gh1-gh2-plugins/"]
authors = [ "verena" ]
categories = [ "Plug-in Development" ]
description = "Use Claude Desktop to transform a Grasshopper 1 plugin to Grasshopper 2."
keywords = [ "developer", "ai", "grasshopper", "grasshopper 2", "plugins", "migration", "rhinomcp", "claude" ]
languages = [ "C#" ]
sdk = [ "AI", "Grasshopper", "Grasshopper 2" ]
title = "Port GH1 plugin to GH2"
type = "guides"
weight = 30
override_last_modified = "2026-11-20T00:00:00Z"
short_description = "Use Claude Desktop to transform a Grasshopper 1 plugin to Grasshopper 2."
thumbnail = "plugin-migration-hero.png"
tags = ["rhino", "version 9", "ai", "scripting", "rhinomcp"]

[admin]
TODO = ""
origin = ""
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
eyebrow = "Scripting · Tutorial"
lead = "Port your existing Grasshopper 1 plugin to Grasshopper 2 using the Claude Desktop and the RhinoMCP in Rhino 9"
hero_image = "plugin-migration-hero.png"
meta = ["60 min", "Rhino 9 for Windows / Mac", "Advanced"]
+++

*Draft by Verena Vogler · 2026-11-19*

As a {{< rhino-command english-command="Grasshopper" local-command="Grasshopper" image-name="Grasshopper">}} developer, you can port a **Grasshopper 1 (GH1)** plugin to **Grasshopper 2 (GH2)** much faster by splitting the work between two AI tools. **Claude Code** rewrites the source. **Rhino MCP** tests the result in a live Rhino. This tutorial walks through a practical workflow and shows which parts are easy to hand to the AI, and which need careful human attention.

**Why now?** 
GH2 ships with Rhino 9, and **GH2 does not load GH1 plugins**. Rhino 9 also moves to .NET 10 as its default runtime and changes parts of the UI and SDK. Older Rhino plugins may still load for now, but that is not guaranteed. If you ship a Rhino or Grasshopper plugin, plan for this.

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="gh2-migration-0.png" caption="GH2 by David Rutten." caption-align="center" no-back=true >}}
{{< /div >}}

**You will learn to:**

1. Check how much of your plugin actually has to change.
2. Set up a **GH2 project** next to your **GH1 project**.
3. Port parameters, types and components with **Claude Code**.
4. Test each ported component side by side in Rhino with **Rhino MCP**.
5. Decide what stays with you, the human.

## What you'll need

You need common developer tools, a Claude subscription, and Rhino 9 where both versions of Grasshopper are included.

| Tool | What it does in the port |
| --- | --- |
| Rhino 9, with GH1 and GH2 | Runs both canvases side by side, so you can compare old and new behaviour |
| Your GH1 plugin source (C# project that builds) | The starting point. It stays untouched; the GH2 port lives next to it |
| Visual Studio or Visual Studio Code, plus the .NET SDK | Builds the GH2 `.rhp`. For example, Visual Studio 2022 with Claude Code in its terminal |
| `Rhino.Templates` and the [Grasshopper2 NuGet package](https://www.nuget.org/packages/Grasshopper2/9.0.26258.12303-beta?_src=template) (beta) | Scaffolds the GH2 project and supplies the GH2 SDK |
| GitHub (or any Git host) | A branch for the port, so every AI change is reviewable and reversible |
| Claude subscription with Claude Code | Edits the source, builds, reads compiler errors, iterates. Use it from a terminal, your IDE, or Claude Desktop |
| [Rhino MCP (RhinoAI)](https://github.com/mcneel/RhinoAI) | Lets an AI assistant drive a running Rhino and Grasshopper session. Connect it to Claude Desktop or another MCP client |

{{< call-out info "About Rhino MCP" >}} 
MCP is the language an AI assistant uses to talk to other software. **Rhino&AI is McNeel's free MCP server for Rhino**. Once it is connected, the assistant can see what is in your Rhino and Grasshopper files, create geometry, run commands, write scripts and build Grasshopper definitions. It works with Claude, GitHub Copilot, Codex, Gemini and local models. Follow the Getting Started section of the [Rhino&AI docs](https://github.com/mcneel/RhinoAI) to install it and connect your assistant.
{{< /call-out >}}


## Before you start: know what changes

GH2 is not a version bump. It is a full rewrite, so a GH1 plugin cannot simply be recompiled. Nearly every layer you build against changed:

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="gh2-migration-4.png" caption="GH1 versus GH2." caption-align="center" no-back=true >}}
{{< /div >}}

**Check your plugin architecture first.** The key idea is to only change the Grasshopper layer. Many plugins are layered. Only the top layer talks to the Grasshopper SDK, so only that layer has to be rewritten:

- **Grasshopper layer** (C#, `.gha`): components that read inputs, call your core code and write outputs. This is what you port.
- **Core library** (C#/.NET): your domain logic. Stays as it is.
- **Native code and services** (for example C++ engines, Python pipelines, web APIs): stay as they are.

If each layer is built and versioned on its own, linked through published packages (such as NuGet or Yak) rather than direct source references, the port stays contained to the top layer. The thinner that layer, the smaller your migration.

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="gh2-migration-2.png" caption="Optimize your plugin architecture." caption-align="center" no-back=true >}}
{{< /div >}}

{{< call-out tip  >}} 
How big your port is depends on how much logic lives inside your components. Ideally, components are thin: each takes Grasshopper inputs, hands them to your core library, and puts the results back on the canvas. Code that never knew Grasshopper existed stays exactly as it is. Only the thin top layer is rewritten. If your domain logic lives inside `SolveInstance`, consider moving it into a separate library first. Your port then shrinks to the same thin layer.
{{< /call-out >}}

**Choose your approach.** There are three ways to do the rewrite. In practice you combine them.

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="gh2-migration-3.png" caption="3 ways to rewrite your GH1 plugin." caption-align="center" no-back=true >}}
{{< /div >}}

## Step by step: the migration loop

The two AI tools form a loop. Claude Code edits the source and builds the `.rhp`. Rhino MCP loads it in GH2, runs a test definition, takes a screenshot and reports errors. Those go straight back to Claude Code. You stay in the middle and own the judgement calls.

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="gh2-migration-7.png" caption="The migration loop." caption-align="center" no-back=true >}}
{{< /div >}}

### 1. Set up the GH2 project

Work on a Git branch and keep the GH1 project untouched; the GH2 project lives next to it. Use the `Rhino.Templates` extension to create a GH2 project, which pulls in the Grasshopper2 package:

```bash
dotnet new install Rhino.Templates
dotnet new gh2 --IncludeSample false -n MyPlugin.Grasshopper2 -o gh2
```

Add your core library as a dependency. Set a launch profile that opens Rhino 9 with GH2 when you run. 

### 2. Port parameters and Goos first

Components depend on your custom types, so port those first. `GH_PersistentParam<T>` becomes `Parameter<T>`, and `GH_Goo<T>` becomes `TypeAssistant<T>`. Give each a new `[IoId]` GUID and port their unit tests too. Run this in Claude Code from the project directory:

{{< call-out tip "Skill" >}} 
```text
Port the Grasshopper 1 parameters and Goos from <gh1_project> to <gh2_project>. Match types from Grasshopper 1 to the respective in Grasshopper 2 (GH_PersistentParam<T> -> Parameter<T>, GH_Goo<T> -> TypeAssistant<T>). Be conscious of any inconsistencies in your understanding and refer to the Grasshopper 1 and 2 API documentation for specification. Port parameter and goo unit tests accordingly, and test after porting to ensure they are up to par with the Grasshopper 1 unit tests. Generate unique ids for the new parameters.
```
{{< /call-out >}}

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="gh2-migration-5.png" caption="Visual Studio & Claude Code. Example: Rhino.Ecologic migration." caption-align="center" no-back=true >}}
{{< /div >}}

### 3. Port components

For each component, match the types, add an `[IoId]`, bring over the icons, keep tab and plugin naming consistent, and pull in any helper methods and NuGet packages it needs. In Claude Code:

{{< call-out tip "Skill" >}} 
```text
Port the <name> Grasshopper 1 component to Grasshopper 2, from <gh1_project> to <gh2_project>. Match the types from Grasshopper 1 to Grasshopper 2's types. Refer to the Grasshopper 1 and 2 API documentation for specification. Generate a unique id for the new component and port the icon assets, using the vector version where available, embedded into the built artifact. Be consistent with tab and plugin naming. Where methods from utility or helper classes are called, port them to the new project, respecting the target framework, and add NuGet packages as needed. Use Rhino MCP to convert the test definitions <dir>. After porting, run the definition(s) to validate the ported component behaves according to specification.
```
{{< /call-out >}}

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="gh2-migration-6.png" caption="Visual Studio & Claude Code. Example: Rhino.Ecologic migration." caption-align="center" no-back=true >}}
{{< /div >}}

### 4. Wrap the steps into a skill

Once the prompts work, save them as a Claude Code skill. After that, one line handles a whole component: *convert this `<name>` component from GH1 to GH2*. You rarely type the full prompts again.

### 5. Test in a live Rhino with Rhino MCP

Give the agent your GH1 test definition (or let it write a test definition for you). It opens both canvases, rebuilds the definition in GH2, solves both versions and compares the outputs. Move sliders on either side and check that the values stay in sync. Ask it to report deviations rather than hide mismatches. Through Rhino MCP:

{{< call-out tip "Skill" >}} 
```text
Port this Grasshopper 1 definition <gh1_definition> to <output>. Parse the definition and understand its components and layout. Match the parameters and maintain both the layout and grouping. Maintain references to geometry or external files. If run via Rhino, launch Grasshopper 2 and load the produced definition. Add a step for serializing and exporting fixtures for testing and easy repetition.
```
{{< /call-out >}}

Saved fixtures make every later test repeatable. McNeel's developer guide suggests strict comparison rules: list and tree counts must match exactly; numbers must agree within a tolerance; geometry must match on bounding box and element count; any structure or count mismatch is a hard fail.

### 6. Fix, rebuild, repeat

Feed errors and screenshots back to Claude Code, rebuild, and test again. When a component passes, move to the next one. Keep a list of anything skipped and why.

## What's easy: hand it to the AI

Most of a GH1-to-GH2 port is mechanical and repetitive, and that is where AI does best. A mature plugin can be a whole wall of components, parameters and icons that all need the same treatment. Hand these off:

- **Renames across every file.** `GH_Component` to `Component`; `RegisterInputParams` / `RegisterOutputParams` / `SolveInstance` to `AddInputs` / `AddOutputs` / `Process`.
- **IDs.** Adding an `[IoId]` GUID to every component and parameter, so none silently fails to load.
- **Assemblies and packages.** Swapping `Grasshopper.dll` for `Grasshopper2.dll` and adding the NuGet packages that helpers need.
- **Scaffolding.** Setting up the parallel GH2 build target that outputs the `.rhp`.
- **The compile loop.** Running `dotnet build`, reading compiler errors and fixing them.
- **Icons and naming.** Porting icon assets (vector where available) and keeping tab and plugin names consistent.
- **Test definitions.** Rebuilding GH1 definitions on a GH2 canvas, keeping layout and grouping, and saving fixtures.

## What needs careful attention

AI does the boring 80% well. The 20% that matters is new design work, and it stays with you.

- **Custom data types and the value model.** Porting your Goos to GH2's new value model is a design decision, not a rename. Check that the agent picked the correct GH2 type, not the closest-sounding name.
- **Viewport and preview code.** Custom viewport previews have to be rewritten against the GH2 and Eto viewport APIs. Treat custom display, attributes and mouse interaction as new code.
- **Data trees.** Branch and path handling is the most common source of definitions that solve but are wrong. Compare branch and item counts, not just values.
- **Component IDs.** IDs are hard to change once users have files that reference them. The prompts in this tutorial generate new `[IoId]` GUIDs; McNeel's developer guide suggests reusing the GH1 `ComponentGuid` so existing documents stay identifiable. Decide this once, up front.
- **Builds clean, broken on the canvas.** A plugin that compiles can still misbehave in Grasshopper. Test in a real Rhino, not just the compiler. The Rhino MCP loop is what catches this.
- **Missing equivalents.** When a component has no clean GH2 equivalent, the agent should skip it and list it, not write a stub that silently solves to nothing.
- **The .NET target.** Rhino 9 defaults to .NET 10. Changing the target framework is one line in the project file. The real work is making sure your own libraries and every dependency support .NET 10, since some packages may not yet, or may have changed their APIs.
- **Reviewing generated code.** Read every diff. Agents know GH2 less well than GH1, so they may guess. Ask them to say when they are unsure and to check the GH1 and GH2 API docs.


## Next steps: ship it

A port is finished when users can install it. Publish the GH2 `.rhp` to the **Rhino Package Manager** for one-click installation (see the [Yak guide](https://developer.rhino3d.com/en/guides/yak/)), update your [food4Rhino](https://www.food4rhino.com/en/app/panelingtools-rhino-and-grasshopper) listing, and announce the plugin on the [Rhino Plugins forum](https://discourse.mcneel.com/c/plug-ins/32).

## Resources

- [Upgrade GH1 to GH2 definitions with Rhino&AI](https://mcneel.github.io/RhinoAI/docs/advanced/upgrade-gh1-to-gh2/): porting `.gh` files and comparing canvases.
- [Upgrade GH1 components to GH2 (developers)](https://mcneel.github.io/RhinoAI/docs/developers/upgrade-gh1-to-gh2/): McNeel's plugin porting guide, with fixtures and comparison rules.
- [RhinoAI on GitHub](https://github.com/mcneel/RhinoAI): the public Rhino MCP repo.
- [Grasshopper2 NuGet package](https://www.nuget.org/packages/Grasshopper2/9.0.26258.12303-beta?_src=template) (beta).
- [GH2 template (CSGrasshopper2)](https://github.com/mcneel/RhinoVisualStudioExtensions/tree/main/Rhino.Templates/content/CSGrasshopper2) and [Your first GH2 component](https://developer.rhino3d.com/guides/grasshopper2/your-first-component-mac/).
- [Grasshopper 2 beta announcement](https://discourse.mcneel.com/t/rhino-beta-feature-grasshopper-2-beta/221336) on the McNeel forum.
- Based on a talk by Verena Vogler at the Rhino Developer Meeting, Barcelona, September 25, 2026.

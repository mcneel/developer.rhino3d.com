+++
aliases = ["/en/wip/guides/ai/plugins/"]
authors = [ "vanessa" ]
categories = [ "Plug-in Development" ]
description = "Use an AI coding assistant and RhinoMCP to build a real Rhino plug-in from scratch, from prototyping the idea in conversation to packaging it for distribution."
keywords = [ "developer", "ai", "plugins", "python", "scripting", "rhinomcp", "vibe coding" ]
languages = [ "Python" ]
sdk = [ "AI", "RhinoCommon" ]
title = "Vibe Coding a Rhino Plug-in"
type = "guides"
weight = 40
override_last_modified = "2026-11-20T00:00:00Z"
short_description = "Build a real Rhino plug-in with an AI coding assistant, from prototype to package."
thumbnail = ""
tags = ["rhino", "version 9", "python", "scripting", "rhinomcp", "plugins"]

[admin]
TODO = "Scaffolded from everyday-tools/index.md — needs real walkthrough content, screenshots, and a working sample plug-in."
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
lead = "Chat with an AI assistant connected to Rhino through RhinoMCP to prototype a plug-in idea live, then turn it into a packaged, distributable Rhino plug-in."
hero_image = ""
meta = ["30 min", "Rhino 9 for Windows / Mac", "Intermediate"]
+++

Rhino connects to an AI assistant through the [Model Context Protocol](https://modelcontextprotocol.io) (MCP) with the native {{< rhino-command english-command="RhinoMCP" local-command="RhinoMCP">}} and {{< rhino-command english-command="mcpstart" local-command="mcpstart">}} commands. Where [Vibe Coding your Tools in Rhino](/docs/guides/vibe-coding/everyday-tools/) turns a single conversation into a script and a command alias, this tutorial goes further: we'll use an AI coding assistant and a developer tool such as Visual Studio Code to build a real Rhino plug-in, from first prototype to something you can package and share.

## What You'll Need

{{< checklist >}}
- **Rhino 9** for Windows or Mac.
- **An MCP-capable AI chat client**, such as Claude Desktop, that can connect to a local MCP server.
- **Visual Studio Code** (or another code editor) to hold the plug-in project.
- **No prior plug-in development experience required.** The assistant writes and edits the code for you; some familiarity with C# or Python is helpful, but not necessary, if you want to read along.
{{< /checklist >}}

## Connect Rhino to an AI Assistant

**NOTE TO SELF:** Reuse/link the connection steps from [Vibe Coding your Tools in Rhino](/docs/guides/vibe-coding/everyday-tools/#connect-rhino-to-an-ai-assistant) once that section is finalized, instead of duplicating it here.

{{< call-out danger "This Gives the Assistant Real Control" >}}
Once connected, the assistant can create, modify, and delete geometry, and run arbitrary code in your Rhino session. Only connect it to a file you don't mind an AI editing, and run {{< rhino-command english-command="mcpstart" local-command="mcpstart">}} again to close the bridge, or quit the chat client, once you're done experimenting.
{{< /call-out >}}

## Prototype the Plug-in Idea in Conversation

**NOTE TO SELF:** Walk through describing the plug-in's intended behavior to the assistant and iterating on a working prototype in the live Rhino session, the same way `everyday-tools` iterates on the speaker grid script.

## Scaffold the Plug-in Project

**NOTE TO SELF:** Cover generating a real Rhino plug-in project (e.g. via the `yak` / Visual Studio / VS Code plug-in templates) with the assistant's help, and moving the prototyped logic into it.

## Build and Test in Rhino

**NOTE TO SELF:** Cover loading the plug-in into Rhino for testing (`PlugInManager`, debug attach from the editor), and iterating with the assistant when something doesn't work.

## Package the Plug-in

**NOTE TO SELF:** Cover packaging with {{< rhino-command english-command="PackageManager" local-command="PackageManager">}} / Yak for distribution. See [How to Use Scripts and Plugins](/docs/guides/scripts-plugins/how-to-use/) for existing packaging guidance to draw from.

## Where to Go from Here

- Prefer a lighter-weight approach first? See [Vibe Coding your Tools in Rhino](/docs/guides/vibe-coding/everyday-tools/) for turning a single script into a command and toolbar button, no packaging required.
- Remember to close the {{< rhino-command english-command="mcpstart" local-command="mcpstart">}} bridge when you're not actively using it — there's no reason to leave an AI assistant with live code execution access to Rhino running in the background.

---

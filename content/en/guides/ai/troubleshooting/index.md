+++
aliases = []
authors = [ "callum" ]
categories = [ "Troubleshooting" ]
description = "Answers to common Rhino MCP problems: the assistant can't see Rhino, crashes, missing geometry, targeting Rhino 9, Grasshopper tools, and plug-in install issues."
keywords = [ "developer", "ai", "rhinomcp", "mcp", "troubleshooting", "FAQ", "support", "connection" ]
languages = []
sdk = [ "AI" ]
title = "Rhino MCP Troubleshooting"
type = "guides"
weight = 100
override_last_modified = "2026-11-23T00:00:00Z"
short_description = "Fixes for common Rhino MCP connection and setup problems."
thumbnail = ""
tags = ["rhino", "version 8", "version 9", "ai", "rhinomcp", "troubleshooting"]

[admin]
TODO = ""
origin = "https://github.com/mcneel/RhinoAI/tree/main/docs/content/docs/troubleshooting.md"
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
eyebrow = "Rhino MCP · Troubleshooting"
lead = "Plain-language answers to the most common Rhino MCP gotchas."
hero_image = ""
meta = ["5 min", "Rhino 8 / 9 for Windows / Mac", "Beginner"]
+++

Common issues. If you don't find your problem here, [open an issue on GitHub](https://github.com/mcneel/RhinoAI/issues) or ask in the [Rhino Discourse AI category](https://discourse.mcneel.com/c/rhino/artificial-intelligence-rhino/162).

## My AI Agent doesn't see Rhino at all

Most often this means the connection wasn't made on startup.

1. Restart **quit and reopen** your AI assistant
2. Make sure you installed the Rhino plugin via Rhino's `PackageManager` (search for **Rhino-MCP-Platform**).
3. In Claude Desktop, check Settings → Extensions to see if the Rhino3d connector is listed as connected.

## Rhino just crashed mid-conversation

The connector notices when Rhino crashes and tells your assistant, so the assistant can offer to relaunch and retry.

{{< call-out warning >}}
If the same prompt keeps causing a crash, ask Claude or your LLM of choice to help you file an issue on GitHub.
{{< /call-out >}}

## The assistant says it did something, but I don't see it

A few things to check:

- **Are you looking at the right Rhino window?** If you have several open, the assistant may have edited a different one. Look at the window titles.
- **Use View → Zoom → Zoom Extents.** the geometry may be far from the origin.
- **Check the layers panel.** Geometry may be on a hidden layer.

## I want to use Rhino 9 (WIP/BETA) instead of Rhino 8

The router defaults to Rhino 8. To target Rhino 9:

- **Claude Desktop:** Open the settings for the connector and change 8 to 9
- **Claude Code / custom config:** Add `"args": ["-v", "9"]` to the `mcpServers` -> `rhino` key in `~/.claude.json`.

## Grasshopper tools aren't working

- Grasshopper 2 tools (`gh2_`) require **Rhino 9 WIP/BETA**.
- If you want to use Grasshopper 2, specify Rhino WIP to your AI Agent

## The MCP Plugin doesn't load or show up in the package manager?

- Net framework is not supported
- Intel Macs are not supported
- Update your Rhino to the latest release

## Anywhere else to ask?

{{< call-out info >}}
- [GitHub issues](https://github.com/mcneel/RhinoAI/issues) for bugs or documentation errors.
- [Rhino Discourse AI category](https://discourse.mcneel.com/c/rhino/artificial-intelligence-rhino/162) for questions and ideas.
{{< /call-out >}}

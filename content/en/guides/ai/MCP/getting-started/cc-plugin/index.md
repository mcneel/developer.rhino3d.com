+++
aliases = []
authors = [ "callum" ]
categories = [ "Getting Started" ]
description = "Connect the Claude Code terminal assistant to Rhino and Grasshopper using the Rhino-MCP-Platform plugin."
keywords = [ "developer", "ai", "rhinomcp", "mcp", "Claude Code", "Anthropic", "agents", "terminal" ]
languages = []
sdk = [ "AI" ]
title = "Claude Code"
type = "guides"
weight = 3
override_last_modified = "2026-11-21T00:00:00Z"
short_description = "Connect Claude Code to Rhino with the Rhino MCP."
thumbnail = ""
tags = ["rhino", "ai", "rhinomcp", "mcp"]

[admin]
TODO = ""
origin = "https://github.com/mcneel/RhinoAI/tree/main/docs/content/docs/getting-started/cc-plugin.md"
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
eyebrow = "Rhino MCP · Getting Started"
lead = "Use Claude Code, Anthropic's terminal-based assistant, to drive Rhino and Grasshopper through the Rhino MCP."
hero_image = ""
meta = ["10 min", "Rhino 8 for Windows / Mac", "Beginner"]
+++

[Claude Code](https://claude.com/claude-code) is Anthropic's terminal-based AI assistant. Claude Code is a great fit if you're comfortable in a terminal or already use it for code. If you're not sure, start with [Claude Desktop](../connector/), it's much more friendly.

## 1. Install Claude Code

[Claude Code](https://claude.com/claude-code)

## 2. Install the Rhino plugin (Rhino 8 only!)

1. Open Rhino 8 (and/or Rhino 9 WIP/BETA)
2. Run the `PackageManager` command
3. Search for, and install Rhino-MCP-Platform

## 3. Connect the two

1. Run the `MCPConnect` command
2. Copy and Paste the prompt into a new Claude Code session
3. Restart Claude Code if prompted to

## Try it out

{{< call-out info >}}
Open Claude Code and follow the prompts on the [Try It Out](../../try-it-out/) page.
{{< /call-out >}}

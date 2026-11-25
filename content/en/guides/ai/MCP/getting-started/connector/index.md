+++
aliases = []
authors = [ "callum" ]
categories = [ "Getting Started" ]
description = "Install the Rhino MCP connector in Claude Desktop and the Rhino-MCP-Platform plugin in Rhino."
keywords = [ "developer", "ai", "rhinomcp", "mcp", "Claude Desktop", "connector", "Anthropic", "setup" ]
languages = []
sdk = [ "AI" ]
title = "Claude Desktop"
type = "guides"
weight = 2
override_last_modified = "2026-11-21T00:00:00Z"
short_description = "Connect Claude Desktop to Rhino with the Rhino MCP connector."
thumbnail = ""
tags = ["rhino", "ai", "rhinomcp", "mcp"]

[admin]
TODO = ""
origin = "https://github.com/mcneel/RhinoAI/tree/main/docs/content/docs/getting-started/connector.md"
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
lead = "Claude Desktop is the easiest way to start: install the connector, install the Rhino plugin, and start chatting."
hero_image = ""
meta = ["10 min", "Rhino 8 for Windows / Mac", "Beginner"]
+++

[Claude Desktop](https://claude.ai/download) is Anthropic's user-friendly chat app for Windows and Mac. With our connector installed, anything you ask Claude in the chat window can now happen in Rhino & Grasshopper.

## 1. Install Claude Desktop

[Claude Desktop](https://claude.ai/download)

## 2. Install the Claude connector

1. Download [`connector.mcpb`](https://github.com/mcneel/RhinoAI/releases/download/connector-v0.1.6/connector.mcpb).
2. Open Claude Desktop and go to `Settings` &rarr; `Extensions` &rarr; `Advanced settings`.
3. Click `Install Extension` and select the downloaded `connector.mcpb`.
4. Click `Install` to confirm.

That's it. The connector is now wired up.

## 3. Install the Rhino plugin (Rhino 8 only!)

1. Open Rhino 8
2. Run the `PackageManager` command
3. Search for, and install Rhino-MCP-Platform

### Or let Claude install it

> The desktop connector can also install the plugin for you if you ask it to.

Paste the following into your AI agent. It will install it for you, so there is no need to open Rhino.

{{< call-out tip "Prompt" >}}
```text
Install the `Rhino-MCP-Platform` plugin into Rhino using Yak (Rhino's Package Manager). `$1` is the Rhino major version to target (e.g. `8`). If omitted, default to `8`.

1. Locate the Yak CLI for Rhino `$1`. It ships with Rhino:
   - macOS: `/Applications/Rhino $1.app/Contents/Resources/bin/yak`
   - Windows: `C:\Program Files\Rhino $1\System\Yak.exe`
2. Install the plugin from the public package server:
   
   `yak install Rhino-MCP-Platform`
   
3. Restart Rhino `$1` so the newly installed plugin is loaded.
4. In Rhino, run the `MCPStart` command to confirm the plugin is available.

To upgrade an existing install, run `yak update Rhino-MCP-Platform`. To remove it, run `yak uninstall Rhino-MCP-Platform`.
```
{{< /call-out >}}

## Try it out

{{< call-out info >}}
Open Claude Desktop, start a new chat, and follow the prompts on the [Try It Out](../../try-it-out/) page.
{{< /call-out >}}

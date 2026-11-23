+++
aliases = []
authors = [ "stevef" ]
categories = [ "Getting Started" ]
description = "Configure Google Gemini CLI to use the Rhino MCP router."
keywords = [ "developer", "ai", "rhinomcp", "mcp", "Gemini CLI", "Google", "terminal", "CLI" ]
languages = []
sdk = [ "AI" ]
title = "Gemini CLI"
type = "guides"
weight = 6
override_last_modified = "2026-11-21T00:00:00Z"
short_description = "Connect Gemini CLI to Rhino with the Rhino MCP."
thumbnail = ""
tags = ["rhino", "ai", "rhinomcp", "mcp"]

[admin]
TODO = ""
origin = "https://github.com/mcneel/RhinoAI/tree/main/docs/content/docs/getting-started/gemini.md"
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
lead = "Add the Rhino MCP router to Gemini CLI's MCP settings to drive Rhino and Grasshopper from the terminal."
hero_image = ""
meta = ["10 min", "Rhino 8 for Windows / Mac", "Beginner"]
+++

[Gemini CLI](https://github.com/google-gemini/gemini-cli) is Google's open-source terminal AI assistant. It speaks MCP, so once you point it at the Rhino MCP server it can drive Rhino & Grasshopper the same way Claude or Codex can.

If you're choosing between assistants and aren't sure, start with [Claude Desktop](../connector/); it's the gentler entry point.

## 1. Install Gemini CLI

[Gemini CLI](https://github.com/google-gemini/gemini-cli) — install and sign in. See the [Gemini CLI install guide](https://github.com/google-gemini/gemini-cli#installation) if you need it.

## 2. Install the Rhino plugin (Rhino 8 only!)

1. Open Rhino 8
2. Run the `PackageManager` command
3. Search for, and install Rhino-MCP-Platform

## 3. Wire up the Rhino MCP server

1. In Rhino, run the `MCPConnect` command. It prints the command Gemini CLI needs to launch the Rhino MCP router.
2. Open `~/.gemini/settings.json` (create it if it doesn't exist).
3. Add an `mcpServers` entry for the Rhino server, pasting the command and args from step 1:

   ```json
   {
     "mcpServers": {
       "rhino": {
         "command": "rhino-mcp-router",
         "args": ["--default-version", "8"]
       }
     }
   }
   ```

4. Restart Gemini CLI. The `rhino` server should appear when you list MCP servers from inside a session.

{{< call-out tip "Rhino version" >}}
Pick the Rhino version by changing the `--default-version` arg. Use `8` for Rhino 8, `9` for Rhino 9 WIP/BETA.
{{< /call-out >}}

## Try it out

{{< call-out info >}}
Start a Gemini CLI session and follow the prompts on the [Try It Out](../../try-it-out/) page.
{{< /call-out >}}

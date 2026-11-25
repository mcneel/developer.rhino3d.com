+++
aliases = []
authors = [ "stevef" ]
categories = [ "Getting Started" ]
description = "Configure GitHub Copilot agent mode in VS Code to use the Rhino MCP router."
keywords = [ "developer", "ai", "rhinomcp", "mcp", "GitHub Copilot", "VS Code", "MCP", "agent mode" ]
languages = []
sdk = [ "AI" ]
title = "GitHub Copilot"
type = "guides"
weight = 4
override_last_modified = "2026-11-21T00:00:00Z"
short_description = "Connect GitHub Copilot in VS Code to Rhino with the Rhino MCP."
thumbnail = ""
tags = ["rhino", "ai", "rhinomcp", "mcp"]

[admin]
TODO = ""
origin = "https://github.com/mcneel/RhinoAI/tree/main/docs/content/docs/getting-started/copilot.md"
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
lead = "Run GitHub Copilot in agent mode inside VS Code and point it at the Rhino MCP router."
hero_image = ""
meta = ["10 min", "Rhino 8 for Windows / Mac", "Beginner"]
+++

[GitHub Copilot](https://github.com/features/copilot) in VS Code can act as an MCP client when run in **agent mode**. Point it at the Rhino MCP server and Copilot can drive Rhino directly from your editor.

If you're choosing between assistants and aren't sure, start with [Claude Desktop](../connector/); it's the gentler entry point.

## 1. Install GitHub Copilot

[VS Code 1.99](https://code.visualstudio.com) or newer, with the **GitHub Copilot** and **GitHub Copilot Chat** extensions installed and signed in. Agent mode lives in Copilot Chat: open the Chat view and switch the mode selector from **Ask** to **Agent**.

## 2. Install the Rhino plugin (Rhino 8 only!)

1. Open Rhino 8
2. Run the `PackageManager` command
3. Search for, and install Rhino-MCP-Platform

## 3. Wire up the Rhino server

1. In Rhino, run the `MCPConnect` command. It prints the command Copilot needs to launch the Rhino MCP router.
2. In your workspace, create `.vscode/mcp.json` (or edit your User `settings.json` if you want it available everywhere).
3. Add an entry for the Rhino server, pasting the command and args from step 1:

   ```json
   {
     "servers": {
       "rhino": {
         "command": "rhino-mcp-router",
         "args": ["--default-version", "8"]
       }
     }
   }
   ```

4. Reload VS Code. In the Copilot Chat agent-mode tool picker, you should see the `rhino` server and its tools listed.

{{< call-out tip "Rhino version" >}}
Pick the Rhino version by changing the `--default-version` arg. Use `8` for Rhino 8, `9` for Rhino 9 WIP/BETA.
{{< /call-out >}}

## Try it out

{{< call-out info >}}
Open Copilot Chat in **Agent** mode and follow the prompts on the [Try It Out](../../try-it-out/) page.
{{< /call-out >}}

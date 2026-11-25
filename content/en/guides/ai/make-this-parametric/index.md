+++
aliases = []
authors = [ "callum" ]
categories = [ "Automation" ]
description = "Use an AI assistant and RhinoMCP to reverse-engineer hand-modeled Rhino geometry into a slider-driven Grasshopper 2 definition."
keywords = [ "developer", "ai", "rhinomcp", "parametric", "grasshopper", "grasshopper 2", "GH2", "reverse engineer" ]
languages = []
sdk = [ "AI", "Grasshopper 2" ]
title = "Make This Parametric"
type = "guides"
weight = 47
override_last_modified = "2026-11-21T00:00:00Z"
short_description = "Rebuild hand-modeled geometry as a slider-driven GH2 definition."
thumbnail = ""
tags = ["rhino", "version 9", "ai", "rhinomcp", "grasshopper"]

[admin]
TODO = "Source page was draft. Needs a hero image and a tested example. Removed Related link to the advanced 'Upgrade a GH1 script to GH2' page; restore once that page exists on the developer site."
origin = "https://github.com/mcneel/RhinoAI/tree/main/docs/content/docs/advanced/make-this-parametric.md"
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
eyebrow = "Grasshopper · Tutorial"
lead = "Hand-modeled something and now need it parametric? Have the assistant read your geometry, infer the recipe, and rebuild it as a GH2 graph driven by sliders."
hero_image = ""
meta = ["30 min", "Rhino 9 for Windows / Mac", "Intermediate"]
+++

You've modeled something by hand (a stair, a panelized facade, a piece of furniture) and now you wish you'd built it in Grasshopper from the start, because the client just asked for "the same thing but 200mm taller and with seven of them instead of five."

This workflow puts the assistant in the role of a Grasshopper author: it reads the geometry you already made, infers the recipe, and rebuilds it as a GH2 graph that drives the same result from sliders.

## What you need

- An MCP-connected assistant ([Claude Code](../MCP/getting-started/cc-plugin/), Claude Desktop, or similar).
- **Rhino 9** with Rhino MCP running, your hand-built model open, and a GH2 canvas available.
- A rough mental model of what the parameters should be. The assistant can guess, but you'll get a better graph if you say so.

## A prompt to start with

{{< call-out tip "Prompt" >}}
```text
I've modeled this stair by hand. Look at the geometry on layer
`Stair`, work out the construction recipe, and rebuild it as a GH2
definition driven by sliders for tread depth, riser height, total
rise, and number of treads. Reference my existing geometry in the
Rhino doc only as a target to match; the GH definition should
generate it from scratch. Solve and compare.
```
{{< /call-out >}}

## What you should see

The assistant calls `list_objects` and reads attributes off your geometry (layer, dimensions, counts, bounding boxes) to reverse-engineer the rules. Then it builds the GH2 graph with `g2_place_component`, `g2_connect`, and `g2_place_slider`, solves it, and compares the output to your reference geometry, usually by checking key dimensions and counts rather than a literal Brep diff.

Expect a back-and-forth: the assistant will often ask "is the spacing uniform, or does it follow a curve?" before committing to a topology.

## What to review

- **The parameter set.** You wanted four sliders: did you get four? The assistant sometimes adds extras for things you'd rather hard-code, or hard-codes something you wanted to expose. A quick prompt fixes it.
- **Did it match, or did it cheat?** The cheapest way to "match" your geometry is to bake your existing Rhino objects into the GH output. That's not parametric. Have the assistant show you the graph and confirm it generates from primitives, not from referenced objects.
- **Edge cases.** Push the sliders to extremes (1 tread, 100 treads, zero rise) and see whether the graph degrades gracefully or explodes. Real-world stairs don't have 100 treads, but the failure mode tells you whether the topology is right.

## When the assistant gets stuck

- **Ambiguous intent.** If your hand model has irregular spacing or one-off tweaks, the assistant can't tell whether those are intentional features or sloppy modeling. Tell it explicitly which variations are parametric and which were drift.
- **Missing GH2 components.** If the recipe needs something GH2 doesn't have yet, ask for the gap to be called out rather than papered over with a `run_python` node that hides the logic.
- **Over-fitting to one example.** A graph that exactly reproduces your reference but breaks for any other input isn't useful. If you only see it solve once, push it.

+++
aliases = []
authors = [ "callum" ]
categories = [ "Automation" ]
description = "Use an AI assistant and RhinoMCP slots to capture viewport images from many files, cameras, or design options without touching your active document."
keywords = [ "developer", "ai", "rhinomcp", "headless", "render farm", "slots", "viewport capture", "automation" ]
languages = [ "Python", "C#" ]
sdk = [ "AI", "RhinoCommon" ]
title = "Headless Render Farm"
type = "guides"
weight = 46
override_last_modified = "2026-11-21T00:00:00Z"
short_description = "Batch-capture viewport images in headless RhinoMCP slots."
thumbnail = ""
tags = ["rhino", "version 8", "version 9", "ai", "rhinomcp", "automation", "rendering"]

[admin]
TODO = "Source page was draft. Needs a hero image and a tested example. Removed link to the Recipes doc-handle note; restore once that page exists on the developer site."
origin = "https://github.com/mcneel/RhinoAI/tree/main/docs/content/docs/advanced/headless-render-farm.md"
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
eyebrow = "Automation · Tutorial"
lead = "Spin up headless Rhino documents, point cameras, dump viewport images, and tear them down again, for turntables, sun studies, and option matrices."
hero_image = ""
meta = ["30 min", "Rhino 8 / 9 for Windows / Mac", "Intermediate"]
+++

If you have a model you need to capture from many angles (a study model with twenty options, a presentation board, a turntable, a daylight sweep), the MCP can spin up headless Rhino documents in parallel, point cameras at them, dump viewport images, and tear them down again without you ever clicking "New Document".

This is what the **slot** tools are for. Each slot is its own Rhino document; the assistant can open, drive, and close them programmatically while your main session keeps its window focused on whatever you were actually doing.

## What you need

- An MCP-connected assistant ([Claude Code](../MCP/getting-started/cc-plugin/), Claude Desktop, or similar).
- **Rhino** running with Rhino MCP.
- A `.3dm` (or several) you want to capture, or a recipe the assistant can build from scratch.
- A folder you're happy for the assistant to write images into.

## A prompt to start with

{{< call-out tip "Prompt" >}}
```text
Open `studies/option-*.3dm`, each in its own slot. For every file,
set the camera to an isometric view framed on layer `Massing`, render
the active viewport at 1920&times;1080, save it as
`renders/<filename>.png`, and close the slot. Don't touch my current
document.
```
{{< /call-out >}}

Variations worth trying:

- **Turntable**: "spin the camera around the model in 15&deg; steps, save each frame numbered."
- **Sun study**: "step the sun from 08:00 to 18:00 in 30-minute intervals, capture from the same camera each time."
- **Option matrix**: "for every combination of these three GH sliders, solve, capture, label the filename with the slider values."

## What you should see

The assistant calls `spawn_slot` for each file or variation, `open_doc` into that slot, `set_camera` (or `run_command` for named views), `get_viewport_image` to capture, then `close_slot` when it's done. Your main Rhino window stays on whatever you had open; the slot documents are headless siblings, not takeovers.

If it's working from a Grasshopper definition, expect to see `g2_*` solve calls between the camera move and the capture so the geometry updates before the shutter clicks.

## What to review

- **Camera framing.** Headless slots don't have a viewport you can eyeball, so the assistant is guessing at zoom and target. Ask it to do one capture first and show you the image before it loops over fifty.
- **Render settings.** `get_viewport_image` captures the display mode, not a Rendered/Raytraced pass by default. If you need ray-traced output, say so explicitly and check the first frame matches what you expected.
- **Output paths.** Make the assistant echo the full output folder before it starts. Cheaper than discovering forty PNGs landed in the wrong place.

## When the assistant gets stuck

Common failure modes:

- **Slot leak.** If a run errors halfway through, slots may stay open. Ask for a `list_slots` and have it close anything stray.
- **ActiveDoc confusion.** Remind it that each slot has its own document handle; `sc.doc` inside a `run_python` call may not be the slot you think.
- **Memory pressure.** Spinning up many slots at once can chew RAM. Cap the parallelism ("do at most four at a time") rather than letting it fan out.

## Related

- [Bulk file processing](../bulk-file-processing/): same slot-per-file shape, but the per-file job is "modify and save", not "render".

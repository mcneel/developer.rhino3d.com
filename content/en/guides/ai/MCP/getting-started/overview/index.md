+++
aliases = []
authors = [ "callum" ]
categories = [ "Getting Started" ]
description = "Choose an MCP-capable AI assistant and connect it to Rhino and Grasshopper in about ten minutes."
keywords = [ "developer", "ai", "rhinomcp", "mcp", "getting started", "installation", "setup" ]
languages = []
sdk = [ "AI" ]
title = "Getting Started with Rhino MCP"
type = "guides"
weight = 1
override_last_modified = "2026-11-21T00:00:00Z"
short_description = "Pick an AI assistant and connect it to Rhino and Grasshopper."
thumbnail = ""
tags = ["rhino", "ai", "rhinomcp", "mcp"]

[admin]
TODO = ""
origin = "https://github.com/mcneel/RhinoAI/tree/main/docs/content/docs/getting-started/_index.md"
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
lead = "Connect an AI assistant to Rhino and Grasshopper through the Rhino MCP in about ten minutes."
hero_image = ""
meta = ["10 min", "Rhino 8 for Windows / Mac", "Beginner"]
+++

{{< call-out warning >}}
This guide assumes you have [Rhino 3D](https://www.rhino3d.com/download/) already installed and licensed.
{{< /call-out >}}

In about ten minutes you'll have your AI assistant making geometry in your Rhino and/or Grasshopper window. We'll do it in a couple steps:

## Pick an AI assistant

Any AI assistant that speaks the [Model Context Protocol](https://modelcontextprotocol.io) can drive Rhino & Grasshopper. *Choose one of the AI assistants below to continue.*

- [**Claude Desktop**](../connector/) — A friendly chat app from Anthropic. _Easiest to install and use._
- [**Claude Code**](../cc-plugin/) — A terminal-based (CLI) assistant that feels more like coding than chat.
- [**GitHub Copilot**](../copilot/) — GitHub's AI assistant inside VS Code. Switch to Agent mode and point it to the Rhino MCP router.
- [**OpenAI Codex**](../codex/) — OpenAI's terminal-based assistant (CLI). Point its MCP config at the Rhino MCP router and go.
- [**Gemini CLI**](../gemini/) — Google's open-source terminal assistant (CLI). Drop the Rhino MCP router into its MCP config.
- [**Local LLM**](../lm-studio/) — Run an open-weight model on your own machine and drive Rhino & Grasshopper without Internet.

{{< call-out info >}}
**Other MCP clients work, too.** [Cursor](https://cursor.com) and other MCP-capable assistants can point at the same Rhino MCP router.
{{< /call-out >}}

## Workflow ideas

Once your assistant is connected, try one of these. Each one starts with a single prompt. Keep the conversation going after the first result: "make it taller," "try it in red," or "space them 1.5m apart" all work.

### Model from an image

Paste a photo into your AI assistant and have it build the geometry in Rhino.

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="kettle.jpg" caption="Reference image." caption-align="center" no-back=true >}}
{{< /div >}}

{{< call-out tip "Prompt" >}}
```text
Model this image in Rhino
```
{{< /call-out >}}

The assistant creates the object in Rhino. It won't be exact, but it should capture the general form of the photo.

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="ai-kettle.png" caption="The AI-modeled kettle." caption-align="center" no-back=true >}}
{{< /div >}}

### Build a Grasshopper definition

Have the assistant place and wire up Grasshopper components, using a mix of components and scripts.

{{< call-out tip "Prompt" >}}
```text
Create a Grasshopper script that generates a twisty tower.
```
{{< /call-out >}}

The assistant opens Grasshopper, places the components, connects them, and solves the canvas. The first attempt often fails; the assistant checks the canvas and iterates until it works. When it's done, move the sliders and watch the tower update in Rhino.

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="twisty-tower-gh.png" caption="A twisty tower definition built from one prompt." caption-align="center" no-back=true >}}
{{< /div >}}

### Generate variations

Sweep across size, position, color, or count without building each variant by hand.

{{< call-out tip "Prompt" >}}
```text
Create 30 columns in a grid, randomize their heights between 2m and 6m,
and color them by height (short = pale, tall = dark).
```
{{< /call-out >}}

A grid of 30 columns appears, each at its own height and tinted to match. Refine with follow-ups: "space them 1.5m apart," "use a 5×6 grid," or "weight the heights toward the center."

### Inspect and report

Ask questions about an existing document and get a structured answer back. Useful for audits, hand-offs, and catching problems before a client does. Try it on the sample model: [casa_rhino_shapes.zip](casa_rhino_shapes.zip) (4.8 MB).

{{< call-out tip "Prompt" >}}
```text
What's in this document? Group it by layer and tell me which objects are
off-layer or on a hidden layer.
```
{{< /call-out >}}

The assistant returns a summary of each layer, the object types on it, and a callout for anything off-layer. Drill in with follow-ups: "show me the off-layer objects," "how many blocks have unused definitions?", or "list every layer that's empty."

### Assign objects to layers

One prompt, a chore done. Try it on the sample model: [RayGun.3dm.zip](RayGun.3dm.zip) (1.4 MB).

{{< call-out tip "Prompt" >}}
```text
Assign every object in this file to an appropriate layer.
```
{{< /call-out >}}

The assistant evaluates the model, decides on groupings, and places each group on its own layer.

{{< div style="width:100%" >}}
{{< figure class="figure-no-margins" src="raygun-layers.png" caption="The Ray Gun model sorted onto layers." caption-align="center" no-back=true >}}
{{< /div >}}

## Prompt recipes

More prompts to copy into your assistant, grouped by what you want to do. Treat them as starting points: tweak the numbers, swap the materials, and ask follow-up questions.

### Modeling

#### Parametric furniture

{{< call-out tip "Prompt" >}}
```text
Design a parametric coffee table. Top is 1200×600×30mm walnut.
Four tapered legs, 400mm tall, splayed outward 5°. Put it on a layer
called `Furniture` and apply a wood material.
```
{{< /call-out >}}

#### A spiral staircase

{{< call-out tip "Prompt" >}}
```text
Build a spiral staircase. 20 steps, 250mm rise per step, 1.5m radius.
Each tread is a 30mm-thick wedge in oak. Add a central column in steel.
```
{{< /call-out >}}

#### Random scatter

{{< call-out tip "Prompt" >}}
```text
Scatter 200 spheres of varying radius (between 10 and 80mm) across a
5×5m region. Color them by radius from blue (small) to red
(large). No overlaps.
```
{{< /call-out >}}

#### Boolean exploration

{{< call-out tip "Prompt" >}}
```text
Make me five variations of a chair, each blending a primitive
(cube, sphere, cylinder, cone, torus) into the seat in a different way.
Lay them out in a row, 1.5m apart.
```
{{< /call-out >}}

### Inspection & reporting

#### Document audit

{{< call-out tip "Prompt" >}}
```text
Audit this document. Tell me: how many objects per layer, anything
off-layer, any zero-length curves, any naked edges on the breps, and
the total bounding box.
```
{{< /call-out >}}

#### What's selected?

{{< call-out tip "Prompt" >}}
```text
Look at what I have selected and describe it to me. Give me the
object IDs, types, areas, and what layers they're on.
```
{{< /call-out >}}

#### Viewport snapshot

{{< call-out tip "Prompt" >}}
```text
Take a screenshot of the current viewport and describe what you see.
If anything looks broken or off, point it out.
```
{{< /call-out >}}

### Drawings & drafting

#### Plan and elevations

{{< call-out tip "Prompt" >}}
```text
Set up four standard views of the current geometry: top plan, front
elevation, right elevation, and a 3/4 perspective. Frame each one to
fit the geometry.
```
{{< /call-out >}}

#### Quick dimensions

{{< call-out tip "Prompt" >}}
```text
Add dimensions to the selected object. Use horizontal/vertical
dimensions for orthogonal edges, and aligned dimensions for any
diagonals.
```
{{< /call-out >}}

### Grasshopper

#### From scratch

{{< call-out tip "Prompt" >}}
```text
Build a Grasshopper definition that takes a curve, divides it into
N points (with a slider for N), and places a sphere of slider-controlled
radius at each point.
```
{{< /call-out >}}

#### Explain this definition

{{< call-out tip "Prompt" >}}
```text
Look at the current Grasshopper canvas and walk me through it.
What does each cluster of components do, and what's the final output?
```
{{< /call-out >}}

#### Simplify

{{< call-out tip "Prompt" >}}
```text
Look at the Grasshopper canvas. Are there components that could be
merged, removed, or replaced with a simpler equivalent? Suggest
changes, but don't apply them until I say so.
```
{{< /call-out >}}

#### De-spaghetify

{{< call-out tip "Prompt" >}}
```text
This canvas is a mess. Tidy it up: align components into a left-to-right
flow, group related logic with colored groups and short scribbled
labels, straighten out crossed wires (insert relays where needed), and
hide any wires that are purely structural. Don't change what the
definition does, just make it readable.
```
{{< /call-out >}}

### Cleanup & chores

#### Layer hygiene

{{< call-out tip "Prompt" >}}
```text
Tidy this document's layers. Title case every layer name, delete any
layers with no geometry, and group related layers under sensible
parents.
```
{{< /call-out >}}

#### Standardize materials

{{< call-out tip "Prompt" >}}
```text
Look at every object's material. Where multiple objects share the same
color, consolidate them onto a single named material.
```
{{< /call-out >}}

#### Find the duplicates

{{< call-out tip "Prompt" >}}
```text
Find any objects that are exact duplicates (same geometry, same
position). Move all duplicates to a layer called `Duplicates` so I
can review and delete them.
```
{{< /call-out >}}

### Teaching & learning

#### Walk me through a workflow

{{< call-out tip "Prompt" >}}
```text
I want to model a turbine blade. Walk me through the steps in Rhino:
what curves to draw first, how to sweep them, and what to
watch out for. Don't make geometry yet; just explain.
```
{{< /call-out >}}

#### Explain what just happened

{{< call-out tip "Prompt" >}}
```text
I just ran a boolean and got an unexpected result. Look at what's in
the document and tell me what probably went wrong.
```
{{< /call-out >}}

{{< call-out info >}}
Got a good prompt? Share it in the [Rhino Discourse AI category](https://discourse.mcneel.com/c/rhino/artificial-intelligence-rhino/162).
{{< /call-out >}}

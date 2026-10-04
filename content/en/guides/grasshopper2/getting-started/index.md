+++
aliases = []
authors = [ "mathias" ]
categories = [ "Getting Started" ]
description = "Where to start as a Grasshopper 2 plugin developer: documentation, icons, immutable inputs, and your plugin's id."
keywords = [ "developer", "grasshopper2", "grasshopper", "gh2", "plugin", "icon", "documentation", "guid", "assembly", "immutable" ]
languages = [ "C#" ]
sdk = [ "Grasshopper 2" ]
title = "Getting Started with Grasshopper 2 Plugins"
type = "guides"
weight = 1

[admin]
TODO = "WWW-3714: draft, rephrase the TODO(Mathias) paragraphs"
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 9

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

<!-- TODO(Mathias): rephrase in your own voice. -->

This guide is for anyone who wants to write a Grasshopper 2 plugin. It does not matter whether you have written Grasshopper 1 components before. There is no code in this guide. It covers a few things that are good to know before you start.

## Prerequisites

Grasshopper 2 requires Rhino 9. You also need the development tools. See Installing Tools ([Windows](/guides/grasshopper/installing-tools-windows/), [Mac](/guides/grasshopper/installing-tools-mac/)).

## Learn Grasshopper 2 First

Grasshopper 2 ships with extensive documentation. It is written for users. It is also the best place to learn the concepts the SDK is built on: the *solution*, *components*, *parameters*, *data trees*, and *preview geometry*.

To open it:

1. In Grasshopper 2, click *Help* > *Documentation...*, or press *F1*.
1. In Rhino, run the `GH2Docs` command.
1. For a single component, hover over it and press *?*.

The documentation is interactive. For example, many pages contain live Grasshopper documents. You can drag them onto the canvas and try them out. <!-- TODO(Mathias): confirm the wording of the drag-and-drop example. -->

A read-only copy is available on the web at [rhino3d.com/docs/grasshopper2](https://www.rhino3d.com/docs/grasshopper2/).

## Document Your Components

Your users will expect documentation for your components too. You write it with the same tools we use. Run the `GH2DocsAuthoring` command in Rhino to get started. <!-- TODO(Mathias): one sentence on the authoring workflow, and where the content ends up. -->

## Icons

Grasshopper 2 icons are 3D drawings. You model them in Rhino. This may sound intimidating. It is not. The icons stay sharp at any size, and they follow the light and dark themes on their own.

The tool is the *GH2 Icon* panel in Rhino. It appears once Grasshopper 2 has been loaded, for example after running the `GH2` command. To try it:

1. Run `GH2IconSetup` to set the icon size.
1. Draw some curves. Select them. Set edges and fills in the *GH2 Icon* panel.
1. Click *Save* in the panel's preview to export a *.ghicon* file.
1. Embed the *.ghicon* file in your project. Name it after your component class, for example *MyComponent.ghicon*. Grasshopper 2 finds it on its own.

Colours have a meaning in Grasshopper 2. You do not pick an RGB value. You pick a role, such as *Input*, *Output*, or *Analysis*. Grasshopper 2 picks the actual colour for the current theme. The *GH2 Icon* panel offers these roles. The documentation explains them. <!-- TODO(Mathias): link the documentation topic on icon colours once there is one. -->

If you prefer, you can use SVG icons instead. They use the same colour roles. Write `fill="gh:Input"` instead of a fixed colour. <!-- TODO(Mathias): SVG support (SvgIcon.FromResource) is labelled "proof of concept" in the source. Decide how strongly to recommend it. -->

## Inputs Are Immutable

This is the most important difference to Grasshopper 1, and the easiest to miss.

In Grasshopper 1 you could often get away with modifying your input data in place. In Grasshopper 2 you cannot. The solver is multi-threaded. Several instances of your component may read the same data at the same time.

Treat all input data as immutable. If you need to change something, duplicate it first. When in doubt, duplicate.

***Note***: This applies to geometry too. Do not transform or edit a curve, mesh, or Brep you received as an input. Duplicate it, then work on the copy.

See [Component Processing](../migrating-components-to-gh2/#component-processing) in the migration guide for the details.

## Your Plugin's Id

Rhino identifies your plugin by the GUID of its assembly. This is the `[assembly: Guid("...")]` attribute in your project. The template generates one for you. Keep it. Never change it once you have shipped.

```cs
[assembly: Guid("88888888-4444-4444-4444-121212121212")]
```

If you ship more than one assembly:

- Assemblies that **replace** each other share the same id. For example, a build for .NET 8 and a build for another .NET version. Only one of them is ever loaded.
- Assemblies that are loaded **at the same time** need different ids.

## Rhino Commands in Your Plugin

Your assembly may also contain a Rhino plugin class and Rhino commands. Both share the assembly's id.

***Note***: If a Rhino command uses Grasshopper 2, Grasshopper 2 must be running first. It is not enough that the assembly is loaded. The `GH2` command has to have run at least once. Make sure of this in your command before you call into Grasshopper 2. <!-- TODO(Mathias): recommend one way to do this, e.g. RhinoApp.RunScript("-_GH2 _Enter", false), or a check on Grasshopper2.UI.Editor.Instance. -->

## Next Steps

Start with Your First Component ([Windows](../your-first-component-windows/), [Mac](../your-first-component-mac/)). It takes you from the project template to a running component.

Then read [Migrating Components to Grasshopper 2](../migrating-components-to-gh2/). Despite the title, it is the most complete description of the Grasshopper 2 SDK so far. It is long. You do not need to read it in one go. Keep it as a reference.

## Related Topics

- Your First Component ([Windows](../your-first-component-windows/), [Mac](../your-first-component-mac/))
- [Migrating Components to Grasshopper 2](../migrating-components-to-gh2/)
- [Grasshopper 2 documentation](https://www.rhino3d.com/docs/grasshopper2/)
- [Grasshopper developer forum](https://discourse.mcneel.com/c/grasshopper-developer)

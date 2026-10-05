+++
aliases = []
authors = [ "mathias" ]
categories = [ "Getting Started" ]
description = "Where to start as a Grasshopper 2 plugin developer: tools, documentation, icons, immutable inputs, styling, and your plugin's id."
keywords = [ "developer", "grasshopper2", "grasshopper", "gh2", "plugin", "icon", "documentation", "guid", "assembly", "immutable", "attributes", "migration" ]
languages = [ "C#" ]
sdk = [ "Grasshopper 2" ]
title = "Getting Started with Grasshopper 2 Plugins"
type = "guides"
weight = 1

[admin]
TODO = ""
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


This guide is for anyone who wants to write a Grasshopper 2 plugin, whether you have written Grasshopper 1 components or plugins before or not. There is no code in here. This guide should help you get started, and aims at filling gaps by pointing you at hard-to-find places in the rest of the documentation.

## Prerequisites

Grasshopper 2 requires Rhino 9 and the C# development tools. See Installing Tools ([Windows](/guides/grasshopper/installing-tools-windows/), [Mac](/guides/grasshopper/installing-tools-mac/)).

## Templates

There are project templates for Visual Studio, Visual Studio Code, and the command line:

- **Visual Studio**: install the [Rhino Visual Studio Extension](https://github.com/mcneel/RhinoVisualStudioExtensions/releases/latest). Look for the *Grasshopper 2 Plug-In for Rhino (C#)* template.
- **Visual Studio Code and the command line**: run `dotnet new install Rhino.Templates`, then `dotnet new gh2`.

Both templates reference the [Grasshopper2](https://www.nuget.org/packages/Grasshopper2) NuGet package. It contains the reference assemblies and the API documentation. Please note that your plugin won't load on any Rhino version prior to that NuGet package's version. To address the largest audience, we recommend targeting the 9.0 version. Choose a later version only if you are sure you need features that are not in 9.0.

## Do You Need a Plugin?

Not every developer needs to ship a plugin. Grasshopper 2 has script components for C# and Python. For a one-off tool, or to try an idea, a script component can be faster. In some cases, a Grasshopper 2 snippet might be sufficient to share your functionality.
See Grasshopper 2 Scripting ([C#](/guides/scripting/scripting-gh2-csharp/), [Python](/guides/scripting/scripting-gh2-python/)).

Write a plugin when you want to share your components, give them icons and documentation, or ship them with a Rhino plugin.

## Learn Grasshopper 2 First

Grasshopper 2 ships with plenty of documentation written for users. It is also the best place to learn the concepts the SDK is built on: the *solution*, *components*, *parameters*, *data trees*, and *preview geometry*.

To open it:

1. In Grasshopper 2, click *Help* > *Documentation...*, or press *F1*.
1. In Rhino, run the `GH2Docs` command.

The documentation is live in the sense that many pages contain live Grasshopper documents. You can drag them onto the canvas and try them out.

A read-only copy is available on the web at [rhino3d.com/docs/grasshopper2](https://www.rhino3d.com/docs/grasshopper2/).

## Open Your Grasshopper 1 Files

Grasshopper 2 opens Grasshopper 1 files, both *.gh* and *.ghx*. Try it on your own existing files. It is a quick way to see how familiar things look in Grasshopper 2. Components can be dragged from Grasshopper 1 to Grasshopper 2.

Behind this is a migration framework. Each Grasshopper 1 component is either migrated to its Grasshopper 2 counterpart, or hosted in an interop component that still runs on Grasshopper 1. If you have a Grasshopper 1 plugin, you can supply migrations for your own components. Implement `IMigrateComponent` or `IMigrateParameter` from the `Grasshopper2.Doc.Migration` namespace, or use `Gh1MigrationRule` for simple one-to-one cases. Grasshopper 2 finds these types in your plugin on its own.

## Document Your Components

Your users will expect documentation for your components too. You write it with the same tools we use. Run the `GH2DocsAuthoring` command in Rhino to get started. Documentation shipped with your plugin will get loaded automatically by Grasshopper 2 and be available to your users. While you author documentation, it is helpful to know about the *Help* > *Custom Folders...* menu to point at your working folder.

## Icons

Grasshopper 2 icons are 2D drawings, but the recommended way to design them is in Rhino, which is a 3D editor. This may sound intimidating, but it is not. The icons stay sharp at any size, and they follow the light and dark themes on their own.

The tool is the *GH2 Icon* panel in Rhino. It appears once Grasshopper 2 has been loaded, for example after running the `GH2` command. To try it:

1. Run `GH2IconSetup` to set the icon size.
1. Draw some curves. Select them. Set edges and fills in the *GH2 Icon* panel.
1. Click *Save* in the panel's preview to export a *.ghicon* file.
1. Embed the *.ghicon* file in your project. Name it after your component class, for example *MyComponent.ghicon*. Grasshopper 2 finds it on its own.

Colours have a meaning in Grasshopper 2. You do not pick an RGB value. You pick a role, such as *Input*, *Output*, or *Analysis*. Grasshopper 2 picks the actual colour for the current theme. The *GH2 Icon* panel offers these roles.
 <!-- TODO(): link the documentation topic on icon colours once there is one. -->

If you prefer, you can use SVG icons instead. They use the same colour roles. Write `fill="gh:Input"` instead of a fixed colour, for example.

## Five Rules for Component Code

Grasshopper 2 looks a lot like Grasshopper 1 from the outside. Inside, it is a different machine. Five habits from Grasshopper 1 will not carry over immediately. If you are new to Grasshopper altogether, the same five rules will save you the most time. They are easy to miss, and experience shows that many developers, including the author, miss one or more of them even repeatedly.

1. **Inputs are immutable.** Neither in Grasshopper 1 nor in Grasshopper 2 can you modify input data in place. However, doing so often had no bad consequences in Grasshopper 1. In Grasshopper 2 it can have much more dire consequences because it is inherently multi-threaded. Components solve in parallel by default, so several components may read the same data at the same time. This could lead to data corruption and hard-to-debug crashes.

   Duplicate before you modify, to prevent those. This applies to geometry too: duplicate a curve, mesh, or Brep before you transform or edit it. When in doubt, duplicate.

1. **Long loops must be cancellable.** The user can interrupt the solver at any time. Check `access.Solution.Token` for cancellation frequently, and let the exception it throws propagate, or simply return early without throwing. Doing so is very fast and won't affect your plugin's performance considerably. Any component whose solver does anything non-trivial must periodically check its cancellation token.
1. **The access level is a contract.** Each parameter is declared as `Item`, `Twig`, or `Tree`. That decides which `access.Get...` and `access.Set...` methods you call on it. The wrong one may compile and fail at run time. This is similar to how Grasshopper 1 operates, but is still easy to miss.
1. **Not every type comes from RhinoCommon.** Some types that look like RhinoCommon types are Grasshopper 2 types, for example `Angle`, `Colour`, and `Grasshopper2.Types.Shapes.Triangle`. Check the namespace before you reach for the Rhino version.
1. **Look it up before you write it.** The `Grasshopper2` NuGet package ships the full XML documentation. Your IDE shows it as you type. The API is new. Guessing a name from Grasshopper 1 is the most common cause of code that does not compile.

See [Component Processing](../migrating-components-to-gh2/#component-processing) in the migration guide for the details on threading and cancellation.

## Meta Data

Every value in Grasshopper 2 can carry meta data, such as a colour or a layer name. You will read about this in the documentation and in the migration guide. You do not need to understand it before you write your first component. In simple components, Grasshopper 2 passes meta data from inputs to outputs for you. Learn about it when you need it.

## Styling Your Components

Grasshopper 2 lets you change how your component looks and behaves on the canvas. The entry point is the `IAttributes` interface. Every document object has one. It handles layout, drawing, and mouse interaction, like `GH_ComponentAttributes` did in Grasshopper 1.

To customise a component, override `CreateAttributes()` in your component class and return your own subclass of `Grasshopper2.Doc.Attributes.ComponentAttributes`. Then override the drawing methods you need, such as `DrawBackground`, `DrawContent`, or `DrawOutputs`. Colours come from the `Skin` passed to every drawing method. Do not hard-code them.

Start reading in the API documentation at `Grasshopper2.Doc.IAttributes` and `Grasshopper2.Doc.Attributes.ComponentAttributes`.

***Note***: All custom drawing uses Eto, not WinForms or GDI+. It must work on both Windows and Mac.

## Your Plugin's Id

Rhino identifies your plugin by the GUID of its assembly. This is the `[assembly: Guid("...")]` attribute in your project. The template generates one for you. Keep it. Never change it once you have shipped.

```cs
[assembly: Guid("88888888-4444-4444-4444-121212121212")]
```

If you ship more than one assembly:

- Assemblies that **replace** each other share the same id. For example, a build for .NET 8 and a build for another .NET version. Only one of them is ever loaded.
- Assemblies that are loaded **at the same time** need different ids.

## Rhino Commands in Your Plugin

Your assembly may also contain a Rhino plugin class and Rhino commands. A Rhino plugin class is one that derives from `Rhino.PlugIns.PlugIn`. Both share the assembly's id.

***Note***: If such a Rhino command uses Grasshopper 2, Grasshopper 2 must be running first. It is not enough that the assembly is loaded. The `GH2` command has to have run at least once. Make sure of this in your command before you call into Grasshopper 2. <!-- TODO): recommend one way to do this, e.g. RhinoApp.RunScript("-_GH2 _Enter", false)?? -->

## Native Code

You can call C or C++ code from your plugin. See [Wrapping Native Libraries](/guides/rhinocommon/wrapping-native-libraries/) and the [Moose sample](https://github.com/dalefugier/Moose) on GitHub. Moose shares one C++ library between a Rhino C++ plugin, a RhinoCommon plugin, and a Grasshopper component.

***Note***: Compile your native code against the [Rhino C/C++ SDK](/guides/cpp/what-is-the-cpp-sdk/), not against the public openNURBS toolkit. The two are not binary compatible. A library built on public openNURBS cannot exchange geometry with Rhino in memory.

## Testing Your Plugin

The templates set up debugging for you. Press *F5* and Rhino starts with your plugin.

To load a build by hand, open Grasshopper 2 and click *Grasshopper* > *Plugins...*. Click *Install...* and pick your *.rhp* file. Grasshopper 2 remembers it and loads it again next time.

## Publishing Your Plugin

Publish your plugin with the [Package Manager](/guides/yak/). The `yak build` command recognises Grasshopper 2 plugins. The Yak guides were written for Rhino and Grasshopper 1 plugins, but the steps are the same. <!-- TODO: none of the Yak guides mentions Grasshopper 2. Worth a separate issue. -->

## Working With an AI Assistant

Many developers write Grasshopper 2 code with an AI assistant. These models were trained on Grasshopper 1 code. Left alone, they will write Grasshopper 1 code with new names, and it will not compile or not behave.

The [five rules](#five-rules-for-component-code) above apply to your assistant as much as to you. Put them in a short instruction file in your project, and point the assistant to this page and to the migration guide. <!-- TODO: consider publishing a ready-made instruction file developers can copy. -->

## Next Steps

Start with Your First Component ([Windows](../your-first-component-windows/), [Mac](../your-first-component-mac/)). It takes you from the project template to a running component.

Then read [Migrating Components to Grasshopper 2](../migrating-components-to-gh2/). Despite the title, it is the most complete description of the Grasshopper 2 SDK so far. It is long. You do not need to read it in one go. Keep it as a reference.

## Related Topics

- Your First Component ([Windows](../your-first-component-windows/), [Mac](../your-first-component-mac/))
- [Migrating Components to Grasshopper 2](../migrating-components-to-gh2/)
- Grasshopper 2 Scripting ([C#](/guides/scripting/scripting-gh2-csharp/), [Python](/guides/scripting/scripting-gh2-python/))
- [Grasshopper 2 documentation](https://www.rhino3d.com/docs/grasshopper2/)
- [Wrapping Native Libraries](/guides/rhinocommon/wrapping-native-libraries/)
- [Package Manager guides](/guides/yak/)
- [Grasshopper developer forum](https://discourse.mcneel.com/c/grasshopper-developer)

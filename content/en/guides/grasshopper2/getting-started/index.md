+++
aliases = []
authors = [ "mathias" ]
categories = [ "Getting Started" ]
description = "What every Grasshopper 2 plugin developer should know before writing the first line: plugin identity, assembly ids, and how Rhino and Grasshopper 2 find your plugin."
keywords = [ "developer", "grasshopper2", "grasshopper", "gh2", "plugin", "guid", "assembly", "id" ]
languages = [ "C#" ]
sdk = [ "Grasshopper 2" ]
title = "Getting Started with Grasshopper 2 Plugins"
type = "guides"
weight = 1

[admin]
TODO = "WWW-3714: skeleton, rephrase all TODO(Mathias) blocks"
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

<!-- TODO(Mathias): rephrase. Who this page is for: everyone writing a GH2 plugin, whether new or
coming from GH1 (-> migration guide) or from an early Rhino 9 WIP build. Short, two or three sentences. -->

This page collects a few facts about plugin identity and loading that are easy to miss.
Whether you start from the [project templates](../your-first-component-windows/), port a GH1 plugin
([migration guide](../migrating-components-to-gh2/)), or update a plugin written against an early
Rhino 9 WIP, read these before you ship.

## Plugin identity

{{< nugget name="assembly-id" >}}{{< /nugget >}}
{{< call-out type="info" title="Your plugin's id is the assembly GUID" open=false >}}
<!-- TODO(Mathias): rephrase -->
- There is exactly **one id per assembly**: the .NET `[assembly: Guid("...")]` attribute.
- Rhino and Grasshopper 2 both read that attribute and nothing else.
  Neither the Rhino `PlugIn` class nor the Grasshopper 2 `Plugin` class can override it.
- Grasshopper 2 refuses to load a plugin without it:
  *"plugin does not declare an id; add an [assembly: Guid] attribute to the plugin project."*
- The project templates generate a fresh GUID for every new project. Keep it.
- **Never change it after release.** Rhino and Grasshopper 2 remember your plugin by this id:
  - plugin settings and load protection
  - toolbars and panels
  - licensing
  - data your plugin writes into `.3dm` files, and the Package Manager's "install the missing plug-in" prompt
  - package lookup on the package server
  - the list of required plugins stored in every `.ghz` file

  A new id makes your plugin a different plugin: settings are lost and old documents report it as missing.

```cs
// Properties/AssemblyInfo.cs
[assembly: Guid("88888888-4444-4444-4444-121212121212")] // generate your own, once
```
{{< /call-out >}}
{{< nugget name="assembly-id-end" >}}{{< /nugget >}}

See the [Plugin Assembly](../migrating-components-to-gh2/#plugin-assembly) section of the migration
guide for the attributes that supply your plugin's name, author, version and so on.

## One .rhp, one or two roles

{{< call-out type="note" title="Rhino plugin class, Grasshopper 2 plugin class, or both" open=false >}}
<!-- TODO(Mathias): rephrase -->
- A Grasshopper 2 plugin is a `.rhp` file (not a `.gha`).
- It needs one public, non-abstract class deriving from `Grasshopper2.Framework.Plugin`, with a
  public **parameterless** constructor. Without it, Grasshopper 2 won't load components from the assembly.
- The Rhino `Rhino.PlugIns.PlugIn` class is **optional**. Add it if you also need Rhino commands,
  panels, or Rhino plugin events. Without it, Rhino recognises the file as a "Grasshopper-only" `.rhp`
  and leaves it to Grasshopper 2.
- Either way it is one assembly with one id (see above). A `.rhp` containing both classes is a
  Rhino plugin and a Grasshopper 2 plugin under the same id.
<!-- TODO(Mathias): mention the template contains both classes; delete the Rhino one if unused? -->
{{< /call-out >}}

## Shipping several assemblies

{{< call-out type="note" title="When to share an id and when not to" open=false >}}
<!-- TODO(Mathias): rephrase -->
- **Same function, same id.** Builds of one plugin for different targets (`net48` / `net8.0`,
  `-windows` / `-macos`) must carry the **same** GUID. Only one of them is ever loaded; Rhino and
  Grasshopper 2 pick the build matching the running runtime.
- **Different function, different id.** Assemblies that are meant to be loaded at the same time
  (e.g. a component library and a separate UI library) need **different** GUIDs.
- What users see when two different files claim the same id:
  - Grasshopper 2 loads only one and shows a dialog. If the names differ, the dialog says this
    "points to a mistake by one of the plugin developers".
  - Rhino (Windows): *"Unable to load … plug-in: ID already in use."* The first one loaded wins.
<!-- TODO(Mathias): keep or drop the macOS detail (no error, last loaded wins)? -->
{{< /call-out >}}

## Coming from an early Rhino 9 WIP

{{< call-out type="warning" title="The Plugin constructor no longer takes an id" open=false >}}
<!-- TODO(Mathias): rephrase -->
- Until the end of July 2026 the Grasshopper 2 `Plugin` base constructor took an id, a `Nomen` and a
  version. That constructor has been removed. Identity now comes only from assembly attributes.
- Plugins compiled against the old `Grasshopper2.dll` no longer load. Recompile.
- **Trap:** your project probably already has an `[assembly: Guid]` generated by Visual Studio,
  and it is *not* the GUID you used to pass to the constructor. If you just delete the constructor
  argument, your plugin's id silently changes and existing `.ghz` files will report it as missing.
  Copy the GUID you used to pass to the constructor into `[assembly: Guid]`.

```cs
// before
public MyPluginInfo() : base(new Guid("aaaaaaaa-..."), new Nomen("My Plugin", "..."), new Version(1, 0)) { }

// after: constructor has no arguments, and in AssemblyInfo.cs:
[assembly: Guid("aaaaaaaa-...")] // the GUID you used to pass to the constructor
```
{{< /call-out >}}

## Ids that are not the plugin id

{{< call-out type="note" title="Don't mix these up" open=false >}}
<!-- TODO(Mathias): rephrase -->
- `[IoId("...")]` on components, parameters and other storable types identifies a *type*, not the
  plugin. Each needs its own GUID, and it too must never change.
- A GH1 `.gha` is identified by `GH_AssemblyInfo.Id`, not by its assembly GUID. If you ship GH1 and
  GH2 versions side by side, they are separate plugins.
<!-- TODO(Mathias): recommend same or different id for the GH2 port of a GH1 plugin? -->
{{< /call-out >}}

## Work in progress

{{< call-out type="warning" title="Not everything is in place yet" open=false >}}
<!-- TODO(Mathias): rephrase; keep as statements of intent, no dates -->
- The rule above is the contract: **Rhino will refer to your assembly by its GUID, Rhino-wide**,
  whether or not it contains a Rhino plugin class.
- Rhino does not yet keep a registry of Grasshopper-only assemblies, or deduplicate them across
  Rhino and Grasshopper. Following the id rules now means your plugin will be ready for that.
- The Package Manager does not yet show whether a package contains a Rhino plugin, a Grasshopper 1
  plugin, a Grasshopper 2 plugin, or several of these.
{{< /call-out >}}

## Next steps

- Your First Component ([Windows](../your-first-component-windows/), [Mac](../your-first-component-mac/))
- [Migrating Components to Grasshopper 2](../migrating-components-to-gh2/)
- [Developer discussions on Discourse](https://discourse.mcneel.com/c/grasshopper-developer)

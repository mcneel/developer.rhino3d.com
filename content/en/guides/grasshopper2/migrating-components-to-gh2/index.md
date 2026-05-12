+++
aliases = []
authors = [ "" ]
categories = [ "Getting Started" ]
description = "A brief description of this feature"
keywords = [ "developer", "another_keyword"]
languages = [ "C#" ]
sdk = [ "Grasshopper 2" ]
title = "Migrating Components to Grasshopper 2"
type = "guides"
weight = 10

[admin]
TODO = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 9

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true
+++

By the end of this document, you should have a sufficient grip on what it takes to port components from a Grasshopper 1.0 GHA plugin to a Grasshopper 2.0 RHP plugin. It will discuss the major and minor differences in both the over-arching architecture and specific namespace and type names.

## Prerequisites

This document presumes you have experience with developing components for Grasshopper 1.0 in C#.

## Introduction

From a bird's eye view, component development in GH1 and GH2 are two almost identical processes. On both platforms one must create a distinct class per component, assign it a unique ID, give it a name and description, a tab and panel location, specify the input and output parameters and finally implement the function which computes the outputs from the inputs. However, the specifics differ to lesser and greated degrees, occasionally in unexpected ways.

Here's a list of conceptually significant differences in no particular order:
- Many types in Grasshopper 2 are immutable, which often necessitates a different way of doing things.
- Component IDs are type attributes rather than class properties.
- The solver is inherently multi-threaded, which makes it much harder to store values or states in class-level variables.
- The solver is inherently cancellable.
- New native data types such as `Functions`, `Fields`, `Gradients`, `BigIntegers`, and `Angles` often require a rethinking of how components can/should work.
- Type functionality is provided via Assistants rather than an `IGH_Goo` interface.
- The existence of meta data complicates operations which shuffle or restructure lists of values.
- Vector based icons are now supported and recommended.
- Documentation content is created using authoring tools provided by Grasshopper 2.

## Plugin Assembly Layout

For a .NET assembly to be considered a valid Grasshopper Plugin it should use the `.RHP` extension and it must contain a public class with an empty constructor which inherits from the `Grasshopper2.Framework.Plugin` type:

```cs
public sealed class MyPluginInfo : Plugin
{
  public MyPluginInfo()
    : base(new Guid("88888888-4444-4444-4444-121212121212"),
           new Nomen("My Plugin Name", "Components for ... something or other."),
           new Version(2, 0, 0, 0))
  {
    Icon = AbstractIcon.FromResource("PluginIcon", typeof(MyPluginInfo));
  }

  public override IIcon Icon { get; }
  public override string Author => "Your Name Here.";
  public override sealed string Copyright => $"Copyright © 2026 Your Name";
  public override sealed string Website => "http://www.yourwebsite.com/";
  public override sealed string Contact => "website, email, ...";
  public override sealed string LicenceDescription => "MIT";
  public override sealed string LicenceAgreement => "https://opensource.org/license/mit";
}
```

Without this, Grasshopper will not attempt to load your plugin.
The `Nomen` type bundles together relevant values for describing and positioning objects within the Grasshopper 2 user interface. It is used everywhere when objects need a name, a descriptive info text, and tab and panel locations.

## Component Class Layout

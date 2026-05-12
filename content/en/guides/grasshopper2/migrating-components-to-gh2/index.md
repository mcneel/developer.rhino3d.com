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

## Plugin Assembly

For a .NET assembly to be considered a valid Grasshopper Plugin it should use the `.RHP` extension and it must contain a public class with an empty constructor which inherits from the `Grasshopper2.Framework.Plugin` type, which is the equivalent of the `GH_AssemblyInfo` type in GH1:

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

The `Nomen` type bundles together relevant values for describing and positioning objects within the Grasshopper user interface. It is used everywhere when objects need a name, a descriptive info text, and tab+panel locations.

### Loading Plugins

[[[Package Manager, G2PluginViewer.]]]


## Component Class

The basic layout for a component class in GH2 closesly tracks with what you're probably used to, with just a few minor administrative changes. As mentioned above, the component identifier is not a property of the class, but rather an attribute of the `IoIdAttribute` type, provided by the `GrasshopperIO.dll` assembly. The `Nomen` provided in the constructor provides not just the name, info, tab and panel data, but also the `Slot` (placing the component in a specific slot within the panel) and the `Rank` (specifying the importance of the component, affecting sort order within the UI).

Due to the nature of the (de)serialisation api in GH2, a second constructor is required which takes a single `IReader` argument and calls the base class constructor. This is an unfortunate complication caused by the fact that the GH2 deserialisation logic must work for immutable types. C# OOP rules do not allow for such a constraint, so you're just going to have to remember that this is important.

```cs
[IoId("88888888-4444-4444-4444-121212121212")]
public sealed class Component2 : Component
{
  public Component2() : base(new Nomen("Component 2", "An example component.", "Tab", "Panel", 0, Rank.Normal)) { }
  public Component2(IReader reader) : base(reader) { }

  protected override void AddInputs(InputAdder inputs) { }
  protected override void AddOutputs(OutputAdder outputs) { }
  protected override void Process(IDataAccess access) { }
}
```

For comparison's sake, below is an equivalent example component class as it would be written in GH1. Note that the three properties at the bottom have all disappeared in the GH2 code. The `Exposure` property is now part of the `Nomen` type, the `ComponentGuid` has morphed into an attribute, and the `Icon` property can be omitted altogether, provided that an icon file with the same name as the component class is available as an embedded resource in the plugin assembly.

```cs
public class Component1 : GH_Component
{
  public Component1() : base("Component 1", "Cp1", "An example component.", "Tab", "Panel") { }

  protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager) { }
  protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager) { }
  protected override void SolveInstance(IGH_DataAccess DA) { }

  public override GH_Exposure Exposure
  {
    get { return GH_Exposure.primary; }
  }
  public override Guid ComponentGuid
  {
    get { return new System.Guid("{88888888-4444-4444-4444-121212121212}"); }
  }
  protected override System.Drawing.Bitmap Icon
  {
    get { return ThisAssembly.Properties.Resources.Icon_Component1; }
  }
}
```

### Component Parameters

[[[new types in GH2, settings, default values.]]]

```cs
protected override void AddInputs(InputAdder inputs)
{
  inputs.AddPlane("Plane", "Pl", "Plane for circle centre and orientation.").Set(Plane.WorldXY);
  inputs.AddField("Radius", "Rd", "Radius for circle.").Set(1.0);
}
protected override void AddOutputs(OutputAdder outputs)
{
  outputs.AddCircle("Circle", "Cr", "Circle defined by the plane and radius.");
}
```

[[[Access, Requirement]]]
[[[Enums as type, UiName, UiInfo, UiTint]]]


### Component Processing

[[[Multithreading, access.Solution, access.Solution.Token, temporary data.]]]

### Variable Parameter Layouts

[[[No interface, CanCreateInput, DoCreateInput, VariableParameterMaintenance, ...]]]

### Modular Components

[[[Mention, but don't elaborate.]]]


## Data Types

### Structured Storage

[[[Tree, Twig, Path, Pear]]]

### Garden

[[[One-stop-shop for creating trees and twigs.]]]

### Meta Data

[[[Design, immutability, StandardNames, transformable entries.]]]

### Type Assistants

[[[TypeAssistantServer, ITypeAssistant, ZupportsXXXXX properties.]]]

### Curve and Surface Assistants

[[[Basic ideology, CurveBroker, SurfaceBroker]]]

### Type Conversion

[[[ConversionServer, ConversionRepository, Inspecting conversions in the UI.]]]
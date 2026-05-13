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

Adding inputs and outputs to a component is, again, conceptually very similar in GH1 and GH2. Two methods need to be overridden, and the provided parameter manager is used to add new parameters in the order in which they appear on the component from top to bottom. Consider the following code snippet which was taken from the GH1 `Circle` component:

```cs
protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
{
  pManager.AddPlaneParameter("Plane", "P", "Base plane of circle", GH_ParamAccess.item, Plane.WorldXY);
  pManager.AddNumberParameter("Radius", "R", "Radius of circle", GH_ParamAccess.item, 1.0);
}
protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
{
  pManager.AddCircleParameter("Circle", "C", "Resulting circle", GH_ParamAccess.item);
}
```

Apart from some name changes, the equivalent code in the GH2 `Circle Radius` component is nearly identical:

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

The minor differences worth noting include:
- The `Item` access is implied and need not be specified in GH2. Only inputs and outputs which operate on twigs or trees need to have their `Access` property set.
- Default values are no longer part of the `AddX()` methods, but are instead assigned using the `Set(...)` method on the returned parameter. It is recommended that all non-optional inputs have default values assigned, so that a component works "out of the box" when dragged onto the canvas.
- Inputs and outputs in GH2 ought to have two-letter user names instead of single letter names. This provides a much richer layer of information to the user.
- The optionality of inputs is slightly more advanced in GH2. Instead of a single boolean value marking an input as `Optional`, GH2 provides a three state enumeration. Inputs by default have `Requirement.MustExist`, but have two different optional states called `Requirement.MayBeNull` and `Requirement.MayBeMissing`. The component `Process()` function will not run if the input values are not compliant with the set requirement.

Major differences worth noting include:
- GH2 provides a larger set of native types and parameters, which should be used whenever they make sense. More on this below.
- GH2 provides some additional options on some parameters (such as Indexing on Integer parameters, or Type Filters on Numeric parameters) which ought to be set accordingly.
- GH2 parameters all have a `Preset` system, although this is used almost exclusively on Integer parameters to represents enumerations.

The table below lists some new parameter types and when to use them.

| Types | Usage |
|----:|:----|
| `Field` | Fields (although technically not new) replace number or vector inputs when the component operates on an unambiguous location in space. Using the example code above, the circle radius input is no longer a number in GH2, but a field, since the circle centre point provides a clear location for the sampling of the field. |
| `Angle` | The angle type replaces `Number` whenever that number was used to represent an angle. Angles can be represented in Degrees, Radians, Turns, Grades and Spreads, allowing the user to specify them in whatever unit makes the most sense to them.  |
| `Numeric` | The Numeric parameter supports all native number types in GH2, including `System.Double`, `System.Int32`, `System.Numerics.BigInteger`, `System.Numerics.Complex` and `Grasshopper2.Types.Numeric.Angle`. Exactly which of these is allowed in any specific numeric parameter depends on the filter set by the developer. |
| `Function` | Functions sometimes replace numbers if the context allows for that. |
| `Gradient` | Gradients sometimes replace colours if the context allows for that. |
| `Random` | The `Random` parameter replaces an integer seed input. GH2 supports a variety of random engines, and the `RandomEngine` type combines the choice of engine plus seed value into one. |

The use of enumerations as inputs is fairly common in GH2 and has been implemented via the `Integer` parameter along with presets. The `inputs.AddEnum(...)` method provides a shorthand for adding an integer parameter with registered presets. For an `Enum` to be used in this way it must derive from the `System.Int32` type, and ideally it provides detailed descriptions and a unique colour for each value. Below is the partial code for the `DistanceMetric` enumeration, which for each item provides a `UiInfo()` and `UiTint()` attribute, and for some items even a `UiName()` attribute to override the name as shown in the GH2 UI.

```cs
public enum DistanceMetric
{
  [UiInfo("Linear distance measured along the geodesic."), UiTint("Green 8")]
  Euclidean,
  [UiInfo("Square of the Euclidean distance."), UiTint("Green 7")]
  Quadrance,
  [UiInfo("Sum of absolute differences per dimension, also called the 'L1-norm'."), UiTint("Green 6")]
  Manhattan,
  [UiInfo("Weighted version of Manhattan distance."), UiTint("Green 5")]
  Canberra,
  [UiInfo("One minus the Pearson correlation coefficient."), UiTint("Pink 8")]
  Pearson,
  [UiName("MAE"), UiInfo("Normalised Manhattan distance. I.e. Manhattan distance divided by the dimensionality."), UiTint("Blue 8")]
  MeanAbsoluteError
}
```

When properly set up this way, presets can be chosen using the `Preset Picker` object:

{{< image url="/images/EnumAsPresetInGH2.png" alt="/images/EnumAsPresetInGH2.png" class="image_center" width="75%" >}}


### Component Processing

The key difference to bear in mind when writing processing code for GH2 components is that every component iteration by default runs on multiple threads. Because of this, the code inside the `Process(IDataAccess access)` method must be thread-safe. If this is impossible, the threading state of the component must be downgraded from the default `ThreadingState.MultiThreaded` to `ThreadingState.SingleThreaded` via the `Component.Threading` property.

Furthermore, if the processing code is liable to take longer than a few milliseconds, the component should pay attention to cancellation requests by occasionally calling `access.Solution.Token.ThrowIfCancellationRequested()`.




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
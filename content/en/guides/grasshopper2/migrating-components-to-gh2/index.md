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

{{< image url="/images/EnumPresetsGH2Migration.png" alt="How UiName, UiInfo, and UiTint manifest in the GH2 interface." class="image_center" width="80%" >}}


### Component Processing

The key difference to bear in mind when writing processing code for GH2 components is that every component iteration by default runs on multiple threads. Because of this, the code inside the `Process(IDataAccess access)` method must be thread-safe. If this is impossible, the threading state of the component must be downgraded from the default `ThreadingState.MultiThreaded` to `ThreadingState.SingleThreaded` via the `Component.Threading` property.

Furthermore, if the processing code is liable to take longer than a few milliseconds, the component should pay attention to cancellation requests by occasionally calling `access.Solution.Token.ThrowIfCancellationRequested()`.

[[[GetItem, GetPear, GetTwig, GetITwig, GetITree, GetTree]]]
[[[Rectify vs. Verify]]]
[[[access.AddWarning, access.AddError]]]

#### A Random Walk Example

Let's start with a relatively simple example of a component which doesn't operate on lists or trees, and doesn't need to deal with meta data. This example will introduce getting and setting individual values, dealing with fields and random engines, and how to implement cancellation. The component contains three inputs; a `Sphere`, a `Field` and a `RandomEngine`, and outputs a single `Polyline` representing a random walk from the centre of the sphere to the boundary. First, the code:

```cs
protected override void Process(IDataAccess access)
{
  // 1. Retrieve values from inputs.
  access.GetItem(0, out Sphere sphere);
  access.GetItem(1, out Field stepField);
  access.GetItem(2, out RandomEngine engine);
  
  // 2. Start the computation.
  var point = sphere.Center;
  var track = new Polyline { point };
  var random = engine.CreateInstance();
  while (true)
  {
    // 3. Abort the computation when the solution is cancelled.
    access.Solution.Token.ThrowIfCancellationRequested();
    
    var step = Math.Max(1e-8, stepField.ScalarAt(point));
    point += step * random.NextUnitVector3D();
    track.Add(point);
    if (point.DistanceTo(sphere.Center) >= sphere.Radius)
      break;
  }
  
  // 4. Assign results to outputs.
  access.SetItem(0, track);
}
```

1. Getting values in GH2 components uses the `out` rather than the `ref` keyword, so is somewhat more economical. Null checks aren't required if the input `Requirement` is set to `MustExist`. Validity checks may be necessary, but we'll focus on those in a later example. 
2. This component operates with a pseudo-random aspect, which means it requires a `RandomEngine` as an input. The `CreateInstance()` is used on an engine value to create a new random number generator of the correct type with the specified seed. Also note that GH2 provides a lot of useful extension methods via the `Grasshopper2.Extensions` namespace, so when that is added to the `using` block of your C# file you'll get access to methods like `Random.NextUnitVector3D()`.
3. Since the `while` loop in this component can potentially run for a *very* long time, it is important that cancellation is checked often. the `Solution` object passed to the component via the `IDataAccess` argument has a token which can be used for this. In GH2, very time a new solution starts in the same document, any currently running solution is automatically cancelled.
4. Assignment of output values works exactly the same in GH2 as in GH1, at least when metadata or twigs or trees are not involved.

{{< image url="/images/RandomWalkGH2Migration.png" alt="The RandomWalk component running with 100 different random seeds." class="image_center" width="90%" >}}


#### Working with Twigs and Curves

Grasshopper 2 takes a different approach to curve values. There are still dedicated parameters for specific curve types such as `Line`, `Circle`, `Arc`, `Rectangle`, etc., but the `Curve` parameter does *not* convert all curve-like values into `Rhino.Geometry.Curve` compliant types. Instead, the `Curve` parameter stores all curve values as-is, and only makes sure that each value is associated with a centrally registered `CurveAssistant`. This new approach has two benefits. First, it allows values to be stored without converting them to a different type. Second, it allows plug-ins to add their own curve-like types and trust that all existing components that operate on curves will be able to handle these new values. The drawback to this approach is that dealing with curves can be significantly more complicated for component developers, depending on what curve operations a component needs to perform.

In the following example, we'll create a component which sorts curves based on whether their end-points are both within a box, both outside of that box, or one-within-and-one-without. This example will discuss how to deal with twigs, curve assistants, and how to correctly persist meta data from input curves to output curves. The default meta-data-copying-mechanism in components will fail if the order of input and output values is not consistent.

This component must operate on entire twigs instead of individual values. If each curve was treated individually, a `null` value would be automatically inserted into the two outputs where the curve did not end up. If this is desired behaviour, then by all means operate on single values, but in this case we want the outputs to contain no nulls.

As such, the first input and all three outputs need to be marked with `Access.Twig` when adding these parameters:

```cs
protected override void AddInputs(InputAdder inputs)
{
  inputs.AddCurve("Curves", "Cr", "Curves to sort.", Access.Twig);
  inputs.AddBox("Box", "Bx", "Box volume used for sorting.");
}
protected override void AddOutputs(OutputAdder outputs)
{
  outputs.AddCurve("Inside", "In", "Curves whose end-points fall within the box.", Access.Twig);
  outputs.AddCurve("Crossing", "Cx", "Curves whose end-points fall on both sides of the box.", Access.Twig);
  outputs.AddCurve("Outside", "Ot", "Curves whose end-points fall outside the box.", Access.Twig);
}
```

"Twigs" in GH2 are equivalent to "Branches" in GH1. The word "branch" wasn't only topologically slightly incorrect, it also did not consist of four letters. GH2 uses exclusively 4-letter words to refer to the various types involved in data trees; [tree, twig, item, path, pear, site, rule, null, meta].

The `Process()` method for this component has to take care to correctly deal with null items in the twig, and to maintain the pairing of items with their original meta data. First consider the implementation, then we'll discuss the details:

```cs
protected override void Process(IDataAccess access)
{
  // 1. Retrieve values from inputs.
  access.GetITwig(0, out var curves);
  access.GetItem(1, out Box box);
  
  // 2. Collections for aggregating pears.
  var inside = new List<IPear>();
  var crossing = new List<IPear>();
  var outside = new List<IPear>();
 
  // 3. Iterate over all pears in the twig.
  foreach (var pear in curves.NonNullPears)
  {
    // 4. Cancellation support.
    access.Solution.Token.ThrowIfCancellationRequested();
  
    // 5. Find the curve assistant associated with the current value.
    var assistant = TypeAssistantServer.FindCurveAssistantByType(pear.Type);
    assistant.GetEndPoints(pear.Item, out var p0, out var p1);
 
    var i0 = box.Contains(p0);
    var i1 = box.Contains(p1);
 
    // 6. Copy the pears into the appropriate list.
    if (i0 != i1)
      crossing.Add(pear);
    else if (i0)
      inside.Add(pear);
    else
      outside.Add(pear);
  }

  // 7. Create new twigs from the pear collections.
  access.SetTwig(0, Garden.ITwigFromPears(inside));
  access.SetTwig(1, Garden.ITwigFromPears(crossing));
  access.SetTwig(2, Garden.ITwigFromPears(outside));
}
```

1. When the type constraint of an input is known, for example when the input is an Integer Parameter, then the generic `access.GetTwig<int>(0, out var integers)` method can be used. However in the case of curves it cannot be known ahead of time what the type constraint of the twig in question may be. If the input contains only `Circle` values, then it will be a `Twig<Circle>`, but a curve parameter may contain a mixture of different types, so we ought to revert to the non-generic `ITwig` approach.
2. Similarly, since we can't know the type constraints ahead of time, it is not possible to use `Pear<T>` as a list constraint and we must fall back to the non-generic `IPear`. A pear is nothing more than the pairing of a value along with its meta data. It is called a "pear" rather than a "pair" because "pair" was already taken and "pear" fits nicely within the tree-paradigm. All data tree types in GH2 are immutable, which means we cannot build a twig or tree over time. Instead, we must aggregate the contents in mutable collection types which are then converted into the appropriate twig/tree all at once.
3. There are several ways to iterate over the contents of a twig, but if the indices of values are not required, there are several handy enumerators which allow `foreach` to do all the heavy lifting.
4. The only reason this component needs cancellation support is because the twigs it operates on may contain thousands if not millions of values.
5. We need to find the curve assistant for each curve-like value in the twig. The `TypeAssistantServer` is a static class which maintains all registered assistants and provides easy lookup based on values or types. The curve assistant allows us to query the start and end-points of the curve value, even if we don't know the type of that value. It could be a `Rhino.Geometry.Line`, or a `Rhino.Geometry.NurbsCurve`, or even a curve type which is shipped as part of a 3rd party plugin years after the code for this component was written.
6. This part seems self-explanatory.
7. Once all pear lists have been made they can be converted into twigs and assigned to each output.

{{< image url="/images/CurveSortingGH2Migration.png" alt="Curve end-point sorting in action." class="image_center" width="90%" >}}

### Custom Properties

[[[Use CustomValues to store your simple properties since IO is taken care of.]]]
[[[Overriding Store() and new(IReader) is possible, but discouraged.]]]


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
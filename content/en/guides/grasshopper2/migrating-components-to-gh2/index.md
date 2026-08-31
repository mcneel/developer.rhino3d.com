+++
aliases = []
authors = [ "David Rutten" ]
categories = [ "Getting Started" ]
description = "Information germain to Grasshopper component developers who want to migrate from GH1 to GH2."
keywords = [ "developer", "grasshopper", "component", "migration", "migrate", "upgrade"]
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

# Plugin Assembly

For a .NET assembly to be considered a valid Grasshopper Plugin it should use the `.RHP` extension and it must contain a public class with an empty constructor which inherits from the `Grasshopper2.Framework.Plugin` type, which is the equivalent of the `GH_AssemblyInfo` type in GH1.

Unlike `GH_AssemblyInfo` however, plugin identity and authorship are no longer specified in code. Instead they are read from assembly attributes, so that a single `*.rhp` file can act as both a Rhino plugin and a Grasshopper plugin using a single set of metadata. The table below lists which attribute feeds which plugin property:

| Property | Assembly attribute | Notes |
|----:|:----|:----|
| `Id` | `[assembly: Guid]` | The same id Rhino uses to identify the plugin. |
| `Name` | `[assembly: AssemblyTitle]` | The `<AssemblyTitle>` project property. Falls back to the file name. |
| `Info` | `[assembly: AssemblyDescription]` | The `<Description>` project property. |
| `Version` | `[assembly: AssemblyFileVersion]` | The `<FileVersion>` project property. The same version Rhino reports for the plugin. |
| `Author` | `[assembly: PlugInDescription(DescriptionType.Organization, ...)]` | Falls back to the `AssemblyCompany` attribute. |
| `Contact` | `[assembly: PlugInDescription(DescriptionType.Email, ...)]` | |
| `Website` | `[assembly: PlugInDescription(DescriptionType.WebSite, ...)]` | |
| `Copyright` | `[assembly: AssemblyCopyright]` | The `<Copyright>` project property. A `{now}` placeholder in the text is expanded to the current year when the plugin loads. |

In an SDK-style project the standard .NET attributes are generated from properties in the `*.csproj` file, while the `Guid` and the Rhino `PlugInDescription` attributes are typed directly into a source file:

```cs
using System.Runtime.InteropServices;
using Rhino.PlugIns;

[assembly: Guid("88888888-4444-4444-4444-121212121212")]
[assembly: PlugInDescription(DescriptionType.Organization, "Your Name Here")]
[assembly: PlugInDescription(DescriptionType.Email, "you@yourwebsite.com")]
[assembly: PlugInDescription(DescriptionType.WebSite, "http://www.yourwebsite.com/")]
```

That leaves very little for the plugin class itself to do. The icon and licence details are the only pieces of information which still have to be supplied from code:

```cs
public sealed class MyPluginInfo : Plugin
{
  public MyPluginInfo()
  {
    Icon = AbstractIcon.FromResource("PluginIcon", typeof(MyPluginInfo));
  }

  public override IIcon Icon { get; }
  public override string LicenceDescription => "MIT";
  public override string LicenceAgreement => "https://opensource.org/license/mit";
}
```

All the properties in the table remain virtual, so whenever a value has to be computed at runtime rather than baked into the assembly metadata, simply override the property in question and the corresponding attribute will be ignored.

## Loading Plugins

[[[Package Manager, G2PluginViewer.]]]


# Components

The basic layout for a component class in GH2 closesly tracks with what you're probably used to, with just a few minor administrative changes. As mentioned above, the component identifier is not a property of the class, but rather an attribute of the `IoIdAttribute` type, provided by the `GrasshopperIO.dll` assembly. The `Nomen` type bundles together the values which describe and position an object within the Grasshopper user interface; it is used everywhere objects need a name, a descriptive info text, and tab+panel locations. The `Nomen` provided in the constructor provides not just the name, info, tab and panel data, but also the `Slot` (placing the component in a specific slot within the panel) and the `Rank` (specifying the importance of the component, affecting sort order within the UI).

Due to the nature of the (de)serialisation api in GH2, a second constructor is required which takes a single `IReader` argument and calls the base class constructor. This is an unfortunate complication caused by the fact that the GH2 deserialisation logic must work for immutable types, requiring deserialisation to be implemented via constructors.

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

## Component Parameters

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
- The optionality of inputs is slightly more advanced in GH2. Instead of a single boolean value marking an input as `Optional`, GH2 provides a three state enumeration. Inputs by default have `Requirement.MustExist`, but have two different optional states called `Requirement.MayBeNull` and `Requirement.MayBeMissing`. The component `Process()` function will not run if the input values are not compliant with the set requirements.

Major differences worth noting include:
- GH2 provides a larger set of native types and parameters, which should be used whenever they make sense. More on this below.
- GH2 provides some additional options on some parameters (such as Indexing on Integer parameters, or Type Filters on Numeric parameters) which ought to be set when appropriate.
- GH2 parameters all have a `Preset` system, although this is used almost exclusively on Integer parameters to represents enumerations.

### New Parameter Types

The table below lists some new parameter types and when to use them.

| Types | Usage |
|----:|:----|
| `Field` | Fields (although technically not new) replace number or vector inputs when the component operates on an unambiguous location in space. Using the example code above, the circle radius input is no longer a number in GH2, but a field, since the circle centre point provides a clear location for the sampling of the field. |
| `Angle` | The angle type replaces `Number` whenever that number was used to represent an angle. Angles can be represented in Degrees, Radians, Turns, Grades and Spreads, allowing the user to specify them in whatever unit makes the most sense to them.  |
| `Numeric` | The Numeric parameter supports all native number types in GH2, including `System.Double`, `System.Int32`, `System.Numerics.BigInteger`, `System.Numerics.Complex` and `Grasshopper2.Types.Numeric.Angle`. Exactly which of these is allowed in any specific numeric parameter depends on the filter set by the developer. |
| `Function` | Functions sometimes replace numbers if the context allows for that. |
| `Gradient` | Gradients sometimes replace colours if the context allows for that. |
| `Random` | The `Random` parameter replaces an integer seed input. GH2 supports a variety of random engines, and the `RandomEngine` type combines the choice of engine plus seed value into one. |
| `Surface` | The `Surface` parameter in GH2 acts as a unified container for all surface types; `Rhino.Geometry.Surface`, `Rhino.Geometry.Brep`, `Rhino.Geometry.SubD`, `Rhino.Geometry.Sphere`, `Rhino.Geometry.Box`, and `Grasshopper2.Types.Shapes.Tube` for example. |
| `Point 2` | A two-dimensional point, typically used to represent (uv) coordinates and sometimes statistical samples. |
| `Triangle` | It's just for triangle primitives bro. |
| `Polyline` | Polylines are their own type now bro. |
| `Sphere` | Spheres are available now bro. |
| `Tube` | Tubes are a GH2 native type able to represent cones, cylinders, and tubes, both with and without wall thickness. |
| `Deform` | Deformations, i.e. SpaceMorphs are available as native types in GH2. |
| `Region` | A region is a set of closed co-planar curves without self-intersections. Use this instead of regular curves when dealing with planar inside-outside logic. |
| `Curve Locus` | Loci replace curve parameters in GH2. Do not use numbers to identify points on curves, use a curve locus. |
| `Surface Locus` | Loci replace surface uv-parameters in GH2. Do not use numbers to identify points on surfaces, use a surface locus. |

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

{{< image url="/images/gh2/EnumPresetsGH2Migration.png" alt="How UiName, UiInfo, and UiTint manifest in the GH2 interface." class="image_center" width="80%" >}}

Also note that GH2 supports `Quaternions` alongside old-fashioned 4x4 transform matrices. *HOW-EVER*, quaternions are encoded inside `Transform` matrices so whenever your component consumes transforms, be sure to always check whether they actually represent quaternions using the `IsQuaternion()` and `ToQuaternion()` extension methods on `Rhino.Geometry.Transform`.
  

## Component Processing

The key difference to bear in mind when writing processing code for GH2 components is that component iterations by default run on separate threads. Because of this, the code inside the `Process(IDataAccess access)` method must be thread-safe. If this is impossible, the threading state of the component must be downgraded from the default `ThreadingState.MultiThreaded` to `ThreadingState.SingleThreaded` via the `Component.Threading` property.

Furthermore, if the processing code is liable to take longer than a few milliseconds, the component should pay attention to cancellation requests by occasionally calling `access.Solution.Token.ThrowIfCancellationRequested()`.

### A Random Walk Example

Let's start with a relatively simple example of a component which doesn't operate on lists or trees, and doesn't need to deal with meta data. This example will introduce getting and setting individual values, dealing with fields and random engines, and how to implement cancellation. The component contains three inputs; a `Sphere`, a `Field` and a `RandomEngine`, and outputs a single `Polyline` representing a random walk from the centre of the sphere to the boundary. First, the code:

```cs
protected override void Process(IDataAccess access)
{
  // 1. Retrieve values from inputs. All the inputs 
  //    have Requirement=MustExist, so we don't have
  //    to check for missing or null values.
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
2. This component has a pseudo-random aspect, which means it requires a `RandomEngine` as an input. The `RandomEngine.CreateInstance()` method is used on an engine value to create a new random number generator of the correct type with the specified seed. Also note that GH2 provides a lot of useful extension methods via the `Grasshopper2.Extensions` namespace, so when that is added to the `using` block of your C# file you'll get access to methods like `Random.NextUnitVector3D()`.
3. Since the `while` loop in this component can potentially run for a *very* long time, it is important that cancellation is checked often. The `Solution` object passed to the component via the `IDataAccess` argument has a token which can be used for this. In GH2, every time a new solution starts, any currently running solution in that document is automatically cancelled.
4. Assignment of output values works exactly the same in GH2 as in GH1, at least when metadata or twigs or trees are not involved.

{{< image url="/images/gh2/RandomWalkGH2Migration.png" alt="The RandomWalk component running with 100 different random seeds." class="image_center" width="90%" >}}


### Working with Twigs and Curves

Grasshopper 2 takes a different approach to curve values. There are still dedicated parameters for specific curve types such as `Line`, `Circle`, `Arc`, `Rectangle`, etc., but the `Curve` parameter does *not* convert all curve-like values into `Rhino.Geometry.Curve` compliant types. Instead, the `Curve` parameter stores all curve values as-is, and only makes sure that each value is associated with a centrally registered `CurveAssistant`. This new approach has two benefits. First, it allows values to be stored without converting them to a different type. Second, it allows plug-ins to add their own curve-like types and trust that all existing components that operate on curves will be able to handle these new values. The drawback to this approach is that dealing with curves can be somewhat or significantly more complicated for component developers, depending on what curve operations a component needs to perform.

In the following example, we'll create a component which sorts curves based on whether their end-points both lie within a box, both outside of that box, or one-within-and-one-without. This example will discuss how to deal with twigs, curve assistants, and how to correctly persist meta data from input curves to output curves. The default meta-data-copying-mechanism in components will fail if the order of input and output values is not consistent.

This component must operate on entire twigs instead of individual values, for if each curve was treated individually, a `null` value would be automatically inserted into the two outputs where the curve did not end up. If this is desired behaviour, then by all means operate on single values, but in this case we want the outputs to contain no nulls.

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

"Twigs" in GH2 are equivalent to "Branches" in GH1. The word "branch" was not only topologically slightly incorrect, it also did not consist of four letters. GH2 uses exclusively 4-letter words to refer to the various types involved in data trees; tree, twig, item, path, pear, site, rule, null, and meta.

The `Process()` method for this component has to take care to correctly deal with null items in the twig, and to maintain the pairing of items with their original meta data. First consider the implementation, then we'll discuss the details:

```cs
protected override void Process(IDataAccess access)
{
  // 1. Retrieve values from inputs.
  access.GetITwig(0, out ITwig curves);
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
2. Similarly, since we can't know the type constraints ahead of time, it is not possible to use `Pear<T>` as a list constraint and we must fall back to the non-generic `IPear`. A pear is nothing more than the pairing of a value with its meta data. It is called a "pear" rather than a "pair" because "pair" was already taken and "pear" fits nicely within the tree-paradigm. All data tree types in GH2 are immutable, which means we cannot build a twig or tree over time. Instead, we must aggregate the contents in mutable collection types which are then converted into the appropriate twig/tree all at once.
3. There are several ways to iterate over the contents of a twig, but if the indices of values are not required, there are several handy enumerators which allow `foreach` to do all the heavy lifting.
4. The only reason this component needs cancellation support is because the twigs it operates on may contain thousands if not millions of values.
5. We need to find the curve assistant for each curve-like value in the twig. The `TypeAssistantServer` is a static class which maintains all registered assistants and provides easy lookup based on values or types. The curve assistant allows us to query the start and end-points of the curve value, even if we don't know the type of that value. It could be a `Rhino.Geometry.Line`, or a `Rhino.Geometry.NurbsCurve`, or even a curve type which is shipped as part of a 3rd party plugin years after the code for this component was written.
6. This part seems self-explanatory.
7. Once all pear lists have been made they can be converted into twigs and assigned to each output. The `Garden` static class provides a large number of utility functions for creating and modifying pears, twigs and trees.

{{< image url="/images/gh2/CurveSortingGH2Migration.png" alt="Curve end-point sorting in action." class="image_center" width="90%" >}}

// TODO: working with Trees/Pears/Meta still needed.

### Validation and Messaging

Components in GH2 have the ability, just as they did in GH1, to collate warning and error messages during processing. In general, warnings ought to be used when there was a problem the component could work around, and errors ought to be used when the component could not complete its calculations. However, unlike in GH1, the `IDataAccess` argument provides a set of validation and rectification methods which automatically set warning and error messages, if need be. This tends to simplify the portion of the processing code which deals with input validation.

Next time you need to make sure numbers are positive, or fall within a given range, or that two vectors aren't parallel, or three points aren't colinear, have a look at all the methods starting with `Rectify___` and `Verify___` on `IDataAccess.

When a custom warning or error needs to be signaled to the user, the `access` argument also provides direct ways of adding runtime messages to the component. The `IDataAccess.AddWarning()` and `IDataAccess.AddError()` methods allow the developer to set runtime messages with custom phrasing and custom actions. Adding message actions which allow the user to fix problems is strongly encouraged whenever possible. When messages have actions, they will appear in the message menu as follows:

{{< image url="/images/gh2/MessageActionGH2Migration.png" alt="Actions attached to runtime messages provide fast ways to fix issues." class="image_center" width="90%" >}}


### Custom Properties

In GH1, any component which needed to remember a custom setting (a mode picked from the context menu, a toggle state, ...) had to override the `Write(GH_IWriter)` and `Read(GH_IReader)` methods and handle the serialisation of that setting by hand. GH2 still allows this (see below), but for settings usig primitive types there is now an easier to use mechanism which requires no serialisation code at all.

Every document object carries a `CustomValues` property of type `KeyedValues`; a mutable collection of named values which is automatically included whenever the object is written to or read from a file. Storing a setting takes a single `Set()` call and retrieving it takes a single `Get()` call, where the second argument acts as the fallback in case the key has not (yet) been assigned:

```cs
// Read the current smoothing setting, using 0.5 if none was ever set.
var smoothing = CustomValues.Get("Smoothing", 0.5);

// Assign a new smoothing setting.
CustomValues.Set("Smoothing", 0.75);
```

Because every getter takes a fallback value, there is no need to check whether a key exists before reading it, and components loaded from files which predate the introduction of a setting will just get the fallback. Key comparisons are case-insensitive, and access is thread-safe.

The natively supported types are `bool`, `int`, `double`, `string`, `Guid`, `DateTime`, `TimeSpan`, and the `Eto.Drawing` primitives (`Color`, `Point`, `PointF`, `Size`, `SizeF`, `Rectangle`, `RectangleF`).

Two caveats. First, assigning a custom value does not expire the solution or the display; if the setting affects computed results, it is up to you to expire the object. Second, changes to custom values are not automatically undoable. When a change ought to appear on the undo stack, you must create an undo snapshot of the values *before* modifying them using a `CustomValueAction`, then commit that action afterwards:

```cs
var undoAction = new CustomValueAction(this, "Smoothing");
AddUndoRecord(new VerbNoun("Change", "Smoothing"), undoAction);

CustomValues.Set("Smoothing", 0.75);
```

#### Overriding Store() and the Reader Constructor

When object state does not fit into the `CustomValues` collection (collections, nested data structures, other complex types) the GH1 approach is still available. The `Store(IWriter)` method is the equivalent of `Write()`, and deserialisation happens in the constructor which takes an `IReader`, the very same constructor every document object is already required to have:

```cs
public override void Store(IWriter writer)
{
  base.Store(writer);
  writer.Number64Array("Weights", _weights);
}

public MyComponent(IReader reader) : base(reader)
{
  if (reader.HasItem("Weights"))
    _weights = reader.Number64Array("Weights");
}
```

Note that the `Store()` override must *always* invoke `base.Store(writer)`, and the reader constructor must *always* invoke `: base(reader)`. Forgetting either will lead to broken file IO.

This approach is discouraged for simple settings because it shifts all versioning responsibility onto the developer. Every name and type you ever write into a file becomes a contract with every file saved from that day forward, and reading code must forever guard against items which are absent from older files (note the `HasItem()` check above). The `CustomValues` mechanism handles all of that for you; reserve `Store()` overrides for state which genuinely cannot be expressed any other way.


## Variable Parameter Layouts

As in GH1, components in GH2 can have variable numbers of inputs and outputs. All that is needed to enable the user interface for adding or removing inputs and outputs is to override the `CanCreateParameter()`, `DoCreateParameter()` and `CanRemoveParameter()` methods. The `DoRemoveParameter()` may be overridden as well, but the default behaviour already does what it says on the tin. Lastly, the `VariableParameterMaintenance()` method is still the best place to ensure that all properties of all parameters are correctly set.

Let's explore this with a component which creates boundingboxes for points in a variable number of inputs. Since we are creating a component which has a fully functional `VariableParameterMaintenance()` implementation, we can avoid assinging names and requirements inside the `AddInputs()` method:

```cs
protected override void AddInputs(InputAdder inputs)
{
  inputs.AddPoint(string.Empty, string.Empty, string.Empty);
  inputs.AddPoint(string.Empty, string.Empty, string.Empty);
}
protected override void AddOutputs(OutputAdder outputs)
{
  outputs.AddBox("Bounding Box", "Bx", "Box containing all input points.");
}
```

Now the three required overrides, with an absolutely minimal implementation:

```cs
public override bool CanCreateParameter(Side side, int index)
{
  // Parameters can be added everywhere on the input side.
  return side == Side.Input;
}
public override bool CanRemoveParameter(Side side, int index)
{
  // All inputs except for the last remaining one can be removed.
  return side == Side.Input && Parameters.InputCount > 1;
}
public override void DoCreateParameter(Side side, int index, ActionList undo)
{
  // The access is assigned at construction, but the nomen is 
  // left for the VariableParameterMaintenance() method.
  // Note that we are required to pass the undo action list 
  // to the AddInput() method.
  var param = new Point3Parameter(Nomen.Empty, Access.Item);
  Parameters.AddInput(param, index, undo);
}
```

Lastly the implementation of the maintenance method, which does all the heavy lifting:

```cs
public override void VariableParameterMaintenance()
{
  // Each input must be set up correctly.
  for (int i = 0; i < Parameters.InputCount; i++)
  {
    var param = Parameters.Input(i);
    param.Requirement = Requirement.MayBeMissing;
    param.ModifyNameAndInfo($"Point {i + 1}", 
      "Point to include in bounding box.");
    param.FallbackName = $"P{i + 1}";
  }
}
```

Note that this code assigns the `FallbackName` of each parameter rather than the `UserName`. This prevents us from overwriting user typed names on inputs. The `DisplayName` of a parameter is either the `UserName` or the `FallbackName`, depending on which one has been set.

Iterating over a variable number of parameters is quite easy by using the `IDataAccess.CountIn` and `IDataAccess.CountOut` properties. Since the inputs have a requirement of `MayBeMissing`, we need to check to see whether the `IDataAccess.GetItem()` method returns `true` or `false`. An input with a null value or with no values at all will return `false` when queried.

```cs
protected override void Process(IDataAccess access)
{
  var points = new List<Point3d>();
  for (int i = 0; i < access.CountIn; i++)
    if (access.GetItem(i, out Point3d point))
      points.Add(point);
  
  if (points.Count == 0)
    access.AddError("Insufficient Points", 
      "At least a single point is required for a valid bounding box.");
  else
    access.SetItem(0, new Box(new BoundingBox(points)));
}
```

{{< image url="/images/gh2/VariableParametersGH2Migration.gif" alt="Variable parameter UI on the canvas.." class="image_center" width="40%" >}}

## Modular Components

Whereas variable parameters are typically used for adding inputs or outputs that are all the same kind of thing, and for which is there is no upper limit, Grasshopper 2 adds the notion of a 'Modular Component' which is capable of hiding and showing specific inputs and outputs. When a component class is derived not from `Grasshopper2.Components.Component` but from `Grasshopper2.Components.ModularComponent`, the `AddInputs()` and `AddOutputs()` methods are replaced with their modular counterparts.

Creating modular components is quite a bit more involved as modular inputs and outputs need to be grouped into categories, given UI tinting, and often even icons. This document will only mention this corner of the Grasshopper 2 SDK without providing any examples.

# Data Types

## Data Trees

Structured data in GH2 is still organised in trees, and any GH1 developer will recognise the overall shape immediately: a tree is a collection of twigs, each one uniquely identified by a path of integers, and each twig contains an ordered list of items. What has changed is the naming, the type constraints, meta data support, and above all the mutability.

The types involved, from large to small:

| Type | Role |
|:----|:----|
| `Tree<T>` / `ITree` | The whole data structure; the equivalent of `GH_Structure<T>`. |
| `Paths` | The sorted collection of paths in a tree. |
| `Path` | An ordered, immutable list of non-negative integers identifying a twig; the equivalent of `GH_Path`. |
| `Twig<T>` / `ITwig` | An immutable list worth of items and their associated meta data; the equivalent of `List<GH_Goo<T>>` in GH1. |
| `Pear<T>` / `IPear` | A single value paired with its meta data. |
| `Site` | The location (path plus index) of an item within a tree. |
| `MetaData` | The immutable collection of named meta values associated with a single item. |

Most of these types come in a generic and a non-generic interface flavour. Use `Tree<T>`, `Twig<T>`, and `Pear<T>` whenever the item type is known at compile time, and fall back to `ITree`, `ITwig`, and `IPear` when the data may be of mixed or unknown types.

The salient differences with GH1 are:

- **No more goo.** `GH_Structure<T>` demanded that `T` implemented `IGH_Goo`; `Tree<T>` stores plain values.
- **Everything is immutable.** Trees, twigs, paths, and pears cannot be modified after creation. The GH1 habit of creating an empty structure and appending to it as you go has been replaced by aggregating values in ordinary mutable collections (a `List<T>`, an array) and converting to a twig or tree in a single step at the end.
- **Meta data exists.** Every item in a twig may carry meta data, and the pear is the unit which keeps a value and its meta data together. A `Twig<int>` which contains both metadata and null values will under the hood maintain three separate arrays; `int[]` for the actual values, `bool[]` for the null states, and `MetaData[]` for the meta data.

Twigs and trees are not created via constructors; the actual instances are specialised internal implementations chosen based on content (with or without nulls, with or without meta data, value or reference types). Instead, all creation goes through the static `Garden` class; the one-stop-shop for growing trees. It contains factory methods for a lot of different tree and twig creation methods: `TwigFromList()`, `TwigFromPears()`, `TreeFromArrays()`, `ITreeFromITwigs()`, and dozens more, along with utilities for merging trees, casting between generic and non-generic forms, and comparing pears.

Modifying existing trees and twigs is often done with instance methods on `ITree`, `Tree<T>`, `ITwig` or `Twig<T>` directly, just remember these methods always return new tree and twig instances, as the existing instance are immutable.

## Meta Data

[[[Design, immutability, StandardNames, transformable entries.]]]

## Type Handling

In GH1, every value was wrapped in an `IGH_Goo` container, and that container was responsible for everything the value could do: formatting, duplication, validity, previews, baking, transformations, and casting to and from other types. GH2 takes a dramatically different tack. Values in GH2 are stored as-is (a circle in a data tree really is a `Rhino.Geometry.Circle`) and all shared functionality is provided by separate objects which are registered centrally. The many features which `IGH_Goo` used to provide are now handled by two separate systems; *assistants* provide type functionality, and the *conversion server* provides data conversion between types.

Both systems share the same registration model: when a plugin loads, its assembly is scanned and all assistant and conversion repository classes are instantiated and registered automatically. There is no manual registration step; the classes merely have to be public and have parameterless constructors.

This chapter only explains the design from the perspective of a component developer consuming existing types. Creating your own data types — and the assistants, conversions, and parameters that come with them — is a big enough topic to deserve a document of its own.

### Type Assistants

Every type which flows through Grasshopper 2 should be associated with an `ITypeAssistant`, and the static `TypeAssistantServer` class maintains the registry and provides lookup by type or by value. The assistant answers on behalf of the type whenever Grasshopper has a question: "What is your name?", "Are you valid?", "How do I create a duplicate?", "How are you drawn in the Rhino viewports?", "Do you have a boundingbox, and if 'yes' how big is it?", ...

Not every type supports every operation (a colour cannot be drawn in viewports, a mesh has no length) so each capability is advertised through a property with a `Zupports` prefix: `ZupportsDraw`, `ZupportsBake`, `ZupportsLength`, `ZupportsClosestPoint`, and so on. Whenever a type assistant overrides a virtual method, the base class detects this and sets the appropriate `ZupportsXyz` property to `true`. Code which consumes an unfamiliar assistant ought to check the relevant `Zupports` property before relying on the matching operation.

Curve-like and surface-like types get an additional, more specialised treatment. Whereas the GH1 `Curve` parameter converted every incoming value to a `Rhino.Geometry.Curve`, the GH2 parameter stores values untouched and requires only that each curve-like type registers an `ICurveAssistant` (in practice by deriving from the `CurveAssistant` base class; never implement the interface from scratch). The assistant answers all curve questions — domains, spans, end points, conversion to NURBS or polyline form — so a component which operates on curves through assistants automatically works with *every* registered curve type, including types shipped by other plugins years after the component was written. Surface-like types follow the same pattern via `ISurfaceAssistant` and the `SurfaceAssistant` base class.

Component developers who do not care about any of this and simply want a Rhino curve or brep out of whatever value they were handed can use the static `CurveBroker` and `SurfaceBroker` utility classes, which perform the type-checking and conversion song-and-dance in a single call.

### Type Conversion

The `CastTo`/`CastFrom` logic which used to live inside each `IGH_Goo` type is replaced by the static `ConversionServer`, a central registry of conversion delegates keyed by (source type, target type) pairs. Plugins contribute conversions by deriving a class from `ConversionRepository` and filling it with public static methods which take a source value and produce a target value via an `out` parameter.

Every conversion method must be decorated with a `Merit` attribute, which expresses how sensible the conversion is: `Direct`, `Fair`, `Plausible`, `Strange`, or `Weird`. When data of one type arrives at a parameter of another, the server picks the best available conversion, and the merit travels along with the result. Low-merit conversions are deliberately surfaced to users as a hint that, although Grasshopper managed to perform the requested conversion, they may well be doing something wrong.

The complete set of registered conversions can be inspected from within Grasshopper via the *Conversion Graph* entry in the Solver menu, which displays all conversion pairs known to the server as a chord diagram.

{{< image url="/images/gh2/RegisteredTypeConversions.png" alt="The Type Conversion Diagram shows all centrally registered type coversions currently available." class="image_center" width="70%" >}}

# Renaming Cheat-Sheet

The table below maps the GH1 types, members, and concepts you're likely to search for onto their GH2 counterparts. It is organised roughly by topic: plugin level first, then components and parameters, data access, data structures, document objects, user interface, and finally (de)serialisation.

| GH1 name | GH2 name | Salient differences |
|:----|:----|:----|
| `*.gha` file | `*.rhp` file | A single `.rhp` can be both a Rhino plugin and a Grasshopper plugin. |
| `GH_AssemblyInfo` | `Grasshopper2.Framework.Plugin` | Identity and authorship now come from assembly attributes; see the Plugin Assembly section. |
| `GH_Component` | `Grasshopper2.Components.Component` | Requires an additional deserialisation constructor taking an `IReader`. |
| `ComponentGuid` property | `[IoId]` class attribute | Lives in `GrasshopperIO.dll`. Applies to all storable types, not just components. |
| `GH_Exposure` property | `Rank` and `Slot` (inside `Nomen`) | Part of the `Nomen` passed to the constructor rather than a separate override. |
| `Icon` property (`Bitmap`) | `IIcon` / `AbstractIcon` | Vector icons are supported and recommended. The override can be omitted when an embedded resource matches the class name exactly. |
| `NickName` | `UserName`, `FallbackName`, `DisplayName` | Split in two: `FallbackName` is set by code, `UserName` by the user. `DisplayName` picks whichever is appropriate. |
| Name, description, category, subcategory | `Nomen` | One immutable type bundling name, info, tab, panel, slot, and rank. |
| `RegisterInputParams(GH_InputParamManager)` | `AddInputs(InputAdder)` | Defaults are assigned via `Set()` on the returned parameter rather than an argument. |
| `RegisterOutputParams(GH_OutputParamManager)` | `AddOutputs(OutputAdder)` | |
| `GH_ParamAccess.item/list/tree` | `Access.Item/Twig/Tree` | Item access is the default and need not be specified. |
| `Optional` property | `Requirement` property | Three states instead of a boolean: `MustExist`, `MayBeNull`, `MayBeMissing`. |
| `GH_PersistentParam<T>.PersistentData` | `Parameter<T>.Set(...)` | Overloads exist for single items, collections, and entire trees. |
| `IGH_Param` | `Grasshopper2.Parameters.Parameter` / `IParameter` | Type-specific functionality lives in `Parameter<T>`. |
| `IGH_VariableParameterComponent` | virtual methods on `Component` | No separate interface; override `CanCreateParameter()`, `DoCreateParameter()`, `CanRemoveParameter()`, and `VariableParameterMaintenance()`. |
| `Params` property | `Parameters` property | E.g. `Parameters.InputCount` and `Parameters.Input(i)`. |
| `SolveInstance(IGH_DataAccess)` | `Process(IDataAccess)` | Runs multi-threaded by default; must be thread-safe or downgrade `Component.Threading`. |
| `GH_TaskCapableComponent` | — | Gone. The solver is inherently multi-threaded and cancellable. |
| `DA.GetData(...)` / `SetData(...)` | `access.GetItem(...)` / `SetItem(...)` | Uses `out` instead of `ref`. Returns `false` for missing or null data. |
| - | `access.GetPear(...)` / `SetPear(...)` | New. Getting and settings values with metadata requires pears.  |
| `DA.GetDataList(...)` / `SetDataList(...)` | `access.GetTwig<T>(...)` / `SetTwig(...)` | Use `GetITwig(...)` when the value types cannot be known ahead of time. |
| `DA.GetDataTree(...)` / `SetDataTree(...)` | `access.GetTree<T>(...)` / `SetTree(...)` | Likewise `GetITree(...)` for mixed or unknown types. |
| `AddRuntimeMessage(GH_RuntimeMessageLevel, ...)` | `access.AddWarning` / `access.AddError(...)` | Messages take a text and details, and optionally actions which let the user fix the problem. Also see the `VerifyXyz` and `RectifyXyz` methods. |
| `GH_Structure<T>` | `Grasshopper2.Data.Tree<T>` | Immutable. Aggregate values in mutable collections and construct trees at the end, typically via `Garden`. |
| branch or `List<T>` | `Twig<T>` / `ITwig` | Immutable, and items are paired with meta data (see pears). |
| `GH_Path` | `Grasshopper2.Data.Path` | |
| `IGH_Goo` / `GH_Goo<T>` | — | Gone. Values are stored as-is; shared functionality is provided by type assistants, conversions by the conversion server. |
| `GH_ObjectWrapper` | - | Gone. Values are stored as-is and do not need to be wrapped. |
| `GH_Convert` / `CastTo` / `CastFrom` | `ConversionServer` / `ConversionRepository` | Conversions are registered centrally instead of being implemented per data type. |
| `GH_Document` | `Grasshopper2.Doc.Document` | |
| `GH_DocumentObject` | `Grasshopper2.Doc.DocumentObject` | |
| `GH_ActiveObject` | `Grasshopper2.Doc.ActiveObject` | |
| `OnPingDocument()` | `Document` property | |
| `ExpireSolution(true)` | `Expire()` + `Document?.Solution.Start()` or `Document?.Solution.DelayedExpire(this)` | Expiry and recomputation are separate steps. Expiring also request-cancels any running solution in the document. |
| `Locked` | `Activity` property | An `ObjectActivity` enumeration instead of a boolean. |
| `Hidden` | `Display` property | An `ObjectDisplay` enumeration instead of a boolean. |
| `RecordUndoEvent(...)` | `AddUndoRecord(...)` | Takes a `VerbNoun` plus any number of `Undo.Action` instances. |
| `DrawViewportWires/Meshes(...)` | `PopulateDisplay(...)` | Display geometry is cached centrally rather than drawn per frame. |
| `ClippingBox` | `DisplayBounds()` | |
| `AppendAdditionalMenuItems(...)` | `AppendToInputPanel(...)` | Context menus are replaced by the input panel, built from `Grasshopper2.UI.InputPanel` parts. |
| `IGH_Attributes` / `GH_ComponentAttributes` | `IAttributes` / `Attributes<T>` | All custom UI is drawn with Eto rather than WinForms/GDI+, and must work on both Windows and Mac. |
| `GH_Canvas` | `Grasshopper2.UI.Canvas.Canvas` | An Eto control rather than a WinForms one. |
| `GH_IO.dll` | `GrasshopperIO.dll` | |
| `GH_IWriter` / `GH_IReader` | `IWriter` / `IReader` | |
| `Write(GH_IWriter)` / `Read(GH_IReader)` | `Store(IWriter)` / constructor taking `IReader` | Deserialisation happens in a constructor so that immutable types can be restored. Prefer `CustomValues` for simple settings. |
| `GH_Archive` | `GrasshopperIO.IO` | Static methods for reading and writing storable objects to streams, files, and byte arrays. |
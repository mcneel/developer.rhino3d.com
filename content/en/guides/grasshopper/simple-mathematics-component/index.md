+++
aliases = ["/en/5/guides/grasshopper/simple-mathematics-component/", "/en/6/guides/grasshopper/simple-mathematics-component/", "/en/7/guides/grasshopper/simple-mathematics-component/", "/wip/guides/grasshopper/simple-mathematics-component/"]
authors = [ "david" ]
categories = [ "Fundamentals" ]
description = "This guide contains a brief example of a component that deals with some simple mathematics and multiple input and output parameters."
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#", "VB" ]
sdk = [ "Grasshopper" ]
title = "Simple Mathematics Component"
type = "guides"
weight = 2
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Overview

We'll discuss parameter order, legacy support for changing component layouts and default values for input parameters.

For this component we'll bundle the Sine(), Cosine() and Tangent() trigonometry functions while allowing inputs to be specified in either Radians or Degrees.  We'll need to define two input parameter (one of which will have a default value) and three output parameters.

## Prerequisites

We will not be dealing with any of the basics of component development.  Please start with the [Your First Component](/guides/grasshopper/your-first-component-windows) guide and the [Simple Component](/guides/grasshopper/simple-component) guide before starting this one.

Before you start, create a new class that derives from `Grasshopper.Kernel.GH_Component`, as outlined in the [Simple Component](/guides/grasshopper/simple-component) guide.

## Input parameters

This component will require two input parameters, one of which has a default value.  We'll need to register these parameters inside the `RegisterInputParams()` method:

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'vb')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content" id="cs">

```cs
...
protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
{
  pManager.AddNumberParameter("Angle", "A", "The angle to measure", GH_ParamAccess.item);
  pManager.AddBooleanParameter("Radians", "R", "Work in Radians", GH_ParamAccess.item, true); // The default value is 'true'
}
...

```

</div>

<div class="codetab-content" id="vb">

```vbnet
...
Protected Overrides Sub RegisterInputParams(ByVal pManager As GH_Component.GH_InputParamManager)
  pManager.AddNumberParameter("Angle", "A", "The angle to measure", GH_ParamAccess.item)
  pManager.AddBooleanParameter("Radians", "R", "Work in Radians", GH_ParamAccess.item, True) 'The default value is 'True'
End Sub
...
```

</div>
</div>

The first parameter is of type Double meaning it accepts floating point values.  It only has a name, abbreviation, description and access level defined.  The second parameter is of type `bool` and it will accept `true` and `false` values.  The `pManager` object allows us to specify a single default value for many parameter types.

The order in which we register the parameters is also the order in which they'll appear on the component.  We should not change the order (or the types, or the number) of the parameters once the component has been released to the world.  Every Grasshopper file that was saved with one of our components will expect to be deserialized by the exact same component layout.  If you add an additional parameter to an component and someone tries to open a file which was saved while an older version of that component, it will fail to deserialize as the data in the file no longer matches the new layout.  An exception will be thrown and Grasshopper will short circuit that particular instance.  The entire component and all connections to it will be missing when the file is eventually displayed to the user.

*If you must* change the parameter layout of a component, you should create a completely new `GH_Component` class with a different `ComponentGuid`, while maintaining the old component type for legacy file purposes.  You can hide components from the Grasshopper GUI by overriding the [Exposure](/api/grasshopper/html/P_Grasshopper_Kernel_IGH_DocumentObject_Exposure.htm) property of the `GH_Component` class and changing the return value to `GH_Exposure.hidden`:

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'vb1')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content1" id="cs1">

```cs
public override Grasshopper.Kernel.GH_Exposure Exposure
{
  get { return GH_Exposure.hidden; }
}

```

</div>

<div class="codetab-content1" id="vb1">

```vbnet
Public Overrides ReadOnly Property Exposure() As Grasshopper.Kernel.GH_Exposure
  Get
    Return GH_Exposure.hidden
  End Get
End Property
```

</div>
</div>

## Output Parameters

Our component will also need three output parameters.  Output parameters differ from input parameters in that they have much fewer options.  Users cannot add expressions to them, there are no default values, they don't support persistent data.  Outputs are always cleared when the component expires, and they are slowly filled out from within the `SolveInstance()` routine.

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'vb2')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content2" id="cs2">

```cs
...
protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
{
  pManager.AddNumberParameter("Sin", "sin", "The sine of the Angle.", GH_ParamAccess.item);
  pManager.AddNumberParameter("Cos", "cos", "The cosine of the Angle.", GH_ParamAccess.item);
  pManager.AddNumberParameter("Tan", "tan", "The tangent of the Angle.", GH_ParamAccess.item);
}
...

```

</div>

<div class="codetab-content2" id="vb2">

```vbnet
...
Protected Overrides Sub RegisterOutputParams(ByVal pManager As GH_Component.GH_OutputParamManager)
  pManager.AddNumberParameter("Sin", "sin", "The sine of the Angle.", GH_ParamAccess.item)
  pManager.AddNumberParameter("Cos", "cos", "The cosine of the Angle.", GH_ParamAccess.item)
  pManager.AddNumberParameter("Tan", "tan", "The tangent of the Angle.", GH_ParamAccess.item)
End Sub
...
```

</div>
</div>

## SolveInstance

The `SolveInstance()` implementation for this component is hardly any more complicated than it was for the [Simple Component](/guides/grasshopper/simple-component/#the-solver-routine).  The only difference is that we now have more than one parameter on each side.

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'vb3')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content3" id="cs3">

```cs
...
protected override void SolveInstance(IGH_DataAccess DA)
{
  // Declare variables to contain all inputs.
  // We can assign some initial values that are either sensible or indicative.
  double angle = double.NaN;
  bool radians = false;

  // Use the DA object to retrieve the data inside the input parameters.
  // If the retrieval fails (for example if there is no data) we need to abort.
  if (!DA.GetData(0, ref angle)) { return; }
  if (!DA.GetData(1, ref radians)) { return; }

  // If the angle value is not a valid number, we should abort.
  if (!Rhino.RhinoMath.IsValidDouble(angle)) { return; }

  // If the user wants to work in degrees rather than radians,
  // we assume that angle is defined in degrees.
  // We need to convert it into Radians again.
  if (!radians)
  {
    angle = Rhino.RhinoMath.ToRadians(angle);
  }

  // Now we are ready to assign the outputs via the DA object.
  // Since the Sin(), Cos() and Tan() never fail, we might as well
  // combine them with the assignment.
  DA.SetData(0, Math.Sin(angle));
  DA.SetData(1, Math.Cos(angle));
  DA.SetData(2, Math.Tan(angle));
}
...

```

</div>

<div class="codetab-content3" id="vb3">

```vbnet
...
Protected Overrides Sub SolveInstance(ByVal DA As Grasshopper.Kernel.IGH_DataAccess)
  'Declare variables to contain all inputs.
  'We can assign some initial values that are either sensible or indicative.
  Dim angle As Double = Double.NaN
  Dim radians As Boolean = False

  'Use the DA object to retrieve the data inside the input parameters.
  'If the retrieval fails (for example if there is no data) we need to abort.
  If (Not DA.GetData(0, angle)) Then Return
  If (Not DA.GetData(1, radians)) Then Return

  'If the angle value is not a valid number, we should abort.
  If (Not Rhino.RhinoMath.IsValidDouble(angle)) Then Return

  'If the user wants to work in degrees rather than radians,
  'we assume that angle is defined in degrees.
  'We need to convert it into Radians again.
  If (Not radians) Then
    angle = Rhino.RhinoMath.ToRadians(angle)
  End If

  'Now we are ready to assign the outputs via the DA object.
  'Since the Sin(), Cos() and Tan() never fail, we might as well
  'combine them with the assignment.
  DA.SetData(0, Math.Sin(angle))
  DA.SetData(1, Math.Cos(angle))
  DA.SetData(2, Math.Tan(angle))
End Sub
...
```

</div>
</div>

**DONE!**

We've discussed parameter order, legacy support for changing component layouts, and default values for input parameters.  **Now what?**

## Next Steps

Next, check out the [Simple Geometry Component](/guides/grasshopper/simple-geometry-component) guide to see how to use some of the simpler geometry types and classes in RhinoCommon and Grasshopper.

## Related Topics

- [What is a Grasshopper Component?](/guides/grasshopper/what-is-a-grasshopper-component)
- [Installing Tools (Windows)](/guides/grasshopper/installing-tools-windows/)
- [Your First Component](/guides/grasshopper/your-first-component-windows)
- [Simple Component](/guides/grasshopper/simple-component)
- [Simple Geometry Component](/guides/grasshopper/simple-geometry-component)

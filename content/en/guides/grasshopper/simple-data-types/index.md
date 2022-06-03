+++
authors = [ "david" ]
categories = [ "Fundamentals" ]
description = "This guide discusses how Grasshopper deals with data items and types."
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#", "VB" ]
sdk = [ "Grasshopper" ]
title = "Simple Data Types"
type = "guides"
weight = 4
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

It's a rather complicated topic as data is an integral part of the Grasshopper process and GUI.  Grasshopper needs to be able to (de)serialize data, display data in tooltips, convert data to other types of data, prompt the user for persistent data, draw geometry preview data in viewports and bake geometric data.  In this topic I'll only talk about non-geometric data, we'll get to previews and baking in a later topic.

Practically all native data types in Grasshopper are based either on a .NET Framework type or a RhinoCommon type.  For example `System.Boolean`, `System.String`, `Rhino.Geometry.Point3d` and `Rhino.Geometry.Brep` to name but a few.  However, the parameters in Grasshopper don't directly store Booleans, String, Points and Breps as these types can't handle themselves in the cauldron that is Grasshopper.

## Prerequisites

We will not be dealing with any of the basics of component development in this guide.  Please start with the [Your First Component](/guides/grasshopper/your-first-component-windows) guide and the [Simple Component](/guides/grasshopper/simple-component) guide before starting this one.

Before you start, create a new class that derives from `Grasshopper.Kernel.GH_Component`, as outlined in the [Simple Component](/guides/grasshopper/simple-component) guide.

## The IGH_Goo interface

In this section I'll briefly discuss all the methods and properties that are defined in IGH_Goo.  What they're for, who uses them at what time, etc, etc.

All data used in Grasshopper must implement the [IGH_Goo](/api/grasshopper/html/T_Grasshopper_Kernel_Types_IGH_Goo.htm) interface.  `IGH_Goo` defines the bare minimum of methods and properties for any kind of data before it is allowed to play ball.

### IsValid

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'vb')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content" id="cs">

```cs
bool IsValid { get{} }

```

</div>

<div class="codetab-content" id="vb">

```vbnet
ReadOnly Property IsValid() As Boolean
```

</div>
</div>

Not all data types are valid all the time, and this property allows you to test the current instance of your data.  When data is invalid it will often be ignored by components.

### TypeName

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'vb1')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content1" id="cs1">

```cs
string TypeName { get{} }

```

</div>

<div class="codetab-content1" id="vb1">

```vbnet
ReadOnly Property TypeName() As String
```

</div>
</div>

This property must return a human-readable name for your data type.

### TypeDescription

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'vb2')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content2" id="cs2">

```cs
string TypeDescription { get{} }

```

</div>

<div class="codetab-content2" id="vb2">

```vbnet
ReadOnly Property TypeDescription() As String
```

</div>
</div>

This property must return a human-readable description of your data type.

### Duplicate

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'vb3')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content3" id="cs3">

```cs
IGH_Goo Duplicate()

```

</div>

<div class="codetab-content3" id="vb3">

```vbnet
Function Duplicate() As IGH_Goo
```

</div>
</div>

This function must return an exact duplicate of the data item.  Data is typically shared amongst multiple Grasshopper parameters, so before data is changed, it first needs to copy itself.  When data only contains ValueTypes and Primitives, making a copy of an instance is usually quite easy.

### ToString

<div class="codetab">
  <button class="tablinks4" onclick="openCodeTab(event, 'cs4')" id="defaultOpen4">C#</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'vb4')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content4" id="cs4">

```cs
string ToString()

```

</div>

<div class="codetab-content4" id="vb4">

```vbnet
Function ToString() As String
```

</div>
</div>

This function is called whenever Grasshopper needs a human-readable version of your data.  It is this function that populates the data panel in parameter tooltips.  You don't need to create a String that is parsable, it only needs to be somewhat informative.

### EmitProxy

<div class="codetab">
  <button class="tablinks5" onclick="openCodeTab(event, 'cs5')" id="defaultOpen5">C#</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'vb5')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content5" id="cs5">

```cs
IGH_GooProxy EmitProxy()

```

</div>

<div class="codetab-content5" id="vb5">

```vbnet
Function EmitProxy() As IGH_GooProxy
```

</div>
</div>

Data proxies are used in the Data Collection Manager.  You can ignore this function (i.e. Return Nothing) without crippling your data type.

### CastTo

<div class="codetab">
  <button class="tablinks6" onclick="openCodeTab(event, 'cs6')" id="defaultOpen6">C#</button>
  <button class="tablinks6" onclick="openCodeTab(event, 'vb6')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content6" id="cs6">

```cs
bool CastTo<T>(out T target)

```

</div>

<div class="codetab-content6" id="vb6">

```vbnet
Function CastTo(Of T)(ByRef target As T) As Boolean
```

</div>
</div>

Data Casting is a core feature of Grasshopper data.  It basically allows data types defined in Grasshopper add-ons to become an integral part of Grasshopper.  Lets assume that we have a Component that operates on data type [A].  But instead of playing nice, we provide data of type [B]. Two conversion (casting) attempts will be made in order to change [B] into [A].  If [B] implements IGH_Goo, then it is asked if it knows how to convert itself into an instance of [A].  Failing that, if [A] implements `IGH_Goo`, it is asked whether or not it knows how to construct itself from an instance of [B].

The `CastTo()` function is responsible for step 1.  The `CastTo()` method is a generic method, meaning the types on which it operates are not defined until the method is actually called.  This allows the function to operate "intelligently" on data types.  It also unfortunately means you have to be "intelligent" when implementing this function.

See the [Grasshopper Data Types](/guides/grasshopper/grasshopper-data-types) guide for more information on conversion.

### CastFrom

<div class="codetab">
  <button class="tablinks7" onclick="openCodeTab(event, 'cs7')" id="defaultOpen7">C#</button>
  <button class="tablinks7" onclick="openCodeTab(event, 'vb7')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content7" id="cs7">

```cs
bool CastFrom(object source)

```

</div>

<div class="codetab-content7" id="vb7">

```vbnet
Function CastFrom(ByVal source As Object) As Boolean
```

</div>
</div>

The `CastFrom()` function is responsible for step 2 of data casting.  Some kind of data is provided as a source object and if the local Type knows how to "read" the source data it can perform the conversion.

See the [Grasshopper Data Types](/guides/grasshopper/grasshopper-data-types) guide for more information on conversion.

### ScriptVariable

<div class="codetab">
  <button class="tablinks8" onclick="openCodeTab(event, 'cs8')" id="defaultOpen8">C#</button>
  <button class="tablinks8" onclick="openCodeTab(event, 'vb8')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content8" id="cs8">

```cs
object ScriptVariable()

```

</div>

<div class="codetab-content8" id="vb8">

```vbnet
Function ScriptVariable() As Object
```

</div>
</div>

When data is fed into a VB or C# script component, it is usually stripped of `IGH_Goo` specific data and methods.  The `ScriptVariable()` method allows a data type to provide a stripped down version of itself for use in a Script component.

## The GH_Goo abstract class

Although all data in Grasshopper must implement the `IGH_Goo` interface, it is not necessary to actually write a type from scratch.  It is good practice to inherit from the abstract class `GH_Goo<T>`, as it takes care of some of the basic functionality.  `GH_Goo` is a generic type (that's what the "`<T>`" bit means), where `T` is the actual type you're wrapping.  `GH_Goo<T>` has several abstract methods and properties which *must* be implemented, but a lot of the other methods are already implemented with basic (though usually useless) functionality.

## An Example Type

We'll now create a very simple custom type.  This will introduce the basic concept of custom type development, without dealing with any of the baking and previewing logic yet.  Our custom type will be a TriState flag, similar to boolean values but with an extra state called "Unknown".  We'll represent these different states using integers:

- Negative One `-1` = Unknown
- Zero `0` = False
- One `1` = True

We'll start with the general class layout, then drill down into each individual function.  Create a new public class called `TriStateType` and inherit from `GH_Goo<Integer>`.  Be sure to import the Grasshopper `Kernel` and `Kernel.Types` namespaces as we'll need them both:

<div class="codetab">
  <button class="tablinks9" onclick="openCodeTab(event, 'cs9')" id="defaultOpen9">C#</button>
  <button class="tablinks9" onclick="openCodeTab(event, 'vb9')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content9" id="cs9">

```cs
using Grasshopper.Kernel;
using Grasshopper.Kernel.Types;

namespace MyTypes
{
  public class TriStateType : GH_Goo<int>
  {

  }
}

```

</div>

<div class="codetab-content9" id="vb9">

```vbnet
Imports Grasshopper.Kernel
Imports Grasshopper.Kernel.Types

Namespace MyTypes
  Public Class TriStateType
    Inherits GH_Goo(Of Integer)

  End Class
End Namespace
```

</div>
</div>

### Constructors

Unless a constructor is defined, .NET classes always have a default constructor which initializes all the fields of the class to their default values.  This constructor does not require any inputs and when you develop custom types it is a good idea to always provide a default constructor.  If there is no default constructor, then class instances cannot be created automatically which thwarts certain algorithms in Grasshopper.

In addition to a default constructor I also find it useful to supply so called copy constructors which create a new instance of the type class with a preset value.

<div class="codetab">
  <button class="tablinks10" onclick="openCodeTab(event, 'cs10')" id="defaultOpen10">C#</button>
  <button class="tablinks10" onclick="openCodeTab(event, 'vb10')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content10" id="cs10">

```cs
// Default Constructor, sets the state to Unknown.
public TriStateType()
{
  this.Value = -1;
}

// Constructor with initial value
public TriStateType(int tristateValue)
{
  this.Value = tristateValue;
}

// Copy Constructor
public TriStateType(TriStateType tristateSource)
{
  this.Value = tristateSource.Value;
}

// Duplication method (technically not a constructor)
public override IGH_Goo Duplicate()
{
  return new TriStateType(this);
}

```

</div>

<div class="codetab-content10" id="vb10">

```vbnet
'' Default Constructor, sets the state to Unknown.
Public Sub New()
  Me.Value = -1
End Sub

'' Constructor with initial value
Public Sub New(ByVal tristateValue As Integer)
  Me.Value = tristateValue
End Sub

'' Copy Constructor
Public Sub New(ByVal tristateSource As TriStateType)
  Value = tristateSource.Value
End Sub

'' Duplication method (technically not a constructor)
Public Overrides Function Duplicate() As Kernel.Types.IGH_Goo
  Return New TriStateType(Me)
End Function
```

</div>
</div>

Incidentally, the Value property which we are using to assign integers to our local instance is provided by the `GH_Goo<T>` base class.  `GH_Goo<T>` defines a protected field of type `T` called `m_value` and also a public accessor property called `Value` which gets or sets the `m_value` field.

In this particular case, it actually makes sense to override the default `Value` property implementation, as the number of sensible values we can assign (-1, 0 and +1) is a subset of the total number values available through the Integer data type.  It makes no sense to assign -62 for example. We *could* of course agree that all negative values indicate an "Unknown" state, but we should try to restrict ourselves to only three integer values:

<div class="codetab">
  <button class="tablinks11" onclick="openCodeTab(event, 'cs11')" id="defaultOpen11">C#</button>
  <button class="tablinks11" onclick="openCodeTab(event, 'vb11')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content11" id="cs11">

```cs
// Override the Value property to strip non-sensical states.
public override int Value
{
  get { return base.Value; }
  set
  {
    if (value < -1) { value = -1; }
    if (value > +1) { value = +1; }
    base.Value = value;
  }
}

```

</div>

<div class="codetab-content11" id="vb11">

```vbnet
'' Override the Value property to strip non-sensical states.
Public Overrides Property Value() As Integer
  Get
    Return MyBase.Value
  End Get
  Set(ByVal value As Integer)
    If (value < -1) Then value = -1
    If (value > +1) Then value = +1
    MyBase.Value = value
  End Set
End Property
```

</div>
</div>

### Formatters

Formatting data is primarily a User Interface task.  Both the data type and the data state need to be presented in human-readable form every now and again.  This mostly involves readonly properties as looking at data does not change its state:

<div class="codetab">
  <button class="tablinks12" onclick="openCodeTab(event, 'cs12')" id="defaultOpen12">C#</button>
  <button class="tablinks12" onclick="openCodeTab(event, 'vb12')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content12" id="cs12">

```cs
// TriState instances are always valid
public override bool IsValid
{
  get { return true; }
}

// Return a string with the name of this Type.
public override string TypeName
{
  get { return "TriState"; }
}

// Return a string describing what this Type is about.
public override string TypeDescription
{
  get { return "A TriState Value (True, False or Unknown)"; }
}

// Return a string representation of the state (value) of this instance.
public override string ToString()
{
  if (this.Value == 0) { return "False"; }
  if (this.Value > 0) { return "True"; }
  return "Unknown";
}

```

</div>

<div class="codetab-content12" id="vb12">

```vbnet
'' TriState instances are always valid
Public Overrides ReadOnly Property IsValid() As Boolean
  Get
    Return True
  End Get
End Property

'' Return a string with the name of this Type.
Public Overrides ReadOnly Property TypeName() As String
  Get
    Return "TriState"
  End Get
End Property

'' Return a string describing what this Type is about.
Public Overrides ReadOnly Property TypeDescription() As String
  Get
    Return "A TriState Value (True, False or Unknown)"
  End Get
End Property

'' Return a string representation of the state (value) of this instance.
Public Overrides Function ToString() As String
  If (Value = 0) Then Return "False"
  If (Value > 0) Then Return "True"
  Return "Unknown"
End Function
```

</div>
</div>

### Serialization

Some data types can be stored as *persistent data*.  Persistent data must be able to serialize and deserialize itself from a Grasshopper file. Most simple types support this feature (Booleans, Integers, Strings, Colours, Circles, Planes etc.), most complex geometry types cannot be stored as persistent data (Curves, Breps, Meshes). If possible, you should aim to provide robust (de)serialization for your data:

<div class="codetab">
  <button class="tablinks13" onclick="openCodeTab(event, 'cs13')" id="defaultOpen13">C#</button>
  <button class="tablinks13" onclick="openCodeTab(event, 'vb13')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content13" id="cs13">

```cs
// Serialize this instance to a Grasshopper writer object.
public override bool Write(GH_IO.Serialization.GH_IWriter writer)
{
  writer.SetInt32("tri", this.Value);
  return true;
}

// Deserialize this instance from a Grasshopper reader object.
public override bool Read(GH_IO.Serialization.GH_IReader reader)
{
  this.Value = reader.GetInt32("tri");
  return true;
}

```

</div>

<div class="codetab-content13" id="vb13">

```vbnet
'' Serialize this instance to a Grasshopper writer object.
Public Overrides Function Write(ByVal writer As GH_IO.Serialization.GH_IWriter) As Boolean
  writer.SetInt32("tri", Value)
  Return True
End Function

'' Deserialize this instance from a Grasshopper reader object.
Public Overrides Function Read(ByVal reader As GH_IO.Serialization.GH_IReader) As Boolean
  Value = reader.GetInt32("tri")
  Return True
End Function
```

</div>
</div>

### Casting

There are three casting methods on `IGH_Goo`; the `CastFrom()` and `CastTo()` methods that facilitate conversions between different types of data and the `ScriptVariable()` method which creates a safe instance of this data to be used inside untrusted code (such as VB or C# Script components).

<div class="codetab">
  <button class="tablinks14" onclick="openCodeTab(event, 'cs14')" id="defaultOpen14">C#</button>
  <button class="tablinks14" onclick="openCodeTab(event, 'vb14')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content14" id="cs14">

```cs
// Return the Integer we use to represent the TriState flag.
public override object ScriptVariable()
{
  return this.Value;
}

// This function is called when Grasshopper needs to convert this
// instance of TriStateType into some other type Q.
public override bool CastTo<Q>(ref Q target)
{
  //First, see if Q is similar to the Integer primitive.
  if (typeof(Q).IsAssignableFrom(typeof(int)))
  {
    object ptr = this.Value;
    target = (Q)ptr;
    return true;
  }

  //Then, see if Q is similar to the GH_Integer type.
  if (typeof(Q).IsAssignableFrom(typeof(GH_Integer)))
  {
    object ptr = new GH_Integer(this.Value);
    target = (Q)ptr;
    return true;
  }

  //We could choose to also handle casts to Boolean, GH_Boolean,
  //Double and GH_Number, but this is left as an exercise for the reader.
  return false;
}

// This function is called when Grasshopper needs to convert other data
// into TriStateType.
public override bool CastFrom(object source)
{
  //Abort immediately on bogus data.
  if (source == null) { return false; }

  //Use the Grasshopper Integer converter. By specifying GH_Conversion.Both
  //we will get both exact and fuzzy results. You should always try to use the
  //methods available through GH_Convert as they are extensive and consistent.
  int val;
  if (GH_Convert.ToInt32(source, out val, GH_Conversion.Both))
  {
    this.Value = val;
    return true;
  }

  //If the integer conversion failed, we can still try to parse Strings.
  //If possible, you should ensure that your data type can 'deserialize' itself
  //from the output of the ToString() method.
  string str = null;
  if (GH_Convert.ToString(source, out str, GH_Conversion.Both))
  {
    switch (str.ToUpperInvariant())
    {
      case "FALSE":
      case "F":
      case "NO":
      case "N":
        this.Value = 0;
        return true;

      case "TRUE":
      case "T":
      case "YES":
      case "Y":
        this.Value = +1;
        return true;

      case "UNKNOWN":
      case "UNSET":
      case "MAYBE":
      case "DUNNO":
      case "?":
        this.Value = -1;
        return true;
    }
  }

  //We've exhausted the possible conversions, it seems that source
  //cannot be converted into a TriStateType after all.
  return false;
}

```

</div>

<div class="codetab-content14" id="vb14">

```vbnet
'' Return the Integer we use to represent the TriState flag.
Public Overrides Function ScriptVariable() As Object
  Return Value
End Function

'' This function is called when Grasshopper needs to convert this
'' instance of TriStateType into some other type Q.
Public Overrides Function CastTo(Of Q)(ByRef target As Q) As Boolean
  'First, see if Q is similar to the Integer primitive.
  If (GetType(Q).IsAssignableFrom(GetType(Integer))) Then
    Dim ptr As Object = Value
    target = DirectCast(ptr, Q)
    Return True
  End If

  'Then, see if Q is similar to the GH_Integer type.
  If (GetType(Q).IsAssignableFrom(GetType(GH_Integer))) Then
    Dim int As Object = New GH_Integer(Value)
    target = DirectCast(int, Q)
    Return True
  End If

  'We could choose to also handle casts to Boolean, GH_Boolean,
  'Double and GH_Number, but this is left as an exercise for the reader.
  Return False
End Function

'' This function is called when Grasshopper needs to convert other data
'' into TriStateType.
Public Overrides Function CastFrom(ByVal source As Object) As Boolean
  'Abort immediately on bogus data.
  If (source Is Nothing) Then Return False

  'Use the Grasshopper Integer converter. By specifying GH_Conversion.Both
  'we will get both exact and fuzzy results. You should always try to use the
  'methods available through GH_Convert as they are extensive and consistent.
  Dim int As Integer
  If (GH_Convert.ToInt32(source, int, GH_Conversion.Both)) Then
    Value = int
    Return True
  End If

  'If the integer conversion failed, we can still try to parse Strings.
  'If possible, you should ensure that your data type can 'deserialize' itself
  'from the output of the ToString() method.
  Dim str As String = Nothing
  If (GH_Convert.ToString(source, str, GH_Conversion.Both)) Then
    Select Case str.ToUpperInvariant()
      Case "FALSE", "F", "NO", "N"
        Value = 0
        Return True
      Case "TRUE", "T", "YES", "Y"
        Value = +1
        Return True
      Case "UNKNOWN", "UNSET", "MAYBE", "DUNNO", "?"
        Value = -1
        Return True
    End Select
  End If

  'We've exhausted the possible conversions, it seems that source
  'cannot be converted into a TriStateType after all.
  Return False
End Function
```

</div>
</div>

## Related Topics

- [Grasshopper Data Types](/guides/grasshopper/grasshopper-data-types)
- [Simple Component](/guides/grasshopper/simple-component)
- [Simple Parameters](/guides/grasshopper/simple-parameters)

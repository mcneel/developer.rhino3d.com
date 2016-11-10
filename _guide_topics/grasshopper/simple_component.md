---
title: Simple Component
description: This guide gives an exhaustive, step by step explanation of how to build a simple Grasshopper component.
authors: ['David Rutten']
author_contacts: ['DavidRutten']
apis: ['Grasshopper']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm
order: 1
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Prerequisites

This guide presumes you have all the necessary tools installed and have managed to debug a simple boilerplate component.  If you are not there yet, please read [Installing Tools (Windows)]({{ site.baseurl }}/guides/grasshopper/installing_tools_windows/) and [Your First Component (Windows)]({{ site.baseurl }}/guides/grasshopper/your_first_component_windows)

This guide will skip over any complicated issues (such as mathematics, geometry and data handling) in order to reduce the totality of new concepts.  You will however need to have a good understanding of basic OOP concepts such as classes, types and inheritance.  If you do not understand these essentials, we recommend you start with [some other reading material first]({{ site.baseurl }}/guides/general/rhino_developer_prerequisites/#programming-knowledge).

## Kernel.GH_Component

The Grasshopper component wizards (in both Visual Studio and Xamarin Studio) include an empty Grasshopper component template.  For the moment, let's ignore this and construct a simple component "from scratch."  This guide presumes that you already have a component library setup or are continuing from in the *HelloGrasshopper* solution from the [Your First Component (Windows)]({{ site.baseurl }}/guides/grasshopper/your_first_component_windows) guide.

Add an empty class to your solution, call it *MyFirstComponent*.  At this point a new file should be created (*MyFirstComponent*).  At this point a new file should be created with (something close to) the following content:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs" data-toggle="pill">C#</a></li>
  <li><a href="#vb" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace HelloGrasshopper
{
    class MyFirstComponent
    {
    }
}
```
{: #cs .tab-pane .fade .in .active}

```vbnet
Class MyFirstComponent

End Class
```
{: #vb .tab-pane .fade .in}

</div>

Since we'll be using primarily types from the `Grasshopper.Kernel` namespace.  We'll import this namespace so that we have easy access to all types contained within it (unless otherwise specified, all further types discussed in this topic belong to `Grasshopper.Kernel`).  In C#, we can also remove some unnecessary using statements while we're at it:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs1" data-toggle="pill">C#</a></li>
  <li><a href="#vb1" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
using System;
using Grasshopper.Kernel;

namespace HelloGrasshopper
{
    class MyFirstComponent
    {
    }
}
```
{: #cs1 .tab-pane .fade .in .active}

```vbnet
Imports Grasshopper.Kernel
Class MyFirstComponent

End Class
```
{: #vb1 .tab-pane .fade .in}

</div>

The idea is that this class will be loaded by Grasshopper whenever this component library is loaded, but in order for that to happen we must make sure that this class is "visible" from outside this project. I.e., we need to make the accessor "public":

<ul class="nav nav-pills">
  <li class="active"><a href="#cs2" data-toggle="pill">C#</a></li>
  <li><a href="#vb2" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
using System;
using Grasshopper.Kernel;

namespace HelloGrasshopper
{
  // If a class is not public, it won't be visible
  // from where Grasshopper is sitting.
  public class MyFirstComponent
  {
  }
}
```
{: #cs2 .tab-pane .fade .in .active}

```vbnet
Imports Grasshopper.Kernel
Public Class MyFirstComponent

End Class
```
{: #vb2 .tab-pane .fade .in}

</div>

Now, we need to derive our `MyFirstComponent` class from the [GH_Component]({{ site.baseurl }}/api/grasshopper/html/T_Grasshopper_Kernel_GH_Component.htm) base class defined inside Grasshopper.  `GH_Component` takes care of almost all the complicated actions and mannerisms that constitute a component.  It will handle data conversion, GUI, menus, file Input/Output, Error trapping and much, much more.  This allows us to focus only on the unique aspects of our component. In order to derive from `GH_Component`, add this to the class...

<ul class="nav nav-pills">
  <li class="active"><a href="#cs3" data-toggle="pill">C#</a></li>
  <li><a href="#vb3" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
using System;
using Grasshopper.Kernel;

namespace HelloGrasshopper
{
  public class MyFirstComponent : GH_Component
  {
  }
}
```
{: #cs3 .tab-pane .fade .in .active}

```vbnet
Imports Grasshopper.Kernel
Public Class MyFirstComponent
  Inherits GH_Component

End Class
```
{: #vb3 .tab-pane .fade .in }

</div>

Deriving (inheriting) from `GH_Component` requires you to implement a number of methods.  (Visual Studio can insert default implementations for all of these via the *Implement Abstract Class* menu option when right-clicking `GH_Component`.  In Xamarin Studio, you can right-click `GH_Component` and select *Refactoring* > *Implement abstract members*.)  At this point, you should have the following...

<ul class="nav nav-pills">
  <li class="active"><a href="#cs4" data-toggle="pill">C#</a></li>
  <li><a href="#vb4" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
using System;
using Grasshopper.Kernel;

namespace HelloGrasshopper
{
  public class MyFirstComponent : GH_Component
  {
    protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
    {
      throw new NotImplementedException();
    }

    protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
    {
      throw new NotImplementedException();
    }

    protected override void SolveInstance(IGH_DataAccess DA)
    {
      throw new NotImplementedException();
    }

    public override Guid ComponentGuid
    {
      get { throw new NotImplementedException(); }
    }
  }
}
```
{: #cs4 .tab-pane .fade .in .active}

```vbnet
Imports Grasshopper.Kernel
Public Class MyFirstComponent
  Inherits GH_Component

  Protected Overrides Sub RegisterInputParams(ByVal pManager As GH_Component.GH_InputParamManager)
    'Don't worry about this just yet!
  End Sub

  Protected Overrides Sub RegisterOutputParams(ByVal pManager As GH_Component.GH_OutputParamManager)
    'We'll get to it soon enough.
  End Sub

  Protected Overrides Sub SolveInstance(ByVal DA As IGH_DataAccess)
    'I know it all looks scary.
  End Sub

  Public Overrides ReadOnly Property ComponentGuid() As System.Guid
    Get
      'But we'll deal with it one item at a time.  
    End Get
  End Property
End Class
```
{: #vb4 .tab-pane .fade .in }

</div>

## The Component Constructor

As we've seen in the previous section, Visual Studio (or Xamarin Studio) can populate the `MyFirstComponent` class with a collection of properties and methods that we need to implement.  There is however another method that requires our attention that is missing.  This is the constructor.  The constructor is a special method inside each class which gets called when the class is instantiated (or "constructed").  This can happen only once (we feeble humans can only be born once as well after all) and it necessarily happens before anything else is allowed to happen. The `GH_Component` base class has a constructor which is not empty, so we have to call that constructor from within our constructor and supply it with all the information it needs.  Add the following code near the top of the `MyFirstComponent` class...

<ul class="nav nav-pills">
  <li class="active"><a href="#cs5" data-toggle="pill">C#</a></li>
  <li><a href="#vb5" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
using System;
using Grasshopper.Kernel;

namespace HelloGrasshopper
{
  public class MyFirstComponent : GH_Component
  {
    public MyFirstComponent() : base("MyFirst", "MFC", "My first component", "Extra", "Simple")
    {
    }
  ...
```
{: #cs5 .tab-pane .fade .in .active}

```vbnet
Imports Grasshopper.Kernel
Public Class MyFirstComponent
  Inherits GH_Component

  Public Sub New()
    MyBase.New("MyFirst", "MFC", "My first component", "Extra", "Simple")
  End Sub

  ...
```
{: #vb5 .tab-pane .fade .in }

</div>

As you can see we need to supply a set of text constants, which are used to name and identify our component within the Grasshopper GUI.  The text fields are...

- *name* is the name of our component. The name is what appears on tooltips and panel dropdowns.
- *abbreviation* is the abbreviation of our component.  The abbreviation is what is written on the component once it appears on the canvas.
- *description* is a description of our component. The description is used on tooltips to provide users with a more detailed idea about what this component is for.
- *category* is the tab category for the component. The category equals the name of the tab onto which the component will appear. If a non-existing category is supplied, a new Tab will be added to the Grasshopper GUI.

![Component labels]({{ site.baseurl }}/images/simple_component_01.png)

## Component Guids

Every type of object inside a Grasshopper document must have a `ComponentGuid` associated with it.  When a Grasshopper file (\**.gh* or \**.ghx*) is written these Guids are used as markers, so it becomes clear what portions of the file belong to which object.  When the file is read back in, that marker is compared against the list of all cached components and if a match is found the appropriate component is asked to deserialize itself from the appropriate file portion.  When no matching component can be found it is assumed that whoever wrote the file had access to certain components that are not available locally, and that portion of the file is dutifully skipped.

So, long story short, we need to invent a Guid (Globally Unique IDentifier) that will positively and unerringly indicate *this* component.  You can generate new Guids using an [Online Guid Generator](https://www.guidgenerator.com/) or Microsoft's popular *guidgen.exe*.  **Never** re-use a Guid and **never** edit one by hand.  Always generate a proper one using an official tool.

Once you have a new Guid standing by, modify the [ComponentGuid]({{ site.baseurl }}/api/grasshopper/html/P_Grasshopper_Kernel_IGH_DocumentObject_ComponentGuid.htm) property to return it:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs6" data-toggle="pill">C#</a></li>
  <li><a href="#vb6" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
public override Guid ComponentGuid
{
  // Don't copy this GUID, make a new one
  get { return new Guid("419c3a3a-cc48-4717-8cef-5f5647a5ecfc"); }
}
...
```
{: #cs6 .tab-pane .fade .in .active}

```vbnet
...
Public Overrides ReadOnly Property ComponentGuid() As System.Guid
  Get
    'Don't copy this GUID, make a new one
    Return New Guid("419c3a3a-cc48-4717-8cef-5f5647a5ecfc")  
  End Get
End Property
...
```
{: #vb6 .tab-pane .fade .in }

</div>

## Parameter Registration

Components have unique input and output parameters which are most often fixed.  We are ignoring those rare cases where a component either has no inputs or no outputs, or where there is a variable number of parameters.  There are two methods that allow you to define (or "register") these parameters.  These routines are called from within the base class constructor and they are only called once.  Let's have a look at the default implementation again:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs7" data-toggle="pill">C#</a></li>
  <li><a href="#vb7" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
{
  throw new NotImplementedException();
}

protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
{
  throw new NotImplementedException();
}
...
```
{: #cs7 .tab-pane .fade .in .active}

```vbnet
...
Protected Overrides Sub RegisterInputParams(ByVal pManager As GH_Component.GH_InputParamManager)

End Sub

Protected Overrides Sub RegisterOutputParams(ByVal pManager As GH_Component.GH_OutputParamManager)

End Sub
...
```
{: #vb7 .tab-pane .fade .in }

</div>

Although it would technically be possible to manually register parameters, we highly recommend you use the methods on `pManager`.  `pManager` has methods for adding all the basic parameter types and it often even allows you to specify default values.

In this example we'll only create two parameters (one input, one output) and they will both be of type `String`...

<ul class="nav nav-pills">
  <li class="active"><a href="#cs8" data-toggle="pill">C#</a></li>
  <li><a href="#vb8" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
{
  pManager.AddTextParameter("String", "S", "String to reverse", GH_ParamAccess.item);
}

protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
{
  pManager.AddTextParameter("Reverse", "R", "Reversed string", GH_ParamAccess.item);
}
...
```
{: #cs8 .tab-pane .fade .in .active}

```vbnet
...
Protected Overrides Sub RegisterInputParams(ByVal pManager As Grasshopper.Kernel.GH_Component.GH_InputParamManager)
  pManager.AddTextParameter("String", "S", "String to reverse")
End Sub

Protected Overrides Sub RegisterOutputParams(ByVal pManager As Grasshopper.Kernel.GH_Component.GH_OutputParamManager)
  pManager.AddTextParameter("Reverse", "R", "Reversed string")
End Sub
...
```
{: #vb8 .tab-pane .fade .in }

</div>

When we compile this project (assuming it has been setup correctly), the component will already be available on the Grasshopper tabs and it can be placed onto the canvas:

![Sanity Check]({{ site.baseurl }}/images/simple_component_02.png)

## The Solver Routine

Our new component sure looks perky and expensive, but it doesn't do anything yet.  We still need to write the contents of the `SolveInstance()` subroutine, which is where all the action takes place.  The `SolveInstance()` method is called upon whenever the component needs to handle input data.  In this particular example, if we plug a list of twelve strings into the `[S]` parameter, `SolveInstance()` will be called twelve times.

As you may already have guessed, the component we're writing will reverse a given textual string from `[S]` and output the result to `[R]`. Since we're operating on individual items of data (the default behaviour), all we need to do inside the `SolveInstance()` function is retrieve the current String from `[S]`, reverse it and assign it to `[R]`.  Now, String reversal is not a function that is directly available in the framework `String` type, so we need to actually do some thinking:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs9" data-toggle="pill">C#</a></li>
  <li><a href="#vb9" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">


```cs
...
protected override void SolveInstance(IGH_DataAccess DA)
{
  // Declare a variable for the input String
  string data = null;

  // Use the DA object to retrieve the data inside the first input parameter.
  // If the retieval fails (for example if there is no data) we need to abort.
  if (!DA.GetData(0, ref data)) { return; }

  // If the retrieved data is Nothing, we need to abort.
  // We're also going to abort on a zero-length String.
  if (data == null) { return; }
  if (data.Length == 0) { return; }

  // Convert the String to a character array.
  char[] chars = data.ToCharArray();

  // Reverse the array of character.
  System.Array.Reverse(chars);

  // Use the DA object to assign a new String to the first output parameter.
  DA.SetData(0, new string(chars));
}
...
```
{: #cs9 .tab-pane .fade .in .active}

```vbnet
...
Protected Overrides Sub SolveInstance(ByVal DA As Grasshopper.Kernel.IGH_DataAccess)
  'Declare a variable for the input String
  Dim data As String = Nothing

  'Use the DA object to retrieve the data inside the first input parameter.
  'If the retieval fails (for example if there is no data) we need to abort.
  If (Not DA.GetData(0, data)) Then Return

  'If the retrieved data is Nothing, we need to abort.
  'We're also going to abort on a zero-length String.
  If (data Is Nothing) Then Return
  If (data.Length = 0) Then Return

  'Convert the String to a character array.
  Dim chars As Char() = data.ToCharArray()

  'Reverse the array of character.
  Array.Reverse(chars)

  'Use the DA object to assign a new String to the first output parameter.
  DA.SetData(0, New String(chars))
End Sub
...
```
{: #vb9 .tab-pane .fade .in }

</div>

Build, run, and ...

![That was easy]({{ site.baseurl }}/images/simple_component_03.png)

**DONE!**

You have just built your first Grasshopper component from the ground up.  **Now what?**

---

## Next Steps

Now that you have built a component from scratch, let's discuss parameter order, default values for inputs, and go a little further in depth.  Next, check out the [Simple Mathematics Component]({{ site.baseurl }}/guides/grasshopper/simple_mathematics_component) guide.

---

## Related Topics

- [What is a Grasshopper Component?]({{ site.baseurl }}/guides/grasshopper/what_is_a_grasshopper_component)
- [Installing Tools (Windows)]({{ site.baseurl }}/guides/grasshopper/installing_tools_windows/)
- [Your First Component (Windows)]({{ site.baseurl }}/guides/grasshopper/your_first_component_windows)
- [Simple Mathematics Component]({{ site.baseurl }}/guides/grasshopper/simple_mathematics_component)
- [Simple Geometry Component]({{ site.baseurl }}/guides/grasshopper/simple_geometry_component)
- [Simple Data Types]({{ site.baseurl }}/guides/grasshopper/simple_data_types)
- [Simple Parameters]({{ site.baseurl }}/guides/grasshopper/simple_parameters)
- [Custom Component Options]({{ site.baseurl }}/guides/grasshopper/custom_component_options)

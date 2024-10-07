+++
aliases = ["/en/5/guides/grasshopper/simple-component/", "/en/6/guides/grasshopper/simple-component/", "/en/7/guides/grasshopper/simple-component/", "/en/wip/guides/grasshopper/simple-component/"]
authors = [ "david" ]
categories = [ "Fundamentals" ]
description = "This guide gives an exhaustive, step by step explanation of how to build a simple Grasshopper component."
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#", "VB" ]
sdk = [ "Grasshopper" ]
title = "Simple Component"
type = "guides"
weight = 1
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


## Prerequisites

This guide presumes you have all the necessary tools installed and have managed to debug a simple boilerplate component.  If you are not there yet, please read [Installing Tools (Windows)](/guides/grasshopper/installing-tools-windows/) and [Your First Component (Windows)](/guides/grasshopper/your-first-component-windows)

This guide will skip over any complicated issues (such as mathematics, geometry and data handling) in order to reduce the totality of new concepts.  You will however need to have a good understanding of basic OOP concepts such as classes, types and inheritance.  If you do not understand these essentials, we recommend you start with [some other reading material first](/guides/general/rhino-developer-prerequisites/#programming-knowledge).

## Kernel.GH_Component

The Grasshopper component wizards (in both Visual Studio for Windows and Visual Studio for Mac) include an empty Grasshopper component template.  For the moment, let's ignore this and construct a simple component "from scratch."  This guide presumes that you already have a component library setup or are continuing from in the *HelloGrasshopper* solution from the [Your First Component (Windows)](/guides/grasshopper/your-first-component-windows) guide.

Add an empty class to your solution, call it *MyFirstComponent*.  At this point a new file should be created (*MyFirstComponent*).  At this point a new file should be created with (something close to) the following content:

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'vb')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content" id="cs">

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

</div>

<div class="codetab-content" id="vb">

```vbnet
Class MyFirstComponent

End Class
```

</div>
</div>

Since we'll be using primarily types from the `Grasshopper.Kernel` namespace.  We'll import this namespace so that we have easy access to all types contained within it (unless otherwise specified, all further types discussed in this topic belong to `Grasshopper.Kernel`).  In C#, we can also remove some unnecessary using statements while we're at it:

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'vb1')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content1" id="cs1">

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

</div>

<div class="codetab-content1" id="vb1">

```vbnet
Imports Grasshopper.Kernel
Class MyFirstComponent

End Class
```

</div>
</div>

The idea is that this class will be loaded by Grasshopper whenever this component library is loaded, but in order for that to happen we must make sure that this class is "visible" from outside this project. I.e., we need to make the accessor "public":

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'vb2')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content2" id="cs2">

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

</div>

<div class="codetab-content2" id="vb2">

```vbnet
Imports Grasshopper.Kernel
Public Class MyFirstComponent

End Class
```

</div>
</div>

Now, we need to derive our `MyFirstComponent` class from the [GH_Component](/api/grasshopper/html/T_Grasshopper_Kernel_GH_Component.htm) base class defined inside Grasshopper.  `GH_Component` takes care of almost all the complicated actions and mannerisms that constitute a component.  It will handle data conversion, GUI, menus, file Input/Output, Error trapping and much, much more.  This allows us to focus only on the unique aspects of our component. In order to derive from `GH_Component`, add this to the class...

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'vb3')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content3" id="cs3">

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

</div>

<div class="codetab-content3" id="vb3">

```vbnet
Imports Grasshopper.Kernel
Public Class MyFirstComponent
  Inherits GH_Component

End Class
```

</div>
</div>

Deriving (inheriting) from `GH_Component` requires you to implement a number of methods.  (Visual Studio can insert default implementations for all of these via the *Implement Abstract Class* menu option when right-clicking `GH_Component`.  In Visual Studio for Mac, you can right-click `GH_Component` and select *Refactoring* > *Implement abstract members*.)  At this point, you should have the following...

<div class="codetab">
  <button class="tablinks4" onclick="openCodeTab(event, 'cs4')" id="defaultOpen4">C#</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'vb4')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content4" id="cs4">

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

</div>

<div class="codetab-content4" id="vb4">

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

</div>
</div>

## The Component Constructor

As we've seen in the previous section, Visual Studio can populate the `MyFirstComponent` class with a collection of properties and methods that we need to implement.  There is however another method that requires our attention that is missing.  This is the constructor.  The constructor is a special method inside each class which gets called when the class is instantiated (or "constructed").  This can happen only once (we feeble humans can only be born once as well after all) and it necessarily happens before anything else is allowed to happen. The `GH_Component` base class has a constructor which is not empty, so we have to call that constructor from within our constructor and supply it with all the information it needs.  Add the following code near the top of the `MyFirstComponent` class...

<div class="codetab">
  <button class="tablinks5" onclick="openCodeTab(event, 'cs5')" id="defaultOpen5">C#</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'vb5')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content5" id="cs5">

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

</div>

<div class="codetab-content5" id="vb5">

```vbnet
Imports Grasshopper.Kernel
Public Class MyFirstComponent
  Inherits GH_Component

  Public Sub New()
    MyBase.New("MyFirst", "MFC", "My first component", "Extra", "Simple")
  End Sub

  ...
```

</div>
</div>

As you can see we need to supply a set of text constants, which are used to name and identify our component within the Grasshopper GUI.  The text fields are...

- *name* is the name of our component. The name is what appears on tooltips and panel dropdowns.
- *abbreviation* is the abbreviation of our component.  The abbreviation is what is written on the component once it appears on the canvas.
- *description* is a description of our component. The description is used on tooltips to provide users with a more detailed idea about what this component is for.
- *category* is the tab category for the component. The category equals the name of the tab onto which the component will appear. If a non-existing category is supplied, a new Tab will be added to the Grasshopper GUI.

![Component labels](/images/simple-component-01.png)

## Component Guids

Every type of object inside a Grasshopper document must have a `ComponentGuid` associated with it.  When a Grasshopper file (\**.gh* or \**.ghx*) is written these Guids are used as markers, so it becomes clear what portions of the file belong to which object.  When the file is read back in, that marker is compared against the list of all cached components and if a match is found the appropriate component is asked to deserialize itself from the appropriate file portion.  When no matching component can be found it is assumed that whoever wrote the file had access to certain components that are not available locally, and that portion of the file is dutifully skipped.

So, long story short, we need to invent a Guid (Globally Unique IDentifier) that will positively and unerringly indicate *this* component.  You can generate new Guids using an [Online Guid Generator](https://www.guidgenerator.com/) or Microsoft's popular *guidgen.exe*.  **Never** re-use a Guid and **never** edit one by hand.  Always generate a proper one using an official tool.

Once you have a new Guid standing by, modify the [ComponentGuid](/api/grasshopper/html/P_Grasshopper_Kernel_IGH_DocumentObject_ComponentGuid.htm) property to return it:

<div class="codetab">
  <button class="tablinks6" onclick="openCodeTab(event, 'cs6')" id="defaultOpen6">C#</button>
  <button class="tablinks6" onclick="openCodeTab(event, 'vb6')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content6" id="cs6">

```cs
...
public override Guid ComponentGuid
{
  // Don't copy this GUID, make a new one
  get { return new Guid("419c3a3a-cc48-4717-8cef-5f5647a5ecfc"); }
}
...

```

</div>

<div class="codetab-content6" id="vb6">

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

</div>
</div>

## Parameter Registration

Components have unique input and output parameters which are most often fixed.  We are ignoring those rare cases where a component either has no inputs or no outputs, or where there is a variable number of parameters.  There are two methods that allow you to define (or "register") these parameters.  These routines are called from within the base class constructor and they are only called once.  Let's have a look at the default implementation again:

<div class="codetab">
  <button class="tablinks7" onclick="openCodeTab(event, 'cs7')" id="defaultOpen7">C#</button>
  <button class="tablinks7" onclick="openCodeTab(event, 'vb7')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content7" id="cs7">

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

</div>

<div class="codetab-content7" id="vb7">

```vbnet
...
Protected Overrides Sub RegisterInputParams(ByVal pManager As GH_Component.GH_InputParamManager)

End Sub

Protected Overrides Sub RegisterOutputParams(ByVal pManager As GH_Component.GH_OutputParamManager)

End Sub
...
```

</div>
</div>

Although it would technically be possible to manually register parameters, we highly recommend you use the methods on `pManager`.  `pManager` has methods for adding all the basic parameter types and it often even allows you to specify default values.

In this example we'll only create two parameters (one input, one output) and they will both be of type `String`...

<div class="codetab">
  <button class="tablinks8" onclick="openCodeTab(event, 'cs8')" id="defaultOpen8">C#</button>
  <button class="tablinks8" onclick="openCodeTab(event, 'vb8')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content8" id="cs8">

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

</div>

<div class="codetab-content8" id="vb8">

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

</div>
</div>

When we compile this project (assuming it has been setup correctly), the component will already be available on the Grasshopper tabs and it can be placed onto the canvas:

![Sanity Check](/images/simple-component-02.png)

## The Solver Routine

Our new component sure looks perky and expensive, but it doesn't do anything yet.  We still need to write the contents of the `SolveInstance()` subroutine, which is where all the action takes place.  The `SolveInstance()` method is called upon whenever the component needs to handle input data.  In this particular example, if we plug a list of twelve strings into the `[S]` parameter, `SolveInstance()` will be called twelve times.

As you may already have guessed, the component we're writing will reverse a given textual string from `[S]` and output the result to `[R]`. Since we're operating on individual items of data (the default behaviour), all we need to do inside the `SolveInstance()` function is retrieve the current String from `[S]`, reverse it and assign it to `[R]`.  Now, String reversal is not a function that is directly available in the framework `String` type, so we need to actually do some thinking:

<div class="codetab">
  <button class="tablinks9" onclick="openCodeTab(event, 'cs9')" id="defaultOpen9">C#</button>
  <button class="tablinks9" onclick="openCodeTab(event, 'vb9')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content9" id="cs9">

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

</div>

<div class="codetab-content9" id="vb9">

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

</div>
</div>

Build, run, and ...

![That was easy](/images/simple-component-03.png)

**DONE!**

You have just built your first Grasshopper component from the ground up.  **Now what?**

## Next Steps

Now that you have built a component from scratch, let's discuss parameter order, default values for inputs, and go a little further in depth.  Next, check out the [Simple Mathematics Component](/guides/grasshopper/simple-mathematics-component) guide.

## Related Topics

- [What is a Grasshopper Component?](/guides/grasshopper/what-is-a-grasshopper-component)
- [Installing Tools (Windows)](/guides/grasshopper/installing-tools-windows/)
- [Your First Component (Windows)](/guides/grasshopper/your-first-component-windows)
- [Simple Mathematics Component](/guides/grasshopper/simple-mathematics-component)
- [Simple Geometry Component](/guides/grasshopper/simple-geometry-component)
- [Simple Data Types](/guides/grasshopper/simple-data-types)
- [Simple Parameters](/guides/grasshopper/simple-parameters)
- [Custom Component Options](/guides/grasshopper/custom-component-options)

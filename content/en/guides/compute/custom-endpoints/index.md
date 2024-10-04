+++
aliases = ["/en/5/guides/compute/custom-endpoints/", "/en/6/guides/compute/custom-endpoints/", "/en/7/guides/compute/custom-endpoints/", "/wip/guides/compute/custom-endpoints/"]
authors = [ "steve", "will" ]
categories = [ "Getting Started" ]
description = "Extending Compute with custom endpoints"
keywords = [ "developer", "compute", "plug-in" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Extending Compute with Custom Endpoints"
type = "guides"
weight = 10
override_last_modified = "2021-02-03T14:08:07Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

<!-- originally posted to discourse: https://discourse.mcneel.com/t/extending-rhinocompute-server-with-plugins/84266 -->

By default Compute exposes a long list of endpoints, designed to expose functionality in RhinoCommon as well as enabling Grasshopper definitions and Python scripts to be solved. It's also possible to extend Compute with your own custom endpoints by registering functions in a Rhino plug-in. Compute handles the serialization.

First define a static class in your plug-in and add the new function as a static method (you can add more than one!).

```csharp
static class MyCustomComputeFunctions
{
  public static double Add(double, x, double y, double z) { return x+y+z; }

  public static double AdjustedArea(Curve curve, double adjuster)
  {
    var amp = Rhino.Geometry.AreaMassProperties.Compute(curve);
    return amp.Area * adjuster;
  }
}
```

Then, in the `OnLoad` method of the plug-in's `PlugIn` class, register the function. This code is called once when the plug-in is loaded by Rhino.

```csharp
protected override LoadReturnCode OnLoad(ref string errorMessage)
{
  Rhino.Runtime.HostUtils.RegisterComputeEndPoint("Rhino.CustomEndPoint", typeof(MyCustomComputeFunctions));

  return base.OnLoad(ref errorMessage);
}
```

You will need to install your plug-in in Rhino, both locally for testing and on any servers where Compute runs.

Once this is complete, you should be able to open the `/sdk` endpoint in a browser and see the new functions listed at the bottom of the page.

{{< call-out "note" "Note" >}}
Check out the <a href="https://github.com/mcneel/rhino-developer-samples/tree/7/compute/cs/ComputePlugIn" class="alert-link">ComputePlugIn sample</a> in the Rhino Developer Samples repository.
{{< /call-out >}}
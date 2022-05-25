+++
authors = [ "dalelear" ]
categories = [ "Fundamentals" ]
description = "This guide demonstrates how to convert openNURBS Lightweight Extrusion objects into Breps for importing."
keywords = [ "openNURBS", "Extrusions", "Importing" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS" ]
title = "Importing Lightweight Extrusions"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/onextrusion"
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

 
## Question

I was try to add some code for handling the `ON::extrusion_object` type object. But, I don't now know which API I could use to get data from extrusion object. I know there was a new class `ON_Extrusion` in *opennurbs_beam.cpp*. But I did not know how to use it.  Can you give me some suggestion or some sample code?  I would like know how should I import extrusion object?

## Answer

In most cases, you will want to convert the extrusion object to a Brep and then just pass the Brep to the Brep handling code that you've already written, for example:

```cpp
ONX_Model model = ...

ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
const ON_ModelComponent* model_component = nullptr;
for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
{
  const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
  if (nullptr != model_geometry)
  {
    // Test for extrusion object
    const ON_Extrusion* extrusion = ON_Extrusion::Cast(model_geometry->Geometry(nullptr));
    if (nullptr != extrusion)
    {
      ON_Brep* brep = ON_Brep::New();
      if (brep != extrusion->BrepForm(brep, true))
      {
        delete brep; // don't leak...
        continue;
      }

      // TODO: do something with Brep here...

      delete brep; // don't leak...
    }
  }
}
```

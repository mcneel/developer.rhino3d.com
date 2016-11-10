---
title: Importing Lightweight Extrusions
description: This guide demonstrates how to convert openNURBS Lightweight Extrusion objects into Breps for importing.
authors: ['Dale Lear']
author_contacts: ['dalelear']
apis: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/onextrusion
order: 1
keywords: ['openNURBS', 'Extrusions', 'Importing']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Question

I was try to add some code for handling the `ON::extrusion_object` type object. But, I don't now know which API I could use to get data from extrusion object. I know there was a new class `ON_Extrusion` in *opennurbs_beam.cpp*. But I did not know how to use it.  Can you give me some suggestion or some sample code?  I would like know how should I import extrusion object?

## Answer

In most cases, you will want to convert the extrusion object to a Brep and then just pass the Brep to the Brep handling code that you've already written, for example:

```cpp
int i = 0;
for( i = 0; i < model.m_object_table.Count(); i++ )
{
  const ONX_Model_Object& model_object = model.m_object_table[i];
  if( 0 == model_object.m_object )
    continue;

  if( ON::extrusion_object != model_object.m_object->ObjectType() )
    continue;

  const ON_Extrusion* extrusion = ON_Extrusion::Cast( model_object.m_object );
  if( 0 == extrusion )
    continue;

  ON_Brep* brep = ON_Brep::New();
  if( 0 == brep )
    continue;

  if( brep != extrusion->BrepForm(brep, true) )
  {
    delete brep; // don't leak...
    continue;
  }

  // TODO: do something with brep here...

  delete brep; // don't leak...
}
```

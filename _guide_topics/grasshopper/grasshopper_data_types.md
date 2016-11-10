---
title: Grasshopper Data Types
description: This guide covers the basic data types that Grasshopper deals with.
authors: ['David Rutten']
author_contacts: ['DavidRutten']
apis: ['Grasshopper']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['In Depth']
origin: http://www.grasshopper3d.com/forum/topics/grasshopper-data-types
order: 1
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Overview

Grasshopper is an application that deals with a lot of different types of data.  These data types can come from 6 different sources and some of them will not be known when Grasshopper is written and compiled.  The six potential sources are:

1. Primitive types such as `Booleans`, `Integers`, `Colors`, `Strings`, etc. Grasshopper uses these types itself a lot.
1. Other .NET Framework types such as `System.Drawing.PointF` or `System.Collections.Generic.HashSet<T>`. Grasshopper does not use these types to during component-to-component communication, but someone else might.
1. RhinoCommon types such as `Point3d`, `Circle`, `Plane`, `Brep`, `Curve` etc. Many of these are used natively, but certainly not all of them.
1. Types defined in Grasshopper itself.
1. Types defined in components for Grasshopper.
1. Types defined in VB/C#/Python scripts that run inside Grasshopper.

## What to do with unknowns?

Although clearly some of these are known to the developer during the time of writing, not all of them can be.  Yet Grasshopper still needs to be able to interpret and use types it may know nothing about. Some of the things Grasshopper needs to be able to do with data of any type are:

1. Convert it to text so tooltips and panels can be populated with *useful* descriptions of data.
1. Convert it to and from other types.
1. Duplicate data so we can change it without affecting the original.
1. Test data for validity.
1. Save types to *\*.gh* files and load them back in. (note: this works especially poorly at the moment.)
1. Preview geometric types in the viewport.
1. Bake geometric types to the Rhino document.
1. Transform geometric types.
1. Calculate bounding boxes of geometric types.
1. Be able to store null states of each type.

To overcome the problem of (A) needing to do so many things while (B) knowing nothing about the types in advance an interface is defined in the Grasshopper SDK and all data which is stored inside parameters must implement this interface.  This allows Grasshopper to do the things from the second list to all the types from the first list.

## Goo

The `IGH_Goo` interface is is usually nothing more than a wrapper around the actual data which provides a bunch of functionality for whatever it wraps. For example take the primitive `Boolean` (or `bool` in C#).  It's a structure so it can never be null, and it can only exist in either a *true* or a *false* state.

Grasshopper uses booleans a lot so it provides an `IGH_Goo` implementation for `Boolean`. This wrapper class tells Grasshopper that a boolean value can be converted into an integer (false -> 0, true -> 1), into a colour (false -> black, true -> white), into a string (false -> "false", true -> "true") and so on. The wrapper class also knows how to write and read boolean values to and from *\*.gh* files, and because we're now dealing with a wrapper class we can have null instances in a collection of boolean values.  The wrapper *doesn't* tell Grasshopper how to preview or bake booleans, because booleans are not a geometric type of data.

Because so many data types are not in any way geometric, there is a second interface called `IGH_GeometricGoo` which extends `IGH_Goo` with stuff like transforming, bounding-boxing etc.

*Almost always* component developers and scripters can ignore any of the `IGH_Goo` types, because they are mostly used for internal bookkeeping.  However sometimes a developer will either want to access the functionality that goo provides or they wish to inject a new, previously unknown type of data into a Grasshopper file. In these cases some knowledge of `IGH_Goo` and its derived interface and classes is required.

## Conversion Methods

IGH_Goo requires that the implementor provides three different conversion methods:

1. `CastFrom`
1. `CastTo`
1. `ScriptVariable`

As an elucidation, imagine the following conversation going on between Grasshopper (G), which is trying to push data of type A in one parameter into another parameter which only accepts data of type B...

G:

> "Hmm, two parameters that both store different types have been connected with a wire. That means the user wants to transfer all data from left to right, but I can't simply copy it because the parameter on the right only accepts instances of type B.

> First let me check if A is a more derived type of B, in which case I can just 'trick' the parameter into accepting the original data."

>"Nope, A is not a special flavour of B, which means some conversion needs to happen first...   Hey! You there! Mr. A! I need to move you over to this other place but they don't take kindly to the likes of you. Is there any way I can persuade you to turn yourself into something more B-like?"

A:

> "Oh sorry, I have never heard of this B-thing you mentioned before, afraid I can't help you out here."

G:

> "Never mind, I'll ask over there. Oy, B-man! Any chance of you letting me in on the secret about how to take this A thing over there and turn it into a B thing?"

B:

> "Yeah I know how to do that, but you'll lose some information in the process."

G:

> "That's all right, something's better than nothing."

B:

> "All right, here you go, a B-ified version of the A data which is the best I can do under these imperfect circumstances."

G:

> "Thanks! I'll put it into this data tree over here right away."


More succinctly, Grasshopper calls the `CastTo<B>` method on the instance of A, asking it if it knows how to convert itself into a B type.  If that fails, it'll construct a new empty B instance and ask it using the `CastFrom<A>` method whether it knows how to interpret the A data and mimic it.  If both these methods fail then Grasshopper will put up an error and leave that slot blank.

The `ScriptVariable` method allows data to protect itself from potentially ill-informed programmers.  Using this method, Grasshopper tells some data that it's about to be handed over to a script (ie. a VB/C#/Python component) and whether it would like to maybe provide a different kind of data instead.  For example a `GH_Boolean` might assume that the scripter does't really care for all that `IGH_Goo` malarkey and instead of pumping a `GH_Boolean` instance into a script just the value on the inside is provided.

---

## Related Topics

- [Simple Data Types]({{ site.baseurl }}/guides/grasshopper/simple_data_types)

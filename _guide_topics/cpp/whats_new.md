---
title: What's New?
description: This brief guide outlines the new and changed features in the Rhino C/C++ SDK.
author: dale@mcneel.com, steve@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Overview']
origin: http://wiki.mcneel.com/developer/rhino/5/sdkfeatures
order: 2
keywords: ['c', 'C/C++', 'plugin']
layout: toc-guide-page
TODO: 'needs review and the original contained links to empty wiki entries.'
---

# {{ page.title }}

{{ page.description }}

## Overview

The Rhino C/C++ SDK is *not* an abstract SDK. That is, the native classes and functions that are made available in the SDK are also used internally by Rhino. Thus, when the signatures of classes or functions change, all developers, both internal and external, are required to modify their source code to accommodate for the change. For this reason, the Rhino C/C++ SDK was not broken between Rhino 4 and 5. In doing this, plug-ins that worked in Rhino 4 also worked in Rhino 5.

A lot of time has passed since the Rhino 4 C/C++ SDK was made available. And although there was quite a bit of new functionality added to Rhino 5, some of it required some *creative* programming in order not to break backwards compatibility with Rhino 4.

In order to continue to move Rhino forward, breaking changes needed to be made to the SDK. The following document attempts to describe what has been added, what has changed, and how to deal with these changes.

## Breaking Changes

Although the breaking changes may seem numerous, most fall within the following categories.

### Multi-Document Support

One of the primary goals for Rhino 6 was to consolidate the Rhino for Windows and Rhino for Mac source code into a single codebase. In order to do this, the source code had to become more multiple-document aware, as Rhino for Mac handle multiple documents. Note, Rhino 6 for Windows is still a single document application.

Thus, many SDK functions now require the developer to pass either a pointer or a reference to the active document or the active document’s runtime serial number.

An example of this is the ```CRhinoDisplayConduit``` class, which now requires the document serial number in which it will operate. In Rhino 5, you could enable a display conduit in a plug-in command as follows:

        CMyDisplayConduit conduit;
        conduit.Enable();
        context.m_doc.Redraw();

In Rhino 6, you need to do the following:

        CMyDisplayConduit conduit;
        conduit.Enable(context.m_doc.RuntimeSerialNumber());
        context.m_doc.Redraw();

A number of SDK functions have been modified to require some data from the active document. This is because SDK functions can no longer assume there is a single document.

An example of this is the ```RhinoPointInPlanarClosedCurve``` function, which now requires the absolute tolerance from the active document. In Rhino 5, you could use this function in a command as follows:

        int rc = RhinoPointInPlanarClosedCurve(point, closed_curve, plane);

In Rhino 6, you will need to do the following:

        double tolerance = context.m_doc.AbsoluteTolerance();
        int rc = RhinoPointInPlanarClosedCurve(point, closed_curve, plane, tolerance);

### Model Components
Rhino has a number of model components, such as layers, group, render materials, dimensions style, and more. Over the years, common properties, such as name, index, and id, have been added to these components, but done so in an inconsistent manner. For example, the method for obtaining the id of a layer was different that of a render material.

The Rhino 6 C/C++ SDK contains a new ```ON_ModelComponent``` class that remedies this. Model component classes now inherit from this class.

Providing a consistent interface to common properties, however, means that the names of functions used to access these properties have change.

For example, in Rhino 5, you could access the name of the current Layer as follows:

        const CRhinoLayer& current_layer = context.m_doc.m_layer_table.CurrentLayer();
        ON_wString current_name = current_layer.LayerName();

In Rhino 6, you will need to do the following:

        const CRhinoLayer& current_layer = context.m_doc.m_layer_table.CurrentLayer();
        ON_wString current_name = current_layer.Name();

As another example, in Rhino 5, you could access the id of a Group as follows:

        const CRhinoGroup* group = context.m_doc.m_group_table[0];
        if (group)
          ON_UUID group_id = group->m_group_id;

In Rhino 6, you will need to do the following:

        const CRhinoGroup* group = context.m_doc.m_group_table[0];
        if (group)
          ON_UUID group_id = group->Id();

### Annotations

For Rhino 6, there will be new implementations for all annotation objects, such as Text, Leaders, and Dimensions. The new implementations are much better organized the the prior versions, plus provide new features such as [Rich Text](https://en.wikipedia.org/wiki/Rich_Text_Format).

As of this writing, the new annotations were still in development. More information on the changes and how to migrate to the new annotation classes will be available as we get closer to freezing the SDK.

### Scoped and Strongly Typed Enums
C++11 provides some great new features for C++ programmers. One such feature is scoped and strongly typed enumerations, which ensures some measure of compatibility across compilers. They also make up for some shortcomings of old-style enums:

- Old-style enums do not have their own scope
- Old-style enums convert to integral types, which can lead to strange behavior
- You cannot specify the underlying integral type of an old-style enums

There are a number of places in the Rhino 6 C/C++ SDK were old-style enums have been converted to scoped and strongly typed enums by convert ```enum``` declarations to ```enum class```. Enumerators of these types of enums require a qualified name such as *enumname::enumerator* when you refer to them. 

For example, in Rhino 5, you could specify a unit system in millimeters as follows:
        
        ON_UnitSystem units(ON::millimeters);
        
In Rhino 6, you will need to do the following:        
        
        ON_UnitSystem units(ON::LengthUnitSystem::Millimeters);

### Deprecation

Obsolete functions from Rhino 5 are marked as deprecated with a message to help accomplish the same goal through alternate functions in the Rhino 6 SDK. These deprecations will generate compiler warnings when plug-in code attempts to call these functions.

Functions marked as deprecated may or may not continue to work in Rhino 6. Thus, you should replace all calls to deprecated functions with calls to their replacements before distributing any plug-in.

In Rhino 7, all functions marked as deprecated in Rhino 6 will be removed.

### Other
Not all changes in the Rhino 6 C/C++ SDK could be tagged as deprecated. For example, if a member variable from a class were removed, or a feature was dramatically changed, then deprecation could not be used. These types of breakages will require more time to fix.

To help with this, we are working on updating all of the [C++ SDK samples](https://github.com/mcneel/Rhino6Samples_CPP).

## Related Topics

- [Installing Tools (Windows)]({{ site.baseurl }}/guides/cpp/installing_tools_windows)
- [Migrate your plugin project to Rhino 6]({{ site.baseurl }}/guides/cpp/migrate_your_plugin_windows)
- [Migrate your plugin project to Rhino 6 manually]({{ site.baseurl }}/guides/general/migrate_your_plugin_manual_windows)

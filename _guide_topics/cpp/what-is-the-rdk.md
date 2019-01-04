---
title: What is the RDK?
description: This guide describes the Rhino Renderer Development Kit (AKA RDK) and its features.
authors: ['andrew_le_bihan', 'john_croudy']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin']
layout: toc-guide-page
TODO: 'needs cleanup, standardization, editing, new images, etc.'
---

![RDK Logo]({{ site.baseurl }}/images/what-is-the-rdk-01.png)

## Overview

The RDK is a collection of tools that extend the Rhino application platform with visualization-specific capabilities. Third-party developers can use the RDK SDK to integrate their renderers into Rhino.

## Features

![RDK Features Banner]({{ site.baseurl }}/images/what-is-the-rdk-02.png)

- Extensible Material, Environment and Texture editors which display and edit Materials, Environments and Textures (AKA _Render Content_).
- Render content can have tags assigned.
- Frame buffer implementation with post-processing and multiple channels.
- Pre-process custom mesh provision interface for third party developers.
- Built-in material types, including gem, glass, plastic, plaster, metal, paint, picture and custom.
- Built-in procedural textures, including wood, marble, granite, noise generators, perturbs, and so on.
- Built-in HDR and OpenEXR support.
- Improved render pipeline that makes it much easier for developers to implement a renderer engine in Rhino.
- Sun light and sun angle calculation tools.
- Automatic shader UI support for third party Material/Environment/Texture providers.
- Several utility classes to aid in the development of renderers and visualization related tools.
- Decal support with planar, UV, cylindrical or spherical mapping.
- Ground Plane support with automatic height, material and texture mapping options.
- 360 degree environment preview in the viewport.
- Extensive library of ready-to-use materials, environments and textures with Library browser.

## Material, Environment and Texture Editors

The Material, Environment, and Texture Editors display objects called _Render Contents_ and allow the user to edit them. These editors are all based on a similar interface with only small functional differences between them. Render Contents are the foundation of the RDK core and one of the most important objects it provides. Please see [Render Content](/guides/cpp/rdk-render-content) for more information. The Texture Editor is known to users as the Texture _Palette_ but programmatically it is an editor just like the other two.

![Material Environment and Texture Editors]({{ site.baseurl }}/images/what-is-the-rdk-03.png){:style="float: right; margin-left: 12px;"}

1. Navigation controls similar to those found on a web browser.
2. Resizeable Floating Previews.
3. Configurable thumbnails with multiple sizes and styles.
4. Resizeable preview pane.
5. User interface for editing render content parameters (AKA _fields_).
6. Breadcrumb navigation control similar to those found on file explorers.
7. Task menu for performing actions on render contents and setting editor options.

These editors are integrated with Rhino's tabbed pane system. You can access them through the Rhino Render menu, the Rendering tool bar, or the editor commands.

Lists of materials, environments, and textures are stored in the Rhino document. Each editor displays the relevant render content type as preview thumbnails.

Contents display an interface below the preview thumbnails in an area reserved for collapsible UI panels. An addition to the basic UI panels, several additional collapsible panels are provided by Rhino within the same area as the content UI. These include the Name, Notes, Texture Summary, Local Mapping, Graph and Adjustment panels. These are described later in the content UI section.

Each material, environment or texture can have child nodes (AKA _child slots_ or _sub-nodes_). The children can be of any content type, but specific child slots will only support specific types. The most common child type is a texture. For example, the _Color_ child slot for a Custom Material will only support textures, as will the _Background image_ child slot on a Basic Environment.

{:style="clear:both;"}

## Render Window

![Render Window]({{ site.baseurl }}/images/what-is-the-rdk-04.png)

A user thinks of the Render Window as the window that appears on the screen when one renders a model (see the picture above). However, the render window object used by developers corresponds more to the actual _frame&nbsp;buffer_. It contains information about the channels and pixels that make up the rendered image. The standard render window provides a number of features to renderers, including built-in support for scripting, cloning, saving to high dynamic-range formats, post effects, zooming and channel display.

## HDR and EXR Support

![HDR and EXR Support]({{ site.baseurl }}/images/what-is-the-rdk-05.png){:style="float: right; margin-left: 12px;"}

An HDR image which provides automatic conversion to a bitmap for non-HDR capable renderers. This allows the Rhino renderer and viewport display to show HDR environments while providing HDR tools to third-party renderer engines.

The HDR texture also provides projection conversion features. Most HDRi files come as Light Probe projection. The Basic Environment requires Spherical (Equirectangular) projection for spherical environments, so the HDR texture defaults to this conversion. However, several other types are supported.

The LDR exposure determines the brightness of the image when converted to a bitmap image. This will not affect the rendering when used by a HDR capable renderer.

HDR multiplier is a simple linear multiplier on all values in the image. This can be used to brighten or dim the image in an HDR capable renderer.

The Save As button can be used to convert the image to a bitmap file. The LDR exposure value is used convert the image during this process.

Azimuth and Altitude values modify the way the image is rotated in space during the projection conversion.

{:style="clear:both;"}

## Decals

![Decals]({{ site.baseurl }}/images/what-is-the-rdk-07.png){:style="float: right; margin-left: 12px;"}

Decals are non-repeating textures that are applied to the surface of an object with a given projection. They are an easy-to-use way of attaching single images or similar textures to objects without going through the complexity of the texture mapping process.

Decals are textures that are placed directly on a specified area of one or more objects. They consist of a single instance of a texture, rather than being tiled as they are when used in a material. Users use decals to modify a limited part of an object's color.

![Decals2]({{ site.baseurl }}/images/what-is-the-rdk-08.jpg)

{:style="clear:both;"}

## Sun

![Sun]({{ site.baseurl }}/images/what-is-the-rdk-06.png){:style="float: right; margin-left: 12px;"}

The RDK provides easy-to-use sun tools, including a docking panel to control the [document sun](/guides/cpp/rdk-sun-classes/#DocumentSun), a sunlight preview within the Rendered viewport, a Sunlight command and a number of other scripting and developer tools to make sun-angle calculations easy.

The following classes can be used to access sun features:

- [IRhRdkSun](/guides/cpp/rdk-sun-classes/#IRhRdkSun)
- [CRhRdkSun](/guides/cpp/rdk-sun-classes/#CRhRdkSun)
- [CRhRdkSunDialog](/guides/cpp/rdk-sun-classes/#CRhRdkSunDialog)

{:style="clear:both;"}

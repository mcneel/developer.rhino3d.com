---
title: What is the RDK?
description: This guide describes the Rhino Renderer Development Kit and its features.
authors: ['Andrew le Bihan', '@andy']
author_contacts: ['']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin']
layout: toc-guide-page
TODO: 'needs cleanup, standardization, editing, new images, etc.'
---

# {{ page.title }}

{{ page.description }}

![RDK Logo]({{ site.baseurl }}/images/what_is_the_rdk_01.png)

## Overview

The Rhino RDK is a collection of tools that extend the Rhino application platform with visualization specific capabilities.

The RDK underpins the [Brazil for Rhino](http://brazil.mcneel.com/) product, and all of the above features are supported in that product.  However, all of these features are available to third-party developers to integrate their products into Rhino.

## Features

![RDK Features Banner]({{ site.baseurl }}/images/what_is_the_rdk_02.png)

- Extensible Material, Environment and Texture editor.
- Frame buffer implementation with post and channel handling.
- Pre-process custom mesh provision interface for third party developers.
- Built-in procedural textures, including wood, marble, granite, noise generators, perturbs, and so on.
- Built-in HDR and OpenEXR support.
- Improved render pipeline that makes it much easier for developers to implement a renderer engine in Rhino.
- Rhino sun light and sun-angle calculation tools.
- Automatic shader UI support for third party Material/Environment/Texture providers.
- Several utility classes to aid in the development of renderers and visualization related tools.
- Decal support similar to Flamingo 2.0.
- 360 degree environment preview in the viewport.


## Material, Environment, & Texture Editors

![Material Environment and Texture Editors]({{ site.baseurl }}/images/what_is_the_rdk_03.png)

The material editor, environment editor, and texture palettes interact with the enhanced render content system.  All are based on a similar interface with only small functional differences between them.

Access the editors through the Rhino Render menu, the Rendering toolbar, or the editor commands.

Lists of materials, environments, and textures are stored in the Rhino document.  Each editor displays the relevant render content type as preview thumbnails.

A large button to the left of the editor controls the visibility of the editor side panel which displays a list of common tasks along with the structure of the currently selected material, environment, or texture.

The size of the preview thumbnails area can be adjusted by dragging the handle just below its lowest edge.

Contents display an interface below the preview thumbnails in an area reserved for collapsible UI panels.  An addition to the basic UI panels, several additional collapsible panels are provided by Rhino within the same area as the content UI.  These include the Texture Summary panel, the Notes panel, the Local Mapping panel, Graph panel and the Adjustment panel.  These are described later in the content UI section.

The editor window can be minimized to the caption bar and restored by double clicking on the caption bar.

Each material, environment or texture can have child nodes.  The children can be of any content type, but specific child slots will only support specific types. The most common child type is a texture.  For example, the Texture child for a Basic Material will only support textures, as will the Background image slot on a Basic Environment.

## Render Window

![Render Window]({{ site.baseurl }}/images/what_is_the_rdk_04.png)

The standard render window provides a number of features to renderers, including built in support for scripting, cloning, saving to High-Dynamic-Range formats, post effects, zooming and channel display.

Many renderers call the render window the "frame buffer."  The terms are nearly interchangeable.

## HDR and EXR Support

![HDR and EXR Support]({{ site.baseurl }}/images/what_is_the_rdk_05.png)

An HDR image which provides automatic conversion to a bitmap for non-HDR capable renderers.  This allows the Rhino renderer and viewport display to show HDR environments while providing HDR tools to third-party renderer engines.

The HDR texture also provides projection conversion features.  Most HDRi files come as Light Probe projection.  The Basic Environment requires Spherical (Equirectangular) projection for spherical environments, so the HDR texture defaults to this conversion.  However, several other types are supported.

The LDR exposure determines the brightness of the image when converted to a bitmap image.  This will not affect the rendering when used by a HDR capable renderer.

HDR multiplier is a simple linear multiplier on all values in the image.  This can be used to brighten or dim the image in an HDR capable renderer.

The Save As button can be used to convert the image to a bitmap file.  The LDR exposure value is used convert the image during this process.

Azimuth and Altitude values modify the way the image is rotated in space during the projection conversion.

## Sunlight

![Sunlight]({{ site.baseurl }}/images/what_is_the_rdk_06.png)

Sun tools, including a docking panel to control the document sun, a sunlight preview within the Rendered viewport, a Sunlight command and a number of other scripting and developer tools make sun angle calculations easier.

## Decals

![Decals]({{ site.baseurl }}/images/what_is_the_rdk_07.png)

Decals are non-repeating textures that are applied to the surface of an object with a given projection.  They are an easy-to-use way of attaching single images or similar textures to objects without going through the complexity of the texture mapping process.

Decals are textures that are placed directly on a specified area of one or more objects.  Use decals to modify a limited part of an object's color.

Decals consist of a single instance of a texture, rather than being tiled as they are when used in a material.

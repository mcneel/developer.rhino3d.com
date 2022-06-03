+++
authors = [ "andy", "john.croudy" ]
categories = [ "RDK" ]
description = "This guide describes the Rhino Renderer Development Kit (AKA RDK) and its features."
keywords = [ "RDK", "Rhino", "Renderer", "Development", "Plugin" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "What is the RDK?"
type = "guides"
weight = 1
override_last_modified = "2019-01-23T17:37:16Z"

[admin]
TODO = "needs cleanup, standardization, editing, new images, etc."
origin = "http://wiki.mcneel.com/labs/rendererdevelopmentkit10"
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

![RDK Logo](/images/rdk-what-is-the-rdk-01.png)

### Overview
The RDK is a collection of tools that extend the Rhino application platform with visualization-specific capabilities. Third-party developers can use the RDK SDK to integrate their renderers into Rhino.

### Features
![RDK Features Banner](/images/rdk-what-is-the-rdk-02.png)

- Extensible Material, Environment and Texture editors which display and edit Materials, Environments and Textures (AKA _Render Content_) and allow [operations](/guides/cpp/rdk-task-classes/) to be performed on them.
- Render content can have tags assigned.
- [Frame buffer](/guides/cpp/rdk-rendering-classes/) implementation with multiple channels and post-processing.
- Pre-process custom mesh provision interface for third party developers.
- Built-in material types, including gem, glass, plastic, plaster, metal, paint, picture and custom.
- Built-in procedural textures, including wood, marble, granite, noise generators, perturbs, and so on.
- Built-in HDR and OpenEXR support.
- Improved [render pipeline](/guides/cpp/rdk-rendering-classes/) that makes it much easier for developers to implement a renderer engine in Rhino.
- [Sun light](/guides/cpp/rdk-sun-classes/) and sun angle calculation tools.
- [Skylight](/guides/cpp/rdk-skylight-classes/) support.
- [Safe Frame](/guides/cpp/rdk-safe-frame-classes/) support.
- Gamma, [Linear Workflow](/guides/cpp/rdk-linear-workflow-classes/) and [Dithering](/guides/cpp/rdk-dithering-classes/) support.
- Automatic shader UI support for third party Material/Environment/Texture providers.
- Several utility classes to aid in the development of renderers and visualization related tools.
- Decal support with planar, UV, cylindrical or spherical mapping.
- [Ground Plane](/guides/cpp/rdk-ground-plane-classes/) support with automatic height, material and texture mapping options.
- 360 degree [environment](/guides/cpp/rdk-current-environment-classes/) preview in the viewport.
- Extensive library of ready-to-use materials, environments and textures with Library browser.

### Material, Environment and Texture Editors
{{< image url="/images/rdk-what-is-the-rdk-03.png" alt="MET editors" class="float_right" >}}
The Material, Environment, and Texture Editors display objects called _Render Contents_ and allow the user to edit them. These editors are all based on a similar interface with only small functional differences between them. Render Contents are the foundation of the RDK and one of the most important objects it provides. The RDK SDK provides an extensive system that allows render engine developers to create their own custom render contents. The editors then allow users to create, edit and manage these specialized contents as well as the ones bundled with the RDK and apply them to objects in the scene.

Main articles:

- [Render Content](/guides/cpp/rdk-render-content)
- [Render Content Editors](/guides/cpp/rdk-render-content-editors)

{{< div class="clear_both" />}}

### Render Window
![Render Window](/images/rdk-what-is-the-rdk-04.png)

A user thinks of the [Render Window](/guides/cpp/rdk-rendering-classes/) as the window that appears on the screen when one renders a model (see the picture above). However, the render window object used by developers corresponds more to the actual _frame&nbsp;buffer_. It contains information about the channels and pixels that make up the rendered image. The standard render window provides a number of features to renderers, including built-in support for scripting, cloning, saving to high dynamic-range formats, post effects, zooming and channel display.

### HDR and EXR Support
{{< image url="/images/rdk-what-is-the-rdk-05.png" alt="HDR and EXR Support" class="float_right" >}}

An HDR image which provides automatic conversion to a bitmap for non-HDR capable renderers. This allows the Rhino renderer and viewport display to show HDR environments while providing HDR tools to third-party renderer engines.

The HDR texture also provides projection conversion features. Most HDRi files come as Light Probe projection. The Basic Environment requires Spherical (Equirectangular) projection for spherical environments, so the HDR texture defaults to this conversion. However, several other types are supported.

The LDR exposure determines the brightness of the image when converted to a bitmap image. This will not affect the rendering when used by a HDR capable renderer.

HDR multiplier is a simple linear multiplier on all values in the image. This can be used to brighten or dim the image in an HDR capable renderer.

The Save As button can be used to convert the image to a bitmap file. The LDR exposure value is used convert the image during this process.

Azimuth and Altitude values modify the way the image is rotated in space during the projection conversion.

{{< div class="clear_both" />}}

### Decals
{{< image url="/images/rdk-what-is-the-rdk-07.png" alt="Decals" class="float_right" >}}

Decals are non-repeating textures that are applied to the surface of an object with a given projection. They are an easy-to-use way of attaching single images or similar textures to objects without going through the complexity of the texture mapping process.

Decals are textures that are placed directly on a specified area of one or more objects. They consist of a single instance of a texture, rather than being tiled as they are when used in a material. Users use decals to modify a limited part of an object's color.

![Decals2](/images/rdk-what-is-the-rdk-08.jpg)

{{< div class="clear_both" />}}

The following classes can be used to access decal features:

- [IRhRdkDecal](/guides/cpp/rdk-decal-classes/#IRhRdkDecal)
- [CRhRdkObjectDataAccess](/guides/cpp/rdk-decal-classes/#CRhRdkObjectDataAccess)

### Sun
{{< image url="/images/rdk-what-is-the-rdk-06.png" alt="Sun" class="float_right" >}}

The RDK provides easy-to-use sun tools, including a docking panel to control the [document sun](/guides/cpp/rdk-sun-classes/#DocumentSun), a sunlight preview within the Rendered viewport, a Sunlight command and a number of other scripting and developer tools to make sun-angle calculations easy.

The following classes can be used to access sun features:

- [IRhRdkSun](/guides/cpp/rdk-sun-classes/#IRhRdkSun)
- [CRhRdkSun](/guides/cpp/rdk-sun-classes/#CRhRdkSun)
- [CRhRdkSunDialog](/guides/cpp/rdk-sun-classes/#CRhRdkSunDialog)

{{< div class="clear_both" />}}

### Summary
This article introduced the RDK and described some of its main features. Each feature is explained in more detail in a different article.

<!--
### Automatic UI
The RDK provides an automatic UI system to make it easy to quickly develop user interfaces in your plug-in. See the main article here: [Automatic UI](/guides/cpp/rdk-raw-auto-ui).
-->

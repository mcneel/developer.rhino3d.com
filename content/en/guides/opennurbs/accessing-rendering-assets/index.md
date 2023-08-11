+++
authors = ["john.croudy"]
categories = ["Fundamentals"]
description = "OpenNURBS and Rhino3dm provide direct access to rendering information without the need for Rhino."
keywords = [ "Rendering", "RDK", "OpenNURBS", "Materials", "Textures" ]
languages = [ "C/C++", "C#" ]
sdk = [ "openNURBS" ]
title = "Accessing Rendering Assets"
type = "guides"
weight = 4

[admin]
TODO = "Author this page"
origin = "https://docs.google.com/document/d/1t92RN1Uqb7olnkiH0WNqK3oP8e0rgnomSrutlV3jRGc"
picky_sisters = ""
state = "In Progress"

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true
+++

OpenNURBS and Rhino3dm now provide direct access to rendering information without the need for Rhino. (Prior to this, the only way to access this information outside of Rhino was by getting the data as XML and parsing it.) For example:

**TODO**: Three.js model here?

This guide outlines classes used to access these rendering assets and provides examples.

## Overview

In C++, the following objects are accessible through the use of `ONX_Model`. In C# the equivalent functionality is provided by `File3dm` which under the hood is a wrapper around `ONX_Model`.

<div class="table-responsive" align="center">
<table class="table" style="width:940px;">
  <thead>
    <tr style="border-bottom:1pt solid black;">
      <th style="text-align: left;">C/C++</th>
      <th style="text-align: left;">C# Equivalent</th>
      <th style="text-align: left;">Purpose</th>
    </tr>
  </thead>
  <tbody class="table-striped index_table">
  <tr>
	<td>ON_RenderContent</td>
    <td>File3dmRenderContent</td>
	<td>Provides access to generic render content settings.</td>
  </tr>
  <tr>
    <td>ON_RenderMaterial</td>
    <td>File3dmRenderMaterial</td>
	<td>Provides access to settings specific to render materials.</td>
  </tr>
  <tr>
    <td>ON_RenderEnvironment</td>
	<td>File3dmRenderEnvironment</td>
	<td>Provides access to settings specific to render environments.</td>
  </tr>
  <tr>
    <td>ON_RenderTexture</td>
	<td>File3dmRenderTexture</td>
	<td>Provides access to settings specific to render textures.</td>
  </tr>
  <tr>
    <td>ON_Decals</td>
	<td>Rhino.Render.Decals</td>
	<td>Provides access to a collection of decals stored on object attributes.</td>
  </tr>
    <tr>
    <td>ON_Decal</td>
	<td>Rhino.Render.Decal</td>
	<td>Provides access to settings for an individual decal in the collection.</td>
  </tr>
  <tr>
    <td>ON_Dithering</td>
	<td>Rhino.Render.Dithering</td>
	<td>Provides access to dithering settings.</td>
  </tr>
  <tr>
    <td>ON_EmbeddedFile</td>
	<td>File3dmEmbeddedFile</td>
	<td>Provides access to embedded texture files.</td>
  </tr>
  <tr>
    <td>ON_GroundPlane</td>
	<td>Rhino.Render.GroundPlane</td>
	<td>Provides access to ground plane settings.</td>
  </tr>
    <tr>
    <td>ON_LinearWorkflow</td>
	<td>Rhino.Render.LinearWorkflow</td>
	<td>Provides access to gamma and linear workflow settings.</td>
  </tr>
  <tr>
    <td>ON_RenderChannels</td>
	<td>Rhino.Render.RenderChannels</td>
	<td>Provides access to render channels settings.</td>
  </tr>
  <tr>
    <td>ON_SafeFrame</td>
	<td>Rhino.Render.SafeFrame</td>
	<td>Provides access to safe frame settings.</td>
  </tr>
  <tr>
    <td>ON_Skylight</td>
	<td>Rhino.Render.Skylight</td>
	<td>Provides access to skylighting settings.</td>
  </tr>
    <tr>
    <td>ON_Sun</td>
	<td>Rhino.Render.Sun</td>
	<td>Provides access to sun settings and sun position calculations.</td>
  </tr>
  <tr>
    <td>ON_PostEffects</td>
	<td>Rhino.Render.PostEffects.PostEffectCollection</td>
	<td>Provides access to the list of post effects.</td>
  </tr>
  <tr>
    <td>ON_PostEffect</td>
	<td>Rhino.Render.PostEffects.PostEffectData</td>
	<td>Provides access to settings for an individual post effect in the list.</td>
  </tr>
 </tbody>
 </table>
 </div>

## Decals

To access [decals](/guides/cpp/what-is-the-rdk/#decals) you need to get the `3dmObjectAttributes` object for the model geometry component that you are interested in and then get the decal collection from its attributes. You can then iterate over all the decals in the collection and get and set their properties:

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'py')">Python</button>
  <button class="tablinks" onclick="openCodeTab(event, 'js')">JavaScript</button>
  <button class="tablinks" onclick="openCodeTab(event, 'cpp')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content" id="cs">

```cs
var file3dm = File3dm.Read(filename_in);
var e = file3dm.Manifest.GetEnumerator(
                 Rhino.DocObjects.ModelComponentType.ModelGeometry);
while (e.MoveNext())
{
  if (e.Current is File3dmObject obj)
  {
    foreach (var decal in obj.Attributes.Decals)
    {
      Console.WriteLine("  Mapping:      {0}", decal.DecalMapping);
      Console.WriteLine("  Projection:   {0}", decal.DecalProjection);
      Console.WriteLine("  Origin:       {0}", decal.Origin);
      Console.WriteLine("  Transparency: {0}", decal.Transparency);
    }
  }
}
```

</div>

<div class="codetab-content" id="py">

```py
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)

for obj in model.Objects:
    for decal in obj.Attributes.Decals:
        print(decal.Mapping)
        print(decal.Projection)
        print(decal.Origin)
        print(decal.Transparency)
        print()
```

</div>

<div class="codetab-content" id="js">

```js
// node.js
import * as fs from 'fs' //only if running in node.js
import rhino3dm from 'rhino3dm'

const rhino = await rhino3dm()

const buffer = fs.readFileSync( filename_in )
/*
if you are running this in a browser, you can replace the above line with these two lines:
const file = await fetch( filename_in )
const buffer = await file.arrayBuffer()
*/

const arr = new Uint8Array( buffer )
const file3dm = rhino.File3dm.fromByteArray( arr )
const objects = file3dm.objects()

for( let i = 0; i < objects.count; i ++ ) {

    const attributes = objects.get( i ).attributes()

    for( let j = 0; j < attributes.decals().count; j ++ ) {

        const decal = attributes.decals().get( j )

        console.log( `Decal Mapping: ${decal.mapping.constructor.name}` )
        console.log( `Decal Projection: ${decal.projection.constructor.name}`)
        console.log( `Decal Origin: ${decal.origin}` )
        console.log( `Decal Transparency: ${decal.transparency}` )

    }
}

```

</div>

<div class="codetab-content" id="cpp">

```cpp
ONX_Model model;
model.Read(filename_in);

ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
const auto* component = it.FirstComponent();
while (nullptr != component)
{
  auto* mgc = ON_ModelGeometryComponent::Cast(component);
  if (nullptr != mgc)
  {
    auto* attr = mgc->ExclusiveAttributes();
    if (nullptr != attr)
    {
      const auto& da = attr->GetDecalArray();
      for (int i = 0; i < da.Count(); i++)
      {
        auto* decal = da[i];
        const auto mapping = decal->Mapping();
        const auto origin = decal->Origin();
      }
    }
  }

  component = it.NextComponent();
}
```

</div>
</div>

## Dithering

[Dithering](/guides/cpp/rdk-dithering-classes) information is accessed through `3dmRenderSettings`. To access it, you need to get the render settings and call its `Dithering` method/property to get a reference to a `Dithering` object. You can then read or write the settings by calling the various methods on the `Dithering` object. Any changes you make will persist and can be saved to a 3dm file:

<div class="codetab">
  <button class="tablinks0" onclick="openCodeTab(event, 'cs0')" id="defaultOpen0">C#</button>
  <button class="tablinks0" onclick="openCodeTab(event, 'py0')">Python</button>
  <button class="tablinks0" onclick="openCodeTab(event, 'js0')">JavaScript</button>
  <button class="tablinks0" onclick="openCodeTab(event, 'cpp0')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content0" id="cs0">

```cs
var file3dm = File3dm.Read(filename_in);
var dit = file3dm.Settings.RenderSettings.Dithering;
Console.WriteLine("Enabled: {0}", dit.Enabled);
Console.WriteLine("Method:  {0}", dit.Method);
dit.Enabled = true;
dit.Method = Dithering.Methods.FloydSteinberg;
```

</div>

<div class="codetab-content0" id="py0">

```py
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)
dit = model.Settings.RenderSettings.Dithering
print(dit.Enabled)
print(dit.Method)
dit.Enabled = True
dit.Method = _rhino3dm.DitheringMethods.FloydSteinberg
```

</div>

<div class="codetab-content0" id="js0">

```js
// node.js
import * as fs from 'fs' //only if running in node.js
import rhino3dm from 'rhino3dm'

const rhino = await rhino3dm()

const buffer = fs.readFileSync( filename_in )

/*
if you are running this in a browser, you can replace the above line with these two lines:
const file = await fetch( filename_in )
const buffer = await file.arrayBuffer()
*/

const arr = new Uint8Array( buffer )
const file3dm = rhino.File3dm.fromByteArray( arr )

const dithering = file3dm.settings().renderSettings().dithering

console.log( `Dithering Enabled: ${ dithering.enabled }` )
console.log( `Dithering Method: ${ dithering.method.constructor.name }` )

dithering.enabled = true
dithering.method = rhino.DitheringMethods.SimpleNoise

console.log( `Dithering Enabled: ${ dithering.enabled }` )
console.log( `Dithering Method: ${ dithering.method.constructor.name }` )

```

</div>

<div class="codetab-content0" id="cpp0">

```cpp
ONX_Model model;
model.Read(filename_in);
auto& dit = model.m_settings.m_RenderSettings.Dithering();
const auto on = dit.Enabled();
const auto method = dit.Method();
dit.SetEnabled(true);
dit.SetMethod(ON_Dithering::Methods::FloydSteinberg);
model.Write(filename_out);
```

</div>
</div>

## Ground Plane

[Ground plane](/guides/cpp/rdk-ground-plane-classes/) information is accessed through `3dmRenderSettings`. To access it, you need to get the render settings and call its `GroundPlane` method/property to get a reference to a `GroundPlane` object. You can then read or write the settings by calling the various methods on the `GroundPlane` object. Any changes you make will persist and can be saved to a 3dm file:

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'py1')">Python</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'js1')">JavaScript</button>  
  <button class="tablinks1" onclick="openCodeTab(event, 'cpp1')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content1" id="cs1">

```cs
var file3dm = File3dm.Read(filename_in);
var gp = file3dm.Settings.RenderSettings.GroundPlane;
Console.WriteLine("Enabled:             {0}", gp.Enabled);
Console.WriteLine("Altitude:            {0}", gp.Altitude);
gp.Enabled = false;
model.Write(filename_out);
```

</div>

<div class="codetab-content1" id="py1">

```py
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)
gp = model.Settings.RenderSettings.GroundPlane
print(gp.Enabled)
print(gp.Altitude)
gp.Enabled = False
```

</div>

<div class="codetab-content1" id="js1">

```js
// node.js
import * as fs from 'fs' //only if running in node.js
import rhino3dm from 'rhino3dm'

const rhino = await rhino3dm()

//const file3dm = new rhino.File3dm()

const buffer = fs.readFileSync( filename_in )

/*
if you are running this in a browser, you can replace the above line with these two lines:
const file = await fetch( filename_in )
const buffer = await file.arrayBuffer()
*/

const arr = new Uint8Array( buffer )
const file3dm = rhino.File3dm.fromByteArray( arr )

const gp = file3dm.settings().renderSettings().groundPlane

console.log( `Ground Plane Enabled: ${ gp.enabled }` )
console.log( `Ground Plane Altitude: ${ gp.altitude }` )

gp.enabled = false

```

</div>

<div class="codetab-content1" id="cpp1">

```cpp
ONX_Model model;
model.Read(filename_in);
auto& gp = model.m_settings.m_RenderSettings.GroundPlane();
const auto on = gp.Enabled();
const auto alt = gp.Altitude();
gp.SetEnabled(false);
model.Write(filename_out);
```

</div>
</div>

## Linear Workflow

[Linear workflow](/guides/cpp/rdk-linear-workflow-classes/) information is accessed through `3dmRenderSettings`. To access it, you need to get the render settings and call its `LinearWorkflow` method/property to get a reference to a `LinearWorkflow` object. You can then read or write the settings by calling the various methods on the `LinearWorkflow` object. Any changes you make will persist and can be saved to a 3dm file:

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'py2')">Python</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'js2')">JavaScript</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'cpp2')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content2" id="cs2">

```cs
var file3dm = File3dm.Read(filename_in);
var lw = file3dm.Settings.RenderSettings.LinearWorkflow;
Console.WriteLine("PostProcessGammaOn: {0}", lw.PostProcessGammaOn);
Console.WriteLine("PostProcessGamma:   {0}", lw.PostProcessGamma);
lw.PostProcessGamma = 3.4f;
model.Write(filename_out);
```

</div>

<div class="codetab-content2" id="py2">

```py
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)
lw = model.Settings.RenderSettings.LinearWorkflow
print(lw.PostProcessGammaOn)
print(lw.PostProcessGamma)
lw.PostProcessGamma = 3.4
```

</div>

<div class="codetab-content2" id="js2">

```js
// node.js
import * as fs from 'fs' //only if running in node.js
import rhino3dm from 'rhino3dm'

const rhino = await rhino3dm()

//const file3dm = new rhino.File3dm()

const buffer = fs.readFileSync( filename_in )

/*
if you are running this in a browser, you can replace the above line with these two lines:
const file = await fetch( filename_in )
const buffer = await file.arrayBuffer()
*/

const arr = new Uint8Array( buffer )
const file3dm = rhino.File3dm.fromByteArray( arr )

const lw = file3dm.settings().renderSettings().linearWorkflow

console.log( `Linear Workflow Post Proces Gamma On: ${ lw.postProcessGammaOn }` )
console.log( `Linear Workflow Post Proces Gamma: ${ lw.postProcessGamma }` )
lw.PostProcessGamma = 3.4
```

</div>

<div class="codetab-content2" id="cpp2">

```cpp
ONX_Model model;
model.Read(filename_in);
auto& lw = model.m_settings.m_RenderSettings.LinearWorkflow();
const auto on = lw.PostProcessGammaOn();
const auto gamma lw.PostProcessGamma();
lw.SetPostProcessGamma(3.4f);
model.Write(filename_out);
```

</div>
</div>

## Render Channels

Render channel information is accessed through `3dmRenderSettings`. To access it, you need to get the render settings and call its `RenderChannels` method/property to get a reference to a `RenderChannels` object. You can then read or write the settings by calling the various methods on the `RenderChannels` object. Any changes you make will persist and can be saved to a 3dm file:

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'py3')">Python</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'js3')">JavaScript</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'cpp3')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content3" id="cs3">

```cs
var file3dm = File3dm.Read(filename_in);
var lw = file3dm.Settings.RenderSettings.RenderChannels;
Console.WriteLine("Mode: {0}", rch.Mode);
rch.Mode = RenderChannels.Modes.Custom;
model.Write(filename_out);
```

</div>

<div class="codetab-content3" id="py3">

```py
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)
rch = model.Settings.RenderSettings.RenderChannels
print(rch.Mode)
rch.Mode = _rhino3dm.RenderChannelsModes.Custom
```

</div>

<div class="codetab-content3" id="js3">

```js
// node.js
import * as fs from 'fs' //only if running in node.js
import rhino3dm from 'rhino3dm'

const rhino = await rhino3dm()

//const file3dm = new rhino.File3dm()

const buffer = fs.readFileSync( filename_in )

/*
if you are running this in a browser, you can replace the above line with these two lines:
const file = await fetch( filename_in )
const buffer = await file.arrayBuffer()
*/

const arr = new Uint8Array( buffer )
const file3dm = rhino.File3dm.fromByteArray( arr )

const rch = file3dm.settings().renderSettings().renderChannels

console.log( `renderChannels mode: ${ rch.mode.constructor.name }` )
console.log( `renderChannels customIds: ${ rch.customIds }` )

rch.mode = rhino.RenderChannelsModes.Custom
```

</div>

<div class="codetab-content3" id="cpp3">

```cpp
ONX_Model model;
model.Read(filename_in);
auto& rch = model.m_settings.m_RenderSettings.RenderChannels();
const auto mode = rch.Mode();
rch.SetMode(ON_RenderChannels::Modes::Automatic);
model.Write(filename_out);
```

</div>
</div>

## Safe Frame

[Safe Frame](/guides/cpp/rdk-safe-frame-classes/) information is accessed through `3dmRenderSettings`. To access it, you need to get the render settings and call its `SafeFrame` method/property to get a reference to a `SafeFrame` object. You can then read or write the settings by calling the various methods on the `SafeFrame` object. Any changes you make will persist and can be saved to a 3dm file:

<div class="codetab">
  <button class="tablinks4" onclick="openCodeTab(event, 'cs4')" id="defaultOpen4">C#</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'py4')">Python</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'js4')">JavaScript</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'cpp4')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content4" id="cs4">

```cs
var file3dm = File3dm.Read(filename_in);
var sf = file3dm.Settings.RenderSettings.SafeFrame;
Console.WriteLine("On:                {0}", sf.Enabled);
Console.WriteLine("ActionFrameXScale: {0}", sf.ActionFrameXScale);
sf.ActionFrameXScale = 0.45;
model.Write(filename_out);
```

</div>

<div class="codetab-content4" id="py4">

```py
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)
sf = model.Settings.RenderSettings.SafeFrame
print(sf.Enabled)
print(sf.ActionFrameXScale)
sf.ActionFrameXScale = 0.45
```

</div>

<div class="codetab-content4" id="js4">

```js
// node.js
import * as fs from 'fs' //only if running in node.js
import rhino3dm from 'rhino3dm'

const rhino = await rhino3dm()

//const file3dm = new rhino.File3dm()

const buffer = fs.readFileSync( filename_in )

/*
if you are running this in a browser, you can replace the above line with these two lines:
const file = await fetch( filename_in )
const buffer = await file.arrayBuffer()
*/

const arr = new Uint8Array( buffer )
const file3dm = rhino.File3dm.fromByteArray( arr )

const sf = file3dm.settings().renderSettings().safeFrame

console.log( `Safe Frame Enabled: ${ sf.enabled }` )
console.log( `Safe Frame ActionFrameXScale: ${ sf.actionFrameXScale }` )

sf.actionFrameXScale = 0.45
```

</div>


<div class="codetab-content4" id="cpp4">

```cpp
ONX_Model model;
model.Read(filename_in);
auto& sf = model.m_settings.m_RenderSettings.SafeFrame();
const auto on = sf.On();
const auto xs = sf.ActionFrameXScale();
sf.SetOn(true);
sf.SetActionFrameXScale(0.1f);
model.Write(filename_out);
```

</div>
</div>

## Skylight

[Skylight](/guides/cpp/rdk-skylight-classes/) information is accessed through `3dmRenderSettings`. To access it, you need to get the render settings and call its `Skylight` method/property to get a reference to a `Skylight` object. You can then read or write the settings by calling the various methods on the `Skylight` object. Any changes you make will persist and can be saved to a 3dm file:

<div class="codetab">
  <button class="tablinks5" onclick="openCodeTab(event, 'cs5')" id="defaultOpen5">C#</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'py5')">Python</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'js5')">JavaScript</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'cpp5')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content5" id="cs5">

```cs
var file3dm = File3dm.Read(filename_in);
var sl = file3dm.Settings.RenderSettings.Skylight;
Console.WriteLine("Enabled:         {0}", sl.Enabled);
Console.WriteLine("ShadowIntensity: {0}", sl.ShadowIntensity);
sl.ShadowIntensity = 1.4;
model.Write(filename_out);
```

</div>

<div class="codetab-content5" id="py5">

```py
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)
sl = model.Settings.RenderSettings.Skylight
print(sl.Enabled)
print(sl.ShadowIntensity)
sl.ShadowIntensity = 1.4
```

</div>

<div class="codetab-content5" id="js5">

```js
// node.js
import * as fs from 'fs' //only if running in node.js
import rhino3dm from 'rhino3dm'

const rhino = await rhino3dm()

//const file3dm = new rhino.File3dm()

const buffer = fs.readFileSync( filename_in )

/*
if you are running this in a browser, you can replace the above line with these two lines:
const file = await fetch( filename_in )
const buffer = await file.arrayBuffer()
*/

const arr = new Uint8Array( buffer )
const file3dm = rhino.File3dm.fromByteArray( arr )

const sl = file3dm.settings().renderSettings().skylight

console.log( `Skylight Enabled: ${ sl.enabled }` )
console.log( `Skylight Shadow Intensity: ${ sl.shadowIntensity }` )

sl.shadowIntensity = 0.45
```

</div>


<div class="codetab-content5" id="cpp5">

```cpp
ONX_Model model;
model.Read(filename_in);
auto& sl = model.m_settings.m_RenderSettings.Skylight();
const auto on = sl.Enabled();
const auto si = sl.ShadowIntensity();
sl.SetEnabled(false);
sl.SetShadowIntensity(1.4);
model.Write(filename_out);
```

</div>
</div>

## Sun

[Sun](/guides/cpp/rdk-sun-classes/) information is accessed through `3dmRenderSettings`. To access it, you need to get the render settings and call its `Sun` method/property to get a reference to a `Sun` object. You can then read or write the settings by calling the various methods on the `Sun` object. Any changes you make will persist and can be saved to a 3dm file:

<div class="codetab">
  <button class="tablinks6" onclick="openCodeTab(event, 'cs6')" id="defaultOpen6">C#</button>
  <button class="tablinks6" onclick="openCodeTab(event, 'py6')">Python</button>
  <button class="tablinks6" onclick="openCodeTab(event, 'js6')">JavaScript</button>
  <button class="tablinks6" onclick="openCodeTab(event, 'cpp6')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content6" id="cs6">

```cs
var file3dm = File3dm.Read(filename_in);
var sun = file3dm.Settings.RenderSettings.Sun;
Console.WriteLine("On:            {0}", sun.Enabled);
Console.WriteLine("Time zone:     {0}", sun.TimeZone);
var dt = sun.GetDateTime(DateTimeKind.Local);
var format = "LocalDateTime: {0}.{1}.{2} {3}:{4}";
var message = string.Format(CultureInfo.InvariantCulture,
              format, dt.Year, dt.Month, dt.Day, dt.Hour, dt.Minute);
Console.WriteLine(message);
Console.WriteLine("Place sun observer at the Greenwich observatory in London");
sun.Latitude = 51.4769;
sun.Longitude = -0.0005;
sun.TimeZone = 0.0;
model.Write(filename_out);
```

</div>

<div class="codetab-content6" id="py6">

```py
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)
sun = model.Settings.RenderSettings.Sun;
print(sun.EnableOn);
print(sun.TimeZone);
print(sun.Year, sun.Month, sun.Day, sun.Hours)
print(sun.Azimuth)
print("Place sun observer at the Greenwich observatory in London")
sun.Latitude = 51.4769;
sun.Longitude = -0.0005;
print(sun.Azimuth)
sun.TimeZone = 0.0;
```

</div>

<div class="codetab-content6" id="js6">

```js
// node.js
import * as fs from 'fs' //only if running in node.js
import rhino3dm from 'rhino3dm'

const rhino = await rhino3dm()

//const file3dm = new rhino.File3dm()

const buffer = fs.readFileSync( filename_in )

/*
if you are running this in a browser, you can replace the above line with these two lines:
const file = await fetch( filename_in )
const buffer = await file.arrayBuffer()
*/

const arr = new Uint8Array( buffer )
const file3dm = rhino.File3dm.fromByteArray( arr )

const sun = file3dm.settings().renderSettings().sun

console.log( `Sun enableOn: ${ sun.enableOn }` )
console.log( `Sun timeZone: ${ sun.timeZone }` )
console.log( `Sun azimuth: ${ sun.azimuth }` )
console.log( `Sun year: ${ sun.year }` )
console.log( `Sun month: ${ sun.month }` )
console.log( `Sun day: ${ sun.day }` )
console.log( `Sun hours: ${ sun.hours }` )
console.log('Place sun observer at the Greenwich observatory in London')
sun.latitude = 51.4769
sun.longitude = -0.0005
console.log( `Sun azimuth: ${ sun.azimuth }` )
sun.timeZone = 0.0;
```

</div>


<div class="codetab-content6" id="cpp6">

```cpp
ONX_Model model;
model.Read(filename_in);
auto& sun = model.m_settings.m_RenderSettings.Sun();
const auto on = sun.EnableOn();
const auto tz = sun.TimeZone();
sun.SetEnableOn(true);
sun.SetTimeZone(2.0);
sun.SetLocalDateTime(2022, 5, 1, 12.51);
model.Write(filename_out);
```

</div>
</div>

The sun object is able to do sun calculations and, in fact, will automatically do them whenever "manual control" is disabled (this is the default). Whenever certain properties are modified, the sun object will automatically compute the sun’s azimuth and altitude in the sky. The calculation is deferred until you actually ask for the azimuth or altitude whereupon it is performed once and cached until the next time something changes. The properties that cause the calculation to be performed are the direction of north and also any properties that change the observer’s date, time, location, time zone or daylight saving values.

When manual control is enabled, the azimuth and altitude values are under the control of the programmer and no calculations are performed.

The direction of north and the observer’s latitude and longitude are stored inside an earth anchor point object. This object is inside the 3dmSettings of the `ONX_Model`/`File3dm` and is therefore loaded and saved with the model.

## Post Effects

[Post effect](/guides/cpp/rdk-post-effects/) information is accessed through `3dmRenderSettings`. To access it, you need to get the render settings and call its `PostEffects` method/property to get a reference to a post effect collection object. This object allows you to iterate over the post effects, change the order of post effects and get and set the post effect selection. Iterating over the post effects retrieves individual post effect objects. You can access and change post effect properties by calling the various methods on the post effect object. Any changes you make will persist and can be saved to a 3dm file:

<div class="codetab">
  <button class="tablinks7" onclick="openCodeTab(event, 'cs7')" id="defaultOpen7">C#</button>
  <button class="tablinks7" onclick="openCodeTab(event, 'py7')">Python</button>
  <button class="tablinks7" onclick="openCodeTab(event, 'js7')">JavaScript</button>
  <button class="tablinks7" onclick="openCodeTab(event, 'cpp7')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content7" id="cs7">

```cs
var file3dm = File3dm.Read(filename_in);
var post_effects = file3dm.Settings.RenderSettings.PostEffects;

foreach (var post_effect in post_effects)
{
  Console.WriteLine(pep.LocalName);
  Console.WriteLine("--------------------");
  Console.WriteLine("Id   : {0}", pep.Id);
  Console.WriteLine("Type : {0}", pep.Type);
  Console.WriteLine("On   : {0}", pep.On);
  Console.WriteLine("Shown: {0}", pep.Shown);

  // If the post effect has a radius parameter, change its value.
  var p = pep.GetParameter("radius");
  if (p != null)
  {
    pep.SetParameter("radius", 0.33);
  }
}
```

</div>

<div class="codetab-content7" id="py7">

```py
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)
post_effects = model.Settings.RenderSettings.PostEffects

for pe in post_effects :
    print(pe.LocalName)
    print("--------------------")
    print("Id   : ", pe.Id)
    print("Type : ", pe.Type)
    print("On   : ", pe.On)
    print("Shown: ", pe.Shown)
    print("")
```

</div>

<div class="codetab-content7" id="js7">

```js

```

</div>


<div class="codetab-content7" id="cpp7">

```cpp
ONX_Model model;
model.Read(filename_in);

auto& post_effects = model.m_settings.m_RenderSettings.PostEffects();
ON_SimpleArray<ON_PostEffect*> post_effect_array;
post_effects.GetPostEffects(ON_PostEffect::Types::Early, post_effect_array);
for (int i = 0; i < post_effect_array.Count(); i++)
{
  auto& post_effect = *post_effect_array[i];

  if (post_effect.LocalName().CompareNoCase(L"bloom") == 0)
  {
    post_effect.SetParameter(SS_PEP_BLOOM_INTENSITY, 123.0f);
    const auto v = post_effect.GetParameter(SS_PEP_BLOOM_INTENSITY);
    ASSERT(v.AsFloat() == 123.0f);
  }
}

model.Write(filename_out);
```

</div>
</div>

## Render Content

["Render content"](/guides/cpp/rdk-render-content/) is an abstraction that represents one of three different kinds of object. A render content can be a:

1. Render Material
1. Render Environment
1. Render Texture

Render contents are model components and, in C++, can be accessed by iterating over the model components in a model. In C# you iterate over lists of each kind. Each kind is a subclass of the render content class. The base class contains all methods/properties that are common to all three kinds, and each subclass contains only the methods/properties specific to that kind.

<div class="codetab">
  <button class="tablinks8" onclick="openCodeTab(event, 'cs8')" id="defaultOpen8">C#</button>
  <button class="tablinks8" onclick="openCodeTab(event, 'py8')">Python</button>
  <button class="tablinks8" onclick="openCodeTab(event, 'js8')">JavaScript</button>
  <button class="tablinks8" onclick="openCodeTab(event, 'cpp8')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content8" id="cs8">

```cs
var file3dm = File3dm.Read(filename_in);

foreach (var rm in file3dm.RenderMaterials)
{
  Console.WriteLine("{0}", rm.TypeName);

  IConvertible p = rm.GetParameter("ior");
  if (p != null)
  {
    Console.WriteLine("Setting IOR and transparency");
    rm.SetParameter("ior", 2.5);
    rm.SetParameter("transparency", 0.5);
  }
}

foreach (var re in file3dm.RenderEnvironments)
{
  var env = re.ToEnvironment();
  var col = env.BackgroundColor;
  Console.WriteLine("Color: {0}, {1}, {2}", col.R, col.G, col.B);
}

foreach (var rt in file3dm.RenderTextures)
{
  var tex = rt.ToTexture();
  Console.WriteLine("{0}", tex.FileReference.FullPath);
}
```

</div>

<div class="codetab-content8" id="py8">

```py
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)

for rc in model.RenderContent :
    if isinstance(rc, _rhino3dm.RenderMaterial) :
       print(rc.TypeName)
       print(rc.GetParameter("ior"))
       print("Setting IOR and transparency")
       _ = rc.SetParameter("ior", "2.5")
       _ = rc.SetParameter("transparency", "0.5")
    if isinstance(rc, _rhino3dm.RenderEnvironment) :
       e = rc.ToEnvironment()
       print(e.BackgroundColor)
    if isinstance(rc, _rhino3dm.RenderTexture) :
       print(rc.Filename)
```

</div>

<div class="codetab-content8" id="js8">

```js

```

</div>

<div class="codetab-content8" id="cpp8">

```cpp
ONX_Model model;
model.Read(filename_in);

ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::RenderContent);
auto* component = it.FirstComponent();
while (nullptr != component)
{
  const auto* mat = ON_RenderMaterial::Cast(component);
  if (nullptr != mat)
  {
    const auto typeName = mat->TypeName();
    wprintf(L"Type: %s\n", static_cast<const wchar_t*>(typeName));

    const auto v = mat->GetParameter(ON_MATERIAL_IOR);
    if (!v.IsNull())
    {
      wprintf(L"Setting IOR and transparency\n");
      auto* mat_write = const_cast<ON_RenderMaterial*>(mat);
      mat_write->SetParameter(ON_MATERIAL_IOR, 2.5);
      mat_write->SetParameter(ON_MATERIAL_TRANSPARENCY_AMOUNT, 0.5);
    }
  }

  component = it.NextComponent();
}

component = it.FirstComponent();
while (nullptr != component)
{
  auto* env = ON_RenderEnvironment::Cast(component);
  if (nullptr != env)
  {
    const auto on_env = env->ToOnEnvironment();
    const auto col = on_env.BackgroundColor();
    wprintf(L"Color: %u, %u, %u\n", col.Red(), col.Green(), col.Blue());
  }

  component = it.NextComponent();
}

component = it.FirstComponent();
while (nullptr != component)
{
  auto* tex = ON_RenderTexture::Cast(component);
  if (nullptr != tex)
  {
    const auto on_tex = tex->ToOnTexture();
    const auto& file = on_tex.m_image_file_reference.FullPath();
    wprintf(L"%s\n", static_cast<const wchar_t*>(file));
  }

  component = it.NextComponent();
}
```

</div>
</div>

## Embedded Files

Embedded Files (not to be confused with Embedded Bitmaps) are files that are embedded inside a 3dm file. When a render texture is file-based (i.e., most non-procedural textures), then by default, Rhino saves a copy of the referenced file in the 3dm file. This can be disabled during Save As by unchecking the Save textures check box. These files can be accessed by the programmer by iterating over model components of type `EmbeddedFile`. Although the embedded file object contains a number of methods for loading and saving files in different ways, iterating over the model is probably the most useful way to use it:

<div class="codetab">
  <button class="tablinks9" onclick="openCodeTab(event, 'cs9')" id="defaultOpen9">C#</button>
  <button class="tablinks9" onclick="openCodeTab(event, 'py9')">Python</button>
  <button class="tablinks9" onclick="openCodeTab(event, 'js9')">JavaScript</button>
  <button class="tablinks9" onclick="openCodeTab(event, 'cpp9')">C/C++</button>
</div>

<div class="tab-content">
<div class="codetab-content9" id="cs9">

```cs
var file3dm = File3dm.Read(filename_in);

foreach (var ef in file3dm.EmbeddedFiles)
{
  var dir  = System.IO.Path.GetDirectoryName(ef.Filename);
  var file = System.IO.Path.GetFileName(ef.Filename);
  var new_file = System.IO.Path.Combine(dir, "CopyOf_" + file);
  ef.SaveToFile(new_file);
}
```

</div>

<div class="codetab-content9" id="py9">

```py
import os
import _rhino3dm
model = _rhino3dm.File3dm.Read(filename_in)

for ef in model.EmbeddedFiles :
    dir = os.path.dirname(ef.Filename)
    file = os.path.basename(ef.Filename)
    new_file = os.path.join(dir, "CopyOf_" + file)
    ef.Write(new_file)
```

</div>

<div class="codetab-content9" id="js9">

```js

```

</div>

<div class="codetab-content9" id="cpp9">

```cpp
ONX_Model model;
model.Read(filename_in);

ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::EmbeddedFile);
const auto* component = it.FirstComponent();
while (nullptr != component)
{
  const auto* ef = ON_EmbeddedFile::Cast(component);
  if (nullptr != ef)
  {
    const auto filename = ef->Filename();
    const auto dir  = ON_FileSystemPath::VolumeAndDirectoryFromPath(filename);
    const auto file = ON_FileSystemPath::FileNameFromPath(filename, true);
    const auto new_file = dir + L"CopyOf_" + file;
    ef->SaveToFile(new_file);
  }

  component = it.NextComponent();
}
```d

</div>
</div>

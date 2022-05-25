+++
authors = [ "dale" ]
categories = [ "RDK" ]
description = "This brief guide discusses light attenuation in Rhino."
keywords = [ "rhino", "light" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Light Attenuation"
type = "guides"
weight = 4

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/lightattenuation"
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

 
## Problem

So you are interested in taking advantage `ON_Light::Attenuation` in your render plugin, and you need to clarify how you can use it.  Is the input vector supposed to represent the distance over which you want the light to attenuate to zero?

## Solution

Light attenuation determines how fast the light intensity decreases with distance from objects.

The three coefficients to light attenuation are:

1. Constant attenuation ({{< mathjax >}}$$C$${{< /mathjax >}})
1. Linear attenuation ({{< mathjax >}}$$L$${{< /mathjax >}})
1. Quadratic attenuation ({{< mathjax >}}$$Q$${{< /mathjax >}})

Thus, you could create the input vector as follows:

```cpp
ON_3dVector attenuation( C, L, Q );
```

**NOTE**: Rhino's user interface only uses constant attenuation so that adding a light reveals everything, no matter how far away the light source is from any given piece of geometry.

## Types of Attenuation

### Constant

If you want constant attenuation, or:

{{< mathjax >}}$$1 \over C$${{< /mathjax >}}

then both {{< mathjax >}}$$L$${{< /mathjax >}} and {{< mathjax >}}$$Q$${{< /mathjax >}} must be {{< mathjax >}}$$0$${{< /mathjax >}} and {{< mathjax >}}$$C > 0$${{< /mathjax >}} (usually {{< mathjax >}}$$= 1.0$${{< /mathjax >}}).

### Linear

If you want linear attenuation:

{{< mathjax >}}$$1 \over C + dL$${{< /mathjax >}}

where {{< mathjax >}}$$d$${{< /mathjax >}} = distance to light, then {{< mathjax >}}$$C$${{< /mathjax >}} and {{< mathjax >}}$$L$${{< /mathjax >}} vary and {{< mathjax >}}$$Q$${{< /mathjax >}} must be {{< mathjax >}}$$0$${{< /mathjax >}}.

### Quadratic

If you want quadratic attenuation:

{{< mathjax >}}$$1 \over C + dL + d^{2Q}$${{< /mathjax >}}

then all 3 coefficients can and should vary.

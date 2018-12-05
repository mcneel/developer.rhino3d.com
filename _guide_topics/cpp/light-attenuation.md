---
title: Light Attenuation
description: This brief guide discusses light attenuation in Rhino.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/developer/sdksamples/lightattenuation
order: 4
keywords: ['rhino', 'light']
layout: toc-guide-page
---

 
## Problem

So you are interested in taking advantage `ON_Light::Attenuation` in your render plugin, and you need to clarify how you can use it.  Is the input vector supposed to represent the distance over which you want the light to attenuate to zero?

## Solution

Light attenuation determines how fast the light intensity decreases with distance from objects.

The three coefficients to light attenuation are:

1. Constant attenuation ($$C$$)
1. Linear attenuation ($$L$$)
1. Quadratic attenuation ($$Q$$)

Thus, you could create the input vector as follows:

```cpp
ON_3dVector attenuation( C, L, Q );
```

**NOTE**: Rhino's user interface only uses constant attenuation so that adding a light reveals everything, no matter how far away the light source is from any given piece of geometry.

## Types of Attenuation

### Constant

If you want constant attenuation, or:

$$1 \over C$$

then both $$L$$ and $$Q$$ must be $$0$$ and $$C > 0$$ (usually $$= 1.0$$).

### Linear

If you want linear attenuation:

$$1 \over C + dL$$

where $$d$$ = distance to light, then $$C$$ and $$L$$ vary and $$Q$$ must be $$0$$.

### Quadratic

If you want quadratic attenuation:

$$1 \over C + dL + d^{2Q}$$

then all 3 coefficients can and should vary.

---
title: Morphing a Surface
description: An example of how to morph a surface using RhinoScript.
authors: ['stylianos_dritsas']
author_contacts: ['']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Surfaces']
origin: http://wiki.mcneel.com/developer/scriptsamples/morph
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
''
'' Morphing example (morph.rvb)
''
'' Copyright  2004 Stylianos Dritsas
''
'' This software is provided 'as-is', without any expressed or implied warranty.
'' In no event will the author be held liable for any damages arising from the
'' use of this software.
''
'' Permission is granted to anyone to use this software for any purpose,
'' including commercial applications, and to alter it and redistribute it
'' freely, subject to the following restrictions:
''
'' 1. The origin of this software must not be misrepresented; you must not
'' claim that you wrote the original software. If you use this software
'' in a product, an acknowledgment in the product documentation would be
'' appreciated but is not required.
'' 2. Altered source versions must be plainly marked as such, and must not be
'' misrepresented as being the original software.
'' 3. This notice may not be removed or altered from any source distribution.
''
'' Stylianos Dritsas dritsas@alum.mit.edu
''
Dim u: u = 0: Dim min: min = 0
Dim v: v = 1: Dim max: max = 1
sa = Rhino.GetObject( "sa" )
sb = Rhino.GetObject( "sb" )
Dim steps: steps = 12
For i = 1 To steps - 1
  Call surface_interpolate( sa, sb, 10, 10, i/steps )
Next
Function surface_interpolate( sa, sb, cols, rows, factor )
  Dim nu: nu = cols
  Dim nv: nv = rows
  Dim cpa: cpa = Array( nu, nv )
  Dim cpb: cpb = Array( nu, nv )
  Dim da: da = Array( Rhino.surfacedomain( sa, U ), Rhino.surfacedomain( sa, V ) )
  Dim db: db = Array( Rhino.surfacedomain( sb, U ), Rhino.surfacedomain( sb, V ) )
  Dim dua: dua = ( da( U )( MAX ) - da( U )( MIN ) ) / ( cpa( U ) - 1 )
  Dim dva: dva = ( da( V )( MAX ) - da( V )( MIN ) ) / ( cpa( V ) - 1 )
  Dim ua: ua = da( U )( MIN )
  Dim va: va = da( V )( MIN )
  Dim dub: dub = ( db( U )( MAX ) - db( U )( MIN ) ) / ( cpb( U ) - 1 )
  Dim dvb: dvb = ( db( V )( MAX ) - db( V )( MIN ) ) / ( cpb( V ) - 1 )
  Dim ub: ub = db( U )( MIN )
  Dim vb: vb = db( V )( MIN )
  Dim point: point = 0
  ReDim points( nu * nv - 1 )
  Dim pu, pv
  For pu = 0 To nu - 1
    For pv = 0 To nv - 1
      Dim pa: pa = Rhino.evaluatesurface( sa, Array( pu * dua + ua, pv * dva + va ) )
      Dim pb: pb = Rhino.evaluatesurface( sb, Array( pu * dub + ub, pv * dvb + vb ) )
      points( point ) = vertex_interpolate( pa, pb, factor )
      point = point + 1
    Next
  Next
  surface_interpolate = Rhino.addsrfptgrid( cpa, points )
End Function
```

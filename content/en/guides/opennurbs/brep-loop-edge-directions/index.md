+++
authors = [ "dalelear" ]
categories = [ "Fundamentals" ]
description = "This guide discusses Brep loop end edge directions in the openNURBS toolkit."
keywords = [ "openNURBS", "Brep", "Loop", "Edge", "Directions" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS" ]
title = "Brep Loop & Edge Directions"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/onloopdirection"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Question

Is there a function to query if a loop `ON_BrepLoop` is reversed on the face `ON_BrepFace`?  In other words, whether the boundary of the face agrees with or opposes that of the corresponding loop?

Also, is there a way to query if the edge `ON_BrepEdge` direction is reversed?  Or, whether an edge curve agrees with the start and end vertices?

## Answer

Loops are always oriented so that the active region of the face is to the left of the 2D curve.  Thus, outer loops are oriented counter-clockwise and inner loops are oriented clockwise.

Also, to determine whether or not an edge is reversed, use `ON_BrepEdge::ProxyCurveIsReversed()`.  See *opennurbs_curveproxy.h* for details.

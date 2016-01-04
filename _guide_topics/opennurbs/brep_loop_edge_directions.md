---
title: Brep Loop & Edge Directions
description: unset
author: dalelear@mcneel.com
apis: ['openNURBS']
languages: ['C/C++']
platforms: ['Cross-Platform']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/onloopdirection
order: 1
keywords: ['openNURBS', 'Brep', 'Loop', 'Edge', 'Directions']
layout: toc-guide-page
---

# Brep Loop & Edge Directions

This guide discusses Brep loop end edge directions in the openNURBS toolkit.

## Question

Is there a function to query if a loop `ON_BrepLoop` is reversed on the face `ON_BrepFace`?  In other words, whether the boundary of the face agrees with or opposes that of the corresponding loop?

Also, is there a way to query if the edge `ON_BrepEdge` direction is reversed?  Or, whether an edge curve agrees with the start and end vertices?

## Answer

Loops are always oriented so that the active region of the face is to the left of the 2D curve.  Thus, outer loops are oriented counter-clockwise and inner loops are oriented clockwise.

Also, to determine whether or not an edge is reversed, use `ON_BrepEdge::ProxyCurveIsReversed()`.  See *opennurbs_curveproxy.h* for details.

---
title: Superfluous Knots
description: This guide discusses superfluous knots and the openNURBS toolkit.
authors: ['dale_lear']
author_contacts: ['dalelear']
sdk: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/onsuperfluousknot
order: 1
keywords: ['openNURBS', 'knots']
layout: toc-guide-page
---

 
## Question

How is the representation of knot vector in openNURBS different from that in OpenGL's NURBS renderer?  In openNURBS, the formula is:

$$m = n + p - 2 $$

where m is the number of knots in the knot vector; n is the number of control points; p is the order of the curve.

While in OpenGL, the formula is:

$$m = n + p$$

So, in OpenGL, there are two additional knots required to draw a NURBS curve.

Could you explain how the two knot values are calculated?  And, why openNURBS adopted a representation different from most NURBS books?

## Answer

The knots are superfluous because they are not used in NURBS evaluation and they make it appear the first and last spans are different from interior spans.

If you grab a pencil and paper and work through the details you will understand why dragging around and setting these two knot values is a waste of time and adds needless complications to NURBS evaluation, NURBS degree changing, NURBS knot insertion/deletion, NURBS span conversion to/from bezier, NURBS periodic closure, NURBS curve fitting, etc., algorithms.  If you look at the openNURBS evaluation source code, you will see no knot juggling; it's just a simple computationally efficient calculation.

One reason some mathematical texts on NURBS, like Carl DeBoor's b-splines, have the extra knots is that it makes proving the theorems easier because it means that the recursive b-spline basis function definition DeBoor uses is well defined for degree zero b-splines.  DeBoor's use of the recursive definition of the basis functions is elegant and having the extra knot values along helps make them elegant.

There is no good reason for modern computer code or text books focused solely on computer aided applications of NURBS to drag this kind of theoretical baggage along.  Having modern code drag these knot values around is akin to having Excel store prime factors of integer cell entries and requiring Excel add-in developers to compute the factorization.  Prime factorization is fundamental to understanding how integers work and it is interesting to people that it interests, but it is not required if all you are trying to do is add/subtract/multiply integers in spreadsheet cells.

Why the creators of the OpenGL specification, IGES NURBS specification, and STEP NURBS specification decided to store two useless values in their knot vectors is a mystery to us.

Rhino and openNURBS are not the only applications and toolkits that don't carry around the extra knots. The older versions of Alias and ACIS that we are familiar with do not have the extra knots.

+++
aliases = ["/5/guides/opennurbs/what-is-opennurbs/", "/6/guides/opennurbs/what-is-opennurbs/", "/7/guides/opennurbs/what-is-opennurbs/", "/wip/guides/opennurbs/what-is-opennurbs/"]
authors = [ "dalelear" ]
categories = [ "Overview" ]
description = "This guide gives an overview of the openNURBS toolkit."
keywords = [ "openNURBS", "overview" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS" ]
title = "What is openNURBS?"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/opennurbs/faq"
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

## Overview

The openNURBS Initiative provides CAD, CAM, CAE, and computer graphics software developers the tools to accurately transfer 3-D geometry between applications.

The openNURBS Toolkit consists of C++ source code for a library that will read and write openNURBS 3D model files (*.3dm*). More than 400 software development teams and applications, including *Rhinoceros®*, exchange 3D models using the openNURBS (*.3dm*) file format.

The openNURBS Toolkit reads and writes all Rhino 3DM files. Additionally, the openNURBS Toolkit provides NURBS evaluation tools and elementary geometric and 3D view manipulation tools.

Unlike other open development initiatives, alliances, or consortia:

- Commercial use is encouraged.
- The tools, support, and membership are free.
- There are no restrictions. Neither copyright nor copyleft restrictions apply.
- No contribution of effort or technology is required from the members, although it is encouraged.

The openNURBS Toolkit is intended for C++ programmers. The toolkit includes complete source code to create a library that will read and write 3DM files. The toolkit also includes source code for several example programs.

## Details

The tools provided by openNURBS include:

- [openNURBS C++ source SDK and samples](https://www.rhino3d.com/download/openNURBS/7/release) - the original cross platform SDK.
- Quality assurance and revision control.
- Technical support.

## Limitations

Although the openNURBS toolkit appears to be a full-featured geometry library, it is not. The toolkit does not include a number of important features, including:

- Closest point calculations
- Intersection calculations
- Surface tessellation (meshing)
- SubD to Brep conversion
- Interpolation
- Booleans
- Area and mass property calculations
- Other miscellaneous geometry calculations

openNURBS is an open source toolkit for only reading and writing 3DM models. Our full-featured development platform is *Rhinoceros®*. All of the above features are found in the Rhino SDKs, the toolkit used to build plugins for Rhino.

## Who is funding the openNURBS Initiative and why?

Robert McNeel & Associates. We feel that the 3-D market is stifled because of the inability to reliably transfer 3-D geometry between applications. The problem is too big for us to solve alone. By funding the operating cost of openNURBS, others will get involved in the toolkit design and development. It will be a much cheaper and effective way to solve the problem.

## References

The following are references to fundamental work on NURBS:

- Bohm, Wolfgang, Gerald Farin, Jurgen Kahman (1984). *A survey of curve and surface methods in CAGD*, Computer Aided Geometric Design Vol 1. 1-60
- DeBoor, Carl. (1978).  *A Practical Guide To Splines*, Springer Verlag; ISBN: 0387953663
- Farin, Gerald. (1997). *Curves and Surfaces for Computer-Aided Geometric Design: A Practical Guide*, 4th edition, Academic Press; ISBN: 0122490541

## Related Topics

- [openNURBS Migration Guide](/guides/opennurbs/migration-guide)

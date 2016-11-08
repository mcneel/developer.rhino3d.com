---
title: Getting Started
description: This guide aims to get you started using openNURBS in your project.
author: ['Dale Lear', '@dalelear']
apis: ['openNURBS']
languages: ['C/C++', 'C#']
platforms: ['Windows', 'Mac']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/opennurbs/faq
order: 2
keywords: ['openNURBS', 'C#', '.NET', 'Rhino3dmIO']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Prerequisites

openNURBS is intended for *skilled* C++ and .NET developers. Please read [What is openNURBS?]({{ site.baseurl }}/guides/opennurbs/what_is_opennurbs) if you have not already.  It is also presumed that you have an application that wishes to access *3dm* files outside of Rhinoceros.

## Supported Compilers

The openNURBS C++ toolkit has been successfully used with the following compilers:

- *Microsoft Visual Studio 2010* (VC 10.0 SP1) (Windows 7 Professional SP1): to build openNURBS and the examples with *Visual Studio 2010 SP1*, use the solution *build_opennurbs_vs2010.sln*.
- *gcc version 4.2.1* (Apple Build 5658): to build openNURBS and the examples with gcc use the makefile.
- *Apple Xcode 4.6.3* (4H1503) (OSX 10.8.2): To build openNURBS and the examples with *Xcode 4.5* (or later), use the workspace *build_opennurbs_xcode.workspace*.

The openNURBS C++ source code is clean and simple.  You should be able to use any good C++ compiler that has 32-bit integers, 32-bit or 64-bit pointers, and `wchar_t` support.

If you are using a good quality C++ compiler and run into some toolkit code that causes problems, please [let us know](http://discourse.mcneel.com/category/opennurbs).  We'll attempt to change the code to accommodate the compiler.

## Read and Write

If your goal is to read and write 3DM files, then you may find that the class `ONX_Model::Read()` and `ONX_Model::Write()` an easy route.  See *example_read.cpp* and *example_write.cpp* for more details.

1. Compile the openNURBS Toolkit library.  To compile the example programs you must link with the openNURBS Toolkit library.
1. Study *example_read\example_read.cpp*.  All the openNURBS geometry classes are derived from the `ON_Geometry` class.  If you need generic attribute information, there is probably an `ON_Geometry` member function that will answer your query.  See the `Dump()` function in *example_read.cpp* for code that demonstrates how to use the `Cast()` function to get at the actual class definitions.
1. Study *example_write\example_write.cpp*.  If you want to write points, meshes, NURBS curves, NURBS surfaces, or trimmed NURBS surfaces, you should be able to cut and paste most of what you need from the functions in *example_write.cpp*.  If you want to write trimmed surfaces or b-reps, then please study *example_brep.cpp*.
1. Study *example_brep\example_brep.cpp*.  If you want to write solid models or more general b-reps, then first work through *example_write.cpp* and then work through *example_brep.cpp*.
1. The comments in the openNURBS Toolkit header files are the primary source of documentation.  I suggest that you use a development environment that has high quality tags capabilities and a good class browser.
1. In the code you write include only *opennurbs.h*. The *opennurbs.h* header file includes the necessary openNURBS toolkit header files in the appropriate order.
1. Other items to note:
     1. openNURBS uses UTF-16 to store text in *3dm* files and provides tools for converting UTF-16 strings to and from UTF-8, UTF-32 and `wchar_t` strings.  The `ON_wString` class has `wchar_t` characters.
     1. All memory allocations and frees are done through `onmalloc()`, `onfree()`, and `onrealloc()`.  The source that ships with openNURBS has `onmalloc()` call `malloc()` and `onfree()` call `free()`.
     1. If you want to use Open GL to render openNURBS geometry, you may want to include *opennurbs_gl.h* after *opennurbs.h* and add *opennurbs_gl.cpp* to your openNURBS library.  See *example_gl.cpp* for details.
     1. The openNURBS Toolkit works correctly on both big and little endian CPUs. (Generally, Intel CPUs use little endian byte order and MIPS, Motorola, and Sparc CPUs use big endian byte order.)

## 3DM File Versions

The following is brief history of the 3dm file versions...

1. *Version 1 3DM files*. The openNURBS toolkit will read version 1 files.  Rhino 1 and other applications using the old Rhino I/O toolkit create version 1 files.
1. *Version 2 3DM files*. The openNURBS toolkit will read and write version 2 files.  Rhino 2 and applications using an openNURBS toolkit released on or after December 2000 create version 2 files.  (Rhino 1 and the old Rhino I/O toolkit will not read version 2 files.)
1. *Version 3 3DM files*. The openNURBS toolkit will read and write version 3 files.  Rhino 3 and applications using an openNURBS toolkit released on or after October 2002 create version 3 files.  (Rhino 1 and Rhino 2 will not read version 2 files.)
1. *Version 4 3DM files*. The openNURBS toolkit will read and write version 4 files.  Rhino 4 and applications using an openNURBS toolkit released on or after September 2006 create version 4 files.  (Rhino 1, Rhino 2, and Rhino 3 will not read version 4 files.)
1. *Version 5 3DM files*. The openNURBS toolkit will read and write version 5 files.  Rhino 5 and applications using an openNURBS toolkit released on or after September 2009 create version 5 files.  (Rhino 1, Rhino 2, Rhino 3 and Rhino 4 will not read version 5 files.)

## Examples

This is an overview of the examples included with the openNURBS toolkit:

- *example_read\example_read.cpp*: Create a program by compiling *example_read.cpp* and statically linking with the openNURBS library.  The code in *example_read.cpp* illustrates how to read an openNURBS *.3dm* file.
- *example_write\example_write.cpp*: Create a program by compiling *example_write.cpp* and linking with the openNURBS library.  The code in *example_write.cpp* illustrates how to write layers, units system and tolerances, viewports, spotlights, points, meshes, NURBs curves, NURBs surfaces, trimmed NURBs surfaces, texture and bump map information, render material name, and material definitions to an openNURBS *.3dm* file.  
- The bitmap in *example_write\example_texture.bmp* is used for a rendering material texture in *example_write\example_write.cpp*.
- *example_brep\example_brep.cpp*: Create a program by compiling *example_brep.cpp* and linking with the openNURBS library.  The code in *example_write.cpp* illustrates how to write a solid model.
- *example_dump\example_dump.cpp*: Create a program by compiling *example_dump.cpp* and linking with the openNURBS library.  The code in *example_dump* demonstrates the low level structure of an openNURBS *.3dm* file.
- *example_userdata\example_userdata.cpp*: Create a program by compiling *example_userdata.cpp* and linking with the openNURBS library.  The code in *example_userdata* demonstrates how to create and manage arbitrary user defined information in *.3dm* files.
- *The Open GL example*: Past versions of openNURBS have included a crude version of an Open GL example.  The code for this example is still included in the current version, but we no longer provide support for using OpenGL with openNURBS.  Nothing has changed in openNURBS with respect to using OpenGL.  We simply do not have the resources to provide quality OpenGL support on the wide variety of platforms where openNURBS is used.

## Common Issues

### ON_Mesh

#### Vertex ordering in ON_Mesh faces

All faces in a `ON_Mesh` are stored with vertices listed in counter-clockwise order.  In particular, for quads the vertices are ordered as:

![Vertex Ordering]({{ site.baseurl }}/images/opennurbs_getting_started_01.png)

The quads may be non-planar.

The definition of `void ON_GL( const ON_Mesh& )` in *opennurbs_gl.cpp* demonstrates how to go through an `ON_Mesh` and render all the quads as two triangles.

### ON_Brep

#### Orientation of ON_Brep faces

The UV orientation of surfaces in a Brep is arbitrary.  If the `BOOL ON_BrepFace::m_bRev` member is `FALSE`, then the face's orientation agrees with the surface's natural $$Du \times Dv$$ orientation.  When the member is `TRUE`, the face's orientation is opposite the surface's natural $$Du \times Dv$$ orientation.

If your application cannot handle `ON_BrepFaces` that have a `TRUE` `m_bRev` flag, then call `ON_Brep::FlipReversedSurfaces()`.  See the comments in `ON_Brep::FlipReversedSurfaces()` and `ON_Brep::SwapFaceParameters()` for details.

#### Trimming loop order and nesting

The `ON_BrepLoop::m_type` member records the type of boundary (inner, outer, etc.).  A `ON_BrepFace` has exactly one outer loop and it is the first loop referenced in the `ON_BrepFace::m_li[]` array.  The inner loops all define "holes" in the `ON_BrepFace`.  All the inner holes lie inside of the outer loop.  A `ON_BrepFace` is always path connected.  In particular, inner loops are not "nested."

#### Surfaces in Rhino are read as ON_Breps

Internally, Rhino stores all surfaces as some type of b-rep and the openNURBS toolkit reads these objects as b-reps. To see if an entire

`ON_Brep` is really just a surface, use:

`BOOL ON_Brep::IsSurface()`

If `ON_Brep::IsSurface()` returns `TRUE`, then the b-rep geometry is the same as the surface `ON_Brep::m_S[0]`.

To see of a particular face in a b-rep is really just a surface, use:

`BOOL ON_Brep::FaceIsSurface( face_index )`

If `ON_Brep::FaceIsSurface( face_index )` returns `TRUE`, then the face's geometry is the same as the surface `ON_Brep::m_S[face.m_si]`.

---

## Related Topics

- [What is openNURBS?]({{ site.baseurl }}/guides/opennurbs/what_is_opennurbs)
- [What is Rhino3dmIO?]({{ site.baseurl }}/guides/opennurbs/what_is_rhino3dmio)

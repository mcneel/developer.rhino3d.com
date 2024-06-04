+++
aliases = ["/5/guides/rhinopython/primer-101/", "/6/guides/rhinopython/primer-101/", "/7/guides/rhinopython/primer-101/", "/wip/guides/rhinopython/primer-101/"]
authors = [ "skylar-tibbits", "arthur-van-der-harten", "steve" ]
categories = [ "Unsorted" ]
description = "A full course on Rhino.Python"
keywords = [ "rhino", "developer" ]
languages = "unset"
sdk = "unset"
title = "Rhino.Python 101"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T13:57:39Z"
draft = false

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 7
until = 0

+++

<div class="row">
<div class="col-md-12" markdown="1">  

</div>
<div class="col-md-8 col-sm-12 col-sm-12" markdown="1">  
{{< image url="/images/primer-normals.svg" alt="/images/primer-normals.svg" width="30%" class="float_right" >}}

You’ve just opened the first edition of the Rhino Python primer. This guide [was originally written](/guides/rhinoscript/primer-101) by <a href="https://discourse.mcneel.com/u/davidrutten/summary">David Rutten</a> for Rhino 4 and VBscript and has now been translated to encompass [Python for Rhino 6](/guides/rhinopython). As always, this primer is intended to teach programming to absolute beginners, people who have tinkered with programming a bit or expert programmers looking for a quick introduction to the methods in Rhino.  [Rhinoscript](/guides/rhinoscript) (VBscript) has been supported for many years, with a large user group and extensive support material. As well as giving a basic introduction, this primer looks to easily transition those familiar with VBscript into the world of Rhino Python.  For this reason, David Rutten's original primer has been used extensively as the underlying framework for this Python Primer. Python offers exciting new potentials for programming in Rhino with Object-Oriented functionality, simple syntax, access to the .NET framework and a vast number of user-built libraries to extend Rhino's functionality. The same powerful methods that were previously in VBscript are still available, as well as a ton of other exciting methods and features available natively with Python.  

Similar to the previous primers, we have the advantage of using geometric and visual examples to help teach programming. In many traditional scenarios, programming is taught with non-visual examples and difficult to understand engineering problems. For this reason, as well as Python's easy-to-read syntax, we should hopefully be able to bring everyone to understand and write simple programs to help automate and design within Rhino.

{{< div class="clear_both" />}}

{{< image url="/images/primer-branchpropagation2.svg" alt="/images/primer-branchpropagation2.svg" width="30%" class="float_right" >}}

Programming offers users the powerful ability to automate tasks, make decisions, perform powerful calculations and geometric manipulations, thus, essentially acting as a designer's side kick. This can allow thousands of computations to occur based on dynamic conditions, something that would take a human far too long to process. As a tool for iteration, generation, analysis and design evolution, programming is limitless! Programming also offers a new language to communicate with the world because almost every discipline, from the Sciences, Engineering to Art, utilize code as a progressive new medium - and this primer should hopefully give you an easy introduction into this powerful language for communicating with the world. (With that example, it should be noted that programming may be looked at as any other human language in the sense that it truly takes many hours of practice to become fluent. So don't get discouraged if you aren't an expert in one day!)

I hope we have convinced you of the powerful and exciting potential for this new opportunity of Python in Rhino. Without further ado, lets dive in!  

Good luck!   

</div>  

  
</div>  

{{< row >}}

{{< column >}}  

**Skylar Tibbits**<br/>
<a href="http://www.sjet.us">SJET</a><br/>
<a href="http://www.scriptedbypurpose.net">www.scriptedbypurpose.net</a>

{{< /column >}}
{{< column >}}  

**Arthur van der Harten**<br/>
<a href="http://www.kirkegaard.com">Kirkegaard Associates</a><br/>
<a href="http://www.perspectivesketch.com">www.perspectivesketch.com</a>

{{< /column >}}
{{< column >}}

**Steve Baer**<br/>
<a href="http://www.rhino3d.com">Robert McNeel & Associates</a>
{{< /column >}}  
{{< /row >}}  

<div class="row">  
<div class="col-md-12" markdown="1">  

*A special thanks to David Rutten for the inspiration and invaluable work, pioneering the original [RhinoScript 101 Primer](/guides/rhinoscript/primer-101). Also many thanks to Bob McNeel and everyone at Robert McNeel & Associates for their generous support!*

[{{< awesome "fas fa-download">}} ](http://download.rhino3d.com/IronPython/5.0/RhinoPython101/)  [Download the Rhino.Python 101 Primer as a single PDF ](http://download.rhino3d.com/IronPython/5.0/RhinoPython101/)

### Table of Contents  
</div>  
</div>  

{{< row >}}  
{{< column >}}  

### 1. [What's it all about?](/guides/rhinopython/primer-101/1-whats-it-all-about/)

   1.1 [Macros](/guides/rhinopython/primer-101/1-whats-it-all-about/#macros)  
   1.2 [Scripts](/guides/rhinopython/primer-101/1-whats-it-all-about/#scripts)  
   1.3 [Running Scripts](/guides/rhinopython/primer-101/1-whats-it-all-about/#scripts-1)  

### 2. [Python Essentials](/guides/rhinopython/primer-101/2-python-essentials/)  

   2.1	[Language Origin](/guides/rhinopython/primer-101/2-python-essentials/#language-origin)  
   2.2	[Flow Control](/guides/rhinopython/primer-101/2-python-essentials/#flow-control)  
   2.3	[Variable Data](/guides/rhinopython/primer-101/2-python-essentials/#variable-data)  
&nbsp;&nbsp; 2.3.1	[Integers and Doubles](/guides/rhinopython/primer-101/2-python-essentials/#integers-and-doubles/)  
&nbsp;&nbsp; 2.3.2	[Booleans]((/guides/rhinopython/primer-101/2-python-essentials/#booleans/))  
&nbsp;&nbsp; 2.3.3	[Strings]((/guides/rhinopython/primer-101/2-python-essentials/#strings/))  
&nbsp;&nbsp; 2.3.4	[None Variable](/guides/rhinopython/primer-101/2-python-essentials/#none-variable/)  
&nbsp;&nbsp; 2.3.5	[Using Variables]((/guides/rhinopython/primer-101/2-python-essentials/#using-variables/))  

### 3. [Script Anatomy](/guides/rhinopython/primer-101/3-script-anatomy/)

   3.1 [Programming in Rhino](/guides/rhinopython/primer-101/3-script-anatomy/#31-programming-in-rhino)    
   3.2 [The Bones](/guides/rhinopython/primer-101/3-script-anatomy/#32-the-bones)  
   3.3 [The Buts](/guides/rhinopython/primer-101/3-script-anatomy/#33-the-guts)  
   3.4 [The Skin](/guides/rhinopython/primer-101/3-script-anatomy/#34-the-skin)  
   3.5 [The Debugger](/guides/rhinopython/primer-101/3-script-anatomy/#35-the-debugger)   

{{< /column >}}
{{< column >}}

### 4. [Operators and Functions](/guides/rhinopython/primer-101/4-operators-and-functions/)

   4.1	[What on Earth are they and why should I care?](/guides/rhinopython/primer-101/4-operators-and-functions/#what-on-earth-are-they-and-why-should-i-care)   
   4.2	[Careful…](/guides/rhinopython/primer-101/4-operators-and-functions/#careful)     
   4.3	[Logical Operators](/guides/rhinopython/primer-101/4-operators-and-functions/#logical-operators)     
   4.4	[Functions and Procedures](/guides/rhinopython/primer-101/4-operators-and-functions/#functions-and-procedures)     
&nbsp;&nbsp; 4.4.1 [A Simple Function Example](/guides/rhinopython/primer-101/4-operators-and-functions/#a-simple-function-example)     
&nbsp;&nbsp; 4.4.2 [Advanced Function Syntax](/guides/rhinopython/primer-101/4-operators-and-functions/#advanced-function-syntax)     
   4.5	[Mutability](/guides/rhinopython/primer-101/4-operators-and-functions/#mutability)      

### 5. [Conditional Execution](/guides/rhinopython/primer-101/5-conditional-execution/)

   5.1	[What if?](/guides/rhinopython/primer-101/5-conditional-execution/#what-if)  
   5.2	[Looping](/guides/rhinopython/primer-101/5-conditional-execution/#looping)  
   5.3	[Conditional Loops](/guides/rhinopython/primer-101/5-conditional-execution/#conditional-loops)  
   5.4	[Incremental Loops](/guides/rhinopython/primer-101/5-conditional-execution/#incremental-loops)  


### 6. [Tuples, Lists, and Dictionaries](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/)

   6.1	[Tuples](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/#tuples)  
   6.2	[Lists](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/#lists)  
&nbsp;&nbsp; 6.2.1	[List Comprehensions](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/#list-comprehension)  
   6.3	[Dictionaries](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/#dictionaries)  
   6.4	[Points and Vectors](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/#points-and-vectors)  
   6.5	[An AddVector() Example](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/#an-addvector-example)  
   6.6	[Nested Lists](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/#nested-lists)  

{{< /column >}}  
{{< column >}}  


### 7. [Classes](/guides/rhinopython/primer-101/7-classes/)

7.1	[Class Syntax](/guides/rhinopython/primer-101/7-classes/#class-syntax)


### 8. [Geometry](/guides/rhinopython/primer-101/8-geometry/)

   8.1	[The openNURBS™ Kernel](/guides/rhinopython/primer-101/8-geometry/#the-opennurbs-kernel)  
   8.2	[Objects in Rhino](/guides/rhinopython/primer-101/8-geometry/#obects-in-rhino)  
   8.3	[Points and Pointclouds](/guides/rhinopython/primer-101/8-geometry/#points-andpointclouds)  
   8.4	[Lines and Polylines](/guides/rhinopython/primer-101/8-geometry/#lines-and-polylines)  
   8.5	[Planes](/guides/rhinopython/primer-101/8-geometry/#planes)  
   8.6	[Circles, Ellipses, and Arcs](/guides/rhinopython/primer-101/8-geometry/#circles-ellipses-and-arcs)  
&nbsp;&nbsp; 8.6.1 [Ellipses](/guides/rhinopython/primer-101/8-geometry/#ellipses)  
&nbsp;&nbsp; 8.6.2 [Arcs](/guides/rhinopython/primer-101/8-geometry/#arcs)  
   8.7	[NURBS Curves](/guides/rhinopython/primer-101/8-geometry/#nurbs-curves)  
&nbsp;&nbsp; 8.7.1 [Control-Point Curves](/guides/rhinopython/primer-101/8-geometry/#control-point-curves)  
&nbsp;&nbsp; 8.7.2 [Interpolated Curves](/guides/rhinopython/primer-101/8-geometry/#interpolate-curves)  
&nbsp;&nbsp; 8.7.3 [Geometric Curve Properties](/guides/rhinopython/primer-101/8-geometry/#geometric-curve-properties)    
   8.8	[Meshes](/guides/rhinopython/primer-101/8-geometry/#meshes)  
&nbsp;&nbsp; 8.8.1 [Geometry vs. Topology](/guides/rhinopython/primer-101/8-geometry/#geometry-vs-topology)  
&nbsp;&nbsp; 8.8.1 [Shape vs. Image](/guides/rhinopython/primer-101/8-geometry/#shape-vs-image)  
   8.9	[Surfaces](/guides/rhinopython/primer-101/8-geometry/#surfaces)  
&nbsp;&nbsp; 8.9.1 [NURBS Surfaces](/guides/rhinopython/primer-101/8-geometry/#nurbs-surfaces)  
&nbsp;&nbsp; 8.9.2 [Surface Curvature](/guides/rhinopython/primer-101/8-geometry/#surface-curvature)  
&nbsp;&nbsp; 8.9.3 [Vector And Tensor Spaces](/guides/rhinopython/primer-101/8-geometry/#vector-and-tensor-spaces)   

{{< /column >}}
{{< /row >}}

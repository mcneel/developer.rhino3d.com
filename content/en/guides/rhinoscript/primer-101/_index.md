+++
authors = [ "david" ]
categories = [ "Unsorted" ]
description = "A full course on RhinoScript"
keywords = [ "rhino", "developer" ]
languages = "unset"
sdk = "unset"
title = "RhinoScript 101"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

<div class="row">
<div class="col-md-12" markdown="1">  
  
</div>
<div class="col-md-8 col-sm-12 col-sm-12" markdown="1">  

{{< image url="/images/primer-normals.svg" alt="/images/primer-normals.svg" width="30%" class="float_right" >}}

You’ve just opened the third edition of the RhinoScript primer. This booklet was originally written as a workshop handout for the students at the Architecture faculty of the Universität für Angewandte Kunst in Vienna. The aim of the workshop was to teach them how to program Rhino in no more than four days and, counter all my expectations, they did. Most of them had never programmed before so I had to make sure the text was suitable for absolute beginners. I did not expect at the time that this proved to be the most successful aspect of the primer. After the workshop, a slightly reworked version was made available to the public and it has helped many non-programmers getting rid of the "non" since. Incidentally, if you do not succeed in learning RhinoScript within a time-span of four days, do not feel bad about yourself. Remember that those students received additional lectures and intensive support from someone who took two months to reach the same level.


This new edition essentially caters for two major demands; the release of Rhinoceros 4.0 and the superficiality of the old edition. RhinoScript has existed for many years, but has recently taken a big leap forward with the development of Rhino4. Scripters of course want to take advantage of all the new functionality offered by this release and new programmers don’t want to start learning an outdated language. I have tried to combine the original aims of the primer with the requests for more in-depth articles, but it is always hard to judge the clarity of a text when one is highly familiar with its subject matter to begin with. You will have to be the judge. But always remember that learning programming -though fun- is no laughing matter so to speak. The ancient Greeks already understood that hubris is a party spoiler and the best way to prevent this learning experience turning into a classic tragedy, is to take it slow. Do not continue reading if you’re uncomfortable with past paragraphs. Re-read when in doubt. Ask questions if necessary. Programming is not difficult, but it requires a certain frame of mind which some beginners find hard to acquire. I know I did.


{{< div class="clear_both" />}}

{{< image url="/images/primer-branchpropagation2.svg" alt="/images/primer-branchpropagation2.svg" width="30%" class="float_right" >}}

The one advantage I enjoy over authors of other programming books, is that I shall be teaching you to program Rhino. Writing scripts for Rhino means you have an exceptionally powerful geometry kernel at your disposal which enables you to achieve the most outrageous results with a minimum of code. Instead of boring you with days-of-the-week and employee-salary-classes examples, I get to bore you with freeform surfaces, evolving curves and inflating meshes.

Hopefully, this third edition of the RhinoScript primer will help existing scripters get the most out of Rhino4, while teaching regular human beings how to become scripters in the first place.

Good luck!  


{{< image url="/images/primer-autograph.svg" alt="/images/primer-autograph.svg" width="40%" >}}  

</div>  

  
</div>  

<div class="row">  
<div class="col-md-12" markdown="1">  

David Rutten
Robert McNeel & Associates

[{{< awesome "fas fa-download">}} ](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101) [Download the RhinoScript 101 Primer as a single PDF ](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101)

### Table of Contents  
</div>  
</div>  

{{< row >}}  
{{< column >}}  

### 1. [What's it all about?](/guides/rhinoscript/primer-101/1-whats-it-all-about/)

   1.1 [Macros](/guides/rhinoscript/primer-101/1-whats-it-all-about/#11-macros)  
   1.2 [Scripts](/guides/rhinoscript/primer-101/1-whats-it-all-about/#12-scripts)  
   1.3 [Running Scripts](/guides/rhinoscript/primer-101/1-whats-it-all-about/#13-scripts)  

### 2. [VBscript Essentials](/guides/rhinoscript/primer-101/2-vbscript-essentials/)  

   2.1	[Language origin](/guides/rhinoscript/primer-101/2-vbscript-essentials/#21-language-origin)  
   2.2	[Flow control](/guides/rhinoscript/primer-101/2-vbscript-essentials/#f22-low-control)  
   2.3	[Variable data](/guides/rhinoscript/primer-101/2-vbscript-essentials/#23-variable-data)  
&nbsp;&nbsp; 2.3.1	[Integers and Doubles](/guides/rhinoscript/primer-101/2-vbscript-essentials/#231-integers-and-doubles)  
&nbsp;&nbsp; 2.3.2	[Booleans](/guides/rhinoscript/primer-101/2-vbscript-essentials/#232-booleans)  
&nbsp;&nbsp; 2.3.3	[Strings](/guides/rhinoscript/primer-101/2-vbscript-essentials/#233-strings)  
&nbsp;&nbsp; 2.3.4	[None variable](/guides/rhinoscript/primer-101/2-vbscript-essentials/#234-none-variable)  
&nbsp;&nbsp; 2.3.5	[Using variables](/guides/rhinoscript/primer-101/2-vbscript-essentials/#235-using-variables)  

### 3. [Script anatomy](/guides/rhinoscript/primer-101/3-script-anatomy/)

   3.1 [Programming in Rhino](/guides/rhinoscript/primer-101/3-script-anatomy/#31-programming-in-rhino)    
   3.2 [The bones](/guides/rhinoscript/primer-101/3-script-anatomy/#32-the-bones)  
   3.3 [The guts](/guides/rhinoscript/primer-101/3-script-anatomy/#33-the-guts)  
   3.4 [The skin](/guides/rhinoscript/primer-101/3-script-anatomy/#34-the-skin)  

{{< /column >}}
{{< column >}}


### 4. [Operators and functions](/guides/rhinoscript/primer-101/4-operators-and-functions/)

   4.1	[What on earth are they and why should I care?](/guides/rhinoscript/primer-101/4-operators-and-functions/#41-what-on-earth-are-they-and-why-should-i-care)   
   4.2	[Careful…](/guides/rhinoscript/primer-101/4-operators-and-functions/#42-careful)     
   4.3	[Logical operators](/guides/rhinoscript/primer-101/4-operators-and-functions/#43-logical-operators)     
   4.4	[Functions and Procedures](/guides/rhinoscript/primer-101/4-operators-and-functions/#44-functions-and-procedures)     
&nbsp;&nbsp; 4.4.1 [A simple function example](/guides/rhinoscript/primer-101/4-operators-and-functions/#441-a-simple-function-example)     
&nbsp;&nbsp; 4.4.2 [Advanced function syntax](/guides/rhinoscript/primer-101/4-operators-and-functions/#442-advanced-function-syntax)     


### 5. [Conditional execution](/guides/rhinoscript/primer-101/5-conditional-execution/)

   5.1	[What if?](/guides/rhinoscript/primer-101/5-conditional-execution/#51-what-if)  
   5.2	[Select Case](/guides/rhinoscript/primer-101/5-conditional-execution/#52-select-case)  
   5.3	[Looping](/guides/rhinoscript/primer-101/5-conditional-execution/#53-looping)  
   5.4	[Conditional loops](/guides/rhinoscript/primer-101/5-conditional-execution/#54-conditional-loops)  
   5.5	[Alternate syntax](/guides/rhinoscript/primer-101/5-conditional-execution/#55-alternate-syntax)   
   5.6	[Incremental loops](/guides/rhinoscript/primer-101/5-conditional-execution/#56-incremental-loops)


### 6. [Arrays](/guides/rhinoscript/primer-101/6-arrays/)

   6.1	[My favorite things](/guides/rhinoscript/primer-101/6-arrays/#61-my-favorite-things)  
   6.2	[Points and Vectors](/guides/rhinoscript/primer-101/6-arrays/#62-points-and-vectors)  
   6.3	[An AddVector() example](/guides/rhinoscript/primer-101/6-arrays/#63-an-addvector-example)  
   6.4	[Nested Lists](/guides/rhinoscript/primer-101/6-arrays/#64-nested-lists)  

{{< /column >}}
{{< column >}}


### 7. [Geometry](/guides/rhinoscript/primer-101/7-geometry/)

   7.1	[The openNURBS™ kernel](/guides/rhinoscript/primer-101/7-geometry/#71-the-opennurbs-kernel)  
   7.2	[Objects in Rhino](/guides/rhinoscript/primer-101/7-geometry/#72-objects-in-rhino)  
   7.3	[Points and Pointclouds](/guides/rhinoscript/primer-101/7-geometry/#73-points-and-pointclouds)  
   7.4	[Lines and Polylines](/guides/rhinoscript/primer-101/7-geometry/#74-lines-and-polylines)  
   7.5	[Planes](/guides/rhinoscript/primer-101/7-geometry/#75-planes)  
   7.6	[Circles, Ellipses and Arcs](/guides/rhinoscript/primer-101/7-geometry/#76-circles-ellipses-and-arcs)  
&nbsp;&nbsp; 7.6.1 [Ellipses](/guides/rhinoscript/primer-101/7-geometry/#761-ellipses)  
&nbsp;&nbsp; 7.6.2 [Arcs](/guides/rhinoscript/primer-101/7-geometry/#762-arcs)  
   7.7	[Nurbs Curves](/guides/rhinoscript/primer-101/7-geometry/#77-nurbs-curves)  
&nbsp;&nbsp; 7.7.1 [Control-point curves](/guides/rhinoscript/primer-101/7-geometry/#771-control-point-curves)  
&nbsp;&nbsp; 7.7.2 [Interpolated curves](/guides/rhinoscript/primer-101/7-geometry/#772-interpolate-curves)  
&nbsp;&nbsp; 7.7.3 [Geometric curve properties](/guides/rhinoscript/primer-101/7-geometry/#773-geometric-curve-properties)    
   7.8	[Meshes](/guides/rhinoscript/primer-101/7-geometry/#78-meshes)  
&nbsp;&nbsp; 7.8.1 [Geometry vs. Topology](/guides/rhinoscript/primer-101/7-geometry/#781-geometry-vs-topology)  
&nbsp;&nbsp; 7.8.1 [Shape vs. Image](/guides/rhinoscript/primer-101/7-geometry/#781-shape-vs-image)  
   7.9	[Surfaces](/guides/rhinoscript/primer-101/7-geometry/#79-surfaces)  
&nbsp;&nbsp; 7.9.1 [Nurbs surfaces](/guides/rhinoscript/primer-101/7-geometry/#791-nurbs-surfaces)  
&nbsp;&nbsp; 7.9.2 [Surface Curvature](/guides/rhinoscript/primer-101/7-geometry/#792-surface-curvature)  
&nbsp;&nbsp; 7.9.3 [Vector And Tensor Spaces](/guides/rhinoscript/primer-101/7-geometry/#793-vector-and-tensor-spaces)   

{{< /column >}}
{{< /row >}}

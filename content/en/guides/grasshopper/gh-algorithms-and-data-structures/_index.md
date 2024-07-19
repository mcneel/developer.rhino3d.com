+++
aliases = [""]
authors = [ "rajaa" ]
categories = [ "" ]
description = "Introduces the fundementals of algorithmic design and data structures using Grasshopper."
keywords = [ "grasshopper", "developer" ]
languages = [ "" ]
sdk = [ "" ]
title = "Essential Algorithms and Data Structures for Grasshopper"
type = "guides"
weight = 1
override_last_modified = ""

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

<div class="row">
<div class="col-12" markdown="1">   

</div>
{{< column >}}  

<br>

{{< image url="ads-000-cover-s.png" alt="" class="float_right" >}}

The Essential Algorithms and Data Structures guide introduces to design professionals effective methodologies to develop complex 3D modeling algorithms using [Grasshopper® (GH)](https://www.grasshopper3d.com), the generative modeling environment for [Rhinoceros® (Rhino)](https://www.rhino3d.com). It also covers extensively the data structure adopted by Grasshopper and its core organization and management tools.

The material is directed towards designers who are interested in parametric design and have little or no background in programming. All concepts are explained visually using Grasshopper. This guide is not intended as a beginners guide to Grasshopper in terms of user interface or tools. Basic knowledge of the interface and workflow is assumed. For more resources and getting started guides, go to the learn section in www.rhino3d.com.

The content is divided into three chapters. [Chapter 1](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/) discusses algorithms and data. It introduces a rigorous methodology to help create and manage parametric solutions. It also introduces basic data concepts such as data types, sources and common ways to process them. [Chapter 2](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures) reviews basic data structures in Grasshopper. That includes single items and lists. [Chapter 3](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures) includes an in-depth review of the tree data structure in Grasshopper and practical applications in design problems. All Grasshopper examples and tutorials are written with Rhinoceros version 6 and are included in the download.

{{< /column >}}  
</div>  

<div class="row">  
<div class="col-md-12" markdown="1">  

***[Rajaa Issa](https://discourse.mcneel.com/u/rajaa/activity)***  
*Robert McNeel & Associates*

<br>

#### Download:
* [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6.0/essential-algorithms) [Essential Algorithms and Data Structures](https://www.rhino3d.com/download/rhino/6.0/essential-algorithms) containing the guide text (PDF) and all the example Grasshopper files in this guide.

<br>

### Table of Contents  

</div>  
</div>  

{{< row >}}  
{{< column >}}  

### 1. [Algorithms and Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/)

   1.1 [Algorithmic design](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#11-algorithmic-design)  
   1.2 [Algorithms parts](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#12-algorithms-parts)  
   1.3 [Designing algorithms: the 4-step process](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#13-designing-algorithms-the-4-step-process)  
   1.4 [Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#14-data)  
   1.5 [Data sources](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#15-data-sources)  
   1.6 [Data types](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#16-data-types)  
   1.7 [Processing Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#17-processing-data)  
&nbsp;&nbsp; Numeric operations  
&nbsp;&nbsp; Logical operations  
&nbsp;&nbsp; Data analysis  
&nbsp;&nbsp; Sorting  
&nbsp;&nbsp; Selection  
&nbsp;&nbsp; Mapping  
   1.8 [Pitfalls of algorithmic design](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#18-pitfalls-of-algorithmic-design)  
&nbsp;&nbsp; Invalid or wrong input type  
&nbsp;&nbsp; Unintended input  
&nbsp;&nbsp; Incorrect order of operation  
&nbsp;&nbsp; Mismatched data structures  
&nbsp;&nbsp; Long processing time  
&nbsp;&nbsp; Poor organization  
   1.9 [Tutorials: algorithms and data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#19-tutorials-algorithms-and-data)  
&nbsp;&nbsp; Unioned circles tutorial  
&nbsp;&nbsp; Sphere with bounds tutorial  
&nbsp;&nbsp; Data operations tutorial  
&nbsp;&nbsp; Pitfalls tutorial  

{{< /column >}}
{{< column >}}

### 2. [Introduction to Data Structures](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/)

   2.1 [Overview](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#21-overview)  
   2.2 [Generating lists](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#22-generating-lists)  
   2.3 [List operations](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#23-list-operations)  
   2.4 [List matching](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#24-list-matching)  
   2.5 [Tutorials: data structures](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#25-tutorials-data-structures)  
&nbsp;&nbsp; Variable thickness pipe tutorial  
&nbsp;&nbsp; Custom list matching tutorial  
&nbsp;&nbsp; Simple truss tutorial  
&nbsp;&nbsp; Pearl necklace tutorial  

{{< /column >}}
{{< column >}}

### 3. [Advanced Data Structures](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/)

   3.1 [The Grasshopper data structure](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#31-the-grasshopper-data-structure)  
&nbsp;&nbsp; Introduction  
&nbsp;&nbsp; Processing data trees  
&nbsp;&nbsp; Data tree notation  
   3.2 [Generating trees](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#32-generating-trees)  
   3.3 [Tree matching](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#33-tree-matching)  
   3.4 [Traversing trees](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#34-traversing-trees)  
   3.5 [Basic tree operations](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#35-basic-tree-operations)  
&nbsp;&nbsp; Viewing the tree structure  
&nbsp;&nbsp; List operations on trees  
&nbsp;&nbsp; Grafting from lists to a trees  
&nbsp;&nbsp; Flattening from trees to lists  
&nbsp;&nbsp; Combining data streams  
&nbsp;&nbsp; Flipping the data structure  
&nbsp;&nbsp; Simplifying the data structure  
   3.6 [Advanced tree operations](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#36-advanced-tree-operations)  
&nbsp;&nbsp; Relative items  
&nbsp;&nbsp; Split trees  
&nbsp;&nbsp; Path mapper  
   3.7 [Tutorials: advanced data structures](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#37-tutorials-advanced-data-structures)  
&nbsp;&nbsp; Sloped roof tutorial  
&nbsp;&nbsp; Diagonal triangles tutorial  
&nbsp;&nbsp; Zigzag tutorial  
&nbsp;&nbsp; Weaving tutorial  

{{< /column >}}
{{< /row >}}

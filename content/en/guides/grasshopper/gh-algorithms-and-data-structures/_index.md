+++
aliases = ["/en"]
authors = [ "rajaa" ]
categories = [ "" ]
description = "Introduces the fundementals of algorithmic design and data structures using Grasshopper."
keywords = [ "grasshopper", "developer", "algorithms", "data", "data structures" ]
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
{{<awesome "fas fa-solid fa-video">}} <a href="https://vimeo.com/showcase/11456959/video/1030213652" target="_blank"> Introduction video</a>
{{< image url="ads-cover2nd.png" alt="Essential Algorithms and Data Structures" class="float_right" >}}

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

#### The Guide Material:
* [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6.0/essential-algorithms) [Download the guide PDF and all Grasshopper examples](https://www.rhino3d.com/download/rhino/6.0/essential-algorithms)
* [{{< awesome "fas fa-solid fa-video">}}](https://vimeo.com/showcase/11456959) [Link to the guide video recordings](https://vimeo.com/showcase/11456959)

<br>

### Table of Contents  

</div>  
</div>  

{{< row >}}  
{{< column >}}  

### 1. [Algorithms and Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/)

   &nbsp;&nbsp;1.1 [Algorithmic design](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#11-algorithmic-design)  
   &nbsp;&nbsp;1.2 [Algorithms parts](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#12-algorithms-parts)  
   &nbsp;&nbsp;1.3 [Designing algorithms: the 4-step process](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#13-designing-algorithms-the-4-step-process)  
   &nbsp;&nbsp;1.4 [Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#14-data)  
   &nbsp;&nbsp;1.5 [Data sources](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#15-data-sources)  
   &nbsp;&nbsp;1.6 [Data types](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#16-data-types)  
   &nbsp;&nbsp;1.7 [Processing Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#17-processing-data)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.7.1 [Numeric operations](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#171-numeric-operations)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.7.2 [Logical operations](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#172-logical-operations)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.7.3 [Data analysis](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#173-data-analysis)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.7.4 [Sorting](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#174-sorting)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.7.5 [Selection](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#175-selection)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.7.6 [Mapping](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#176-mapping)  
   &nbsp;&nbsp;1.8 [Pitfalls of algorithmic design](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#18-pitfalls-of-algorithmic-design)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.8.1 [Invalid or wrong input type](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#181-invalid-or-wrong-input-type)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.8.2 [Unintended input](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#182-unintended-input)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.8.3 [Incorrect order of operation](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#183-incorrect-order-of-operation)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.8.4 [Mismatched data structures](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#184-mismatched-data-structures)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.8.5 [Long processing time](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#185-long-processing-time)  
   &nbsp;&nbsp;&nbsp;&nbsp;1.8.6 [Poor organization](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#186-poor-organization)  
   &nbsp;&nbsp;1.9 [Tutorials: algorithms and data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#19-tutorials-algorithms-and-data)   


{{< /column >}}
{{< column >}}

### 2. [Introduction to Data Structures](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/)

   &nbsp;&nbsp;2.1 [Overview](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#21-overview)  
   &nbsp;&nbsp;2.2 [Generating lists](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#22-generating-lists)  
   &nbsp;&nbsp;2.3 [List operations](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#23-list-operations)  
   &nbsp;&nbsp;2.4 [List matching](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#24-list-matching)  
   &nbsp;&nbsp;2.5 [Tutorials: data structures](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#25-tutorials-data-structures)  

### 3. [Advanced Data Structures](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/)

   &nbsp;&nbsp;3.1 [The Grasshopper data structure](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#31-the-grasshopper-data-structure)  
   &nbsp;&nbsp;&nbsp;&nbsp;3.1.1 [Introduction](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#311-introduction)  
   &nbsp;&nbsp;&nbsp;&nbsp;3.1.2 [Processing data trees](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#312-processing-data-trees)  
   &nbsp;&nbsp;&nbsp;&nbsp;3.1.3 [Data tree notation](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#313-data-tree-notation)  
   &nbsp;&nbsp;3.2 [Generating trees](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#32-generating-trees)  
   &nbsp;&nbsp;3.3 [Tree matching](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#33-tree-matching)  
   &nbsp;&nbsp;3.4 [Traversing trees](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#34-traversing-trees)  
   &nbsp;&nbsp;3.5 [Basic tree operations](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#35-basic-tree-operations)  
   &nbsp;&nbsp;&nbsp;&nbsp; 3.5.1 [Viewing the tree structure](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#351-viewing-the-tree-structure)  
   &nbsp;&nbsp;&nbsp;&nbsp; 3.5.2 [List operations on trees](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#352-list-operations-on-trees)  
   &nbsp;&nbsp;&nbsp;&nbsp; 3.5.3 [Grafting from lists to a trees](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#353-grafting-from-lists-to-a-trees)  
   &nbsp;&nbsp;&nbsp;&nbsp; 3.5.4 [Flattening from trees to lists](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#354-flattening-from-trees-to-lists)  
   &nbsp;&nbsp;&nbsp;&nbsp; 3.5.5 [Combining data streams](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#355-combining-data-streams)  
   &nbsp;&nbsp;&nbsp;&nbsp; 3.5.6 [Flipping the data structure](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#356-flipping-the-data-structure)  
   &nbsp;&nbsp;&nbsp;&nbsp; 3.5.7 [Simplifying the data structure](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#357-simplifying-the-data-structure)  
   &nbsp;&nbsp;3.6 [Advanced tree operations](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#36-advanced-tree-operations)  
   &nbsp;&nbsp;&nbsp;&nbsp; 3.6.1 [Relative items](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#361-relative-items)  
   &nbsp;&nbsp;&nbsp;&nbsp; 3.6.2 [Split trees](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#362-split-trees)  
   &nbsp;&nbsp;&nbsp;&nbsp; 3.6.3 [Path mapper](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#363-path-mapper)  
   &nbsp;&nbsp;3.7 [Tutorials: advanced data structures](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#37-tutorials-advanced-data-structures)  

{{< /column >}}
{{< /row >}}

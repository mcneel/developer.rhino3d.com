+++
aliases = [""]
authors = [ "rajaa" ]
categories = [ "Basic" ]
description = "A full course on RhinoComon in Grasshopper using C#"
keywords = [ "rhino", "developer", "grasshopper", ".NET", "RhinoCommon", "Plugin"  ]
languages = [ "C#"]
sdk = [ "RhinoCommon", "RhinoPython", "Grasshopper" ]
title = "Essential C# Scripting for Grasshopper"
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

This is an essential scripting guide

<div class="row">
<div class="col-12" markdown="1">   


</div>
{{< column >}}  

{{< image url="/images/math-logo.svg" alt="/images/math-logo.svg" class="float_right" >}}

This manual is intended for designers who are experienced in [Grasshopper® (GH)](www.grasshopper3d.com) visual scripting, and would like to take their skills to the next level to create their own custom scripts using C# programming language. This guide does not assume nor require any background in programming. The document is divided into four parts. [Chapter 1](/guides/general/essential-mathematics/vector-mathematics/) explains the general interface of the C# scripting component in Grasshopper. [Chapter 2](/guides/general/essential-mathematics/matrices-transformations/) reviews the basics of the C# DotNet programming language. [Chapter 3](/guides/general/essential-mathematics/parametric-curves-surfaces/) covers the main geometry types and functions in the RhinoCommon SDK. [Chapter 4](/guides/general/essential-mathematics/parametric-curves-surfaces/) includes examples of a number of design algorithms. The guide includes many examples that are also available as a Grasshopper file available with the download of this guide. Note that all examples are written in version 8 of [Rhinoceros® (Rhino)](www.rhino3d.com) and Grasshopper.

I would like to acknowledge the excellent technical review by Mr. Steve Baer of Robert McNeel and Associates. I would also like to acknowledge Ms. Sandy McNeel for reviewing the writing and formatting of this document.

{{< /column >}}  
</div>  

<div class="row">  
<div class="col-md-12" markdown="1">  

***[Rajaa Issa](https://discourse.mcneel.com/users/rajaa/activity)***

Robert McNeel & Associates

### Table of Contents  

</div>  
</div>  

{{< row >}}  
{{< column >}}  

### 1. [C# Component in Grasshopper](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)
   1.1 [Introduction](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   1.2 [C# component interface](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   1.3 [The input parameters](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   1.4 [The output parameters](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   1.5 [The out string](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   1.6 [Main menu](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   1.7 [Code editor](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 1.7.1 [Imports](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 1.7.2 [Utility members and functions](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 1.7.3 [The RunScript](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   1.8 [Data access](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 1.8.1 [Item access](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 1.8.2 [Lists access](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 1.8.3 [Tree access](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  

{{< /column >}}
{{< column >}} 

### 2. [C# Programming Basics](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)
   2.1 [Introduction](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   2.2 [Comments](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   2.3 [Variables](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   2.4 [Operators](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   2.5 [Namespaces](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   2.6 [Data](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.6.1 [Primitive data types](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.6.2 [Collections](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   2.7 [Flow control](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.7.1 [Conditional statements](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.7.2 [Loops](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   2.8 [Methods](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.8.1 [Overview](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.8.2 [Method parameters](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   2.9 [User-defined data types](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.9.1 [Enumerations](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.9.2 [Structures](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.9.3 [Classes](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.9.4 [Value vs reference types](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 2.9.5 [Interface](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   2.10 [Read and write text files](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   2.11 [Recursive functions](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  

{{< /column >}}
{{< column >}} 


### 3. [RhinoCommon Geometry](/guides/general/essential-mathematics/parametric-curves-surfaces/)

   3.1 [Overview](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
   3.2 [Geometry structures](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
&nbsp;&nbsp; 3.2.1 [The Point3d structure](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 3.2.2 [Points and vectors](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 3.2.3 [Lightweight curves](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 3.2.4 [Lightweight surfaces](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 3.2.5 [Lightweight surfaces](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   3.3 [Geometry classes](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
&nbsp;&nbsp; 3.3.1 [Curves](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 3.3.2 [Surfaces](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 3.3.3 [Meshes](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 3.3.4 [Boundary representation (Brep)](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 3.3.5 [Other geometry classes](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   3.4 [Geometry transformations](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  

### 4. [RhinoCommon Geometry](/guides/general/essential-mathematics/parametric-curves-surfaces/)

   4.1 [Introduction](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
   4.2 [Geometry algorithms](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
&nbsp;&nbsp; 4.2.1 [Sine curves and surface](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 4.2.2 [De Casteljau algorithm to interpolate a Bezier curve](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 4.2.3 [Simple subdivision mesh](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
   4.3 [Generative algorithms](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
&nbsp;&nbsp; 4.3.1 [Dragon curve](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 4.3.2 [Fractal tree](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 4.3.3 [Penrose tiling](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  
&nbsp;&nbsp; 4.3.4 [Conway Game of Life](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)  

{{< /column >}}
{{< /row >}}

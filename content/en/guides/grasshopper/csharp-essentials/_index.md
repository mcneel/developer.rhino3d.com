+++
aliases = [""]
authors = [ "rajaa" ]
categories = [ "Unsorted" ]
description = "A full course on RhinoComon in Grasshopper using C#"
keywords = [ "rhino", "developer", "grasshopper" ]
languages = "unset"
sdk = "unset"
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

*Essential Mathematics for Computational Design* introduces to design professionals the foundation mathematical concepts that are necessary for effective development of computational methods for 3D modeling and computer graphics. This is not meant to be a complete and comprehensive resource, but rather an overview of the basic and most commonly used concepts. The material is directed towards designers who have little or no background in mathematics beyond high school. All concepts are explained visually using [Grasshopper® (GH)](www.grasshopper3d.com), the generative modeling environment for [Rhinoceros® (Rhino)](www.rhino3d.com).  

The content is divided into three chapters. [Chapter 1](/guides/general/essential-mathematics/vector-mathematics/) discusses vector math including vector representation, vector operation, and line and plane equations. [Chapter 2](/guides/general/essential-mathematics/matrices-transformations/) reviews matrix operations and transformations. [Chapter 3](/guides/general/essential-mathematics/parametric-curves-surfaces/) includes an in-depth review of parametric curves with special focus on NURBS curves and the concepts of continuity and curvature.  It also reviews NURBS surfaces and polysurfaces.

*I would like to acknowledge the excellent and thorough technical review by [Dr. Dale Lear](https://discourse.mcneel.com/u/dalelear/activity) of Robert McNeel & Associates. His valuable comments were instrumental in producing this edition. I would also like to acknowledge Ms. [Margaret Becker](https://discourse.mcneel.com/u/margaret/activity) of Robert McNeel & Associates for reviewing the technical writing and formatting*.

{{< /column >}}  
</div>  

<div class="row">  
<div class="col-md-12" markdown="1">  

***[Rajaa Issa](https://discourse.mcneel.com/users/rajaa/activity)***

Robert McNeel & Associates

Download the [{{< awesome "fas fa-download">}} ](/files/math-samplesandtutorials.zip.zip) [math-samplesandtutorials.zip](/files/math-samplesandtutorials.zip) archive, containing all the example Grasshopper and code files in this guide.

[{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6/essentialmathematics) [Download Essential Mathematics for Computational Design as a single PDF ](https://www.rhino3d.com/download/rhino/6/essentialmathematics/)

<a href="https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK"><span class="glyphicon glyphicon-play"></span></a> [Watch the Essential Mathematics Videos... ](https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK)

The current 4th Edition is available in four languages:

* [Essential Mathematics 4th Edition in German (Deutsch)](https://files.mcneel.com/rhino/6/docs/de/TheEssentialMathematics_4thEdition_de.zip)
* [Essential Mathematics 4th Edition in French (Français)](https://files.mcneel.com/rhino/6/docs/fr/TheEssentialMathematics_4thEdition_fr.zip)
* [Essential Mathematics 4th Edition in Spanish (Español)](https://files.mcneel.com/rhino/6/docs/es/TheEssentialMathematics_4thEdition2019_es.zip)
* [Essential Mathematics 4th Edition in Italian (Italiano)](https://files.mcneel.com/rhino/6/docs/it/TheEssentialMathematics_4thEdition_it.zip)

The 2nd edition is available in four languages:

* [Essential Mathematics 2nd Edition in Korean](http://download.rhino3d.com/Rhino/4.0/EssentialMathematics_Korean/)
* [Essential Mathematics 2nd Edition in Japanese（日本語)](http://download.rhino3d.com/ja/Rhino/4.0/EssentialMathematicsSecondEdition)
* [Essential Mathematic 2nd Edition in Traditional Chinese (繁體中文版)](http://download.mcneel.com/download.asp?id=EssentialMathematics_ChineseTraditional)
* [Essential Mathematic 2nd Edition in Simplified Chinese(簡體中文版)](http://download.rhino3d.com/Rhino/4.0/EssentialMathematics_ChineseSimplified/)

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

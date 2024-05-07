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

This manual is intended for designers who are experienced in [Grasshopper® (GH)](www.grasshopper3d.com) visual scripting, and would like to take their skills to the next level to create their own custom scripts using C# programming language. This guide does not assume nor require any background in programming. The document is divided into four parts. 

1. [C# Component in Grasshopper](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/) explains the general interface of the C# scripting component in Grasshopper. 
1. [C# Programming Basics](/guides/grasshopper/csharp-essentials/2-csharp-basics/) reviews the basics of the C# DotNet programming language. 
1. [RhinoCommon Geometry](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/) covers the main geometry types and functions in the RhinoCommon SDK. 
1. [Design Algorithms](/guides/grasshopper/csharp-essentials/4-design-algorithms/) includes examples of a number of design algorithms. 

The guide includes many examples that are also available as a Grasshopper file available with the download of this guide. Note that all examples are written in version 8 of [Rhinoceros® (Rhino)](www.rhino3d.com) and Grasshopper.

I would like to acknowledge the excellent technical review by Mr. Steve Baer of Robert McNeel and Associates. I would also like to acknowledge Ms. Sandy McNeel for reviewing the writing and formatting of this document.

{{< /column >}}  
</div>  

<div class="row">  
<div class="col-md-12" markdown="1">  

***[Rajaa Issa](https://discourse.mcneel.com/u/rajaa/activity)***

Robert McNeel & Associates

### Table of Contents  

</div>  
</div>  

{{< row >}}  
{{< column >}}  

### 1. [C# Component in Grasshopper](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/)
   1.1 [Introduction](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#11-introduction)  
   1.2 [C# component interface](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#12-c-component-interface)  
   1.3 [The input parameters](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#13-the-input-parameters)  
   1.4 [The output parameters](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#14-the-output-parameters)  
   1.5 [The out string](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#15-the-out-string)  
   1.6 [Main menu](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#16-main-menu)  
   1.7 [Code editor](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#17-code-editor)  
&nbsp;&nbsp; 1.7.1 [Imports](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#171-imports)  
&nbsp;&nbsp; 1.7.2 [Utility members and functions](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#172-utility-members--functions)  
&nbsp;&nbsp; 1.7.3 [The RunScript](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#173-the-runscript)  
   1.8 [Data access](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#18-data-access)  
&nbsp;&nbsp; 1.8.1 [Item access](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#181-item-access)  
&nbsp;&nbsp; 1.8.2 [Lists access](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#182-list-access)  
&nbsp;&nbsp; 1.8.3 [Tree access](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#183-tree-access)  

{{< /column >}}
{{< column >}} 

### 2. [C# Programming Basics](/guides/grasshopper/csharp-essentials/2-csharp-basics/)
   2.1 [Introduction](/guides/grasshopper/csharp-essentials/2-csharp-basics/#21-introduction)  
   2.2 [Comments](/guides/grasshopper/csharp-essentials/2-csharp-basics/#22-comments)  
   2.3 [Variables](/guides/grasshopper/csharp-essentials/2-csharp-basics/#23-variables)  
   2.4 [Operators](/guides/grasshopper/csharp-essentials/2-csharp-basics/#24-operators)  
   2.5 [Namespaces](/guides/grasshopper/csharp-essentials/2-csharp-basics/#25-namespaces)  
   2.6 [Data](/guides/grasshopper/csharp-essentials/2-csharp-basics/#26-data)  
&nbsp;&nbsp; 2.6.1 [Primitive data types](/guides/grasshopper/csharp-essentials/2-csharp-basics/#261-primitive-data-types)  
&nbsp;&nbsp; 2.6.2 [Collections](/guides/grasshopper/csharp-essentials/2-csharp-basics/#262-collections)  
   2.7 [Flow control](/guides/grasshopper/csharp-essentials/2-csharp-basics/#27-flow-control)  
&nbsp;&nbsp; 2.7.1 [Conditional statements](/guides/grasshopper/csharp-essentials/2-csharp-basics/#271-conditional-statements)  
&nbsp;&nbsp; 2.7.2 [Loops](/guides/grasshopper/csharp-essentials/2-csharp-basics/#272-loops)  
   2.8 [Methods](/guides/grasshopper/csharp-essentials/2-csharp-basics/#28-methods)  
&nbsp;&nbsp; 2.8.1 [Overview](/guides/grasshopper/csharp-essentials/2-csharp-basics/#281-overview)  
&nbsp;&nbsp; 2.8.2 [Method parameters](/guides/grasshopper/csharp-essentials/2-csharp-basics/#282-method-parameters)  
   2.9 [User-defined data types](/guides/grasshopper/csharp-essentials/2-csharp-basics/#29-user-defined-data-types)  
&nbsp;&nbsp; 2.9.1 [Enumerations](/guides/grasshopper/csharp-essentials/2-csharp-basics/#291-enumerations)  
&nbsp;&nbsp; 2.9.2 [Structures](/guides/grasshopper/csharp-essentials/2-csharp-basics/#292-structures)  
&nbsp;&nbsp; 2.9.3 [Classes](/guides/grasshopper/csharp-essentials/2-csharp-basics/#293-classes)  
&nbsp;&nbsp; 2.9.4 [Value vs reference types](/guides/grasshopper/csharp-essentials/2-csharp-basics/#294-value-vs-reference-types)  
&nbsp;&nbsp; 2.9.5 [Interface](/guides/grasshopper/csharp-essentials/2-csharp-basics/#295-interface)  
   2.10 [Read and write text files](/guides/grasshopper/csharp-essentials/2-csharp-basics/#210--read--write-text-files)  
   2.11 [Recursive functions](/guides/grasshopper/csharp-essentials/2-csharp-basics/#211-recursive-functions)  

{{< /column >}}
{{< column >}} 


### 3. [RhinoCommon Geometry](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/)

   3.1 [Overview](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#31-overview)  
   3.2 [Geometry structures](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#32-geometry-structures)  
&nbsp;&nbsp; 3.2.1 [The Point3d structure](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#321-the-point3d-structure)  
&nbsp;&nbsp; 3.2.2 [Points and vectors](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#322-points--vectors)  
&nbsp;&nbsp; 3.2.3 [Lightweight curves](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#323-lightweight-curves)  
&nbsp;&nbsp; 3.2.4 [Lightweight surfaces](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#324-lightweight-surfaces)  
&nbsp;&nbsp; 3.2.5 [Lightweight surfaces](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#325-other-geometry-structures)  
   3.3 [Geometry classes](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#33-geometry-classes)  
&nbsp;&nbsp; 3.3.1 [Curves](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#331-curves)  
&nbsp;&nbsp; 3.3.2 [Surfaces](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#332-surfaces)  
&nbsp;&nbsp; 3.3.3 [Meshes](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#333-meshes)  
&nbsp;&nbsp; 3.3.4 [Boundary representation (Brep)](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#334-boundary-representation-brep)  
&nbsp;&nbsp; 3.3.5 [Other geometry classes](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#335-other-geometry-classes)  
   3.4 [Geometry transformations](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#34-geometry-transformations)  

### 4. [Design Algorithms](/guides/grasshopper/csharp-essentials/4-design-algorithms/)

   4.1 [Introduction](/guides/grasshopper/csharp-essentials/4-design-algorithms/#41-introduction)  
   4.2 [Geometry algorithms](/guides/grasshopper/csharp-essentials/4-design-algorithms/#42-geometry-algorithms)  
&nbsp;&nbsp; 4.2.1 [Sine curves and surface](/guides/grasshopper/csharp-essentials/4-design-algorithms/#421-sine-curves-and-surface)  
&nbsp;&nbsp; 4.2.2 [De Casteljau algorithm to interpolate a Bezier curve](/guides/grasshopper/csharp-essentials/4-design-algorithms/#421-sine-curves-and-surface)  
&nbsp;&nbsp; 4.2.3 [Simple subdivision mesh](/guides/grasshopper/csharp-essentials/4-design-algorithms/#422-de-casteljau-algorithm-to-interpolate-a-bezier-curve)  
   4.3 [Generative algorithms](/guides/grasshopper/csharp-essentials/4-design-algorithms/#43-generative-algorithms)  
&nbsp;&nbsp; 4.3.1 [Dragon curve](/guides/grasshopper/csharp-essentials/4-design-algorithms/#431-dragon-curve)  
&nbsp;&nbsp; 4.3.2 [Fractal tree](/guides/grasshopper/csharp-essentials/4-design-algorithms/#432-fractal-tree)  
&nbsp;&nbsp; 4.3.3 [Penrose tiling](/guides/grasshopper/csharp-essentials/4-design-algorithms/#433-penrose-tiling)  
&nbsp;&nbsp; 4.3.4 [Conway Game of Life](/guides/grasshopper/csharp-essentials/4-design-algorithms/#434-conway-game-of-life)  

{{< /column >}}
{{< /row >}}

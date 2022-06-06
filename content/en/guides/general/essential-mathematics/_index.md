+++
aliases = ["/5/guides/general/essential-mathematics/", "/6/guides/general/essential-mathematics/", "/7/guides/general/essential-mathematics/", "/wip/guides/general/essential-mathematics/"]
authors = [ "rajaa" ]
categories = [ "General" ]
description = "Introduces to design professionals the foundation mathematical concepts for effective development of computational 3D models."
keywords = [ "rhino", "developer" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "General" ]
title = "Essential Mathematics for Computational Design"
type = "guides"
weight = 1
override_last_modified = "2022-05-12T15:41:51Z"

[admin]
TODO = "This needs to be shimmed for Mac Platform."
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

### 1. [Vector Mathematics](/guides/general/essential-mathematics/vector-mathematics/)

   1.1 [Vector representation](/guides/general/essential-mathematics/vector-mathematics/#11-vector-representation)  
&nbsp;&nbsp; Position vector   
&nbsp;&nbsp; Vectors vs. points   
&nbsp;&nbsp; Vector length   
&nbsp;&nbsp; Unit vector    

   1.2 [Vector operations](/guides/general/essential-mathematics/vector-mathematics/#12-vector-operations)  
&nbsp;&nbsp; Vector scalar operation   
&nbsp;&nbsp; Vector addition    
&nbsp;&nbsp; Vector subtraction   
&nbsp;&nbsp; Vector properties  
&nbsp;&nbsp; Vector dot product   
&nbsp;&nbsp; Vector dot product, lengths, and angles    
&nbsp;&nbsp; Dot product properties    
&nbsp;&nbsp; Vector cross product   
&nbsp;&nbsp; Cross product and angle between vectors    
&nbsp;&nbsp; Cross product properties   

   1.3 [Vector equation of line](/guides/general/essential-mathematics/vector-mathematics/#13-vector-equation-of-line)  

   1.4 [Vector equation of a plane](/guides/general/essential-mathematics/vector-mathematics/#14-vector-equation-of-a-plane)  

   1.5 [Tutorials](/guides/general/essential-mathematics/vector-mathematics/#15-tutorials)   
&nbsp;&nbsp; Face direction  
&nbsp;&nbsp; Exploded box  
&nbsp;&nbsp; Tangent spheres  

{{< /column >}}
{{< column >}} 

### 2. [Matrices and Transformations](/guides/general/essential-mathematics/matrices-transformations/)
   2.1 [Matrix operations](/guides/general/essential-mathematics/matrices-transformations/#21-matrix-operations)  
&nbsp;&nbsp; Matrix multiplication  
&nbsp;&nbsp; Identity matrix  

   2.2 [Transformation operations](/guides/general/essential-mathematics/matrices-transformations/#22-transformation-operations)  
&nbsp;&nbsp; Translation (move) transformation   
&nbsp;&nbsp; Rotation transformation  
&nbsp;&nbsp; Scale transformation  
&nbsp;&nbsp; Shear transformation  
&nbsp;&nbsp; Mirror or reflection transformation  
&nbsp;&nbsp; Planar Projection transformation  

{{< /column >}}
{{< column >}} 


### 3. [Parametric Curves and Surfaces](/guides/general/essential-mathematics/parametric-curves-surfaces/)

   3.1 [Parametric curve](/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
&nbsp;&nbsp; Curve parameter  
&nbsp;&nbsp; Curve domain or interval  
&nbsp;&nbsp; Curve evaluation  
&nbsp;&nbsp; Tangent vector to a curve  
&nbsp;&nbsp; Cubic polynomial curves  
&nbsp;&nbsp; Evaluating cubic Bézier curves  

   3.2 [NURBS curves](/guides/general/essential-mathematics/parametric-curves-surfaces/#32-nurbs-curves)  
&nbsp;&nbsp; Degree  
&nbsp;&nbsp; Control points  
&nbsp;&nbsp; Weights of control points  
&nbsp;&nbsp; Knots  
&nbsp;&nbsp; Knots are parameter values  
&nbsp;&nbsp; Evaluation rule  
&nbsp;&nbsp; Characteristics of NURBS curves  
&nbsp;&nbsp; Evaluating NURBS curves  

   3.3 [Curve geometric continuity](/guides/general/essential-mathematics/parametric-curves-surfaces/#33-curve-geometric-continuity)   

   3.4 [Curve curvature](/guides/general/essential-mathematics/parametric-curves-surfaces/#34-curve-curvature)   

   3.5 [Parametric surfaces](/guides/general/essential-mathematics/parametric-curves-surfaces/#35-parametric-surfaces)   
&nbsp;&nbsp; Surface parameters  
&nbsp;&nbsp; Surface domain  
&nbsp;&nbsp; Surface evaluation  
&nbsp;&nbsp; Tangent plane of a surface  

   3.6 [Surface geometric continuity](/guides/general/essential-mathematics/parametric-curves-surfaces/#36-surface-geometric-continuity)     

   3.7 [Surface curvature](/guides/general/essential-mathematics/parametric-curves-surfaces/#37-surface-curvature)     
&nbsp;&nbsp; Principal curvatures  
&nbsp;&nbsp; Gaussian curvature  
&nbsp;&nbsp; Mean curvature  

   3.8 [NURBS surfaces](/guides/general/essential-mathematics/parametric-curves-surfaces/#38-nurbs-surfaces)     
&nbsp;&nbsp; Characteristics of NURBS surfaces  
&nbsp;&nbsp; Singularity in NURBS surfaces  
&nbsp;&nbsp; Trimmed NURBS surfaces  

   3.9 [Polysurfaces](/guides/general/essential-mathematics/parametric-curves-surfaces/#39-polysurfaces)     

   3.10 [Tutorials](/guides/general/essential-mathematics/parametric-curves-surfaces/#310-tutorials)     
&nbsp;&nbsp; Continuity between curves  
&nbsp;&nbsp; Surfaces with singularity  

{{< /column >}}
{{< /row >}}

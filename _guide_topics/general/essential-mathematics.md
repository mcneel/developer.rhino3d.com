---
title: Essential Mathematics for Computational Design
description: Introduces to design professionals the foundation mathematical concepts for effective development of computational 3D models.
authors: ['rajaa_issa']
sdk: ['General']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['General']
origin: unset
order: 1
keywords: ['rhino', 'developer']
layout: fullwidth-page
TODO: This needs to be shimmed for Mac Platform.
---

<div class="row">
<div class="col-12" markdown="1">   
# Essential Mathematics for Computational Design

</div>
<div class="col-md-7 col-sm-12 col-sm-12" markdown="1">  

*Essential Mathematics for Computational Design* introduces to design professionals the foundation mathematical concepts that are necessary for effective development of computational methods for 3D modeling and computer graphics. This is not meant to be a complete and comprehensive resource, but rather an overview of the basic and most commonly used concepts. The material is directed towards designers who have little or no background in mathematics beyond high school. All concepts are explained visually using [Grasshopper® (GH)](www.grasshopper3d.com), the generative modeling environment for [Rhinoceros® (Rhino)](www.rhino3d.com).  

The content is divided into three chapters. [Chapter 1]({{ site.baseurl }}/guides/general/essential-mathematics/vector-mathematics/) discusses vector math including vector representation, vector operation, and line and plane equations. [Chapter 2]({{ site.baseurl }}/guides/general/essential-mathematics/matrices-transformations/) reviews matrix operations and transformations. [Chapter 3]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/) includes an in-depth review of parametric curves with special focus on NURBS curves and the concepts of continuity and curvature.  It also reviews NURBS surfaces and polysurfaces.

*I would like to acknowledge the excellent and thorough technical review by [Dr. Dale Lear](https://discourse.mcneel.com/u/dalelear/activity) of Robert McNeel & Associates. His valuable comments were instrumental in producing this edition. I would also like to acknowledge Ms. [Margaret Becker](https://discourse.mcneel.com/u/margaret/activity) of Robert McNeel & Associates for reviewing the technical writing and formatting*.

</div>  

<div class="col-md-5 hidden-sm hidden-xs" markdown="1">   

![{{ site.baseurl }}/images/math-logo.svg]({{ site.baseurl }}/images/math-logo.svg){: width="100%"}

</div>  
</div>  

<div class="row">  
<div class="col-md-12" markdown="1">  

***[Rajaa Issa](https://discourse.mcneel.com/users/rajaa/activity)***

Robert McNeel & Associates

Download the <a href="{{ site.baseurl }}/files/math-samplesandtutorials.zip.zip"><span class="glyphicon glyphicon-download"></span></a> [math-samplesandtutorials.zip]({{ site.baseurl }}/files/math-samplesandtutorials.zip) archive, containing all the example Grasshopper and code files in this guide.

<a href="https://www.rhino3d.com/download/rhino/6/essentialmathematics"><span class="glyphicon glyphicon-download"></span></a> [Download Essential Mathematics for Computational Design as a single PDF ](https://www.rhino3d.com/download/rhino/6/essentialmathematics/)

<a href="https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK"><span class="glyphicon glyphicon-play"></span></a> [Watch the Essential Mathematics Videos... ](https://www.youtube.com/playlist?list=PLWIvZT_UEpWW6Kgq8mxOgliGBFHhrI4mK)

The current 4th Edition is availabe in four languages:

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

<div class="row-fluid">  
<div class="col-md-4" markdown="1">  

### 1. [Vector Mathematics]({{ site.baseurl }}/guides/general/essential-mathematics/vector-mathematics/)

   1.1 [Vector representation]({{ site.baseurl }}/guides/general/essential-mathematics/vector-mathematics/#11-vector-representation)  
&nbsp;&nbsp; Position vector   
&nbsp;&nbsp; Vectors vs. points   
&nbsp;&nbsp; Vector length   
&nbsp;&nbsp; Unit vector    

   1.2 [Vector operations]({{ site.baseurl }}/guides/general/essential-mathematics/vector-mathematics/#12-vector-operations)  
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

   1.3 [Vector equation of line]({{ site.baseurl }}/guides/general/essential-mathematics/vector-mathematics/#13-vector-equation-of-line)  

   1.4 [Vector equation of a plane]({{ site.baseurl }}/guides/general/essential-mathematics/vector-mathematics/#14-vector-equation-of-a-plane)  

   1.5 [Tutorials]({{ site.baseurl }}/guides/general/essential-mathematics/vector-mathematics/#15-tutorials)   
&nbsp;&nbsp; Face direction  
&nbsp;&nbsp; Exploded box  
&nbsp;&nbsp; Tangent spheres  

</div>
<div class="col-md-4" markdown="1"> 

### 2. [Matrices and Transformations]({{ site.baseurl }}/guides/general/essential-mathematics/matrices-transformations/)
   2.1 [Matrix operations]({{ site.baseurl }}/guides/general/essential-mathematics/matrices-transformations/#21-matrix-operations)  
&nbsp;&nbsp; Matrix multiplication  
&nbsp;&nbsp; Identity matrix  

   2.2 [Transformation operations]({{ site.baseurl }}/guides/general/essential-mathematics/matrices-transformations/#22-transformation-operations)  
&nbsp;&nbsp; Translation (move) transformation   
&nbsp;&nbsp; Rotation transformation  
&nbsp;&nbsp; Scale transformation  
&nbsp;&nbsp; Shear transformation  
&nbsp;&nbsp; Mirror or reflection transformation  
&nbsp;&nbsp; Planar Projection transformation  

</div>
<div class="col-md-4" markdown="1"> 


### 3. [Parametric Curves and Surfaces]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/)

   3.1 [Parametric curve]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/#31-parametric-curves)  
&nbsp;&nbsp; Curve parameter  
&nbsp;&nbsp; Curve domain or interval  
&nbsp;&nbsp; Curve evaluation  
&nbsp;&nbsp; Tangent vector to a curve  
&nbsp;&nbsp; Cubic polynomial curves  
&nbsp;&nbsp; Evaluating cubic Bézier curves  

   3.2 [NURBS curves]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/#32-nurbs-curves)  
&nbsp;&nbsp; Degree  
&nbsp;&nbsp; Control points  
&nbsp;&nbsp; Weights of control points  
&nbsp;&nbsp; Knots  
&nbsp;&nbsp; Knots are parameter values  
&nbsp;&nbsp; Evaluation rule  
&nbsp;&nbsp; Characteristics of NURBS curves  
&nbsp;&nbsp; Evaluating NURBS curves  

   3.3 [Curve geometric continuity]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/#33-curve-geometric-continuity)   

   3.4 [Curve curvature]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/#34-curve-curvature)   

   3.5 [Parametric surfaces]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/#35-parametric-surfaces)   
&nbsp;&nbsp; Surface parameters  
&nbsp;&nbsp; Surface domain  
&nbsp;&nbsp; Surface evaluation  
&nbsp;&nbsp; Tangent plane of a surface  

   3.6 [Surface geometric continuity]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/#36-surface-geometric-continuity)     

   3.7 [Surface curvature]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/#37-surface-curvature)     
&nbsp;&nbsp; Principal curvatures  
&nbsp;&nbsp; Gaussian curvature  
&nbsp;&nbsp; Mean curvature  

   3.8 [NURBS surfaces]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/#38-nurbs-surfaces)     
&nbsp;&nbsp; Characteristics of NURBS surfaces  
&nbsp;&nbsp; Singularity in NURBS surfaces  
&nbsp;&nbsp; Trimmed NURBS surfaces  

   3.9 [Polysurfaces]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/#39-polysurfaces)     

   3.10 [Tutorials]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces/#310-tutorials)     
&nbsp;&nbsp; Continuity between curves  
&nbsp;&nbsp; Surfaces with singularity  

</div>
</div>

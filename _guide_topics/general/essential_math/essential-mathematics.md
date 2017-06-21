---
title: Essential Mathematics for Computational Design
description: Introduces to design professionals the foundation mathematical concepts for effective development of computational 3-D models.
platforms: ['Windows' ]
layout: fullwidth-page
TODO: THis needs to be shimmed for Mac Platform.
---

# Essential Mathematics for Computational Design

*Essential Mathematics for Computational Design* introduces to design professionals the foundation mathematical concepts that are necessary for effective development of computational methods for 3-D modeling and computer graphics. This is not meant to be a complete and comprehensive resource, but rather an overview of the basic and most commonly used concepts. The material is directed towards designers who have little or no background in mathematics beyond high school. All concepts are explained visually using Grasshopper® (GH), the generative modeling environment for Rhinoceros® (Rhino). For more information, go to www.rhino3d.com and www.grasshopper3d.com.  The content is divided into three chapters. Chapter 1 discusses vector math including vector representation, vector operation, and line and plane equations. Chapter 2 reviews matrix operations and transformations. Chapter 3 includes an in-depth review of parametric curves with special focus on NURBS curves and the concepts of continuity and curvature.  It also reviews NURBS surfaces and polysurfaces. I would like to acknowledge the excellent and thorough technical review by Dr. Dale Lear of Robert McNeel & Associates. His valuable comments were instrumental in producing this third edition. I would also like to acknowledge Ms. Margaret Becker of Robert McNeel & Associates for reviewing the technical writing and formatting the document. 

**Rajaa Issa** 

Robert McNeel & Associate

### Table of Contents

<table id="math_table">  
<tbody>  
<tr>  
<td width="30%">  
  1.<a href="{{ site.baseurl }}/guides/general/essential_math/vector-mathematics/">Vector Mathematics</a>  
    <ol><li><a href="{{ site.baseurl }}/guides/general/essential_math/vector-mathematics/#11-vector-representation">1.1 Vector representation</a></li>   
        <ul> <li>Position vector</li>  
        <li>Vectors vs. points</li>  
        <li>Vector length</li>  
        <li>Unit vector</li></ul>   
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/vector-mathematics/#12-vector-operations">1.2 Vector operations</a></li>   
        <ul><li>Vector scalar operation</li>  
      	<li>Vector addition</li>   
        <li>Vector subtraction</li>  
        <li>Vector properties</li>
        <li>Vector dot product</li>  
        <li>Vector dot product, lengths, and angles</li>   
        <li>Dot product properties</li>   
        <li>Vector cross product</li>  
        <li>Cross product and angle between vectors</li>   
        <li>Cross product properties</li></ul>  
   <li><a href="{{ site.baseurl }}/guides/general/essential_math/vector-mathematics/#13-vector-equation-of-line">1.3 Vector equation of line</a></li>
   <li><a href="{{ site.baseurl }}/guides/general/essential_math/vector-mathematics/#14-vector-equation-of-a-plane">1.4 Vector equation of a plane</a></li>  
   <li><a href="{{ site.baseurl }}/guides/general/essential_math/vector-mathematics/#15-tutorials">1.5 Tutorials</a></li>  
      <ul><li>Face direction</li>  
        <li>Exploded box</li>
        <li>Tangent spheres</li></ul>  
	</ol>
</td>
<td width="30%">
   2. <a href="{{ site.baseurl }}/guides/general/essential_math/matrices-transformations/">Matrices and Transformations</a>
    <ol><li><a href="{{ site.baseurl }}/guides/general/essential_math/matrices-transformations/#21-matrix-operations">2.1 Matrix operations</a></li> 
        <ul><li>Matrix multiplication</li>  
            <li>Identity matrix</li></ul> 
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/matrices-transformations/#22-transformation-operations">2.2 Transformation operations</a></li> 
        <ul><li>Translation (move) transformation </li>  
            <li>Rotation transformation</li>   
            <li>Scale transformation</li>   
            <li>Shear transformation</li>   
            <li>Mirror or reflection transformation</li>   
            <li>Planar Projection transformation</li></ul>
    </ol>			
</td>
<td>
   3. <a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/">Parametric Curves and Surfaces</a>
    <ol><li><a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/#31-parametric-curves">3.1 Parametric curves</a></li>    
        <ul><li>Curve parameter</li>    
            <li>Curve domain or interval</li>    
            <li>Curve evaluation</li>    
            <li>Tangent vector to a curve</li>    
            <li>Cubic polynomial curves</li>    
            <li>Evaluating cubic Bézier curves</li></ul>    
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/#32-nurbs-curves">3.2 NURBS curves</a></li> 
        <ul><li>Degree</li>  
            <li>Control points</li>  
            <li>Weights of control points</li>  
            <li>Knots</li>  
            <li>Knots are parameter values</li>  
            <li>Evaluation rule</li>  
            <li>Characteristics of NURBS curves</li>  
            <li>Evaluating NURBS curves</li></ul>  
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/#33-curve-geometric-continuity">3.3 Curve geometric continuity</a></li>   
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/#34-curve-curvature">3.4Curve curvature</a></li>   
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/#35-parametric-surfaces">3.5Parametric surfaces</a></li>   
        <ul><li>Surface parameters</li>   
            <li>Surface domain</li>   
            <li>Surface evaluation</li>   
            <li>Tangent plane of a surface</li></ul>  
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/#36-surface-geometric-continuity">3.6 Surface geometric continuity</a></li>     
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/#37-surface-curvature">3.7 Surface curvature</a></li>     
        <ul><li>Principal curvatures</li>   
            <li>Gaussian curvature</li>   
            <li>Mean curvature</li></ul>   
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/#38-nurbs-surfaces">3.8 NURBS surfaces</a></li>     
        <ul><li>Characteristics of NURBS surfaces</li>   
            <li>Singularity in NURBS surfaces</li>   
            <li>Trimmed NURBS surfaces</li></ul>   
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/#39-polysurfaces">3.9 Polysurfaces</a></li>     
    <li><a href="{{ site.baseurl }}/guides/general/essential_math/parametric-curves-surfaces/#310-tutorials">3.10 Tutorials</a></li>     
        <ul><li>Continuity between curves</li>   
            <li>Surfaces with singularity</li></ul>
    </ol>			
</td>
</tr>
</tbody>
</table>

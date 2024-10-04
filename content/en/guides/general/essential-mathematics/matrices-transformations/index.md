+++
aliases = ["/en/5/guides/general/essential-mathematics/matrices-transformations/", "/en/6/guides/general/essential-mathematics/matrices-transformations/", "/en/7/guides/general/essential-mathematics/matrices-transformations/", "/wip/guides/general/essential-mathematics/matrices-transformations/"]
authors = [ "rajaa" ]
categories = [ "Essential Mathematics" ]
category_page = "guides/general/essential-mathematics/"
description = "This guide reviews matrix operations and transformations."
keywords = [ "mathematics", "geometry", "grasshopper3d" ]
languages = "unset"
sdk = [ "General" ]
title = "2 Matrices and Transformations"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

*Transformations* refer to operations such as moving (also called *translating*), rotating, and scaling objects. They are stored in 3 D programming using matrices, which are nothing but rectangular arrays of numbers. Multiple transformations can be performed very quickly using matrices. It turns out that a [4x4] matrix can represent all transformations. Having a unified matrix dimension for all transformations saves calculation time.

{{< mathjax >}}$$\begin{array}{rcc} \mbox{matrix}&\begin{array}{cccc} c1& c2&c3&c4\end{array}\\\begin{array}{c}row(1)\\row(2)\\row(3)\\row(4)\end{array}& \left[\begin{array}{cr} +&+&+&+\\  +&+&+&+\\ +&+&+&+\\ +&+&+&+\end{array}\right] \end{array}$${{< /mathjax >}}

## 2.1 Matrix operations

The one operation that is most relevant in computer graphics is matrix multiplication. We will explain it with some detail.

### Matrix multiplication

Matrix multiplication is used to apply transformations to geometry. For example if we have a point and would like to rotate it around some axis, we use a rotation matrix and multiply it by the point to get the new rotated location.


{{< mathjax >}}$$\begin{array}{ccc} \text{rotate matrix} & \text{input point}  & \text{rotate point}\\\begin{bmatrix}a & b & c & d \\e & f & g & h \\i & j & k & l \\0 & 0 & 0 & 1 \\\end{bmatrix}& \cdot\begin{bmatrix}x \\y\\z\\1 \\\end{bmatrix}&= \begin{bmatrix}x' \\y'\\z'\\1 \\\end{bmatrix}\end{array}$${{< /mathjax >}}    

Most of the time, we need to perform multiple transformations on the same geometry. For example, if we need to move and rotate a thousand points, we can use either of the following methods.

**Method 1**  

1. Multiply the move matrix by 1000 points to move the points.
2. Multiply the rotate matrix by the resulting 1000 points to rotate the moved points.  

Number of operations = **2000**.  

**Method 2**  

1. Multiply the rotate and move matrices to create a combined transformation matrix.
2. Multiply the combined matrix by 1000 points to move and rotate in one step.

Number of operations = **1001**.

Notice that method 1 takes almost twice the number of operations to achieve the same result. While method 2 is very efficient, it is only possible if both the move and rotate matrices are {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}}. This is why in computer graphics a {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}} matrix is used to represent all transformations, and a {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}} matrix is used to represent points.

Three-dimensional modeling applications provide tools to apply transformations and multiply matrices, but if you are curious about how to mathematically multiply matrices, we will explain a simple example. In order to multiply two matrices, they have to have matching dimensions. That means the number of columns in the first matrix must equal the number of rows of the second matrix. The resulting matrix has a size equal to the number of rows from the first matrix and the number of columns from the second matrix. For example, if we have two matrices, {{< mathjax >}}$$M$${{< /mathjax >}} and {{< mathjax >}}$$P$${{< /mathjax >}}, with dimensions equal to {{< mathjax >}}$$[4\times 4]$${{< /mathjax >}} and {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}} respectively, then there resulting multiplication matrix {{< mathjax >}}$$M · P$${{< /mathjax >}} has a dimension equal to {{< mathjax >}}$$[4 \times 1]$${{< /mathjax >}} as shown in the following illustration:

{{< mathjax >}}$$\begin{array}{ccc} M & P  & P' \\\begin{bmatrix}\color{red}{a} & \color{red}{b}  & \color{red}{c} & \color{red}{d}  \\e & f & g & h \\i & j & k & l \\0 & 0 & 0 & 1 \\\end{bmatrix}& \cdot\begin{bmatrix}\color{red}{x} \\\color{red}{y} \\\color{red}{z} \\\color{red}{1}  \\\end{bmatrix}&= \begin{bmatrix}\color{red}{x'=a*x+b*y+c*z+d*1}\\y'=e*x+f*y+g*z+h*1\\z'=i*x+j*y+k*z+l*1 \\1=0*x+0*y+0*z+1*1\\\end{bmatrix}\end{array}$${{< /mathjax >}}    

### Identity matrix

The identity matrix is a special matrix where all diagonal components equal 1 and the rest equal 0.

<img src="/images/math-image68.png">

The main property of the identity matrix is that if it is multiplied by any other matrix, the values multiplied by zero do not change.

<img src="/images/math-image52.png">

## 2.2 Transformation operations

Most transformations preserve the parallel relationship among the parts of the geometry. For example collinear points remain collinear after the transformation. Also points on one plane stay coplanar after transformation. This type of transformation is called an *affine* transformation.  

### Translation (move) transformation

Moving a point from a starting position by certain a vector can be calculated as follows:

{{< mathjax >}}$$P' = P + \mathbf{\vec v}$${{< /mathjax >}}  

{{< image url="/images/math-image35.png" alt="/images/math-image35.png" class="float_right" width="275" >}}   

Suppose:  
&nbsp; {{< mathjax >}}$$P(x,y,z)$${{< /mathjax >}} is a given point  
&nbsp; {{< mathjax >}}$$\mathbf{\vec v}=<a,b,c>$${{< /mathjax >}} is a translation vector  
Then:  
&nbsp; {{< mathjax >}}$$P'(x) = x + a$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'(y) = y + b$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'(z) = z + c$${{< /mathjax >}}  

{{< div class="clear_both" />}}  

Points are represented in a matrix format using a [4x1] matrix with a 1 inserted in the last row. For example the point P(x,y,z) is represented as follows:

{{< mathjax >}}$$\begin{bmatrix}x\\y\\z\\1\\\end{bmatrix}$${{< /mathjax >}}   

Using a {{< mathjax >}}$$[4 \times 4]$${{< /mathjax >}} matrix for transformations (what is called a homogenous coordinate system), instead of a {{< mathjax >}}$$[3 \times 3]$${{< /mathjax >}} matrices, allows representing all transformations including translation. The general format for a translation matrix is:  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 &  \color{red}{a1} \\0 & 1 & 0 & \color{red}{a2} \\0 & 0 & 1 &  \color{red}{a3} \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

For example, to move point {{< mathjax >}}$$P(2,3,1)$${{< /mathjax >}} by vector {{< mathjax >}}$$\vec v <2,2,2>$${{< /mathjax >}}, the new point location is:

{{< mathjax >}}$$P’ = P + \mathbf{\vec v} = (2+2, 3+2, 1+2) = (4, 5, 3)$${{< /mathjax >}}  

If we use the matrix form and multiply the translation matrix by the input point, we get the new point location as in the following:

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 2 \\0 & 1 & 0 & 2 \\0 & 0 & 1 & 2 \\0 & 0 & 0 & 1 \\\end{bmatrix}\cdot\begin{bmatrix}2 \\3\\1\\1 \\\end{bmatrix}= \begin{bmatrix}(1*2 + 0*3 + 0*1 + 2*1) \\(0*2 + 1*3 + 0*1 + 2*1)\\(0*2 + 0*3 + 1*1 + 2*1)\\(0*2 + 0*3 + 0*1 + 1*1)\\\end{bmatrix}=\begin{bmatrix}4 \\5\\3\\1 \\\end{bmatrix}$${{< /mathjax >}}   

Similarly, any geometry is translated by multiplying its construction points by the translation matrix. For example, if we have a box that is defined by eight corner points, and we want to move it 4 units in the x-direction, 5 units in the y-direction and 3 units in the z- direction, we must multiply each of the eight box corner points by the following translation matrix to get the new box.  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 4\\ 0 & 1 & 0 & 5 \\0 & 0 & 1 & 3 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

<figure>
   <img src="/images/math-image37.png">
   <figcaption>Figure (19): Translate all box corner points.</figcaption>
</figure>  

### Rotation transformation

This section shows how to calculate rotation around the z-axis and the origin point using trigonometry, and then to deduce the general matrix format for the rotation.

{{< image url="/images/math-image39.png" alt="/images/math-image39.png" class="float_right" width="275" >}}   

Take a point on {{< mathjax >}}$$x,y$${{< /mathjax >}} plane {{< mathjax >}}$$P(x,y)$${{< /mathjax >}} and rotate it by angle({{< mathjax >}}$$b$${{< /mathjax >}}).  From the figure, we can say the following:  

&nbsp; {{< mathjax >}}$$x = d cos(a)$${{< /mathjax >}}   (1)  
&nbsp; {{< mathjax >}}$$y = d sin(a)$${{< /mathjax >}}    (2)  
&nbsp; {{< mathjax >}}$$x' = d cos(b+a)$${{< /mathjax >}}  (3)  
&nbsp; {{< mathjax >}}$$y' = d sin(b+a)$${{< /mathjax >}}   (4)  
Expanding {{< mathjax >}}$$x$${{< /mathjax >}}' and {{< mathjax >}}$$y'$${{< /mathjax >}} using trigonometric identities for the sine and cosine of the sum of angles:  
&nbsp; {{< mathjax >}}$$x' = d cos(a)cos(b) - d sin(a)sin(b)$${{< /mathjax >}}  (5)  
&nbsp; {{< mathjax >}}$$y' = d cos(a)sin(b) + d sin(a)cos(b)$${{< /mathjax >}}  (6)  
Using Eq 1 and 2:  
&nbsp; {{< mathjax >}}$$x' = x cos(b) - y sin(b)$${{< /mathjax >}}  
&nbsp; y' = x sin(b) + y cos(b)  

The rotation matrix around the **z-axis** looks like:  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{\cos{b}} & \color{red}{-\sin{b}} & 0 & 0 \\\color{red}{\sin{b}} & \color{red}{\cos{b}} & 0 & 0 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

The rotation matrix around the **x-axis** by angle {{< mathjax >}}$$b$${{< /mathjax >}} looks like:  

{{< mathjax >}}$$\begin{bmatrix}1 & 0 & 0 & 0 \\0 & \color{red}{\cos{b}} & \color{red}{-\sin{b}} & 0 \\0 & \color{red}{\sin{b}} & \color{red}{\cos{b}} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

The rotation matrix around the **y-axis** by angle {{< mathjax >}}$$b$${{< /mathjax >}} looks like:  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{\cos{b}} &0 & \color{red}{\sin{b}} & 0 \\0 & 1 & 0 & 0 \\\color{red}{-\sin{b}} & 0 &\color{red}{\cos{b}} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

For example, if we have a box and would like to rotate it 30 degrees, we need the following:  

1\. Construct the 30-degree rotation matrix. Using the generic form and the cos and sin values of 30-degree angle, the rotation matrix will look like the following:  

{{< mathjax >}}$$\begin{bmatrix}0.87 & -0.5 & 0 & 0 \\0.5 & 0.87 & 0 & 0 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}   

2\. Multiply the rotation matrix by the input geometry, or in the case of a box, multiply by each of the corner points to find the box's new location.  

<figure>
   <img src="/images/math-image41.png">
   <figcaption>Figure (20): Rotate geometry.</figcaption>
</figure>  

### Scale transformation

In order to scale geometry, we need a scale factor and a center of scale. The scale factor can be uniform scaling equally in x-, y-, and z-directions, or can be unique for each dimension.   

Scaling a point can use the following equation:  

&nbsp; {{< mathjax >}}$$P' = ScaleFactor(S) * P$${{< /mathjax >}}  

Or:  

&nbsp; {{< mathjax >}}$$P'.x = Sx * P.x$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'.y = Sy * P.y$${{< /mathjax >}}  
&nbsp; {{< mathjax >}}$$P'.z = Sz * P.z$${{< /mathjax >}}  

This is the matrix format for scale transformation, assuming that the center of scale is the World origin point (0,0,0).  

{{< mathjax >}}$$\begin{bmatrix}\color{red}{Scale-x} & 0 & 0 & 0 \\0 & \color{red}{Scale-y} & 0 & 0 \\0 & 0 & \color{red}{Scale-z} & 0 \\0 & 0 & 0 & 1 \\\end{bmatrix}$${{< /mathjax >}}  

For example, if we would like to scale a box by 0.25 relative to the World origin, the scale matrix will look like the following:

<figure>
   <img src="/images/math-image43.png">
   <figcaption>Figure (21): Scale geometry</figcaption>
</figure>  

### Shear transformation  

Shear in 3‑D is measured along a pair of axes relative to a third axis. For example, a shear along a z‑axis will not change geometry along that axis, but will alter it along x and y. Here are few examples of shear matrices:

1\. Shear in x and z, keeping the y-coordinate fixed:


{{< image url="/images/math-image45.png" alt="/images/math-image45.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 &\color{red}{0.5} & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image47.png" alt="/images/math-image47.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 &\color{red}{0.5} & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

2\. Shear in y and z, keeping the x-coordinate fixed:  


{{< image url="/images/math-image49.png" alt="/images/math-image49.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 & \color{red}{0.5} & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image50.png" alt="/images/math-image50.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & \color{red}{0.5} & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

3\. Shear in x and y, keeping the z-coordinate fixed:

{{< image url="/images/math-image32.png" alt="/images/math-image32.png" class="float_left" width="100" >}}   

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & \color{red}{0.5} & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   


{{< div class="clear_both" />}}  

{{< image url="/images/math-image33.png" alt="/images/math-image33.png" class="float_left" width="100" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & \color{red}{0.5} & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< div class="clear_both" />}}  

### Mirror or reflection transformation

The mirror transformation creates a reflection of an object across a line or a plane. 2-D objects are mirrored across a line, while 3-D objects are mirrored across a plane. Keep in mind that the mirror transformation flips the normal direction of the geometry faces.  

<figure>
   <img src="/images/math-image98.png">
   <figcaption>Figure (23): Mirror matrix across World xy-plane. Face directions are flipped.</figcaption>
</figure>  

### Planar Projection transformation

Intuitively, the projection point of a given 3-D point {{< mathjax >}}$$P(x,y,z)$${{< /mathjax >}} on the world xy-plane equals {{< mathjax >}}$$P_{xy} (x,y,0)$${{< /mathjax >}} setting the z value to zero. Similarly, a projection to xz-plane of point P is {{< mathjax >}}$$P_{xz}(x,0,z)$${{< /mathjax >}}. When projecting to yz-plane, {{< mathjax >}}$$P_{xz} = (0,y,z)$${{< /mathjax >}}. Those are called orthogonal projections.   

If we have a curve as an input, and we apply the planar projection transformation, we get a curve projected to that plane. The following shows an example of a curve projected to xy‑plane with the matrix format.  

Note: NURBS curves (explained in the next chapter) use control points to define curves. Projecting a curve amounts to projecting its control points.  

{{< image url="/images/math-image100.png" alt="/images/math-image100.png" class="float_left" width="175" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & \color{red}{0.0} & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< image url="/images/math-image102.png" alt="/images/math-image102.png" class="float_left" width="175" >}}    

{{< mathjax >}}$$\begin{bmatrix}1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & \color{red}{0.0} & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

{{< image url="/images/math-image104.png" alt="/images/math-image104.png" class="float_left" width="175" >}}    

{{< mathjax >}}$$\begin{bmatrix} \color{red}{0.0} & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 &  0.0 & 0.0 & 1.0 \\\end{bmatrix}$${{< /mathjax >}}   

## Download Sample Files

Download the [{{< awesome "fas fa-download">}} ](/files/math-samplesandtutorials.zip.zip) [math-samplesandtutorials.zip](/files/math-samplesandtutorials.zip) archive, containing all the example Grasshopper and code files in this guide.

## Next Steps

Now that you know more about matrices and trasnformasion, check out the [Parametric Curves and Surfaces](/guides/general/essential-mathematics/parametric-curves-surfaces/) guide to learn more about the detailed structure of NURBS curves and surfaces.  

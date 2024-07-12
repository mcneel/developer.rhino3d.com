+++
aliases = ["/5/guides/general/essential-mathematics/vector-mathematics/", "/6/guides/general/essential-mathematics/vector-mathematics/", "/7/guides/general/essential-mathematics/vector-mathematics/", "/wip/guides/general/essential-mathematics/vector-mathematics/"]
authors = [ "rajaa" ]
categories = [ "Essential Mathematics" ]
category_page = "guides/general/essential-mathematics/"
description = "This guide discusses vector math including vector representation, vector operation, and line and plane equations."
keywords = [ "mathematics", "geometry", "grasshopper3d" ]
languages = "unset"
sdk = [ "General" ]
title = "1 Vector Mathematics"
type = "guides"
weight = 1
override_last_modified = "2021-06-03T20:37:31Z"

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
A vector indicates a quantity, such as velocity or force, that has direction and length. Vectors in 3D coordinate systems are represented with an ordered set of three real numbers and look like:

{{< mathjax >}}$$\mathbf{\vec v}  = <a_1, a_2, a_3>$${{< /mathjax >}}

{{< youtube NU34_aCoN3E >}}

## 1.1 Vector representation

In this document, lower case bold letters with arrow on top will notate vectors. Vector components are also enclosed in angle brackets. Upper case letters will notate points. Point coordinates will always be enclosed by parentheses.

Using a coordinate system and any set of anchor points in that system, we can represent or visualize these vectors using a line-segment representation. An arrowhead shows the vector direction.

For example, if we have a vector that has a direction parallel to the x-axis of a given 3D coordinate system and a length of 5 units, we can write the vector as follows:

{{< mathjax >}}$$\mathbf{\vec v} = <5, 0, 0>$${{< /mathjax >}}  

To represent that vector, we need an anchor point in the coordinate system. For example, all of the arrows in the following figure are equal representations of the same vector despite the fact that they are anchored at different locations.  

<figure>
   <img src="/images/math-image169.png">
   <figcaption>Figure (1): Vector representation in the 3-D coordinate system.</figcaption>
</figure>  

{{< call-out note "Note" >}}

Given a 3D vector {{< mathjax >}}$$\vec v = <a_1, a_2, a_3>$${{< /mathjax >}} , all vector components {{< mathjax >}}$$a_1$${{< /mathjax >}}, {{< mathjax >}}$$a_2$${{< /mathjax >}}, {{< mathjax >}}$$a_3$${{< /mathjax >}} are real numbers. Also all line segments from a point {{< mathjax >}}$$A(x,y,z)$${{< /mathjax >}} to point {{< mathjax >}}$$B(x+a_1, y+a_2, z+a_3)$${{< /mathjax >}} are equivalent representations of vector {{< mathjax >}}$$\vec v$${{< /mathjax >}}.

{{< /call-out >}}   

So, how do we define the end points of a line segment that represents a given vector?
Let us define an anchor point (A) so that:

{{< mathjax >}}$$A = (1, 2, 3)$${{< /mathjax >}}

And a vector:

{{< mathjax >}}$$\mathbf{\vec v} = <5, 6, 7>$${{< /mathjax >}}

The tip point {{< mathjax >}}$$(B)$${{< /mathjax >}} of the vector is calculated by adding the corresponding components from anchor point and vector {{< mathjax >}}$$\vec v$${{< /mathjax >}}:  

{{< mathjax >}}$$B = A + \mathbf{\vec v}$${{< /mathjax >}}  
{{< mathjax >}}$$B = (1+5, 2+6, 3+7) $${{< /mathjax >}}  
{{< mathjax >}}$$B = (6, 8, 10)$${{< /mathjax >}}  


<figure>
   <img src="/images/math-image172.png">
   <figcaption>Figure (2): The relationship between a vector, the vector anchor point, and the point coinciding with the vector tip location.</figcaption>
</figure>  

{{< youtube ELQ8NgENhJY >}}
{{< youtube INtNgczxyWg >}}

### Position vector

One special vector representation uses the {{< mathjax >}}$$\text{origin point} (0,0,0)$${{< /mathjax >}} as the vector anchor point.
The position vector {{< mathjax >}}$$\mathbf{\vec v} = <a_1,a_2,a_3>$${{< /mathjax >}} is represented with a line segment between two points, the origin and the tip point B, so that:  

{{< mathjax >}}$$\text{Origin point} = (0,0,0)$${{< /mathjax >}}  
{{< mathjax >}}$$B = (a_1,a_2,a_3)$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image171.png">
   <figcaption>Figure (3): Position vector. The tip point coordinates equal the corresponding vector components.</figcaption>
</figure>  

{{< call-out note "Note" >}}

A *position vector* for a given vector {{< mathjax >}}$$\vec v= < a_1,a_2,a_3 >$${{< /mathjax >}} is a special line segment representation from the origin point {{< mathjax >}}$$(0,0,0)$${{< /mathjax >}} to point {{< mathjax >}}$$(a_1, a_2, a_3)$${{< /mathjax >}}.

{{< /call-out >}}

{{< youtube 8BNyMC4EBcw >}}

{{< youtube Ft2edI4g1qY >}}

### Vectors vs. points  

Do not confuse vectors and points. They are very different concepts. Vectors, as we mentioned, represent a quantity that has direction and length, while points indicate a location. For example, the North direction is a vector, while the North Pole is a location (point).
If we have a vector and a point that have the same components, such as:  

{{< mathjax >}}$$\mathbf{\vec v} = <3,1,0>$${{< /mathjax >}}  
{{< mathjax >}}$$P = (3,1,0)$${{< /mathjax >}}  

We can draw the vector and the point as follows:  

<figure>
   <img src="/images/math-image174.png">
   <figcaption>Figure (4): A vector defines a direction and length. A point defines a location.</figcaption>
</figure>  

{{< youtube RRrTz_QO_rA >}}

### Vector length  

As mentioned before, vectors have length. We will use {{< mathjax >}}$$\vert a \vert$${{< /mathjax >}} to notate the length of a given vector {{< mathjax >}}$$ a $${{< /mathjax >}}. For example:  

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = 5$${{< /mathjax >}}  

In general, the length of a vector {{< mathjax >}}$$\mathbf{\vec a} <a_1,a_2,a_3>$${{< /mathjax >}} is calculated as follows:

{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{(a_1)^2 + (a_2)^2 + (a_3)^2} $${{< /mathjax >}}

<figure>
   <img src="/images/math-image173.png">
   <figcaption>Figure (5): Vector length.</figcaption>
</figure>  

### Unit vector

A unit vector is a vector with a length equal to one unit. Unit vectors are commonly used to compare the directions of vectors.

{{< call-out note "Note" >}}

A unit vector is a vector whose length is equal to one unit.

{{< /call-out >}}

To calculate a unit vector, we need to find the length of the given vector, and then divide the vector components by the length. For example:

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec a} \vert  = 5 \text{ unit length}$${{< /mathjax >}}  

If {{< mathjax >}}$$\mathbf{\vec b} = \text{unit vector}$${{< /mathjax >}} of {{< mathjax >}}$$a$${{< /mathjax >}}, then:  
&nbsp;&nbsp;     {{< mathjax >}}$$\mathbf{\vec b} = <4/5, 3/5, 0/5>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\mathbf{\vec b} = <0.8, 0.6, 0>$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{0.8^2 + 0.6^2 + 0^2}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{0.64 + 0.36 + 0}$${{< /mathjax >}}  
&nbsp;&nbsp;     {{< mathjax >}}$$\vert \mathbf{\vec b} \vert  = \sqrt{(1)} = 1 \text{ unit length}$${{< /mathjax >}}  

In general:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  

The unit vector of {{< mathjax >}}$$\mathbf{\vec a} = <a_1/\vert \mathbf{\vec a} \vert , a_2/\vert \mathbf{\vec a} \vert , a_3/\vert \mathbf{\vec a} \vert >$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image176.png">
   <figcaption>Figure (6): Unit vector equals one-unit length of the vector.</figcaption>
</figure>  

{{< youtube yVSigpl3EUo >}}

## 1.2 Vector operations

{{< youtube uInxocphhxI >}}

### Vector scalar operation

Vector scalar operation involves multiplying a vector by a number. For example:  

{{< mathjax >}}$$\mathbf{\vec a} = <4, 3, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$2* \mathbf{\vec a} = <2*4, 2*3, 2*0> $${{< /mathjax >}}  
{{< mathjax >}}$$2*\mathbf{\vec a} = <8, 6, 0>$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image175.png">
   <figcaption>Figure (7): Vector scalar operation</figcaption>
</figure>  

In general, given vector {{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}, and a real number {{< mathjax >}}$$t$${{< /mathjax >}}   

{{< mathjax >}}$$t*\mathbf{\vec a} = < t* a_1, t* a_2, t* a_3 >$${{< /mathjax >}}  

{{< youtube S59M8BnDYAQ >}}

### Vector addition

Vector addition takes two vectors and produces a third vector. We add vectors by adding their components.

{{< call-out note "Note" >}}

Vectors are added by adding their components.

{{< /call-out >}}

For example, if we have two vectors:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 0> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <4, 1, 3> $${{< /mathjax >}}   
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <1+4, 2+1, 0+3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <5, 3, 3>$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image179.png">
   <figcaption>Figure (8): Vector addition.</figcaption>
</figure>  

In general, vector addition of the two vectors a and b is calculated as follows:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}+\mathbf{\vec b} = <a_1+b_1, a_2+b_2, a_3+b_3>$${{< /mathjax >}}  

Vector addition is useful for finding the average direction of two or more vectors. In this case, we usually use same-length vectors. Here is an example that shows the difference between using same-length vectors and different-length vectors on the resulting vector addition:  

<figure>
   <img src="/images/math-image177.png">
   <figcaption>Figure (9): Adding various length vectors (left). Adding same length vectors (right) to get the average direction.</figcaption>
</figure>  

Input vectors are not likely to be same length. In order to find the average direction, you need to use the unit vector of input vectors. As mentioned before, the unit vector is a vector of that has a length equal to 1.

{{< youtube VTVk3t3WeAY >}}

### Vector subtraction

Vector subtraction takes two vectors and produces a third vector. We subtract two vectors by subtracting corresponding components. For example, if we have two vectors {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} and {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} and we subtract {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} from {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, then:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 0> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <4, 1, 4> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <1-4, 2-1, 0-4>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <-3, 1, -4> = \mathbf{\mathbf{\vec b}a}$${{< /mathjax >}}

If we subtract {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} from {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, we get a different result:  

{{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a} = <4-1, 1-2, 4-0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a} = <3, -1, 4> = \mathbf{\mathbf{\vec a}b}$${{< /mathjax >}}  

Note that the vector {{< mathjax >}}$$\mathbf{\vec b} - \mathbf{\vec a}$${{< /mathjax >}} has the same length as the vector {{< mathjax >}}$$\mathbf{\vec a} - \mathbf{\vec b}$${{< /mathjax >}}, but goes in the opposite direction.  

<figure>
   <img src="/images/math-image178.png">
   <figcaption>Figure (10): Vector subtraction.</figcaption>
</figure>  

In general, if we have two vectors, {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} and {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}, then {{< mathjax >}}$$\mathbf{\vec a} - \mathbf{\vec b}$${{< /mathjax >}} is a vector that is calculated as follows:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}-\mathbf{\vec b} = <a_1 - b_1, a_2 - b_2, a_3 - b_3> = \mathbf{\mathbf{\vec b}a}$${{< /mathjax >}}  

Vector subtraction is commonly used to find vectors between points. So if we need to find a vector that goes from the tip point of the position vector {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} to the tip point of the position vector {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, then we use vector subtraction {{< mathjax >}}$$(\mathbf{\vec a}-\mathbf{\vec b})$${{< /mathjax >}} as shown in Figure (11).  

<figure>
   <img src="/images/math-image180.png">
   <figcaption>Figure (11): Use vector subtraction to find a vector between two points. </figcaption>
</figure> 

{{< youtube RQK8pCIWKNY >}} 

### Vector properties

There are eight properties of vectors. If a, b, and c are vectors, and s and t are numbers, then:  

{{< mathjax >}}$$\mathbf{\vec a} + \mathbf{\vec b} = \mathbf{\vec b} + \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + 0 = a$${{< /mathjax >}}  
{{< mathjax >}}$$s * (\mathbf{\vec a} + \mathbf{\vec b}) = s * a + s * \mathbf{\vec b}$${{< /mathjax >}}  
{{< mathjax >}}$$s * t * (\mathbf{\vec a}) = s * (t * \mathbf{\vec a})$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + (\mathbf{\vec b} + \mathbf{\vec c}) = (\mathbf{\vec a} + \mathbf{\vec b}) + \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} + (-\mathbf{\vec a}) = 0$${{< /mathjax >}}  
{{< mathjax >}}$$(s + t) * \mathbf{\vec a} = s * \mathbf{\vec a} + t * \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$1 * \mathbf{\vec a} = \mathbf{\vec a}$${{< /mathjax >}}  

### Vector dot product

The dot product takes two vectors and produces a number.
For example, if we have the two vectors a and b so that:

{{< mathjax >}}$$\mathbf{\vec a} = <1, 2, 3> $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <5, 6, 7>$${{< /mathjax >}}  

Then the dot product is the sum of multiplying the components as follows:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = 1 * 5 + 2 * 6 + 3 * 7$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = 38$${{< /mathjax >}}  

In general, given the two vectors a and b:  

{{< mathjax >}}$$\mathbf{\vec a} = <a_1, a_2, a_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <b_1, b_2, b_3>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = a_1 * b_1 + a_2 * b_2 + a_3 * b_3$${{< /mathjax >}}  

We always get a positive number for the dot product between two vectors when they go in the same general direction. A negative dot product between two vectors means that the two vectors go in the opposite general direction.

<figure>
   <img src="/images/math-image181.png">
   <figcaption>Figure (12): When the two vectors go in the same direction (left), the result is a positive dot product. When the two vectors go in the opposite direction (right), the result is a negative dot product. </figcaption>
</figure>  

When calculating the dot product of two unit vectors, the result is always between 1 and +1. For example:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <0.6, 0.8, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = (1 * 0.6, 0 * 0.8, 0 * 0) = 0.6$${{< /mathjax >}}  

In addition, the dot product of a vector with itself is equal to that vector’s length to the power of two. For example:  

{{< mathjax >}}$$\mathbf{\vec a} = <0, 3, 4>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = 0 * 0 + 3 * 3 + 4 * 4 $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = 25$${{< /mathjax >}}  

Calculating the square length of vector {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} :  

{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = \sqrt{4^2 + 3^2 + 0^2}$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert = 5$${{< /mathjax >}}  
{{< mathjax >}}$$\vert \mathbf{\vec a} \vert 2 = 25$${{< /mathjax >}}  

### Vector dot product, lengths, and angles

There is a relationship between the dot product of two vectors and the angle between them.  

{{< call-out note "Note" >}}

The dot product of two non-zero unit vectors equals the cosine of the angle between them.

{{< /call-out >}}

In general:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = \vert \mathbf{\vec a} \vert * \vert \mathbf{\vec b} \vert * cos(ө)$${{< /mathjax >}} , or  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} / (\vert \mathbf{\vec a} \vert * \vert \mathbf{\vec b} \vert) = cos(ө)$${{< /mathjax >}}

Where:  

{{< mathjax >}}$$ө$${{< /mathjax >}} is the angle included between the vectors.  

If vectors a and b are unit vectors, we can simply say:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = cos(ө)$${{< /mathjax >}}  

And since the cosine of a 90-degree angle is equal to 0, we can say:  

{{< call-out note "Note" >}}

Vectors {{< mathjax >}}$$\vec a$${{< /mathjax >}} and {{< mathjax >}}$$\vec b$${{< /mathjax >}} are orthogonal if, and only if, {{< mathjax >}}$$\vec{a} \cdot  \vec{b} = 0$${{< /mathjax >}}.

{{< /call-out >}}

For example, if we calculate the dot product of the two orthogonal vectors, World xaxis and yaxis, the result will equal zero.  

{{< mathjax >}}$$\mathbf{\vec x} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec y} = <0, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec x} · \mathbf{\vec y} = (1 * 0) + (0 * 1) + (0 * 0)$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec x} · \mathbf{\vec y} = 0$${{< /mathjax >}}  

There is also a relationship between the dot product and the projection length of one vector onto another. For example:  

{{< mathjax >}}$$\mathbf{\vec a} = <5, 2, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <9, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$unit(\mathbf{\vec b}) = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · unit(\mathbf{\vec b}) = (5 * 1) + (2 * 0) + (0 * 0) $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · unit(\mathbf{\vec b}) = 2 (\text{which is equal to the projection length of mathbf{\vec a} onto mathbf{\vec b}})$${{< /mathjax >}}

<figure>
   <img src="/images/math-image182.png">
   <figcaption>Figure (13): The dot product equals the projection length of one vector onto a non-zero unit vector. </figcaption>
</figure>  

In general, given a vector a and a non-zero vector b, we can calculate the projection length pL of vector a onto vector b using the dot product.  

{{< mathjax >}}$$pL = \vert \mathbf{\vec a} \vert * cos(ө) $${{< /mathjax >}}  
{{< mathjax >}}$$pL = \mathbf{\vec a} · unit(\mathbf{\vec b})$${{< /mathjax >}} 

 {{< youtube ZsM2RQbVDf4 >}}

### Dot product properties

If {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}, and {{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} are vectors and s is a number, then:  

{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec a} = \vert  \mathbf{\vec a} \vert ^2$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b} + \mathbf{\vec c}) = \mathbf{\vec a} · \mathbf{\vec b} + \mathbf{\vec a} · \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$0 · \mathbf{\vec a} = 0$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · \mathbf{\vec b} = \mathbf{\vec b} · \mathbf{\vec a}$${{< /mathjax >}}  
{{< mathjax >}}$$(s * \mathbf{\vec a}) · \mathbf{\vec b} = s * (\mathbf{\vec a} · \mathbf{\vec b}) = \mathbf{\vec a} · (s * \mathbf{\vec b})$${{< /mathjax >}}  

### Vector cross product

The cross product takes two vectors and produces a third vector that is orthogonal to both.

<figure>
   <img src="/images/math-image183.png">
   <figcaption>Figure (14): Calculating the cross product of two vectors. </figcaption>
</figure>  

For example, if you have two vectors lying on the World xy-plane, then their cross product is a vector perpendicular to the xy-plane going either in the positive or negative World z-axis direction. For example:  

{{< mathjax >}}$$\mathbf{\vec a} = <3, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <1, 2, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = < (1 * 0 – 0 * 2), (0 * 1 - 3 * 0), (3 * 2 - 1 * 1) > $${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <0, 0, 5>$${{< /mathjax >}}  

{{< call-out note "Note" >}}

The vector {{< mathjax >}}$$\vec a \times \vec b$${{< /mathjax >}} is orthogonal to both {{< mathjax >}}$$\vec a$${{< /mathjax >}} and {{< mathjax >}}$$\vec b$${{< /mathjax >}}.

{{< /call-out >}}

You will probably never need to calculate a cross product of two vectors by hand, but if you are curious about how it is done, continue reading; otherwise you can safely skip this section. The cross product {{< mathjax >}}$$a × b$${{< /mathjax >}} is defined using determinants. Here is a simple illustration of how to calculate a determinant using the standard basis vectors:  

{{< mathjax >}}$$ \color {red}{i} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$ \color {blue}{j} = <0,1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$ \color {green}{k} = <0, 0, 1>$${{< /mathjax >}}  

<img src="/images/math-image184.png">

The cross product of the two vectors {{< mathjax >}}$$\mathbf{\vec a} = <a1, a2, a3>$${{< /mathjax >}} and {{< mathjax >}}$$\mathbf{\vec b} = <b1, b2, b3>$${{< /mathjax >}} is calculated as follows using the above diagram:  

{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = \color {red}{i (a_2 * b_3)} + \color {blue}{ j (a_3 * b_1)} + \color {green}{k(a_1 * b_2)} - \color {green}{k (a_2 * b_1)} - \color {red}{i (a_3 * b_2)} -\color {blue}{ j (a_1 * b_3)}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = \color {red}{i (a_2 * b_3 - a_3 * b_2)} + \color {blue}{j (a_3 * b_1 - a_1 * b_3)} +\color {green}{k (a_1 * b_2 - a_2 * b_1)}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <\color {red}{a_2 * b_3 – a_3 * b_2},  \color {blue}{a_3 * b_1 - a_1 * b_3},  \color {green}{a_1 * b_2 - a_2 * b_1} >$${{< /mathjax >}}  

{{< youtube I5WkhSo4p6o >}}

### Cross product and angle between vectors

There is a relationship between the angle between two vectors and the length of their cross product vector. The smaller the angle (smaller sine); the shorter the cross product vector will be. The order of operands is important in vectors cross product. For example:  

{{< mathjax >}}$$\mathbf{\vec a} = <1, 0, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <0, 1, 0>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = <0, 0, 1>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} × \mathbf{\vec a} = <0, 0, -1>$${{< /mathjax >}}  


<figure>
   <img src="/images/math-image185.png">
   <figcaption>Figure (15): The relationship between the sine of the angle between two vectors and the length of their cross product vector.</figcaption>
</figure>  

In Rhino's right-handed system, the direction of {{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b}$${{< /mathjax >}} is given by the right-hand rule (where {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} = index finger, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} = middle finger, and {{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b}$${{< /mathjax >}} = thumb).  

<img src="/images/math-image186.png" width="375px">  

In general, for any pair of 3-D vectors {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} and {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}:  

{{< mathjax >}}$$\vert \mathbf{\vec a} × \mathbf{\vec b} \vert  = \vert  \mathbf{\vec a} \vert  \vert  \mathbf{\vec b} \vert  sin(ө)$${{< /mathjax >}}  

Where:   

{{< mathjax >}}$$ө$${{< /mathjax >}} is the angle included between the position vectors of {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} and {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}  

If a and b are unit vectors, then we can simply say that the length of their cross product equals the sine of the angle between them. In other words:  

{{< mathjax >}}$$\vert \mathbf{\vec a} × \mathbf{\vec b} \vert = sin(ө)$${{< /mathjax >}}  

The cross product between two vectors helps us determine if two vectors are parallel. This is because the result is always a zero vector.  

{{< call-out note "Note" >}}

Vectors {{< mathjax >}}$$\vec a$${{< /mathjax >}} and {{< mathjax >}}$$\vec b$${{< /mathjax >}} are parallel if, and only if, {{< mathjax >}}$$a \times b = 0$${{< /mathjax >}}.

{{< /call-out >}}

### Cross product properties

If {{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}}, {{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}}, and {{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} are vectors, and {{< mathjax >}}$$s$${{< /mathjax >}} is a number, then:  
{{< mathjax >}}$$\mathbf{\vec a} × \mathbf{\vec b} = -\mathbf{\vec b} × \mathbf{\vec a}$${{< /mathjax >}}   
{{< mathjax >}}$$(s * \mathbf{\vec a}) × \mathbf{\vec b} = s * (\mathbf{\vec a} × \mathbf{\vec b}) = \mathbf{\vec a} × (s * \mathbf{\vec b})$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × (\mathbf{\vec b} + \mathbf{\vec c}) = \mathbf{\vec a} × \mathbf{\vec b} + \mathbf{\vec a} × \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$(\mathbf{\vec a} + \mathbf{\vec b}) × \mathbf{\vec c} = \mathbf{\vec a} × \mathbf{\vec c} + \mathbf{\vec b} × \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} · (\mathbf{\vec b} × \mathbf{\vec c}) = (\mathbf{\vec a} × \mathbf{\vec b}) · \mathbf{\vec c}$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a} × (\mathbf{\vec b} × \mathbf{\vec c}) = (\mathbf{\vec a} · \mathbf{\vec c}) * \mathbf{\vec b} – (\mathbf{\vec a} · \mathbf{\vec b}) * \mathbf{\vec c}$${{< /mathjax >}}  

## 1.3 Vector equation of line

The vector line equation is used in 3D modeling applications and computer graphics.

<figure>
   <img src="/images/math-image187.png">
   <figcaption>Figure (16): Vector equation of a line.</figcaption>
</figure>  

For example, if we know the direction of a line and a point on that line, then we can find any other point on the line using vectors, as in the following:

{{< mathjax >}}$$\overline{L} = line$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec v} = <a, b, c>$${{< /mathjax >}} line direction unit vector  
{{< mathjax >}}$$Q = (x_0, y_0, z_0)$${{< /mathjax >}} line position point  
{{< mathjax >}}$$P = (x, y, z)$${{< /mathjax >}} any point on the line  

We know that:  

{{< mathjax >}}$$\mathbf{\vec a} = t *\mathbf{\vec v}$${{< /mathjax >}}   (2)  
{{< mathjax >}}$$\mathbf{\vec p} = \mathbf{\vec q} + \mathbf{\vec a}$${{< /mathjax >}}   (1)  

From 1 and 2:  

{{< mathjax >}}$$\mathbf{\vec p} = \mathbf{\vec q} + t * \mathbf{\vec v}$${{< /mathjax >}}  (3)   

However, we can write (3) as follows:  

{{< mathjax >}}$$<x, y, z> = <x_0, y_0, z_0> + <t * a, t * b, t * c>$${{< /mathjax >}}  
{{< mathjax >}}$$<x, y, z> = <x_0 + t * a, y_0 + t * b, z_0 + t * c>$${{< /mathjax >}}  

Therefore:  

{{< mathjax >}}$$x = x_0 + t * a$${{< /mathjax >}}  
{{< mathjax >}}$$y = y_0 + t * b$${{< /mathjax >}}  
{{< mathjax >}}$$z = z_0 + t * c$${{< /mathjax >}}  

Which is the same as:  

{{< mathjax >}}$$P = Q + t * \mathbf{\vec v}$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Given a point {{< mathjax >}}$$Q$${{< /mathjax >}} and a direction {{< mathjax >}}$$\vec v$${{< /mathjax >}} on a line, any point {{< mathjax >}}$$P$${{< /mathjax >}} on that line can be calculated using the vector equation of a line {{< mathjax >}}$$P = Q + t * \vec v$${{< /mathjax >}} where {{< mathjax >}}$$t$${{< /mathjax >}} is a number.  

{{< /call-out >}}

Another common example is to find the midpoint between two points. The following shows how to find the midpoint using the vector equation of a line:  

{{< mathjax >}}$$\mathbf{\vec q}$${{< /mathjax >}} is the position vector for point {{< mathjax >}}$$Q$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec p}$${{< /mathjax >}} is the position vector for point {{< mathjax >}}$$P$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec a}$${{< /mathjax >}} is the vector going from {{< mathjax >}}$$Q \rightarrow P$${{< /mathjax >}}  

From vector subtraction, we know that:  

{{< mathjax >}}$$\mathbf{\vec a} = \mathbf{\vec p} - \mathbf{\vec q}$${{< /mathjax >}}  

From the line equation, we know that:  

{{< mathjax >}}$$M = Q + t * \mathbf{\vec a}$${{< /mathjax >}}  

And since we need to find midpoint, then:  

{{< mathjax >}}$$t = 0.5$${{< /mathjax >}}  

Hence we can say:  

{{< mathjax >}}$$M = Q + 0.5 * \mathbf{\vec a}$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image159.png">
   <figcaption>Figure (17): Find the midpoint between two input points.</figcaption>
</figure>  

In general, you can find any point between {{< mathjax >}}$$Q$${{< /mathjax >}} and {{< mathjax >}}$$P$${{< /mathjax >}} by changing the {{< mathjax >}}$$t$${{< /mathjax >}} value between 0 and 1 using the general equation:  

{{< mathjax >}}$$M = Q + t * (P - Q)$${{< /mathjax >}}  

{{< call-out note "Note" >}}

Given two points {{< mathjax >}}$$Q$${{< /mathjax >}} and {{< mathjax >}}$$P$${{< /mathjax >}}, any point {{< mathjax >}}$$M$${{< /mathjax >}} between the two points is calculated using the equation {{< mathjax >}}$$M = Q + t * (P - Q)$${{< /mathjax >}} where t is a number between 0 and 1.

{{< /call-out >}}

## 1.4 Vector equation of a plane

One way to define a plane is when you have a point and a vector that is perpendicular to the plane. That vector is usually referred to as normal to the plane. The normal points in the direction above the plane.  

One example of how to calculate a plane normal is when we know three non-linear points on the plane.   

In Figure (16), given:  

{{< mathjax >}}$$A$${{< /mathjax >}} = the first point on the plane  
{{< mathjax >}}$$B$${{< /mathjax >}} = the second point on the plane  
{{< mathjax >}}$$C$${{< /mathjax >}} = the third point on the plane  

And:  

{{< mathjax >}}$$\mathbf{\vec a} $${{< /mathjax >}} = a position vector of point {{< mathjax >}}$$A$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b}$${{< /mathjax >}} = a position vector of point {{< mathjax >}}$$B$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec c}$${{< /mathjax >}} = a position vector of point {{< mathjax >}}$$C$${{< /mathjax >}}  

We can find the normal vector {{< mathjax >}}$$\mathbf{\vec n}$${{< /mathjax >}} as follows:  

{{< mathjax >}}$$\mathbf{\vec n} = (\mathbf{\vec b} - \mathbf{\vec a}) × (\mathbf{\vec c} - \mathbf{\vec a})$${{< /mathjax >}}  

<figure>
   <img src="/images/math-image160.png">
   <figcaption>Figure (18): Vectors and planes</figcaption>
</figure>  

We can also derive the scalar equation of the plane using the vector dot product:  

{{< mathjax >}}$$\mathbf{\vec n} · (\mathbf{\vec b} - \mathbf{\vec a}) = 0$${{< /mathjax >}}  

If:  

{{< mathjax >}}$$\mathbf{\vec n} = <a, b, c>$${{< /mathjax >}}  
{{< mathjax >}}$$\mathbf{\vec b} = <x, y, z>$${{< /mathjax >}}  
{{< mathjax >}}$$ \mathbf{\vec a} = <x_0, y_0, z_0>$${{< /mathjax >}}  

Then we can expand the above:  

{{< mathjax >}}$$<a, b, c> · <x-x_0, y-y_0, z-z_0 > = 0$${{< /mathjax >}}  

Solving the dot product gives the general scalar equation of a plane:  

{{< mathjax >}}$$a * (x - x_0) + b * (y - y_0) + c * (z - z_0) = 0$${{< /mathjax >}}  

## 1.5 Tutorials

All the concepts we reviewed in this chapter have a direct application to solving common geometry problems encountered when modeling. The following are stepbystep tutorials that use the concepts learned in this chapter using Rhinoceros and Grasshopper (GH).

### 1.5.1 Face direction
Given a point and a surface, how can we determine whether the point is facing the front or back side of that surface?  

**Input:**  

1. a surface  
2. a point  

<img src="/images/math-image161.png">  

**Parameters:**  

The face direction is defined by the surface normal direction. We will need the following information:  

* The surface normal direction at a surface location closest to the input point.  
* A vector direction from the closest point to the input point.  

Compare the above two directions, if going the same direction, the point is facing the front side, otherwise it is facing the back.  

**Solution:**  

1\. Find the closest point location on the surface relative to the input point using the Pull component. This will give us the uv location of the closest point, which we can then use to evaluate the surface and find its normal direction.  

<img src="/images/math-image162.png">  

2\. We can now use the closest point to draw a vector going towards the input point. We can also draw:  

<img src="/images/math-image163.png">  

3\. We can compare the two vectors using the dot product. If the result is positive, the point is in front of the surface. If the result is negative, the point is behind the surface.  

<img src="/images/math-image164.png">  

The above steps can also be solved using other scripting languages. Using the Grasshopper VB component:  

<img src="/images/math-image165.png">  

```vb
Private Sub RunScript(ByVal pt As Point3d, ByVal srf As Surface, ByRef A As Object)

  'Declare variables
  Dim u, v As Double
  Dim closest_pt As Point3d

  'get closest point u, v
  srf.ClosestPoint(pt, u, v)

  'get closest point
  closest_pt = srf.PointAt(u, v)

  'calculate direction from closest point to test point
  Dim dir As New Vector3d(pt - closest_pt)

  'calculate surface normal
  Dim normal = srf.NormalAt(u, v)

  'compare the two directions using the dot product
  A = dir * normal
End Sub
```

Using the Grasshopper Python component with RhinoScriptSyntax:

<img src="/images/math-image14.png">  

```python
import rhinoscriptsyntax as rs #import RhinoScript library

#find the closest point
u, v = rs.SurfaceClosestPoint(srf, pt)

#get closest point
closest_pt = rs.EvaluateSurface(srf, u, v)

#calculate direction from closest point to test point
dir = rs.PointCoordinates(pt) - closest_pt

#calculate surface normal
normal = rs.SurfaceNormal(srf, [u, v])

#compare the two directions using the dot product
A = dir * normal
```



Using the Grasshopper Python component with RhinoCommon only:

<img src="/images/math-image13.png">  

```python
#find the closest point
found, u, v = srf.ClosestPoint(pt)

if found:

    #get closest point
    closest_pt = srf.PointAt(u, v)

    #calculate direction from closest point to test point
    dir = pt - closest_pt

    #calculate surface normal
    normal = srf.NormalAt(u, v)

    #compare the two directions using the dot product
    A = dir * normal
```



Using the Grasshopper C# component:  

<img src="/images/math-image165.png">  

```cs
private void RunScript(Point3d pt, Surface srf, ref object A)
{
  //Declare variables
  double u, v;
  Point3d closest_pt;

  //get closest point u, v
  srf.ClosestPoint(pt, out u, out v);

  //get closest point
  closest_pt = srf.PointAt(u, v);

  //calculate direction from closest point to test point
  Vector3d dir = pt - closest_pt;

  //calculate surface normal
  Vector3d normal = srf.NormalAt(u, v);

  //compare the two directions using the dot product
  A = dir * normal;
}
```

### 1.5.2 Exploded box  

The following tutorial shows how to explode a polysurface. This is what the final exploded box looks like:   

<img src="/images/math-image15.jpg">  

**Input:**  

Identify the input, which is a box. We will use the Box parameter in GH:

<img src="/images/math-image17.jpg">  

**Parameters:**  

* Think of all the parameters we need to know in order to solve this tutorial.  
* The center of explosion.  
* The box faces we are exploding.  
* The direction in which each face is moving.   


<img src="/images/math-image19.jpg">  

Once we have identified the parameters, it is a matter of putting it together in a solution by piecing together the logical steps to reach an answer.

**Solution:**

1\. Find the center of the box using the **Box Properties** component in GH:

<img src="/images/math-image21.png">  

2\. Extract the box faces with the **Deconstruct Brep** component:

<img src="/images/math-image23.png">

3\. The direction we move the faces is the tricky part. We need to first find the center of each face, and then define the direction from the center of the box towards the center of each face as follows:

<img src="/images/math-image25.png">

4\. Once we have all the parameters scripted, we can use the **Move** component to move the faces in the appropriate direction. Just make sure to set the vectors to the desired amplitude, and you will be good to go.

<img src="/images/math-image27.png">

The above steps can also be solved using VB script, C# or Python. Following is the solution using these scripting languages.

Using the Grasshopper VB component:

<img src="/images/math-image29.png">

```vb
Private Sub RunScript(ByVal box As Brep, ByVal dis As Double, ByRef A As Object)

    'get the brep center
    Dim area As Rhino.Geometry.AreaMassProperties
    area = Rhino.Geometry.AreaMassProperties.Compute(box)

    Dim box_center As Point3d
    box_center = area.Centroid

    'get a list of faces
    Dim faces As Rhino.Geometry.Collections.BrepFaceList = box.Faces

    'decalre variables
    Dim center As Point3d
    Dim dir As Vector3d
    Dim exploded_faces As New List( Of Rhino.Geometry.Brep )
    Dim i As Int32
    'loop through all faces

    For i = 0 To faces.Count() - 1
      'extract each of the face
      Dim extracted_face As Rhino.Geometry.Brep = box.Faces.ExtractFace(i)

      'get the center of each face
      area = Rhino.Geometry.AreaMassProperties.Compute(extracted_face)
      center = area.Centroid

      'calculate move direction (from box centroid to face center)
      dir = center - box_center
      dir.Unitize()
      dir *= dis

      'move the extracted face
      extracted_face.Transform(Transform.Translation(dir))

      'add to exploded_faces list
      exploded_faces.Add(extracted_face)
    Next

    'assign exploded list of faces to output
    A = exploded_faces
  End Sub
```
Using the Grasshopper Python component with RhinoCommon:

<img src="/images/math-image4.png">

```python
import Rhino

#get the brep center
area = Rhino.Geometry.AreaMassProperties.Compute(box)
box_center = area.Centroid

#get a list of faces
faces = box.Faces

#decalre variables
exploded_faces = []

#loop through all faces
for i, face in enumerate(faces):

	#get a duplicate of the face
	extracted_face = faces.ExtractFace(i)
	
	#get the center of each face
	area = Rhino.Geometry.AreaMassProperties.Compute(extracted_face)
	center = area.Centroid
	
	#calculate move direction (from box centroid to face center)
	dir = center - box_center
	dir.Unitize()
	dir *= dis
	
	#move the extracted face
	move = Rhino.Geometry.Transform.Translation(dir)
	extracted_face.Transform(move)
	
	#add to exploded_faces list
	exploded_faces.append(extracted_face)

#assign exploded list of faces to output
A = exploded_faces
```

Using the Grasshopper C# component:

<img src="/images/math-image2.png">

```cs
private void RunScript(Brep box, double dis, ref object A)
{

    //get the brep center
  Rhino.Geometry.AreaMassProperties area =        Rhino.Geometry.AreaMassProperties.Compute(box);
  Point3d box_center = area.Centroid;

  //get a list of faces
  Rhino.Geometry.Collections.BrepFaceList faces = box.Faces;

  //decalre variables
  Point3d center;   Vector3d dir;
  List<Rhino.Geometry.Brep> exploded_faces = new List<Rhino.Geometry.Brep>();

  //loop through all faces   for( int i = 0; i < faces.Count(); i++ )
  {
    //extract each of the face
    Rhino.Geometry.Brep extracted_face = box.Faces.ExtractFace(i);

    //get the center of each face
    area = Rhino.Geometry.AreaMassProperties.Compute(extracted_face);
    center = area.Centroid;

    //calculate move direction (from box centroid to face center)
    dir = center - box_center;
    dir.Unitize();
    dir *= dis;

    //move the extracted face
    extracted_face.Transform(Transform.Translation(dir));

    //add to exploded_faces list
    exploded_faces.Add(extracted_face);
  }

  //assign exploded list of faces to output
  A = exploded_faces;
}
```

### 1.5.3 Tangent spheres

This tutorial will show how to create two tangent spheres between two input points.
This is what the result looks like:

<img src="/images/math-image5.png">

**Input:**  
Two points ({{< mathjax >}}$$A$${{< /mathjax >}} and {{< mathjax >}}$$B$${{< /mathjax >}}) in the 3-D coordinate system.

<img src="/images/math-image6.png">

Parameters:
The following is a diagram of the parameters that we will need in order to solve the problem:
{{< mathjax >}}$$A$${{< /mathjax >}} tangent point {{< mathjax >}}$$D$${{< /mathjax >}} between the two spheres, at some {{< mathjax >}}$$t$${{< /mathjax >}} parameter (0-1) between points {{< mathjax >}}$$A$${{< /mathjax >}} and {{< mathjax >}}$$B$${{< /mathjax >}}.

* The center of the first sphere or the midpoint {{< mathjax >}}$$C1$${{< /mathjax >}} between {{< mathjax >}}$$A$${{< /mathjax >}} and {{< mathjax >}}$$D$${{< /mathjax >}}.  
* The center of the second sphere or the midpoint {{< mathjax >}}$$C2$${{< /mathjax >}} between {{< mathjax >}}$$D$${{< /mathjax >}} and {{< mathjax >}}$$B$${{< /mathjax >}}.  
* The radius of the first sphere {{< mathjax >}}$$(r1)$${{< /mathjax >}} or the distance between {{< mathjax >}}$$A$${{< /mathjax >}} and {{< mathjax >}}$$C1$${{< /mathjax >}}.  
* The radius of the second sphere {{< mathjax >}}$$(r2)$${{< /mathjax >}} or the distance between {{< mathjax >}}$$D$${{< /mathjax >}} and {{< mathjax >}}$$C2$${{< /mathjax >}}.  

**Solution:**

1\. Use the **Expression** component to definepoint {{< mathjax >}}$$D$${{< /mathjax >}} between {{< mathjax >}}$$A$${{< /mathjax >}} and {{< mathjax >}}$$B$${{< /mathjax >}} atsome parameter {{< mathjax >}}$$t$${{< /mathjax >}}. The expression we will use is based onthe vector equation of a line:  

{{< mathjax >}}$$D = A + t*(B-A)$${{< /mathjax >}}  

{{< mathjax >}}$$B-A$${{< /mathjax >}} : is the vector that goes from {{< mathjax >}}$$B$${{< /mathjax >}} to {{< mathjax >}}$$A  (\vec{BA}) using the vector subtraction   operation.  

$${{< /mathjax >}}t*(B-A){{< mathjax >}}$$ : where $${{< /mathjax >}}t{{< mathjax >}}$$ is between 0 and 1 to get us a location on the vector.  

$${{< /mathjax >}}A+t*(B-A){{< mathjax >}}$$ : gets apoint on the vector between A and B.  

<img src="/images/math-image8.png">

2\. Use the Expression component to also define the mid points $${{< /mathjax >}}C1{{< mathjax >}}$$ and $${{< /mathjax >}}C2{{< mathjax >}}$$.  

<img src="/images/math-image9.png">  

3\. The first sphere radius $${{< /mathjax >}}(r1){{< mathjax >}}$$ and the second sphere radius $${{< /mathjax >}}(r2){{< mathjax >}}$$ can be calculated using the **Distance** component.  

<img src="/images/math-image10.png">  

4\. The final step involves creating the sphere from a base plane and radius. We need to make sure the origins are hooked to $${{< /mathjax >}}C1{{< mathjax >}}$$ and $${{< /mathjax >}}C2{{< mathjax >}}$$ and the radius from $${{< /mathjax >}}r1{{< mathjax >}}$$ and $${{< /mathjax >}}r2$$.  

<img src="/images/math-image54.png">  

**Using the Grasshopper VB component:**  

<img src="/images/math-image56.png">  

```vb
Private Sub RunScript(ByVal A As Point3d, ByVal B As Point3d, ByVal t As Double, ByRef S1 As Object, ByRef S2 As Object)

  'declare variables
  Dim D, C1, C2 As Rhino.Geometry.Point3d
  Dim r1, r2 As Double

  'find a point between A and B
  D = A + t * (B - A)

  'find mid point between A and D
  C1 = A + 0.5 * (D - A)

  'find mid point between D and B
  C2 = D + 0.5 * (B - D)
  'find spheres radius
  r1 = A.DistanceTo(C1)
  r2 = B.DistanceTo(C2)

  'create spheres and assign to output
  S1 = New Rhino.Geometry.Sphere(C1, r1)
  S2 = New Rhino.Geometry.Sphere(C2, r2)

End Sub
```

Using Python component:

<img src="/images/math-image62.png">

```python
import Rhino

#find a point between A and B
D = A + t * (B - A)

#find mid point between A and D
C1 = A + 0.5 * (D - A)

#find mid point between D and B
C2 = D + 0.5 * (B - D)

#find spheres radius
r1 = A.DistanceTo(C1)
r2 = B.DistanceTo(C2)

#create spheres and assign to output
S1 = Rhino.Geometry.Sphere(C1, r1)
S2 = Rhino.Geometry.Sphere(C2, r2)
```

Using the Grasshopper C# component:

<img src="/images/math-image58.png">

```cs
private void RunScript(Point3d A, Point3d B, double t, ref object S1, ref object S2)
{
  //declare variables
  Rhino.Geometry.Point3d D, C1, C2;
  double r1, r2;

  //find a point between A and B
  D = A + t * (B - A);

  //find mid point between A and D
  C1 = A + 0.5 * (D - A);

  //find mid point between D and B
  C2 = D + 0.5 * (B - D);

  //find spheres radius
  r1 = A.DistanceTo(C1);
  r2 = B.DistanceTo(C2);

  //create spheres and assign to output
  S1 = new Rhino.Geometry.Sphere(C1, r1);
  S2 = new Rhino.Geometry.Sphere(C2, r2);
}
```

## Download Sample Files

Download the [{{< awesome "fas fa-download">}} ](/files/math-samplesandtutorials.zip.zip) [math-samplesandtutorials.zip](/files/math-samplesandtutorials.zip) archive, containing all the example Grasshopper and code files in this guide.

## Next Steps

Now that you know vector math, check out the [Matrices and Transformations](/guides/general/essential-mathematics/matrices-transformations/) guide to learn more about the moving, rotating and scaling objects..

+++
aliases = [""]
authors = [ "rajaa" ]
categories = [ "Csharp Essentials" ]
category_page = "guides/grasshopper/csharp-essentials/"
keywords = [ "csharp", "commands" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Chapter 3: RhinoCommon Geometry"
type = "guides"
weight = 15
override_last_modified = "2024-04-15T14:59:06Z"
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 7
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"

+++

## 3.1: Overview

**RhinoCommon** is the **.NET SDK** for Rhino. It is used by Rhino plug-in developers to write **.NET** plug-ins for Rhino and Grasshopper. All Grasshopper scripting components can access **RhinoCommon** including all geometry objects and functions. For the whole namespace, see the **[RhinoCommon documentation](https://developer.rhino3d.com/api/RhinoCommon)**.

In this chapter, we will focus on the part of the **SDK** dealing with Rhino geometry.  We will show examples of how to create and manipulate geometry using the Grasshopper C# component.

The use of the geometry classes in the **SDK** requires basic knowledge in vector mathematics, transformations, and NURBS geometry. If you need to review or refresh your knowledge in these topics, then refer to the *[Essential Mathematics for Computational Design](https://www.rhino3d.com/download/rhino/6/essentialmathematics)*

If you recall from Chapter 2, we worked with value types such as **int** and **double**. Those are system built-in types provided by the programming language, **C#** in this case. We also learned that you can pass the value types to a function without changing the original variables (unless passed by reference using the **ref** keyword). We also learned that some types, such as **objects**, are always passed by reference. That means changes inside the function also changes the original value.

The system built-in types, whether they are value or reference types, are often very limiting in specialized programming applications. For example, in computer graphics, we commonly deal with points, lines, curves, or matrices. These types need to be defined by the **SDK** to ease the creation, storage, and manipulation of geometry data. Programming languages offer the ability to define new types using **structures** (value types) and **classes** (reference types). The **RhinoCommon SDK** defines many new types as we will see in this chapter.

## 3.2: Geometry Structures

**RhinoCommon** defines basic geometry types using structures. We will dissect the **Point3d** structure, show how to read in the documentation, and use it in a script. This should help you navigate and use other structures. Below is a list of the geometry structures:

<table class="rounded">
  <tr>
    <th>Structures</th>
    <th>Summary description</th>
  </tr>
  <tr>
    <td><b>Point3d</b></td>
    <td>Location in 3D space. There are other points that have different dimensions such as: Point2d (parameter space point) and Point4d to represent control points.</td>
  </tr>
  <tr>
    <td><b>Vector3d</b></td>
    <td>Vector in 3D space. There is also Vector2d for vectors in parameter space.</td>
  </tr>
  <tr>
    <td><b>Interval</b></td>
    <td>Domain. Has min and max numbers</td>
  </tr>
  <tr>
    <td><b>Line</b></td>
    <td>A line defined by two points (from-to)</td>
  </tr>
  <tr>
    <td><b>Plane</b></td>
    <td>A plane defined by a plane origin, X-Axis, Y-Axis, and Z-Axis</td>
  </tr>
 <tr>
    <td><b>Arc</b></td>
    <td>Represents the value of a plane, two angles, and a radius in a subcurve of a circle</td>
  </tr>
 <tr>
    <td><b>Circle</b></td>
    <td>Defined by a plane and radius</td>
  </tr>
 <tr>
    <td><b>Ellipse</b></td>
    <td>Defined by a plane and 2 radii</td>
  </tr>
 <tr>
    <td><b>Rectangle3d</b></td>
    <td>Represents the values of a plane and two intervals that form an oriented rectangle</td>
  </tr>
 <tr>
    <td><b>Cone</b></td>
    <td>Represents the center plane, radius, and height values in a right circular cone</td>
  </tr>
 <tr>
    <td><b>Cylinder</b></td>
    <td>Represents the values of a plane, a radius, and two heights--on top and beneath--that define a right circular cylinder</td>
  </tr>
 <tr>
    <td><b>BoundingBox</b></td>
    <td>Represents the value of two points in a bounding box defined by the two extreme corner points.This box is therefore aligned to the world X, Y, and Z axes</td>
  </tr>
 <tr>
    <td><b>Box</b></td>
    <td>Represents the value of a plane and three intervals in an orthogonal, oriented box that is not necessarily parallel to the world Y, X, Z axes</td>
  </tr>
 <tr>
    <td><b>Sphere</b></td>
    <td>Represents the plane and radius values of a sphere</td>
  </tr>
 <tr>
    <td><b>Torus</b></td>
    <td>Represents the value of a plane and two radii in a torus that is oriented in 3D space</td>
  </tr>
 <tr>
    <td><b>Transform</b></td>
    <td>4x4 matrix of numbers to represent geometric transformation</td>
  </tr>
</table>

### 3.2.1: The Point3d Structure

The **[Point3d](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Point3d.htm)** type includes three **fields** (X, Y, and Z). It defines a number of **properties** and also has **constructors** and **methods**. We will walk through all the different parts of **Point3d** and how it is listed in the **RhinoCommon** documentation. First, you can navigate to **Point3d** from the left menu under the **Rhino.Geometry** namespace. When you click on it, the full documentation appears on the right. At the very top, you will see the following:

<img src="point3d_api.png">

#### Here is a break down of what each part in the above **Point3d** documentation means:

<table class="rounded">
  <tr>
    <th>Part</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><b>Point3D</b> Structure Represents the ...</td>
    <td>Title and description</td>
  </tr>
  <tr>
    <td><b>Namespace: Rhino.Geometry</b></td>
    <td>The namespace that contains Point3d</td>
  </tr>
  <tr>
    <td><b>Assembly: RhinoCommon (in RhinoCommon.dll)</b></td>
    <td>The assembly that includes that type. All geometry types are part of the RhinoCommon.dll.</td>
  </tr>
  <tr>
    <td>/[SerializableAttribute/]</td>
    <td>Allow serializing the object</td>
  </tr>
  <tr>
    <td><b>public struct Point3d</b></td>
    <td>public: public access: your program can instantiate an object of that type</br>struct: structure value type.</br>Point3d: name of your structure</td>
  </tr>
 <tr>
    <td>: ISerializable,</br>
    IEquatable<Point3d>, </br>
    IComparable<Point3d>, </br>
    IComparable, </br>
    IEpsilonComparable<Point3d>
</td>
    <td>The “:” is used after the struct name to indicate what the struct implements.
Structures can implement any number of interfaces. An interface contains a common functionality that a structure or a class can implement. It helps with using consistent names to perform similar functionality across different types. For example, IEquatable interface has a method called “Equal”. If a structure implements IEquatable, it must define what it does (in Point3d, it compares all X, Y, and Z values and returns true or false).</td>
  </tr>
</table>

#### Point3d Constructors

Structures define constructors to instantiate the data. One of the **Point3d** constructors takes three numbers to initialize the values of X, Y, and Z. Here are all the constructors of the **Point3d** structure .

<img src="constructors.png">

The following example shows how to define a variable of type Point3d using a GH C# component.

<img src="point3d_gh.png">

```C#
private void RunScript(double x, double y, double z, ref object Point)
{
    // Create an instance of a point and initialize to x, y, and z
    Point3d pt = new Point3d(x, y, z);

    // Assign the point "pt" to output
    Point = pt;
}
```

#### Point3d Properties

Properties are mostly used to “get” and/or “set” the fields of the structure. For example, there are the “X”, “Y”, and “Z” properties to get & set the coordinates of an instance of **Point3d**. Properties can be **static** to get specific points, such as the origin of the coordinate system (0,0,0). The following are **Point3d** properties as they appear in the documentation:

<img src="properties.png">
 
Here are two GH examples to show how to get & set the coordinates of a **Point3d**. 

<img src="set_point3d.png">

```C#
private void RunScript(Point3d pt, ref object A, ref object B, ref object C)
{
    // Assign the point coordinates to output
    a = pt.X;
    b = pt.Y;
    c = pt.Z;
}
```
<img src="set_point_coordinate.png">

```C#
private void RunScript(double x, double y, double z, ref object Point)
{
    // Declare a new point
    Point3d newPoint = new Point3d(Point3d.Unset);

    // Set "new_pt" coordinates
    newPoint.X = x;
    newPoint.Y = y;
    newPoint.Z = z;

    // Assign the point coordinates to output
    Point = newPoint;
}
```
Static properties get or set a generic data of that type. The above example uses the static **Point3d** method **Unset** to unset the new point. Another example that is commonly used is the **origin** property in **Point3d** to get the origin of the coordinate system, which is (0,0,0) as in the following example.

<img src="get_origin_point.png">

```C#
private void RunScript( ref object Origin)
{
   Origin = Point3d.Origin;
}
```

#### Point3d Methods

The methods are used to help inquire about the data or perform specific calculations, comparisons, etc. For example, **Point3d** has a method to measure the distance to another point. All methods are listed in the documentation with full details about the parameters and the return value, and sometimes an example to show how they are used. In the documentation, **Parameters** refer to the input passed to the method and the **Return Value** describes the data returned to the caller. Notice that all methods can also be navigated through the left menu.

<img src="distance_to_point.png">

Here is how the **DistanceTo** method is used in an example.

<img src="distanceto_method.png">

```C#
private void RunScript( double x, double y, double z, Point3d other, ref object Point, ref object Distance)
{
    // Create an instance of a point and initialize to x, y, and z
    Point3d pt = new Point3d(x, y, z);
    // Calculate the distance from "pt" to the "other" input point
    double dis = pt.DistanceTo(other);
    // Assign the point "point" to the A output
    Point = pt;
    // Assign the distance to the B output
    Distance = dis;
}
```

The **DistanceTo** method does not change the fields (the X, Y, and Z). However, other methods such as **Transform** change the fields. The **Transform** method resets the X, Y, and Z values to reflect the new location after applying the transform.

<img src="transform_point_method.png">

Here is an example that uses **Point3d.Transform**.

<img src="point_transform_component.png">

```C#
private void RunScript(Point3d pt, Transform xform, ref object Point)
{
    // Create an instance of a point and initialize to input point
    Point3d newPoint = new Point3d(pt);
    // Transform the point
    newPoint.Transform(xform);
    // Assign the point "new_pt" to the A output
    Point = newPoint;
}
```
#### Point3d Static Methods

Point3d has **static** methods that are accessible without instantiating an instance of **Point3d**. For example, if you would like to check if a list of given instances of points are all coplanar, you can call the static method **Point3d.ArePointsCoplanar** without creating an instance of a point. Static methods have the little red “s” symbol in front of them in the documentation.

<img src="arepointcoplaner.png">

The **ArePointsCoplanar** has the following syntax, parameters, and the return value.

<img src="arepointscoplanar_method.png">

Here is an example that uses the static method **Point3d.ArePointsCoplanar**.

<img src="pointscoplaner_component.png">

```C#
private void RunScript(List<Point3d> pts, double tol, ref object IsCoplanar)
{
    // Test if the list of input points are coplanar
    bool coplanar = Point3d.ArePointsCoplanar(pts, tol);

    // Assign the co-planar test to output
    IsCoplanar = coplanar;
}
```
#### Point3d Operators

Many Structures & Classes in RhinoCommon implement operators whenever relevant. Operators enable you to use the “+” to add two points or use the “=” to assign the coordinates of one point to the other. **Point3d** structure implements many operators, and this simplifies the coding & its readability. Although it is fairly intuitive in most cases, you should check the documentation to verify which operators are implemented and what they return. For example, the documentation of adding 2 **Point3d** indicates the result is a new instance of **Point3d** where X, Y, and Z are calculated by adding corresponding fields of 2 input **Point3d**.

<img src="point3d_addition_operator.png">

Note that all operators are declared **public** and **static**. Here is an example that shows how the “+” operator in **Point3d** is used. Note that the “+” returns a new instance of a **Point3d**.

<img src="add_points_component.png">

```C#
private void RunScript(Point3d pt1, Point3d pt2, ref object Point)
{
    // Add 2 points and assign result to output
    Point = pt1 + pt2;
}
```
#### Point3d as a Function Parameter

**Point3d** is a value type because it is a structure. That means if you pass an instance of **Point3d** to a function and change its value inside that function, the original value outside the function will not be changed, as in the following example:

<img src="struct_point_pass.png">

```C#
private void RunScript(double x, double y, double z, Point3d pt2, ref object Point)
{
    Point3d pt = new Point3d(x, y, z);
    Print("Before calling ChangeX function: pt.x=" + pt.X);


    // Call a function to change the value of X in the point
    ChangeX(pt);

    Print("After ChangeX: pt.x=" + pt.X);
    Point = pt;
}
 public void ChangeX(Point3d pt) 
 {
    pt.X = 100;
    Print("Inside ChangeX: pt.x=" + pt.X);
  }
```
### 3.2.2: Points & Vectors

**RhinoCommon** has a few structures to store and manipulate points and vectors. Take for example the double precision points. There are three types of points that are commonly used listed in the table below. For more detailed explanation of vectors and points, please refer to the *[Essential Mathematics for Computational Design](https://www.rhino3d.com/download/rhino/6/essentialmathematics)*, a publication by McNeel.

<table class="rounded">
  <tr>
    <th>Class Name</th>
    <th>Member Variables</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><b>Point2d</b></td>
    <td>X as Double </br>Y as Double</td>
    <td>Used for parameter space points</td>
  </tr>
  <tr>
    <td><b>Point3d</b></td>
    <td>X as Double </br>Y as Double</td>
    <td>Most commonly used to represent points in three dimensional coordinate space</td>
  </tr>
  <tr>
    <td><b>Point4d</b></td>
    <td>X as Double </br>Y as Double </br>Z as Double </br>W as Double</td>
    <td>Used for grips or control points. Grips have weight information in addition to the 3D location.</td>
  </tr>
</table>

As for vectors, there are two main types:

<table class="rounded">
  <tr>
    <th>Class Name</th>
    <th>Member Variables</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><b>Vector2d</b></td>
    <td>X as Double </br>Y as Double</td>
    <td>Used in two dimensional space</td>
  </tr>
  <tr>
    <td><b>Vector3d</b></td>
    <td>X as Double </br>Y as Double </br>Z as Double</td>
    <td>Used in three dimensional space</td>
  </tr>
</table>

The following are a few point and vector operations with examples of output. The script starts with declaring and initializing a few values, then applying some operations:


<table class="multiline" width="100%">
<tr>
<th width="20%">Notation</th>
<th width="50%">Syntax</th>
<th>result</th>
</tr>
<tr>
<td>
Create a new instance of a point and vector
</td>
<td>

```C#
Point3d p0 = new Point3d(3, 6, 0);
Vector3d v0 = new Vector3d(4, 1.5, 0);
double factor = 0.5;
```

</td>
<td><img src="point_vector_instance.png" width="100%"></td>
</tr>
<tr>
<td>Move a point by a vector</td>
<td>

```C#
Point3d p1 = new Point3d(Point3d.Unset);
p1 = p0 + v0;
```

</td>
<td></td>
</tr>
<tr>
<td>
Distance between 2 points
</td>
<td>

```C#
double distance = p0.DistanceTo(p1);
```

</td>
<td></td>
</tr>
<tr>
<td>
Point subtraction (create vector between two points)
</td>
<td>

```C#
Vector3d v1 = new Vector3d(Vector3d.Unset);
v1 = Point3d.Origin - p0;
```

</td>
<td><img src="point_subtraction.png" width="100%"></td>
</tr>
<tr>
<td>
Vector addition (create average vector)
</td>
<td>

```C#
Vector3d addVectors = new Vector3d(Vector3d.Unset);
addVectors = v0 + v1;
```

</td>
<td><img src="vector_addition.png" width="100%"></td>
</tr>
<tr>
<td>
Vector subtraction
</td>
<td>

```C#
Vector3d subtractVectors = v0 - v1;
```

</td>
<td><img src="vector_subtraction.png" width="100%"></td>
</tr>
<tr>
<td>
Vector dot product (if result is positive number, then vectors are in the same direction)
</td>
<td>

```C#
double dot = v0 * v1;

/*---
For example if
v0 = <10, 0, 0>
v1 = <0, 10, 0>

then
dot = 0
*/
```

</td>
<td><img src="dot_product.png" width="100%"></td>
</tr>
<tr>
<td>
Vector cross product (result is a vector normal to the 2 input vectors)
</td>
<td>

```C#
Vector3d cross = new Vector3d(Vector3d.Unset);
cross = Vector3d.CrossProduct(v0, v1);
```

</td>
<td><img src="cross_product.png" width="100%"></td>
</tr>
<tr>
<td>
Scale a vector
</td>
<td>

```C#
Vector3d scaleV0 = new Vector3d(Vector3d.Unset);
scaleV0 = factor * v0;
```

</td>
<td><img src="scale_vector.png" width="100%"></td>
</tr>
<tr>
<td>
Get vector length
</td>
<td>

```C#
double v0Length = v0.Length;
```

</td>
<td></td>
</tr>
<tr>
<td>
Use vector operations to get the angle between 2 vectors
</td>
<td>

```C#
// Unitize the input vectors
v0.Unitize();
v1.Unitize();
double dot = v0 * v1;

// Force the dot product of the two input vectors to
// fall within the domain for inverse cosine, which
// is -1 <= x <= 1. This will prevent runtime
// "domain error" math exceptions.
if ((dot < -1.0))
    dot = -1.0;
if ((dot > 1.0))
    dot = 1.0;
double angle = System.Math.Acos(dot);
```

</td>
<td><img src="dot_product.png" width="100%">


```C#
v0 = <10, 0, 0>
v1 = <0, 10, 0>
dot = 0
angle = acos(0) = 90 degrees
```

</td>
</tr>
</table>

### 3.2.3: Lightweight Curves

**RhinoCommon** defines basic types of curves such as lines & circles as structures, and hence, most of them are value types. The mathematical representation is easier to understand and is typically more lightweight. If needed, it is relatively easy to get the NURBS approximation of these curves using the method **ToNurbsCurve**. The following is a list of the lightweight curves:


<table class="rounded">
  <tr>
    <th>Lightweight Curves Types </th>
    <th></th>
  </tr>
  <tr>
    <td><b>Line</b></td>
    <td>Line between two points</td>
  </tr>
  <tr>
    <td><b>Polyline</b></td>
    <td>Polyline connecting a list of points (not value type)</td>
  </tr>
  <tr>
    <td><b>Arc</b></td>
    <td>Arc on a plane from center, radius, start, and end angles</td>
  </tr>
  <tr>
    <td><b>Circle</b></td>
    <td>Circle on a plane from center point and radius</td>
  </tr>
  <tr>
    <td><b>Ellipse</b></td>
    <td>Defined by a plane and 2 radii</td>
  </tr>
 </table>

The following shows how to create instances of different lightweight curve objects:

<table class="multiline" width="100%">
<tr>
<th width="20%">Notation</th>
<th width="50%">Syntax</th>
<th>Result</th>
</tr>
<tr>
<td>
Declare and initialize 3 new Points
</td>
<td>

```C#
Point3d p0 = new Point3d(0, 0, 0);
Point3d p1 = new Point3d(5, 1, 0);
Point3d p2 = new Point3d(6, -3, 0);
```

</td>
<td></td>
</tr>
<tr>
<td>Create an instance of a Line</td>
<td>

```C#
// Create an instance of a lightweight Line
Line line = new Line(p0, p1);
```

</td>
<td><img src="simple_line.png" width="100%"></td>
</tr>
<tr>
<td>
Distance between 2 Points
</td>
<td>

```C#
double distance = p0.DistanceTo(p1);
```

</td>
<td></td>
</tr>
<tr>
<td>
Create an instance of a Arc 
</td>
<td>

```C#
// Create an instance of a lightweight Arc
Arc arc = new Arc(p0, p1, p2);
```

</td>
<td><img src="arc.png" width="100%"></td>
</tr>
<tr>
<td>
Create an instance of a Polyline
</td>
<td>

```C#
// Put the 3 Points in a list
Point3d[ ] pointList = {p0, p1, p2};

// Create an instance of a lightweight Polyline
Polyline polyline = new Polyline(pointList);
```

</td>
<td><img src="polyline.png" width="100%"></td>
</tr>
<tr>
<td>
Create an instance of a Circle
</td>
<td>

```C#
double radius = 3.5;

// Create an instance of a lightweight Circle
Circle circle = new Circle(p0, radius);
```

</td>
<td><img src="circle.png" width="100%"></td>
</tr>
<tr>
<td>
Create an list of instances of an Ellipse
</td>
<td>

```C#
double angle = 0.01; // angle in radian
int ellipseCount = 20; // number of ellipses
double x = 1.5; // shift along X-axis

// Declare a new list of ellipse curve type
List<Ellipse> ellipseListist = new List<Ellipse>();

// Use a loop to create a number of ellipse curves
Plane plane = Plane.WorldXY;

for (Int i = 1; i <= ellipseCount; i++) {
      Point3d pt = new Point3d(x, 0, 0);
      Vector3d y = new Vector3d(0,1,0);
      plane.Rotate(angle * i, y , pt);

      // Declare and instantiate a new ellipse
      Ellipse ellipse = new Ellipse(plane, (double) i / 2, i);

      // Add the ellipse to the list
      ellipseList.Add(ellipse);
    }
```

</td>
<td><img src="elipse.png" width="100%"></td>
</tr>
</table>

### 3.2.4: Lightweight Surfaces

Just like with curves, **RhinoCommon** defines a number of lightweight surfaces that are defined as structures. They can be converted to NURBS surfaces using the **ToNurbsSurface()** method. They include common surfaces such as cones & spheres. Here is a list of them:

<table class="rounded">
  <tr>
    <th>Lightweight Surface Types</th>
    <th></th>
  </tr>
  <tr>
    <td><b>Sphere</b></td>
    <td>Line between two points</td>
  </tr>
  <tr>
    <td><b>Cylinder</b></td>
    <td>Polyline connecting a list of points (not value type)</td>
  </tr>
  <tr>
    <td><b>Cone</b></td>
    <td>Arc on a plane from center, radius, start, and end angles</td>
  </tr>
  <tr>
    <td><b>Torus</b></td>
    <td>Circle on a plane from center point and radius</td>
  </tr>
 </table>

#### The following shows how to create instances of different lightweight surface objects:

<table class="multiline" width="100%">
<tr>
<th width="20%">Notation</th>
<th width="50%">Syntax</th>
<th>result</th>
</tr>
<tr>
<td>
Create an instance of a Sphere
</td>
<td>

```C#
Point3d center = Point3d.Origin;
double radius = 7.5;

Sphere sphere = new Sphere(center, radius);
```

</td>
<td><img src="sphere.png" width="100%"></td>
</tr>
<tr>
<td>
Create an instance of a Cylinder
</td>
<td>

```C#
double height = 7.5;
double radius = 2.5;
Point3d center = Point3d.Origin;
Circle baseCircle = new Circle(center, radius);

Cylinder cy = new Cylinder(baseCircle, height);
```

</td>
<td><img src="cylinder.png" width="100%"></td>
</tr>
<tr>
<td>
Create an instance of a Cone
</td>
<td>

```C#
double distance = p0.DistanceTo(p1);
```

</td>
<td></td>
</tr>
<tr>
<td>
Create an instance of a Arc
</td>
<td>

```C#
double height = 7.5;
double radius = 7.5;

Cone cone = new Cone(Plane.WorldXY, height, radius);
```

</td>
<td><img src="cone.png" width="100%"></td>
</tr>
<tr>
<td>
Create an instance of a Polyline
</td>
<td>

```C#
// Put the 3 Points in a list
Point3d[ ] pointList = {p0, p1, p2};

// Create an instance of a lightweight Polyline
Polyline polyline = new Polyline(pointList);
```

</td>
<td><img src="polyline.png" width="100%"></td>
</tr>
<tr>
<td>
Create an instance of a Torus
</td>
<td>

```C#
double minorRadius = 2.5;
double majorRadius = 7.5;

Torus torus = new Torus(Plane.WorldXY, majorRadius, minorRadius);
```

</td>
<td><img src="torus.png" width="100%"></td>
</tr>
</table>

### 3.2.5: Other Geometry Structures

Now that we have explained the **Point3d** structure in some depth, and some of the lightweight geometry structures, you should be able to review & use the rest using the **RhinoCommon** documentation. As a wrap up, the following example uses eight different structures defined in the **Rhino.Geometry** namespace. Those are **Plane**, **Point3d**, **Interval**, **Arc**, **Vector3d**, **Line**, **Sphere**, and **Cylinder**. The goal is to create the following composition:

<img src="geomtric_structures_gh.png" width="100%">

<img src="geometric_structures.png" width="100%">

#### Create an instance of a circle on the xy-plane, center (2,1,0), and a random radius between 10 and 20

```C#
    // Generate a random radius of a circle
    Random rand = new Random();
    double radius = rand.Next(10, 20);

    // Create xy_plane using Plane static method WorldXY
    Plane plane = Plane.WorldXY;

    // Set plane origin to (2,1,0)
    Point3d center = new Point3d(2, 1, 0);
    plane.Origin = center;

    // Create a circle from plane and radius
    Circle circle = new Circle(plane, radius);
```

#### Create an instance of an arc from the circle and angle interval between 0 and Pi

```C#
    // Create an arc from an input circle and interval
    Interval angleInterval = new Interval(0, Math.PI);

    Arc arc = new Arc(circle, angleInterval);
```

#### Extract the end points of the arc, and create a vertical lines with length = 10 units

```C#
    // Extract end points
    Point3d startPoint = arc.StartPoint;
    Point3d endPoint = arc.EndPoint;

    // Create a vertical vector
    Vector3d vec = Vector3d.ZAxis;
    // Use the multiplication operation to scale the vector by 10
    vec = vec * 10;

    // Create start & end lines
    Line line1 = new Line(startPoint, vec);
    Line line2 = new Line(endPoint, vec);
```
#### Create a cylinder around the start line with radius = line height/4, and crearte a sphere around the second line centered in the middle with radius = line height/4

```C#
    // Create a cylinder at line1 with radius = 1/4 the length
    double height = line1.Length;
    double radius = height / 4;
    Circle circle = new Circle(line1.From, radius);
    Cylinder cylinder = new Cylinder(c_circle, height);

    // Create a sphere at the center of line2 with radius = ¼ the length
    Point3d sphereCenter = line2.PointAt(0.5);
    Sphere sphere = new Sphere(sphereCenter, radius);
```

## 3.3: Geometry Classes

Just like structures, classes enable defining custom types by grouping other types together, along with some custom methods & events. A class is like a blueprint that encapsulates the data and the behavior of the user-defined type. But, unlike structures, classes allow **inheritance** which enables defining a hierarchy of types that starts with a generic type and branches into more specific types. For example, the **Curve** class in RhinoCommon branches into specialized curve types such as **ArcCurve** and **NurbsCurve**. The following diagram shows the hierarchy of the **Curve** class:

<img src="hierarchy.png" width="70%">

Most geometry classes are derived from the **GeometryBase** class. The following diagram shows the hierarchy of these classes:

<img src="geo_class_table.png" width="80%">

You can instantiate an instance of most of the classes above. However, there are some classes that you cannot instantiate. Those are usually higher in the hierarchy, such as the **GeometryBase**, **Curve**, and **Surface**. Those are called **abstract** classes.

* **Abstract Classes**: The **GeometryBase** in **RhinoCommon** is one example of an abstract class. You cannot create an object or instantiate an instance of an abstract class. The purpose is to define common data and functionality that all derived classes can share.
* **Base Classes**: refer to parent classes that define common functionality for the classes that are derived from them. The **Curve** class is an example of a base class that also happens to be an abstract (cannot instantiate an object from it). Base classes do not have to be abstract though.
<img src="base_class_error.png" width="80%">

```C#
private void RunScript(ref object A)
{
    // ERROR: attempt to create an instance of the abstract "Curve" class
    Rhino.Geometry.Curve crv = new Rhino.Geometry.Curve();
}
```

* **Derived Classes**: inherit the members of a class they are derived from and add their own specific functionality and implementation. The **NurbsCurve** is an example of a derived class from the **Curve** class. The **NurbsCurve** can use all members in **Curve** class methods. The same is true for all other classes derived from **Curve**, such as **ArcCurve** & **PolyCurve**. The following example shows how to create a new instance of the **PolylineCurve** class:
<img src="class_derived.png" width="80%">

```C#
private void RunScript(List<Point3d> pts, int degree, ref object Crv, ref object Type)
{
    // Declare & create a new instance of a polyline curve from points
    var crv = new Rhino.Geometry.PolylineCurve(pts);
    // Assign curve to A output
    Crv = crv;
    // Assign curve type to B output
    Type = crv.GetType();
}
```
The most common way to create an instance of a class is to use the new keyword when declaring the object:

<img src="new_linecurve.png" width="80%">

```C#
private void RunScript( Point3d p0, Point3d p1, ref object Line )
{
    // Create an instance of a point object & unset
    var lineCurve = new Rhino.Geometry.LineCurve(p0, p1);
    Print(lineCurve.ToString());
    Line = lineCurve
}
```

There is another common way to create instances of classes. That is to use special methods in some classes to help create and initialize a new instance of an object. For example, the **Curve** class has **static** methods to create a variety of curve types, as in the following example. Notice that you do not need to use **new** in this case:

<img src="new_nurbscrve.png" width="80%">

```C#
private void RunScript(List<Point3d> points, int degree, ref object A, ref object B)
{
    // Declare a curve variable
    Rhino.Geometry.Curve inter_crv = default(Rhino.Geometry.Curve);
    // Create new instance of a curve from interpolate points
    inter_crv = Rhino.Geometry.Curve.CreateInterpolatedCurve(points, degree);

    // Declare a curve variable
    Rhino.Geometry.Curve nurbs_crv = default(Rhino.Geometry.Curve);
    // Create new instance of a curve from control points
    nurbs_crv = Rhino.Geometry.Curve.CreateControlPointCurve(points, degree);

    // Assign output
    A = inter_crv;
    B = nurbs_crv;
}
```

The following sections summarize the different ways to create new instances of objects, which apply to both class & structure types:

#### Use the Class Constructor

Need to use the new keyword. For example, the following creates a line from two points:

```C#
Rhino.Geometry.LineCurve lc = new Rhino.Geometry.LineCurve(p0, p1);
```

Note that each class may have a number of constructors that include different sets of parameters. For example the **LineCurve** class has the following constructors:

<img src="class_constructor.png" width="100%">

Many times, there are “protected” constructors. Those are used internally by the class and you cannot use them to create a new instance of the object with them. They are basically locked. The LineCurve class has one marked in the image above.

#### Use the Class Static Create Methods

Some classes include a **Create** method to generate a new instance of the class. Here is an example:

```C#
Rhino.Geometry.NurbsCurve nc = NurbsCurve.Create(isPeriodic, degree, controlPoints);
```

You can find these methods in the **RhinoCommon** help when you navigate the class “members”. Here are different ways to create a **NurbsCurve** for example and how they appear in the help:

<img src="create_static.png" width="100%">

#### Use the Static Create Methods of the Parent Class

There are times when the parent class has “Create” methods that can be used to instantiate an instance of the derived class. For example, the Curve class has few static methods that a derived class like NurbsCurve can use as in the example:

```C#
Rhino.Geometry.Curve crv= Curve.CreateControlPointCurve(controlPoints, degree);
Rhino.Geometry.NurbsCurve nc = crv as Rhino.Geometry.NurbsCurve;
```

For the full set of the **Curve Create** methods, check the **RhinoCommon** documentation. Here is an example of a few of them:

#### Use the Return Value of a Function

<img src="return_value_function.png" width="100%">

Class methods return values and sometimes those are new instances of objects. For example, the Offset method in the Curve class returns a new array of curves that is the result of the offset.

```C#
Curve[ ] offsetCurves = x.Offset( Plane.WorldXY, 1.4, 0.01, CurveOffsetCornerStyle.None );
```

<img src="value_function_curves.png" width="100%">

Once you create an instance of a class or a structure, you will be able to see all class methods and properties through the auto-complete feature. When you start filling the method parameters, the auto-complete will show you which parameter you are at and its type. This is a great way to navigate all available methods for each class and be reminded of what parameters are needed. Here is an example from a **Point3d** structure. Note that you don’t always get access to all the methods via the auto-complete. For the complete list of properties, operations, and methods of each class, you should use the **RhinoCommon** help file.

<figure>
   <img src="auto_complete_help.png">
   <figcaption>Figure(23): Auto-complete help navigate the type methods</figcaption>
</figure> 

Classes and structures define properties to set & retrieve data. Each property has either a **Get** or a **Set** method, or both. The following example shows how to get and set the coordinates of a **Point3d** object:

<img src="get_set_variable.png" width="100%">

```C#
private void RunScript(double degree, ref object A)
{
    // Create an instance of a point object and initialize to origin (0,0,0)
    Point3d pt = new Point3d(0, 0, 0);
    // Get coordinates and print to "output"
    Print("X = " + pt.X);
    // Set the x coordinate to a new value from input
    pt.X = x;
    // Print the new x value
    Print("X = " + pt.X);
    // Get the pt "x" value and assign to output
    A = pt.X;
}
```

Copying data from an existing class to a new one can be done a few different ways depending on what the class supports. The following example shows how to copy data between two points using three different ways. It also shows how to use the **DuplicateCurve** method of the **Curve** class to create a new identical instance of a **Curve**:

<img src="duplicate_curve.png" width="100%">

```C#
private void RunScript(Point3d pt, Curve crv, ref object newCrv)
{
    // Different ways to copy data between objects
    // Use the constructor when you instantiate an instance Of the Point3d class
    Point3d newPt1 = new Point3d(pt);
    Print("new pt1 = " + newPt1.ToString());

    // Use the “= Operator” If the Class provides one
    Point3d newPt2 = new Point3d(Point3d.Unset);
    newPt2 = pt;
    Print("new pt2 = " + newPt2.ToString());

    // Copy the properties one by one
    Point3d newPt3 = new Point3d(Point3d.Unset);
    newPt3.X = pt.X;
    newPt3.Y = pt.Y;
    newPt3.Z = pt.Z;
    Print("new pt3 = " + newPt3.ToString());

    // Some geometry classes provide a “Duplicate” method that is very efficient to use
    newCrv = crv.DuplicateCurve();
}
```

### 3.3.1: Curves

The **RhinoCommon SDK** has the abstract **Rhino.Geometry.Curve** class that provides a rich set of functionality across all curves. There are many classes derived from the parent **Curve** class, and we will learn about how to create and manipulate them. The following is a list of the classes derived from the **Curve** class:

<table class="rounded">
  <tr>
    <th>Curve Types</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><b>ArcCurve</b></td>
    <td>Used to create arcs & circles</td>
  </tr>
  <tr>
    <td><b>LineCurve</b></td>
    <td>Used to create lines</td>
  </tr>
  <tr>
    <td><b>NurbsCurve</b></td>
    <td>Used to create freeform curves</td>
  </tr>
  <tr>
    <td><b>PolyCurves</b></td>
    <td>A curve that has multiple segments joined together</td>
  </tr>
  <tr>
    <td><b>PolylineCurve</b></td>
    <td>A curve that has multiple lines joined together</td>
  </tr>
  <tr>
    <td><b>CurveProxy</b></td>
    <td>Cannot instantiate an instance of it. Both BrepEdge & BrepTrim types are derived from the CurveProxy class.</td>
  </tr>
 </table>

#### Create Curve Objects

One way to create a curve object is to use the create methods available as **static** methods in the parent **Rhino.Geometry.Curve** class. Here is an example:

Create an instance of a **NurbsCurve** from control points and degree

```C#
Curve nc = Rhino.Geometry.Curve.CreateControlPointCurve(points, degree);
```

<img src="nurbscurve.png" width="50%">

Create an array of tween curves using two input curves and a the number of tween curves

```C#
// Declare a variable of type Curve
Curve[ ] tweenCurves = null;

// Create an array of tween curves
tweenCurves = Rhino.Geometry.Curve.CreateTweenCurves(curve0, curve1, count, 0.01);
```

<img src="tweencurves.png" width="50%">

Another way to create new curves is to use the constructor of the curve with the **new** keyword. The following are examples to create different types of curves using the constructor or the **Create** method in the class. You can reference the **RhinoCommon** help for more details about the constructors of each one of the derived curve classes.

The following example uses 3 new declared points:

```C#
Point3d p0 = new Point3d(0, 0, 0);
Point3d p1 = new Point3d(5, 1, 0);
Point3d p2 = new Point3d(6, -3, 0);
```

Create an instance of a **LineCurve** using the class constructor and **new** keyword:

```C#
// Create an instance of an LineCurve
LineCurve line = new LineCurve(p0, p1);
```

<img src="simple_line.png" width="50%">

Create an instance of a **ArcCurve** using the class constructor and **new** keyword:

```C#
// Create an instance of a lightweight Arc to pass to the 
// constructor of the ArcCurve class
Arc arc = new Arc(p0, p1, p2);

// Create a new instance of ArcCurve
ArcCurve arcCurve = new ArcCurve(arc);
```

<img src="arc.png" width="50%">

Create an instance of a **PolylineCurve** using the class constructor and **new** keyword

```C#
// Put the 3 points in a list
Point3d[ ] pointList = {p0, p1, p2};

// Create an instance of an PolylineCurve
PolylineCurve polyline = new PolylineCurve(pointList);
```

<img src="polyline.png" width="50%">

Create one open and one closed (periodic) curve using the **Create** function of the **NurbsCurve** class

```C#
bool isPeriodic = false;
int degree = 3;
NurbsCurve openCurve = NurbsCurve.Create(isPeriodic , degree, pointList);

isPeriodic = true;
NurbsCurve periodicCurve = NurbsCurve.Create(isPeriodic , degree, pointList);
```

<img src="periodic_curves.png" width="50%">

Curves can also be the return value of a method. For example, offsetting a given curve creates one or more new curves. Also the surface **IsoCurve** method returns an instance of a curve.

Extract isocurve from a surface. A new instance of a curve is the return value of a method:

```C#
// srf = input surface, t = input parameter
var uIso = srf.IsoCurve(0, t);
var vIso = srf.IsoCurve(1, t);
```

<img src="isocurve.png" width="50%">

Or, create multiple offsets of a curve:

```C#
private void RunScript(Curve crv, int num, double dis, double tol, Plane plane)
{
  // Declare the list of curve
  List<Curve> crvs = new List<Curve>();
  Curve lastCurve = crv;
  for (int i = 1; i <= num; i++) 
  {
    Curve[ ] curveArray = last_crv.Offset(plane, dis, tol, CurveOffsetCornerStyle.None);

    // Ignore if output is multiple offset curves
    if (crv.IsValid && curveArray.Count() == 1) {
      // Append offset curve to array
      crvs.Add(curveArray[0]);

      // Update the next curve to offset
      lastCUrve = curveArray[0];
    } 
    else 
        break;
  }
}
```

<img src="offset_curve.png" width="50%">

#### Curve Methods

Each class can define methods that help navigate the data of the class and extract some relevant information. For example, you might want to find the endpoints of a curve, find the tangent at some point, get a list of control points, or divide the curve. **AutoComplete** helps to quickly navigate and access these methods, but you can also find the full description in the **RhinoCommon** help.

Keep in mind that a derived class such as **NurbsCurve** can access not only its own methods but also the methods of the classes it was derived from. Therefore, an instance of a **NurbsCurve** can access the **NurbsCurve** methods and the **Curve** methods as well. The methods that are defined under the **Curve** are available to all of the classes derived from the **Curve** class, such as **LineCurve**, **ArcCurve**, **NurbsCurve**, etc. Here are a few examples of curve methods:


<table class="multiline" width="100%">
<tr>
<th width="60%">NurbsCurve methods</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
// Get the domain or interval of the curve
Interval domain = crv.Domain;
```

</td>
<td>
<img src="curve_domain.png" width="100%">
</td>
</tr>
<tr>
<td>

```C#
// Get the start & end points of a curve
Point3d startPoint = crv.PointAtStart;
Point3d endPoint = crv.PointAtEnd;
```

</td>
<td>
<img src="start_end_point.png" width="100%">
</td>
</tr>
<tr>
<td>

```C#
// Get the tangent at start of a curve
Vector3d startTangent = crv.TangentAtStart;
```

</td>
<td>
<img src="curve_tangent.png" width="100%">
</td>
</tr>
<tr>
<td>

```C#
// Get the control points of a NurbsCurve (nc)
List<Point3d> cpList = new List<Point3d>();
int count = nc.Points.Count;

// Loop to get all cv points
for (int i = 0; i <= count - 1; i++) {
    ControlPoint cp = nc.Points[i];
    cpList.Add(cp.Location);
}
```

</td>
<td>
<img src="curve_control_point.png" width="100%">
</td>
</tr>
<tr>
<td>

```C#
// Get the knot list of a NurbsCurve (nc)
List<double> knotList = new List<double>();
int count = nc.Points.Count;

// Loop to get all knots values
for (int i = 0; i <= count - 1; i++) {
    double knot = nc.Knots[i];
    knotList.Add(knot);
}
```

</td>
<td>
<img src="knots_list.png" width="100%">
</td>
</tr>
<tr>
<td>

```C#
// Divide curve (crv) by number (num)
// Declare an array of points
Point3d[ ] points = { };

// Divide the curve by number
crv.DivideByCount(num, true, out points);
```

</td>
<td>
<img src="kknots_curve.png" width="100%">
</td>
</tr>
</table>

### 3.3.2: Surfaces

There are many surface classes derived from the abstract **Rhino.Geometry.Surface** class. The **Surface** class provides common functionality among all of the derived types. The following is a list of the surface classes and a summary description:

<table class="rounded">
  <tr>
    <th>Surface Types</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><b>Extrusion</b></td>
    <td>Represents surfaces from extrusion. It is much lighter than a NurbsSurface.</td>
  </tr>
  <tr>
    <td><b>NurbsSurface</b></td>
    <td>Used to create free form surfaces</td>
  </tr>
  <tr>
    <td><b>PlaneSurface</b></td>
    <td>Used to create planar surfaces</td>
  </tr>
  <tr>
    <td><b>RevSurface</b></td>
    <td>Represents a surface of revolution</td>
  </tr>
  <tr>
    <td><b>SumSurface</b></td>
    <td>Represents a sum surface or an extrusion of a curve along a curved path</td>
  </tr>
  <tr>
    <td><b>SurfaceProxy</b></td>
    <td>Cannot instantiate an instance of it. Provides a base class to brep faces and other surface proxies</td>
  </tr>
 </table>

#### Create Surface Objects

One way to create surfaces is by using the static methods in the **Rhino.Geometry.Surface** class that start with the keyword **Create**. Here are some of these create methods:

<table class="rounded">
  <tr>
    <th colspan="2">Create methods in Rhino.Geometry.Surface class</th>
    <th></th>
  </tr>
  <tr>
    <td><b>CreateExtrusion</b></td>
    <td>Constructs a surface by extruding a curve along a vector</td>
  </tr>
  <tr>
    <td><b>CreateExtrusionToPoint</b></td>
    <td>Constructs a surface by extruding a curve to a point</td>
  </tr>
  <tr>
    <td><b>CreatePeriodicSurface</b></td>
    <td>Constructs a periodic surface from a base surface & a direction</td>
  </tr>
  <tr>
    <td><b>CreateRollingBallFillet</b></td>
    <td>Constructs a rolling ball fillet between two surfaces</td>
  </tr>
  <tr>
    <td><b>CreateSoftEditSurface</b></td>
    <td>Creates a soft-edited surface from an existing surface using a smooth field of influence</td>
  </tr>
 </table>

The following example creates a fillet surfaces between 2 input surfaces given some radius & tolerance:

<img src="fillet_surface.png"  class="float_right" width="225">

```C#
private void RunScript(Surface srfA, Surface srfB, double radius, double tol, ref object A)
{
    // Declare an array of surfaces
    Surface[ ] surfaces = {};

    // Check for a valid input
    if (srfA != null && srfB != null) {
        // Create fillet surfaces
        surfaces = Surface.CreateRollingBallFillet(srfA, srfB, radius, tol);
      }
  }
```
However, the most common way to create a new instance of a derived surface type is to either use the constructor (with **new** keyword) or the **Create** method of the derived surface class. Here are a couple of examples that show how to create instances from different surface types:


<table class="multiline" width="100%">
<tr>
<th width="60%">NurbsCurve methods</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
// Get the domain or interval of the curve
Interval domain = crv.Domain;
```

</td>
<td>
<img src="curve_domain.png" width="50%">
</td>
</tr>
<tr>
<td>

```C#
// Get the start & end points of a curve
Point3d startPoint = crv.PointAtStart;
Point3d endPoint = crv.PointAtEnd;
```

</td>
<td>
<img src="start_end_point.png" width="80%">
</td>
</tr>
<tr>
<td>

```C#
// Get the tangent at the start of a curve
Vector3d startTangent = crv.TangentAtStart;
```

</td>
<td>
<img src="curve_tangent.png" width="80%">
</td>
</tr>
<tr>
<td>

```C#
// Get the control points of a NurbsCurve (nc)
List<Point3d> cpList = new List<Point3d>();
int count = nc.Points.Count;

// Loop to get all cv points
for (int i = 0; i <= count - 1; i++) {
    ControlPoint cp = nc.Points[i];
    cpList.Add(cp.Location);
}
```

</td>
<td>
<img src="curve_control_point.png" width="80%">
</td>
</tr>
<tr>
<td>

```C#
// Get the knot list of a NurbsCurve (nc)
List<double> knotList = new List<double>();
int count = nc.Points.Count;

// Loop to get all knots values
for (int i = 0; i <= count - 1; i++) {
    double knot = nc.Knots[i];
    knotList.Add(knot);
}
```

</td>
<td>
<img src="knots_list.png" width="50%">
</td>
</tr>
<tr>
<td>

```C#
// Divide curve (crv) by number (num)
// Declare an array of points
Point3d[ ] points = { };

// Divide the curve by number
crv.DivideByCount(num, true, out points);
```

</td>
<td>
<img src="knots_curve.png" width="80%">
</td>
</tr>
</table>

<table class="multiline" width="100%">
<tr>
<th width="20%">Notation</th>
<th width="50%">Syntax</th>
<th>result</th>
</tr>
<tr>
<td>
Create an instance of a **PlaneSurface** using the constructor & **new** keyword
</td>
<td>

```C#
var plane = Plane.WorldXY;
var x_interval = new Interval(1.0, 3.5);
var y_interval = new Interval(2.0, 6.0);

// Create planar surface
var planeSrf = new PlaneSurface(plane, x_interval, y_interval);
```

</td>
<td><img src="planesurface.png" width="100%"></td>
</tr>
<tr>
<td>
Create an instance of a **RevSurface** from a line & a profile curve
</td>
<td>

```C#
RevCurve revCrv = … // from input
Line revAxis = … // from input

// Create surface of revolution
var revSrf = RevSurface.Create(revCrv, revAxis);
```

</td>
<td><img src="revsurface.png" width="100%"></td>
</tr>
<tr>
<td>
Create an instance of a **NurbsSurface** from a list of control points
</td>
<td>

```C#
List<Point3d> points = … // from input

// Create nurbs surface from control points
NurbsSurface ns = null;
ns = NurbsSurface.CreateThroughPoints(points, 2, 2, 1, 1, false, false);
```

</td>
<td><img src="nurbsurface_new.png" width="100%"></td>
</tr>
<tr>
<td>
Create an instance of a **NurbsSurface** from extruding a curve in certain direction 
</td>
<td>

```C#
Curve cv = … // from input
Vector3d dir = … // from input

// Create a nurbs surface from extruding a curve in some dir
var nSrf = NurbsSurface.CreateExtrusion(crv, dir);
// Create an extrusion from extruding a curve in some dir
var ex = Extrusion.Create(crv, 10, false);

// Note that in Grasshopper 1.0 there is no support for extrusion objects, and hence, the output within GH is converted to a NURBS surface. The only way to bake an Extrusion instance is to add the object to the active document from within the scripting component, as in the following:
Rhino.RhinoDoc.ActiveDoc.Objects.AddExtrusion(ex);
```

</td>
<td><img src="extrude_surface.png" width="100%"></td>
</tr>
</table>

#### Surface Methods

Surface methods help edit & extract information about the surface object. For example, you might want to learn if the surface is closed or if it is planar. You might need to evaluate the surface at some parameter to calculate points on the surface or get its bounding box. There are also methods to extract a lightweight geometry out of the surface. They start with the “Try” keyword. For example, you might have a RevSurface that is actually a portion of a torus. In that case, you can call TryGetTorus. All these methods and many more can be accessed through the surface methods. A full list of these methods is documented in the **RhinoCommon SDK** documentation.

<table class="multiline" width="100%">
<tr>
<th width="60%">Examples of the **Surface** & **NurbsSurface** methods</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
Surface srf = … // from input
// Check if the input surface is closed in the u or v direction
bool isClosedU = srf.IsClosed(0);
bool isClosedV = srf.IsClosed(1);

// Check if the surface is planar at zero tolerance
bool isPlanar = srf.IsPlanar();
```

</td>
<td>
<img src="surface_simple.png" width="100%">
</td>
</tr>
<tr>
<td>

```C#
Surface srf = … // from input
double u = 0.5;
double v = 0.5;
// Declare & instantiate the evaluation point and derivative vectors
Point3d evalPt = new Point3d(Point3d.Unset);
Vector3d[ ] derivatives = {};

// Evaluate the surface and extract the first derivative to get tangents
srf.Evaluate(u, v, 1, out evalPt, out derivatives);

Vector3d tanU = derivatives[0];
Vector3d tanV = derivatives[1];
```

</td>
<td>
<img src="surface_derivative.png" width="100%">
</td>
</tr>
<tr>
<td>

```C#
// Declare the list of surfaces
List<Surface> srfs = new List<Surface>();

Surface lastSrf = srf;
for (int i = 1; i <= num; i++) {t
    Surface offset_srf = last_srf.Offset(dis, tol);
    if (srf.IsValid) {
        // append offset surface to array
        srfs.Add(offset_srf);
        // update the next curve to offset
        lastSrf = offset_srf;
    } 
    else 
        break;
}
```

</td>
<td>
<img src="surface_list.png" width="100%">
</td>
</tr>
<tr>
<td>

```C#
// Declare & instantiate an axis and a curve
Line axis = new Line (Point3d.Origin, new Point3d(0, 0, 10));
LineCurve crv = new LineCurve(new Point3d(2, 0, 0), new Point3d(3.5, 0, 5));

// Create surface of revolution
RevSurface revSrf = RevSurface.Create(crv, axis);

// Try to get a Cone
Cone cone;
if( revSrf.TryGetCone(out cone))
    Print(“Cone was successfully create from surface”);
```

</td>
<td>
<img src="cone_surface.png" width="100%">
</td>
</tr>
</table>

### 3.3.3: Meshes

Meshes represent a geometry class that is defined by faces & vertices. The mesh data structure basically includes a list of vertex locations, faces that describe vertices connections, and normal of vertices & faces. More specifically, the geometry lists of a mesh class include the following:

<table class="rounded">
  <tr>
    <th>Mesh geometry</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><b>Vertices</b></td>
    <td>Of type MeshVertexList - includes a list of vertex locations type Point3f</td>
  </tr>
  <tr>
    <td><b>Normals</b></td>
    <td>Of type MeshVertexNormalList - includes a list of normals of type Vector3f</td>
  </tr>
  <tr>
    <td><b>Faces</b></td>
    <td>Of type MeshFaceList - includes a list of normals of type MeshFace</td>
  </tr>
  <tr>
    <td><b>FaceNormals</b></td>
    <td>Of type “MeshFaceNormalList” - includes a list of normals of type Vector3f</td>
  </tr>
 </table>

#### Create Surface Objects

You can create a mesh from scratch by specifying vertex locations & faces and compute the normal as in the following examples:

<table class="multiline" width="100%">
<tr>
<th width="60%">Examples of the **Mesh** methods</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
// Create a simple rectangular mesh that has 1 face
// Create a new instance of a mesh
Rhino.Geometry.Mesh mesh = new Rhino.Geometry.Mesh();

// Add mesh vertices
mesh.Vertices.Add(0.0, 0.0, 0.0); // 0
mesh.Vertices.Add(5.0, 0.0, 0.0); // 1
mesh.Vertices.Add(5.0, 5.0, 0.0); // 2
mesh.Vertices.Add(0.0, 5.0, 0.0); // 3

// Add mesh faces
mesh.Faces.AddFace(0, 1, 2, 3);

// Compute mesh normals
mesh.Normals.ComputeNormals();

// Generate any additional mesh data
mesh.Compact();
```

</td>
<td>
<img src="mesh_face.png" width="100%">
</td>
</tr>
<tr>
<td>

```C#
// Create simple triangular mesh that has 2 faces
// Create a new instance of a mesh
Rhino.Geometry.Mesh mesh = new Rhino.Geometry.Mesh();

// Add mesh vertices
mesh.Vertices.Add(0.0, 0.0, 0.0); // 0
mesh.Vertices.Add(5.0, 0.0, 2.0); // 1
mesh.Vertices.Add(5.0, 5.0, 0.0); // 2
mesh.Vertices.Add(0.0, 5.0, 2.0); // 3

// Add mesh faces
mesh.Faces.AddFace(0, 1, 2);
mesh.Faces.AddFace(0, 2, 3);

// Compute mesh normals
mesh.Normals.ComputeNormals();

// Generate any additional mesh data
mesh.Compact();
```

</td>
<td>
<img src="mesh_faces.png" width="100%">
</td>
</tr>
</table>

The Mesh class includes many **CreateFrom** static methods to create a new mesh from various other geometry. Here is the list with description as it appears in the **RhinoCommon** help:

<img src="mesh_api.png" width="100%">

Here are a couple examples to show how to create a mesh from a brep & a closed polyline:

<table class="multiline" width="100%">
<tr>
<th width="60%">**Mesh** Samples</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
// Set mesh parameters to default
var mp = MeshingParameters.Default;

// Create meshes from brep
var newMesh = Mesh.CreateFromBrep(brep, mp);
```

</td>
<td>
<img src="mesh_revolve.png" width="100%">
</td>
</tr>
<tr>
<td>

```C#
// Create a new mesh from polyline
var newMesh = Mesh.CreateFromClosedPolyline(pline);
```

</td>
<td>
<img src="mesh_closedpoly.png" width="100%">
</td>
</tr>
</table>

#### Navigate Mesh Geometry & Topology

You can navigate mesh data using **Vertices** & **Faces** properties. The list of vertices & faces are stored in a collection class or type with added functionality to manage the list efficiently. **Vertices** list, for example, is of type **MeshVertexList**. So if you need to change the locations of mesh vertices, then you need to get a copy of each vertex, change the coordinates, then reassign in the vertices list. You can also use the Set methods inside the MeshVertexList class to change vertex locations. 

The following example shows how to randomly change the **Z** coordinate of a mesh using two different approaches. Notice that mesh vertices use a **Point3f** and not **Point3d** type because mesh vertex locations are stored as a single precision floating point.

<table class="multiline" width="100%">
<tr>
<th width="60%">Change the location of mesh vertices by assigning the new value to the Vertices’ list</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
// Change mesh vertex location
int index = 0;
Random rand = new Random();

foreach (Point3f loc in mesh.Vertices) {
    Point3f newLoc = loc;
    newLoc.Z = rand.Next(10) / 3;
    mesh.Vertices[index] = newLoc;
    index = index + 1;
}
```

</td>
<td>
<img src="mesh_random_verts.png" width="100%">
</td>
</tr>
</table>

<table class="multiline" width="100%">
<tr>
<th width="60%">Change the location of mesh vertices using the **SetVertix** method</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
Mesh mesh = … // from input

// Create a new instance of random generator
Random rand = new Random();
for (int i = 0; i <= mesh.Vertices.Count - 1; i++){
    // Get vertex
    Point3f loc = mesh.Vertices[i];
    loc.Z = rand.Next(10) / 3;
    // Assign new location
    mesh.Vertices.SetVertex(i, loc);
}
```

</td>
<td>
<img src="mesh_setvert.png" width="100%">
</td>
</tr>
</table>

Here is an example that deletes a mesh vertex and all surrounding faces:

<table class="multiline" width="100%">
<tr>
<th width="60%">Delete mesh faces randomly</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
Mesh mesh = … // from input
int index = 32;
// Remove a mesh vertex (make sure index falls within range)
if (index >= 0 & i < mesh.Vertices.Count)
{
    mesh.Vertices.Remove(index, true);
}
```

</td>
<td>
<img src="mesh_delete_face.png" width="100%">
</td>
</tr>
</table>

You can also manage the **Faces** list of a mesh. Here is an example that deletes about half the faces randomly from a given mesh:

<table class="multiline" width="100%">
<tr>
<th width="60%">Delete mesh faces randomly</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
List<int> faceIndices = new List<int>();
int count = mesh.Faces.Count;

// Create a new instance of random generator
Random rand = new Random();

for (int i = 0; i <= count - 1; i += 2){
      int index = rand.Next(count);
      faceIndices.Add(index);
}

// Delete faces
mesh.Faces.DeleteFaces(distinctIndices);
```

</td>
<td>
<img src="mesh_rand_face.png" width="100%">
</td>
</tr>
</table>

Meshes keep track of the connectivity of the different parts of the mesh. If you need to navigate related faces, edges, or vertices, then this is done using the mesh topology. The following example shows how to extract the outline of a mesh using the mesh topology:

<table class="multiline" width="100%">
<tr>
<th width="60%">Mesh topology example: extract the outline of a mesh</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
// Get the mesh's topology
Rhino.Geometry.Collections.MeshTopologyEdgeList meshEdges = mesh.TopologyEdges;

List<Line> lines = new List<Line>();

// Find all of the mesh edges that have only a single mesh face
for (int i = 0; i <= meshEdges.Count - 1; i++) {
    int numOfFaces = meshEdges.GetConnectedFaces(i).Length;

    if ((numOfFaces  == 1)) {
        Line line = meshEdges.EdgeLine(i);
        lines.Add(line);
    }
}
```

</td>
<td>
<img src="mesh_outline.png" width="100%">
</td>
</tr>
</table>

#### Mesh Methods

Once a new mesh object is created, you can edit & extract data out of that mesh object. The following example extracts naked edges out of some input mesh:

<table class="multiline" width="100%">
<tr>
<th width="60%">Extract the outline of a mesh</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
Mesh mesh = … // from input

// Declare an array of polylines
Polyline[ ] naked_edges = { };

// Create a new mesh from polyline
nakedEdges = mesh.GetNakedEdges();
```

</td>
<td>
<img src="mesh_naked_edges.png" width="100%">
</td>
</tr>
</table>

<table class="multiline" width="100%">
<tr>
<th width="60%">Test if a given point is inside a closed mesh</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
Mesh mesh = … // from input
Point3d pt = … // from input

// Test if the point is inside the mesh
mesh.IsPointInside(pt, tolerance, true);
```

</td>
<td>
<img src="mesh_sphere.png" width="100%">
</td>
</tr>
</table>

<table class="multiline" width="100%">
<tr>
<th width="60%">Delete every other mesh face, then split disjoint meshes</th>
<th width="40%"></th>
</tr>
<tr>
<td>

```C#
Mesh mesh = … // from input
List<int> faceIndeces = new List<int>();

// Loop through faces & delete every other face
for (int i = 0; i <= mesh.Faces.Count - 1; i += 2) {
      faceIndeces.Add(i);
}
// Delete faces
mesh.Faces.DeleteFaces(faceIndeces);
// Split disjoint meshes
Mesh[ ] meshArray = mesh.SplitDisjointPieces();
```

</td>
<td>
<img src="mesh_array.png" width="100%">
</td>
</tr>
</table>

### 3.3.4: Boundary Representation (Brep)

The boundary representation is used to unambiguously represent trimmed nurbs surfaces and polysurfaces. There are two sets of data that are needed to fully describe the 3D objects using the boundary representation. Those are geometry & topology.

#### Brep Geometry

Three geometry elements are used to create any Breps:
1. The 3D untrimmed nurbs surfaces in the modeling space
2. The 3D curves, which are the geometry of edges in modeling space
3. The 2D curves, which are the geometry of trims in the parameter space


<figure>
   <img src="brep_levels.png">
   <figcaption>Figure(24): Geometry elements of a typical trimmed nurbs surface. 
(1) Trimmed surface with control points turned on (2) Underlying 3-D untrimmed surface (3) 3D curves (for the edges) in modeling space (4) 2D curves (for the trims) in parameter space</figcaption>
</figure> 

#### Brep Topology

A topology refers to how different parts of the 3D object are connected. For example, we might have two adjacent faces with one of their edges aligned. There are two possibilities to describe the relationship or connectivity between these two faces. They could either be two separate entities that can be pulled apart, or they are joined in one object sharing that edge. The topology is the part that describes such relationships.

<figure>
   <img src="mesh_connect.png">
   <figcaption>Figure(25): Topology describes connectivity between geometry elements. Two adjacent faces can either be joined together in one polysurface or are two separate faces that can be pulled apart.</figcaption>
</figure> 

Brep topology includes faces, edges, vertices, trims, and loops. The following diagram lists the Brep topology elements and their relation to geometry in the context of **RhinoCommon**:

<figure>
   <img src="brep_topology.png">
   <figcaption>Figure(26): The Brep topology elements and their relation to geometry</figcaption>
</figure> 

The topology elements of the Brep can be defined as follows:

<table class="rounded">
  <tr>
    <th>Topology</th>
    <th>Referenced Geometry</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><b>Vertices</b></td>
    <td>3D points </br>(location in 3D space)</td>
    <td>They describe the corners of the brep. Each vertex has a 3D location. They are located at the ends of edges and are shared between neighboring edges.</td>
  </tr>
  <tr>
    <td><b>Edges</b></td>
    <td>3D Nurbs curves </br>(location in 3D space)</td>
    <td>Edges describe the bounds of the brep. Each references the 3D curve, two end vertices, and the list of trims. If an edge has more than one trim, that means the edge is shared among more than one face. Multiple edges can reference the same 3D curve (typically a different portion of it).</td>
  </tr>
  <tr>
    <td><b>Faces</b></td>
    <td>3D underlying NURBS surfaces</br>(location in 3D space)</td>
    <td>Faces reference the 3D surface and at least one outer loop. A face normal direction might not be the same as that of the underlying surface normal. Multiple faces can reference the same 3D surface (typically a different portion of it).</td>
  </tr>
  <tr>
    <td><b>Loops</b></td>
    <td>2D closed curves of connected trims </br>(in 2D parameter space)</td>
    <td>Each face has exactly one outer loop defining the outer boundary of the face. A face can also have inner loops (holes). Each loop contains a list of trims.</td>
  </tr>
  <tr>
    <td><b>Trims</b></td>
    <td>2D Curves </br>(in 2D parameter space)</td>
    <td>Each trim references one 2D curve & exactly one edge, except in singular trims, there is no edge. The 2D curves of the trims run in a consistent direction. Trims of outer or boundary of the face run counter-clockwise regardless of the 3D curve direction of its edge. The 2D curves of the trims of the inner loops run clockwise.</td>
  </tr>
</table>

Each brep includes lists of geometry & topology elements. Topology elements point to each other and the geometry they reference, which makes it easy to navigate through the brep data structure. The following diagram shows navigation paths of the brep topology & geometry elements:

<figure>
   <img src="brep_navigate.png">
   <figcaption>Figure(27): Navigation diagram of the Brep data structure in RhinoCommon.</figcaption>
</figure> 

The topology of the Brep and navigating different parts:

<img src="fillet_surface.png"  class="float_right" width="225">

```C#
Brep brep = … // from input
// BrepFace topology (3D modeling space)
Rhino.Geometry.Collections.BrepFaceList faces = brep.Faces;
for(int fi = 0; fi < faces.Count; fi++)
    {
      BrepFace face = faces[fi];
      // Get Adjacent faces
      var aFaces = face.AdjacentFaces();
      // Get Adjacent edges
      var aEdges = face.AdjacentEdges();
      // Get face loops
      var faceLoops = face.Loops;
      // Get the 3D untrimmed surface
      var face3dSurface = face.UnderlyingSurface();
}

// BrepLoop topology (2D parameter space)
Rhino.Geometry.Collections.BrepLoopList loops = brep.Loops;
for(int li = 0; li < loops.Count; li++)
{
      BrepLoop loop = loops[li];
      // Get loop face
      var loopFace = loop.Face;
      // Get loop trims
      var loopTrims = loop.Trims;
      // Get loop 2D & 3D curves
      var loop2dCurve = loop.To2dCurve();
      var loop3dCurve = loop.To3dCurve();
}

// BrepEdge topology (3D modeling space)
Rhino.Geometry.Collections.BrepEdgeList edges = brep.Edges;
for(int ei = 0; ei < edges.Count; ei++)
{
      BrepEdge edge = edges[ei];
      // Get edge faces
      var eFaces_i = edge.AdjacentFaces();
      // Get edge start & end vertices
      var eStartVertex = edge.StartVertex;
      var eEndVertex = edge.EndVertex;
      // Get edge trim indices
      var eTrimIndeces = edge.TrimIndices();
      // Get edge 3D curve
      var e3dCurve = edge.EdgeCurve;
}

// BrepTrim topology (2D parameter space)
Rhino.Geometry.Collections.BrepTrimList trims = brep.Trims;
for(int ti = 0; ti < trims.Count; ti++)
{
      BrepTrim trim = trims[ti];
      // Get the edge
      var trimEdge = trim.Edge;
      // Get trim start & end vertices
      var trimStartVertex = trim.StartVertex;
      var trimEndVertex = trim.EndVertex;
      // Get trim loop
      var trimLoop = trim.Loop;
      // Get trim face
      var trimFace = trim.Face;
      // Get trim 2D curve
      var trim2dCurve = trim.TrimCurve;
}

// BrepVertex topology (3D modeling space)
Rhino.Geometry.Collections.BrepVertexList vertices = brep.Vertices;
for(int vi = 0; vi < vertices.Count; vi++)
{
      BrepVertex vertex = vertices[vi];
      // Get vertex edges
      var vEdges = vertex.EdgeIndices();
      // Get vertex location
      var vPoint = vertex.Location;
}
```
In polysurfaces (which are **Breps** with multiple faces), some geometry and topology elements are shared along the connecting curves & vertices where polysurface faces join together. In the following example, the two faces F0 & F1 share one edge E0 and two vertices V0 & V2.

<figure>
   <img src="verts_edges.png">
   <figcaption>Figure(28): Vertices, edges and 3-D curves are shared between neighboring faces. Edge (E0) and Vertices (V0 & V2) are shared between the two faces (F0 & F1).</figcaption>
</figure> 

As illustrated before, **Breps** has a rather complex data structure, and it is useful to learn how to navigate this data. The following examples show how to get some of the geometry parts:

Example to count geometry & topology elements of a Brep and then extract the 3D geometry

<img src="count_brep.png"  class="float_right" width="225">
<img src="count_brep_panel.png"  class="float_right" width="225">


```C#
Brep brep = … // from input
// Print the number of geometry elements
Print("brep.Vertices.Count = {0}", brep.Vertices.Count);
Print("brep.Curves3D.Count = {0}", brep.Curves3D.Count);
Print("brep.Curves2D.Count = {0}", brep.Curves2D.Count);
Print("brep.Surfaces.Count = {0}", brep.Surfaces.Count);

// Print the number of topology elements
Print("brep.Trims.Count = {0}", brep.Trims.Count);
Print("brep.Loops.Count = {0}", brep.Loops.Count);
Print("brep.Faces.Count = {0}", brep.Faces.Count);
Print("brep.Edges.Count = {0}", brep.Edges.Count);

// Extract 3d geometry elements
var V = brep.Vertices;
var C = brep.Curves3D;
var S = brep.Surfaces;
```

Example to extract the outline of a Brep ignoring all holes

<img src="brep_trim.png"  class="float_right" width="225">


```C#
Brep brep = … // from input
// Declare outline list of curves
List<Curve> outline = new List<Curve>();
// Check all the loops and extract naked that are not inner
foreach (BrepLoop eLoop in brep.Loops) {
    // Make sure the loop type is outer
    if (eLoop.LoopType == BrepLoopType.Outer) {
        // Navigate through the trims of the loop
        foreach (BrepTrim trim in eLoop.Trims) {
            // Get the edge of each trim
            BrepEdge edge = trim.Edge;
            // Check if the edge has only one trim
            if (edge.TrimCount == 1) {
                // Add a copy of the edge curve to the list
                outline.Add(edge.DuplicateCurve());
          }
        }
    }
}
```

Example to extract all the faces of a **Brep** box and move them away from the center:

<img src="brep_faces.png"  class="float_right" width="225">

```C#
Brep brep = … // from input
// Declare a new list of faces
List<Brep> faces = new List<Brep>();

// Find the center
Point3d center = brep.GetBoundingBox(true).Center;
for (int i = 0; i <= brep.Faces.Count - 1; i++) {
    // Extract the faces
    int[ ] iList = { i };
    Brep face = brep.DuplicateSubBrep(iList);
    // Find face center
    Point3d faceCenter = face.GetBoundingBox(true).Center;
    // Find moving direction
    Vector3d dir = new Vector3d();
    dir = faceCenter - center;
    // Move the face and add to the list
    face.Translate(dir);
    faces.Add(face);
}
```
#### Create Brep Objects

The **Brep** class has many **Create** methods. For example, if you need to create a twisted box, then you can use the **CreateFromBox** method in the **Brep** class as in the following. You can also create a surface out of boundary curves or create a solid out of bounding surfaces.

Create a **Brep** from corners

<img src="brep_corners.png"  class="float_right" width="225">

```C#
List<Point3d> corners = … // from input

// Create the brep from corners
Brep twistedBox = Brep.CreateFromBox(corners);
```

Create a **Brep** from bounding edge curves

<img src="brep_boundary.png"  class="float_right" width="225">

```C#
List<Curve> crvs = … //  from input

// Build the brep from edges
Brep edgeBrep = Brep.CreateEdgeSurface(crvs);
```

Create a **Brep** from bounding surfaces

<img src="brep_bounding.png"  class="float_right" width="225">

```C#
List<Brep> breps = … // from input
double tol = … // from input

 // Build the brep from corners
Brep[ ] solids = Brep.CreateSolid(breps, tol);
```

#### Brep Methods

Here is a list of some of the commonly used create methods found under the **Brep** class. For the full list and details about each method, please refer to the **RhinoCommon SDK** help.

<img src="brep_methods.png">

The **Brep** methods serve multiple functions. Some are to extract information such as finding out if the brep is solid (closed polysurface), others perform calculations in relation to the brep such as area, volume or find a point inside a solid. Some methods change the brep, such as cap holes or merge coplanar faces. Methods that operate on multiple instances of breps include joining or performing some boolean operations. The following are examples to show the range of **Brep** methods:

Example methods to extract **Brep** information: Find if a brep is valid & is a solid

<img src="brep_solids.png"  class="float_right" width="225">

```C#
Brep[] breps = … // from input

List<bool> isSolid = new List<bool>();
foreach( Brep brep in breps)
    if( brep.IsValid )
        isSolid.Add(brep.IsSolid);
```

Example to calculate a brep area, volume, and centroid

<img src="brep_spiral.png"  class="float_right" width="225">

```C#
Brep brep = … // from input
// Declare variable
double area = 0;
double volume = 0;
Point3d vc = default(Point3d);

// Create a new instance of the mass properties classes
VolumeMassProperties volumeMp = VolumeMassProperties.Compute(brep);
AreaMassProperties areaMp = AreaMassProperties.Compute(brep);

// Calculate area, volume, and centroid
area = brep.GetArea();      // or use: area = areaMp.Area
volume = brep.GetVolume();  // or use: volume = volumeMp.Volume
centroid = volumeMp.Centroid;
```

Example methods that change a brep topology: merge coplanar faces in a brep

<img src="brep_merge.png"  class="float_right" width="225">

```C#
Brep brep = … // from input
double tol = 0.01;

bool merged = brep.MergeCoplanarFaces(tol);
```

Example methods that operate on multiple breps: Boolean union 2 breps

<img src="brep_union.png"  class="float_right" width="225">

```C#
List<Brep> breps = … // from input

// Boolean union the input breps
Brep[ ] unionBrep = Brep.CreateBooleanUnion(breps, tol);
```

### 3.3.5: Other Geometry Classes

There are many important classes under the **Rhino.Geometry** namespace that are not derived from **GeometryBase**. Those are commonly used when writing scripts to create & manipulate geometry. We used a couple of them in the examples. You can find the full list of **RhinoCommon** classes in the documentation. Most of these classes are derived directly from the **C#** abstract class **System.Object**. This is the inheritance hierarchy for these classes:

<img src="rhinogeometry_namespace.png">

One important cluster of classes in this list has to do with extracting 2D outlines of the geometry, (**Make2D**). These classes start with **HiddenLineDrawing** keyword. The following diagram shows the sequence of creating the drawing and which classes are used in each step:

<figure>
   <img src="hiddenline.png">
   <figcaption>Figure(29): Workflow & classes used to extract 2D drawing of the geometry</figcaption>
</figure> 

The first step involves setting the parameters such as the source geometry, view, and all other options. Once the parameters are set, the HLD core class can calculate all the lines and hand back to the HLD Segment class with all visibility information & associated source. The user can then use this information to create the final drawing.

#### Create 2D drawing from 3D geometry (Make2D)

<img src="create_3d_drawing.png">

```C#
List<GeometryBase> geomList = … // from input
List<Plane> cplaneList = … // from input

// Use the active view in the Rhino document
var _view = doc.Views.ActiveView;
// Set Make2D Parameters
var _hldParams = new HiddenLineDrawingParameters
{
        AbsoluteTolerance = doc.ModelAbsoluteTolerance,
        IncludeTangentEdges = false,
        IncludeHiddenCurves = true
        };
    _hldParams.SetViewport(_view.ActiveViewport);

    // Add objects to hld_param
    foreach (var geom in geomList){
      _hldParams.AddGeometry(geom, Transform.Identity, null);
}

// Add clipping planes
foreach (var cplane in cplaneList ){
      _hldParams.AddClippingPlane(cplane);
}

// Perform HLD calculation
var  visibleList = new List<Curve>();
var  hiddenList = new List<Curve>();
var  secVisibleList = new List<Curve>();
var  secHiddenList = new List<Curve>();
var _hld = HiddenLineDrawing.Compute(_hldParams, true);
if (_hld != null)
{
    // Transform
    var flatten = Transform.PlanarProjection(Plane.WorldXY);
    BoundingBox pageBox = _hld.BoundingBox(true);
    var delta2D = new Vector2d(0, 0);
    delta2D = delta2D - new Vector2d(pageBox.Min.X, pageBox.Min.Y);
    var delta3D = Transform.Translation(new Vector3d(delta2D.X, delta2D.Y, 0.0));
    flatten = delta3D * flatten;
    // Add curves to lists
    foreach (HiddenLineDrawingSegment hldCurve in _hld.Segments)
    {
        if (hldCurve == null || 
            hldCurve.ParentCurve == null || 
            hldCurve.ParentCurve.SilhouetteType == SilhouetteType.None)
          continue;
        var crv = hldCurve.CurveGeometry.DuplicateCurve();
        if (crv != null)
        {
          crv.Transform(flatten);
          if (hldCurve.SegmentVisibility == HiddenLineDrawingSegment.Visibility.Visible)
          {
            if (hldCurve.ParentCurve.SilhouetteType == SilhouetteType.SectionCut)
              secVisibleList.Add(crv);
            else
              visibleList.Add(crv);
          }
          else if (hldCurve.SegmentVisibility == HiddenLineDrawingSegment.Visibility.Hidden)
          {
            if (hldCurve.ParentCurve.SilhouetteType == SilhouetteType.SectionCut)
              secHiddenList.Add(crv);
            else
              hiddenList.Add(crv);
          }
        }
    }
}
```

## 3.4: Geometry Transformations

All classes derived from **GeometryBase** inherit four transformation methods. The first three are probably the most commonly used which are **Rotate**, **Scale**, and **Translate**. But, there is also a generic **Transform** method that takes a **Transform** structure and can be set to any transformation matrix. The following example shows how to use the scale, rotate, and translate methods on a list of geometry objects.

Use different transformation methods (Scale, Rotate, and Translate)

<img src="geo_transform.png"  class="float_right" width="225">

```C#
List<GeometryBase> objs = … // from input 

// Create a new list of geometry objects
List<GeometryBase> newObjs = new List<GeometryBase>();

foreach (GeometryBase obj in objs) {
    // Scale, rotate, and move
    obj.Scale(factor);
    obj.Rotate(angle, Vector3d.YAxis, Point3d.Origin);
    obj.Translate(dir);

    // Add to list
    newObjs.Add(obj);
}
```

The **Transform** structure is a 4x4 matrix with several methods to help create geometry transformations. This includes defining a shear, projection, rotation, mirror, and others. The structure also has functions that support operations such as multiplication & transpose. For more information about the mathematics of transformations, please refer to *“The Essential Mathematics for Computational Design”*. The following examples show how to create a shear transform & planar projection:

Create shear transformation and output the matrix

<img src="geo_shear.png"  class="float_right" width="225">

```C#
Brep brep = … // from input 

// Create a shear transform
Plane p = Plane.WorldXY;
var v = new Vector3d(0.5, 0.5, 0);
var y = Vector3d.YAxis;
var z = Vector3d.ZAxis;

var xform = Transform.Shear(p, v, y, z);

// Shear the Brep
brep.Transform(xform);
```

Create planar projection transform to project curves

<img src="geo_projection.png"  class="float_right" width="225">

```C#
List<GeometryBase> objs = … // from input 

// Create a new list of geometry objects
List<GeometryBase> newObjs = new List<GeometryBase>();

foreach (GeometryBase obj in objs) {
    // Create a project transform
    obj.Transform(Transform.PlanarProjection(Plane.WorldXY));

    // Add to list
    newObjs.Add(obj);
}
```

## Next Steps

That was a basic overview of RhinoCommon Geometry in Rhino. Now learn to use these methods in [Design Algorithms](/guides/grasshopper/csharp-essentials/4-design-algorithms/) to get something done.

This is the part 3 of the [Essential C# Scripting for Grasshopper guide](/guides/grasshopper/csharp-essentials/).
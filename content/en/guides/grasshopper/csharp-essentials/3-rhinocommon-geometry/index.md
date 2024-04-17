+++
aliases = [""]
authors = [ "rajaa" ]
categories = [ "Csharp Essentials" ]
category_page = "guides/grasshopper/csharp-essentials/"
keywords = [ "csharp", "commands" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "3: RhinoCommon Geometry"
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

## 3.1 Overview

**RhinoCommon** is the **.NET SDK** for Rhino. It is used by Rhino plug-in developers to write **.NET** plug-ins for Rhino and Grasshopper. All Grasshopper scripting components can access **RhinoCommon** including all geometry objects and functions. For the whole namespace, see the **[RhinoCommon documentation](https://developer.rhino3d.com/api/RhinoCommon)**

In this chapter, we will focus on the part of the **SDK** dealing with Rhino geometry.  We will show examples of how to create and manipulate geometry using the Grasshopper C# component.

The use of the geometry classes in the **SDK** requires basic knowledge in vector mathematics, transformations and NURBS geometry. If you need to review or refresh your knowledge in these topics, then refer to the *[Essential Mathematics for Computational Design](https://www.rhino3d.com/download/rhino/6/essentialmathematics)*

If you recall from Chapter 2, we worked with value types such as **int** and **double**. Those are system built-in types provided by the programming language, **C#** in this case. We also learned that you can pass the value types to a function without changing the original variables (unless passed by reference using the **ref** keyword). We also learned that some types, such as **objects**, are always passed by reference. That means changes inside the function also changes the original value.

The system built-in types, whether they are value or reference types, are often very limiting in specialized programming applications. For example, in computer graphics, we commonly deal with points, lines, curves or matrices. These types need to be defined by the **SDK** to ease the creation, storage and manipulation of geometry data. Programming languages offer the ability to define new types using **structures** ( value types) and **classes** ( reference types). The **RhinoCommon SDK** defines many new types as we will see in this chapter.

## 3.2: Geometry structures

**RhinoCommon** defines basic geometry types using structures. We will dissect the **Point3d** structure and show how to read in the documentation and use it in a script. This should help you navigate and use other structures. Below is a list of the geometry structures.

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
    <td>Vector in 3D space. There is also Vector2d for vectors in parameter space</td>
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
    <td>A plane defined by a plane origin, X-Axis, Y-Axis and Z-Axis</td>
  </tr>
 <tr>
    <td><b>Arc</b></td>
    <td>Represents the value of a plane, two angles and a radius in a subcurve of a circle</td>
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
    <td>Represents the values of a plane and two intervals that form an oriented rectangle </td>
  </tr>
 <tr>
    <td><b>Cone</b></td>
    <td>Represents the center plane, radius and height values in a right circular cone.</td>
  </tr>
 <tr>
    <td><b>Cylinder</b></td>
    <td>Represents the values of a plane, a radius and two heights -on top and beneath- that define a right circular cylinder.</td>
  </tr>
 <tr>
    <td><b>BoundingBox</b></td>
    <td>Represents the value of two points in a bounding box defined by the two extreme corner points.This box is therefore aligned to the world X, Y and Z axes.</td>
  </tr>
 <tr>
    <td><b>Box</b></td>
    <td>Represents the value of a plane and three intervals in an orthogonal, oriented box that is not necessarily parallel to the world Y, X, Z axes.</td>
  </tr>
 <tr>
    <td><b>Sphere</b></td>
    <td>Represents the plane and radius values of a sphere.</td>
  </tr>
 <tr>
    <td><b>Torus</b></td>
    <td>Represents the value of a plane and two radii in a torus that is oriented in 3D space.</td>
  </tr>
 <tr>
    <td><b>Transform</b></td>
    <td>4x4 matrix of numbers to represent geometric transformation</td>
  </tr>
</table>

## 3.2.1: The Point3d structure

The **[Point3d](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Point3d.htm)** type includes three **fields** (X, Y and Z). It defines a number of **properties** and also has **constructors** and **methods**. We will walk through all the different parts of **Point3d** and how it is listed in the **RhinoCommon** documentation. First, you can navigate to **Point3d** from the left menu under the **Rhino.Geometry** namespace. When you click on it, the full documentation appears on the right. At the very top, you will see the following:

<img src="point3d_api.png">

Here is a break down of what each part in the above **Point3d** documentation means:

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
    <td>The assembly that includes that type. All geometry types are part of the RhinoCommon.dll</td>
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
Structures can implement any number of interfaces. An interface contains a common functionality that a structure or a class can implement. It helps with using consistent names to perform similar functionality across different types. 
For example IEquatable interface has a method called “Equal”. If a structure implements IEquatable, it must define what it does (in Point3d, it compares all X, Y and Z values and returns true or false).</td>
  </tr>
</table>

#### Point3d Constructors:

Structures define constructors to instantiate the data. One of the **Point3d** constructors takes three numbers to initialize the values of X, Y and Z. Here are all the constructors of the **Point3d** structure .

<img src="constructors.png">

The following example shows how to define a variable of type Point3d using a GH C# component.

<img src="point3d_gh.png">

```C#
private void RunScript(double x, double y, double z, ref object Point)
{
    //Create an instance of a point and initialize to x, y and z
    Point3d pt = new Point3d(x, y, z);

    //Assign the point "pt" to output
    Point = pt;
}
```

#### Point3d Properties: 

Properties are mostly used to “get” and/or “set” the fields of the structure. For example, there are the “X”, “Y” and “Z” properties to get and set the coordinates of an instance of **Point3d**. Properties can be **static** to get specific points, such as the origin of the coordinate system (0,0,0). The following are **Point3d** properties as they appear in the documentation:

<img src="properties.png">
 
Here are two GH examples to show how to get and set the coordinates of a **Point3d**. 

<img src="set_point3d.png">

```C#
private void RunScript(Point3d pt, ref object A, ref object B, ref object C)
{
    //Assign the point coordinates to output
    a = pt.X;
    b = pt.Y;
    c = pt.Z;
}
```
<img src="set_point_coordinate.png">

```C#
private void RunScript(double x, double y, double z, ref object Point)
{
    //Declare a new point
    Point3d newPoint = new Point3d(Point3d.Unset);

    //Set "new_pt" coordinates
    newPoint.X = x;
    newPoint.Y = y;
    newPoint.Z = z;

    //Assign the point coordinates to output
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
    //Create an instance of a point and initialize to x, y and z
    Point3d pt = new Point3d(x, y, z);
    //Calculate the distance from "pt" to the "other" input point
    double dis = pt.DistanceTo(other);
    //Assign the point "point" to the A output
    Point = pt;
    //Assign the distance to the B output
    Distance = dis;
}
```

The **DistanceTo** method does not change the fields (the X, Y and Z). However, other methods such as **Transform** change the fields. The **Transform** method resets the X, Y and Z values to reflect the new location after applying the transform.

<img src="transform_point_method.png">

Here is an example that uses **Point3d.Transform**.

<img src="point_transform_component.png">

```C#
private void RunScript(Point3d pt, Transform xform, ref object Point)
{
    //Create an instance of a point and initialize to input point
    Point3d newPoint = new Point3d(pt);
    //Transform the point
    newPoint.Transform(xform);
    //Assign the point "new_pt" to the A output
    Point = newPoint;
}
```
#### Point3d static methods:

Point3d has **static** methods that are accessible without instantiating an instance of **Point3d**. For example, if you would like to check if a list of given instances of points are all coplanar, you can call the static method **Point3d.ArePointsCoplanar** without creating an instance of a point. Static methods have the little red “s” symbol in front of them in the documentation.

<img src="arepointcoplaner.png">

The **ArePointsCoplanar** has the following syntax, parameters and the return value.

<img src="arepointscoplanar_method.png">

Here is an example that uses the static method **Point3d.ArePointsCoplanar**.

<img src="pointscoplaner_component.png">

```C#
private void RunScript(List<Point3d> pts, double tol, ref object IsCoplanar)
{
     //Test if the list of input points are coplanar
    bool coplanar = Point3d.ArePointsCoplanar(pts, tol);

    //Assign the co-planar test to output
    IsCoplanar = coplanar;
}
```
#### Point3d Operators:

Many Structures and Classes in RhinoCommon implement operators whenever relevant. Operators enable you to use the “+” to add two points or use the “=” to assign the coordinates of one point to the other. **Point3d** structure implements many operators and this simplifies the coding and its readability. Although it is fairly intuitive in most cases, you should check the documentation to verify which operators are implemented and what they return. For example, the documentation of adding 2 **Point3d** indicates the result is a new instance of **Point3d** where X, Y and Z are calculated by adding corresponding fields of 2 input **Point3d**.

<img src="point3d_addition_operator.png">

Note that all operators are declared **public** and **static**. Here is an example that shows how the “+” operator in **Point3d** is used. Note that the “+” returns a new instance of a **Point3d**.

<img src="add_points_component.png">

```C#
private void RunScript(Point3d pt1, Point3d pt2, ref object Point)
{
    //Add 2 points and assign result to output
    Point = pt1 + pt2;
}
```
#### Point3d as a function parameter:

**Point3d** is a value type because it is a structure. That means if you pass an instance of **Point3d** to a function and change its value inside that function, the original value outside the function will not be changed, as in the following example:

<img src="struct_point_pass.png">

```C#
private void RunScript(double x, double y, double z, Point3d pt2, ref object Point)
{
    Point3d pt = new Point3d(x, y, z);
    Print("Before calling ChangeX function: pt.x=" + pt.X);


    //Call a function to change the value of X in the point
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
### 3.2.2 Points and Vectors

**RhinoCommon** has a few structures to store and manipulate points and vectors.  Take for example the double precision points. There are three types of points that are commonly used listed in the table below. For more detailed explanation of vectors and points, please refer to the [Essential Mathematics for Computational Design](https://www.rhino3d.com/download/rhino/6/essentialmathematics), a publication by McNeel. 

<table class="rounded">
  <tr>
    <th>Class Name</th>
    <th>Member Variables</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><b>Point2d</b></td>
    <td>X as Double </br>Y as Double</td>
    <td>Used for parameter space points.</td>
  </tr>
  <tr>
    <td><b>Point3d</b></td>
    <td>X as Double </br>Y as Double</td>
    <td>Most commonly used to represent points in three dimensional coordinate space</td>
  </tr>
  <tr>
    <td><b>Point4d</b></td>
    <td>X as Double </br>Y as Double </br>Z as Double </br>W as Double</td>
    <td>Used for grips or control points.  Grips have weight information in addition to the 3D location.</td>
  </tr>
</table>

As for vectors, there are two main types.

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

The following are a few point and vector operations with examples of output. The script starts with declaring and initializing a few values, then applying some operations.











## Next Steps

That was a basic overview of Python running in Rhino.  Now learn to use [operators and functions](/guides/rhinopython/primer-101/4-operators-and-functions/) to get something done.

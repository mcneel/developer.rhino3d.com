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

## Next Steps

That was a basic overview of Python running in Rhino.  Now learn to use [operators and functions](/guides/rhinopython/primer-101/4-operators-and-functions/) to get something done.

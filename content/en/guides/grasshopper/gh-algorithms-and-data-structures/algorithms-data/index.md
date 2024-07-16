+++
aliases = [""]
authors = [ "rajaa" ]
categories = [ "Essentials Algorithms and Data Structures" ]
category_page = "guides/grasshopper/gh-algorithms-and-data/"
keywords = [ "algorithms", "data", "grasshopper" ]
languages = [ "" ]
sdk = [ "" ]
title = "Chapter 1: Algorithms and Data"
type = "guides"
weight = 15
override_last_modified = "2024-07-15T14:59:06Z"
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

## 1.1 Algorithmic design

We can define algorithmic design as a design method where the **output** is achieved through **well-defined steps**. In that sense, many human activities are algorithmic. Take, for example, baking a cake. You get the **cake** (output) by using a **recipe** (well-defined steps). Any change in the ingredients (input) or the baking process results in a different cake. We will analyze the parts of typical algorithms, and identify a strategy to build algorithmic solutions from scratch.

Regardless of its complexity, all algorithmic solutions have 3 building blocks: **input, key process,** and **output**. Note that the key process may require additional input and processes.

<figure>
   <img src="ads-002.png">
   <figcaption>Figure(1): The building blocks of algorithmic solutions</figcaption>
</figure>  

Throughout this text, we will organize and label the solutions to identify the three blocks clearly. We will also use consistent color coding to visually distinguish between the parts. This will help us become more comfortable with reading algorithms and quickly identify input, key processing steps, and properly collect and display output. Visual cues are important to develop fluency in algorithmic thinking.

In general, reading existing algorithmic solutions is relatively easy, but building new ones from scratch is much harder and requires a new set of skills. While it is useful to know how to read and modify existing solutions, it is essential to develop algorithmic design skills to build new solutions from scratch.


## 1.2 Algorithms parts

In Grasshopper, a solution flows from left to right. At the far left are input values and parameters, and the far right has the output. In between are one or more key processes, and sometimes additional input and output. Let’s take a simple example to help identify the three parts of any algorithm (input, key process, output). The simple addition algorithm includes two numbers (input), the sum (output) and one key process that takes the numbers and gives the result. We will use purple for the input, maroon for the key processes and light blue for the output. We will also group and label the different parts and adhere to organizing the Grasshopper solutions from left to right.

**Example 1-2-1:**
Algorithm to add 2 numbers
<figure>
   <img src="ads-003.png">
</figure>  

Algorithms may involve intermediate processes. For example, suppose we need to create a circle (output) using a center and a radius (input). Notice that the input is not sufficient because we do not know the plane on which the circle should be created. In this case, we need to generate additional information, namely the plane of the circle. We will call this an intermediate process and use brown color to label it.

**Example 1-2-2:**
Algorithm to create a circle on the XY-Plane from a center and a radius
<figure>
   <img src="ads-004.png">
</figure>  

Some solutions are not written with styles and hence are hard to read and build on. It is very important that you take the time to organize and label your solutions to make them easier to understand, debug and use by others.  

<table class="rounded">
  <tr>
    <th>Tutorial 1-2-3: Read existing algorithm</th>
  </tr>
  <tr>
    <td>
    Given the following definition, write a description of what the algorithm does, identify input, the main process(s) and output, then label and color-code all the parts. Re-write the solution to make it more readable.
    <figure>
    <img src="ads-005.png">
    </figure>
    </td>
  </tr>
  <tr>
    <th>Solution</th>
  </tr>
  <tr>
    <td>
    In order to figure out what the algorithm is meant to do, we need to group the input on the left side, and collect the output on the right side, then organize the processes in the order of execution. We then step through the solution from left to right to deduce what it does. We can examine and preview the output in each step.
    <br><br>
    The example of the tutorial is meant to create a circle that is twice as large as another circle that goes through three given points. One of the points is constructed out of its 3 coordinates.
    <figure>
    <img src="ads-006.png">
    </figure> 
    </td>
  </tr>
</table>

## 1.3 Designing algorithms: the 4-step process

Before we generalize a method to design algorithms, let’s examine an algorithm we commonly use in real life such as baking a cake. If you already have a recipe for a cake, you simply get the recommended ingredients, mix them, pour in a pan, put in a preheated oven for a certain amount of time, then serve. If the recipe is well documented, then it is relatively straightforward to use. As you become more proficient in baking cakes, you may start to modify the recipe. Perhaps add new ingredients (chocolate or nuts) or use different tools (cupcake container).

<figure>
   <img src="ads-007.png">
   <figcaption>Figure(2): Steps to follow existing recipe</figcaption>
</figure>  

When designers write algorithms, they typically try to search for existing solutions and modify them to fit their purposes. While this is a good entry point, using existing solutions can be frustrating and time-consuming. Also, existing solutions have their own flavor and that may influence design decisions and limit creativity. If designers have unique problems, and they often do, they have no choice but to create new solutions from scratch; albeit a much harder endeavor. 

Back to our example, the task of baking a cake is much harder if you don’t have a recipe to follow and have not baked one before. You will have to guess the ingredients and the process. You will likely end up with bad results in the first few attempts, until you figure it out! In general, when you create a new recipe, you have to follow the process in reverse. You start with an image of the desired cake, you then guess the ingredients, tools and steps. Your thinking goes along the following lines:

- The cake needs to be baked, so I need an oven and time,
- What goes in the oven is a cake batter held by a container,
- The batter is a mix of ingredients

<figure>
   <img src="ads-008.png">
   <figcaption>Figure(3): Steps to invent a new recipe from scratch</figcaption>
</figure>  

We can use a similar methodology to design parametric algorithms from scratch. Keep in mind that creating new algorithms is a “skill” and it requires patience, practice and time to develop.

**Algorithmic thinking in 3D modeling vs parametric design**
3D modeling involves a certain level of algorithmic thinking, but it has many implicit steps and data. For example designing a mass model using a 3D modeler may involve the following steps:

1. Think about the output (e.g. a mass out of few intersecting boxes)
2. Identify a command or series of commands to achieve the output ( e.g. run Box command a few times, Move, Scale or Rotate one or more boxes, then BooleanUnion the geometry).

At that point, you are done!

Data such as the base point for your initial box, width, height, scale factor, move direction, rotation angle, etc. are requested by the commands, and the designer does not need to prepare ahead of time. Also, the final output (the boolean mass) becomes directly available and visible as an object in your document.

<figure>
   <img src="ads-009.png">
   <figcaption>Figure(4): Interactive 3D modeling to create and manipulate geometry uses visual widgets and guides</figcaption>
</figure>  

Algorithmic solutions are not interactive and require explicit articulation of data and processes. In the box example, you need to define the box orientation and dimensions. When copy, you need a vector and when rotate you need to define the plane and angle of rotation. 

<figure>
   <img src="ads-010.png">
   <figcaption>Figure(5): Algorithmic solutions involve explicit definition of geometry, vectors and transformations</figcaption>
</figure>  

## 1.4 Data

LabLab

## 1.5 Data sources

LabLab

## 1.6 Data types

LabLab

## 1.7 Processing Data

LabLab

### 1.7.1 Numeric operations

LABLAB

### 1.7.2 Logical operations

LabLAB

### 1.7.3 Data analysis

LabLAB

### 1.7.4 Sorting

LabLAB

### 1.7.5 Selection

LabLAB

### 1.7.6 Mapping

LabLAB

## 1.8 Pitfalls of algorithmic design

### 1.8.1 Invalid or wrong input type

LabLab

### 1.8.2 Unintended input

LabLab

### 1.8.3 Incorrect order of operation

LabLab

### 1.8.4 Mismatched data structures

LabLab

### 1.8.5 Long processing time

LabLab

### 1.8.6 Poor organization

LabLab

## 1.9 Tutorials: algorithms and data

### 1.9.1 Unioned circles tutorial

LabLab

### 1.9.2 Sphere with bounds tutorial

LabLab

### 1.9.3 Data operations tutorial

LabLab

### 1.9.4 Pitfalls tutorial

LabLab

## Next Steps

Those are the algorithms and data. Next, learn [Introduction to Data Structures](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/).

This is part 1-3 of the [Essential Algorithms and Data Structures for Grasshopper](/guides/grasshopper/gh-algorithms-and-data-structures/).

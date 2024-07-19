+++
aliases = [""]
authors = [ "rajaa" ]
categories = [ "Essentials Algorithms and Data Structures" ]
category_page = "guides/grasshopper/gh-algorithms-and-data/"
keywords = [ "data strucutres", "grasshopper" ]
languages = [ "" ]
sdk = [ "" ]
title = "Chapter 3: Advanced Data Structures"
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

This chapter is devoted to the advanced data structure in GH, namely the data trees, and different ways to generate and manage them. The aim is to start to appreciate when and how to use tree structures, and best practices to effectively use and manipulate them.<br>

## 3.1 The Grasshopper data structure

### 3.1.1 Introduction

In programming, there are many data structures to govern how data is stored and accessed. The most common data structures are variables, arrays, and nested arrays. There are other data structures that are optimised for specific purposes such as data sorting or mining. In Grasshopper, there is only one structure to store data, and that is the <b>data tree</b>. Hold on, what about what we have learned so far: <b>single</b> item and <b>list</b> of items? Well, in GH, those are nothing but simple trees. A single item is a tree with one branch, that has one element, and a list is a tree with one branch that has a number of elements. It is actually pretty elegant to be able to fit all data in one unifying data structure, but at the same time, this requires the user to be aware and vigilant about how their data structure changes between operations, and how that can affect intended results. This chapter attempts to demystify the data tree of Grasshopper.

### 3.1.2 Processing data trees

We used the <b>Panel</b> and <b>Parameter Viewer</b> components to view the data structure. We will use both extensively to show how data is stored. Let’s start with a single item input. The Parameter Viewer has two display modes, one with text and one that is graphical. You can see that the single item input is stored in one branch that has only one item.
<figure>
   <img src="ads-200.png" class="image_center" width="85%">
   <figcaption>Figure(51): Different ways to preview the data structure in Grasshopper</figcaption>
</figure>

The <b>Parameter Viewer</b> shows each branch address (called “Path”), and the number of elements in that branch as shown in Figure (52).
<figure>
   <img src="ads-201.png" class="image_center" width="50%">
   <figcaption>Figure(51): The Parameter Viewer indicates the path address and the number of elements in each branch</figcaption>
</figure>

A list of items is typically stored in a tree with one branch. Figure (53). However, the three items can also be stored in three different branches. Figure (54).

<figure>
   <img src="ads-202.png" class="image_center" width="85%">
   <figcaption>Figure(53): A list is a tree that has one branch with multiple elements</figcaption>
</figure>

<figure>
   <img src="ads-203.png" class="image_center" width="85%">
   <figcaption>Figure(54): A tree contains any number of branches with any number of elements in each branch</figcaption>
</figure>

The key to understanding the Grasshopper data structure is to be able to answer the following question:<br>
<b>What is the significance of storing x number of values in one branch vs using x number of branches to store one value in each branch?</b><br>
The data structure informs GH components about how to match input values. In other words, components may process data differently based on their structure. The following example illustrates how different data structures for the same set of values can affect the result.

<figure>
   <img src="ads-204.png">
   <figcaption>Figure(55): Organizing same set of value in different data structures affect the output</figcaption>
</figure>

We will elaborate on data tree matching later, but you can already see that GH components do pay attention to the data structure and the result can vary considerably based on it. This is one of the complications inherited in using one unifying data structure in a programming language.

### 3.1.3 Data tree notation
The first step to understanding data trees is to learn the GH notation of trees. As we have seen from the examples, trees consist of branches, and each branch holds a number of elements. The address or path of each branch is represented with integers separated by semicolons and enclosed in curly brackets. The index of each element is enclosed by square brackets. This diagram shows a breakdown of the address of elements in trees.

<figure>
   <img src="ads-205.png">
   <figcaption>Figure(56): Address of elements include the address of the branch and the index of the element in the branch</figcaption>
</figure>

Here are a few examples of various tree structures and how they show in the <b>Parameter Viewer</b> and the <b>Panel</b>.

<figure>
   <img src="ads-206.png">
   <figcaption>Figure(57): Same set of values held in different structures. Left: 5 trunks (5 trees) with one item in each. Middle: 5 branches out of one trunk (1 tree), and each branch holds a single item. Right: two trunks (2 trees), the first has 2 branches with the first branching into 3 branches, each holds one item, the second holds 1 item. The second trunk holds 2 items.
</figcaption>
</figure>

<table class="rounded">
  <tr>
    <th>Tutorial 3.1.1 Data tree</th>
  </tr>
  <tr>
  <td>
   <table>
    <tr>
     <td>
     1. In the tree, what is the full address to the item <b>1.2</b>? Note that order of branches and leaves is always from left to right going clockwise<br><br>
     2. Construct the tree of numbers shown in the image below using the <b>Number</b> parameter only.
     </td>
     <td>
     <img src="ads-207.png">
     </td>
    </tr>
   </table>
  </td>
  </tr>
  <tr>
    <td>
        <details>
        <summary><b>Solution...</b></summary>
        <br>
        <table>
          <tr>
            <td>
            The path to <b>1.2</b> is: <b>{ 0 ; 3 ; 0} [ 1 ]</b><br>
            <br>Note: The three branches from the main trunk are set here to 0:1, 0:2, and 0:3. They also could have been 0:0, 0:1 and 0:2. Both are correct.
            </td>
            <td>
            <img src="ads-207A.png">
            </td>
          </tr>
        </table>
        <br><img src="ads-209.png"><br>
        </details>
    </td>
  </tr>
</table>

## 3.2 Generating trees

There are many ways to generate complex data trees. Some explicit, but mostly as a result of some processes, and this is why you need to always be aware of the data structures of output before using it as input downstream. It is possible to enter the data and set the data structure directly inside any Grasshopper parameter. Once set, it is relatively hard to change and therefore is best suited for a constant input. The following is an example of how to set a data tree directly inside a parameter.

<figure>
   <img src="ads-210.png">
   <figcaption>Figure(58):  Set data trees directly inside the parameter</figcaption>
</figure>

There are many components that generate data trees such as <b>Grid</b> and <b>DivideSrf</b>, and others that combine lists into a tree structure such as <b>Entwine</b>. Also all the components that produce lists can also create a tree if the input is a list. For example, if you input more than one curve into the <b>DivideCrv</b> component, we get a tree of points.

<figure>
   <img src="ads-211.png">
   <figcaption>Figure(59):  The SDivide component takes one input (surface) and outputs a data tree (grid)</figcaption>
</figure>

All components that generate lists of numbers (such as <b>Range</b> and <b>Series</b>) can also generate trees when given a list of input.

<figure>
   <img src="ads-212.png">
   <figcaption>Figure(60):  Entwine component takes any number of lists and combines them into a tree structure</figcaption>
</figure>

Perhaps one of the most common cases to generate a tree is when dividing a list of curves to generate a grid of points. So the input is one list and the output is a tree.

<figure>
   <img src="ads-213.png">
   <figcaption>Figure(61):  EDivide component takes any list (curves) and generates a tree structure (grid)</figcaption>
</figure>

<table class="rounded">
  <tr>
    <th>Tutorial 3-2-1: Generating trees</th>
  </tr>
  <tr>
    <td>
    Given the following list of points, construct a number tree with 3 branches, one for each coordinate.
    <img src="ads-213A.png" class="image_center" width="75%">
    </td>
  </tr>
  <tr>
    <td>
        <details>
        <summary><b>Solution...</b></summary>
        <br>Each input point is a single data item that contains 3 numbers (coordinates). We know we would like to isolate each coordinate into a separate list, then combine them into one data structure. Hence we need to first deconstruct input points (use <b>Deconstruct</b> of <b>pDecon</b> component), then combine the lists into one structure (use <b>Entwine</b> component).<br>
        <img src="ads-215.png">
        </details>
    </td>
  </tr>
</table>

## 3.3 Tree matching

We explained the <b>Long</b>, <b>Short</b> and <b>Cross</b> matching with lists. Trees follow similar conventions to expand the shorter branches by repeating the last element to match. If one tree has fewer branches, the last branch is repeated. The following illustrates common tree matching cases.

### 3.3.1 Item-to-tree matching
When matching an item to a tree, a matching tree structure is created and the item is repeated. For example when adding a single number to a tree of numbers, the single number is added to every item in the tree and the result is a tree with matching strucuture to the input tree.
<img src="ads-216.png">

### 3.3.2 Short-list-to-tree matching
When matching a short list to a tree, where the length of the list is shorter than the tree branches, a matching tree structure is created where the list is repeated in each branch, and the last item in the short list is repeated. See the following example adding a list of two number to a tree of numbers.
<img src="ads-217.png">

### 3.3.3 Long-list-to-tree matching
When matching a long list to a tree with branches that are shorter than the list, the tree branches expand to match the length of the list. The last item in each branch is repeated to match the list length Note that the resulting tree strucuture will be differenent than the input tree. In the following example, both input, the list and the tree, are modified to arrive to a matching structure, then the addition result have than new data strucuture.
<img src="ads-218.png">

### 3.3.4 Tree-to-tree matching
There are numerous possibilities when matching two trees, but the basic principle apply. The goal is to find a tree strucuture that can combine both input tree strucutures. Let’s assume the case when there is a simple tree with one level of branches that match in depth. There are two possibilities. The first is that both input trees have same number of branches. In this case, the length of the shorter corresponding branches is matched. The output tree might end up matching at least one of the input trees, or be different to both.
<img src="ads-219.png">

The second possibility is that one tree might have more branches than the other. In that case, new branches are inserted into the smaller tree repeating the last branch, then each branch is expanded (repeating the last item in the branch) to create matching length among all corresponding branches as in the following example.
<img src="ads-220.png">

When working with trees, it is of utmost importance to examine the data strucuture of each input before using it as input to one component. A small change in the strucuture can have big impact. For example, the following two trees of numbers appear to be matching at first, but because there is one level depth added to one of the trees (indicating an extra branch near the root of the tree), the result may be different than what is intended.

<table class="rounded">
  <tr>
    <th>Tutorial 3.3.1 Tree matching</th>
  </tr>
  <tr>
  <tr>
    <td>
     Inspect the following 2 number structures, then predict the structure and result of adding them (with default Grasshopper matching). Verify your answer using the <b>Addition</b> components.<br>
     <img src="ads-221.png" class="image_center" width="75%">
    </td>
    </tr>
  <tr>
    <td>
        <details>
        <summary><b>Solution...</b></summary>
        <br>
        <table>
          <tr>
            <td>
            Key solution idea: The two input trees have different number of branches and different number of elements in each branch. The last branch of the shorter tree is repeated to match the number of branches, then corresponding branches are matched by repeating the last element of the shorter branch.<br><br>
            <img src="ads-222.png">
            </td>
          </tr>
        </table>
        </details>
    </td>
  </tr>
</table>

## 3.4 Traversing trees

Grasshopper provides components to help extract branches and items from trees. If you have the path to a branch or to an item, then you can use <b>Branch</b> and <b>Item</b> components. You need to check the structure of your input so you can supply the correct path.

<figure>
   <img src="ads-223.png">
   <figcaption>Figure(62):  Select branches from a tree</figcaption>
</figure>

<figure>
   <img src="ads-224.png">
   <figcaption>Figure(63):  Select items from a tree</figcaption>
</figure>

If you know that your structure might change, or you simply do not want to type the path, you can extract the path using  the <b>Param Viewer</b> and List <b>Item</b> components.

<figure>
   <img src="ads-225.png">
   <figcaption>Figure(64):  Example of how to extract data paths dynamically</figcaption>
</figure>

<table class="rounded">
  <tr>
    <th>Tutorial 3.4.1 Traversing trees</th>
  </tr>
  <tr>
  <tr>
    <td>
     The following tree has 3 branches for each one of the coordinates (x, y, z) of some list of points. Use that tree to construct a list of these points.<br>
     <img src="ads-226.png" class="image_center" width="75%">
    </td>
    </tr>
  <tr>
    <td>
        <details>
        <summary><b>Solution...</b></summary>
        <br>
        <table>
          <tr>
            <td>
            Key solution idea: We can construct a point list using as input 3 lists representing X, Y and Z values. If we can isolate the 3 branches of the input tree, then we will be able to feed them to the point construction component.<br><br>
            <img src="ads-227.png">
            </td>
          </tr>
        </table>
        </details>
    </td>
  </tr>
</table>

## 3.5 Basic tree operations

Basic tree operations are widely used and you will likely need them in most solutions. It is very important to understand what these operations do, and how they affect the output.

### 3.5.1: Viewing the tree structure
As we have seen in the data matching, different data structures of the same set of elements produce different results. Grasshopper offers three ways to view the data structure, the Parameter Viewer in text or diagram format, and the Panel.

<figure>
   <img src="ads-228.png">
   <figcaption>Figure(65):  View trees using the Parameter Viewer and the Panel components</figcaption>
</figure>

Tree information can be extracted using the <b>TStats</b> component. You can extract the list of paths to all branches, number of elements in each branch and the number of branches.

<figure>
   <img src="ads-229.png">
   <figcaption>Figure(66):  Extract trees structure using TStats component</figcaption>
</figure>

### 3.5.2 List operations on trees

Trees can be thought of as a list of branches. When using list operations on trees, each branch is treated as a separate list and the operation is applied to each branch independently. It is tricky to predict the resulting data structure and therefore it is always important to check your input and output structures before and after applying any operation.
To illustrate how list operations work in trees, we will use a simple tree, a grid of points, and apply different list operations on it. We will then examine the output and its data structure.

<table class="rounded">
  <tr>
    <th>Common list operation and how they apply to trees</th>
  </tr>
  <tr>
    <td>
    <b>List Item</b>: Select items at specific index in each branch<br>
    <img src="ads-230.png">
    </td>
  </tr>
    <tr>
    <td>
    <b>List Item</b>: Select multiple indices to isolate part of the tree and perform one operation on such as <b>Mass Addition</b><br>
    <img src="ads-231.png">
    </td>
  </tr>
    <tr>
    <td>
    <b>Split List</b>: Split the elements of branches into 2 trees at the specified index<br>
    <img src="ads-232.png">
    </td>
  </tr>
    <tr>
    <td>
    <b>Shift List</b>: Shifts the elements of each branch<br>
    <img src="ads-233.png" class="image_center" width="75%">
    </td>
  </tr>
    <tr>
    <td>
    <b>Cull Pattern</b>: Culls each branch<br>
    <img src="ads-234.png" class="image_center" width="75%">
    </td>
  </tr>
</table>

### 3.5.3 Grafting from lists to a trees

In some cases you need to turn a list into a tree where each element is placed in its own branch. Grafting can handle complex trees with branches of variable depths.

<figure>
   <img src="ads-235.png">
   <figcaption>Figure(67):  Grafting a tree creates a new branch for each element</figcaption>
</figure>

It might feel unintuitive to complicate the data structure (from a simple list to a tree), but grafting is very useful when trying to achieve certain matching. For example if you need to add each element of one list with all the elements in the second list, then you will need to graft the first list before inputting to the addition process.

<figure>
   <img src="ads-236.png">
   <figcaption>Figure(68):  Grafting complex trees</figcaption>
</figure>

### 3.5.4 Flattening from trees to lists

Other times you might need to turn your tree structure into a simple list. This is achieved with the flattening process. Data from each branch is extracted and sequentially attached to one list.

<figure>
   <img src="ads-237.png">
   <figcaption>Figure(69):  Flattening place all tree elements in one list</figcaption>
</figure>

Flatten also can handle any complex tree. It takes the branches in order starting with the lowest index trunk and put all elements in one list.

<figure>
   <img src="ads-238.png">
   <figcaption>Figure(70):  Flattening complex trees</figcaption>
</figure>

### 3.5.5 Combining data streams

It is possible to compose a number of lists into a tree where each list becomes a branch in a new tree. It is different from the merging of lists where simply one bigger list is created.

<figure>
   <img src="ads-239.png" class="image_center" width="75%">
   <figcaption>Figure(71):  Entwine and Merge components combine lists into trees or bigger lists</figcaption>
</figure>

### 3.5.6 Flipping the data structure

It is logical in some cases to flip the tree to change the direction of branches.This is specially useful in grids when points are organized in rows and columns (similar to a 2 dimensional array structure). Flipping causes corresponding elements across branches (have the same index in their branch) to be grouped in one branch. For example, a data tree that has 2 branches and 4 items in each branch, can be flipped into a tree with 4 branches and 2 elements in each branch.

<figure>
   <img src="ads-240.png">
   <figcaption>Figure(72):  Flip helps reorganize data in a trees</figcaption>
</figure>

If the number of elements in the branches are variable in length, some of the branches in the flipped tree will have “null” values.

<figure>
   <img src="ads-241.png">
   <figcaption>Figure(73):  Add “null” when flipping trees with variable length branches</figcaption>
</figure>

Flipping is one of the operations that cannot handle variable depth branches, simply because there is no logical solution to flip.

<figure>
   <img src="ads-242.png">
   <figcaption>Figure(74):  Flip fails when the input tree has variable depth branches</figcaption>
</figure>

### 3.5.7 Simplifying the data structure

Processing data through multiple components can add unnecessary complexity to the data structure. The most common form is adding leading or trailing zeros to the paths addresses. Complex data structures are hard to match. <b>Simplify Tree</b> process helps remove empty branches. There are other operations such as <b>Clean Tree</b> and <b>Trim Tree</b> to help remove null elements, empty branches and reduce complexity. It is also possible to extract all branches as separate lists using the <b>Explode Tree</b> operation.

<figure>
   <img src="ads-243.png">
   <figcaption>Figure(75): Paths can increase in complexity as more operations are applied to the data. Simplify helps remove empty branches</figcaption>
</figure>

<table class="rounded">
  <tr>
    <th>Tutorial 3.5.A Louvers</th>
  </tr>
  <tr>
  <tr>
    <td>
     Given one curve on XY-Plane, create horizontal and vertical louvers as in the image<br>
     <img src="ads-244.png" class="image_center" width="75%">
    </td>
    </tr>
  <tr>
    <td>
        <details>
        <summary><b>Solution...</b></summary>
        <br>
        <table>
          <tr>
            <td>
            Examine the <b>data structure</b> of output from each step before feeding it into the next process:<br>
            input curve data strucuture: Single item (one branch and one item in the branch)<br>
            <img src="ads-245.png">
            </td>
          </tr>
          <tr>
            <td>
            Divide input curve to extract points.<br>
            Data structure: List (one branch with 11 items). Note that the path has added leading “0”. This indicates the next layer of calculation.<br>
            <img src="ads-246.png">
            </td>
          </tr>
          <tr>
            <td>
            Create vertical lines at each point.<br>
            Data structure: List (one branch with 11 items). Note that the path did not increase in complexity.<br>
            <img src="ads-249.png">
            </td>
          </tr>
          <tr>
            <td>
            Divide vertical lines to create a grid of points.<br>
            Data structure: Tree (11 branches with 6 items). Note that the path has added leading “0”.<br>
            <img src="ads-248.png">
            </td>
          </tr>
          <tr>
            <td>
            Create horizontal lines at each point.<br>
            Data structure: Tree (11 branches with 6 items). Note that the path did not increase in complexity.<br>
            <img src="ads-247.png">
            </td>
          </tr>
          <tr>
            <td>
            Create lofted surfaces through branches of lines.<br>
            Data structure:Tree (11 branches with 1 item each). Note that the path did not increase in complexity.<br>
            <img src="ads-250.png">
            </td>
          </tr>
          <tr>
            <td>
            Flip the tree matrix and then create lofted surfaces through branches of lines.<br>
            Data structure: Tree (11 branches with 1 item each). Note that the path did not increase in complexity.<br>
            You can flatten the tree to create one list of horizontal louvers.<br>
            <img src="ads-251.png">
            </td>
          </tr>
        </table>
        </details>
    </td>
  </tr>
</table>

<table class="rounded">
  <tr>
    <th>Tutorial 3.5.B Shutters</th>
  </tr>
  <tr>
  <tr>
    <td>
     Given four corner points on a plane and a radius for the hinge, create a shutter that can open and shut as in the image using a rotation parameter<br>
     <img src="ads-252.png">
    </td>
    </tr>
  <tr>
    <td>
        <details>
        <summary><b>Solution...</b></summary>
        <br>
        <table>
          <tr>
            <td>
            <b>Algorithm analysis:</b><br>
            For each shutter there are two parts: the rectangle and the hinge.<br>
            Union the rectangle and hinge, then allow rotating around the hinge.<br>
            There is one rotation control to move all shutters together.<br>
            <img src="ads-253.png" class="image_center" width="75%"><br>
            </td>
          </tr>
          <tr>
            <td>
            <br><b>Solution steps:</b>
            </td>
          </tr>
          <tr>
            <td>
            Output: Surface of the shutters and curves for the frame<br>
            <img src="ads-254.png" class="image_center" width="50%">
            </td>
          </tr>
          <tr>
            <td>
            Input: The window four corner points (and center), the hinge radius and the rotation angle parameter<br>
            <img src="ads-255.png" class="image_center" width="75%">
            </td>
          </tr>
          <tr>
            <td>
            Key processe #1: create rectangle and hinges. Use the <b>Rectangle</b> component<br>
            <img src="ads-256.png" class="image_center" width="75%">
            </td>
          </tr>
          <tr>
            <td>
            Key processe #2: Union the curves. Use the <b>RUnion</b> component, then create a surface from the boundary using <b>Boundary</b> component<br>
            <img src="ads-257.png" class="image_center" width="75%">
            </td>
          </tr>
          <tr>
            <td>
            Intermediate process #1: Rotate the rectangles using the angle. Use <b>Rotate</b> component<br>
            <img src="ads-258.png" class="image_center" width="75%">
            </td>
          </tr>
          <tr>
            <td>
            Properly match the data structures of the rectangles and hinges before the region union. Use the <b>Graft</b> so that rectangles and hinges pair correctly.<br>
            <img src="ads-259.png" class="image_center" width="75%">
            </td>
          </tr>
          <tr>
            <td>
            <br><b>Putting it all together:</b>
            </td>
          </tr>
          <tr>
            <td>
            <img src="ads-260.png">
            </td>
          </tr>
        </table>
        </details>
    </td>
  </tr>
</table>

## 3.6 Advanced tree operations

As your solutions increase in complexity, so will your data structures. We will discuss three advanced tree operations that are necessary to solve specific problems, or are used to simplify your solution by tabbing directly into the power of the data tree structure.

### 3.6.1 Relative items

The first operation has to do with solving the general problem of connectivity between elements in one tree or across multiple trees. Suppose you have a grid of points and you need to connect the points diagonally. For each point, you connect to another in the +1 branch and +1 index. For example a point in branch {0}, index [0], connects to the point in branch {1}, index [1].

### 3.6.2 Split trees

LabLab

### 3.6.3 Path mapper

LabLab

## 3.7 Tutorials: advanced data structures

### 3.7.1 Sloped roof tutorial

LabLab

### 3.7.2 Diagonal triangles tutorial

LabLab

### 3.7.3 Zigzag tutorial

LabLab

### 3.7.4 Weaving tutorial

LabLab

## End of guide

This is part 3-3 of the [Essential Algorithms and Data Structures for Grasshopper](/guides/grasshopper/gh-algorithms-and-data-structures/).

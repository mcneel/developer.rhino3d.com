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

LabLab

## 3.3 Tree matching

LabLab

## 3.4 Traversing trees

LabLab

## 3.5 Basic tree operations

### 3.5.1 Viewing the tree structure

LabLab

### 3.5.2 List operations on trees

LabLab

### 3.5.3 Grafting from lists to a trees

LabLab

### 3.5.4 Flattening from trees to lists

LabLab

### 3.5.5 Combining data streams

LabLab

### 3.5.6 Flipping the data structure

LabLab

### 3.5.7 Simplifying the data structure

LabLab

## 3.6 Advanced tree operations

### 3.6.1 Relative items

LabLab

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

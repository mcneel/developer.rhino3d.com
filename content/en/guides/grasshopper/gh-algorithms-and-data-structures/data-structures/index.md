+++
aliases = [""]
authors = [ "rajaa" ]
categories = [ "Essentials Algorithms and Data Structures" ]
category_page = "guides/grasshopper/gh-algorithms-and-data/"
keywords = [ "data structures", "grasshopper" ]
languages = [ "" ]
sdk = [ "" ]
title = "Chapter 2: Introduction to Data Structures"
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

All algorithms involve processing input data to generate a new set of data as output. Data is stored in well-defined structures to help access and manipulate efficiently. Understanding these structures is the key for successful algorithmic designs. This chapter includes an in-depth review of the basic data structures in Grasshopper.<br>

## 2.1 Overview

Grasshopper has three distinct data structures: single item, list of items and tree of items. GH components execute differently based on input data structures, and hence it is essential to be fully aware of the data structure before using. There are tools in GH to help identify the data structure. Those are Panel and Param Viewer.

<figure>
   <img src="ads-100.png">
   <figcaption>Figure(34): Data structures in Grasshopper
</figcaption>
</figure>

Processes in GH execute differently based on the data structure. For example, the Mass Addition component adds all the numbers in a list and produces a single number, but when operating on a tree, it produces a list of numbers representing the sum of each branch.

<figure>
   <img src="ads-101.png">
   <figcaption>Figure(35): Components execute differently based on the data structures. Result of adding numbers from Figure(34)
</figcaption>
</figure>

The wires connecting the data with components in GH offer additional visual reference to the data structure. The wire from a single item is a simple line, while the wire connecting a list is drawn as a double line. A wire output from a tree data structure is a dashed double line. This is very useful to quickly identify the structure of your data.

<table class="rounded">
  <tr>
    <th>Display the data structure</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>
    <b>Item</b>: single branch with single item<br>
    Wire display: single line
    </td>
    <td>
    <img src="ads-102.png">
    </td>
  </tr>
  <tr>
    <td>
    <b>List</b>: single branch with multiple items<br>
    Wire display: double line
    </td>
    <td>
    <img src="ads-103.png">
    </td>
  </tr>
    <tr>
    <td>
    <b>Tree</b>: multiple branches with any number of items per branch<br>
    Wire display: double dashed line
    </td>
    <td>
    <img src="ads-104.png">
    </td>
  </tr>
</table

## 2.2 Generating lists

There are many ways to generate lists of data in GH. So far we have seen how to directly embed a list of values inside a parameter or a panel (with multiline data). There are also special components to generate lists. For example, to generate a list of numbers, there are three key components: <b>Range</b>, <b>Series</b> and <b>Random</b>. The Range component creates equally spaced range of numbers between a min and max values (called domain) and a number of steps (the number of values in the resulting list is equal to the number of steps plus one).

## 2.3 List operations

LabLab


## 2.4 List matching

LabLab

## 2.5 Tutorials: data structures

### 2.5.1 Variable thickness pipe tutorial

LabLab

### 2.5.2 Custom matching tutorial  

LabLab

### 2.5.3 Pearl necklace tutorial

LabLab

### 2.5.4 Pearl necklace tutorial

LabLab

## Next Steps

Those are the introduction to data structures. Next, learn [Advanced Data Structures](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/).

This is part 2-3 of the [Essential Algorithms and Data Structures for Grasshopper](/guides/grasshopper/gh-algorithms-and-data-structures/).

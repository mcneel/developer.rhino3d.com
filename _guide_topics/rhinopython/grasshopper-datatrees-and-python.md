---
title: Grasshopper data trees and Python
description: This guide describes how to use data trees in Python.
authors: ['giulio_piacentino']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/python
order: 2
keywords: ['Rhino.Python', 'Python']
layout: toc-guide-page
---

## Data trees, technically

The data tree data structure is a complex data structure that is best kept in Grasshopper realms. It is a .Net class that is part of the Grasshopper SDK and, as such, all its members can be found on the [DataTree class](http://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_DataTree_1.htm) Grasshopper SDK documentation site.

On the implementation side, in Python it can be thought as an object with behavior similar to a `dict` - really, [System.Collections.Generic.SortedList](https://msdn.microsoft.com/en-us/library/system.collections.sortedlist(v=vs.110).aspx) - of `GH_Path`s, or [Grasshopper.Kernel.Data.GH_Path](http://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Data_GH_Path.htm). For each one of the paths-keys inside, there is an associated [.Net list](https://msdn.microsoft.com/en-us/library/6sh2ey19(v=vs.110).aspx)-value, that is a branch. Items are stored in each list. There is no null-path, but paths can be sparse. Items cannot be sparse, but there can be null-items.

Other data structures would also be able to accommodate similar data. In Python, a similar object with better language support would be a list of lists.

```python
nested_list = [[0, 1], [2, 3]]
```
However, a list of lists cannot always represent the merging of two datatrees with different dimensional depth in data (example: a datatree with an item at {0;1}[0] and an item at {0}[1]). If the data tree is constructed by normal and integral Grasshopper logic, it will have constant dimensional depth, and therefore this problem can be avoided. Alternatively, the data tree with inferior dimension can be 'grafted' to a branch of an upper dimension, and also this way the problem is avoided.


## Coding against the DataTree class

This example shows how to iterate through any data tree and explain the content of it.

```python
a = []

for i in range(x.BranchCount):
    branchList = x.Branch(i)
    branchPath = x.Path(i)
    
    for j in range(branchList.Count):
        s = str(branchPath) + "[" + str(j) + "] "
        s += type(branchList[j]).__name__ + ": "
        s += str(branchList[j])
        
        a.append(s)
```

On the opposite side, this example shows how to create a data tree from scratch:

```python
import ghpythonlib.treehelpers as th
import Rhino

layerTree = [list() for _ in layernames]

for i in range(len(layernames)):
    objs = Rhino.RhinoDoc.ActiveDoc.Objects.FindByLayer(layernames[i])
    
    if objs:
        geoms = [obj.Geometry for obj in objs]
        layerTree[i].extend(geoms)

layerTree = th.list_to_tree(layerTree, source=[0,0])
a = layerTree
```

## A simpler way, coding against lists of lists

As mentioned under the first heading, when possible, it is easier to code against nested lists (lists of lists) in Python, to leverage this more ubiquitous programing paradigm.
The `ghpythonlib.treehelpers` module contains functions that transform trees to nested lists, and vice versa.

The first two examples can be translated to 

```python
import ghpythonlib.treehelpers as th

x = th.tree_to_list(x)

a = []

for i,branch in enumerate(x):
    
    for j,item in enumerate(branch):
        s = str(i) + "[" + str(j) + "] "
        s += type(item).__name__ + ": "
        s += str(item)
        
        a.append(s)
```

```python
import ghpythonlib.treehelpers as th
import Rhino

layerTree = []

for i in range(len(layernames)):
    objs = Rhino.RhinoDoc.ActiveDoc.Objects.FindByLayer(layernames[i])
    
    if objs:
        geoms = [obj.Geometry for obj in objs]
        layerTree.append(geoms)

layerTree = th.list_to_tree(layerTree, source=[0,0])
a = layerTree
```

## Complete sample

- [datatree_examples.gh]({{ site.baseurl }}/files/datatree_examples.gh)

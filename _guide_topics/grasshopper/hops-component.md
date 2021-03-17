---
title: Hops Component
description: Hops adds functions to Grasshopper.
authors: ['steve_baer', 'scott_davidson']
sdk: ['Grasshopper']
languages: ['Grasshopper']
platforms: ['Windows', 'Mac']
categories: ['In Depth']
origin:
order: 2
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
---

## Overview <img src="{{ site.baseurl }}/images/win-logo-small.png" alt="Windows" class="guide_icon"> 
{: #hops }

<img src="{{ site.baseurl }}/images/hops-overview.png">{: .img-center  width="100%"}

Hops is a new component for Grasshopper in Rhino 7. Hops adds functions to Grasshopper. Functions are defined in separate Grasshopper document. Like other programming languages, functions let you:

* Simplify complex algorithms by using the same function multiple times.
* Eliminate duplicate component combinations by placing common combinations in a function.
* Share Grasshopper documents with other team members.
* Reference Grasshopper documents across multiple projects.
* Solve external documents in parallel, potentially speeding up large projects.
 
Hops displays inputs and outputs that match a function specified. During calculation the component solves the definition in a separate process and then returns the outputs to the current document.

## How to use Hops <img src="{{ site.baseurl }}/images/hops.svg" alt="Windows" class="guide_icon"> 

### Install Hops using the Package Manager in Rhino 7:
  1. To install [Hops, click in this link](rhino://package/search?name=hops)
  1. Or, type `PackageManger` on the Rhino command line.
  1. Search for “Hops”
  1. Select Hops and then Install

<img src="{{ site.baseurl }}/images/hopsinstall.jpg">{: .img-center  width="80%"}

### Create a Hops Function

Hops functions are Grasshopper documents with special inputs and outputs.

<img src="{{ site.baseurl }}/images/hops-function.png">{: .img-center  width="100%"}

Hops inputs are Get components. The name of the component is used for the name the Hops input parameter.

<img src="{{ site.baseurl }}/images/hops-input.png">{: .img-center  width="40%"}

Available Get components are:

<img src="{{ site.baseurl }}/images/get-components.jpg">{: .img-center  width="80%"}

Hops outputs are geometry or primitive params in a group named: “RH_OUT:[name]”, where [name] is the name of the output parameter. In this case, the name of the output is “o”.

<img src="{{ site.baseurl }}/images/hops-output.png">{: .img-center  width="30%"}

### Use the Hops component

1. Place the Grasshopper Params Tab > Util Group > Hops component on the canvas.
1. Right-click the Hops Component, then click Path
1. Select a Hops Function.
1. The component will show the inputs and outputs.
1. Wire it up like any other component.

<img src="{{ site.baseurl }}/images/gh-hops-path.png">{: .img-center  width="100%"}

## Frequently asked Questions:

### Can Hops use other machines?

No, at this time Hops functions using the local machine.  Files can be stored at any location available to Windows.

### Can you nest hops functions within other functions?

Not at this time.

### Does it cost money to use Hops?

Hops it free to use.

### Can Hops be used with Grasshopper Player to make commands?

Yes, Hops functions can use Context Bake and Context Print components to create Rhino commands in Grasshopper Player..

### Does hops support parallel processing?

Yes, Hops by default will launch a parallel process for each branch of a datatree input stream. Also, by right-clicking on the component additional parallel threads can be created. (1 vs 6-pack)

### What inputs and output types does hops support? (It supports all common types, ask about other ones if you need them)

Hops passes standard Grasshopper data types (Strings, Numbers, Lines, etc...) For other datatypes such as images or EPW weather files use a string for the file name so that the external function might also read in the same file.

### Can plugin components run in Hops Functions?

Yes, all the installed Grasshopper plugins can run within a Hops Function.

### Can this be used for extremely long calculations within a function?

Yes, Hops will wait for all function calls to return before passing the outputs to the downstream components. 

### Can any existing component be run remotely?

All plugins and existing Grasshopper component can be run as a 

### Can the code for Hops be used in my C# or Python scripts?

Not at this time.  As of now you could embed custom C#or Python component within a function or before or after a Hops component. https://github.com/mcneel/compute.rhino3d/tree/master/src/compute.components

### What is hops performance?

We have not done extensive benchmarking on this. Any performance improvement comes from solving a complex calculation in parallel ; each solution is calculated at the same speed as in Rhino plus the overhead of making the calls to the external function. 

### How does Hops deal with DataTrees?

Standard datamatching rule apply to datatrees.  But Hops will spawn a new parallel thread for each branch of a tree

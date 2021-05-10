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

Hops is a component for Grasshopper in Rhino 7 for Windows. Hops adds external *functions* to Grasshopper. Like other programming languages, functions let you:

* Simplify complex algorithms by using the same function multiple times.
* Eliminate duplicate component combinations by placing common combinations in a function.
* Share Grasshopper documents with other team members.
* Reference Grasshopper documents across multiple projects.
* Solve external documents in parallel, potentially speeding up large projects.

Hops functions are stored as seperate Grasshopper documents. The Hops component will adapt its inputs and outputs to match the function specified. During calculation Hops solves the definition in a separate process, then returns the outputs to the current document.

## How to use Hops <img src="{{ site.baseurl }}/images/hops.svg" alt="Windows" class="guide_icon">

{% include vimeo_player.html id="537493812" %}

### Install Hops using the Package Manager in Rhino 7 for Windows:

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
1. Use the new component like any other Grasshopper component.

<img src="{{ site.baseurl }}/images/gh-hops-path.png">{: .img-center  width="100%"}

## Frequently asked Questions:

#### Can you nest hops functions within other functions?

Not at this time.

#### Does it cost money to use Hops?

Hops it free to use.

#### Can Hops be used with Grasshopper Player to make commands?

Yes, Hops functions can use Context Bake and Context Print components to create Rhino commands in Grasshopper Player.

#### Does hops support parallel processing?

Yes, Hops by default will launch a parallel process for each branch of a datatree input stream. Also, by right-clicking on the component additional parallel threads can be created. (1 vs 6-pack)

#### What inputs and output types does hops support? (It supports all common types, ask about other ones if you need them)

Hops passes standard Grasshopper data types (Strings, Numbers, Lines, etc...) For other datatypes such as images or EPW weather files use a string for the file name so that the external function might also read in the same file.

#### Can plugin components run in Hops Functions?

Yes, all the installed Grasshopper plugins can run within a Hops Function.

#### Can this be used for extremely long calculations within a function?

Yes, Hops will wait for all function calls to return before passing the outputs to the downstream components.

#### Can any existing component be run remotely?

All plugins and existing Grasshopper component can be run as a single component.

#### Can the code for Hops be used in my C# or Python scripts?

Not at this time.  As of now you could embed custom C# or Python component within a function or before or after a Hops component. https://github.com/mcneel/compute.rhino3d/tree/master/src/compute.components

#### What is hops performance?

We have not done extensive benchmarking on this. Any performance improvement comes from solving a complex calculation in parallel ; each solution is calculated at the same speed as in Rhino plus the overhead of making the calls to the external function.

#### How does Hops deal with DataTrees?

Standard datamatching rule apply to datatrees.  But Hops will spawn a new parallel thread for each branch of a tree

## Remote Machine Configuration

By default Hops will use the local computer to solve Grasshopper functions. It is possible to setup remote computers for Hops to call.

Remote machines must be running Windows and have Rhino installed on them.

**Configuring a remote machine as a Hops node:**

1. Install Rhino 7.5 or above on the remote computer.
1. Make sure Rhino runs and is properly licensed.
1. Get the very latest version of compute.geometry.exe. Either build it yourself or get build from our CI server at
https://ci.appveyor.com/project/mcneel/compute-rhino3d/branch/master/artifacts
1. Run compute.geometry.exe from an Adminirator Command Line with an address parameter. For example
'compute.geometry.exe -address http://192.168.1.6:6123'. 192.168.1.6 is your computer's address. The port can be any you want; but we tend to use values above 6000.
1. Note the IP address of the remote machine.

**To test the status of the remote machine:**

1. On another computer, open a browser and enter `http://192.168.1.6:6123/healthcheck`. Use the IP and port numbers entered in the above steps.

If you get the word "healthy" back, you are all set up.

### Setting up Hops to communicate with the remote machine
In the grasshopper preferences > Solver > Hops - Compute Server URLs enter the IP and port of each remote computer.  For the above example enter:
http://192.168.1.6:6123

**Video Tutorial:**

{% include vimeo_player.html id="537494700" %}

## Calling a CPython Server

Use Hops to call into CPython. Some advantages of this component:

1. Call into CPython libraries including Numpy and SciPy
1. Use some of the newest libraries available for CPython such as TensorFlow.
1. Create re-usable functions and parallel processing.
1. Supports real debugging modes including breakpoints.
1. Full support of Visual Studio Code.
1. Other applications and services that support a Python API can also use the libraries included here.  

### Getting started with CPython in Grasshopper.
This python module helps you create python (specifically CPython) functions and use them inside your Grasshopper scripts using the new *Hops* components.

**Required:**

1. [Rhino 7.4 or newer.](https://www.rhino3d.com/download/)
1. [CPython 3.8 or above](https://www.python.org/downloads/)
1. [Hops Component for Grasshopper](https://developer.rhino3d.com/guides/grasshopper/hops-component/)
1. [Visual Studio Code](https://code.visualstudio.com/) highly recommended

**Video Tutorial:**

{% include vimeo_player.html id="524032610" %}

This module can use its built-in default HTTP server to serve the functions as Grasshopper components, or act as a middleware to a [Flask](https://flask.palletsprojects.com/en/1.1.x/) app. It can also work alongside [Rhino.Inside.CPython](https://discourse.mcneel.com/t/rhino-inside-python/78987) to give full access to the [RhinoCommon API](https://developer.rhino3d.com/api/).

## Shortcut to a single Grasshopper Component

Hops can call into a single grasshopper component using the remote instance to solve it. This can be helpful if many parralel instances of the component would speed up a defintinion. Simply enter the name of the component

## Using Remote Services

Hops may call into other applications for results.  What is required on the other application is Hops protocol awarness.  An example of calling into a remote service the Hops component calling into CPython. These libraries can also be used in the Python API of other applciations and services. See the Cpython Example above. For details see the [ReadMe on GH Hops CPython project](https://github.com/mcneel/compute.rhino3d/tree/master/src/ghhops-server-py)

{% include vimeo_player.html id="537498238" %}

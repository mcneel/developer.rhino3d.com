---
title: Hops Component
description: Hops adds functions to Grasshopper.
authors: ['steve_baer', 'scott_davidson', 'andy_payne']
sdk: ['Compute']
languages: ['Grasshopper']
platforms: ['Windows', 'Mac']
categories: ['Hops']
origin:
order: 1
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
redirect_from: "/guides/grasshopper/hops-component/"
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
* Run asynchronously on long running calculations without blocking Rhino and Grasshopper interactions.

Hops functions are stored as separate Grasshopper documents. The Hops component will adapt its inputs and outputs to match the function specified. During calculation Hops solves the definition in a separate process, then returns the outputs to the current document.

## How to use Hops <img src="{{ site.baseurl }}/images/hops.svg" alt="Windows" class="guide_icon">

{% include vimeo_player.html id="537493812" %}

### Installing Hops for Windows:

There are a few ways to install hops on your machine.
  1. [Install Hops](rhino://package/search?name=hops) (This will launch Rhino)
  1. Or, type `PackageManager` on the Rhino command line.
      1. Then, search for “Hops”
      1. Select Hops and then Install

<img src="{{ site.baseurl }}/images/gh-hops-package-manager.png">{: .img-center  width="100%"}

### Create a Hops Function

Hops functions are Grasshopper documents with special inputs and outputs.

<img src="{{ site.baseurl }}/images/hops-function-3.png">{: .img-center  width="100%"}

#### Defining Inputs

Hops inputs are created using the **Get Components**. The available Get components in Grasshopper are found under *Params Tab > Util Group*:

<img src="{{ site.baseurl }}/images/hops-get-components.png">{: .img-center  width="60%"}

The name of the component is used for the name of the Hops input parameter. So, in the example above, we have three Get components with names A, B, and C. Each of these Get components become input parameters when Hops compiles the definition.

<img src="{{ site.baseurl }}/images/hops_inputs-2.png">{: .img-center  width="80%"}

Each Get component has a context menu (right-click) with various settings.

<img src="{{ site.baseurl }}/images/gh-hops-get-component-menu.png">{: .img-center  width="55%"}

* **Component Name** - This is the name that will be assigned to the input of the Hops component.
* **Prompt** - This input will be the tooltip that is displayed when you hover over this parameter on the Hops component.
* **Enable/Disable** - Enable or disable this component.
* **At Least** - This is only used for the Grasshopper Player and will define the minimum number of values to accept for this input.
* **At Most** - This will define the maximum number of values to accept for this input (Default = 1). If this value is set to 1, the Hops component will treat this input as *Item Access*. However, if this value is more than one (or unset) Hops will treat this input as *List Access*.
* **Minimum & Maximum** - These optional inputs are only used for the Grasshopper Player and will clamp numeric inputs to these bounds.
* **Presets** - This optional input is only used for the Grasshopper Player and are only found on the *String*, *Integer*, and *Number* Get components. This dialog allows you to set a list of predefined options which will be displayed to the user via the command line prompt.

#### Defining Outputs

Hops outputs are geometry or primitive params in a group named: “RH_OUT:[name]”, where [name] is the name of the output parameter. In this case, the name of the output is “o”.

<img src="{{ site.baseurl }}/images/hops_output.png">{: .img-center  width="80%"}

### Use the Hops component

1. Place the Grasshopper *Params Tab > Util Group > Hops component* onto the canvas.
1. Right-click the Hops Component, then click Path.
1. Select a Hops Function. Note: this can be a Grasshopper definition on your computer, on a remote computer, or a REST endpoint.
1. The component will show the inputs and outputs.
1. Use the new component like any other Grasshopper component.

<img src="{{ site.baseurl }}/images/gh-hops-path.png">{: .img-center  width="100%"}

### A note about Hops for macOS users

The Hops component works in tandem with a local instance of a [Rhino.compute](https://developer.rhino3d.com/guides/compute/) server which, typically, is spun up whenever you launch Grasshopper. However, this server will not run on macOS which means there are two other options for you to consider. You can:

1. make a REST API call to a remote server running on Windows.
1. make a REST API call to a python ghhops_server running locally.

The first option (making a call to a remote Windows server) will require some setup modifications to the remote machine. For more information on how to setup a remote server, checkout the section on [Remote Machine Configuration](https://developer.rhino3d.com/guides/grasshopper/hops-component/#remote-machine-configuration). 

The second option (making a call to a local python server) is covered in more detail in the section called [Calling a CPython Server](https://developer.rhino3d.com/guides/grasshopper/hops-component/#calling-a-cpython-server).

## Hops Settings

### Application Settings

The Hops settings control how Hops runs on an application level.  It is available through the Grasshopper File pulldown > Preferences.

<img src="{{ site.baseurl }}/images/gh-hops-preferences.jpg">{: .img-center  width="60%"}

* **Hops-Compute server URL** - List the IP address or URL of any remote machines or Compute servers.
* **Max Concurrent requests** - Used to limit the number of active requests in asynchronous situations. This way hops doesn't make thousands of requests while the original request is being processed.
* **Clear Hops Memory cache** - Clears all previously stored solutions from memory.
* **Hide Rhino.Compute Console Window** - Hops will solve in the background, but showing the window can be helpful for troubleshooting.
* **Launch Local Rhino.Compute at Start** - Use this for remote machines when Compute needs to start before any requests are sent.
* **Child Process Count** - Used to limit the number of requests for additional parallel processes. May want to set this to the number of cores available.

Note: As of Rhino version 7.13, the active model tolerances (ie. absolute distance and angle tolerances) are passed from Hops to the running instance of Rhino.compute as part of the JSON request.

### Component Settings

Right_click on the Hops component to select any number of options that control how Hops runs.

<img src="{{ site.baseurl }}/images/gh-hops-component-settings.png">{: .img-center  width="60%"}


* **Parallel Computing** - Pass each item to a new parallel node if available.
* **Path...** - Add the location of the GH function to be solved. This may be a file name, IP address or URL.
* **Show Input: Path** - Makes the Path an input on the component so Path can be set through the GH Canvas.
* **Show Input: Enabled** - Shows an Enabled input that runs the component based on a `True` or `False` Boolean value.
* **Asynchronous** - The user interface will not be blocked while waiting for a remote process to solve and the definition will be updated when the solve is complete.
* **Cache In Memory** - Previous solutions are stored in memory on the local machine to improve performance if the same inputs were previously calculated.
* **Cache On Server** - Previous solutions are stored on the remote server to improve performance. Currently available on Remote Hops services only.

## Remote Machine Configuration

By default Hops will use the local computer to solve Grasshopper functions. It is possible to setup remote computers for Hops to call.

Remote machines must be running Windows and have Rhino installed on them.

**Configuring a remote machine as a Hops node:**

1. Install Rhino 7.5 or above on the remote computer.
1. Make sure Rhino runs and is properly licensed.
1. Get the very latest version of compute.geometry.exe. Either build it yourself or get build from our CI server at
[https://ci.appveyor.com/project/mcneel/compute-rhino3d/branch/master/artifacts](https://ci.appveyor.com/project/mcneel/compute-rhino3d/branch/master/artifacts)
1. Run compute.geometry.exe from an Administrator Command Line with an address parameter. For example
'compute.geometry.exe -address http://192.168.1.6:6123'. 192.168.1.6 is your computer's address. The port can be any you want; but we tend to use values above 6000.
1. Note the IP address of the remote machine.

**To test the status of the remote machine:**

1. On another computer, open a browser and enter `http://192.168.1.6:6123/healthcheck`. Use the IP and port numbers entered in the above steps.

If you get the word "healthy" back, you are all set up.

### Setting up Hops to communicate with the remote machine
In the Grasshopper preferences > Solver > Hops - Compute Server URLs enter the IP and port of each remote computer.  For the above example enter:
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
1. The Hops component attempts to detect when inputs and outputs have changed on a server and will rebuild itself.  

### Getting started with CPython in Grasshopper

This Python module helps you create Python (specifically CPython) functions and use them inside your Grasshopper scripts using the new Hops components.

**Required:**

1. [Rhino 7.4 or newer.](https://www.rhino3d.com/download/)
1. [CPython 3.8 or above](https://www.python.org/downloads/)
1. [Hops Component for Grasshopper](https://developer.rhino3d.com/guides/grasshopper/hops-component/)
1. [Visual Studio Code](https://code.visualstudio.com/) highly recommended

**Video Tutorial:**

{% include vimeo_player.html id="524032610" %}

This module can use its built-in default HTTP server to serve the functions as Grasshopper components, or act as a middleware to a [Flask](https://flask.palletsprojects.com/en/1.1.x/) app. It can also work alongside [Rhino.Inside.CPython](https://discourse.mcneel.com/t/rhino-inside-python/78987) to give full access to the [RhinoCommon API](https://developer.rhino3d.com/api/).

## Frequently Asked Questions:

#### Can you nest Hops functions within other functions?

Yes, it is possible to nest Hops function within other functions. This is called _recursion_ and the default recursion limit is set to 10.

#### Does it cost money to use Hops?

Hops is free to use.

#### Can Hops be used with Grasshopper Player to make commands?

Yes, Hops functions can use Context Bake and Context Print components to create Rhino commands in Grasshopper Player.

#### Does Hops support parallel processing?

Yes, Hops by default will launch a parallel process for each branch of a datatree input stream.

#### What input and output types does Hops support? (It supports all common types, ask about other ones if you need them)

Hops passes standard Grasshopper data types (Strings, Numbers, Lines, etc...). For other datatypes such as images or EPW weather files use a string for the file name so that the external function might also read in the same file.

#### Can plugin components run in Hops Functions?

Yes, all the installed Grasshopper plugins can run within a Hops Function.

#### Can this be used for extremely long calculations within a function?

Yes, each Hops component has an option to solve asynchronously. The user interface will not be blocked while waiting for a remote process to solve and the definition will be updated when the solve is complete. Hops will wait for all function calls to return before passing the outputs to the downstream components.
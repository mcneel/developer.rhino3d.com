+++
aliases = ["/5/guides/compute/compute-javascript-getting-started/", "/6/guides/compute/compute-javascript-getting-started/", "/7/guides/compute/compute-javascript-getting-started/", "/wip/guides/compute/compute-javascript-getting-started/"]
authors = [ "scottd" ]
categories = [ "Getting Started", "Client" ]
description = "This guide covers all the necessary tools required to get started with the Rhino Compute Service through JavaScript."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "JavaScript" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Calling Compute with JavaScript"
type = "guides"
weight = 4
override_last_modified = "2020-11-12T13:14:51Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac", "Unix" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


By the end of this guide, you should have all the tools installed necessary for using the [Rhino Compute](https://www.rhino3d.com/compute) through JavaScript.

The libraries will run on on all major browsers as well as node.js.

## Setting up a Compute Project using JavaScript

There are a few client side tools which need to be referenced that are essential to communicate with the Compute server. These include:

- **rhino3dm.js** -  Is part of the Rhino3dm project.  It is a Javascript wrapper and web assembly (WASM) for [openNURBS](https://developer.rhino3d.com/guides/opennurbs/) which contains the functions to read and write Rhino Geometry Objects. 

- **compute-rhino3d.js** - This is a work in progress package which is meant to add classes available in RhinoCommon, but not available through rhino3dm.js. Compute-rhino3d makes calls into the McNeel Cloud Compute server for these functions. It handles all the transaction authorizations and JSON data conversion.

  ```
  <html>
    <!-- stuff -->
    <body>
      <script async type="text/javascript" src="https://files.mcneel.com/rhino3dm/js/latest/rhino3dm.js"></script>
      <script async type="text/javascript" src="https://files.mcneel.com/rhino3dm/js/latest/compute.rhino3d.js"></script>
      <!-- more stuff -->
    </body>
  </html>
  ```

## The first use of Compute

An example of using JavaScript to access compute can be found in the [Javascript Sample repo](https://github.com/mcneel/rhino3dm/tree/master/docs/javascript/samples) 

# Next Steps

*Congratulations!*  You have the tools to use [Rhino Compute server](https://www.rhino3d.com/compute).  *Now what?*

1. To see the transactional nature of Compute, read through [compute.rhino3d.js](https://files.mcneel.com/rhino3dm/js/latest/compute.rhino3d.js)
1. See a list of the [2400+ API calls](https://compute.rhino3d.com/sdk) available for compute.rhino3d.com.
1. Download the [Compute Samples repo from GitHub](https://github.com/mcneel/compute.rhino3d.samples).
1. The libraries are still very new and changing rapidly. Give them a try or get involved. Ask any questions or share what you are working on the [Compute Discussion Forum](https://discourse.mcneel.com/c/serengeti/compute-rhino3d)


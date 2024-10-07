+++
aliases = ["/en/5/guides/compute/compute-javascript-getting-started/", "/en/6/guides/compute/compute-javascript-getting-started/", "/en/7/guides/compute/compute-javascript-getting-started/", "/en/wip/guides/compute/compute-javascript-getting-started/"]
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

In a browser based application `index.html` would look like this:

  ```
  <html>
    <head>
    <!-- stuff -->
    </head>
    <body>
        <!-- Import maps polyfill -->
        <!-- Remove this when import maps will be widely supported -->
        <script async src="https://unpkg.com/es-module-shims@1.10.0/dist/es-module-shims.js"></script>

        <script type="importmap">
            {
                "imports": {
                    "rhino3dm":"https://unpkg.com/rhino3dm@8.4.0/rhino3dm.module.min.js",
                    "rhinocompute": "https://www.unpkg.com/compute-rhino3d@0.13.0-beta/compute.rhino3d.module.js"
                }
            }
        </script>

        <script type="module" src="./script.js"></script>
	</body>
</html>
  ```

  In the script.js, import the libraries:
  ```
  // Import libraries

import rhino3dm from 'rhino3dm'
import { RhinoCompute } from 'rhinocompute'

// Load rhino3dm
const rhino = await rhino3dm()
console.log('Loaded rhino3dm.')

// Your code ...

  ```

  For a node.js application, first install the libraries with npm:

  `npm i rhino3dm compute-rhino3d`

  Then reference them in your script:

  ```
  // Import libraries

  import rhino3dm from 'rhino3dm'
  import RhinoCompute from 'compute-rhino3d'

  // Load rhino3dm
  const rhino = await rhino3dm()
  console.log('Loaded rhino3dm.')

```

## The first use of Compute

Examples of using JavaScript to access compute can be found in the [Javascript Sample repo](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/js) 

# Next Steps

*Congratulations!*  You have the tools to use [Rhino Compute server](https://www.rhino3d.com/compute).  *Now what?*

1. To see the transactional nature of Compute, read through [compute.rhino3d.js](https://files.mcneel.com/rhino3dm/js/latest/compute.rhino3d.js)
1. See a list of the [2400+ API calls](https://compute.rhino3d.com/sdk) available for compute.rhino3d.com.
1. Download the [Compute Samples repo from GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute).
1. The libraries are still very new and changing rapidly. Give them a try or get involved. Ask any questions or share what you are working on the [Compute Discussion Forum](https://discourse.mcneel.com/c/serengeti/compute-rhino3d)


---
title: What is Hops?
description: This guide will help explain what Hops is all about and why you might want to use it.
authors: ['andy_payne']
sdk: []
languages: ['Grasshopper']
platforms: ['Windows', 'Mac']
categories: []
origin:
order: 1
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
---

In its most basic form, Hops is simply a client application for a rhino.compute server. I know, I've already lost you. But bear with me. Let's break that statement down a bit. 

### What is a Client?

A client is simply a hardware device (i.e., computer) or software application which makes a request for a digital resource from a server over a network connection. The client is designed for end-users to access resources such as files, videos, data or other computing resources.

For Hops, the client interface is simply the Hops component that you can find under the *Params Tab > Util Group* after you install Hops through the package manager. When you right-click on the Hops component and set the path to a Grasshopper file on your local machine, you are telling Hops to bundle up the data in that file and send a request to a Rhino.Compute server to solve that definition and return the results.
<img src="{{ site.baseurl }}/images/hops_hello_world3.png">{: .img-center  width="85%"}

### What is a Server?

 A server's sole purpose is to do what its name implies - serve its clients. It is usually a software application whose job is to receive and process incoming requests from a client and send an appropriate response. A server can be used to provide computing-intensive services to the client on demand and can be run on the same computer as the local client or on remote computer connected via a network.

 In the context of Hops, the server is an application which can process an incoming request and pass the relevant information to a headless version of Rhino. Headless simply means that there is no graphical interface that you can interact with (ie. viewports, toolbars, etc.). It's simply a bare-bones version of Rhino which can run commands or solve Grasshopper definitions. The headless version of Rhino solves the Grasshopper definition and then returns the result in the form of a http response.
 <img src="{{ site.baseurl }}/images/hops_server1.png">{: .img-center  width="70%"}

### Putting it all together

The communication process between Hops and Rhino.Compute is a little more nuanced than sending and receiving a single request and response. The first step in the process occurs when Hops bundles up the referenced Grasshopper definition and sends a http request to an endpoint on the server. An endpoint is simply a URL address where the server can be reached to perform a certain function. In this first request we need to ask the server to open the Grasshopper definition and determine what information we will need to populate the inputs and outputs for the Hops component. So, the endpoint will be called `/io` (short for Input Output).

<img src="{{ site.baseurl }}/images/hops_io_request.png">{: .img-center  width="100%"}

 At this point the Hops component should have enough information to create the necessary inputs and output nodes for itself. In this example, we have one input (cleverly called Input) which accepts some text value and one output (also aptly named as Output) which will return a text value.

<img src="{{ site.baseurl }}/images/hops_get_inputs.png">{: .img-center  width="75%"}

When all of the Hops inputs have been connected to source parameters, it will then send a new http request to the server only this time it will it will send the request to the `/solve` endpoint. We don't need to send the referenced Grasshopper definition again with this call, since this was already stored on the server during the `/io` process. Instead, the data sent in the `/solve` request contains a pointer ID which tells the server where to find the correct file. Additionally, the request contains the data passed into the input parameters so the server can use those values in the Grasshopper definition and return a result. This time, the http response from the server contains all data which would normally be returned from running the Grasshopper file locally.

<img src="{{ site.baseurl }}/images/hops_return_results.png">{: .img-center  width="70%"}

To have a better understanding of how each step above works, you can export the last request/response for both the `/io` and `/solve` endpoints directly from the Hops component.

<img src="{{ site.baseurl }}/images/hops_export_requests.png">{: .img-center  width="100%"}

### Why would you want to use Hops?

At this point you are probably wondering why you would want to use Hops when you can just solve a Grasshopper definition the old-fashioned way. Well, here are a few reasons you might consider.

* **Hops allows you to simplify complex definitions** by breaking them down into smaller "functions" - each of which can be solved by rhino.compute. A function, in the traditional sense of the word, is simply a self-contained module of code that usually takes in data, processes it, and returns a result.

    With Hops, you can break down large definitions into smaller groups of components which perform a specific function. If this function is used multiple times within a regular grasshopper definition, you can elimnate duplicate component combinations by referencing that function inside a Hops component and solving via Rhino.compute. Alternatively, if the function is commonly used among multiple projects, it can be shared and reused simply by referencing a file path.

* **Hops allows you to solve definitions in parallel**, potentially speeding up large projects. Rhino.compute can spin up or down as many headless versions of Rhino as needed (the default is 4 instances). Let's say you have a Grasshopper file which generates any number of permutations based on a set of inputs. You would like to see as many different options as possible so that you make the correct choice. You can configure Hops and Rhino.Compute to solve these definitions concurrently - dramatically improving the design decision making process.

* **Hops allows you to share Grasshopper definitions** with other team members and collaborators. Because Hops and Rhino.Compute are always connected via a network, they can access files on local network drives or on remote servers. This means that there can always be a single source of truth for a document. When this document is modified, all clients (ie. other Hops components who have referenced that file) are updated automatically.

* **Hops allows you to run calculations asynchronously** without blocking Rhino and Grasshopper interactions. Have you ever had a very large definition which takes seconds or even minutes to finish solving? If so, you probably noticed that the Rhino and Grasshopper interface locks up until the results are returned. This happens because Grasshopper is single threaded, and the calculations are being run on the same thread as the graphical interface. 

    Hops can be configured to run asynchronously. This means that it will send the request to the server with the long calculation that you intend to solve. However, the headless version of Rhino is running on a separate thread so it can continue working on the calculation without blocking the thread which controls the main Rhino and Grasshopper interface.
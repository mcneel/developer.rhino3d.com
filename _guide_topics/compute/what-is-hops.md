---
title: 
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
## What is Hops?

Have you ever stared at a large complex Grasshopper definition and marveled at the inscrutability of it all? Visual programming is notorious for its ability to quickly become an illegible, tangled, mess of code. In fact, this state of disogranization is often referred to as [Spaghetti Code](http://wiki.c2.com/?SpaghettiCode) or sometimes a [Big Ball of Mud](https://joeyoder.com/PDFs/mud.pdf) for obvious reasons. There are a number of factors which often contribute to the creation of spaghetti code including time constraints, the skill level of the programmer, or even project complexity - but after trying to decipher a big ball of Grasshopper spaghetti, there is but one universal truth:

> <h3 style="color:black; line-height: 1.3; margin-top: -5px;">Spaghetti code can make the task of understanding what the code actually does impractical or even impossible.</h3>

### Calling Functions in Grasshopper

So how do we begin to untangle this problem that has become so commonplace among Grasshopper developers? We begin by breaking down our spaghetti code into smaller reusable **functions**. In programming, a function is a "self-contained" module of code that usually takes in data, processes it, and returns a result. That sounds a lot like a Grasshopper definition. For example, Grasshopper definitions typically have inputs parameters like sliders, boolean toggles, or text which are fed through the graph to perform a series of actions, ultimately producing a result at the end. So, the key is to learn how to analyze a problem and break it down into smaller sub-definitions which we will use as functions. 

Say, for instance, that you needed to run a shadow analysis for a parametric tower you were designing for New York City. This problem could be broken down into four smaller tasks:
1. Create the building lot outline
1. Create the building envelope
1. Create the floor plates
1. Run the shadow analysis from the building enevlope and surrounding buildings

Once the tasks have been clearly defined, you can determine what information will be needed to perform each task (i.e., the inputs) and what data will be returned at the end (i.e., the outputs). So, for step 1, the inputs needed to generate the building lot outline would include site setbacks and other regulatory parameters from the building and zoning codes. The output for this function would likely include a polyline outlining the maximum building area at the ground floor. 

To define the parameters which will be used in a Grasshopper function, we should use the **Context Get** components for the inputs and the **Context Bake** component for all outputs. Each of these can be found under the *Params Tab > Util Group*.

<img src="{{ site.baseurl }}/images/hops_context_getters.png">{: .img-center  width="92%"}

Now that we have the inputs and outputs defined, all that is left is to fill in the steps to turn those inputs into outputs. Here is the interesting part. After a function has been fully defined as a Grasshopper definition - meaning it contains some inputs and outputs and performs a number of actions in between - we can simplify our project by calling that function through Hops. Hops takes that larger definition and bundles it into a single component, only exposing the inputs and outputs you defined inside your function. Unlike clusters, Hops lets you reference external files which can be saved locally or on a network drive - making it easy to share definitions among other team members and collaborators.

<img src="{{ site.baseurl }}/images/hops_ref_defintion.png">{: .img-center  width="100%"}

In summary, Hops enables you to dramatically increase the legibility of your code by simplifying complex definitions. In addition, it lets you share an reuse functions while eliminating duplicate component combinations which can be placed into a function. Hops also lets you solve functions in parallel, potentially speeding up large projects. And lastly, Hops lets you solve functions asynchronously without blocking Rhino and Grasshopper interactions.

## How does it work?

In its most basic form, Hops is simply a client application for a Rhino.Compute server. I know, I've already lost you. But bear with me. Let's break that statement down a bit. 

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
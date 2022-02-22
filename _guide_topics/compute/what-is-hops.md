---
title: What is Hops
description: This guide will help explain what Hops is all about and why you might want to use it.
authors: ['andy_payne']
sdk: ['Compute']
languages: ['Grasshopper']
platforms: ['Windows', 'Mac']
categories: ['Hops']
origin:
order: 1
keywords: ['developer', 'grasshopper', 'components', 'hops']
layout: toc-guide-page
---

Grasshopper definitions can be big, complicated, and repetitive. This state of disorganization is called [Spaghetti Code](https://www.pcmag.com/encyclopedia/term/spaghetti-code). Many factors contribute to spaghetti code: time constraints, programmer skill level, project complexity, and limitations in the programming language. After trying to decipher a big ball of Grasshopper spaghetti, there is one universal truth:

> <h4 style="color:black; line-height: 1.3; margin-top: -4px;">Spaghetti code is hard to read and understand!</h4>

### Calling Functions in Grasshopper

In programming, a **function** is a "self-contained" module of code that processes inputs and returns a result. Grasshopper definitions also process inputs and returns results. However, Grasshopper wasn’t written with functions in mind. Clusters sort of work, but don’t make it easy to reuse simple definitions in complex projects.

To fix this, the Hops component was added. Hops lets you use separate grasshopper definitions as functions. The key is learning to break a problem into smaller sub-definitions which we will use as functions.

Imagine that you needed to run a shadow analysis for a parametric tower you were designing for New York City. This problem could be broken down into four smaller tasks:
1. Create the building lot outline
1. Create the building envelope
1. Create the floor plates
1. Run the shadow analysis from the building enevlope and surrounding buildings

Once the tasks have been clearly defined, you can determine what information will be needed to perform each task (i.e., the inputs) and what data will be returned at the end (i.e., the outputs). For step 1, the inputs needed to generate the building lot outline would include site setbacks and other regulatory parameters from the building and zoning codes. The output for this function would likely include a polyline outlining the maximum building area at the ground floor. 

To define the parameters which will be used in a Grasshopper function, use the **Context Get** components for the inputs and the **Context Bake** component for the outputs. Each of these can be found under the *Params Tab > Util Group*.

<img src="{{ site.baseurl }}/images/hops_context_getters.png">{: .img-center  width="92%"}

Now that we have the inputs and outputs defined, all that is left is to fill in the steps to turn those inputs into outputs. After a function has been fully defined as a Grasshopper definition it can be called by Hops. Hops exposes the inputs and outputs you defined inside your function in the containing definition. Unlike clusters, Hops lets you reference external files which can be saved locally or on a network drive - making it easy to share definitions among other team members and collaborators.

<img src="{{ site.baseurl }}/images/hops_ref_defintion.png">{: .img-center  width="100%"}

Hops lets you  increase the legibility of your code by simplifying complex definitions, reducing duplication, and sharing and reusing functions. Hops lets you solve functions in parallel, potentially speeding up large projects. It also lets you solve functions asynchronously, without blocking Rhino and Grasshopper interactions.

## How it works?

Behind the scenes, the Hops client passes the Grasshopper definition you specify to a headless instance of Rhino and Grasshopper server.  

### The Hops Client

A client is a hardware device (i.e., computer) or software application which makes a request for a digital resource from a server over a network connection. 

The Hops component is the client. It can be found under the *Params Tab > Util Group* after you install Hops through the package manager. Hops needs the path or URL for the definition that it is going to solve.
<img src="{{ site.baseurl }}/images/hops_hello_world4.png">{: .img-center  width="55%"} 

Once you specify the definition, the component updates to show the inputs and outputs defined in the definition.
<img src="{{ site.baseurl }}/images/hops_io.png">{: .img-center  width="30%"} 

### The Rhino Server

A server serves data to its clients over a network connection. 

In the context of Hops, the server is  a headless (meaning it has no user interface to interact with) version of Rhino and Grasshopper. The headless Rhino server solves the Grasshopper definition sent from Hops and then returns the result.
<img src="{{ site.baseurl }}/images/hops_console.png">{: .img-center  width="100%"}

Hops optionally lets you point to a Rhino.Compute server running on another computer to solve the Grasshopper definitions. This lets you offload some or all of the solving to an external compute resource.

 ---

## Quick Links

 - [How Hops Works](../how-hops-works)
 - [The Hops Component](../hops-component)
 - [Setting up a Production Environment](../deploy-to-iis)

+++
authors = [ "andy.payne" ]
categories = [ "Hops" ]
keywords = [ "developer", "grasshopper", "components", "hops" ]
languages = [ "Grasshopper" ]
sdk = [ "Compute" ]
title = "How Hops Works"
type = "guides"
weight = 2
override_last_modified = "2022-02-18T10:08:37Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

The communication process between Hops and a Hops compliant server is a little more nuanced than simply sending and receiving a single http request and response. The first step in the process occurs when Hops bundles up the referenced Grasshopper definition and sends a http request to an endpoint on the server. 

An endpoint is a URL address where the server can be reached to perform a certain function. In this request, the server opens the Grasshopper definition sent from Hops and determines what information will be needed to populate the inputs and outputs for the Hops component. So, the endpoint will be called `/io` (short for Input Output).

{{< image url="/images/hops_io_request.png" alt="/images/hops_io_request.png" class="image_center" width="100%" >}}

The Hops component should now have enough information to create the necessary inputs and output nodes for itself. 

{{< image url="/images/hops_get_inputs.png" alt="/images/hops_get_inputs.png" class="image_center" width="75%" >}}

When all of the Hops inputs have been connected to source parameters, it will then send another http request to the server - only this time it will it will send the request to the `/solve` endpoint. The Grasshopper definition does not need to be resent since it was stored on the server during the `/io` process. Instead, the data sent in the `/solve` request only contains a pointer ID which tells the server where to find the correct file and all of the input data. 

The http response from the server contains all data which would be returned from running the Grasshopper file in the traditional manner.

{{< image url="/images/hops_return_results.png" alt="/images/hops_return_results.png" class="image_center" width="70%" >}}

To have a better understanding of how each step above works, you can export the last http request and response for both the `/io` and `/solve` endpoints directly from the Hops component.

{{< image url="/images/hops_export_requests.png" alt="/images/hops_export_requests.png" class="image_center" width="100%" >}}

 ---
 
## Quick Links

 - [What is Hops](../what-is-hops)
 - [The Hops Component](../hops-component)
 - [Setting up a Production Environment](../deploy-to-iis)
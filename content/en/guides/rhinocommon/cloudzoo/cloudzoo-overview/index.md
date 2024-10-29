+++
aliases = ["/en/5/guides/rhinocommon/cloudzoo/cloudzoo-overview/", "/en/6/guides/rhinocommon/cloudzoo/cloudzoo-overview/", "/en/7/guides/rhinocommon/cloudzoo/cloudzoo-overview/", "/en/wip/guides/rhinocommon/cloudzoo/cloudzoo-overview/"]
authors = [ "aj" ]
categories = [ "CloudZoo" ]
description = "This guide discusses all the steps needed to create RhinoCommon plugins that support Cloud Zoo."
keywords = [ "Plugin", "Cloud Zoo" ]
languages = "unset"
sdk = [ "RhinoCommon" ]
title = "Creating Plugins that use Cloud Zoo"
type = "guides"
weight = 1
override_last_modified = "2019-06-20T15:35:34Z"

[admin]
TODO = ""
origin = ""
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


## Overview

Add Cloud Zoo support to your Plug-In by following the steps below. Cloud Zoo allows Rhino users to add their license keys to their personal Rhino account or to a team composed of multiple Rhino accounts. The users may then login from any computer that has Rhino installed and run Rhino. Cloud Zoo enforces license restrictions by making sure that users can only run concurrently in as many computers as there are licenses for a specific product. This allows individual users to run Rhino and other Plug-Ins on any machine. In a team scenario, members can be anywhere in the world and have access to a license. 

Cloud Zoo does not require users to have a constant internet connection—only an occasional one every couple of weeks. This is possible because Cloud Zoo employs license lease mechanism wherein a lease--not a license itself--is issued by Cloud Zoo to a client running Rhino. A lease usually expires within a few weeks, but a new lease is frequently issued between Rhino and Cloud Zoo while a client is online. This allows for a buffer of a few weeks in case the computer is offline for extended periods of time. This design allows Rhino and other Plug-Ins to run reliably even in environments with poor internet connections. Cloud Zoo can also void a lease at any point in time. For example, when a license is removed by a user or by the developer (Such as when a customer returns a license for a refund), Cloud Zoo immediately voids all related leases, effectively ending the user's ability to use the software the license is intended for.

Under certain scenarios, such as when adding or removing a license, Cloud Zoo will contact your server to make sure you allow such operations to succeed. Your server is not required to interact with the license lease process.

![Cloud Zoo Overview](/images/cz-overview.png)

## Required Steps

To have your Plug-In support Cloud Zoo, you must:
 1. [Register as an Issuer in Cloud Zoo.](/guides/rhinocommon/cloudzoo/cloudzoo-issuer)
 2. [Add products to Cloud Zoo.](/guides/rhinocommon/cloudzoo/cloudzoo-add-products)
 3. [Implement the required HTTPS callbacks.](/guides/rhinocommon/cloudzoo/cloudzoo-implement-http-callbacks)
 4. [Modify Plug-In licensing code to support Cloud Zoo.](/guides/rhinocommon/cloudzoo/cloudzoo-modify-plugin-licensing-code)
 5. (*Optional*) [Take advantage of Cloud Zoo endpoints for querying and modifying licenses in Cloud Zoo.](/guides/rhinocommon/cloudzoo/cloudzoo-optional-endpoints)



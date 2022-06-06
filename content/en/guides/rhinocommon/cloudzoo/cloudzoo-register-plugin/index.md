+++
aliases = ["/5/guides/rhinocommon/cloudzoo/cloudzoo-register-plugin/", "/6/guides/rhinocommon/cloudzoo/cloudzoo-register-plugin/", "/7/guides/rhinocommon/cloudzoo/cloudzoo-register-plugin/", "/wip/guides/rhinocommon/cloudzoo/cloudzoo-register-plugin/"]
authors = [ "aj" ]
categories = [ "CloudZoo" ]
description = "This guide explains how to register yourself as an issuer in Cloud Zoo"
keywords = [ "Plugin", "Cloud Zoo" ]
languages = "unset"
sdk = [ "RhinoCommon" ]
title = "Register as an Issuer in Cloud Zoo"
type = "guides"
weight = 2
override_last_modified = "2021-05-13T09:15:01Z"

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

In Cloud Zoo, an _issuer_ represents a vendor of products with license keys. If you want your plugin to use Cloud Zoo, you must register to be an issuer by emailing [will@mcneel.com](mailto:will@mcneel.com). You will be provided with an issuer id and a secret that will uniquely identify you as a product vendor and will allow you to implement the required HTTPS callbacks.

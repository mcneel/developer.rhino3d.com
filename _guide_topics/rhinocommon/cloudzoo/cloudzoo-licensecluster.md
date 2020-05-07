---
title: Cloud Zoo License Cluster Object
description: A License Cluster object is a JSON object that represents a list of License objects for a software product issued by a registered issuer in Cloud Zoo. 
authors: ['aj']
sdk: ['RhinoCommon']
languages: unset
platforms: ['Windows', 'Mac']
categories: ['CloudZooDoc']
origin: unset
order: 1
keywords: ['Plugin', 'Cloud Zoo']
layout: toc-guide-page
---


## Structure

    {
		"licenses": [ONE OR MORE LICENSE OBJECTS]
	}

## Description

-   `licenses` - An array of one or more [License objects]({{ site.baseurl }}/guides/rhinocommon/cloudzoo/cloudzoo-license).

## When should I cluster licenses?

Under normal circumstances, a License Cluster contains a single [License object]({{ site.baseurl }}/guides/rhinocommon/cloudzoo/cloudzoo-license) in its `licenses` array. However, particularly when dealing with upgrades, clustering multiple related licenses may be useful. 

For example, consider a hypothetical Plug-In called *3D Donuts*. There are licenses for *3D Donuts* version 1, and licenses for *3D Donuts* version 2. 

The *Donuts* software license agreement can describe one of the following three scenarios:

 1. *After upgrading to version 2, users can run version 1 and version 2, but not concurrently.*
 
	 In this scenario, it makes sense to cluster the version 1 license and the version 2 license. To do this, simply return a license cluster with both License objects. Cloud Zoo will automatically replace the existing version 1 license cluster with the new one passed. Users now have a single seat (Unless `numberOfSeats` is greater than 1) to share between version 1 and version 2. If the licenses in the cluster have an expiration date, the `exp` field of the first license in the array will be assumed to be the expiration date for all licenses. Similarly, the `numberOfSeats` field of the first license will apply to all licenses in the cluster, regardless of the value of their `numberOfSeats` field.
	 
 2. After upgrading to version 2, users can run version 1 and
    version 2 concurrently. 

	In this scenario, it is advisable not to cluster licenses, but to treat them independent of each other--even if the version 1 license is required initially to add the version 2 license. Users will be able to run version 1 and version 2 concurrently.
	 
3. After upgrading to version 2, users can no longer run
    version 1.

	This scenario is similar to scenario #2, but after adding a license, the issuer must manually call the [DELETE endpoint]({{ site.baseurl }}/guides/rhinocommon/cloudzoo/cloudzoo-optional-endpoints#delete-license) to remove version 1 from an entity. 



---
title: Rhino Compute Service with Python
description: This guide covers all the necessary tools required to get started with the Rhino Compute Service using Python.
authors: ['scott_davidson']
sdk: ['RhinoCommon', 'Compute']
languages: ['Python']
platforms: ['Windows', 'Mac', 'Unix']
categories: ['Getting Started']
origin:
order: 2
keywords: ['first', 'RhinoCommon', 'Plugin', 'compute']
layout: toc-guide-page
---


By the end of this guide, you should have all the tools installed necessary for using the [Rhino Compute Service](https://www.rhino3d.com/compute) through Python.

This guide presumes you have Python installed on the platform:

- Python 2.7 - Windows (32 and 64 bit)
- Python 3.7 - Windows (32 and 64 bit)
- Python 2.7 - OSX (installed through homebrew)
- Python 3.7 - OSX (installed through homebrew)
- Linux and other python versions are supported through source distributions on PyPi

---

## Setting up a Compute Project in Python

There are a few client side tools which need to be installed in Python that are essential to communicate with the Compute server. These include:

- **rhino3dm.py** -  This is the part of the [Rhino3dm libraries](https://github.com/mcneel/rhino3dm).  It is a Python wrapper for [OpenNurbs](https://developer.rhino3d.com/guides/opennurbs/) which contains the functions to read and write Rhino Geometry Objects. This is available as a Pip package.

  `pip install rhino3dm`

- **compute-rhino3d.py** - This is a work in progress package which is meant to add classes available in [RhinoCommon](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/), but not available through rhino3dm.py. Compute-rhino3d makes calls into the McNeel Cloud Compute server for these functions. It handles all the transaction authorizations and JSON data conversion.

  `pip install compute-rhino3d`

## The first use of Compute

An example of using Python to access compute can be found in the [MakeMesh example](https://github.com/mcneel/rhino3dm/blob/master/samples/python/makemesh.py).

Please note that the compute Python calls are made through the `compute_rhino3d.py` package using a `_`  (underbar) and not a `-` (dash).

# Next Steps

*Congratulations!*  You have the tools to use [Rhino Compute server](https://www.rhino3d.com/compute).  *Now what?*

1. To see the transactional nature of Compute, read through **compute.rhino3d.py**
1. See a list of the [2400+ API calls](https://compute.rhino3d.com/sdk) available for compute.rhino3d.com.
1. Download the [Compute Samples repo from GitHub](https://github.com/mcneel/compute.rhino3d.samples).
1. The libraries are still very new and changing rapidly. Give them a try or get involved. Ask any questions or share what you are working on the [Compute Discussion Forum](https://discourse.mcneel.com/c/serengeti/compute-rhino3d)

---


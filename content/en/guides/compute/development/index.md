+++
authors = [ "brian", "will" ]
categories = [ "Getting Started", "Development" ]
description = "Deploy Compute for Production"
keywords = [ "developer", "compute", "production" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Running and Debugging Compute Locally"
type = "guides"
weight = 2

[admin]
TODO = "needs editing"
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

How to develop Compute on your Windows 10 computer.

1. [Download](https://www.rhino3d.com/download/rhino-for-windows/7/latest) and install Rhino 7.
1. Start Rhino at least once to configure its license.
1. Clone the [compute.rhino3d](https://github.com/mcneel/compute.rhino3d) repository from GitHub.
1. Open `src\compute.sln` in Visual Studio 2019 and compile as `Debug`.
1. Make sure that `compute.geometry` is set as the startup project.
1. Start the application in the debugger.
1. Wait for Compute to load... ☕️

    ![compute.geometry.exe](/images/compute_geometry_screenshot.png)

1. Browse to [http://localhost:8081/version](http://localhost:8081/version) to check that it's working!

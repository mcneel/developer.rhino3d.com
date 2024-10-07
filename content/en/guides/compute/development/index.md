+++
aliases = ["/en/5/guides/compute/development/", "/en/6/guides/compute/development/", "/en/7/guides/compute/development/", "/en/wip/guides/compute/development/"]
authors = [ "pedro" ]
categories = [ "Getting Started", "Development" ]
description = "Deploy Compute for Production"
keywords = [ "developer", "compute", "production" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Running and Debugging Compute Locally"
type = "guides"
weight = 2
override_last_modified = "2024-05-13T15:49:48Z"

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

Rhino.Compute allows you to bring the Rhino's geometric computation capabilities to the cloud. Before deploying your application to a production environment, you should ensure that everything works perfectly in a controlled environment.

This guide is intended for developers who are familiar with Windows and have basic knowledge of [Visual Studio](https://visualstudio.microsoft.com/downloads/) and [Git](https://git-scm.com/downloads). Whether you are a seasoned Rhino user or new to Rhino.Compute, this documentation will provide you with the necessary steps to set up your development environment and start debugging effectively.

## Prerequisites

Before diving into the setup of Rhino.Compute on your local machine, you need to ensure that you have the right tools. Here’s what you'll need:

- Windows Operating System. Rhino.Compute only runs in Windows.
- Development Environment. You will need [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) to compile the code.
- Version control. [Git](https://git-scm.com/downloads) is necessary for cloning the compute.rhino3d repository and managing branches according to your Rhino version.
- Rhino. Visit our downloads page to get the latest [Rhino 8](https://www.rhino3d.com/download/rhino-for-windows/8/latest) or [Rhino 7](https://www.rhino3d.com/download/rhino-for-windows/7/latest) builds. After downloading and installing it, please start Rhino and follow the instructions at startup to validate your license on your machine or through the Cloud Zoo.

{{< call-out "note" "Note" >}}
You will need to run the specific version of Rhino.Compute according to the Rhino version you installed. In the next section, you will clone the source code from the compute.rhino3d repository. If you have installed Rhino 8 on your machine, you will need to make sure you clone the 8.x branch. Alternatively, if you installed Rhino 7, make sure to clone the 7.x branch.
{{< /call-out >}}

## Clone the repository

To get the latest version of Rhino.Compute you will need to clone its [repository](https://github.com/mcneel/compute.rhino3d) from our official account in Github.

1. Go to [https://github.com/mcneel/compute.rhino3d](https://github.com/mcneel/compute.rhino3d)

1. From the branch drop-down menu, make sure you select either the 8.x or 7.x branch to clone.

1. Once there, click on the green button "<> Code" and copy the URL for the repository.
![compute_geometry_clone](/images/compute_geometry_clone.png)

1. On your local computer, create a folder where you want to clone the repository into.

1. Navigate to that directory through your preferred command prompt and type `git clone` and paste the URL you copied earlier.
    ```python
    git clone https://github.com/mcneel/compute.rhino3d.git
    ```
1. After the cloning operation is complete, you should see a number of files and directories which have be downloaded from the compute.rhino3d repository into the folder you created.

## Anatomy of the solution

The Rhino.Compute repository consists of two main projects, each serving distinct purposes within the framework. Understanding these can help clarify how Rhino.Compute operates, especially if you're looking to work with or contribute to its development. Here's a breakdown of the two projects:

- **compute.geometry**. This project primarily focuses on the geometric calculation aspects. Esentially, compute.geometry provides a REST API that exposes Rhino's geometry engine to be used over the web. This means that geometric operations can be performed on a server, and results can be retrieved remotely, making it highly useful for web-based applications or serices that require complex geometric processing.

- **rhino.compute**. This project can thought of as a higher-level service layer that manages and orchestrates the calls to the compute.geometry API - handling tasks like authentication, spawning child processes, and setting up time limits for the shutting down process.

## Compile the solution

Now that you have the code, it's time to open the project in Visual Studio 2022 and prepare it for debugging.

1. Navigate to the directory where you cloned the repository and find the **compute.sln** file. Double-click it to open the project in Visual Studio 2022.

1. Set the solution configuration to **Debug** mode. This allows you to run the code with full debugging features, making it easier to trace through the code and spot errors.
![compute_geometry_vs_debug](/images/compute_geometry_vs_debug.png)

1. In the File menu, click on Build -> Build Solution (Ctrl + Shift + B). This will compile all of the project files.
![compute_geometry_vs_build](/images/compute_geometry_vs_build.png)

1. In the Solution Explorer panel, right-click on the **rhino.compute** project and select **Set as Startup Project**. This ensures that when you run the debugger, Visual Studio will start this particular project.
![compute_geometry_vs_startup](/images/compute_geometry_vs_startup.png)

1. Click on **rhino.compute** to start the application in the debugger. A console application should show up in your task bar showing the status of the Rhino.Compute loading process.
![compute_geometry_vs_run](/images/compute_geometry_vs_run.png)

1. Now all you need to do is wait for a few seconds for Rhino.Compute to load. Please take into account that the logged information depends on the Rhino version you had chosen previously.
![compute.geometry.exe](/images/compute_geometry_screenshot.png)

## Test an endpoint

With the Rhino.Compute console application running, browse to any of these endpoints to check that everything is working!
- [http://localhost:6500/version](http://localhost:6500/version)
- [http://localhost:6500/healthcheck](http://localhost:6500/healthcheck)
- [http://localhost:6500/activechildren](http://localhost:6500/activechildren)
- [http://localhost:6500/sdk](http://localhost:6500/sdk)
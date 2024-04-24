+++
aliases = ["/5/guides/compute/development/", "/6/guides/compute/development/", "/7/guides/compute/development/", "/wip/guides/compute/development/"]
authors = [ "pedro" ]
categories = [ "Getting Started", "Development" ]
description = "Deploy Compute for Production"
keywords = [ "developer", "compute", "production" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Running and Debugging Compute Locally"
type = "guides"
weight = 2
override_last_modified = "2020-11-26T15:49:48Z"

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

Rhino.Compute allows you to bring the Rhino's geometric computation capabilities to the cloud. But before deploying your application to production, you should ensure that everything works perfectly in a controlled environment. 

This guide is intended for developers who are familiar with Windows and have basic knowledge of Visual Studio and Git. Whether you are a seasoned Rhino user or new to Rhino.Compute, this documentation will provide you with the necessary steps to set up your development environment and start debugging effectively.

## Rerrequisites
Before diving into the setup of Rhino.Compute on your local machine, you need to ensure that you have the right tools and environment ready. Here’s what you'll need:
- Operating System. Rhino.Compute only runs in Windows.
- Development Environment. You will need [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) to compile the code.
- Version control. [Git](https://git-scm.com/downloads) is necessary for cloning the compute.rhino3d repository and managing branches according to your Rhino version.
- Rhino. Visit our downloads page to get the latest [Rhino 7](https://www.rhino3d.com/download/rhino-for-windows/7/latest) or [Rhino 8](https://www.rhino3d.com/download/rhino-for-windows/7/latest). After downloading and installing it, please start Rhino and follow the instructions to validate your code on your machine or through Cloud Zoo.

{{< call-out "note" "Note" >}}
You will need to run the specific version of Rhino.Compute according to the Rhino you installed..
{{< /call-out >}}

## Clone the repository
To get the latest version of Rhino.Compute you will need to clone its [repository](https://github.com/mcneel/compute.rhino3d) from our official account in Github.

Once there, click on the green button "<> Code" and copy the URL for the repository.
![compute_geometry_clone](/images/compute_geometry_clone.png)

On you local computer, create a folder where you want to clone the repository, navigate to there through your preferred command prompt, type `git clone` and paste the URL you copied earlier.

```python
git clone https://github.com/mcneel/compute.rhino3d.git
```

## Compile the solution
Now that you have the code, it's time to open the project in Visual Studio 2019 and prepare it for debugging.

- Open the Solution: Navigate to the directory where you cloned the repository, and find the `compute.sln` file. Double-click it to open the project in Visual Studio 2022.

- Compile as Debug: Set the solution configuration to `Debug` mode. This allows you to run the code with full debugging features, making it easier to trace through the code and spot errors.


![compute_geometry_vs_debug](/images/compute_geometry_vs_debug.png)

- Set `compute.geometry` as the Startup Project: In the Solution Explorer, right-click on the compute.geometry project and select `Set as Startup Project`. This ensures that when you run the debugger, Visual Studio will start this particular project.


![compute_geometry_vs_startup](/images/compute_geometry_vs_startup.png)

- Select the branch according to your Rhino software (7.x or 8.x)


![compute_geometry_vs_branch](/images/compute_geometry_vs_branch.png)

- Click on `compute_geometry` to start the application in the debugger.


![compute_geometry_vs_run](/images/compute_geometry_vs_run.png)

- Now all you need to do is wait for a few seconds to have Rhino.Compute completely loaded. Please take into account that the logged information depends on the Rhino version you had chosen previously.


![compute.geometry.exe](/images/compute_geometry_screenshot.png)

## Test an endpoint
Browse to the version endpoint to check that everything is working fine! Note that the port is different according with the Rhino.Compute version you are running.
- Rhino.Compute branch 7.x. [http://localhost:8081/version](http://localhost:8081/version).
- Rhino.Compute branch 8.x. [http://localhost:5000/version](http://localhost:5000/version).
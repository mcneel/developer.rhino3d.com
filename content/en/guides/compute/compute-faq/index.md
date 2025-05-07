+++
aliases = ["/en/5/guides/compute/compute-faq/", "/en/6/guides/compute/compute-faq/", "/en/7/guides/compute/compute-faq/", "/en/wip/guides/compute/compute-faq/", "/en/guides/compute/faq/"]
authors = [ "andy.payne" ]
categories = [ "Getting Started" ]
description = "This guide is a list of Frequently Asked Questions (FAQ) for Rhino.Compute."
keywords = [ "developer", "compute", "faq" ]
languages = []
sdk = [ "Compute" ]
title = "Frequently Asked Questions"
type = "guides"
weight = 1
override_last_modified = "2025-05-07T09:45:21Z"

[admin]
TODO = ""
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

## General

**What is Rhino.Compute?**

In its simplest definition, Rhino.Compute is a web server that can perform geometry calculations using Rhino's geometry library (i.e. [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/)). It works by receiving requests over the web (using [HTTP](https://en.wikipedia.org/wiki/HTTP) or [HTTPS](https://en.wikipedia.org/wiki/HTTPS)), processing them with Rhino’s geometry engine, and then sending back the results. Any application that can send web requests can interact with Rhino.Compute, making it easy to integrate into different workflows.

**Why would I want to use it?**

Rhino.Compute lets you use Rhino’s powerful tools and features outside of the regular Rhino or Grasshopper interface. It’s great for teams, because you can run Grasshopper definitions or Rhino functions from one central place, making collaboration easier. It can also handle multiple tasks at the same time (in parallel), helping speed up large projects. And for longer calculations, it runs in the background (asynchronously) — so it won’t freeze or slow down your main interface.

**Will it work on macOS?**

No. Rhino.Compute is dependent on [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/) which allows Rhino and Grasshopper to run *inside* other 64-bit applications. Currently, Rhino.Inside is only compatible with the Windows operating system.

**Does it cost money?**

The short answer is: it depends on *where* you run Rhino.Compute. If you're using it on a regular Windows computer, like your personal PC, there’s no extra cost. Rhino.Compute will check for your standard Rhino licence on startup (note: [Rhino evaluation versions](https://www.rhino3d.com/download/) will work just fine). But if you're running it on a Windows Server (such as a virtual machine in the cloud), you’ll be charged based on our [Core-Hour Billing](../core-hour-billing/) model.

**How is it different from Hops?**

[Hops](../what-is-hops/) is a Grasshopper plugin (available from the [package manager](../../yak/what-is-yak/)) that makes it easy to solve Grasshopper definitions using Rhino.Compute. When you install Hops, it automatically starts an instance of Rhino.Compute in the background whenever you open Grasshopper. You can then use the Hops component to send your Grasshopper definition to Rhino.Compute, which solves it and sends the results back. In this context, Hops is the “client” and Rhino.Compute is the “server.”

**Can I make my own interface to work with Rhino.Compute?**

Yes. As mentioned earlier, any app that can send web requests can work with Rhino.Compute. To make things easier, we offer three libraries you can use depending on the language you prefer:
1. [Python Rhino.Compute Library](https://pypi.org/project/compute-rhino3d/)
1. [Javascript Rhino.Compute Library](https://www.npmjs.com/package/compute-rhino3d)
1. [.NET (C#) Rhino.Compute Library](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs)

We also have step-by-step guides to help you get started with the libraries above:
1. [Calling Compute with Python](../compute-python-getting-started/)
1. [Calling Compute with Javascript](../compute-javascript-getting-started/)
1. [Calling Compute with .NET](../compute-net-getting-started/)

Finally, we have a [GitHub repository](https://github.com/mcneel/rhino-developer-samples/tree/8/compute) with lots of sample projects and examples that show how to use Rhino.Compute for different geometry tasks.

**Can I use Rhino.Compute in a production environment?**

Yes. We offer a [step-by-step guide](../deploy-to-iis/) to help you set up Rhino.Compute in a production environment, such as on a virtual machine (VM). The setup is straightforward—just run a simple PowerShell script, and Rhino.Compute will be up and running, ready to handle requests.

## Troubleshooting

We’ve worked hard to make Rhino.Compute as easy to use as possible. But sometimes things don’t go as planned. This section is here to help you troubleshoot and solve any issues you might run into.

**Where can I find the log files?**

If you are running Rhino.Compute with Hops, you will want to make sure that the Rhino.Compute console application is visible whenever it starts up. To do this, follow the following steps:
1. Launch Grasshopper
1. Click on **File -> Preferences** to open the Grasshopper Settings dialog
1. Click on the **Solver** tab in the left-hand menu
1. **Uncheck** the Hide Rhino.Compute Console Window menu item
1. Restart Rhino and Grasshopper 

{{< image url="/images/hops-preferences-1.png" alt="/images/hops-preferences-1.png" class="image_center" width="75%" >}}

At this point, you should see a new application appear in your task bar (if you are using Windows) when you start Grasshopper. This is the Rhino.Compute console application. Useful troubleshooting information will be displayed here as you are working with Rhino.Compute.

{{< image url="/images/hops-console-2.png" alt="/images/hops-console-2.png" class="image_center" width="100%" >}}

<br>
If you are running Rhino.Compute on a VM, then the log files are saved as text files. New log files will be created daily. By default, the log files are saved under the following location: 

```markdown
C:\inetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute\logs\
```

**Can I enable more verbose logging information?**

By default, Rhino.Compute outputs a minimal set of information to the logs. To enable more verbose logging you will need to create an environment variable on your machine.

1. Right-click on the **This PC** icon in the File Explorer, then select **Properties** or **System** from the Control Panel
1. In the System Properties window, click on **Advanced System Settings**
1. In the **Advanced** tab, click on **Environment Variables**
1. Click on the **New** button to create a new system variable
1. In the **Variable name** input, type "RHINO_COMPUTE_DEBUG"
1. In the **Variable value** input, type "true"
1. Click OK to save the system environment variable, and then click OK again to close the Environment Variables dialog box and the System Properties window.

**What do I do if I get an HRESULT E_FAIL Error?**

If Rhino.Compute returns the following error:

```cs
Application startup exception
System.Runtime.InteropServices.COMException (0x80004005): Error HRESULT E_FAIL has been returned from a call to a COM component.
   at Rhino.Runtime.InProcess.RhinoCore.InternalStartup(Int32 argc, String[] argv, StartupInfo& info, IntPtr hostWnd)
```

This is most likely caused because Rhino.Compute can not find a valid license on startup. If you are running a Windows Server based machine (i.e. on a virtual machine) then follow these steps:

1. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) and select the team that you set up with Core-hour billing.
1. Click **Manage Team -> Manage Core-Hour Billing**.
1. Click **Action -> Get Auth Token** to get a token.
1. Create a new environment variable with the name `RHINO_TOKEN` and use the token as the value. Since the token is too long for Windows' Environment Variables dialog, it's easiest to do this via a PowerShell command.

```ps
[System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'your token here', 'Machine')
```

From now on, when you start Rhino on this machine it will use your core-hour billing team.

{{< call-out "warning" "Warning" >}}
<strong>Warning!</strong> Your core-hour billing token allows anyone with it to charge your team at will. Do <strong>NOT</strong> share this token with anyone.
{{< /call-out >}}

**I'm getting a 401 Error message. What does that mean?**

If Rhino.Compute gives you a 401 error, it means the request wasn’t authorized. This usually happens when the request is missing an API key. Rhino.Compute checks for this key—which is saved as an environment variable on the machine it's running on—to make sure only approved clients can connect.

If you are using Hops, you can set the API key in the preferences section.

1. Launch Grasshopper
1. Click on **File -> Preferences** to open the Grasshopper Settings dialog
1. Click on the **Solver** tab in the left-hand menu
1. **Enter the API key** in the input dialog
1. Restart Rhino and Grasshopper

{{< image url="/images/hops-api-key.png" alt="/images/hops-api-key.png" class="image_center" width="75%" >}}

<br>
If you're sending a web request to Rhino.Compute using a different method, make sure to include a key/value pair in the header of the request. The key should be named "RhinoComputeKey", and its value must match the API key set on the machine running Rhino.Compute.

**What does a 500 error code mean?**

If you receive a response from Rhino.Compute containing a 500 error code, this means that the server is malfunctioning and is unable to process the request correctly. If this happens, you may need to try to run Rhino.Compute in debug mode to get further information as to why the server is failing. [Follow this guide](../development/) to learn how to run Rhino.Compute in debug mode.

**What do I do if I get a timeout exception?**

If Rhino.Compute returns the following error:

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Connection id "...", Request id "...": An unhandled exception was thrown by the application.
      System.Threading.Tasks.TaskCanceledException: The request was canceled due to the configured HttpClient.Timeout of 100 seconds elapsing.
```

An HTTP request timeout occurs when a client (like Hops) doesn't receive a response from a server (like Rhino.Compute) within a specified amount of time. Thus there are two timeout values that we should be aware of: 1) the client timeout and 2) the server timeout.

The timeout setting you see in the Hops preferences controls the client-side timeout. The default value is 100 seconds, but this can be extended to alleviate this error.

{{< image url="/images/hops-timeout.png" alt="/images/hops-timeout.png" class="image_center" width="75%" >}}

The server-side timeout is managed separately — it's set by an environment variable on the machine running the server. To set the environment variable follow these steps:

1. Right-click on the **This PC** icon in the File Explorer, then select **Properties** or **System** from the Control Panel
1. In the System Properties window, click on **Advanced System Settings**
1. In the **Advanced** tab, click on **Environment Variables**
1. Click on the **New** button to create a new system variable
1. In the **Variable name** input, type "RHINO_COMPUTE_TIMEOUT"
1. In the **Variable value** input, type the **number of seconds** that you want to use as your server-side timeout value
1. Click OK to save the system environment variable, and then click OK again to close the Environment Variables dialog box and the System Properties window.

**I'm getting an error that says the request body is too large. What do I do?**

If Rhino.Compute returns the following error:

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Connection id "...", Request id "...": An unhandled exception was thrown by the application.
      Microsoft.AspNetCore.Server.Kestrel.Core.BadHttpRequestException: Request body too large.
```

This error may occur if you are trying to send a large amount of data to Rhino.Compute in the body of a request. The default limit for the size of a request is approximately 50mb. To increase this limit, follow these steps:

1. Right-click on the **This PC** icon in the File Explorer, then select **Properties** or **System** from the Control Panel
1. In the System Properties window, click on **Advanced System Settings**
1. In the **Advanced** tab, click on **Environment Variables**
1. Click on the **New** button to create a new system variable
1. In the **Variable name** input, type "RHINO_COMPUTE_MAX_REQUEST_SIZE"
1. In the **Variable value** input, type in the **maximum number of bytes** allowed in a HTTP request body. The default value is 52,428,800 bytes (approximately 50mb). Increase this value to allow larger requests.
1. Click OK to save the system environment variable, and then click OK again to close the Environment Variables dialog box and the System Properties window.

<br><br>
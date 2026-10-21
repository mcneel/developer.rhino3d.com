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
override_last_modified = "2026-10-21T09:45:21Z"

[admin]
TODO = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Linux" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

## General

### What is Rhino.Compute?

In its simplest definition, Rhino.Compute is a web server that can perform geometry calculations using Rhino's geometry library (i.e. [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/)). It works by receiving requests over the web (using [HTTP](https://en.wikipedia.org/wiki/HTTP) or [HTTPS](https://en.wikipedia.org/wiki/HTTPS)), processing them with Rhino’s geometry engine, and then sending back the results. Any application that can send web requests can interact with Rhino.Compute, making it easy to integrate into different workflows.

### Why would I want to use it?

Rhino.Compute lets you use Rhino’s powerful tools and features outside of the regular Rhino or Grasshopper interface. It’s great for teams, because you can run Grasshopper definitions or Rhino functions from one central place, making collaboration easier. It can also handle multiple tasks at the same time (in parallel), helping speed up large projects. And for longer calculations, it runs in the background (asynchronously) — so it won’t freeze or slow down your main interface.

### Will it work on macOS?

No. Rhino.Compute is dependent on [Rhino.Inside](https://www.rhino3d.com/features/rhino-inside/) which allows Rhino and Grasshopper to run *inside* other 64-bit applications. Currently, Rhino.Inside is only compatible with Windows and Linux (tested on Ubuntu 24.04 and AmazonLinux 2023) operating systems.

### Does it cost money?

The short answer is: it depends on *where* you run Rhino.Compute. If you're using it on a regular Windows computer, like your personal PC, there’s no extra cost. Rhino.Compute will check for your standard Rhino licence on startup (note: [Rhino evaluation versions](https://www.rhino3d.com/download/) will work just fine). But if you're running it on a Windows or Linux Server (such as a virtual machine in the cloud), you’ll be charged based on our [Core-Hour Billing](../core-hour-billing/) model.

### How is it different from Hops?

[Hops](../what-is-hops/) is a Grasshopper plugin (available from the [package manager](../../yak/what-is-yak/)) that makes it easy to solve Grasshopper definitions using Rhino.Compute. When you install Hops, it automatically starts an instance of Rhino.Compute in the background whenever you open Grasshopper. You can then use the Hops component to send your Grasshopper definition to Rhino.Compute, which solves it and sends the results back. In this context, Hops is the “client” and Rhino.Compute is the “server.”

### Can I make my own interface to work with Rhino.Compute?

Yes. As mentioned earlier, any app that can send web requests can work with Rhino.Compute. To make things easier, we offer three libraries you can use depending on the language you prefer:

1. [Python Rhino.Compute Library](https://pypi.org/project/compute-rhino3d/)
1. [Javascript Rhino.Compute Library](https://www.npmjs.com/package/compute-rhino3d)
1. [.NET (C#) Rhino.Compute Library](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs)

We also have step-by-step guides to help you get started with the libraries above:

1. [Calling Compute with Python](../compute-python-getting-started/)
1. [Calling Compute with Javascript](../compute-javascript-getting-started/)
1. [Calling Compute with .NET](../compute-net-getting-started/)

Finally, we have a [GitHub repository](https://github.com/mcneel/rhino-developer-samples/tree/8/compute) with lots of sample projects and examples that show how to use Rhino.Compute for different geometry tasks.

### Can I use Rhino.Compute in a production environment?

Yes. We offer a [step-by-step guide](../deploy-to-iis/) to help you set up Rhino.Compute in a production environment, such as on a virtual machine (VM). The setup is straightforward—just run a simple PowerShell script, and Rhino.Compute will be up and running, ready to handle requests.

### How do I keep my server up to date?

Run the [update script](../deploy-to-iis/#updating-the-deployment) on the server. It checks Rhino, Rhino.Compute (with its .NET hosting bundle) and Hops, and updates whichever you choose. Your settings stay in place: the update keeps your web.config, with any command line arguments you added, and your environment variables. If the new Rhino.Compute can't be installed, the previous one is put back.

The update keeps the server on the version of Rhino it was set up for. To move to a newer version of Rhino, see [Moving To A Newer Version Of Rhino](../deploy-to-iis/#moving-to-a-newer-version-of-rhino).

### How many requests can my server handle at once?

Each child process (compute.geometry) solves one Grasshopper definition at a time, so the number of child processes sets how many definitions your server can solve at once. The default is 4. When every child is busy, the next request waits for the least busy child to finish, and that wait counts toward the request's timeout.

To change the number of child processes, set the `childcount` argument in web.config, as described in [Modifying Compute Parameters After Deployment](../deploy-to-iis/#modifying-compute-parameters-after-deployment). Keep in mind:

- Each child process is a full copy of Rhino and Grasshopper with its own memory. If the server runs short of memory, use fewer children or a larger server, or add `--load-children-sequentially` so the children don't all load at once.
- As a starting point, don't run more children than the server has CPU cores. Beyond that, the children just take turns on the same processors.
- Rhino.Compute runs at most 64 child processes.

### Is my server safe on the internet?

The bootstrap script sets up a server with safe defaults, but a server that the internet can reach also needs a few things from you:

- **API key** - Rhino.Compute refuses any request without the right `RhinoComputeKey` header. Use a long, random value, and keep it out of anything others can read, such as web pages or public code repositories. If a web page needs results from Rhino.Compute, have the page call your own web service, and let that service call Rhino.Compute.
- **HTTPS** - Rhino.Compute answers plain HTTP on port 80 by default, so your API key and your data travel unencrypted. For anything beyond testing, follow [Configure Compute to use HTTPS](../configure-compute-for-https/).
- **Firewall** - In your virtual machine's network settings (a security group on AWS, a network security group on Azure), open port 80 or 443 only to the addresses that need it, and Remote Desktop (port 3389) only to your own IP address.
- **Private URLs** - Keep the `--block-private-urls` argument that the bootstrap script puts in web.config. It stops requests from making Rhino.Compute fetch addresses on your private network, such as your cloud provider's metadata service.
- **Debug mode** - Don't set `RHINO_COMPUTE_DEBUG` on a server that others can reach, because error responses then include stack traces. Use `RHINO_COMPUTE_LOG_LEVEL` for more detailed logs instead.
- **Updates** - Run the [update script](../deploy-to-iis/#updating-the-deployment) regularly. Rhino 7 servers no longer get Rhino updates, and Rhino 7's Rhino.Compute runs on .NET 5, which no longer gets security fixes, so move them to Rhino 8.
- **Core-hour billing token** - The token stored on the server as `RHINO_TOKEN` lets anyone who has it charge your team, so keep it secret.

## Troubleshooting

We’ve worked hard to make Rhino.Compute as easy to use as possible. But sometimes things don’t go as planned. This section is here to help you troubleshoot and solve any issues you might run into.

### Where can I find the log files?

If you are running Rhino.Compute with Hops, you will want to make sure that the Rhino.Compute console application is visible whenever it starts up. To do this, follow the following steps:
1. Launch Grasshopper
1. Click on **File -> Preferences** to open the Grasshopper Settings dialog
1. Click on the **Solver** tab in the left-hand menu
1. **Uncheck** the Hide Rhino.Compute Console Window menu item
1. Restart Rhino and Grasshopper 

{{< image url="/images/hops-preferences-2.png" alt="/images/hops-preferences-2.png" class="image_center" width="80%" >}}

At this point, you should see a new application appear in your task bar (if you are using Windows) when you start Grasshopper. This is the Rhino.Compute console application. Useful troubleshooting information will be displayed here as you are working with Rhino.Compute.

{{< image url="/images/hops-console-2.png" alt="/images/hops-console-2.png" class="image_center" width="100%" >}}

<br>
If you are running Rhino.Compute on a VM, then the log files are saved as text files. New log files will be created daily. By default, the log files are saved under the following locations:

- Windows
```cs
C:\inetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute\logs\
```

- Linux
```cs
/var/log/rhino-compute
```

Rhino.Compute writes `log-rhino-compute-<date>.txt` and each child process writes `log-compute-geometry-<date>.txt`. Log files are kept for 10 days; set the `RHINO_COMPUTE_LOG_RETAIN_DAYS` environment variable to keep them for a different number of days.

On a server set up with the [bootstrap script](../deploy-to-iis/), the bootstrap and update scripts keep their own logs in `C:\Rhino-Compute-Installation`: `bootstrap_log.txt` and `update_log.txt`.

When Rhino.Compute runs on your own computer through Hops, its log files are in `%TEMP%\Compute\Logs`. Hops writes its own log there too, named `log-hops-inside-Rhino-<date>.txt`.

### Can I enable verbose logging information?

Yes. By default, Rhino.Compute's logs record general information, warnings and errors. To record more detail, set the `RHINO_COMPUTE_LOG_LEVEL` environment variable to `Debug`. Servers set up for Rhino 8 or 9 with the [bootstrap script](../deploy-to-iis/) already have it set to `Debug`, so the detail is there when you need it.

To set it yourself:

1. Right-click on the **This PC** icon in the File Explorer, then select **Properties** or **System** from the Control Panel
1. In the System Properties window, click on **Advanced System Settings**
1. In the **Advanced** tab, click on **Environment Variables**
1. Click on the **New** button to create a new system variable
1. In the **Variable name** input, type "RHINO_COMPUTE_LOG_LEVEL"
1. In the **Variable value** input, type "Debug"
1. Click OK to save the system environment variable, and then click OK again to close the Environment Variables dialog box and the System Properties window.
1. Restart Rhino.Compute so it reads the new setting. On a server running IIS, run `iisreset` in a PowerShell window opened with **Run As Administrator**. If you use Rhino.Compute through Hops, restart Rhino.

The setting accepts `Verbose`, `Debug`, `Information` (the default), `Warning`, `Error` or `Fatal`. Each level also records everything at the levels after it in that list, so `Verbose` records the most and `Fatal` the least. Hops reads the same setting for its own log.

`RHINO_COMPUTE_LOG_LEVEL` needs a Rhino.Compute build from October 14, 2026 or later. If you're on an older build, update it with the [update script](../deploy-to-iis/#updating-the-deployment).

{{< call-out "note" "Note" >}}
Earlier versions of this guide suggested setting <code>RHINO_COMPUTE_DEBUG</code> to <code>true</code>. That still turns on detailed logging, but it also changes what callers get back: error responses include stack traces, and Grasshopper warnings are sent back with the results. Use it only while you're debugging, not on a server that others can reach. Rhino 7's Rhino.Compute doesn't read <code>RHINO_COMPUTE_LOG_LEVEL</code>, so on Rhino 7 servers <code>RHINO_COMPUTE_DEBUG</code> is the only option.
{{< /call-out >}}

### How do I check which versions of Rhino and Rhino.Compute my server runs?

Send a GET request to `/version` with your API key in the `RhinoComputeKey` header. For example, in PowerShell:

```powershell
Invoke-RestMethod http://your-server-address/version -Headers @{ RhinoComputeKey = "your API key" }
```

The answer lists the version of Rhino (`rhino`), the version of Rhino.Compute (`compute`) and the commit Rhino.Compute was built from (`git_sha`). If the child processes aren't running, this request starts them, so the answer can take a while. Please include these details when you ask for support.

### How do I restart Rhino.Compute?

To restart everything, run `iisreset` in a PowerShell window opened with **Run As Administrator**, or restart the server. IIS starts Rhino.Compute again with the next request.

To restart only the child processes, send a POST request to `/recycle-children` with your API key. The children restart one at a time, so the others keep answering requests. A solve that's running on a child when it restarts is stopped. Rhino 7's Rhino.Compute doesn't have this endpoint.

```powershell
Invoke-RestMethod http://your-server-address/recycle-children -Method Post -Headers @{ RhinoComputeKey = "your API key" }
```

### What do I do if I get an HRESULT E_FAIL Error?

If Rhino.Compute returns the following error:

```cs
Application startup exception
System.Runtime.InteropServices.COMException (0x80004005): Error HRESULT E_FAIL has been returned from a call to a COM component.
   at Rhino.Runtime.InProcess.RhinoCore.InternalStartup(Int32 argc, String[] argv, StartupInfo& info, IntPtr hostWnd)
```

This is most likely caused because Rhino.Compute can not find a valid license on startup. If you are running a Windows Server based machine (i.e. on a virtual machine) then follow these steps:

1. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) and **select the team** that you set up with Core-hour billing.
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

### My plugin works on my computer but not on the server. Why?

On a server set up with the [bootstrap script](../deploy-to-iis/), Rhino.Compute runs as a separate Windows account named `RhinoComputeUser`, not as the administrator account you log in with. Rhino and Grasshopper load plugins for each user separately, so plugins you install while logged in as the administrator aren't loaded by Rhino.Compute. To install a plugin for Rhino.Compute:

1. Log into the server with Remote Desktop as `RhinoComputeUser`. The bootstrap script showed its password when it finished, and saved it in `C:\Rhino-Compute-Installation\RhinoComputeUser.txt`. Only Administrators can open that file, so read it while you're logged in as the administrator.
1. Install the plugin with the Rhino **Package Manager**, or copy its files to `C:\Users\RhinoComputeUser\AppData\Roaming\Grasshopper\Libraries`.
1. Restart the server so Rhino.Compute loads the plugin.

To check which plugins Rhino.Compute can see, send GET requests with your API key to these endpoints. Each answers with a list of plugin names and versions:

- `/plugins/gh/installed` - The Grasshopper plugins Rhino.Compute has loaded, not counting the ones that come with Grasshopper.
- `/plugins/rhino/installed` - The Rhino plugins installed for Rhino.Compute, not counting the ones that ship with Rhino.

```powershell
$headers = @{ RhinoComputeKey = "your API key" }
Invoke-RestMethod http://your-server-address/plugins/gh/installed -Headers $headers
Invoke-RestMethod http://your-server-address/plugins/rhino/installed -Headers $headers
```

If your plugin isn't in the list, Rhino.Compute isn't loading it. Check that it's installed for `RhinoComputeUser`, then restart the server.

Opening Rhino on the server uses your core-hour billing like any other Rhino session on that machine, so close it once the plugin is installed.

### How do I find detailed usage statistics about my core-hour billing license?

1. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) and **select the team** that you set up with Core-hour billing.
1. You should then see a table with a list of available McNeel products. **Click on the name of the product (i.e. Rhino 8)** that you wish to inspect.
1. A new page will be opened which contains some live usage statistics. **Click on the blue button labeled "View Historical Usage"** at the bottom of this page.
1. Another new page will be generated which allows you to set custom time ranges and inspect the historical usage of your core-hour billing license. You may even click on the blue button at the bottom of this page to download a comma-separated value list (CSV) of your usage statistics.

### I'm getting a 401 Error message. What does that mean?

If Rhino.Compute gives you a 401 error, it means the request wasn’t authorized. This usually happens when the request is missing an API key. Rhino.Compute checks for this key—which is saved as an environment variable on the machine it's running on—to make sure only approved clients can connect.

If you are using Hops, you can set the API key in the preferences section.

1. Launch Grasshopper
1. Click on **File -> Preferences** to open the Grasshopper Settings dialog
1. Click on the **Solver** tab in the left-hand menu
1. **Enter the API key** in the input dialog
1. Restart Rhino and Grasshopper

{{< image url="/images/hops-api-key2.png" alt="/images/hops-api-key2.png" class="image_center" width="80%" >}}

<br>

If you're sending a web request to Rhino.Compute using a different method, make sure to include a key/value pair in the header of the request. The key should be named **RhinoComputeKey**, and its value must match the API key set on the machine running Rhino.Compute.

### Why do I get "This server has been turned off"?

McNeel used to run a public Rhino.Compute server at `compute.rhino3d.com`. That server has been turned off, and it now answers every request with this message. The Python (`compute_rhino3d`) and JavaScript (`compute-rhino3d`) libraries still send their requests there unless you tell them to use your own server. Set the address of your server, ending in `/`, and your API key before making any calls.

Python:

```python
import compute_rhino3d.Util
compute_rhino3d.Util.url = "http://your-server-address/"
compute_rhino3d.Util.apiKey = "your API key"
```

JavaScript:

```javascript
RhinoCompute.url = "http://your-server-address/"
RhinoCompute.apiKey = "your API key"
```

If Rhino.Compute is running on your own computer through Hops, its address is `http://localhost:6500/`. The .NET library already uses that address by default.

### What does a 500 error code mean?

If you receive a response from Rhino.Compute containing a 500 error code, this means that the server is malfunctioning and is unable to process the request correctly. If this happens, you may need to try to run Rhino.Compute in debug mode to get further information as to why the server is failing. [Follow this guide](../development/) to learn how to run Rhino.Compute in debug mode.

### Why is the first request after a quiet period so slow?

To save core-hour billing, Rhino.Compute shuts its child processes down when it hasn't received a request for a while: an hour by default, set by the `idlespan` argument. IIS also stops Rhino.Compute itself after 65 minutes without requests. The next request has to start Rhino again in each child process, which can take anywhere from several seconds to a minute or more, depending on the server and the plugins Rhino loads. Requests after that are fast again.

To keep the child processes running longer, raise `idlespan` and the IIS **Idle Time-out**, as described in [Modifying Compute Parameters After Deployment](../deploy-to-iis/#modifying-compute-parameters-after-deployment). Remember that the child processes keep using core-hour billing while they run.

To start the child processes ahead of a batch of requests, send a POST request to `/launch-children` with your API key. It answers right away, and the child processes finish loading in the background. Rhino 7's Rhino.Compute doesn't have this endpoint.

```powershell
Invoke-RestMethod http://your-server-address/launch-children -Method Post -Headers @{ RhinoComputeKey = "your API key" }
```

### What do I do if I get a timeout exception?

If Rhino.Compute returns the following error:

```cs
fail: Microsoft.AspNetCore.Server.Kestrel[13]
      Connection id "...", Request id "...": An unhandled exception was thrown by the application.
      System.Threading.Tasks.TaskCanceledException: The request was canceled due to the configured HttpClient.Timeout of 100 seconds elapsing.
```

An HTTP request timeout occurs when a client (like Hops) doesn't receive a response from a server (like Rhino.Compute) within a specified amount of time. Thus there are two timeout values that we should be aware of: 1) the client timeout and 2) the server timeout.

The timeout setting you see in the Hops preferences controls the client-side timeout. The default value is 100 seconds, but this can be extended to alleviate this error.

{{< image url="/images/hops-timeout2.png" alt="/images/hops-timeout2.png" class="image_center" width="80%" >}}

The server-side timeout is managed separately — it's set by an environment variable on the machine running the server. To set the environment variable follow these steps:

1. Right-click on the **This PC** icon in the File Explorer, then select **Properties** or **System** from the Control Panel
1. In the System Properties window, click on **Advanced System Settings**
1. In the **Advanced** tab, click on **Environment Variables**
1. Click on the **New** button to create a new system variable
1. In the **Variable name** input, type **RHINO_COMPUTE_TIMEOUT**
1. In the **Variable value** input, type the **number of seconds** that you want to use as your server-side timeout value
1. Click OK to save the system environment variable, and then click OK again to close the Environment Variables dialog box and the System Properties window.

### Large results take a long time to download. Can Rhino.Compute compress them?

Yes. Rhino.Compute builds from October 13, 2026 or later compress answers of 1 KB or more with gzip for clients that ask for it, and accept gzipped uploads. On one customer's batch of 41 requests, this cut the data sent and received from 489 MB to 81 MB.

- Hops 0.17.1 or later, web browsers, JavaScript `fetch` and Python `requests` (including the compute-rhino3d libraries) ask for compressed answers and unpack them for you.
- In .NET, turn on automatic decompression in the handler you create your `HttpClient` with: `new HttpClientHandler { AutomaticDecompression = DecompressionMethods.GZip }`.
- With curl, add `--compressed`.

Compression is on by default. To turn it off, for example for a client that asks for gzip but can't unpack it, set the `RHINO_COMPUTE_COMPRESSION` environment variable to `false`. Rhino 7's Rhino.Compute doesn't compress.

### I'm getting an error that says the request body is too large. What do I do?

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
1. In the **Variable name** input, type **RHINO_COMPUTE_MAX_REQUEST_SIZE**
1. In the **Variable value** input, type in the **maximum number of bytes** allowed in a HTTP request body. The default value is 52,428,800 bytes (approximately 50mb). Increase this value to allow larger requests.
1. Click OK to save the system environment variable, and then click OK again to close the Environment Variables dialog box and the System Properties window.

<br><br>
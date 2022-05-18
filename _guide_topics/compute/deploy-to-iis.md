---
title: 'Deployment to Production Servers'
description: How to deploy rhino compute for production on a machine running Internet Information Services (IIS).
authors: ['andy_payne']
sdk: ['Compute']
languages: ['C#', 'VB']
platforms: ['Windows']
categories: ['Deployment']
order: 4
keywords: ['developer', 'compute', 'production', 'IIS']
layout: toc-guide-page
redirect_from: ["/guides/compute/deployToIIS/", "/guides/compute/deploy/"]
---

## Overview

This guide will walk you through how to setup an instance of rhino.compute on a virtual machine running Internet Information Services (IIS). [IIS](https://www.iis.net/), is a flexible, general-purpose web server developed by Microsoft which can be configured to serve requested HTML pages or files. We can setup IIS to process incoming requests (either from Hops or some other client) and forward that request to the rhino.compute instance. 

You may be asking yourself, "Why do I need IIS at all? Why can't I simply launch the rhino.compute server and send API requests directly to that instance?". Technically speaking, you don't need IIS. However, you would need to figure out how to relaunch the compute server should it crash or malfunction. You would also need to configure rhino.compute to launch whenever the virtual machine is launched. 

One of the main benefits of using IIS as a middleware is that it can automatically spin up an instance of the rhino.compute server whenever a request is recieved. With this configuration, you do not have to have compute running continuously. Instead, IIS can launch an instance of compute when it is needed which in turn will launch one or more child processes. These child processes are what perform the actual computation and also what require your license authorization. 

When rhino.compute.exe does not receive requests to solve over a period of seconds (this is called idlespans and the default is set to 1 hour), child compute.geometry.exe processes will shut down and stop incurring core hour billing. At some date in the future when a new request is received, IIS will make sure that rhino.compute.exe is running which will then relaunch the child processes. Note, there may be some small delay in the response while the child processes are launching.

<img src="{{ site.baseurl }}/images/IIS_Request.png">{: .img-center  width="100%"}
<figcaption align = "left"><b>Fig.1 - A flow diagram showing how IIS recieves an incoming request and launches rhino.compute.exe which in turn spins up child processes.</b></figcaption>

## Prerequisites

Before running the bootstrap script on your server or virtual machine, you will need the following pieces of information.

* **`EmailAddress`** - The script will use this email to download a copy of Rhino to install. This is similar to the Rhino download page behavior.
* **`ApiKey`** - The API key is a string of text that is secret to your compute server and your applications that are using the compute API e.g. `b8f91f04-3782-4f1c-87ac-8682f865bf1b`. It is basically how the compute server ensures that the API calls are coming from your apps only. You can enter any string that is unique and secret to you and your compute apps. Make sure to keep this in a safe place.
* **`RhinoToken`** – This is a long token that identifies your instance of Rhino Compute to the core-hour billing system. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) to generate this unique id based on your license. See ["Using Core-Hour Billing" guide](../core-hour-billing/#using-core-hour-billing) for more information.

<div class="alert alert-info" role="alert">
Running rhino compute locally uses your existing Rhino license and does not cost any additional money (other than your initial rhino license investment). Running compute locally is the best option for development and testing and to find out more, read <a href="../development"><u>Running and Debugging Compute Locally</u></a>.<br><br>

However, when setting up a production environment you will need a server or virtual machine pre-installed with Windows Server 2019 or higher. Licensing works differently when running Rhino (ie. via Compute) in a production environment (ie. server-setting) and you will be charged at a rate of <strong>$0.10 per core per hour</strong>. <br><br>

Follow the <a href="../core-hour-billing"><u>"Core-Hour Billing" guide</u></a> to get set up. <b>This is important so do not skip.</b>
</div>

## Create the VM

The first step in the process of deploying **rhino.compute** for production is to either setup a physical machine to act as a server or create a virtual machine (VM). For this guide, we will be using a virtual machine. There are several popular services which can be configured to setup a wide array of virtual machines depending on your resource needs. Two of the most prominent providers include [Azure](https://azure.microsoft.com/en-us/free/virtual-machines/) and [AWS](https://aws.amazon.com/ec2/instance-types/).  

Depending on your preferences, we recommend starting with an Azure or AWS VM. Use the following guides to walkthrough that process.

* [Create a Virtual Machine on Azure](../creating-an-Azure-VM).

* [Create a Virtual Machine on AWS](../creating-an-aws-vm).

### Connect via RDP

Now that we've configured the virtual machine, we need to be able to log onto it so that we can setup IIS and the rhino.compute instance. We'll do this by using a remote desktop protocol (RDP) which connects two computers over a network.

To start, let's download the RDP file. We'll use the Azure VM Portal but a similar process is used for AWS.

1. First, make sure the virtual machine is running. Click on the **Overview** tab in the left-hand menu. If the *Status* says *Stopped (Deallocated)*, click on the **Start** button at the top to start the remote machine. After a few seconds, the status should say *Running*.

1. Click on the **Connect** menu item in the left-hand menu to pull out the connection settings blade.

1. Click on the **Download RDP File** button and save the file somewhere on your computer.
<img src="{{ site.baseurl }}/images/Azure_VM_Connect1.png">{: .img-center  width="100%"}

1. Click on the Windows **Start** menu and start typing *remote desktop connection* in the search bar. Click on the link to launch app.

1. Click on the button at the bottom of the app to **Show Options**

1. Under the *Connection Settings* area, select **Open** and navigate to the directory where you saved your RDP file. Choose that file and hit Open.

1. Select the checkbox to **Allow me to save credentials**

1. Click **Connect**.
<img src="{{ site.baseurl }}/images/Azure_VM_Connect2.png">{: .img-center  width="60%"}

1. A security pop-up will be opened. Click the checkbox for **Don't ask me again for connections to this computer** and then click **Connect**.

1. Enter the administrator credentials that you entered in step 7 of [Creating a Virtual Machine](../deploy-to-iis/#setting-up-a-virtual-machine).

1. You may see another security pop-up. Again, select **Don't ask me again for connections to this computer** and click **Yes**.

Congratulations. You should now have access to the desktop of the remote machine running Windows Server 2019 or higher.

## Running the Bootstrap script
Assuming that you are now logged into the virtual machine (using RDP), follow the following steps to install Rhino.Compute behind IIS. Note: The following steps assume that this is an installation on a new virtual machine or server (meaning Rhino.Compute has not been previously installed on this machine). If you have already setup Rhino.Compute and IIS on this machine and simply need to update Rhino and/or Rhino.Compute on this VM, please proceed to the section on [Updating Rhino Compute](../deploy-to-iis/#updating-the-deployment).

### Step 1

1. Click on the Windows Start menu and type in "Powershell". In the menu that appears, right-click on the **Windows Powershell app** and choose **Run As Administrator**.
<img src="{{ site.baseurl }}/images/powershell_1.png">{: .img-center  width="50%"}

1. **Copy and paste** the command below into the Powershell prompt and hit **Enter**. This command will download the latest step 1 bootstrap script and install Rhino and IIS onto your VM. Note: you will be prompted to enter your **Email Address**, **API Key**, and **Rhino Token**, so please have that information handy.

   ```powershell
   $F="/bootstrap_step-1.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/master/script/production/bootstrap_step-1.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\boostrap_step-1.ps1" 
   ```
1. At the end of step 1, your VM will automatically be restarted (You will be logged out of Remote Desktop).

### Step 2

1. Log back into your VM using Remote Desktop.

1. Open a new instance of **Windows Powershell**. Make sure to right-click on the application and select **Run As Administrator**.

1. **Copy and paste** the command below into the Powershell prompt and hit **Enter**. This command will download the latest step 2 bootstrap script and will configure IIS to work with Rhino.Compute.

   ```powershell
   $F="/bootstrap_step-2.zip";$T="$($Env:temp)\tmp$([convert]::tostring((get-random 65535),16).padleft(4,'0')).tmp"; New-Item -ItemType Directory -Path $T; iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/master/script/production/bootstrap_step-2.zip -outfile $T$F; Expand-Archive $T$F -DestinationPath $T; Remove-Item $T$F;& "$T\boostrap_step-2.ps1"
   ```

1. At the end of the step 2 installation script, you should see the message *Congratulations! All components have now been installed.* This will be followed by some instructions about how to install 3rd party plugins so that they will work properly with Rhino.Compute. Please take note of the new **Username** and **Password** which will be required when logging back in to install any additional plugin.

## Testing the app

At this point, IIS should be configured to launch the rhino.compute instance when an API request is made. Let's try getting Hops to send a definition to our virtual machine's URL. 

1. Launch **Rhino** on your local machine.

1. If you have not already installed hops on this machine, please do so by searching for it in the Rhino **Package Manager**.

1. Start **Grasshopper** by typing the word *Grasshopper* into the command prompt and hitting enter.

1. Go to **File** and then **Preferences** to open the preferences dialog. 

1. Click on the **Solver** tab in the left-hand menu. 

1. In the **Hops - Compute server URLs** section, type in the web address of your virtual machine. Start by typing in `http://` followed by the IP address of the virtual machine followed by a `:` and the port number `80`. So, the full address would look something like this:
            
        http://52.168.38.105:80/

1. In the **API Key** section, enter the API Key that you saved in the [Prerequisites](../deploy-to-iis/#prerequisites) section.
<img src="{{ site.baseurl }}/images/Hops_To_IIS_4.png">{: .img-center  width="80%"}

1. Add a **Hops** component to the **Grasshopper canvas** (Params/Util)

1. Right-click on the **Hops** component and set the **Path** to a valid Hops/Grasshopper definition. To learn more about setting up a Grasshopper definition that will work properly with Hops, [follow this guide](../hops-component/).
<img src="{{ site.baseurl }}/images/Hops_To_IIS_2.png">{: .img-center  width="50%"}

Once the path is set, the Hops component will create the appropriate API request and sends it to the URL that we specified in step 6 (the rhino.compute server running on IIS). The compute server processes the request and sends a response back to Hops, which returns the result.
<img src="{{ site.baseurl }}/images/Hops_To_IIS_3.png">{: .img-center  width="70%"}

Congratulations! You have successfully setup an instance of rhino.compute running behind IIS on a virtual machine. 

## Modifying Compute Parameters After Deployment

There are a number of command line arguments that can be used to modify how rhino.compute behaves. This section covers how to change those parameters after rhino.compute has been deployed.

1. Log into your VM (via RDP). See the section, [Connect via RDP](#connect-via-rdp) for more details.

1. On the **Start** menu, click in the search area and type *Internet Information Services (IIS) Manager*. Click to launch the app.

1. In the IIS Manager, **click** on the web server node in the **Connections** panel on the left. Note, this web server name should be the same name you used when setting up the name of your virtual machine. 

1. In the **Actions** pane on the right, click **Stop** to stop the web server.
<img src="{{ site.baseurl }}/images/iis_manager.png">{: .img-center  width="100%"}

Now that the IIS web server has been stopped, we need to go and modify the **web.config* file for rhino.compute. The [web.config](https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/web-config?view=aspnetcore-6.0) file is a file that is read by IIS and the ASP.NET Core module to configure an which is hosted by IIS. 

1. Open a **File Explorer** window and navigate to *C:\inetpub\wwwroot\aspnet_client\system_web\4_0_30319\rhino.compute*. At the end of this directory, you should see a file labled **web.config**. Note, you may need to click on the **View** tab and click the checkbox to turn on **file name extensions**. Open the web.config file with **Notepad** or any other text editor you prefer.

The full web.config file should look like this:

```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.webServer>
    <handlers>
      <add name="aspNetCore" path="*" verb="*" modules="AspNetCoreModuleV2" resourceType="Unspecified"/>
    </handlers>
    <aspNetCore processPath=".\rhino.compute.exe" arguments="--port 80" stdoutLogEnabled="true" stdoutLogFile="..\..\..\..\..\logs\LogFiles\W3SVC1\" forwardWindowsAuthToken="true" hostingModel="InProcess"/>
  </system.webServer>
</configuration>
```
The line we are most interested in modifying is the one which starts with the **`<aspNetCore>`** tag. You can see the second parameter on this line is called **`arguments`**. This is the section that you would edit to add other command line arguments to modify rhino.compute. 

Below is a description of each command line argument which can be modified.

- **port** - This is the port number to run rhino.compute on. Port number 80 is typically reserved for HTTP communication, while port number 443 is used for the HTTPS protocol. We have setup rhino.compute to be bound to port 80 in the bootstrap script, so do not modify this value unless you know what you are doing. Example usage: `--port 80`.

- **childcount** - This parameter controls the number of child compute.geometry processes to manage. The *default value is 4* which means that rhino.compute will spawn four child processes each of which can handle incoming requests. Example usage: `--childcount 8` would tell rhino.compute to launch eight child processes.

- **childof** - This is the process handle of parent process. Compute watches for the existence 
of this handle and will shut down when this process has exited. Since we are relying on IIS starting and stopping rhino.compute, you do not need this parameter when running in a production environment.

- **spawn-on-startup** - This flag determines whether to launch a child compute.geometry process when rhino.compute gets started. The *default value is false*. This parameter is a flag which means that if it is not included in the argument list, the value will be false. If you include this parameter, then its value will be true. For production environments, this value should remain false.

- **idlespan** - This is the number of seconds that a child compute.geometry processes should remain open between requests. The *default value is 1 hour*. When rhino.compute.exe does not receive requests to solve over a period of `idlespan` seconds, child compute.geometry.exe processes will shut down and stop incurring core hour billing. At some date in the future when a new request is received, the child processes will be relaunched which will cause a small delay on requests while the child processes are launching. Example usage: `--idlespan 1800` would tell rhino.compute to shutdown the child processes after 30 minutes (30 mins x 60 secs = 1800).

    If you change the `idelspan` value in the command line arguments for rhino.compute, you will also need to make a modification to the IIS configuration. This is because IIS also contains a setting to shut down rhino.compute if no new requests are received after a period of time. When rhino.compute gets shutdown, it will in turn shutdown any child processes. 

    For example, lets say you change the `idlespan` value to 7,200 (2 hours). The bootstrap script sets the IIS `IdleTimeout` value to 65 minutes (slightly longer than the default `idlespan` value). After 65 minutes, IIS would shutdown rhino.compute, which would then shutdown all of its child processes much earlier than the expected 2 hour time limit. So, if you change the `idlespan` value, it is recommended that you also change the `IdleTimeout` value in the IIS settings.

    1. To do this, go back to the IIS Manager and click on the **Application Pools** item in the **Connections** pane on the left. 
    
    1. In the center window click on the **RhinoComputeAppPool**.

    1. In the **Actions** pane on the right, click **Advanced Settings**.

    1. Find the **Idle Time-out** row under the **Process Model** section and change the time out value to be slightly longer than the `idlespan` value you set in the command line arguments. Note: the `idlespan` value is in seconds while the `Idle Timeout` value is in minutes.
    <img src="{{ site.baseurl }}/images/iis_idletimout.png">{: .img-center  width="60%"}

Once you have modified web.config file, **save** it and close the file. You can then go back to the IIS Manager and **Start** the web server by clicking on the web server node in the **Connections** panel on the left and clicking **Start** in the **Actions** pane on the right.

## Updating The Deployment
If you have already setup Rhino.Compute and/or IIS on this machine, you may need to periodically update Rhino and/or the Rhino.Compute build files to the latest version. Follow the steps below to update these applications.

### Update Rhino

1. Click on the Windows Start menu and type in "Powershell". In the menu that appears, right-click on the **Windows Powershell app** and choose **Run As Administrator**.

1. **Copy and paste** the command below into the Powershell prompt and hit **Enter**. This command will download the latest version of Rhino for Windows. Note: you will be prompted to enter your **Email Address** so please have that information available.

    ```powershell
iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/master/script/production/module_update_rhino.ps1 -outfile update_rhino.ps1; .\update_rhino.ps1 
    ```

### Update Compute

1. Click on the Windows Start menu and type in "Powershell". In the menu that appears, right-click on the **Windows Powershell app** and choose **Run As Administrator**.

1. **Copy and paste** the command below into the Powershell prompt and hit **Enter**. This command will download the latest version of Rhino.Compute.

    ```powershell
iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/master/script/production/module_update_compute.ps1 -outfile update_compute.ps1; .\update_compute.ps1 
    ```

 ---
 
## Quick Links

 - [What is Hops](../what-is-hops)
 - [How Hops Works](../how-hops-works)
 - [The Hops Component](../hops-component)

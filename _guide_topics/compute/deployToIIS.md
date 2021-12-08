---
title: 'Deployment to a Virtual Machine running IIS'
description: How to deploy compute for production on a virtual machine running Internet Information Services (IIS).
authors: ['andy_payne']
sdk: ['Compute']
languages: ['C#', 'VB']
platforms: ['Windows']
categories: ['Deployment']
order: 2
keywords: ['developer', 'compute', 'production', 'IIS']
layout: toc-guide-page
---

## Overview

This guide will walk you through how to setup an instance of rhino.compute on a virtual machine running Internet Information Services (IIS). [IIS](https://www.iis.net/), is a flexible, general-purpose web server developed by Microsoft which can be configured to serve requested HTML pages or files. We can setup IIS to process incoming requests (either from Hops or some other client) and forward that request to the rhino.compute instance. 

You may be asking yourself, "Why do I need IIS at all? Why can't I simply launch the rhino.compute server and send API requests directly to that instance?". Technically speaking, you don't need IIS. However, you would need to figure out how to relaunch the compute server should it crash or malfunction. You would also need to configure rhino.compute to launch whenever the virtual machine is launched. 

One of the main benefits of using IIS as a middleware is that it can automatically spin up an instance of the rhino.compute server whenever a request is recieved. With this configuration, you do not have to have compute running continuously. Instead, IIS can launch an instance of compute when it is needed which in turn will launch one or more child processes. These child processes are what perform the actual computation and also what require your license authorization. 

When rhino.compute.exe does not receive requests to solve over a period of seconds (this is called idlespans and the default is set to 1 hour), child compute.geometry.exe processes will shut down and stop incurring core hour billing. At some date in the future when a new request is received, IIS will make sure that rhino.compute.exe is running which will then relaunch the child processes. Note, there may be some small delay in the response while the child processes are launching.

<img src="{{ site.baseurl }}/images/IIS_Request.png">{: .img-center  width="100%"}
<figcaption align = "left"><b>Fig.1 - A flow diagram showing how IIS recieves an incoming request and launches rhino.compute.exe which in turn spins up child processes.</b></figcaption>

## Creating a VM

In this guide, we will walk through the process of setting up a virtual machine using Azure services. If you are configuring a VM on a different platform (ie. AWS), the settings should be similar, although the user interface and process may vary. 

To start, please confirm that you have a valid Azure subscription and that you have already setup a resource group to hold the various resources for this instance. To learn more about setting up a resource group on Azure, [visit this page](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal).

### Azure Settings

1. Sign in to the Azure [portal](https://portal.azure.com/#home).

1. Type **virutal machines** in the search bar.

1. Under **Services**, select **Virtual machines**.

1. In the **Virtual machines** page, select **Create** then **Virtual Machine**

1. In the **Basics** tab, under **Project details**, make sure the correct Subscription and Resource group are selected.

1. Under **Instance details**, create a unique name for the virutal machine. We'll use *Rhino-Compute-VM* for our VM name. Select a region close to you, and then select *Windows Server 2022 Datacenter - Azure Edition Gen2* for the **Image**. Feel free to select any **Size** VM that fits your needs. We'll use *Standard DS2_v2* for this example. Leave the other defaults.
<img src="{{ site.baseurl }}/images/Azure_VM_Create3.png">{: .img-center  width="100%"}

1. Under **Administrator account**, provide a username and a password. Take note of these credentials as we will use these when we log into the remote machine.

1. Under **Inbound port rules**, choose **Allow selected ports** then select **RDP (3389)**, **HTTPS (443)**, and **HTTP (80)**.
<img src="{{ site.baseurl }}/images/Azure_VM_Create4.png">{: .img-center  width="100%"}

1. Select **Next : Disk >**.

1. Select **Next : Networking >**.

1. Under the **Network interface** section, click on the *Create new* button under the **Public IP** subsection.

1. When the pop-out blade opens up, select **Static** under the Assignment tab. Click **OK** to save this setting.
<img src="{{ site.baseurl }}/images/Azure_VM_Create5.png">{: .img-center  width="100%"}

1. Leave all other defaults. Select **Review + create**.

1. Once your configuration passes the validation check, select **Create** to deploy your virtual machine.

### Add an inbound port rule

Once your virtual machine has been deployed you should be able to go to the resources home page. Here, you can change various settings and configurations. We are going to add an inbound port rule so that we can send API requests on a dedicated port.

By default, Azure locks most (if not all) ports down from inbound traffic (for security reasons). In our VM configuration, we specified that we wanted to create inbound port rules for **RDP (port 3389)**, **HTTPS (port 443)**, and **HTTP (port 80**). Let's add one more port rule to allow incoming requests on a dedicated port.

1. On the left-hand side menu, select the **Networking** menu item. This will open the Networking blade.

1. Click on the **Add inbound port rule** button
<img src="{{ site.baseurl }}/images/Azure_VM_Create6.png">{: .img-center  width="100%"}

1. In the pop-out panel, set the **Destination port ranges** to **81**. Note: this number is arbitrary and can be any valid integer value. 

1. In the *Name* area, type in **Port_81**. Again, you can change this if you wish.
<img src="{{ site.baseurl }}/images/Azure_VM_Create7.png">{: .img-center  width="75%"}

1. Click **Add** to create the new inbound port rule.

### Connect via RDP

Now that we've configured the virtual machine, we need to be able to log onto it so that we can setup IIS and the rhino.compute instance. We'll do this by using a remote desktop protocol (RDP) which connects two computers over a network.

To start, let's download the RDP file for our Azure VM.

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

1. Enter the administrator credentials that you entered in step 7 of [Creating a Virtual Machine](https://developer.rhino3d.com/guides/compute/deployToIIS/#setting-up-a-virtual-machine).

1. You may see another security pop-up. Again, select **Don't ask me again for connections to this computer** and click **Yes**.

Congratulations. You should now have access to the desktop of the remote machine running Windows Server 2022.

## Configuring the VM

Now that you have logged into the virtual machine via RDP, let's take a look at how to setup Windows Server to host our instance of rhino.compute.

### Install .NET Core Hosting Bundle

The first thing we need to do is install the *.NET Core Hosting Bundle* on the VM in order to run rhino.compute (an ASP.NET Core app) on the VM. The bundle installs the .NET Core Runtime, .Net Core Library, and the ASP.NET Core Module which allows ASP.NET Core apps to run behind IIS.

1. Download the [.NET Core Hosting Bundle (direct download)](https://dotnet.microsoft.com/download/dotnet/thank-you/runtime-aspnetcore-5.0.12-windows-hosting-bundle-installer) Note: Rhino.compute currently targets the .NET Core 5.0 Framework.

1. Restart your virtual machine.

### Open Firewall Port

We have already created an inbound port rule for the Azure network interface, however we must also create a rule to allow messages through the Windows firewall.

1. From the **Start** menu, click **Control Panel**, click **System and Security**, and then click **Windows Defender Firewall**. 

1. Click **Advanced Settings** in the left-hand menu.

1. Click **Inbound Rules**.

1. Click **New Rule** in the **Actions** window.
<img src="{{ site.baseurl }}/images/Firewall_Rule_01.png">{: .img-center  width="100%"}

1. Click **Rule Type** of **Port**.

1. Click **Next**.

1. On the **Protocol and Ports** page click **TCP**.

1. Select **Specific Local Ports** and type a value of **81**. This port number is arbitrary but it should match the same value as the one which was set in the Azure portal.
<img src="{{ site.baseurl }}/images/Firewall_Rule_02.png">{: .img-center  width="100%"}

1. Click **Next**.

1. On the **Action** page, click **Allow the connection**.

1. Click **Next**.

1. On the **Profile** page, make sure **Domain**, **Private**, and **Public** checkboxes are marked.

1. Click **Next**.

1. On the **Name** page, enter a name of **Rhino.Compute Server (TCP on port 81)**.

1. Click **Finish**.

1. Restart your virtual machine.

### Install Rhino

Next we need to install Rhino on the virtual machine and setup core-hour billing.

1. [Download the Rhino 7.0](https://www.rhino3d.com/download/rhino-for-windows/7/latest).

1. [Follow this guide](https://developer.rhino3d.com/guides/compute/core-hour-billing/) for setting up core-hour billing on the virtual machine.

### Install IIS

By default, IIS is not enabled on Windows Server. To install IIS on the virtual machine, follow these steps.

1. Open the **Server Manager** console. This usually opens by default after startup, however if its not there, click on the **Start** menu and search for *Server Manager*.

1. Click the **Add roles and features** button.
<img src="{{ site.baseurl }}/images/IIS_Setup_1.png">{: .img-center  width="100%"}

1. Click **Next** on the **Before you begin** page

1. On the **Installation type** page, select **Role-based or feature-based installation**.
<img src="{{ site.baseurl }}/images/IIS_Setup_2.png">{: .img-center  width="100%"}

1. We will be installing IIS on this local machine, so leave **Select a server from the server pool** checked.

1. Click **Next**.
<img src="{{ site.baseurl }}/images/IIS_Setup_3.png">{: .img-center  width="100%"}

1. On the **Select server roles** page, check the box next to **Web Server (IIS)**. A pop-up dialog will be opened advising that additional features are required. Click the **Add Features** button to install these as well.

1. Click **Next**.
<img src="{{ site.baseurl }}/images/IIS_Setup_4.png">{: .img-center  width="100%"}

1. We do not need to install any additional features at this time, so click **Next** on the **Select Features** page.
<img src="{{ site.baseurl }}/images/IIS_Setup_5.png">{: .img-center  width="100%"}

1. On the **Select role services** page, review the available features that are available. For now, we will simply leave the default selections, but you can always come back and add more later.

1. Click **Next**.
<img src="{{ site.baseurl }}/images/IIS_Setup_6.png">{: .img-center  width="100%"}

1. Finally, on the **Confirmation** page, review the items that are going to be installed on the VM. When satisfied, click the **Install** button. Note, no reboot should be required with a standard IIS installation. However, if you remove the role a reboot will be needed.
<img src="{{ site.baseurl }}/images/IIS_Setup_7.png">{: .img-center  width="100%"}

1. Once the installation has succeeded, click the **Close** button. At this point, IIS should be running on port 80 (by default).
<img src="{{ site.baseurl }}/images/IIS_Setup_8.png">{: .img-center  width="100%"}

1. You can now open the **IIS Manager** app by clicking on the Windows **Start** menu and searching for *IIS Manager**. This will launch the IIS Manager console app. We won't do anything in the IIS Manager just yet, but you should be able to confirm that IIS is now operational on the VM.
<img src="{{ site.baseurl }}/images/IIS_Setup_9.png">{: .img-center  width="100%"}

## Publish rhino.compute

The next step in the process will be to publish the `rhino.compute` and `compute.geometry` projects. In order to do this, you will need to have the [Visual Studio 2019 IDE](https://visualstudio.microsoft.com/) and [Git](https://git-scm.com/downloads) installed on your machine.

You have two options as to where you can install these applications. You can either install these on virtual machine and publish the rhino.compute applications locally, or you can install these on a different machine and then copy/paste the published files over to the VM. In this walkthrough, I will choose the later approach.

1. Go to [https://github.com/mcneel/compute.rhino3d](https://github.com/mcneel/compute.rhino3d) and clone the repo to a directory on your machine. To do this:
   
   * Open **Powershell** and navigate to a directory where you want to clone the repository.
   * Type `$ git clone https://github.com/mcneel/compute.rhino3d.git compute` into the terminal.
   * Press **Enter** to create a local clone of the rhino.compute repo on your machine.

1. Next, launch **Visual Studio**

1. Choose **Open a Project or Solution** and navigate to the directory where you cloned the repo, then choose the **src** subfolder. Choose the **compute.sln** file and choose **Open**.

1. In the **Solution Explorer** you should see two projects. One is called **rhino.compute** and the other **compute.geometry**. Right-click on the **rhino.compute** project and select **Publish** from the menu.
<img src="{{ site.baseurl }}/images/Compute_Publish_2.png">{: .img-center  width="100%"}

1. A new **Publish** dialog will be opened. For the **Target** choose the **Folder** option.
<img src="{{ site.baseurl }}/images/Compute_Publish_3.png">{: .img-center  width="100%"}

1. Next you will be asked for a directory to save all of the published files. You can choose any location but I have created a directory called *compute-for-IIS*. Inside this folder, I've created two subfolders called *rhino.compute* and *compute.geometry*. Select the *rhino.compute* subfolder as the target location to save the files. 
<img src="{{ site.baseurl }}/images/Compute_Publish_4.png">{: .img-center  width="100%"}
Your folder structure looks like this:


        * compute-for-IIS
            * rhino.compute
            * compute.geometry


1. Click **Finish**.

1. Back in the Visual Studio **Publish** window, select **Show all settings**.
<img src="{{ site.baseurl }}/images/Compute_Publish_5.png">{: .img-center  width="100%"}

1. In the **Publish** setting dialog, select **Settings**. Make sure that the **Configuration** is set to *Release*, **Deployment Mode** is set to *Self-contained*, and the **Target Runtime** is set to *win-x64*. Leave all other defaults.

1. Click **Save**.
<img src="{{ site.baseurl }}/images/Compute_Publish_6.png">{: .img-center  width="100%"}

1. Click the **Publish** button to begin the process of saving the rhino.compute project to the target directory.
<img src="{{ site.baseurl }}/images/Compute_Publish_7.png">{: .img-center  width="100%"}

1. Now, we have to go through a similar process to publish all of the files for the compute.geometry project. This time, right-click on the **compute.geometry** project in the **Solution Explorer** and select **Publish**.
<img src="{{ site.baseurl }}/images/Compute_Publish_8.png">{: .img-center  width="100%"}

1. Choose **Folder** as the **Target** type, just like in step 5.

1. This time, set the *compute.geometry* subfolder that you created in step 6.

1. Click **Finish**.
<img src="{{ site.baseurl }}/images/Compute_Publish_9.png">{: .img-center  width="100%"}

1. We can leave all of the other configuration settings to their defaults. Click **Publish** to save the files to the target directory.

<br>
At this point, you should have a folder on your machine labeled **compute-for-IIS**. Inside that folder, you should have two subfolders each of which contain a number of files. Next, we need to copy those two subfolders over to a directory on the virtual machine.

If you aren't already logged into your virtual machine through the **Remote Desktop Connection** app, please do so now.

When we installed IIS on the virtual machine, it created a folder called *inetpub* on the *C:\\* drive. 

The folder structure looks like this:

    * C:\inetpub
        * custerr
        * history
        * logs
        * temp
        * wwwroot   <- copy/paste compute-for-IIS folder here 


We need to copy/paste the contents of the **compute-for-IIS** folder into the **wwwroot** directory.

<img src="{{ site.baseurl }}/images/Compute_Publish_10.png">{: .img-center  width="85%"}

In the next step, we will create an IIS application and point it to this directory in order to launch an instance of rhino.compute when it receives an API request.
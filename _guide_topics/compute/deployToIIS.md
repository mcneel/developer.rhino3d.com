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

## Setting up a Virtual Machine

In this guide, we will walk through the process of setting up a virtual machine using Azure services. If you are configuring a VM on a different platform (ie. AWS), the settings should be similar, although the user interface and process may vary. 

To start, please confirm that you have a valid Azure subscription and that you have already setup a resource group to hold the various resources for this instance. To learn more about setting up a resource group on Azure, [visit this page](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal).

### Creating the Virtual Machine

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

### Download the RDP file and connect to the VM

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
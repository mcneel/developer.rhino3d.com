---
title: 'How to create a virtual machine (VM) on Azure'
description: 
authors: ['andy_payne']
sdk: ['Compute']
languages: ['C#', 'VB']
platforms: ['Windows']
categories: ['Deployment']
order: 2
keywords: ['developer', 'compute', 'production', 'Azure']
layout: toc-guide-page
---

## Creating the Virtual Machine

In this guide, we will walk through the process of setting up a virtual machine using Azure services. 

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

1. After deployment is complete, select **Go to resource**.

Congratulations! In this guide, you deployed a simple virtual machine on Azure.
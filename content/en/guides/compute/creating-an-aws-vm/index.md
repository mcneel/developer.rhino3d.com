+++
aliases = ["/5/guides/compute/creating-an-aws-vm/", "/6/guides/compute/creating-an-aws-vm/", "/7/guides/compute/creating-an-aws-vm/", "/wip/guides/compute/creating-an-aws-vm/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "AWS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "How to create a virtual machine (VM) on Amazon Web Service"
type = "guides"
weight = 3
override_last_modified = "2021-12-14T13:16:19Z"

[admin]
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

## Overview

In this guide, we will walk through the process of setting up a virtual machine using Amazon Elastic Compute Cloud (Amazon EC2). 

To start, you will need to confirm your AWS subscription. If you are new to AWS, you can get started with Amazon EC2 using the [AWS Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all). 

{{< call-out "note" "Note" >}}
If you created your AWS account less than 12 months ago, and have not already exceeded the free tier benefits for Amazon EC2, it will not cost you anything to complete this tutorial. Otherwise, you'll incur the standard Amazon EC2 usage fees from the time that you launch the instance until you terminate the instance, even if it remains idle.
{{< /call-out >}}

## Prerequisites

1. [Create an account for AWS](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#sign-up-for-aws)

1. [Create a key pair](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-key-pair). Note: We recommend saving the **private key file** as a **.pem** format with **RSA** encryption.

1. [Create a security group](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/get-set-up-for-amazon-ec2.html#create-a-base-security-group). Note, we recommend adding a rule for **HTTP**, **HTTPS**, **RDP**, and **All ICMP - IPv4**.

## Launch the instance

To create a new virtual machine instance on AWS, follow these steps:

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/).

1. From the EC2 console dashboard, select **Launch Instance**.

1. Provide a name for the VM instance. For this tutorial, we'll use the name **"RhinoComputeVM"**.

1. Under the section titled Application and OS Images, click on the **Windows** button under the Quick Start tab. Under the Amazon Machine Image (AMI) section there should be a drop-down menu listing all of the available machine images. Select the AMI for **Microsoft Windows Server 2022 Base**.</p>
{{< image url="/images/AWS_Setup_11.png" alt="/images/AWS_Setup_11.png" class="image_left" width="90%" >}}

1. In the **Instance Type** section, select the **t2.micro** instance type (default) or a larger instance type if needed. Note: the *t2.micro* instance type is elegible for the free tier. In regions where *t2.micro* is unavailable, you can use a *t3.micro** instance under the free tier.</p>
{{< image url="/images/AWS_Setup_12.png" alt="/images/AWS_Setup_12.png" class="image_left" width="90%" >}}

1. In the **Key Pair (login)** section, select the key pair name that you created in step 2 of the prerequisite section [prerequisite section](../creating-an-aws-vm/#prerequisites) from the drop-down list.</p>
{{< image url="/images/AWS_Setup_13.png" alt="/images/AWS_Setup_13.png" class="image_left" width="90%" >}}

1. In the **Network Settings** section, under the **Firewall (security groups)** choose the **Select existing security group** radio button. Then, under the **Common Security Groups** drop-down list, select the security group you created in step 3 of the [prerequisite section](../creating-an-aws-vm/#prerequisites).{{< call-out "warning" "Important" >}}If the **Auto-assign public IP** setting is set to **Disabled**, click on the **Edit** button on the top-right of this section panel and change this setting to **Enabled**.{{< /call-out >}}
{{< image url="/images/AWS_Setup_14.png" alt="/images/AWS_Setup_14.png" class="image_left" width="90%" >}}

1. In the **Configure storage** section, select the default amount of storage for this instance.

1. Now, on the far right select the **Launch Instance**.

1. A confirmation page lets you know that your instance has successfully launched. In the top-most menu which reads **EC2 > Instances > Launch an instance**, select the **Instances** menu item to view the instances console window.</p>
{{< image url="/images/AWS_Setup_15.png" alt="/images/AWS_Setup_15.png" class="image_left" width="90%" >}}

1. On the **Instances** screen, you can view the status of the launched instance. The instance should automatically be running after launch, but if not select the instance row checkbox and then select the **Instance State** menu item at the top. Select **Start Instance** to start the virtual machine.

1. With the instance row selected, click the **Connect** button in the top menu.

1. On the **Connect to instance** page, select the **RDP client** tab. Select the **Download remote desktop file** and save the .rdp file somewhere on your local computer.

1. Next, select the **Get password** button.

1. Choose **Upload private key file** and navigate to the private key (.pem) file that you created when you launched the instance.

1. Choose **Decrypt Password**. The console displays the default administrator password for the instance under **Password**, replacing the **Get password** link shown previously. **Save this password in a safe place**. This passord is required to connect to the instance.

1. Select **Download remote desktop file** to save the .rdp file to your local computer. You will need this file when you connect to your instance using the Remote Desktop Connect app.

Congratulations! In this tutorial, you successfully launched a virtual machine on AWS and downloaded the RDP file which can be used to connect to that instance.
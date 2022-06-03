+++
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

1. The **Choose an Amazon Machine Image (AMI)** page displays a list of basic machine configurations (AMIs) to choose from. Select the AMI for **Windows Server 2019 Base** or later. Note that these AMIs are marked *Free tier eligible*.
{{< image url="/images/AWS_Setup_01.png" alt="/images/AWS_Setup_01.png" class="image_center" width="100%" >}}

1. On the **Choose an Instance Type** page, select the **t2.micro** instance type (default). Note: the *t2.micro* instance type is elegible for the free tier. In regions where *t2.micro* is unavailable, you can use a *t3.micro** instance under the free tier.
{{< image url="/images/AWS_Setup_02.png" alt="/images/AWS_Setup_02.png" class="image_center" width="100%" >}}

1. On the **Choose an Instance Type** page, select **Review and Launch** to let the wizard complete the other configuration settings for you.

1. On the **Review Instance Launch** page, under **Security Groups**, you'll see that the wizard created and selected a security group for you. We will need to specify the security group that was created in step 3 of the **Prerequisites** section.
    * Choose **Edit security groups**.
    * On the **Configure Security Group** page, choose **Select an existing security group**.
    * In the table, select the **security group** from the list of existing security groups.
    * Choose **Review and Launch**.

1. On the **Review Instance Launch** page, select **Launch** to create the new virtual machine.

1. When prompted for a key pair, select **Choose an existing key pair**. Then select the key pair that you created in step 2 of the **Prerequisites** section
    <div class="alert alert-info" role="alert">Do not select <strong>Proceed without a key pair</strong>. If you launch your instance without a key pair, then you can't connect to it.
    </div>
    {{< image url="/images/AWS_Setup_03.png" alt="/images/AWS_Setup_03.png" class="image_center" width="100%" >}}

1. Select the **acknowledgement** checkbox and then choose **Launch Instances**.

1. A confirmation page lets you know that your instance is launching. Select **View Instances** to close the confirmation page and return to the console.

1. On the **Instances** screen, you can view the status of the launch. In the **Name** column, select the **Edit** icon. In the popup dialog, type **RhinoComputeVM** to assign a namge to this instance.
{{< image url="/images/AWS_Setup_04.png" alt="/images/AWS_Setup_04.png" class="image_center" width="50%" >}}

1. Once the **Instance State** column says that the VM is **Running**, you can then try to connect to it via RDP.

1. With the instance row selected, click the **Connect** button in the top menu.

1. On the **Connect to instance** page, select the **RDP client** tab. Select the **Download remote desktop file** and save the .rdp file somewhere on your local computer.

1. Next, select the **Get password** button.

1. Choose **Browse** and navigate to the private key (.pem) file that you created when you launched the instance.

1. Choose **Decrypt Password**. The console displays the default administrator password for the instance under **Password**, replacing the **Get password** link shown previously. **Save this password in a safe place**. This passord is required to connect to the instance.

1. Select **Download remote desktop file** to save the .rdp file to your local computer. You will need this file when you connect to your instance using the Remote Desktop Connect app.

Congratulations! In this tutorial, you successfully launched a virtual machine on AWS and downloaded the RDP file which can be used to connect to that instance.
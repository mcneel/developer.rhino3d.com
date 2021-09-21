---
title: 'Deployment to Production Servers'
description: Deploy Compute for Production
authors: ['brian_gillespie', 'will_pearson']
sdk: ['Compute']
languages: ['C#', 'VB']
platforms: ['Windows']
categories: ['Deployment']
order: 1
keywords: ['developer', 'compute', 'production']
layout: toc-guide-page
---

How to deploy Compute to production server environment. To run Compute locally for development and testing, read [Running and Debugging Compute Locally](../development).

<div class="alert alert-info" role="alert">
Running Compute locally uses your existing Rhino license. This is the best option for development and testing. Licensing works differently when running Rhino (i.e. via Compute) in a server-setting and you will be charged at a rate of <strong>$0.10 per core per hour</strong> if you follow this guide. 
</div>

## 1. Set up Core-Hour Billing

Follow the ["Core-Hour Billing" guide](../core-hour-billing) to get set up. This is important so do not skip.

## 2. Prepare Windows Server

To run Compute you'll need a server or virtual machine pre-installed with Windows Server 2019.

We'll assume you're deploying Compute to one of Amazon's EC2 instances. There are a few things to pay attention to when setting up the instance – use this as a rough guide if you're using a virtual machine from another cloud provider or a physical server.

* Start with the "Microsoft Windows Server 2019 Base" AMI.
* The t2.medium instance type (2 vCPU, 4 GB RAM) is recommended.
* Assign a public ip, or better yet use an [Elastic IP and Route53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-ec2-instance.html).
* Set a "Name" tag to help keep track of instances.
* Configure the security group to allow Compute traffic:
    * RDP - 3389 TCP
    * HTTP - 80 TCP
    * HTTPS - 443 TCP

Wait for the virtual machine to spin up... ☕️

## 3. Install Rhino and Compute

1. Connect to the server or virtual machine (usually using RDP) and open a PowerShell window.
2. Copy and paste the command below and hit Enter, to download and run the installer scripts:

    ```powershell
    iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/master/script/bootstrap-server.ps1 -outfile bootstrap.ps1; .\bootstrap.ps1 -install
    ```

    This [script](https://github.com/mcneel/compute.rhino3d/blob/master/script/bootstrap-server.ps1) will install Rhino and the latest build of Compute as well as ensuring that clients can communicate with Compute. Compute will be installed as a Windows service (named "rhino.compute") so that it starts automatically when the server or virtual machine starts. You will be asked to enter a few things...
    * `EmailAddress` - The script will use this email to download a copy of Rhino to install. This is similar to the Rhino download page behavior.
    * `ApiKey` - The API key is a string of text that is secret to your compute server and your applications that are using the compute API e.g. `u5E5kFMKDx5GDfYsnJPf3dy0BcVjJF4O`. It is basically how the compute server ensures that the API calls are coming from Your apps only. You can enter any string that is unique and secret to you and your compute apps. Make sure to keep this in a safe place.
    * `RhinoToken` – This is a long token that identifies your instance of Rhino Compute to the core-hour billing system. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) to generate this unique id based on your license. See ["Using Core-Hour Billing" guide](../core-hour-billing#using-core-hour-billing) for more information.

4. At the end of the installation process, Windows will restart to complete the setup. Wait a minute and log back in to check that the "rhino.compute" service is running.

<!-- Compute won't start the first time because the .NET 4.8 install needs to finish up -->
<!-- TODO: check if we can install the service with "delayed" start to make this work better -->
<div class="alert alert-warning" role="alert">
<strong>After the first restart</strong> you may need to start the "rhino.compute" service manually. <strong>Every other time it will start automatically.</strong>
</div>

<div class="alert alert-info" role="alert">
The Windows service display name was changed from "compute.geometry" to "rhino.compute" in early 2021. The underlying service name was not changed, so existing installations should keep functioning as normal.
</div>

## 4. Verify Compute and license usage

1. Open a browser and go to _http://public-dns-or-ip/version_. If Compute is working it will return its version and Rhino's version.
1. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) (login to your Rhino account if prompted).
1. Under _Team Licenses_ click your new team.
1. Verify that Rhino is in use in your core-hour billing team.

<div class="alert alert-info" role="alert">
You are now being charged via <a href="../core-hour-billing" class="alert-link">Core-Hour Billing</a>. To stop the billing, either stop the "rhino.compute" service or shutdown the server or virtual machine.
</div>

## 5. Next steps

Check out the [Rhino Compute AppServer](https://github.com/mcneel/compute.rhino3d.appserver) – a node.js server acting as a bridge between client apps and private Compute servers.

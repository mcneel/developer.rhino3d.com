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

## 1. Set up Core-Hour Billing

Follow the ["Core-Hour Billing" guide](../core-hour-billing) to get set up.

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

On the virtual machine, copy and paste the command below into a powershell window and hit Enter. You will be asked to enter a few things...

* `EmailAddress` - the Rhino download link requires a valid email address
* `ApiKey` - the API Key that clients will use when communicating with Compute
* `RhinoToken` – the long token that links Rhino to your core-hour billing team

```powershell
iwr -useb https://raw.githubusercontent.com/mcneel/compute.rhino3d/master/script/bootstrap-server.ps1 -outfile bootstrap.ps1; .\bootstrap.ps1 -install
```
At the end of the installation process, Windows will restart to complete the setup. Wait a minute and log back in to check that the compute.geometry service is running.

<!-- Compute won't start the first time because the .NET 4.8 install needs to finish up -->
<!-- TODO: check if we can install the service with "delayed" start to make this work better -->
<div class="alert alert-warning" role="alert">
<strong>After the first restart</strong> you may need to start the compute.geometry service manually. <strong>Every other time it will start automatically.</strong>
</div>

## 4. Verify Compute and license usage

1. Open a browser and go to _http://public-dns-or-ip/version_. If Compute is working it will return its version and Rhino's version.
1. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) (login to your Rhino account if prompted).
1. Under _Team Licenses_ click your new team.
1. Verify that Rhino is in use in your core-hour billing team.

## 5. Next steps

Check out the [Rhino Compute AppServer](https://github.com/mcneel/compute.rhino3d.appserver) – a node.js server acting as a bridge between client apps and private Compute servers.
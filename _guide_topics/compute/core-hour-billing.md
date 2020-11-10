---
title: Licensing & Billing
description: 
authors: ['brian']
sdk: ['Compute']
languages: []
platforms: ['Windows']
categories: ['Deployment']
origin: http://www.grasshopper3d.com/forum/topics/how-do-i-install-a-custom-ghx
order: 4
keywords: ['developer', 'compute', 'core-hour']
layout: toc-guide-page
TODO: 'needs editing'
---


## About Core-Hour Billing

When Rhino is logged in to a service account and is running on a Windows Server-based operating system, you will be billed **$0.10 per core per hour** that Rhino is running (pro-rated per minute).

***Example 1:** Rhino running on a 32-core server for one hour:*

  * 32-cores * 1 hour * $0.10/core-hour = $3.20

***Example 2:** Rhino running on 200 4-core servers for 6 minutes:*

  * 200 computers * 4 cores * 0.1 hour * $0.10/core-hour = $8.00

**Billing is based on uptime**, not on usage - we don’t track the activity of each core, just that you have one running with Rhino. You can scale your workloads up and down to optimize performance and cost to you.

**Multiple instances are allowed** - you may run as many instances of Rhino on the same machine as you want, and the cost will be the same as running one instance.

## Setting Up Core-Hour Billing:
Core-hour billing is required when running Rhino on a Windows Server-based operating system.

1. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) (Login to your Rhino account if prompted).
2. Click _Create New Team_ and create a team to use for your compute project.
3. Click _Action_ -> _Manage Core-Hour Billing_.
4. Check the checkbox next to Rhino 6 and Rhino 7 and the checkbox signaling you agree to pay.
5. Click _Save_, and enter payment information when prompted for your new team.
6. Once the payment information is saved and core-hour billing is enabled, click _Action_ -> _Get Auth Token_.
7. We'll pass this token to the bootstrap script in the next step to set the `RHINO_TOKEN` environment variable on the virtual machine. Just leave the page open for now.

⚠️ _**WARNING:** This token allows anyone with it to charge your team at will. Do **NOT** share this token with anyone._

## Using Core-Hour Billing
  1. Install Rhino on one or more instances of Windows Server where `RHINO_TOKEN` is set.


## Single-Computer licensing Not Supported
When running on Windows Server, it is not possible to enter a license key to run as a single-computer license, as Rhino requires a license per core.

+++
aliases = ["/5/guides/compute/core-hour-billing/", "/6/guides/compute/core-hour-billing/", "/7/guides/compute/core-hour-billing/", "/wip/guides/compute/core-hour-billing/"]
authors = [ "brian" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "core-hour" ]
languages = []
sdk = [ "Compute" ]
title = "Licensing & Billing"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://www.grasshopper3d.com/forum/topics/how-do-i-install-a-custom-ghx"
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


## About Core-Hour Billing

When Rhino is logged in to a service account and is running on a Windows Server-based operating system, you will be billed **$0.10 per core per hour** that Rhino is running (pro-rated per minute).

***Example 1:** Rhino running on a 32-core server for one hour:*

  * 1 computer * 32-cores * 1 hour * $0.10/core-hour = $3.20

***Example 2:** Rhino running on 200 4-core servers for 6 minutes:*

  * 200 computers * 4 cores * 0.1 hour * $0.10/core-hour = $8.00

***Example 3:** 1 Rhino instance running on a 2-core server 8 hours a day for 30 days:*
  * 1 computer * 2 cores * 8 hours/day * 30 days/month * $0.10/core-hour = $48/month

***Example 4:** 10 Rhino instances running on a 2-core server 8 hours a day for 30 days:*
  * 1 computer * 2 cores * 8 hours/day * 30 days/month * $0.10/core-hour = $48/month
  * (Notice that the number of instances of Rhino does not affect your bill)

**Billing is based on uptime**, not on usage - we don’t track the activity of each core, just that you have one running with Rhino. You can scale your workloads up and down to optimize performance and cost to you.

**Multiple instances are allowed** - you may run as many instances of Rhino on the same machine as you want, and the cost will be the same as running one instance.

## Setting Up Core-Hour Billing

Core-hour billing is required when running Rhino on a Windows Server-based operating system.

1. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) (login to your Rhino account if prompted).
2. Click _Create New Team_ and create a team to use for your compute project. {{< call-out "note" "Note" >}}
Creating a new team is not strictly required, but core-hour billing is *not compatible* with existing licenses in the team. So if your team has licenses in it, core-hour billing will not be allowed.
{{< /call-out >}}

3. Click _Manage Team_ -> _Manage Core-Hour Billing_.
4. Check the checkbox next to the products you want to enable. \
**Note, if you've had a team running for years, you may need to enable newer versions of Rhino.**
5. Click _Save_, and enter payment information when prompted for your new team.

## Using Core-Hour Billing

1. Go to the [Licenses Portal](https://www.rhino3d.com/licenses?_forceEmpty=true) and select the team that you just set up with Core-hour billing.
1. Click _Manage Team_ -> _Manage Core-Hour Billing_.
2. Click _Action_ -> _Get Auth Token_ to get a token.
3. Create a new environment variable with the name `RHINO_TOKEN` and use the token as the value. Since the token is too long for Windows' Environment Variables dialog, it's easiest to do this via a PowerShell command.

    ```ps
    [System.Environment]::SetEnvironmentVariable('RHINO_TOKEN', 'your token here', 'Machine')
    ```

From now on, when you start Rhino on this machine it will use your core-hour billing team.

{{< call-out "warning" "Warning" >}}
<strong>Warning!</strong> This token allows anyone with it to charge your team at will. Do <strong>NOT</strong> share this token with anyone.
{{< /call-out >}}

## Single-Computer licensing Not Supported

When running on Windows Server, it is not possible to enter a license key to run as a single-computer license, as Rhino requires a license per core.

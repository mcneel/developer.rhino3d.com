+++
aliases = ["/5/guides/compute/configure-https/", "/6/guides/compute/configure-https/", "/7/guides/compute/configure-https/", "/wip/guides/compute/configure-https/"]
authors = [ "andy.payne" ]
categories = [ "Deployment" ]
keywords = [ "developer", "compute", "production", "AWS" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Configure Compute to use HTTPS"
type = "guides"
weight = 5
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

In this guide, we will walk through the process of creating a valid SSL certificate so that Rhino.Compute can communicate with clients using the HTTPS protocol.

## Prerequisites

First, a few prerequisites must be completed.

1. You must have an active virtual machine (VM) instance. Use the following guides to walk through setting up a VM.

    * [Create a Virtual Machine on Azure](../creating-an-Azure-VM).
    * [Create a Virtual Machine on AWS](../creating-an-aws-vm).

1. The VM must be accessible to the web (open port 80, and 443).

1. A static public IPv4 address associated with your virtual machine.

1. An existing domain and access to its DNS settings.

1. An A-record in your DNS settings must point to the public IPv4 address of your virtual machine. For example, the procedure for the GoDaddy domain registrar is as follows:

    * Sign in and select the custom domain you want to use
    * In the **Domains** section, select **Manage All**, then select **DNS | Manage Zones**/
    * For the **Domain Name**, enter your custom domain, then select **Search**.
    * From the **DNS Management Page**, select **Add**, then select *A* in the Type list.
    * Complete the fields of the *A* entry:
        * Type: Leave **A** selected
        * Host: Enter @
        * Points to: Enter the public IP address of your virtual machine
        * TTL: Leave the default value
    * Select **Save**.
    
    The A-record will be added to the DNS records table. It usually takes about an hour for the DNS to propagate, although it can sometimes take up to 48 hours. You can use tools such as [https://www.whatsmydns.net](https://www.whatsmydns.net/) to check your DNS record against servers located in different parts of the world.

## Modify the Host Name

Before we step through the process of generating an SSL certificate, we need to make one modification to our existing IIS configuration for Rhino.Compute.

1. If you have not already done so, log into your VM (via RDP). See the section [Connect via RDP](../deploy-to-iis/#connect-via-rdp) for more details.

1. On the **Start** menu, click in the search area and type *Internet Information Services (IIS) Manager*. Click to launch the app.

1. In the IIS Manager, **click** on the web server node in the **Connections** panel on the left to expand the menu tree. Then **click** on the **Sites** node to expand the sub-menu. Lastly, select the **Rhino.Compute** node from the menu tree to adjust its settings.

1. In the **Actions** pane on the right, click **Bindings**. {{< image url="/images/Site_Binding_2.png" alt="/images/Site_Binding_2.png" class="image_center" width="100%" >}}

1. In the **Site Bindings** pane, select the row whose **Type** is set to **http**. On the right-hand side, click the **Edit** button.

1. In the **Host name** text field, type in the subdomain name that you created when setting up the A-Record. Click **OK** when done.
{{< image url="/images/Site_Binding_1.png" alt="/images/Site_Binding_1.png" class="image_center" width="80%" >}}

## Generate the Certificate

The next step in the process is to create and install an SSL certificate for the local IIS server. An SSL certificate is a digital certificate that authenticates a website's identity and enables an encrypted connection. It is required in order to use the HTTPS protocol.

To generate the certificate, we recommend using [Win-ACME](https://www.win-acme.com/). Win-ACME is a simple interactive client which can create and install the certificate as well as handle renewing the certificate when needed.

1. [Download the Win-ACME Client](https://github.com/win-acme/win-acme/releases/download/v2.2.2.1449/win-acme.v2.2.2.1449.x64.pluggable.zip) on the virtual machine. Note: Win-ACME is distributed as .zip file.

1. Right-click on the download .zip file and select **Extract All**. It doesn't really matter what directory you choose to extract the files to as we will manually move/rename them in the next step. Click **Extract**.

1. Select the newly extracted directory and type **Ctrl+X** to **Cut** and then **Ctrl+V** to **Paste** this folder into the root <i>C:\\</i> drive. 

1. Now, right-click on the directory that you just copied to the <i>C:\\</i> drive and select **Rename** from the menu. Shorten the folder name to just *"win-acme"*. 
{{< image url="/images/win_acme_1.png" alt="/images/win_acme_1.png" class="image_center" width="100%" >}}

1. Click on the Windows Start menu and type in "Powershell". In the menu that appears, right-click on the **Windows Powershell app** and choose **Run As Administrator**.

1. Type in the following command and hit **Enter** to launch the Win-ACME application.
```powershell
    C:\win-acme\wacs.exe
```
1. You should see an interactive menu appear with a set of instructions which can be run by typing in a specific letter.
{{< image url="/images/win_acme_2.png" alt="/images/win_acme_2.png" class="image_center" width="100%" >}} 

1. Type the letter **N** and hit **Enter** to create a certificate with the default settings. You should see a list of available IIS sites that are available. If you do not see an entry for **Rhino.Compute (1 binding)** then it is likely that you have not set the host name correctly in the previous step. See the section on [modifying the host name](#modify-the-host-name).
{{< image url="/images/win_acme_3.png" alt="/images/win_acme_3.png" class="image_center" width="100%" >}} 

1. Type the number associated with the row for **Rhino.Compute (1 binding)** and hit **Enter**.

1. Hit **Enter** again to accept the default **Pick all bindings**.

1. When prompted to *Continue with this selection?* hit **Enter** or type **Y** for yes.
{{< image url="/images/win_acme_4.png" alt="/images/win_acme_4.png" class="image_center" width="100%" >}} 

1. When prompted to *Open in default application?* hit **Enter** or type **Y** for yes.

1. When prompted *Do you agree with the terms?* hit **Enter** or type **Y** for yes.

1. Enter a valid email(s) address to receive notifications about problems or abuses with this certificate. Hit **Enter** when the email address has been provided.
{{< image url="/images/win_acme_5.png" alt="/images/win_acme_5.png" class="image_center" width="100%" >}} 

Congratulations. If successful, the application will then run a series of authorization and validation tests to confirm host is secure. Win-ACME will then generate the SSL certificate and install it with IIS and add a new binding **(*:443)** to the Rhino.Compute site. The SSL certificate will be valid for 90 days. However, the Win-ACME application will create a task scheduler which will try to renew the certificate after 60 days. You should now be able to send an HTTPS request to your Rhino.Compute server and get a valid response back.

{{< image url="/images/win_acme_6.png" alt="/images/win_acme_6.png" class="image_center" width="95%" >}} 

<br>

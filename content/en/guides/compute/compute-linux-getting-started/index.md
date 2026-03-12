+++
aliases = []
authors = [ "luis" ]
categories = [ "Getting Started" ]
description = "A guide to getting started with Rhino.Compute on Linux"
keywords = [ "developer", "compute", "faq", "linux" ]
languages = []
sdk = [ "Compute" ]
title = "Getting Started with Rhino.Compute on Linux"
type = "guides"
weight = 10
override_last_modified = "2025-05-07T09:45:21Z"

[admin]
TODO = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac", "Linux" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

{{< call-out "warning" "Warning" >}}

- This project is part of the Rhino WIP (work in progress) and as such should be considered WIP software. We do not recommend using this for production work.
- Things we are still working on:
  - GH: RhinoCode enabled script components 
  - File IO: Importing and exporting files other than 3dm
  - 3rd Party Plug-in Management. There is currently no mechanism to load 3rd party plugins, other than what can be installed by the yak-cli and only in cases where the package includes a GHA for Grasshopper to load.
  - Probably many other things

{{< /call-out >}}

## Prerequisites
- A system capable of running Ubuntu Server 24.04 or AmazonLinux 2023. The steps in this guide should also work for Debian 13. This system can exist locally as a docker container or a VM, or it can be set up in production environments that support Linux instances.
- A Core-Hour Billing Token. Follow this guide to get a token: https://developer.rhino3d.com/guides/compute/core-hour-billing/#setting-up-core-hour-billing 

{{< call-out "warning" "Warning" >}}
Your core-hour billing token allows anyone with it to charge your team at will. Do <strong>NOT</strong> share this token with anyone.
{{< /call-out >}}

## Provision System

Rhino.Compute on Linux has been tested to run on Ubuntu Server 24.04 and AmazonLinux 2023. You can run these systems as virtual machines or in docker containers on macOS, Windows, or Linux.

We have also tested running Rhino.Compute on Linix on AWS EC2 and Azure instances.

### Containers (Docker)

Running rhino-compute in a container is a straightforward way of getting started, but is not recommended for production environments as docker containers lack the systemd service manager which enables the start of the rhino-compute service when the system reboots. At the time of writing, we are typically developing on Ubuntu 24.04 and ensuring that things work on AmazonLinux 2023. There has been no additional effort to ensure these instructions work on Debian 13, other than testing them on this base image.

1. Install Docker - You need either Docker Desktop (macOS, Windows, Linux Desktop) of Docker Engine (Linux, CLI)
    - Desktop: https://docs.docker.com/get-started/get-docker/
    - Engine: https://docs.docker.com/engine/install/ 
2. Start container

```bash
docker run --rm -it -p 5000:5000 amazonlinux:2023 /bin/bash
```

or 

```bash
docker run --rm -it -p 5000:5000 ubuntu:noble /bin/bash 
```

{{< call-out "note" "Note" >}}
Flags:
- <code>--rm</code>: remove the container after exit
- <code>-it</code>: interactive terminal (stdin and stdout).
- <code>-p 5000:5000</code>: port mapping [Host Port:Container Port]. Please note, your host OS might already have certain ports reserved. For example, macOS reserves port 5000 for AirPlay. In this case, you should choose a different HOST port: <code>-p 5001:5000</code>
- <code>amazonlinux:2023</code> or <code>ubuntu:noble</code>: the base image for the container. ubuntu:noble = Ubuntu 24.04. debian:trixie = Debian 13
- <code>/bin/bash</code>: start bash shell
{{< /call-out >}}

3. Continue to the setup section for your Linux distribution:
    - [Ubuntu](#ubuntu)
    - [AmazonLinux](#amazonlinux)

### VMs (Multipass, WSL, etc)

Running rhino-compute on a VM is a good way to test out how to run rhino-compute as a service, which is how it is meant to be run in production.

#### Multipass

Multipass can be used to run <strong>Ubuntu</strong> on macOS, Windows, and Linux host operating systems

1. Download [Multipass](https://canonical.com/multipass)
2. Create an instance. The recommendation for a lightweight local VM is to provision an instance with 4 cpus, 8gb ram, and 10gb of storage. After launching, you can open a shell right from the multipass interface.
3. Make a note of the IP address of the instance you just created, as that will be necessary for connecting to Rhino.Compute running on this VM.
4. Continue to the [Ubuntu](#ubuntu) setup.

#### WSL2

The Windows Subsystem for Linux (WSL2) can be used to run <strong>Ubuntu and AmazonLinux</strong> on a Windows 10 or 11 host operating system. 

{{< call-out "note" "Note" >}}
While it should be possible, we have yet to setup and test AmazonLinux on WSL2
{{< /call-out >}}

1. Install the default Ubuntu image
```powershell
wsl --install
```
2. Continue to the setup section for your Linux distribution:
    - [Ubuntu](#ubuntu)
    - [AmazonLinux](#amazonlinux)

### Production Environment (AWS, Azure, etc)

#### AWS EC2
TODO
#### Azure
TODO
### Other

#### Raspberry Pi

We have tested running Rhino.Compute on a rpi 400 running Ubuntu. It is highly recommended to use the advanced settings in the [RPi imager](https://www.raspberrypi.com/software/) to add your wifi credentials and a ssh key so that your rpi can connect to the internet. https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview. After you complete this, you can follow the [Ubuntu](#ubuntu) setup.

## Setup

{{< call-out "warning" "Important" >}}
If you are on a VM or Production Environment, switch to root first: <code>sudo -s</code>
{{< /call-out >}}

### Ubuntu

1. Install dependencies

```bash
# dotnet
wget https://dotnet.microsoft.com/download/dotnet/scripts/v1/dotnet-install.sh -O dotnet-install.sh
chmod +x ./dotnet-install.sh
./dotnet-install.sh --version 9.0.102 --install-dir /usr/share/dotnet
```

2. Add mcneel-packages to package sources

```bash
# Import the GPG key
wget -qO- https://mcneel-packages.s3.amazonaws.com/mcneel-packages.gpg.key | gpg --dearmor -o /usr/share/keyrings/mcneel-archive-keyring.gpg

# Add repository
echo "deb [signed-by=/usr/share/keyrings/mcneel-archive-keyring.gpg] https://mcneel-packages.s3.amazonaws.com/deb stable main" | tee /etc/apt/sources.list.d/mcneel.list
```

3. Install rhino-compute

```bash
apt update && apt install -y rhino-compute
```

4. Set the <code>RHINO_TOKEN</code>

The <code>RHINO_TOKEN</code> is your [Core-Hour Billing](/guides/compute/core-hour-billing/#setting-up-core-hour-billing) token.

{{< call-out "warning" "Warning" >}}
Your core-hour billing token allows anyone with it to charge your team at will. Do <strong>NOT</strong> share this token with anyone.
{{< /call-out >}}

```bash
cp /etc/rhino-compute/environment.example /etc/rhino-compute/environment
nano /etc/rhino-compute/environment

# control + x, y, enter to save the file and exit nano
```

5. Optional: Install yak-cli to install 3rd party packages.

{{< call-out "note" "Note" >}}
Expect that 3rd party plugins will not work at this time. Only packages that are marked "-any" (i.e. <code>package-0.0.0-\<some rhino version>\_any.yak</code>) will be installed, and only packages with Grasshopper add-ons will be loaded. We are actively working on expanding the support for loading 3rd party plugins on Rhino.Compute on Linux.
{{< /call-out >}}

```bash
apt install yak-cli
```

6. Continue to the [Run rhino-compute](#run-rhino-compute) section. 

### AmazonLinux

1. Install dependencies

{{< call-out "note" "Note" >}}
Install additional dependencies if you are running AmazonLinux in a container
```bash
dnf install -y wget tar gzip nano findutils
```
{{< /call-out >}}

```bash
# dotnet
wget https://dotnet.microsoft.com/download/dotnet/scripts/v1/dotnet-install.sh -O dotnet-install.sh
chmod +x ./dotnet-install.sh
./dotnet-install.sh --version 9.0.102 --install-dir /usr/share/dotnet
```

2. Add mcneel-packages to package sources

```bash
wget -O /etc/yum.repos.d/mcneel.repo https://mcneel-packages.s3.amazonaws.com/rpm/repos/mcneel-amzn2023.repo
```

3. Install rhino-compute

```bash
dnf install -y rhino-compute
```

4. Set the <code>RHINO_TOKEN</code>

The <code>RHINO_TOKEN</code> is your [Core-Hour Billing](/guides/compute/core-hour-billing/#setting-up-core-hour-billing) token.

{{< call-out "warning" "Warning" >}}
<strong>Warning!</strong> Your core-hour billing token allows anyone with it to charge your team at will. Do <strong>NOT</strong> share this token with anyone.
{{< /call-out >}}

```bash
cp /etc/rhino-compute/environment.example /etc/rhino-compute/environment
nano /etc/rhino-compute/environment

# control + x, y, enter to save the file and exit nano
```

5. Optional: Install yak-cli to install 3rd party packages.

{{< call-out "note" "Note" >}}
Expect that 3rd party plugins will not work at this time. Only packages that are marked "-any" (i.e. <code>package-0.0.0-\<some rhino version>\_any.yak</code>) will be installed, and only packages with Grasshopper add-ons will be loaded. We are actively working on expanding the support for loading 3rd party plugins on Rhino.Compute on Linux.
{{< /call-out >}}

```bash
dnf install -y yak-cli
```

6. Continue to the [Run rhino-compute](#run-rhino-compute) section. 

{{< call-out "note" "Note" >}}
If you are running AmazonLinux in a container, access on the container from the host with http://localhost:5001 or whichever port you have set in [docker run](#containers-docker)
{{< /call-out >}}

## Run Rhino.Compute

{{< call-out "warning" "Important" >}}
If you had previously run the setup as root (<code>sudo -s</code>), please exit root now and return to the default user:
```bash
exit
```
{{< /call-out >}}

### VM or Production Environments

- Start the Rhino.Compute service
```bash
sudo systemctl start rhino-compute
```
- Stop the Rhino.Compute service
```bash
sudo systemctl stop rhino-compute
```
- Enable automatic startup of the Rhino.Compute service on system reboot
```bash
sudo systemctl enable rhino-compute
```
- Check the status of the service
```bash
sudo systemctl status rhino-compute
```
- Follow real-time logs
```bash
sudo journalctl -u rhino-compute -f
```

### Containers
```bash
rhino-compute-start
```

{{< call-out "note" "Note" >}}
Logs are written to <code>/var/log/rhino-compute</code> on the system running Rhino.Compute
{{< /call-out >}}

## Solve a Grasshopper definition on Rhino.Compute

This section requires the Host computer to have Rhino 8 or Rhino WIP with Hops installed for Grasshopper. Grasshopper should have the IP of the VM or container, as well as the API Key, which is the same as the <code>RHINO_TOKEN</code> set in the [Setup](#setup). It also helps to have a definition ready to pass to Hops.

1. Open Rhino 8 or WIP, open GH, and navigate to the Grasshopper Solver Settings.
2. In the text field under "Hops - Compute server URLs", enter in the IP and port of your Linux system
3. In the text field next to "API Key" enter in your Core-Hour Billing token aka the <code>RHINO_TOKEN</code>.
4. Drag the Hops component onto the canvas and reference a definition. If you are following the logs in real-time, you should see your Linux system start to log events related to Rhino.Compute.





    

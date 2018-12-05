---
title: Digitally Signing Zoo Plugins
description: This guide discusses how to digitally sign Zoo and Rhino plugins.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['RhinoCommon', 'C/C++']
languages: ['BAT']
platforms: ['Windows']
categories: ['Zoo']
origin: http://wiki.mcneel.com/developer/digital-signatures/create-request
order: 5
keywords: ['Zoo', 'Plugin', 'Digital']
layout: toc-guide-page
TODO: 'move out of Zoo because it applies to both Zoo and Rhino plugins'
---


## Overview

To add plugins to Zoo, and to call the license functions from within your Rhino plugin, you must digitally sign your plugins using a certificate signed by the *Robert McNeel & Associates Code Signing Authority*.

## Generate Private Key & Certificate Signing Request

Follow these steps to generate the necessary info to forward to *Robert McNeel & Associates Code Signing Authority*...

1. Download and install the latest [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html). Note, download and installing the "light" version (smaller download) is sufficient.
2. Save the contents of <a href="{{ site.baseurl }}/files/mcneelcodesigning.zip"><span class="glyphicon glyphicon-download"></span></a> [mcneelcodesigning.zip]({{ site.baseurl }}/files/mcneelcodesigning.zip) into a folder where you have write permissions. This is generally in your plugin project folder.
3. Start a *Windows Command Prompt*.
4. Add the OpenSSL installation folder to your Windows path: `set path=C:\OpenSSL-Win32\bin;%path%`
5. From the command prompt, run `CreateRequest.bat <filename>`, where *filename* is the name (without an extension) that will be used to save your private key (*.key*), certificate signing request (*.csr*), and final signed digital certificate (*.crt*).
6. You will be prompted to answer some questions.  Be sure to answer them correctly...

```cmd
C:\Dev\Zoo> CreateRequest.bat TestZooPluginKey
Loading 'screen' into random state - done
Generating RSA private key, 4096 bit long modulus
................................................................................
e is 65537 (0x10001)
Loading 'screen' into random state - done
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) []: <COUNTRY NAME>
State or Province Name (full name) []: <STATE OR PROVINCE>
Locality Name (eg, city) []: <CITY>
Organization Name (eg, company) []: <ORGANIZATON>
Organizational Unit Name (eg, section) []: <ORGANIZATIONAL UNIT>
Common Name (eg, your websites domain name) []: <DOMAIN NAME>

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []: <PASSWORD>

Saved private key: 'TestZooPluginKey.key'
Saved CSR: 'TestZooPluginKey.csr'
```

## Requesting a Signed Digital Certificate

1. Email the certificate signing request (*.csr*) created above to <a href="mailto:brian@mcneel.com"><span class="glyphicon glyphicon-envelope"></span></a> [Brian Gillespie](mailto:brian@mcneel.com) along with a certificate request.
2. We will process your request and, if it is approved, will send you a signed digital certificate (*.crt*).

## Creating a Personal Information Exchange

To digitally sign your Zoo or Rhino plugin, convert the signed digital certificate (*.crt*), emailed to you upon approval, into a personal information exchange (*.pfx*) file...

1. Copy the signed digital certificate (*.crt*) you receive into the same folder as your private key (*.key*) and certificate signing request (*.csr*).
2. Start a *Windows Command Prompt*.
3. Add the OpenSSL installation folder to your Windows path: `set path=C:\OpenSSL-Win32\bin;%path%`
4. From the command prompt, run `MakePfxFile.bat <filename>`, where *filename* is the name (without an extension)...

```cmd
C:\Dev\Zoo\TestZooPlugin>MakePfxFile.bat TestZooPluginKey
Loading 'screen' into random state - done
Enter Export Password: <PRESS ENTER>
Verifying - Enter Export Password: <PRESS ENTER>
Created 'TestZooPluginKey.pfx'. Use this to sign your executable code.
```

## Sign Your Plugins

Now that you have a personal information exchange (*.pfx*), you can use it to sign Zoo and Rhino plugins. 

1. Open a *Visual Studio Command Prompt*.
2. Use *Signtool.exe*, with the following syntax, to digitally sign your plugins...

```cmd
signtool.exe sign /f <filename>.pfx /t http://timestamp.verisign.com/scripts/timstamp.dll /v <plugin>
```

For example:

```cmd
C:\Dev\Zoo\TestZooPlugin> signtool sign /f TestZooPluginKey.pfx /t http://timestamp.verisign.com/scripts/timstamp.dll /v TestZooPlugin.dll
The following certificate was selected:
    Issued to: MCNEEL.COM
    Issued by: McNeel Software Development
    Expires:   <DATE>
    SHA1 hash: <HASH>

Done Adding Additional Store
Successfully signed and timestamped: TestZooPlugin.dll

Number of files successfully Signed: 1
Number of warnings: 0
Number of errors: 0
```

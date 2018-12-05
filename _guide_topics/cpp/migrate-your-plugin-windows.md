---
title: Migrate your plugin project to Rhino 6
description: This guide walks you through using migrator.exe.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
origin: unset
order: 6
keywords: ['c', 'C/C++', 'plugin']
layout: toc-guide-page
---

## Prerequisites

It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Windows)]({{ site.baseurl }}/guides/cpp/installing-tools-windows)

## Run the Migration Application

1. Download [cpp-migrator.zip](http://www.rhino3d.com/download/rhino/6.0/v6-cpp-migrator)
2. Unzip the downloaded file into it's own folder.
3. Backup your plug-in project and source code. This tool modifies your source in place.
4. Open a Windows command prompt and navigate to the folder where you unzipped the utility.
5. Run `migrator.exe [plugin_directory]`, where `[plugin_directory]` is the full path to the plug-in source folder.

Your plugin project should now be ready to build with the Rhino 6 C/C++ SDK.

## Related Topics

- [What's New?]({{ site.baseurl }}/guides/general/whats-new)
- [Migrate your plugin project to Rhino 6 manually]({{ site.baseurl }}/guides/cpp/migrate-your-plugin-manual-windows)

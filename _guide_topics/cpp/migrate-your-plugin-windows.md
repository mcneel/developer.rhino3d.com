---
title: Migrate your plugin project to Rhino 6
description: This guide walks you through using `migrator.exe`.
authors: ['Dale Fugier']
author_contacts: ['dale']
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

[These Windows development tools installed]({{ site.baseurl }}/guides/cpp/installing-tools-windows).

## Run the Migration Application

1. Download [cpp-migrator.zip](http://www.rhino3d.com/download/rhino/6.0/v6-cpp-migrator)
1. Unpack the plugin
1. Backup your plug-in project and source code. This tool modifies your source in place.
1. Run `migrator.exe [plugin_directory]` from the Windows command prompt. 
`[plugin_directory]` is the full path to the plug-in source folder.

Your plugin project should now be ready to build with the Rhino 6 C/C++ SDK.

## Related Topics

- [What's New?]({{ site.baseurl }}/guides/general/whats-new)
- [Migrate your plugin project to Rhino 6 manually]({{ site.baseurl }}/guides/cpp/migrate-your-plugin-manual-windows)

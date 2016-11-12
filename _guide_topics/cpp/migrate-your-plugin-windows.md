---
title: Migrate your plugin project to Rhino 6
description: This guide walks you through migrating your Rhino 5 plugin project to Rhino 6.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
order: 6
keywords: ['c', 'C/C++', 'plugin']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Windows)]({{ site.baseurl }}/guides/cpp/installing-tools-windows).

## Run the Migration Application

1. Download [cpp-migrator.zip](http://www.rhino3d.com/download/rhino/6.0/v6-cpp-migrator)
1. Unpack the plugin
1. Make a backup of your plug-in project and all source code. This tool modifies your source in place.
1. From the Windows command prompt, run `migrator.exe [plugin_directory]`
where [plugin_directory] is the full path to the folder where your plug-in source lives.

Your plugin project should now be ready to build with the Rhino 6 C/C++ SDK.

## Related Topics

- [What is a Rhino Plugin?]({{ site.baseurl }}/guides/general/what-is-a-rhino-plugin)
- [Installing Tools (Windows)]({{ site.baseurl }}/guides/cpp/installing-tools-windows)
- [Migrate your plugin project to Rhino 6 manually]({{ site.baseurl }}/guides/cpp/migrate-your-plugin-manual-windows)

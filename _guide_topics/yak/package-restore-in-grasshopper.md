---
title: Package Restore in Grasshopper
description: How can Grasshopper use Yak to make your life easier?
authors: ['Will Pearson']
author_contacts: ['will']
sdk: ['Yak']
languages:
platforms: ['Windows']
categories: ['Features']
order: 1
keywords: ['yak', 'grasshopper']
layout: toc-guide-page
---

## Overview

For starters, this is less of a developer guide and more of a description of how
this feature works, so that you, the developer, can better understand how your
package and plug-in needs to be set up in order to leverage it.

<!-- One of the key features of having a writing a bespoke package management system
for Rhino is that  -->

One of the biggest problems that Yak is supposed to help with is that of
automatically fetching packages when you try to open a Grasshopper definition
that uses plug-ins which aren't installed.

![Package restore can still operate when the plug-in name doesn't match the package]({{ site.base_url }}/images/yak-gh-restore-guid.gif)
![Package restore can still operate when the plug-in name doesn't match the package]({{ site.base_url }}/images/yak-gh-restore-guid.png)
![Package restore can still operate when the plug-in name doesn't match the package]({{ site.base_url }}/images/yak-gh-restore.gif)

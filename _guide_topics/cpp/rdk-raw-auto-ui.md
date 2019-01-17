---
title: RDK Automatic UI
description: This document describes how to use the RDK's automatic UI classes in C/C++.
authors: ['john_croudy']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin', 'UI']
layout: toc-guide-page
---

<div class="bs-callout bs-callout-danger">
  <h4>UNDER CONSTRUCTION</h4>
  <p>This guide has yet to be written. Please check back soon for updates.

<!--

### Introduction
The RDK provides a user interface that integrates into Rhino's docking panel system and separates different areas by using collapsible sections, or roll-ups. There are several areas where these sections appear; in the render content UI, in the _Rendering_ panel, and in the _Sun_ panel. Each of these areas allows the plug-in developer to add customized sections. Creating these sections can take a lot of work, especially when using MFC on Windows. Sometimes it's convenient, especially when prototyping, to be able to just see and edit a collection of values quickly. The RDK provides an automatic UI system for just that purpose. There are two ways to use this system. The _raw_ automatic UI provides access to the entire system and allows control of almost every aspect of the interface. The _Content Automatic UI_ uses the raw system internally to expose a much simpler interface suitable for quickly developing UIs for render contents. The latter is described in detail in the discussion of [render contents](/guides/cpp/rdk-render-content/#UI). The former, a more complicated interface, is described here.

### Getting started
Using the automatic UI at this level requires you to provide a _data source_ that is capable of converting your data items to a form the automatic UI can understand. This form is called a _param block_ and uses the `IRhRdkParamBlock` interface. The data source must respond to `GetData(uuidData_RdkParamBlock)` and populate a param block object which is returned as a pointer to `IRhRdkParamBlock`.

TODO: finish this

### Summary
-->

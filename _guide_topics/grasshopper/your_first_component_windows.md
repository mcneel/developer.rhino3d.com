---
title: Your First Component (Windows)
description: This guide has yet to be authored or ported.
author: dan@mcneel.com
apis: ['Grasshopper']
languages: ['C#', 'VB']
platforms: ['Windows']
categories: ['Overview']
origin: unset
order: 3
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
TODO: 'Needs testing and elaboration.  Should be back-ported to master (Rhino 5)'
---

# {{ page.title }}

{{ page.description }}

## Create your component
1. Open *Visual Studio*
2. From the *File* menu, click *New* then click *Project...*
3. In the New Project dialog box, select *Installed > Templates > Visual C# > Rhinoceros* then select *Grasshopper Add-On for v6*
4. Enter a name and location for the project
5. Click *OK*
6. Fill out information about your first component:
    1. Name: the name of the component as displayed in the ribbon bar and search menus  
    2. Nickname: the default name of the component when inserted into the canvas
    3. Description: description shown in tooltip when mouse is over the component icon in the menu
    4. Category: name of tab where component icon will be shown
    5. Sub Category: name of group inside tab where icon will be shown
6. Download [GrasshopperSDK.chm](http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm) and read about how to set up component inputs, output, and solve the component in the Examples.

## Preparing to Debug Your Component
1. Set your project as the start-up project in Visual Studio.
2. From the *Debug* menu in Visual Studio, click *Start Debugging*
3. After Rhino starts, run the *GrasshopperDeveloperSettings* command
4. Clear the *Memory load .GHA assemblies using COFF byte arrays* checkbox
5. Click *Add Folder* and add the bin\Debug output folder of your project to Grasshopper's search path
6. (Optional) Automatically start Grasshopper every time Rhino starts
    1. From the *Tools* menu, click *Options*, then click *General*
    2. In the *Run these commands every time Rhino starts* text area, type *_Grasshopper* then click *OK*
7. Close Rhino

## Debugging your Component
1. Set breakpoints as needed
2. From the *Debug* menu in Visual Studio, click *Start Debugging*

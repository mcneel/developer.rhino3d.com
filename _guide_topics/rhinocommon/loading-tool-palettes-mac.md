---
title: Loading Tool Palettes (Mac)
description: This guide covers how to create and load a tool palette collection from your RhinoCommon plugin in Rhino for Mac.
authors: ['dan_rigdon_bel']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Mac']
categories: ['Fundamentals']
origin: unset
order: 7
keywords: ['RhinoCommon', 'Tool', 'Palette', 'Collection', 'RUI']
layout: toc-guide-page
---


## Prerequisites

This guide presumes that you have a RhinoCommon plugin that has commands that can be run from a tool palette.  In Rhino for Windows, this UI is normally stored in an *rui* file that includes the buttons, the icons, and their associated commands.  If you do not yet have a plugin, please begin with the [Your First Plugin (Mac)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-mac) guide.

## Overview

There are three steps in creating and loading a tool palette collection for your plugin in Rhino for Mac:  

1. The first step is to [create (or convert) a tool palette collection](#create-or-convert-a-tool-palette-collection) that calls the appropriate commands - or to convert a Rhino for Windows *.rui* file - to *ToolPaletteCollection.plist* file.  
1. The second step is to [add this *.plist* in your plugin project](#add-the-palette-to-your-project) as a resource.  
1. The third and final step is to tell Rhino for Mac to [load the tool palette from the appropriate file](#load-the-tool-palette) when your plugin is being loaded.

## Create or Convert A Tool Palette Collection

If you are familiar with the [Command Editor](http://docs.mcneel.com/rhino/mac/help/en-us/index.htm#macpreferencesandsettings/commands.htm) in Rhino for Mac, you are already well on your way to understanding how to create a custom tool palette collection for use in your plugin.  If not, don't worry: creating a tool palette collection is relatively easy.  

If you already have an existing *rui* file from Rhino for Windows, this job is even easier: you can [import that *rui* and convert it to a *plist*](#convert-rui-to-plist).

### Creating from Scratch

1. Open Rhino - if it is not already open - and start a new modeling window.
1. Enter the `TestEditToolPaletteCollection` command.  (You will need to type the entire command; it will not autocomplete).  This launches a developer tool similar to the Command Editor where tool palette collections can be created, organized, and saved to *plist* files...
1. By default, the `TestEditToolPaletteCollection` editor presumes you have a Rhino for Windows *rui* file you would like to convert.  A finder window opens where you can navigate to the *rui* file to import.  
1. If you do not have a Rhino for Windows *rui* file that you would like to convert, you will need to create your Tool Palette Collection "from scratch."  On the finder window, press *Cancel*.  An interface much like the [Command Editor](http://docs.mcneel.com/rhino/mac/help/en-us/index.htm#macpreferencesandsettings/commands.htm) window appears.  This is where you can create, configure, organize, and save your tool palette collection.
1. Press the *+* (add) button in the *Palette Browser*...
![TestEditToolPaletteCollection]({{ site.baseurl }}/images/loading-tool-palettes-mac-01.png)
1. An *Untitled* tool palette appears in the *Palette Browser* (upper left).  Click on the name of the *Untitled* palette and give your tool palette a name...
![Name Tool Palette]({{ site.baseurl }}/images/loading-tool-palettes-mac-02.png)
1. In the *Command Button Browser* (the area in the lower-left corner), click the *+* button to *add a new button*.  An *Untitled* button should appear.  Select it.
![Add a button]({{ site.baseurl }}/images/loading-tool-palettes-mac-03.png)
1. In the *Button Editor* (area at lower-right), you can configure your button.  Add a Text title, some Menu text, some informative tooltip, and - most importantly - the macro or command (from your plugin) that you wish to run when this button is clicked.
![Button Editor]({{ site.baseurl }}/images/loading-tool-palettes-mac-04.png)
1. You can drag new images onto the button icon displayed in the *Button Editor*.  Rhino for Mac prefers PDF icons as they will scale nicely between Retina and non-Retina displays.  If you do not have PDF assets for your icons, use 64 x 64 png images.
![Add a PNG]({{ site.baseurl }}/images/loading-tool-palettes-mac-05.png)
1. You may add as many buttons as you need to the *Command Button Browser*.  These are the buttons that can be added to Tool Palettes.
1. With the tool palette you want to add buttons to, drag buttons from the *Command Button Browser* into the *Palette Contents* area (top, center)...
![Add to Palette]({{ site.baseurl }}/images/loading-tool-palettes-mac-07.png)
1. When you are satisfied with the contents of your tool palette(s), you can save your converted tool palette collection to a *plist* by clicking on the *Save* button in the lower-right corner of the *Command Editor* window.
1. *NOTE*: Should you want to make changes to this tool palette collection, you can always reload the tool palette collection by re-running the `TestEditToolPaletteCollection` command and opening the *plist* file you created.  In order to add a menu to a tool palette button you must save and reload the tool palette in order for the menu to show up in the available menus.

### Convert RUI to plist

1. Open Rhino - if it is not already open - and start a new modeling window.
1. Enter the `TestEditToolPaletteCollection` command.  (You will need to type the entire command; it will not autocomplete).  This launches a developer tool similar to the Command Editor where tool palette collections can be created, organized, and saved to *plist* files...
1. By default, the `TestEditToolPaletteCollection` editor presumes you have a Rhino for Windows *rui* file you would like to convert.  A finder window opens where you can navigate to the *rui* file to import.  Navigate to the folder containing your *rui*, select it, click *Open*.  Rhino for Mac imports this *rui* and uses it as a template.
1. The contents of your *rui* should appear.  Notice that there is a *Modified Tool Palette* with the name of your toolbar(s)...
![Imported RUI]({{ site.baseurl }}/images/loading-tool-palettes-mac-06.png)
1. The buttons with their associated icons should appear in the *Command Button Browser* (the area in the lower-left corner).  If you select buttons in this area, you will notice their editable details appear in the *Button Editor* (area at lower-right).  
1. You can drag new images onto the button icon displayed in the *Button Editor*.  Rhino for Mac prefers PDF icons as they will scale nicely between Retina and non-Retina displays.  If you do not have PDF assets for your icons, use 64 x 64 png images.
1. With the tool palette you want to add buttons to, drag buttons from the *Command Button Browser* into the *Palette Contents* area (top, center)...
![Add to Palette]({{ site.baseurl }}/images/loading-tool-palettes-mac-07.png)
1. When you are satisfied with the contents of your tool palette(s), you can save your converted tool palette collection to a *plist* by clicking on the *Save* button in the lower-right corner of the *Command Editor* window.
1. *NOTE*: Should you want to make changes to this tool palette collection, you can always reload the tool palette collection by re-running the `TestEditToolPaletteCollection` command and opening the *plist* file you created.  In order to add a menu to a tool palette button you must save and reload the tool palette in order for the menu to show up in the available menus.

## Add the Palette to your Project

Now that you have Tool Palette Collection *plist*, you need to add it to your plugin as a resource.  The best practice is to create a folder within your project called *Resources* (or similar) and move your Tool Palette Collection *plist* into to that folder.  *NOTE*: You are free to place your *plist* anywhere you think appropriate.

1. Open *Visual Studio for Mac* if you have not done so already and open your plugin project.
1. Right-click your plugin project in the *Solution Explorer* and select *Add* > *New Folder*...
1. Name this folder *Resources* (or similar).
1. Right-click the new *Resources* folder in the *Solution Explorer* and select *Add* > *Add Files...*.
1. Navigate to the *plist* you saved and add it to the plugin project *Resources* folder.  When prompted, *Move* the *plist* to the plugin *Resources* project folder.
1. Select your *ToolPaletteCollection.plist* in *Solution Explorer* and open the *Properties* panel.
1. In the *Build* section of *Properties*, in the *Copy the output directory* entry, select *Copy if newer*.

## Load the Tool Palette

1. In order to load the tool palette, you must reference *RhinoMac.dll* and *Rhino.UI.dll*.  In *Visual Studio for Mac*, right-click on the project entry in the *Solution Explorer* and select *Tools* > *Edit File*.  This opens up the *csproj* file for your project as xml text in the code editor.
1. Find the area of the xml near where *RhinoCommon* is being referenced and add the following entries:

```
<Reference Include="Rhino.UI">
  <HintPath>\Applications\Rhinoceros.app\Contents\Frameworks\RhCore.framework\Versions\Current\Resources\Rhino.UI.dll</HintPath>
  <Private>False</Private>
</Reference>
<Reference Include="RhinoMac">
  <HintPath>\Applications\Rhinoceros.app\Contents\Frameworks\RhCore.framework\Versions\Current\Resources\RhinoMac.dll</HintPath>
  <Private>False</Private>
</Reference>
```
1. Close the *csproj* that is open in the code editor.  Visual Studio for Mac reloads the project.  If you check in the *References* section of your project in the *Solution Explorer*, you should see references to *RhinoMac* and *Rhino.UI*.
1. In your `Plugin` class, if you have not done so already, override the `OnLoad` method.
1. Load your tool palette plist from your desired location by calling the `RhinoMac.Runtime.MacPlatformService.LoadToolPaletteCollection` and passing in the full path to your *plist*.  For example, if your *plist* is in the *Resources* folder of your *rhp*, use the following example:

```cs
protected override Rhino.PlugIns.LoadReturnCode OnLoad (ref string errorMessage)
{
  var pluginPath = System.IO.Path.GetDirectoryName(Assembly.Location);
  var resourcesPath = System.IO.Path.Combine (pluginPath, "Resources");
  var plistPath = System.IO.Path.Combine (resourcesPath, "ToolPalette.plist");
  bool didLoad = RhinoMac.Runtime.MacPlatformService.LoadToolPaletteCollection (plistPath);
  if (!didLoad)
    System.Diagnostics.Debug.WriteLine("WARNING: Failed to load tool palette.");

  return base.OnLoad (ref errorMessage);
}
```

Your tool palette collection will be loaded and displayed when Rhino loads your plugin.

---

## Related Topics

- [Your First Plugin (Mac)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-mac)
- [Command Editor (from Rhino Help)](http://docs.mcneel.com/rhino/mac/help/en-us/index.htm#macpreferencesandsettings/commands.htm)

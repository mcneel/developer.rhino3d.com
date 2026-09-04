+++
aliases = ["/en/8/guides/general/rhino-ui-system/"]
authors = [ "dale", "callum" ]
categories = [ "Fundamentals" ]
description = "This guide outlines Rhino's User Interface System."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Rhino UI System"
type = "guides"
layout = "single"
weight = 3

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

This guide provides an overview of Rhino's User Interface (UI) system, and documents changes made in each version.


## Overview

Rhino's toolbars, menus and the commands behind them are all defined in **RUI files**. Everything below lives inside one of those files, and nothing in a file can reference anything outside it. Hover or tap any part of the diagram to see where it shows up in Rhino:

{{< rui-hierarchy >}}

### RUI Files

RUI files are collections of items — macros, toolbars, toolbar groups and menu items — and are stored in a text file. Changes to items in the file are saved automatically when Rhino is closed. You may open or close RUI files or manually choose to save a file at any time. The current version of a file is backed up and changes are saved to the file name. If a file gets damaged you can delete it and rename the backup file in an attempt to restore the previous version. If the backup file is damaged then nothing can be recovered.

Rhino plug-ins can install an RUI file with the same name as the plug-in and it will get copied into a writeable location and opened automatically when Rhino starts. This gives a plug-in the ability to extend the Rhino interface while allowing the plug-in to not load until it is referenced.

RUI Files can be managed using the **[Toolbar](https://docs.mcneel.com/rhino/{{< latest-rhino-version >}}/help/en-us/index.htm#options/appearance_toolbars.htm#(null))** command.

### Toolbar Groups

Toolbar groups are collections of references to toolbars from the same RUI file. Dragging a toolbar from one file to a group in another file results in the toolbar and its referenced macros being copied from the source file to the destination file. Toolbar groups can't reference Rhino panels.

### Toolbars

Toolbars are collections of Toolbar buttons. Toolbars also have a name and optionally an image representing them in a tab.

Toolbars can link to a group or a toolbar which will update the sidebar when that toolbar is made active. The sidebar is a panel on the left of the Rhino user interface.

### Toolbar Buttons

Toolbar buttons can contain left and/or right mouse click actions. Mouse click actions are assigned to macros which contain a script to run when clicked. Toolbar buttons display the image associated with the macro assigned to the left mouse action if present; if not, the right click macro image is used.

Toolbar buttons can optionally be configured to temporarily display other toolbars in a floating panel, known as a fly-out. This is similar in behaviour to the **[Pop Up Toolbar](https://docs.mcneel.com/rhino/{{< latest-rhino-version >}}/help/en-us/commands/popuppopular.htm#PopupToolbar)**.

Toolbar buttons can only reference macros from the same RUI file as the toolbar they belong to.

### Macros

Macros contain information needed to display or describe the command script that gets run when the macro is executed. Macro definitions include the following:

- Image which is displayed when possible
- Name
- Menu item text
- Command script to execute

### Menus

The Rhino menu system can be extended using menu items defined in an RUI file. The RUI file contains location information describing where to insert an item into the menu system. New menu items are defined by referencing a Macro which contains:

- Menu text
- Menu item image
- Command script which is run when the menu item is clicked on

<br/>


## Rhino 9

The goals of the Rhino 9 UI system were to:

- Simplify RUIs
- Improve and simplify on the prior 8 system
- 100% compatibility with moving files from Rhino 8 to 9 and back again
- Create a more fluid editing experience

### RUI Files

- RUI files are modified directly (again) without diffs exactly as Rhino 7 and prior worked
- Any links to other RUIs are resolved and copied into the RUI (except for fly-outs or sidebars)
- Diffs will be combined with the respective RUI on migrating to Rhino 9
- Every part of the RUI file (except menus) is now edited in one dialog, reached via the Toolbar command

#### Groups & Containers

Containers will not convert back to Toolbar Groups. To modify groups, edit them using the **[Toolbar](https://docs.mcneel.com/rhino/9/help/en-us/index.htm#options/appearance_toolbars.htm#(null))** command.

#### Macros

Macros have been simplified and no longer need editing separately, nor do they have their own dialog.

<br/>

## Rhino 8

{{< call-out "warning" "Caution" >}}
This section describes the Rhino 8 UI system, which is **superseded in Rhino 9**. Rhino 9 modifies RUI files directly again, the way Rhino 7 and earlier did. If you are targeting Rhino 9, read [Rhino 9](#rhino-9) above instead — the behaviour below does not apply.
{{< /call-out >}}

The goals of the Rhino 8 UI system were to:

- Display panels and toolbars in the same tabbed container.
- Reference toolbars and macros from multiple sources without having to copy definitions from one RUI file to another.
- Deliver Rhino User Interface (RUI) changes without overwriting or replacing existing files in Rhino or plug-in service releases. (In prior Rhino versions, replacing the RUI file to deliver updated toolbars and macros caused user changes to RUI files to be overwritten.)
- Quickly change the Rhino UI to display task-oriented tools.
- Share UI layouts amongst users.
- Allow users to arbitrarily modify the UI without having to be aware of the location or source of a UI component and to automatically track changes.
- Provide unified Windows and Mac UI.

The major changes in the Rhino 8 UI system are:

- Toolbar Groups auto-convert to Containers. Containers can display both panels and toolbars.
- RUI files are used to provide toolbar and macro libraries, and they are no longer modified directly. Rhino tracks RUI changes and applies them when loading. Doing this allows Rhino to deliver updated RUI files without losing user changes to a toolbar or macro.
- Window Layouts have been added and can be used to quickly switch between different UI configurations. They can be exported as files and will include modifications to toolbars and macros and user RUI files.

The Rhino 8 UI System is designed to allow referencing of UI components from many sources: including panels, toolbars, and macros, defined by any RUI file or plug-in. When Rhino closes, changes to the UI are saved and original RUI files are never modified unless specifically requested. Configurations of UI layouts can be saved, restored, exported and imported as Window Layouts and shared between Windows and Mac.

### Containers

Containers hold references to panels and toolbars. Toolbars can be referenced from any valid RUI source. Items are displayed as a tab in a container. Containers may be visible or hidden.

Containers can be modified by dragging tabs from one container into another, or by clicking on the container's `Gear` menu to add or remove references to panels or toolbars. The same panel may be referenced by multiple containers meaning it is possible to have the `Layers` tab, for example, displayed in multiple containers.

Container definitions, visibility, location, and size are saved when Rhino closes and restored when restarting Rhino. This information can also be stored and shared via Window Layouts.

Containers can be managed using Rhino's **[Containers](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/containers.htm#(null))** command.

Containers created from toolbar groups will do their best to synchronize any changes back to the RUI file, but this is not always possible.

### Window Layouts

Window Layouts are a snapshot of container definitions, visibility states, locations, and size. Restoring a Window Layout will reconfigure the current UI to make it appear as it did when the layout was created. Restored containers will display tabs in the order they were in when the Window Layout was created and will appear in the same location and size. Toolbar tabs will reference the current definition of a toolbar, if the toolbar no longer exists the tab will not be displayed.

Window Layouts can be managed using Rhino's **[WindowLayout](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/windowlayout.htm#(null))** command.

#### Exporting and Importing Window Layouts

Window Layouts may be exported to a Rhino Window Layout file (RHW). Exported RHW files include referenced custom RUI files and the changes associated with all RUI files at the time of the RHW file creation.

Importing an RHW file will check to see if an embedded custom RUI file is currently open. If the file is not open then the custom file is extracted and opened. Once the customizations have been extracted or verified the RUI changes saved in the RHW file will be applied to current RUI files. Change information associated with toolbars defined by plug-in files that don't exist will be ignored. Once the RUI data is restored containers will be created or modified to match the definition stored in the RHW file. Containers that only reference toolbars from plug-ins that are not installed will be ignored. Once imported the layout will appear in the window layout list and may then be restored.

### RUI Files

In Rhino 8, RUI files are intended to provide libraries of toolbars that can be referenced by containers. Changes to toolbars and macros can now be delivered with Rhino and plug-in updates. New toolbars defined in the updated RUI library will automatically appear in the Toolbar command list. Buttons added or removed from a toolbar will be added to or removed from the toolbar reference.

Toolbar groups defined in RUI files are converted into containers when loaded to support legacy and plug-in RUI files and provide a plug-in RUI file a way to create containers associated with the plug-in.

#### Macros

Macros can be managed using the **[MacroEditor](https://docs.mcneel.com/rhino/8/help/en-us/toolbarsandmenus/windowlayout.htm#Macros)** command.

<br/>

## Rhino 7

In Rhino 7, panels and toolbars could not be mixed.

### Layouts

The Rhino 7 user interface could not be switched for a different layout and only one could exist per user.

### Toolbars

Toolbars could be docked at the top or bottom of the Rhino user interface.

### Panels

Panels could be docked at the left or right of the Rhino user interface.


## Related Topics

- [Creating Macros](/guides/general/creating-command-macros/)

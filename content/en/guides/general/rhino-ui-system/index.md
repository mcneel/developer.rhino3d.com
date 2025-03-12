+++
aliases = ["/en/8/guides/general/rhino-ui-system/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide outlines Rhino's User Interface System."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "The Rhino UI System"
type = "guides"
weight = 3
override_last_modified = "2023-11-20T08:29:10Z"

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

This guide proves an overview of Rhino's User Interface (UI) system, and it compares the new system found in Rhino 8 with the previous system found in Rhino 7 and earlier.

## Rhino 8 UI System

The goals of the new Rhino 8 UI system were to:

- Display panels and toolbars in the same container.
- Reference toolbars and macros from multiple sources without having to copy definitions from one RUI file to another.
- Deliver Rhino User Interface (RUI) changes without overwriting or replacing existing files in Rhino or plug-in service releases. (In prior Rhino versions, replacing the RUI file to deliver updated toolbars and macros caused user changes to RUI files to be overwritten.)
- Quickly change the Rhino UI to display task-orientated tools.
- Share UI layouts amongst users.
- Allow users to arbitrarily modify the UI without having to be aware of the location or source of a UI component and to automatically track changes.
- Provide unified Windows and Mac UI.

The major changes in the new Rhino 8 UI system are:

- Toolbar Groups have been replaced by Containers. Containers can display both panels and toolbars.
- RUI files are used to provide toolbar and macro libraries, and they are no longer modified directly. Rhino tracks RUI changes and applies them when loading. Doing this allows Rhino to deliver updated RUI files without losing user changes to a toolbar or macro.
- Window Layouts have been added and can be used to quickly switch between different UI configurations. They can be exported as files and will include modifications to toolbars and macros and user RUI files
- Importing a Window Layout will extract user RUI files as necessary and apply RUI modifications.

The new Rhino 8 UI System is designed to allow for the referencing UI components from many sources: including panels, toolbars, and macros, defined by any RUI file or plug-in. When Rhino closes, changes to the UI are saved and original RUI files are never modified unless specifically requested. Configurations of UI layouts can be saved, restored, exported and imported as Window Layouts and shared between Windows and Mac.

### Containers

Containers hold references to panels and toolbars. Toolbars can be referenced from any valid RUI source. Items are displayed as a tab in a container. Containers may be visible or hidden.

Containers can be modified by dragging tabs from one container into another, or by clicking on the container's `Gear` menu to adding or removing references to panels or toolbars. The same panel may be referenced by multiple containers meaning it is possible to have the `Layers` tab, or example, displayed in multiple containers.

Container definitions, visibility, location, and size are saved when Rhino closes and restored when restarting Rhino. This information can also be stored and shared via Window Layouts.

Containers can be managed using Rhino's **[Containers](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/containers.htm#(null))** command.

### Window Layouts

Window Layouts are a snapshot of container definitions, visibility states, locations, and size. Restoring a Window Layout will reconfigure the current UI to make it appear as it did when the layout was created. Restored containers will display tabs in the order they were in when the Window Layout was created and will appear in the same location and size. Toolbar tabs will reference the current definition of a toolbar, if toolbar no longer exists the tab will not be displayed.

Window Layouts can be managed using Rhino's **[WindowLayout](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/windowlayout.htm#(null))** command.

#### Exporting and Importing Window Layouts

Window Layouts may be exported to a Rhino Window Layout file (RHW). Exported RHW files include referenced custom RUI files and the changes associated with all RUI files at the time of the RHW file creation.

Importing RHW file will check to see if an embedded custom RUI file is currently open. If the file is not open then the custom file is extracted and opened. Once the custom list has been extracted or verified the RUI changes saved in the RHW file will be applied to current RUI files. Change information associated with toolbars defined by plug-in files that don’t exist will be ignored. Once the RUI data is restored containers will be created or modified to match the definition stored in the RHW file. Containers that only reference toolbars from plug-ins that are not installed will be ignored. Once imported the layout will appear in the window layout list and may then be restored.

Window Layouts can be exported and imported using Rhino's **[WindowLayout](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/windowlayout.htm#(null))** command.

### RUI Files

In Rhino 8, RUI files are now simply a collection of toolbars, macros and images. These files are intended to provide libraries of toolbars that can be referenced by containers. Changes to toolbars and macros can now be delivered with Rhino and plug-in updates. New toolbars defined in the updated RUI library will automatically appear in the Toolbar command list. Buttons added or removed from a toolbar will be added or removed to the toolbar reference.

Toolbar groups defined in RUI files are converted into containers when loaded to support legacy and plug-in RUI files and provide a plug-in RUI file a way to create containers associated with the plug-in.

Linked RUI files can be managed using Rhino's **[Options > Toolbars](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#options/appearance_toolbars.htm#(null))** option.

### Toolbars

Toolbars are collections of buttons. Toolbar buttons reference macros which may come from any valid RUI source. Toolbars are displayed as tabs in a container.

#### Toolbar Groups

Toolbar Groups are now converted to containers when initially loaded. They exist as a way to support legacy RUI files. Groups may also be used by plug-in developers to provide container definitions associated with a plug-in.

#### Toolbar

Toolbars are collections of toolbar buttons and can be referenced by multiple containers. They can be modified by dragging and dropping buttons from other toolbars or using the new button wizard.

Toolbars can be managed using Rhino's **[Toolbar](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/toolbar.htm#(null))** command.

#### Toolbar Button

Toolbar buttons can contain left and/or right mouse click actions. Left and right mouse click actions are assigned to macros which contain a script to run when clicked. Toolbar buttons display the image associated with macro assigned to the left mouse action if present, if not the right click macro image is used.

#### Menus

The Rhino menu system can be extended using menu objects defined in an RUI file. The RUI file contains location information describing where to insert an item into the menu system. New menu items are defined by referencing a Macro which contains:

- Menu text.
- Menu item image.
- Help text which is displayed in the status bar when the mouse is over a menu item.
- Command script which is run when the menu item is clicked on.

Menus can be managed using Rhino's **[Menus](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#toolbarsandmenus/workspace_editor.htm#(null))** command.

#### Macro

Macros contain information needed to describe the command script that gets run when the macro is executed. Macro definitions include the following:

- Name
- Image, both light and dark mode versions
- Command script
- Button text
- Button tooltip
- Menu text
- Help text

Macros can be managed using Rhino's **[Macros](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#commands/macros.htm#(null))** command.

### Panels

Panels are modeless user interface forms created by Rhino or by plug-ins. They can appear in any container as a tab, and they may be moved between containers by dragging and dropping.

Panels can be referenced by multiple containers, but they cannot appear in the same container more than once.

## Previous Rhino UI System

The Rhino UI system, found in Rhino for Windows version 7 and earlier consists of the following:

### Toolbars

Rhino toolbars are collections of toolbar buttons. Toolbar buttons reference macros which must be defined in the same RUI file as the toolbar. Buttons contain an: image, tooltip, menu text, help text, and script. Toolbars are displayed in toolbar groups.

### Toolbar Group

Toolbar groups are collections of references to toolbars from the same RUI file. Dragging a toolbar from one file to a group in another file results in the toolbar and its referenced macros being copied from the source file to the destination file. Toolbar groups can’t reference Rhino panels.

### Toolbar

Toolbars are collections of toolbar buttons and are only ever referenced and displayed by toolbar groups.

### Toolbar Button

Toolbar buttons can contain left and/or right mouse click actions. Mouse click actions are assigned to macros which contain a script to run when clicked. Toolbar buttons display the image associated with macro assigned to the left mouse action if present, if not the right click macro image is used.

Toolbar buttons can optionally be configured to temporarily fly out other toolbars if desired.

Toolbar buttons can only reference macros from the same RUI file as the toolbar they belong to.

### Menu

The Rhino menu system can be extended using menu objects defined in an RUI file. The RUI file contains location information describing where to insert an item into the menu system. New menu items are defined by referencing a Macro which contains:

- Menu text.
- Menu item image.
- Help text which is displayed in the status bar when the mouse is over a menu item.
- Command script which is run when the menu item is clicked on.

### Macro

Macros contain information needed to display or describe the command script that gets run when the macro is executed. Macro definitions include the following:
Image which is displayed either on a referenced toolbar button or menu item.

- Button tool-tip.
- Button text.
- Menu item text
- Help text which is displayed in the status bar when the mouse is over a menu item.
- Command script to execute.

### RUI File

RUI files are collections of the items above and are stored in a writable directory. Items stored in an RUI file can only reference items defined in the same file. Changes to items in the file are saved automatically when Rhino is closed. You may open or close RUI files or manually choose to save a file at any time. The current version of a file is backed up and changes are saved to the file name. If a file gets damaged you can delete it and rename the backup file in an attempt to restore the previous version. If the backup file is damaged then nothing can be recovered.

Rhino plug-ins can install a RUI file with the same name as the plug-in and it will get copied into a writable location and opened automatically when Rhino starts. This gives a plug-in the ability to extend the Rhino interface while allowing the plug-in to not load until it is referenced.

Note, all of the above can be managed using Rhino 7's **[Toobars](https://docs.mcneel.com/rhino/7/help/en-us/index.htm#options/toolbars.htm#(null))** command.

### Rhino Panels

Rhino panels are modeless user interface definitions created by core Rhino or a plug-in.

Panels are displayed in a collection of tabs. Tab collections can only contain references to panels and a panel can only be referenced by a single collection. Displaying a panel in a collection will remove references to that panel from any other collections.

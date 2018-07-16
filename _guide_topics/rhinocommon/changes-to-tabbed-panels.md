---
title: Changes to Tabbed Panels
description: Discusses the changes in tabbed panels for Rhino 6.
authors: ['John Morse']
author_contacts: ['JohnM']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows', 'Mac']
categories: ['Advanced']
origin: unset
order: 1
keywords: ['RhinoCommon', 'Rhino', 'Panel', 'Plugin']
layout: toc-guide-page
---


## Overview

Many Rhino controls are contained in tabbed, dockable panels. 

You can create tabbed panels in plug-in using WinForms or WPF (Windows) or Eto (Windows and Mac).

You can find sample that demonstrate how to create tabbed panels in the [Developer Samples repository](https://github.com/mcneel/rhino-developer-samples) on GitHub.

## Details

The tabbed panel systems work differently in Rhino 6 than it did in Rhino 5.

##### Rhino 5 for Windows Behavior

- The registered panel class must be a ```public``` class and contain a default constructor that takes no parameters.
- A panel object is created one time when it is referenced by a visible host container and will survive for the length of a Rhino session.
- When a panel is moved to a different host container the panel objects parent is changed to the new host and the same panel object is used.

##### Rhino 6 for Windows Behavior (Per-Document Panels)

- The registered panel class must be a ```public``` class and registered as a ```PanelType.PerDoc``` panel (the default ```PanelType```).
- Rhino looks for public constructors in the following order:
  - Constructor taking a ```RhinoDoc```.
  - Constructor taking a ```uint``` representing the documents runtime serial number.
  - Constructor with no arguments.
- A panel object is created for each time a new document is created, if the panel is in a visible host container, and disposed of when the document closes.
- When a panel is moved to a different host container, the panel objects parent is changed to the new host and the same panel object is used.

##### Rhino 6 for Windows Behavior (System Panels)

- The registered panel class must be a ```public``` class and registered as a ```PanelType.System``` panel.
- Rhino looks for public constructors in the following order:
  - Constructor taking a ```RhinoDoc```.
  - Constructor taking a ```uint``` representing the documents runtime serial number.
  - Constructor with no arguments.
- A panel object is created one time when it is referenced by a visible host container, and it will survive for the length of a Rhino session.
- When a panel is moved to a different host container, the panel objects parent is changed to the new host and the same panel object is used.

##More Information

Rhino for Mac works the same as Rhino for Windows, with the exception that there may be more than one panel instance per document.

Rhino 6 includes a ```IPanel``` interface which can be implemented to determine when a panel is shown, hidden or closed.

Static methods on ```RhinoDoc``` should be hooked by your panel class when created and unhooked when dispose of in both Rhino 5 and Rhino 6.



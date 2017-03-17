---
title: Plugin Build Configurations
description: This guide discusses Rhino C/C++ plugin build configurations and how to use them.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/buildconfigurations
order: 6
keywords: ['rhino']
layout: toc-guide-page
---

 
## Overview

Visual Studio's Build Configurations provide a way to store multiple versions of solution and project properties.  The active configuration can be quickly accessed and changed, allowing you to easily build multiple configurations of the same project.

By default, standalone C/C++ projects created with Visual Studio include *Debug* and *Release* configurations.  *Debug* configurations are automatically configured for debugging an application, and Release configurations are configured for the final release of an application.

- The *Debug* configuration of your program is compiled with full symbolic debug information and no optimization. Optimization complicates debugging, because the relationship between source code and generated instructions is more complex. The *Debug* configuration also links with debug runtime libraries.
- The *Release* configuration of your program contains no symbolic debug information and is fully optimized. *Debug* information can be generated in PDB Files (C/C++) depending on the compiler options used.  Creating PDB files can be very useful if you later need to debug your release version.  The *Release* configuration also links with release runtime libraries.

**NOTE**: You can switch between *Release* and *Debug* build configurations by using Visual Studio's *Standard toolbar* or the *Configuration Manager* dialog.

## Build Configurations

The Rhino C/C++ SDK provides all of the tools (C/C++ header and library files) necessary to build plugins that can be used by Rhino.  In addition to this, the Rhino SDK includes a debug build of Rhino (*Rhino_d.exe*).  The debug version of Rhino is installed in the same location as the production, or release, version of Rhino (*Rhino.exe*).

In order to take advantage of the inclusion of debug Rhino, the build configurations created by the *Rhino Plugin AppWizard* are somewhat different than what is described above.  Projects created with the *Rhino Plugin AppWizard* include *Debug*, *PseudoDebug*, and *Release* configurations.  *Debug* and *PseudoDebug* configurations are automatically configured for debugging an application, and *Release* configurations are configured for the final release of an application.

- The *Debug* configuration of your program is compiled with full symbolic debug information and no optimization.  Optimization complicates debugging, because the relationship between source code and generated instructions is more complex.  The *Debug* configuration also links with debug runtime libraries. Plugins built with the *Debug* configuration will only load in debug Rhino (*Rhino_d.exe*).
- The *PseudoDebug* project is a *Release* project that disables optimizations and generates debugging information using the compiler’s *Program Database (/Zi)* option and the linker’s *Generate Debug Information (/DEBUG)* option.  These option settings allow you to use the debugger while you are developing your custom plugin.  The *PseudoDebug* configuration also links with release runtime libraries.  Plugins built with the *PseudoDebug* configuration will only load in release Rhino (*Rhino.exe*).
- The *Release* configuration of your program contains no symbolic debug information and is fully optimized.  *Debug* information can be generated in PDB Files (C/C++) depending on the compiler options used.  Creating PDB files can be very useful if you later need to debug your release version.  The *Release* configuration also links with release runtime libraries.  Plugins built with the *Release* configuration will only load in release Rhino (*Rhino.exe*).

These plugin build configurations link with the following SDK libraries and target the following executables:

| Configuration     | | | | Rhino Lib     | | | | 	opennurbs Lib     | | | | Target Executable     |
| :------------- | | | | :------------- | | | | :------------- | | | | :------------- |
| *Debug*       | | | | *Rhino_d.lib*      | | | | *opennurbs_d.lib*       | | | | *Rhino_d.exe*       |
| *PseudoDebug*	       | | | | *Rhino.lib*       | | | | *opennurbs.lib*       | | | | *Rhino.exe*       |
| *Release*       | | | | *Rhino.lib*       | | | | *opennurbs.lib*      | | | | *Rhino.exe*       |

Again, you can switch between *Release*, *PseudoDebug*, and *Debug* build configurations by using Visual Studio's *Standard toolbar* or the *Configuration Manager* dialog.

## Debugging Plugins

<div class="bs-callout bs-callout-danger">
  <h4>CRITICAL</h4>
  <p>In order to run the debug version of Rhino (<i>Rhino_d.exe</i>), you will need a non-evaluation version of Rhino installed on your system.  Also, the non-evaluation version of Rhino that you are using must match your Rhino C/C++ SDK version.  For example, if you are using Rhino 5.0 SR7, you must also have the Rhino 5.0 SR7 SDK order to run debug Rhino.  By the same token, in order to run the debug version of Rhino (<i>Rhino_d.exe</i>), your system must have the correct Debug libraries. To ensure this, make sure your development system is "up-to-date" with all of the available Visual Studio service packs and security updates.  Using Windows Updates will ensure this.  Or, just select <i>Help</i> > <i>Check for Updates</i> inside of Visual Studio.</p>
</div>

You can debug your plugin in the following build configurations:

- *Debug* configuration.  The advantage of debugging your plugin using the *Debug* configuration is that you can debug into MFC, as this configuration links with debug MFC libraries.  The disadvantage of debugging your plugin using the Debug configuration is that no other plugins will be loaded during the debugging session.  This is because debug Rhino (*Rhino_d.exe*) can only load debug plugins.
- *PseudoDebug* configuration.  The advantage of debugging your plugin using the *PseudoDebug* configuration is that all other plugins will be loaded during the debugging session.  This is because release Rhino (*Rhino.exe*) will load all release plugins.  The disadvantage of debugging your plugin using the *PseudoDebug* configuration is that you cannot debug into MFC, as this configuration links with release MFC libraries.

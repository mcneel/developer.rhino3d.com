+++
aliases = ["/5/guides/", "/6/guides/", "/7/guides/", "/wip/guides/"]
description = "All the guides available for developing for Rhino or Grasshopper."
title = "Guides"
type = "guides"
weight = 2

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = []
since = 0

[page_options]
byline = false
toc = true
toc_type = "single"

+++

## [General](/guides/general)

*Guides that apply across platforms and SDKs*

### Overview

- [Developing Software In Public](/guides/general/developing-software-in-public)
- [Rhino Technology Overview](/guides/general/rhino-technology-overview)
- [Frequently Asked Questions (FAQ)](/guides/general/frequently-asked-questions)

### Getting Started

- [Developer Prerequisites](/guides/general/rhino-developer-prerequisites)
- [Contributing](/guides/general/contributing)

### Fundamentals

- [What is a Rhino Plugin?](/guides/general/what-is-a-rhino-plugin)
- [Rhino Installer Engine](/guides/general/rhino-installer-engine)
- [Simple Command Macros](/guides/general/creating-command-macros/)
- [Rhino Package Manager](/guides/yak/)

### [Essential Mathematics](/guides/general/essential-mathematics)

- [Introduction](/guides/general/essential-mathematics)  
- [Vector Mathematics](/guides/general/essential-mathematics/vector-mathematics)  
- [Matrices and Transformations](/guides/general/essential-mathematics/matrices-transformations)  
- [Parametric Curves and Surfaces](/guides/general/essential-mathematics/parametric-curves-surfaces)  
- [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/6/essentialmathematics/) [Download Essential Mathematics for Computational Design as a single PDF ](https://www.rhino3d.com/download/rhino/6/essentialmathematics/)

### This Site

- [How This Site Works](/guides/general/how-this-site-works)
- [Getting Started with Developer Docs](https://github.com/mcneel/developer-rhino3d-com/blob/main/README.md)
- [Developer Docs Style Guide](/guides/general/developer-docs-style-guide)


## [Scripting](/guides/scripting)      <!-- RH-76268 -->

*Guides on using scripting features in Rhino 8 and above, that apply to all programming languages*

### Overview
- [What is Script Editor?](/guides/scripting/what-is-scripteditor)

### Getting Started

- [ScriptEditor Command](/guides/scripting/scripting-command)
- [Grasshopper Script Component](/guides/scripting/scripting-component)
- <!-- [Python Scripting](/guides/scripting/scripting-python) --> Python Scripting {{% comingsoon-label %}}
- <!-- [C# Scripting](/guides/scripting/scripting-csharp) --> C# Scripting {{% comingsoon-label %}}

### Editor Features

- <!-- [Editing Features](/guides/scripting/editor-editing) --> Editing Features {{% comingsoon-label %}}
- <!-- [Explorer](/guides/scripting/editor-explorer) --> Explorer {{% comingsoon-label %}}
- <!-- [Search & Replace](/guides/scripting/editor-search) --> Search & Replace {{% comingsoon-label %}}
- <!-- [Terminal](/guides/scripting/editor-terminal) --> Terminal {{% comingsoon-label %}}
- <!-- [Problems Tray](/guides/scripting/editor-problems) --> Problems Tray {{% comingsoon-label %}}
- <!-- [Debugging Your Scripts](/guides/scripting/editor-debug-scripts) --> Debugging Your Scripts {{% comingsoon-label %}}
- <!-- [Templates](/guides/scripting/editor-templates) --> Templates {{% comingsoon-label %}}
- <!-- [Help & Examples](/guides/scripting/editor-help) --> Help & Examples {{% comingsoon-label %}}
- <!-- [Configurations](/guides/scripting/editor-configs) --> Configurations {{% comingsoon-label %}}
- <!-- [Logs](/guides/scripting/editor-logs) --> Logs {{% comingsoon-label %}}

### Publishing

- [Creating Rhino Projects](/guides/scripting/projects-create)
- [Creating Rhino and Grasshopper Plugins](/guides/scripting/projects-publish)

### Advanced

- <!-- [Language Initialization](/guides/scripting/advanced-langinit) --> Language Initialization {{% comingsoon-label %}}
- <!-- [CPython Runtime and Language Server](/guides/scripting/advanced-pyruntime) --> CPython Runtime and Language Server {{% comingsoon-label %}}
- <!-- [Language Libraries](/guides/scripting/advanced-libraries) --> Language Libraries {{% comingsoon-label %}}
- <!-- [Async Execution](/guides/scripting/advanced-async) --> Async Execution {{% comingsoon-label %}}
- <!-- [VisualStudioCode Extension](/guides/scripting/advanced-vscode) --> VisualStudioCode Extension {{% comingsoon-label %}}
- <!-- [RhinoCode Command Line Interface](/guides/scripting/advanced-cli) --> RhinoCode Command Line Interface {{% comingsoon-label %}}
- <!-- [RhinoCode API](/guides/scripting/advanced-core-api) --> RhinoCode API {{% comingsoon-label %}}
- <!-- [RhinoCodeEditor API](/guides/scripting/advanced-editor-api) --> RhinoCodeEditor API {{% comingsoon-label %}}

## [RhinoCommon](/guides/rhinocommon)

*The cross-platform .NET plugin SDK for Rhino.*

### Overview

- [What is RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon/)
- [What's New?](/guides/rhinocommon/whats-new/)

### Getting Started

- Installing Tools ([Windows](/guides/rhinocommon/installing-tools-windows/), [Mac](/guides/rhinocommon/installing-tools-mac/))
- Your First Plugin ([Windows](/guides/rhinocommon/your-first-plugin-windows/), [Mac](/guides/rhinocommon/your-first-plugin-mac/), [Cross-Platform](/guides/rhinocommon/your-first-plugin-crossplatform/))
- Plugin Installers ([Windows](/guides/rhinocommon/plugin-installers-windows/), [Mac](/guides/rhinocommon/plugin-installers-mac/))
- [Distributing a Rhino Plug-In with the Package Manager](/guides/yak/creating-a-rhino-plugin-package/)

### Fundamentals

{{< dev-topic-list "guides" "RhinoCommon" "Fundamentals" "weight" >}}

### Rendering

{{< dev-topic-list "guides" "RhinoCommon" "Rendering" "weight" >}}

### Advanced

{{< dev-topic-list "guides" "RhinoCommon" "Advanced" "weight" >}}

### Zoo

{{< dev-topic-list "guides" "RhinoCommon" "Zoo" "weight" >}}

### Cloud Zoo

{{< dev-topic-list "guides" "RhinoCommon" "CloudZoo" "weight" >}}

## [Rhino.Python](/guides/rhinopython)


*Quickly add functionality to Rhino or automate repetitive tasks.*

### Overview

{{< dev-topic-list "guides" "RhinoPython" "Overview" "weight" >}}

### Getting Started

- Your First Python Script in Rhino ([Windows](/guides/rhinopython/your-first-python-script-in-rhino-windows), [Mac](/guides/rhinopython/your-first-python-script-in-rhino-mac), [Grasshopper](/guides/rhinopython/your-first-python-script-in-grasshopper))
- [Where to get help...](/guides/rhinopython/python-where-to-find-help)
- [Troubleshooting Installation](/guides/rhinopython/python-troubleshooting-install)

### Python Editor for Windows

{{< dev-topic-list "guides" "RhinoPython" "Python Windows" "weight" >}}

### Python in Grasshopper

{{< dev-topic-list "guides" "RhinoPython" "GhPython" "weight" >}}


### Fundamentals

{{< dev-topic-list "guides" "RhinoPython" "Fundamentals" "weight" >}}

### Python in Rhino

{{< dev-topic-list "guides" "RhinoPython" "Python in Rhino" "weight" >}}

### [Rhino.Python 101](/guides/rhinopython/primer-101)

&nbsp;&nbsp; [Introduction](/guides/rhinopython/primer-101)  
&nbsp;&nbsp; [Where to find help](/guides/rhinopython/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [What's it all about?](/guides/rhinopython/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [Python Essentials](/guides/rhinopython/primer-101/2-python-essentials/)  
&nbsp;&nbsp; 3. [Script anatomy](/guides/rhinopython/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operators and functions](/guides/rhinopython/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Conditional execution](/guides/rhinopython/primer-101/5-conditional-execution/)  
&nbsp;&nbsp; 6. [Tuples, Lists and Dictionaries](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/)  
&nbsp;&nbsp; 7. [Classes](/guides/rhinopython/primer-101/7-classes/)  
&nbsp;&nbsp; 8. [Geometry](/guides/rhinopython/primer-101/8-geometry/)  

&nbsp;&nbsp; [{{< awesome "fas fa-download">}} ](https://download.rhino3d.com/IronPython/5.0/RhinoPython101/) [Download the Rhino.Python 101 Primer as a single PDF ](https://download.rhino3d.com/IronPython/5.0/RhinoPython101/)  


### Intermediate

{{< dev-topic-list "guides" "RhinoPython" "Intermediate" "weight" >}}

### Custom Dialogs in Eto

{{< dev-topic-list "guides" "RhinoPython" "Eto" "weight" >}}


### Other Resources

- [Rhino Scripting Forum (Discourse)](https://discourse.mcneel.com/c/scripting)  
- [Rhino.Python Samples](/samples/#rhinopython)  
- [Rhino.Python Developer Samples GitHub](https://github.com/mcneel/rhino-developer-samples/tree/master/rhinopython)  
- [Designalyze Python Tutorials](https://designalyze.com/)
- [Plethora Project](https://www.plethora-project.com/education/2017/5/31/rhino-python-programming)
- [Steve Baer's Blog](https://stevebaer.wordpress.com/category/python/)
- [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide/Programmers)
- [Tutorials Point Python Series](https://www.tutorialspoint.com/python/index.htm)
- [Rhino.Python Dash Docset](https://discourse.mcneel.com/t/rhino-python-dash-docset/6399)
- [Nature of Code Video Tutorials](https://www.youtube.com/watch?v=Kyi_K85Gsm4&list=PL5Up_u-XkWgP7nB7XIevMTyBCZ7pvLBGP)

## [openNURBS](/guides/opennurbs)

*Read/Write Rhino 3dm files in your application.*

### Overview

{{< dev-topic-list "guides" "openNURBS" "Overview" "weight" >}}

### Getting Started

{{< dev-topic-list "guides" "openNURBS" "Getting Started" "weight" >}}

### Fundamentals

{{< dev-topic-list "guides" "openNURBS" "Fundamentals" "weight" >}}

### Advanced

{{< dev-topic-list "guides" "openNURBS" "Advanced" "weight" >}}

## [C/C++](/guides/cpp)

*Native SDK for Rhino for Windows plugins.*

### Overview

{{< dev-topic-list "guides" "C/C++" "Overview" "weight" >}}

### Getting Started

{{< dev-topic-list "guides" "C/C++" "Getting Started" "weight" >}}

### Fundamentals

{{< dev-topic-list "guides" "C/C++" "Fundamentals" "weight" >}}

### Advanced

{{< dev-topic-list "guides" "C/C++" "Advanced" "weight" >}}

### Rendering (RDK)

{{< dev-topic-list "guides" "C/C++" "RDK" "weight" >}}

### Zoo

{{< dev-topic-list "guides" "C/C++" "Zoo" "weight" >}}

### Troubleshooting

{{< dev-topic-list "guides" "C/C++" "Troubleshooting" "weight" >}}

## [Grasshopper](/guides/grasshopper)


*Create custom Grasshopper components and plugins.*

### Overview

- [What is a Grasshopper Component?](/guides/grasshopper/what-is-a-grasshopper-component/)

### Getting Started

- Installing Tools ([Windows](/guides/grasshopper/installing-tools-windows/), [Mac](/guides/grasshopper/installing-tools-mac/))
- Your First Component ([Windows](/guides/grasshopper/your-first-component-windows/), [Mac](/guides/grasshopper/your-first-component-mac/))
- [Distributing a Grasshopper Plug-In with the Package Manager](/guides/yak/creating-a-rhino-plugin-package/)

### Fundamentals

{{< dev-topic-list "guides" "Grasshopper" "Fundamentals" "weight" >}}

### Advanced

{{< dev-topic-list "guides" "Grasshopper" "Advanced" "weight" >}}

### In Depth

{{< dev-topic-list "guides" "Grasshopper" "In Depth" "weight" >}}

### Python in Grasshopper

{{< dev-topic-list "guides" "RhinoPython" "GhPython" "weight" >}}


## [RhinoScript](/guides/rhinoscript)


*RhinoScript is a scripting tool based on Microsoft's VBScript language. With RhinoScript, you can quickly add functionality to Rhino for Windows, or automate repetitive tasks.*

### Overview

- [What are VBScript and RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript)

### [RhinoScript 101](/guides/rhinoscript/primer-101)

&nbsp;&nbsp; [Introduction](/guides/rhinoscript/primer-101)  
&nbsp;&nbsp; [Where to find help](/guides/rhinoscript/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [What's it all about?](/guides/rhinoscript/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [RhinoScript Essentials](/guides/rhinoscript/primer-101/2-vbscript-essentials/)  
&nbsp;&nbsp; 3. [Script anatomy](/guides/rhinoscript/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operators and functions](/guides/rhinoscript/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Conditional execution](/guides/rhinoscript/primer-101/5-conditional-execution/)  
&nbsp;&nbsp; 6. [Arrays](/guides/rhinoscript/primer-101/6-arrays/)  
&nbsp;&nbsp; 7. [Geometry](/guides/rhinoscript/primer-101/7-geometry/)  
&nbsp;&nbsp; [{{< awesome "fas fa-download">}} ](https://www.rhino3d.com/download/rhino/5.0/rhinoscript101) [Download the RhinoScript 101 Primer as a single PDF ](https://www.rhino3d.com/download/rhino/5.0/rhinoscript101)

### Fundamentals

{{< dev-topic-list "guides" "RhinoScript" "Fundamentals" "weight" >}}


### Intermediate

{{< dev-topic-list "guides" "RhinoScript" "Intermediate" "weight" >}}

### Advanced

{{< dev-topic-list "guides" "RhinoScript" "Advanced" "weight" >}}

### Troubleshooting

{{< dev-topic-list "guides" "RhinoScript" "Troubleshooting" "weight" >}}

### Other Resources

- [Pascal Golay's scripted utilities for Rhino](https://wiki.mcneel.com/people/pascalgolay)
- [RhinoScript Samples on GitHub](https://github.com/mcneel/rhinoscript)
- [RhinoScript Dash Docset](https://discourse.mcneel.com/t/rhinoscript-dash-docset/6382)
- [RhinoScript Help File On-Line](https://www.rhino3d.com/5/rhinoscript/index.html)

<!-- ## [Compute](/guides/compute) -->
<h2 id="compute"><a href="/guides/compute">Compute</a></h2>


### Getting Started

{{< dev-topic-list "guides" "Compute" "Getting Started" "weight" >}}

### Production Deployment

{{< dev-topic-list "guides" "Compute" "Deployment" "weight" >}}

### Hops

{{< dev-topic-list "guides" "Compute" "Hops" "weight" >}}

## Developer Services

### [Localization](https://www.rhino3d.com/localization)

Our regional office in Europe provides a translation and localization service for third-party developers and anyone else interested in translating their products to French, German, Italian, Spanish, etc. [Details…](https://www.rhino3d.com/localization)

### Marketing Support

If you have developed a Rhino add-on that you would like to make available to other Rhino users, [food4Rhino](https://www.food4rhino.com/) is the place to post the details about your plug-ins for Rhino and Grasshopper. Food4Rhino is the Plug-in Community Service by McNeel.  Users can find the newest Rhino Plug-ins, Grasshopper Add-ons, Materials, Textures and Backgrounds, Scripts and much more. It is free. [See the frequently asked questions...](https://www.food4rhino.com/faq)

+++
aliases = ["/en/5/guides/", "/en/6/guides/", "/en/7/guides/", "/en/wip/guides/"]
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

- [New for Developers in V9](/guides/general/new-in-v9/)
- [Developing Software In Public](/guides/general/developing-software-in-public)
- [Rhino Technology Overview](/guides/general/rhino-technology-overview)
    - [OpenGL in Rhino 9](/guides/general/rhino-technology-overview/opengl/) {{< new-label version="9" style="inline" link="/guides/general/new-in-v9/" >}}
- [Frequently Asked Questions (FAQ)](/guides/general/frequently-asked-questions)

### Getting Started

- [Developer Prerequisites](/guides/general/rhino-developer-prerequisites)
- [Contributing](/guides/general/contributing)

### Fundamentals

- [What is a Rhino Plugin?](/guides/general/what-is-a-rhino-plugin)
- [Rhino Installer Engine](/guides/general/rhino-installer-engine)
- [Rhino Package Manager](/guides/yak/)
- [Rhino UI System](/guides/general/rhino-ui-system/)
- [In-Viewport User Interface](/guides/general/rhino-ui-system/in-viewport-ui/) {{< new-label version="9" style="inline" link="/guides/general/new-in-v9/" >}}
- [Simple Command Macros](/guides/general/creating-command-macros/)

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

## [Scripting](/guides/scripting)

*Guides on using scripting features in Rhino 8 and above, that apply to all programming languages*

### Getting Started

#### ScriptEditor Command
  - [Opening Script Editor](/guides/scripting/scripting-command/#opening-script-editor)
  - [First Script](/guides/scripting/scripting-command/#first-script)
  - [Edit Script](/guides/scripting/scripting-command/#edit-script)
  - [Running Scripts](/guides/scripting/scripting-command/#running-scripts)
  - [Debugging Scripts](/guides/scripting/scripting-command/#debugging-scripts)
  - [Using Packages](/guides/scripting/scripting-command/#using-packages)
  - [Editor Features](/guides/scripting/scripting-command/#editor-features)

#### Script Component
  - [Create Script Component](/guides/scripting/scripting-component/#script-component)
  - [First Script](/guides/scripting/scripting-component/#first-script)
  - [Script Inputs and Outputs](/guides/scripting/scripting-component/#script-inputs-and-outputs)
  - [Edit Script](/guides/scripting/scripting-component/#edit-script)
  - [Run Scripts](/guides/scripting/scripting-component/#debugging-scripts)
  - [Debugging Scripts](/guides/scripting/scripting-component/#debugging-scripts)
  - [Using Packages](/guides/scripting/scripting-component/#using-packages)
  - [Editor Features](/guides/scripting/scripting-component/#editor-features)

### Python Scripting

- [Scripting: Python](/guides/scripting/scripting-python)
- [Grasshopper Scripting: Python](/guides/scripting/scripting-gh-python)
- [Grasshopper 2 Scripting: Python](/guides/scripting/scripting-gh2-python) {{< new-label version="9" style="inline" link="/guides/general/new-in-v9/" >}}

### C# Scripting

- [Scripting: C#](/guides/scripting/scripting-csharp)
- [Grasshopper Scripting: C#](/guides/scripting/scripting-gh-csharp)
- [Grasshopper 2 Scripting: C#](/guides/scripting/scripting-gh2-csharp) {{< new-label version="9" style="inline" link="/guides/general/new-in-v9/" >}}

### Editor Features

- [Editing Features](/guides/scripting/editor-editing)
- [Explorer](/guides/scripting/editor-explorer)
- [Search & Replace](/guides/scripting/editor-search)
- [Terminal](/guides/scripting/editor-terminal)
- [Problems](/guides/scripting/editor-problems)
- [Debugging Your Scripts](/guides/scripting/editor-debug)
- [Templates](/guides/scripting/editor-templates)
- [Examples](/guides/scripting/editor-examples)
- [Tests](/guides/scripting/editor-tests) {{< new-label version="9" style="inline" link="/guides/general/new-in-v9/" >}}
- [Help](/guides/scripting/editor-help)
- [Options](/guides/scripting/editor-configs)
- [Logs](/guides/scripting/editor-logs)

### Publishing Script Plugins

- [Creating Rhino/Grasshopper Script Plugins](/guides/scripting/projects-create)
- [Building & Publishing Script Plugins](/guides/scripting/projects-publish)

### Advanced

- [ScriptEditor Macros](/guides/scripting/advanced-scripteditor-macros)
- [Language Initialization](/guides/scripting/advanced-langinit)
- [Script Package References](/guides/scripting/advanced-packages) {{< new-label version="9" style="inline" link="/guides/general/new-in-v9/" >}}
- [Python Path Files](/guides/scripting/advanced-pthfiles)
- [Python Package Environments](/guides/scripting/advanced-pyvenvs)
- [Asynchronous Execution](/guides/scripting/advanced-async)
- [RhinoCode Command Line Interface](/guides/scripting/advanced-cli)
<!-- [RhinoCode API](/guides/scripting/advanced-core-api) -->
<!-- [RhinoCodeEditor API](/guides/scripting/advanced-editor-api) -->

## [RhinoCommon](/guides/rhinocommon)

*The cross-platform .NET plugin SDK for Rhino.*

### Overview

- [What is RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon/)
- [What's New?](/guides/rhinocommon/whats-new/)
- [Moving to .NET Core](/guides/rhinocommon/moving-to-dotnet-core)

### Getting Started

- Installing Tools ([Windows](/guides/rhinocommon/installing-tools-windows/), [Mac](/guides/rhinocommon/installing-tools-mac/))
- Your First Plugin ([Windows](/guides/rhinocommon/your-first-plugin-windows/), [Mac](/guides/rhinocommon/your-first-plugin-mac/))
- Plugin Installers ([Windows](/guides/rhinocommon/plugin-installers-windows/), [Mac](/guides/rhinocommon/plugin-installers-mac/))
- [Distributing a Rhino Plug-In with the Package Manager](/guides/yak/creating-a-rhino-plugin-package/)

### Fundamentals

{{< dev-topic-list "guides" "RhinoCommon" "Fundamentals" "weight" >}}

### RhinoCommon Geometry

- [Overview](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#31-overview)  
- [Geometry Structures](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#32-geometry-structures)  
    - [The Point3d Structure](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#321-the-point3d-structure)  
    - [Points and Vectors](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#322-points--vectors)  
    - [Lightweight Curves](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#323-lightweight-curves)  
    - [Lightweight Surfaces](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#324-lightweight-surfaces)  
    - [Other Geometry Structures](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#325-other-geometry-structures)  
- [Geometry classes](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#33-geometry-classes)  
    - [Curves](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#331-curves)  
    - [Surfaces](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#332-surfaces)  
    - [Meshes](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#333-meshes)  
    - [Boundary Representation (Brep)](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#334-boundary-representation-brep)  
    - [Other Geometry Classes](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#335-other-geometry-classes)  
- [Geometry transformations](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/#34-geometry-transformations)  

### Rendering

{{< dev-topic-list "guides" "RhinoCommon" "Rendering" "weight" >}}

### Advanced

{{< dev-topic-list "guides" "RhinoCommon" "Advanced" "weight" >}}

### LAN Zoo

{{< dev-topic-list "guides" "RhinoCommon" "Zoo" "weight" >}}

### Cloud Zoo

{{< dev-topic-list "guides" "RhinoCommon" "CloudZoo" "weight" >}}

### Other Resources

- [Developer samples on GitHub](https://github.com/mcneel/rhino-developer-samples)
- [Developer discussions on Discourse](https://discourse.mcneel.com/c/rhino-developer)

## [Rhino.Python](/guides/rhinopython)


*Quickly add functionality to Rhino or automate repetitive tasks.*

### Overview

{{< dev-topic-list "guides" "RhinoPython" "Overview" "weight" "8" >}}

### Getting Started

- Your First Python Script in Rhino ([Windows](/guides/rhinopython/your-first-python-script-in-rhino-windows), [Grasshopper](/guides/rhinopython/your-first-python-script-in-grasshopper))
- [Where to get help...](/guides/rhinopython/python-where-to-find-help)
- [Troubleshooting Installation](/guides/rhinopython/python-troubleshooting-install)

### Python Editor for Windows

{{< dev-topic-list "guides" "RhinoPython" "Python Windows" "weight" "8" >}}

### Python in Grasshopper

{{< dev-topic-list "guides" "RhinoPython" "GhPython" "weight" "8" >}}

### Fundamentals

{{< dev-topic-list "guides" "RhinoPython" "Fundamentals" "weight" "8" >}}

### Python in Rhino

{{< dev-topic-list "guides" "RhinoPython" "Python in Rhino" "weight" "8" >}}

### [Rhino.Python 101](/guides/rhinopython/primer-101)

&nbsp;&nbsp; [Introduction](/guides/rhinopython/primer-101)  
&nbsp;&nbsp; [Where to find help](/guides/rhinopython/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [What's it all about?](/guides/rhinopython/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [Python Essentials](/guides/rhinopython/primer-101/2-python-essentials/)  
&nbsp;&nbsp; 3. [Script Anatomy](/guides/rhinopython/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operators and Functions](/guides/rhinopython/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Conditional Execution](/guides/rhinopython/primer-101/5-conditional-execution/)  
&nbsp;&nbsp; 6. [Tuples, Lists, and Dictionaries](/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/)  
&nbsp;&nbsp; 7. [Classes](/guides/rhinopython/primer-101/7-classes/)  
&nbsp;&nbsp; 8. [Geometry](/guides/rhinopython/primer-101/8-geometry/)  

&nbsp;&nbsp; [{{< awesome "fas fa-download">}} ](https://download.rhino3d.com/IronPython/5.0/RhinoPython101/) [Download the Rhino.Python 101 Primer as a single PDF ](https://download.rhino3d.com/IronPython/5.0/RhinoPython101/)  


### Intermediate

{{< dev-topic-list "guides" "RhinoPython" "Intermediate" "weight" "8" >}}

### Custom Dialogs in Eto

{{< dev-topic-list "guides" "RhinoPython" "Eto" "weight" "8" >}}


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

### Other Resources

- [Developer discussions on Discourse](https://discourse.mcneel.com/c/opennurbs)

## [C/C++](/guides/cpp)

*Native SDK for Rhino plugins on Windows and Mac.*

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

### LAN Zoo

{{< dev-topic-list "guides" "C/C++" "Zoo" "weight" >}}

### Troubleshooting

{{< dev-topic-list "guides" "C/C++" "Troubleshooting" "weight" >}}

### Other Resources

- [Developer samples on GitHub](https://github.com/mcneel/rhino-developer-samples)
- [Developer discussions on Discourse](https://discourse.mcneel.com/c/rhino-developer)

## [Grasshopper](/guides/grasshopper)


*Create custom Grasshopper components and plugins.*

### [Essential Algorithms and Data Structures for Grasshopper](/guides/grasshopper/gh-algorithms-and-data-structures/)

- [Introduction](/guides/grasshopper/gh-algorithms-and-data-structures/)
- [Algorithms and Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/)
  - [1.1 Algorithmic design](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#11-algorithmic-design)
  - [1.2 Algorithms parts](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#12-algorithms-parts)
  - [1.3 Designing algorithms: the 4-step process](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#13-designing-algorithms-the-4-step-process)
  - [1.4 Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#14-data)
  - [1.5 Data sources](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#15-data-sources)
  - [1.6 Data types](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#16-data-types)
  - [1.7 Processing Data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#17-processing-data)
  - [1.8 Pitfalls of algorithmic design](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#18-pitfalls-of-algorithmic-design)
  - [1.9 Tutorials: algorithms and data](/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#19-tutorials-algorithms-and-data)
- [Introduction to Data Structures](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/)
  - [2.1 Overview](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#21-overview)
  - [2.2 Generating lists](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#22-generating-lists)
  - [2.3 List operations](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#23-list-operations)
  - [2.4 List matching](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#24-list-matching)
  - [2.5 Tutorials: data structures](/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#25-tutorials-data-structures)
- [Advanced Data Structures](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/)
  - [3.1 The Grasshopper data structure](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#31-the-grasshopper-data-structure)
  - [3.2 Generating trees](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#32-generating-trees)
  - [3.3 Tree matching](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#33-tree-matching)
  - [3.4 Traversing trees](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#34-traversing-trees)
  - [3.5 Basic tree operations](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#35-basic-tree-operations)
  - [3.6 Advanced tree operations](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#36-advanced-tree-operations)
  - [3.7 Tutorials: advanced data ](/guides/grasshopper/gh-algorithms-and-data-structures/advanced-data-structures/#37-tutorials-advanced-data-structures)
- [{{< awesome "fas fa-download">}}](https://www.rhino3d.com/download/rhino/6.0/essential-algorithms/) [Download full PDF and GH examples](https://www.rhino3d.com/download/rhino/6.0/essential-algorithms/)

### Python Scripting in Grasshopper

- [Create Script Component](/guides/scripting/scripting-component/#script-component)
- [First Script](/guides/scripting/scripting-component/#first-script)
- [Script Inputs and Outputs](/guides/scripting/scripting-component/#script-inputs-and-outputs)
- [Edit Script](/guides/scripting/scripting-component/#edit-script)
- [Run Scripts](/guides/scripting/scripting-component/#debugging-scripts)
- [Debugging Scripts](/guides/scripting/scripting-component/#debugging-scripts)
- [Using Packages](/guides/scripting/scripting-component/#using-packages)
- [Editor Features](/guides/scripting/scripting-component/#editor-features)
- [Grasshopper Scripting: Python](/guides/scripting/scripting-gh-python)
- [Creating Global Sticky Variables](/guides/rhinopython/ghpython-global-sticky/)
- [Node in Code from Python](/guides/rhinopython/ghpython-call-components/)
- [Custom GhPython Baking Component](/guides/rhinopython/ghpython-bake/)
- [Grasshopper data trees and Python](/guides/rhinopython/grasshopper-datatrees-and-python/)
- [GhPython Common Questions and Answers](/guides/rhinopython/ghpython-question-answer/)

### [C# Scripting in Grasshopper](/guides/grasshopper/csharp-essentials/)

- [C# Component in Grasshopper](/guides/grasshopper/csharp-essentials/1-grasshopper-csharp-component/#21-introduction)
- [C# Programming Basics](/guides/grasshopper/csharp-essentials/2-csharp-basics/)
- [RhinoCommon Geometry](/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/)
- [Design Algorithms](/guides/grasshopper/csharp-essentials/4-design-algorithms/)

### Grasshopper Plugins

- [What is a Grasshopper Component?](/guides/grasshopper/what-is-a-grasshopper-component/)
- Installing Tools ([Windows](/guides/grasshopper/installing-tools-windows/), [Mac](/guides/grasshopper/installing-tools-mac/))
- Your First Component ([Windows](/guides/grasshopper/your-first-component-windows/), [Mac](/guides/grasshopper/your-first-component-mac/))
- [Developer samples on GitHub](https://github.com/mcneel/rhino-developer-samples)
- [Developer discussions on Discourse](https://discourse.mcneel.com/c/grasshopper-developer)
- [Distributing a Grasshopper Plug-In with the Package Manager](/guides/yak/creating-a-grasshopper-plugin-package/)

#### Plugin Fundamentals
{{< dev-topic-list "guides" "Grasshopper" "Fundamentals" "weight" >}}

#### In Depth
{{< dev-topic-list "guides" "Grasshopper" "In Depth" "weight" >}}

#### Advanced
{{< dev-topic-list "guides" "Grasshopper" "Advanced" "weight" >}}


## [Grasshopper 2](/guides/grasshopper2)

*Create custom Grasshopper 2 components and plugins.*

### Grasshopper 2 Plugins

- Installing Tools ([Windows](/guides/grasshopper/installing-tools-windows/), [Mac](/guides/grasshopper/installing-tools-mac/))
- [Getting Started](/guides/grasshopper2/getting-started/) {{< new-label version="9" style="inline" link="/guides/general/new-in-v9/" >}}
- Your First Component ([Windows](/guides/grasshopper2/your-first-component-windows/), [Mac](/guides/grasshopper2/your-first-component-mac/))
- [Migrating Components to Grasshopper 2](/guides/grasshopper2/migrating-components-to-gh2/) {{< new-label version="9" style="inline" link="/guides/general/new-in-v9/" >}}
- [Developer discussions on Discourse](https://discourse.mcneel.com/c/grasshopper-developer)


## [RhinoScript](/guides/rhinoscript)


*RhinoScript is a scripting tool based on Microsoft's VBScript language. With RhinoScript, you can quickly add functionality to Rhino for Windows, or automate repetitive tasks.*

### Overview

- [What are VBScript and RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript)

### [RhinoScript 101](/guides/rhinoscript/primer-101)

&nbsp;&nbsp; [Introduction](/guides/rhinoscript/primer-101)  
&nbsp;&nbsp; [Where to find help](/guides/rhinoscript/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [What's it all about?](/guides/rhinoscript/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [RhinoScript Essentials](/guides/rhinoscript/primer-101/2-vbscript-essentials/)  
&nbsp;&nbsp; 3. [Script Anatomy](/guides/rhinoscript/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operators and Functions](/guides/rhinoscript/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Conditional Execution](/guides/rhinoscript/primer-101/5-conditional-execution/)  
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

- [Developer samples on GitHub](https://github.com/mcneel/rhino-developer-samples)
- [Pascal Golay's scripted utilities for Rhino](https://wiki.mcneel.com/people/pascalgolay)
- [RhinoScript Samples on GitHub](https://github.com/mcneel/rhinoscript)
- [RhinoScript Dash Docset](https://discourse.mcneel.com/t/rhinoscript-dash-docset/6382)
- [RhinoScript Help File On-Line](https://www.rhino3d.com/5/rhinoscript/index.html)
- [Scripting discussions on Discourse](https://discourse.mcneel.com/c/scripting)

<!-- ## [Compute](/guides/compute) -->
<h2 id="compute"><a href="/guides/compute">Compute</a></h2>


### Getting Started

{{< dev-topic-list "guides" "Compute" "Getting Started" "weight" >}}

### Production Deployment

{{< dev-topic-list "guides" "Compute" "Deployment" "weight" >}}

### Hops

{{< dev-topic-list "guides" "Compute" "Hops" "weight" >}}

<!-- ## [Eto](/guides/eto) -->
<h2 id="eto"><a href="/guides/eto">Eto</a></h2>

### Overview

- [What is Eto?](/guides/eto/what-is-eto)
- [Why Eto?](/guides/eto/why-eto)

### Getting Started

- [Required Tools](/guides/eto/required-tools)
- [Your First UI](/guides/eto/your-first-ui)

### Fundamentals

- [Forms & Dialogs](/guides/eto/forms-and-dialogs)
- [Existing Dialogs](/guides/eto/existing-dialogs)
- [Containers](/guides/eto/containers)
- [Control Properties](/guides/eto/control-properties)
- [Clipboard (Copy & Paste)](/guides/eto/clipboard)
- [Basic Controls](/guides/eto/controls)
- [Drawable](/guides/eto/advanced-controls/drawable)
- [Cells](/guides/eto/cells)

### DataContext and View Models

- [DataContext](/guides/eto/view-and-data/data-context)
- [What is a View Model?](/guides/eto/view-and-data/view-models)
- [Binding Data with a ViewModel](/guides/eto/view-and-data/binding)
- [Complex Bindings](/guides/eto/view-and-data/complex-bindings)
- [How do Bindings work?](/guides/eto/view-and-data/bindings-explained)

### Rhino Specific Eto

- [Extensions and Helpers](/guides/eto/rhino-specific)

### Advanced

- [Async](/guides/eto/async/)
- [Events](/guides/eto/events/)
- [Examples](/guides/eto/misc-examples/)

## Developer Services

### [Localization](https://www.rhino3d.com/localization)

Our regional office in Europe provides a translation and localization service for third-party developers and anyone else interested in translating their products to French, German, Italian, Spanish, etc. [Details…](https://www.rhino3d.com/localization)

### Marketing Support

If you have developed a Rhino add-on that you would like to make available to other Rhino users, [food4Rhino](https://www.food4rhino.com/) is the place to post the details about your plug-ins for Rhino and Grasshopper. Food4Rhino is the Plug-in Community Service by McNeel.  Users can find the newest Rhino Plug-ins, Grasshopper Add-ons, Materials, Textures and Backgrounds, Scripts and much more. It is free. [See the frequently asked questions...](https://www.food4rhino.com/faq)

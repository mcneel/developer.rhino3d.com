+++
aliases = [ "8/guides/eto", "/wip"]
authors = [ "callum"]
categories = [ "Eto" ]
description = "Guides that apply to developing UIs across platforms using Eto."
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
title = "Eto Guides"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++

{{< call-out note "Follow Along" >}}
  If you're new to Eto, or even an advanced user, it is recommended to open the [script editor](http://localhost:1313/guides/scripting/scripting-command/#first-script) and copy/paste (or better yet write out!) the sample code so you can walk through and understand how Eto works.

  Each page with samples will have both C# and Python 3 (The samples ARE NOT designed for Python 2), will work on both Windows and Mac and assumes little familiarity with Rhino.

  If you're new to programming, this guide will not cover the basics, but will help you dive head-first into C# and/or Python.
{{< /call-out >}}

{{< row >}}
{{< column >}}

### Overview

- [What is Eto?](what-is-eto/)
- [Why Eto?](why-eto/)

{{< /column >}}
{{< column >}}

### Getting Started

- [Required Tools](required-tools/)
<!-- - [Your First UI](your-first-ui/) -->

{{< /column >}}
{{< /row >}}

## Fundamentals

{{< row >}}
{{< column >}}

### Overview 

- [Forms & Dialogs](forms-and-dialogs)
- [Existing Dialogs](existing-dialogs)
- [Containers](containers)
    - [Panels](containers#panels)
    - [Tables](containers#tables)
    - [Stack Layouts](containers#stack-layouts)
    - [Dynamic Layouts](containers#dynamic-layouts)
    - [Pixel Layouts](containers#pixel-layouts)
- [Control Properties](control-properties)
<!-- - [Menu Bar](menu-bar) -->
  <!-- Ensure to mention advanced menu bars -->
<!-- - [Commands](commands) -->
  <!-- I think commands are awesome and should be used more  -->
<!-- - [Layouts](layouts) -->
  <!-- Spacing, Padding (using nulls to space things out!) all the good stuff  -->
<!-- - [Sizing](sizing) -->
  <!-- Spacing, Padding (using nulls to space things out!) all the good stuff  -->
<!-- - [Pixels](screen-pixels) -->

{{< /column >}}
{{< column >}}

### Eto Native Controls
<!-- A simple overview of eto native controls, nothing _too_ fancy -->
- [Basic Controls](controls/)
  - [Button](controls#button)
  - [DropDown](controls#drop-down)
  - [Radio Buttons](controls#radio-buttons)
  - [Check Boxes](controls#check-boxes)
  - [Text Box](controls#text-box)
  - [Text Area](controls#text-area)
- Advanced Controls
  - [Drawable](advanced-controls/drawable)
- Grids
  - [Cells](cells)
  - [Grid View](grid-view)           <!-- Documenting this will be so helpful -->
  - [Tree Grid View](tree-grid-view) <!-- Documenting this will be so helpful -->
  
<!-- - [Image View](advanced-controls/imageviews/) -->
<!-- - [ComboBox](controls#combobox/) -->
<!-- I think this is worth being a bit more extensive than others -->
<!-- - [Numeric Input](advanced-controls/numericUpDown) -->

{{< /column >}}
{{< /row >}}

## DataContext and View Models

{{< call-out note "View Models" >}}
  This section is not for Python, python cannot use View Models and bindings in the same way as C#.
{{< /call-out >}}

{{< row >}}
{{< column >}}

### Getting Started
- [DataContext](view-and-data/data-context/) <!-- Explain how the DataContext trickles downwards! -->
- [What is a View Model?](view-and-data/view-models)
- [Binding Data with a ViewModel](view-and-data/binding)
<!-- - [Binding without a View Model](view-and-data/no-view-model) -->

{{< /column >}}
{{< column >}}

### Advanced
- [Complex Bindings](view-and-data/complex-bindings)
  <!-- Things such as Convert, etc. -->
- [How do Bindings work?](view-and-data/bindings-explained)
  <!-- Very detailed explanation of Bindings -->
  <!-- Why do I need to bind to a property? -->
<!-- - [Alternatives to Bindings](view-and-data/alternatives) {{%comingsoon-label %}} -->
<!-- - [Focus](focus) {{%comingsoon-label %}} -->

{{< /column >}}
{{< /row >}}

<!-- 
## Your First Eto Project {{%comingsoon-label %}}

Building a cross platform UI Layout Manager

{{< row >}}
{{< column >}}

1. [Setup](my-first-eto/setup) // Creating the command and the initial space for our project
1. The Form // Set up the form
1. The View Model // Set up the view model
1. The Rhino Command // Set up the command
1. Starting the View // Set up the view with a layout
1. The Eto Commands // Set up the ui commands
1. Creating a Toolbar // Set up the toolbar, buttons with icons etc
1. Styling // Set up the styling
1. The MenuBar // Set up the MenuBar

{{< /column >}}
{{< column >}}

n. Creating the ...

{{< /column >}}
{{< /row >}}

-->

## Further Reading

{{< call-out warning "Rhino 8" >}}
  The examples below assume you are using Rhino 8, many of these methods or controls may not exist in Rhino 7 or earlier.
{{< /call-out >}}

{{< row >}}
{{< column >}}

### Rhino Specific Eto

{{< dev-topic-list "guides" "eto" "Advanced" "weight" >}}

- [Extensions and Helpers](rhino-specific)
  - [Proper Parenting](rhino-specific#showing-a-dialog)
  - [Light and Dark Mode](rhino-specific#rhinostyle)
  - [Converters](rhino-specific#converters)
  - [Rhino Document](rhino-specific#rhino-doc)
<!--
  - UIs in Grasshopper {{%comingsoon-label %}}
  - UIs in the Script Editor {{%comingsoon-label %}}
  - UIs in Commands {{%comingsoon-label %}}
-->
<!-- -->
<!--
- [Rhino Controls](rhino-specific/controls) {{%comingsoon-label %}}
  - NumericUpDownWithUnitParsing {{%comingsoon-label %}}
  - ViewportControl {{%comingsoon-label %}}
  - RhinoButtonStackLayout {{%comingsoon-label %}}
  - RhinoDialogPanel {{%comingsoon-label %}}
  - ImageButton {{%comingsoon-label %}}
  - AddRemoveButton {{%comingsoon-label %}}
-->
{{< /column >}}
{{< column >}}

### Advanced
- [Async](async/)
- [Events](events/)
<!--
- OS Specific eccentricities {{%comingsoon-label %}}
  - Windows {{%comingsoon-label %}}
// I can't think of any in particular
  - Mac OSX {{%comingsoon-label %}}
    - Multiple Documents {{%comingsoon-label %}}
  - Styling {{%comingsoon-label %}}
// How to create os specific styles 
- Custom Controls {{%comingsoon-label %}}
// Inheriting from and modifying controls
- Custom Handlers {{%comingsoon-label %}}
// Custom platform wrapping stuff
// Maybe even drag/drop?
- Localization {{%comingsoon-label %}}
  - Strings {{%comingsoon-label %}}
  - Menus {{%comingsoon-label %}}
// bits to know about cross platform
// What is with that & thing
// Windows access keys?
// Ensure to use GET not NEW
-->

### Miscellaneous Eto examples
- [Examples](misc-examples/)


{{< /column >}}
{{< /row >}}

## Eto Links

- [Eto Source](https://github.com/picoe/eto)
- [Eto License](https://github.com/picoe/Eto/blob/develop/LICENSE.txt)
- [Eto API Reference](http://pages.picoe.ca/docs/api/)
- [Contributing to Eto](https://github.com/picoe/Eto/wiki/Contributing)
- [Discus Rhino and Eto](https://discourse.mcneel.com/)

<!-- - [How does Eto work?](eto-explained) {{%comingsoon-label %}} -->
<!-- An explanation of How eto wraps other UIs, mostly for my own benefit -->

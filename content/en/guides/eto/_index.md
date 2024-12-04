+++
aliases = [ "8/guides/eto", "/wip/guides/eto/"]
authors = [ "callum", "curtis" ]
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
  It is worth noting that many, if not all of these pages will have code samples. If you're new to Eto, or even an advanced user, it is recommended to open the [script editor](http://localhost:1313/en/guides/scripting/scripting-command/#first-script) and copy/paste (or better yet write out!) the sample code so you can walk through and understand how Eto works.

  Each page with samples will have both C# and Python 3, will work on both Windows and Mac and assumes minor familiarity with Rhino.
{{< /call-out >}}

{{< row >}}
{{< column >}}

### Overview

- [What is Eto?](/guides/eto/what-is-eto/)
- [Why Eto?](/guides/eto/why-eto/)
<!-- - [What's New?](/guides/eto/whats-new/) -->

{{< /column >}}
{{< column >}}

### Getting Started

- [Required Tools](/guides/eto/required-tools/)
- [Your First UI](/guides/eto/your-first-ui/)

{{< /column >}}
{{< /row >}}

## Fundamentals

{{< row >}}
{{< column >}}

### Overview 

- [Forms & Dialogs](/guides/eto/forms-and-dialogs)
- [Containers](/guides/eto/containers)
    - [Panels](/guides/eto/containers#panels)
    - [Tables](/guides/eto/containers#tables)
    - [Stack Layouts](/guides/eto/containers#stack-layouts)
    - [Dynamic Layouts](/guides/eto/containers#dynamic-layouts)
    - [Pixel Layouts](/guides/eto/containers#pixel-layouts)
- [Menu Bar](/guides/eto/menu-bar)
  <!-- Ensure to mention advanced menu bars -->
- [Commands](/guides/eto/commands)
  <!-- I think commands are awesome and should be used more  -->
- [Layouts](/guides/eto/layouts)
  <!-- Spacing, Padding (using nulls to space things out!) all the good stuff  -->
- [Sizing](/guides/eto/sizing)
  <!-- Sizing, automatic, manual etc. -->

{{< /column >}}
{{< column >}}

### Eto Native Controls
<!-- A simple overview of eto native controls, nothing _too_ fancy -->
- [Controls](/guides/controls/)
  - [Button](/guides/eto/controls/button/)
  - [ComboBox](/guides/eto/controls/combobox/)
  - [Radio Buttons](/guides/eto/controls/radiobuttons/)
  - [Check Boxes](/guides/eto/controls/checkboxes/)
  - [Text Inputs](/guides/eto/controls/textinput/)
    - [Text Box](/guides/eto/controls/textinput/box)
    - [Text Area](/guides/eto/controls/textinput/area)
  - [Grid View](/guides/eto/containers#grid-view)
    <!-- Ensuring the data works on these is so annoying. Documenting this will be so helpful -->
  - [Tree Views](/guides/eto/controls/treeviews/)
    <!-- Ensuring the data works on these is so annoying. Documenting this will be so helpful -->
  - [Image View](/guides/eto/controls/imageviews/)
  - [Drawable](/guides/eto/controls//drawable)
    <!-- I think this is worth being a bit more extensive than others -->
  - [Numeric Input](/guides/eto/controls//numericUpDown)

{{< /column >}}
{{< /row >}}

## DataContext and View Models

{{< row >}}
{{< column >}}

### Getting Started
- [DataContext](/guides/eto/view-and-data/data-context/) <!-- Explain how the DataContext trickles downwards! -->
- [What is a View Model?](/guides/etoview-and-data//view-models)
- [Binding Data with a ViewModel](/guides/etoview-and-data//binding)
- [Binding without a View Model](/guides/eto/view-and-data/no-view-model)

{{< /column >}}
{{< column >}}

### Advanced
- [Complex Bindings](/guides/eto/view-and-data/complex-bindings)
  <!-- Things such as Convert, etc. -->
- [How do Bindings work?](/guides/eto/view-and-data/bindings-explained) {{%comingsoon-label %}}
  <!-- Very detailed explination of Bindings -->
  <!-- Why do I need to bind to a property? -->
- [Alternatives to Bindings](/guides/eto/view-and-data/alternatives) {{%comingsoon-label %}}

{{< /column >}}
{{< /row >}}

## Your First Eto Project {{%comingsoon-label %}}

Building a cross platform UI Layout Manager

{{< row >}}
{{< column >}}

1. [Setup](my-first-eto/setup) <!-- Creating the command and the initial space for our project -->
1. The Form <!-- Set up the form -->
1. The View Model <!-- Set up the view model -->
1. The Rhino Command <!-- Set up the command -->
1. Starting the View <!-- Set up the view with a layout -->
1. The Eto Commands <!-- Set up the ui commands -->
1. Creating a Toolbar <!-- Set up the toolbar, buttons with icons etc -->
1. Styling <!-- Set up the styling -->
1. The MenuBar <!-- Set up the MenuBar -->

{{< /column >}}
{{< column >}}

n. Creating the ...

{{< /column >}}
{{< /row >}}

## Further Reading

{{< call-out warning "Rhino 8" >}}
  The examples below assume you are using Rhino 8, many of these methods or controls may not exist in Rhino 7 or earlier.
{{< /call-out >}}

{{< row >}}
{{< column >}}

### Rhino Specific Eto

{{< dev-topic-list "guides" "eto" "Advanced" "weight" >}}

- [Extensions and Helpers](/guides/eto/rhino-specific)
  - [Proper Parenting](/guides/eto/rhino-specific#showing-a-dialog)
  - [Light and Dark Mode](/guides/eto/rhino-specific#rhinostyle)
  - [Converters](/guides/eto/rhino-specific#converters)
  - [Rhino Document](/guides/eto/rhino-specific#rhino-doc)
  - UIs in Grasshopper {{%comingsoon-label %}}
  - UIs in the Script Editor {{%comingsoon-label %}}
  - UIs in Commands {{%comingsoon-label %}}
<!-- -->
- [Rhino Controls](/guides/eto/rhino-specific/controls) {{%comingsoon-label %}}
  - NumericUpDownWithUnitParsing {{%comingsoon-label %}}
  - ViewportControl {{%comingsoon-label %}}
  - RhinoButtonStackLayout {{%comingsoon-label %}}
  - RhinoDialogPanel {{%comingsoon-label %}}
  - ImageButton {{%comingsoon-label %}}
  - AddRemoveButton {{%comingsoon-label %}}

{{< /column >}}
{{< column >}}

### Advanced

{{< dev-topic-list "guides" "eto" "Advanced" "weight" >}}

- OS Specific eccentricities {{%comingsoon-label %}}
  - Windows {{%comingsoon-label %}}
    <!-- I can't think of any in particular -->
  - Mac OSX {{%comingsoon-label %}}
    - Multiple Documents {{%comingsoon-label %}}
  - Styling {{%comingsoon-label %}}
    <!-- How to create os specific styles  -->
- Custom Controls {{%comingsoon-label %}}
  <!-- Inheriting from and modifying controls -->
- Custom Handlers {{%comingsoon-label %}}
  <!-- Custom platform wrapping stuff -->
- Mouse Events {{%comingsoon-label %}}
  <!-- Maybe even drag/drop? -->
- Async {{%comingsoon-label %}}
  <!-- Line between async and non-async -->
  <!-- async events -->
  <!-- invoke async -->
  <!-- DO NOT FORCE WAIT ASYNC ON NON-ASYNC -->
- Localization {{%comingsoon-label %}}
  - Strings {{%comingsoon-label %}}
  - Menus {{%comingsoon-label %}}
      <!-- bits to know about cross platform -->
      <!-- What is with that & thing -->
      <!-- Windows access keys? -->
      <!-- Ensure to use GET not NEW -->

{{< /column >}}
{{< /row >}}

## Eto Links

{{< row >}}
{{< column >}}

- [Eto Source](https://github.com/picoe/eto)
- [Eto API Reference](http://pages.picoe.ca/docs/api/)
- [Eto License](https://github.com/picoe/eto/LICENSE.md)

<!-- - [How does Eto work?](/guides/eto/eto-explained) {{%comingsoon-label %}} -->
<!-- An explaination of How eto wraps other UIs, mostly for my own benefit -->

#### Get Involved
Eto is completely open source and accepting edits, fixes, changes and suggestions
- [Work on Eto](https://github.com/picoe/eto)

{{< /column >}}
{{< /row >}}

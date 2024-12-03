+++
aliases = [ "8/guides/eto", "/wip/guides/eto/"]
authors = "unset"
categories = [ "Unsorted" ]
description = "Guides that apply to developing UIs across platforms using Eto."
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "unset"
title = "Eto Guides"
type = "guides"
weight = 1
draft = true

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

+++
{{< row >}}
{{< column >}}

### Overview

- [What is Eto?](/guides/eto/what-is-eto/)
- [Why Eto?](/guides/eto/why-eto/)
<!-- - [What's New?](/guides/eto/whats-new/) -->

{{< /column >}}
{{< column >}}

### Getting Started

- Installing Tools ([Cross Platform](/guides/eto/installing-tools/))
- Your First UI ([Cross Platform](/guides/eto/your-first-ui/))

{{< /column >}}
{{< /row >}}

## Fundamentals

{{< row >}}
{{< column >}}

### Overview 

- [Forms & Dialogs](/guides/eto/forms-and-dialogs)
  - [Premade Dialogs](/guides/eto/forms-and-dialogs/premade)
- [Containers](/guides/eto/containers)
    - [Panel](/guides/eto/containers/panel)
    - [Tables](/guides/eto/containers/tables)
    - [Stack Layout](/guides/eto/containers/stack-layout)
    - [Dynamic Layout](/guides/eto/containers/dynamic-layout)
    - [Pixel Layout](/guides/eto/containers/pixel-layout)
- [Menu Bar](/guides/eto/menu-bar)
  <!-- Ensure to mention advanced menu bars -->
- [Commands](/guides/eto/commands)
  <!-- I think commands are awesome and should be used more  -->

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
  - [Grid View](/guides/eto/containers/grid-view)
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

1. [Setup](/guides/eto/project-1/step-1) <!-- Creating the command and the initial space for our project -->
1. [The Form](/guides/eto/project-1/step-2) <!-- Set up the form -->
1. [The View Model](/guides/eto/project-1/step-3) <!-- Set up the view model -->
1. [The Rhino Command](/guides/eto/project-1/step-4) <!-- Set up the command -->
1. [Starting the View](/guides/eto/project-1/step-5) <!-- Set up the view with a layout -->
1. [The Eto Commands](/guides/eto/project-1/step-6) <!-- Set up the ui commands -->
1. [Creating a Toolbar](/guides/eto/project-1/step-7) <!-- Set up the toolbar, buttons with icons etc -->
1. [Styling](/guides/eto/project-1/step-...) <!-- Set up the styling -->
1. [The MenuBar](/guides/eto/project-1/step-...) <!-- Set up the MenuBar -->

{{< /column >}}
{{< column >}}

n. [Creating the ...](/guides/eto/project-1/step-n)

{{< /column >}}
{{< /row >}}

## Further Reading {{%comingsoon-label %}}

{{< row >}}
{{< column >}}

### Rhino Specific Eto

{{< dev-topic-list "guides" "eto" "Advanced" "weight" >}}

- [Eto UIs in Rhino](/guides/eto/rhino-specific)
  - [UIs in Grasshopper](/guides/eto/rhino-specific/grasshopper)
  - [UIs in the Script Editor](/guides/eto/rhino-specific/script-editor)
  - [UIs in Commands](/guides/eto/rhino-specific/command-uis)
<!-- -->
- [Rhino Controls](/guides/eto/rhino-controls)
  - [Rhino Controls](/guides/eto/rhino-controls)

{{< /column >}}
{{< column >}}

### Advanced

{{< dev-topic-list "guides" "eto" "Advanced" "weight" >}}

- [OS Specific eccentricities](/guides/eto/os-specifics)
  - [Windows](/guides/eto/os-specifics/win)
    <!-- I can't think of any in particular -->
  - [Mac OSX](/guides/eto/os-specifics/mac)
    - [Multiple Documents](/guides/eto/os-specifics/mac/multi-doc)
  - [Styling](/guides/eto/os-specifics/styling)
    <!-- How to create os specific styles  -->
- [Custom Controls](/guides/eto/custom-controls)
  <!-- Inheriting from and modifying controls -->
- [Custom Handlers](/guides/eto/custom-handlers)
  <!-- Custom platform wrapping stuff -->
- [Mouse Events](/guides/eto/mouse-events)
  <!-- Maybe even drag/drop? -->
- [Async](/guides/eto/async)
  <!-- Line between async and non-async -->
  <!-- async events -->
  <!-- invoke async -->
  <!-- DO NOT FORCE WAIT ASYNC ON NON-ASYNC -->
- [Localization](/guides/eto/localization)
  - [Strings](/guides/eto/localization/strings)
  - [Menus](/guides/eto/localization/menus)
      <!-- bits to know about cross platform -->
      <!-- What is with that & thing -->
      <!-- Windows access keys? -->
      <!-- Ensure to use GET not NEW -->

{{< /column >}}
{{< /row >}}

## Further Reading

{{< row >}}
{{< column >}}

- [Eto Source](www.website.com)
- [Eto API Reference](www.website.com)
- [Eto License](www.website.com)
- [How does Eto work?](/guides/eto/eto-explained) {{%comingsoon-label %}}
<!-- An explaination of How eto wraps other UIs, mostly for my own benefit -->

{{< /column >}}
{{< /row >}}

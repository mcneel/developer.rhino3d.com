+++
title = ""
description = ""
type = "guides"
categories = ["Scripting"]
keywords = [ "", "" ]
languages = [ "C#", "Python", "CPython", "IronPython", "VB" ]
authors = ["ehsan"]
sdk = [ "RhinoCommon" ]
weight = 4

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

<style>
    .main-content img { zoom: 50%; }
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
        font-size: 14px;
    }
</style>

Rhino Script Editor is designed to utilize the widespread plugin infrastructure in both Rhino and Grasshopper, and generate plugins from your scripts.

Script editor can:

- Convert scripts into Rhino commands and publish as Rhino plugin (`.rhp` file)
- Convert scripts into Grasshopper components and publish as Grasshopper plugin (`.gha` file)
- Create a Yak package and publish on Rhino package server

It can also:

- Generate toolbar layout files for published Rhino commands (`.rui` file)
- Share code libraries and data files with published commands or components
- Generate dotnet project solution for published plugins for furthur customization (`.sln` and `.csproj` files)

## Create a Project

To create a project:

- Run `ScriptEditor` command
- Choose **Create Project** from main *File* menu
- Navigate to where you would like to save the project. Project file will be stored with `.rhproj` extension
- Editor displays **Edit Project** dialog.

  This dialog highlights the most important pieces of information about the new project:

  - **Id**: Unique UUID of this project. It should not be changed. See [Project Id](#project-id)
  - **Name**: Plugins will be published with this name. See [Project Name](#project-name)
  - **Version**: Plugins will be published with this version. See [Project Version](#project-version)
  - **Author**: This is required and if there are no authors available, this field will show a *No Author* error. See [Project Authors](#project-authors)

![](project-edit-info.png)

- Choose **Save Changes**
- Project file is now saved and editor opens the **Projects** panel on the left browser tray

![](project-open-in-tray.png)

- Now that the project saved and open, we can add command and components. We will get a chance to edit project information before publishing the project as plugins.

## Add Commands

To add a command, click on the **+** icon on the *Project Tray* toolbar and select **Add Commands/** item:

![](project-commands-add-button.png)

You can also right-click on the **Commands/** to add new commands:

![](project-commands-add-rclick.png)

You can select a single or multiple scripts and add them to the project. Once scripts are added, they are opened in the editor and a black circle appears in front of project name in *Project Tray* to show that project is modified and must be saved. Click the Save Project button in *Project Tray* toolbar to save the project:

![](project-commands-added.png)

{{< call-out "note" "Note" >}}
Rhino commands can be created from Grasshopper scripts that contain contextual inputs and outputs. In the example above, `Script_C` is a Grasshopper 1 definition (`Script_C.gh`) that contains two contextual integer inputs and a contextual print output component.

![](project-commands-gh1.png)

See [Running Published Commands](#running-published-commands) for information on how the inputs are collected on Rhino command line.
{{< /call-out >}}

During build, each script under **Commands/** is converted into a Rhino command. The script name is the default name of the command. See [Edit Commands](#edit-commands) for information on editing command, assigning icons, and changing command types.

## Add Components

To add components, click on the **+** icon on the *Project Tray* toolbar and select **Add Components/** item:

![](project-comps-add-button.png)

You can also right-click on the **Components/** to add new components:

![](project-comps-add-rclick.png)

#### Components Types

When adding components to a project, an open dialog appears asking for Grasshopper definitions (`.gh` or `.ghx`). Depending on the contents of the definition, one of these two types of components are created in the project:

- **Script:** If Grasshopper definition *does not contain* any contextual inputs or outputs, a component is created for each *Script* that exist in the definition. The new component matches nickname, inputs, and outputs of the *Script* and runs the same code.

  **Example:**

  In this example, the definition contains 3 *Script* components, nicknamed *First*, *Second*, and *Third*. Each script components becomes a component in published Grasshopper plugin matching the nickname, inputs, and outputs. See [Edit Components](#edit-components) on how to edit components, add icons, and set their exposure.

  ![](project-comps-added-scripts.png)

  This is how the components look like when published. They show a default icon since we have not added any icons yet. Also note that although they are generated from scripts of different languages, the published components are language agnostic and the three components look the same:

  ![](project-comps-published-script.png)

- **Contextual:** If Grasshopper definition *does contain* contextual inputs or outputs, a single component is created for the complete definition. The new component matches the contextual inputs and outputs of the definition and runs the full definition on each iteration.

  **Example:**

  In this example, the definition contains contextual inputs and outputs. The complete definition becomes a component in published Grasshopper plugin, and its name matches the definition name by default. Component inputs and outputs will match contextual inputs and outputs of the definition. Note that any other *Script* component in this definition is not converted. See [Project Components](#project-components) on how to edit components, add icons, and set their exposure.

  ![](project-comps-added-ctx.png)

  This is how the component looks like when published. It shows a default icon since we have not added any icons yet:

  ![](project-comps-published-ctx.png)

## Build and Publish

Once the project is built, a Yak package is generated that contains both Rhino and Grasshopper plugins.

{{< call-out "note" "Note" >}}
See [Pushing a Package to the Server](/guides/yak/pushing-a-package-to-the-server) on how to publish `.yak` files to package server
{{< /call-out >}}

## Run Published Commands

## Use Published Components

## Edit Project Info

### Project Id

### Project Name

### Project Version

### Project Authors

### Project Copyright, License, and URL

## Edit Commands

## Edit Components

## Advanced

### Shared Libraries

### Shared Resources

### Project Solution

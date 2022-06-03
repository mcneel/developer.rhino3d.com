+++
authors = [ "john.croudy" ]
categories = [ "RDK" ]
description = "This guide describes the RDK Material, Environment, and Texture Editors"
keywords = [ "material", "environment", "texture", "RDK", "Render Content", "editor" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "RDK Render Content Editors"
type = "guides"
weight = 5
override_last_modified = "2019-01-22T17:37:39Z"

[admin]
TODO = ""
origin = "http://developer.rhino3d.com/files/rhino_rdk_documentation.pdf"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++
The _RDK Render Content Editors_ display objects called _Render Contents_ and allow the user to edit them. These editors are all based on a similar interface with only small functional differences between them. Render Contents are the foundation of the RDK core and one of the most important objects it provides. Please see [Render Content](/guides/cpp/rdk-render-content) for more information. The Texture Editor is known to users as the Texture _Palette_ but programmatically it is an editor just like the other two.

{{< image url="/images/rdk-met-editors.png" alt="Material Environment and Texture Editors" class="float_right" >}}

1. Navigation controls similar to those found on a web browser.
2. Resizeable Floating Previews.
3. Configurable thumbnails with multiple sizes and styles.
4. Resizeable preview pane.
5. User interface for editing render content parameters (AKA _fields_).
6. Breadcrumb navigation control similar to those found on file explorers.
7. [Task](/guides/cpp/rdk-task-classes/) menu for performing actions on render contents and setting editor options.

These editors are integrated with Rhino's tabbed pane system. You can access them through the Rhino Render menu, the Rendering tool bar, or the editor commands.

Lists of materials, environments, and textures are stored in the Rhino document. Each editor displays the relevant render content type as preview thumbnails.

Contents display an interface below the preview thumbnails in an area reserved for collapsible UI panels. An addition to the basic UI panels, several additional collapsible panels are provided by Rhino within the same area as the content UI. These include the Name, Notes, Texture Summary, Local Mapping, Graph and Adjustment panels.

Each material, environment or texture can have child nodes (AKA _child slots_ or _sub-nodes_). The children can be of any content type, but specific child slots will only support specific types. The most common child type is a texture. For example, the _Color_ child slot for a Custom Material will only support textures, as will the _Background image_ child slot on a Basic Environment.

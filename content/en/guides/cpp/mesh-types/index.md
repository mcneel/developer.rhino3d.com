+++
aliases = ["/en/5/guides/cpp/mesh-types/", "/en/6/guides/cpp/mesh-types/", "/en/7/guides/cpp/mesh-types/", "/wip/guides/cpp/mesh-types/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide discusses the types of meshes found in Rhino."
keywords = [ "rhino", "mesh" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Mesh Types"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/meshtypes"
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

 
## Which Mesh?

There is an `ON_Brep::GetMeshes()` routine of the C/C++ SDK.  You might find that very adequate meshes can be pulled from this routine when specifying `ON::render_mesh`.  You may have also noticed that you can also run this routine with an enumeration for an "analysis mesh," a "default mesh," a "preview mesh," or "any mesh."

What are the differences between all of these options?

## Discussion

Here is an overview of the mesh types:

1. `ON::render_mesh` is a mesh for, obviously, rendering.  This rendering can be for shaded or rendered display. It can also be used by rendering plugins.  The quality of these meshes is controlled by the Meshes page in the Document Properties dialog, but can also be overridden on a per-object basis.
1. `ON::analysis_mesh` is used by analysis modes, such as curvature, draft angle, environment map, and zebra.
1. `ON::preview_mesh` is used when you use the Mesh command and poke the preview button - the pipeline needs a way to display preview meshes and this is it.
1. `ON::default` mesh returns `ON::render_mesh` if it exists.  Otherwise it returns `ON::analysis_mesh` if it exists.
1. `ON::any_mesh` is only used when we want delete all meshes at one time.

**NOTE**: render and analysis meshes do not appear automatically.  Some command must trigger their creation, whether its just setting viewport for rendered display or running an analysis command.  The can also be generated from plugins that call SDK functions.

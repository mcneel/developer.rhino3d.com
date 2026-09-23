+++
aliases = [""]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "An overview of the new and changed items for developers in Rhino 9."
keywords = [ "developer", "rhino", "v9", "whats new" ]
languages = [ "All" ]
sdk = [ "General" ]
thumbnail = "/images/new-in-v9/unfurl.png"
title = "New for Developers in V9"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac", "Linux" ]
since = 0

[page_options]
block_webcrawlers = true
+++

{{< presenter-mode >}}

Rhino 9 brings a C++ SDK on Mac, Rhino.Compute on Linux, significant improvements to its code editor, support for CPython 3.13 and .NET 10, major improvements to our free SDKs, with API refinements, and the introduction of Grasshopper 2 as a development target. Some changes can also have an effect on your existing plugins.

## Platforms and Targets

{{< card-gallery >}}
{{< feature-card page="/guides/cpp" url="/guides/cpp/your-first-plugin-mac/" image="/images/new-in-v9/cpp-mac.png" title="C++ SDK on Mac" description="Build with C++ for both Windows and Mac" >}}
{{< feature-card page="/guides/compute/compute-linux-getting-started" image="/images/new-in-v9/compute-linux.png" title="Rhino.Compute on Linux" description="Access the Rhino and Grasshopper SDKs through a stateless REST API. Now available on Linux Servers." >}}
{{< feature-card page="/guides/rhinocommon/moving-to-dotnet-core" image="/images/new-in-v9/dotnet-10.png" title=".NET 10 Upgrade" description=".NET 10 framework running on both Windows and Mac." >}}
{{< feature-card page="/guides/grasshopper2/your-first-component-windows" image="/images/new-in-v9/gh2-component.png" title="Grasshopper 2 Components" description="A beginners guide to creating your first Grasshopper 2 Component" >}}
{{< feature-card page="/guides/grasshopper2/migrating-components-to-gh2" image="/images/new-in-v9/gh2-migrate.png" title="Move to Grasshopper 2" description="Migrate your Grasshopper 1 Components to Grasshopper 2" >}}
{{< /card-gallery >}}

## SDK Enhancements

{{< card-gallery >}}
{{< feature-card page="/guides/cpp/dotnet-interop" image="/images/new-in-v9/cpp-dotnet-interop.png" title="C++ to .NET Interop" description="Named Callbacks in C++ for easier access to .NET functionality" >}}
{{< feature-card page="/guides/rhinocommon" url="https://mcneel-apidocs.herokuapp.com/api/rhinocommon/whatsnew/9.0" image="/images/new-in-v9/rhinocommon.png" title="RhinoCommon" description="New APIs for Shrinkwrap, Flair, Code-Driven File IO, and more..." >}}
{{< feature-card page="/guides/general/rhino-ui-system/in-viewport-ui" image="/images/new-in-v9/in-viewport-ui.png" title="In-Viewport User Interface" description="Controls and grips directly in the Rhino viewport" >}}
{{< /card-gallery >}}

## Scripting Updates

{{< card-gallery >}}
{{< feature-card page="/guides/rhinopython/python-3-in-rhino" image="/images/new-in-v9/python3.png" title="Python Updates" description="Support for Python 3 in Rhino and Grasshopper." >}}
{{< feature-card page="/guides/scripting" url="https://www.rhino3d.com/features/developer/scripting/" image="/images/new-in-v9/scripting.png" title="Scripting Improvements" description="Entirely new editor for Python 3 and C#, in Rhino and Grasshopper." >}}
{{< /card-gallery >}}

## Changes That Can Affect Your Plugin

Be aware of these changes before you release a plugin for Rhino 9.

{{< card-gallery >}}
{{< feature-card page="/guides/general/rhino-technology-overview/opengl" image="/images/new-in-v9/opengl.png" title="OpenGL Is Not the Default" description="Rhino 9 does not use OpenGL by default. Read this if your plugin calls OpenGL directly." >}}
{{< feature-card page="/guides/rhinocommon/moving-to-dotnet-core" url="/guides/rhinocommon/moving-to-dotnet-core/#choosing-the-net-runtime-on-windows" image="/images/new-in-v9/dotnet-framework.png" title=".NET Framework Is Deprecated" description="Move your plugins to .NET 10. Do not release new plugins that target .NET Framework only." >}}
{{< feature-card page="/guides/rhinocommon/moving-to-dotnet-core" url="/guides/rhinocommon/moving-to-dotnet-core/#binaryformatter" image="/images/new-in-v9/binaryformatter.png" title="BinaryFormatter in Rhino.Inside" description="Hosts that use .NET 10 do not enable BinaryFormatter. Code that uses it will fail." >}}
{{< feature-card page="/guides/general/rhino-ui-system" url="/guides/general/rhino-ui-system/#rhino-9" image="/images/new-in-v9/toolbars.png" title="Toolbars" description="Toolbars work as they did in Rhino 7. Read how RUI files work in Rhino 9." >}}
{{< /card-gallery >}}

<br/><br/>
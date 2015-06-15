---
layout: default
---

# Welcome

**Rhino developer tools are royalty free and include support.**

This site is the _future home_ of developer.rhino3d.com.  The goal of this site is to consolidate all the (now) scattered developer documentation into a single canonical site that is clear, easy-to-navigate, with consistent formatting and nomenclature.  _This site is a work-in-progress_.  

The sources of content-to-be-consolidated are:

- [Rhino Developer Tools wiki](http://wiki.mcneel.com/developer/home)
- [RhinoCommon API references](http://4.rhino3d.com/5/rhinocommon/)
- [C++ SDK API references](http://4.rhino3d.com/5/rhinocppsdk/idx.html)
- [RhinoCommon samples on GitHub](https://github.com/mcneel/rhinocommon/tree/master/examples)
- [DaleF's CsCommands](https://github.com/dalefugier/SampleCsCommands/)
- [Doxygen Docs (on McNeel intranet)](http://phab.mcneel.com/docs/rhino/6/rhinocommon/)

This website is [open source on GitHub](https://github.com/mcneel/developer-rhino3d-com). If you find errors or think a page could be improved, just click the “Edit page on GitHub” link at the bottom of the page.  See [contributing to this website](#this-website) below for more details.

## Overview

Rhino exposes purpose-built APIs in C#, C/C++, VB.NET, and Python...

| API | &nbsp; &nbsp; &nbsp; &nbsp; | Platforms | &nbsp; &nbsp; &nbsp; &nbsp; | Languages |  &nbsp; &nbsp; &nbsp; &nbsp; | Primary Uses |
|:----|:----:|:------------------------:|:----:|:----------:|:----:|:----|
| RhinoCommon  |  &nbsp; &nbsp; &nbsp; &nbsp; | ![Windows]({{ site.baseurl }}/images/win_logo_small.png){:height="35px" width="35px"} &nbsp; ![Mac OS X]({{ site.baseurl }}/images/mac_logo_small.png){:height="35px" width="35px"} |  &nbsp; &nbsp; &nbsp; &nbsp;  | ![C#]({{ site.baseurl }}/images/cs_logo_small.png){:height="35px" width="35px"} &nbsp; ![VB.NET]({{ site.baseurl }}/images/vb_logo_small.png){:height="35px" width="35px"} &nbsp; ![Python]({{ site.baseurl }}/images/python_logo_small.png){:height="35px" width="35px"} |   &nbsp; &nbsp; &nbsp; &nbsp; |  Cross-platform plugins.  Grasshopper plugins.
| Rhino.Python  |  &nbsp; &nbsp; &nbsp; &nbsp; | ![Windows]({{ site.baseurl }}/images/win_logo_small.png){:height="35px" width="35px"} &nbsp; ![Mac OS X]({{ site.baseurl }}/images/mac_logo_small.png){:height="35px" width="35px"} |  &nbsp; &nbsp; &nbsp; &nbsp;  | ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} &nbsp; ![Python]({{ site.baseurl }}/images/python_logo_small.png){:height="35px" width="35px"} |   &nbsp; &nbsp; &nbsp; &nbsp; |  Cross-platform scripting.
| openNURBS  |  &nbsp; &nbsp; &nbsp; &nbsp; | ![Windows]({{ site.baseurl }}/images/win_logo_small.png){:height="35px" width="35px"} &nbsp; ![Mac OS X]({{ site.baseurl }}/images/mac_logo_small.png){:height="35px" width="35px"} |  &nbsp; &nbsp; &nbsp; &nbsp;  | ![C#]({{ site.baseurl }}/images/cs_logo_small.png){:height="35px" width="35px"} &nbsp; ![C/C++]({{ site.baseurl }}/images/cpp_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |   &nbsp; &nbsp; &nbsp; &nbsp; |  openNURBS 3dm file IO outside Rhino.
| RhinoScript  |  &nbsp; &nbsp; &nbsp; &nbsp; | ![Windows]({{ site.baseurl }}/images/win_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |  &nbsp; &nbsp; &nbsp; &nbsp;  | ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} &nbsp; ![VB.NET]({{ site.baseurl }}/images/vb_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |   &nbsp; &nbsp; &nbsp; &nbsp; |  Rhino for Windows scripting.
| C/C++  |  &nbsp; &nbsp; &nbsp; &nbsp; | ![Windows]({{ site.baseurl }}/images/win_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |  &nbsp; &nbsp; &nbsp; &nbsp;  | ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} &nbsp; ![C/C++]({{ site.baseurl }}/images/cpp_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |   &nbsp; &nbsp; &nbsp; &nbsp; |  Rhino for Windows plugins.
| Grasshopper  |  &nbsp; &nbsp; &nbsp; &nbsp; | ![Windows]({{ site.baseurl }}/images/win_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |  &nbsp; &nbsp; &nbsp; &nbsp;  | ![C#]({{ site.baseurl }}/images/cs_logo_small.png){:height="35px" width="35px"} &nbsp; ![VB.NET]({{ site.baseurl }}/images/vb_logo_small.png){:height="35px" width="35px"} &nbsp; ![Python]({{ site.baseurl }}/images/python_logo_small.png){:height="35px" width="35px"} |   &nbsp; &nbsp; &nbsp; &nbsp; |  Grasshopper plugins.
| RDK  |  &nbsp; &nbsp; &nbsp; &nbsp; | ![Windows]({{ site.baseurl }}/images/win_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |  &nbsp; &nbsp; &nbsp; &nbsp;  | ![C#]({{ site.baseurl }}/images/cs_logo_small.png){:height="35px" width="35px"} &nbsp; ![C/C++]({{ site.baseurl }}/images/cpp_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |   &nbsp; &nbsp; &nbsp; &nbsp; |  Renderer plugin development on Windows.
| RAP  |  &nbsp; &nbsp; &nbsp; &nbsp; | ![Windows]({{ site.baseurl }}/images/win_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |  &nbsp; &nbsp; &nbsp; &nbsp;  | ![C#]({{ site.baseurl }}/images/cs_logo_small.png){:height="35px" width="35px"} &nbsp; ![C/C++]({{ site.baseurl }}/images/cpp_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |   &nbsp; &nbsp; &nbsp; &nbsp; |  "Skinning" Rhino for Windows.
| Zoo  |  &nbsp; &nbsp; &nbsp; &nbsp; | ![Windows]({{ site.baseurl }}/images/win_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |  &nbsp; &nbsp; &nbsp; &nbsp;  | ![C#]({{ site.baseurl }}/images/cs_logo_small.png){:height="35px" width="35px"} &nbsp; ![C/C++]({{ site.baseurl }}/images/cpp_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |   &nbsp; &nbsp; &nbsp; &nbsp; |  Zoo license manager plugins on Windows.
| RhinoMobile  |  &nbsp; &nbsp; &nbsp; &nbsp; | ![Android]({{ site.baseurl }}/images/android_logo_small.png){:height="35px" width="35px"} &nbsp; ![iOS]({{ site.baseurl }}/images/ios_logo_small.png){:height="35px" width="35px"} |  &nbsp; &nbsp; &nbsp; &nbsp;  | ![C#]({{ site.baseurl }}/images/cs_logo_small.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} &nbsp; ![na]({{ site.baseurl }}/images/blank.png){:height="35px" width="35px"} |   &nbsp; &nbsp; &nbsp; &nbsp; |  3D mobile application development.
|=====
| &nbsp; &nbsp; |
{: rules="groups"}


## Contributing

Hey, make yourself useful!

#### GitHub

Many [McNeel projects](http://github.com/mcneel) are open-source and on [GitHub](http://github.com/).  [RhinoCommon](https://github.com/mcneel/rhinocommon) - our cross-platform .NET API - is a great example. Even [this very website](https://github.com/mcneel/developer-rhino3d-com) you are reading now. Browse source, fork a repo, correct a typo: we welcome participation and pull-requests.


#### Discourse

[discourse.mcneel.com](http://discourse.mcneel.com) is the McNeel forum.  This is the fastest place to get help.  Specific categories to  in are:

- [Rhino Developer](http://discourse.mcneel.com/c/rhino-developer): Customizing Rhino through VB.NET, C#, C++, RhinoScript, and Python.
- [Scripting](http://discourse.mcneel.com/c/scripting): Topics related to RhinoScript and Python scripting.
- [Grasshopper developer](http://discourse.mcneel.com/c/grasshopper-developer): VB.NET, C#, and Python in Grasshopper components.

#### Report Bugs

Whenever you encounter something that doesn't work as it should, we'd love it if you could file a bug report.  At McNeel, we use [YouTrack](http://mcneel.myjetbrains.com/youtrack/) to track issues and bugs.  YouTrack requires that you create a login. The vast majority of bugs are visible to the public.  Please report issues or bugs with our APIs or SDKs on YouTrack.

#### This website <a id="this-website"></a>

This website is [open source on GitHub](https://github.com/mcneel/developer-rhino3d-com). If you find errors or think a page could be improved, just click the “Edit page on GitHub” link at the bottom of any page.  If you are a McNeel employee, you should already have permissions to commit to this repository.  If you are a Rhino Plugin Developer, you can [request permissions to commit](mailto:steve@mcneel.com).  Anyone can clone the repository and submit a pull-request.

This site uses [Markdown](http://daringfireball.net/projects/markdown/) - specifically [Kramdown](http://kramdown.gettalong.org/quickref.html) - as the base-format for all content.  In the [Guides]({{ site.baseurl }}/guides) area of the site, in the [Developer Docs]({{ site.baseurl }}/guides#dev-docs) section, you will find a number of references to get started contributing to this site.

## Contacts

Who to talk to for what:

- Steve Baer (RhinoCommon) - [steve@mcneel.com](mailto:steve@mcneel.com) - [github.com/sbaer](http://github.com/sbaer)
- Dale Fugier (C/C++ SDK, Zoo, RAP) - [dale@mcneel.com](mailto:dale@mcneel.com) - [github.com/dalefugier](http://github.com/dalefugier)
- Alain Cormier (RhinoPython) - [alain@mcneel.com](mailto:alain@mcneel.com) - [github.com/acormier](http://github.com/acormier)
- David Rutten (Grasshopper) - [david@mcneel.com](mailto:david@mcneel.com) - [github.com/DavidRutten](http://github.com/DavidRutten)
- Andy le Bihan (RDK) - [andy@mcneel.com](mailto:andy@mcneel.com) - [github.com/andylebihan](http://github.com/andylebihan)
- Curtis Wensley (Eto) - [curtis@mcneel.com](mailto:curtis@mcneel.com) - [github.com/cwensley](http://github.com/cwensley)
- Dan Belcher (RhinoMobile) - [dan@mcneel.com](mailto:dan@mcneel.com) - [github.com/dbelcher](http://github.com/dbelcher)

## Plugin Distribution

- Food4Rhino
- package manager

## Rhino Developer Training <a id="rhino-developer-training"></a>

Developer training is a custom, one-on-one session designed to help you become more familiar with the Rhino C++ SDK or the RhinoCommon (.NET) SDK, and to get help in improving your Rhino plug-in product.

Rhino Developer Training is available at both the McNeel Headquarters in **Seattle**, and at our European Headquarters in **Barcelona**.

**We provide**:

* A room and a desk for you to set up your computer.
* A high-speed Internet connection.
* Access to senior Rhino developers for questions and support.
* Inexpensive lodging may be available.

**You should bring**:

Your computer with:

* Rhino C++ SDK:
  * Microsoft Visual C++ 2010 for Rhino 5 64-bit.
  * Microsoft Visual C++ 2005 for Rhino 5 32-bit.
  * The [Rhino C++ SDK](http://www.rhino3d.com/download/rhino-sdk/5.0/release).
  * _Note, Visual C++ 2008, 2012, 2013, and the Express Editions of Visual C++ **will not** work._


* RhinoCommon SDK:
  * Microsoft Visual Studio 2010, 2012 or 2013, with either C# or Visual Basic; or
  * Xamarin Studio (for Mac plugin development).
  * The [RhinoCommon Templates](http://visualstudiogallery.msdn.microsoft.com/16053049-7db2-4c9f-961a-53274ac92ace).
  * _Note, the Express Editions of Visual Studio 2010, 2012, 2013 **will** work._

  * Your Rhino plug-in project source code.
  * Any software you will need to test your plug-in, including copies of your own software.

**Pricing and scheduling**

Developer training is free. You are responsible for paying for travel, lodging, and any other expenses.

For scheduling and travel arrangements in Seattle, contact [Janet Brock](mailto:janet@mcneel.com).

For scheduling and travel arrangements in Barcelona, contact [Carlos Pérez](mailtp:carlos@mcneel.com).

{% comment %}
Ported from: http://wiki.mcneel.com/developer/training
{% endcomment %}

## FAQ

- What SDK is right for me?
- What is Mono?
- Other questions?

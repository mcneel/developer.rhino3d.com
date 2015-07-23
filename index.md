---
layout: toc-page
---


# Welcome
{: .toc-title }

**Rhino developer tools are royalty free and include support.**

This site is the *future home* of all Developer Documentation relating to [Rhinoceros 3D](http://www.rhino3d.com).  [_This website is a work-in-progress_]({{site.baseurl }}/admin/).  The entire site is [open source on GitHub](https://github.com/mcneel/developer-rhino3d-com). If you find errors or think a page could be improved, just click the “Edit page on GitHub” link at the bottom of the page.  See [contributing to this website](#this-website) below for more details.


## Start Here
{: .toc-header }

#### If you want to...

<div>
  <table style="width:100%; border: 1px; margin: 0 auto; padding:0; border-spacing: 0px; border-collapse: separate;">
    <tbody>
      <tr>
        <td style="padding: 20px;">
          <a href="{{ site.baseurl }}/guides/#rhinocommon" title="RhinoCommon: The cross-platform .NET API for Rhino and Grasshopper">
            <img src="{{ site.baseurl }}/images/rhinocommon_logo_intro.png" class="index_use_images">
          </a>
        </td>
        <td style="padding: 20px;">
          <a href="{{ site.baseurl }}/guides/#rhinopython" title="Rhino.Python: Pythonic in three dimensions!">
            <img src="{{ site.baseurl }}/images/rhino_python_logo_intro.png" class="index_use_images">
          </a>
        </td>
        <td style="padding: 20px;">
          <a href="{{ site.baseurl }}/guides/#opennurbs" title="openNURBS is free and open source">
            <img src="{{ site.baseurl }}/images/opennurbs_logo_intro.png" class="index_use_images">
          </a>
        </td>
      </tr>
    </tbody>
  </table>
</div>

The above three paths are not the only options!  Keep reading for more...

## Overview
{: .toc-header }

Rhino exposes purpose-built SDKs in C#, C/C++, VB.NET, VBScript, and Python...

<div class="table-responsive">
<table class="table">
  <thead>
    <tr style="border-bottom:1pt solid black;">
      <th>SDK</th>
      <th width="95px">Platforms</th>
      <th width="125px">Languages</th>
      <th>Primary Uses</th>
    </tr>
  </thead>
  <tbody class="table-striped index_table">
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#rhinocommon" title="RhinoCommon: The cross-platform .NET API for Rhino and Grasshopper"> RhinoCommon</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="index_table_icon" title="Mac OS X"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/vb_logo_small.png" alt="VB.NET" class="index_table_icon" title="VB.NET"><img src="{{ site.baseurl }}/images/python_logo_small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">The cross-platform .NET API for Rhino and Grasshopper</td>  
  </tr>
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#rhinopython" title="Rhino.Python: Pythonic in three dimensions!"> Rhino.Python</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="index_table_icon" title="Mac OS X"></td>
	<td><img src="{{ site.baseurl }}/images/python_logo_small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Cross-platform scripting.</td>  
  </tr>
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#opennurbs" title="openNURBS is free and open source"> openNURBS</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"><img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="index_table_icon" title="Mac OS X"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/cpp_logo_small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">openNURBS 3dm file IO outside Rhino.</td>  
  </tr>
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#rhinoscript" title="RhinoScript is based on Microsoft's VBScript language"> RhinoScript</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/vbscript_logo_small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Rhino for Windows scripting.</td>  
  </tr>
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#cc" title="C/C++ SDK for Rhino for Windows"> C/C++</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/cpp_logo_small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Rhino for Windows plugins.</td>  
  </tr>
   <tr>
    <td><a href="{{ site.baseurl }}/guides/#grasshopper" title="Grasshopper Component Development"> Grasshopper</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/vb_logo_small.png" alt="VB.NET" class="index_table_icon" title="VB.NET"><img src="{{ site.baseurl }}/images/python_logo_small.png" alt="Python via IronPython" class="index_table_icon" title="Python via IronPython"></td>
    <td class="index_table_primary_use">Grasshopper plugins.</td>  
  </tr>
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#rdk" title="Renderer Development Kit"> RDK</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/cpp_logo_small.png" alt="C/C++" class="index_table_icon" title="C/C++"><img src="{{ site.baseurl }}/images/vbscript_logo_small.png" alt="Microsoft VBScript" class="index_table_icon" title="Microsoft VBScript"></td>
    <td class="index_table_primary_use">Renderer plugin development on Windows.</td>  
  </tr>
  <!-- RAP is really just a feature of the C/C++ SDK and the RhinoCommon SDK
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#rap" title="Rhino Application Platform"> RAP</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/cpp_logo_small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">"Skinning" Rhino for Windows.</td>  
  </tr>
  -->
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#zoo" title="Zoo License Manager Plugins"> Zoo</a></td>
	<td><img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="index_table_icon" title="Windows"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"><img src="{{ site.baseurl }}/images/cpp_logo_small.png" alt="C/C++" class="index_table_icon" title="C/C++"></td>
    <td class="index_table_primary_use">Zoo license manager plugins on Windows.</td>  
  </tr>
  <tr>
    <td><a href="{{ site.baseurl }}/guides/#rhinomobile" title="Tools for using 3dm files in mobile applications"> RhinoMobile</a></td>
	<td><img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="index_table_icon" title="Android"><img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="index_table_icon" title="Apple iOS"></td>
	<td><img src="{{ site.baseurl }}/images/cs_logo_small.png" alt="C#" class="index_table_icon" title="C#"></td>
    <td class="index_table_primary_use">3D mobile application development.</td>  
  </tr>
 </tbody>
 </table>
 </div>


{: rules="groups"}

Still unclear?  Browse the [Guides]({{ site.baseurl }}/guides/).  Ask a question in [the Forum](#discourse).  Check out the [FAQ](#faq) below. Ask [a developer](#contacts).


## Contributing
{: .toc-header }

Hey, make yourself useful!


#### GitHub
{: .toc-subheader }

Many [McNeel projects](http://github.com/mcneel) are open-source and on [GitHub](http://github.com/).  [RhinoCommon](https://github.com/mcneel/rhinocommon) - our cross-platform .NET API - is a great example. Even [this very website](https://github.com/mcneel/developer-rhino3d-com) you are reading now. Browse source, fork a repo, correct a typo: we welcome participation and pull-requests.


#### Discourse
{: .toc-subheader }

[discourse.mcneel.com](http://discourse.mcneel.com) is the McNeel forum.  This is the fastest place to get help.  Specific categories to post in are:

- [Rhino Developer](http://discourse.mcneel.com/c/rhino-developer): Customizing Rhino through VB.NET, C#, C++, RhinoScript, and Python.
- [Scripting](http://discourse.mcneel.com/c/scripting): Topics related to RhinoScript and Python scripting.
- [openNURBS](http://discourse.mcneel.com/c/opennurbs): Topics related to the openNURBS toolkit.
- [Grasshopper developer](http://discourse.mcneel.com/c/grasshopper-developer): VB.NET, C#, and Python in Grasshopper components.


#### Report Bugs
{: .toc-subheader }

Whenever you encounter something that doesn't work as it should, we'd love it if you could file a bug report.  At McNeel, we use [YouTrack](http://mcneel.myjetbrains.com/youtrack/) to track issues and bugs.  YouTrack requires that you create a login. The vast majority of bugs are visible to the public.  Please report issues or bugs with our APIs or SDKs on YouTrack.


#### This website
{: .toc-subheader }

This website is [open source on GitHub](https://github.com/mcneel/developer-rhino3d-com). If you find errors or think a page could be improved, just click the “Edit page on GitHub” link at the bottom of any page.  If you are a McNeel employee, you should already have permissions to commit to this repository.  If you are a Rhino Plugin Developer, you can [request permissions to commit](mailto:steve@mcneel.com).  Anyone can clone the repository and submit a pull-request.

This site uses [Markdown](http://daringfireball.net/projects/markdown/) - specifically [Kramdown](http://kramdown.gettalong.org/quickref.html) - as the base-format for all content.  In the [Guides]({{ site.baseurl }}/guides) area of the site, in the [Developer Docs]({{ site.baseurl }}/guides/#developer-docs) section, you will find a number of references to get started contributing to this site.


## Contacts
{: .toc-header }

Who to talk to for what:

- **Steve Baer** (RhinoCommon) - **@stevebaer** on [Discourse](http://discourse.mcneel.com/c/rhino-developer)
- **Alain Cormier** (Rhino.Python) - **@alain** on [Discourse](http://discourse.mcneel.com/c/rhino-developer)
- **Dale Fugier** (C/C++ SDK, Zoo, RAP) - **@dale** on [Discourse](http://discourse.mcneel.com/c/rhino-developer)
- **Dale Lear** (openNURBS) - **@dalelear** on [Discourse](http://discourse.mcneel.com/c/rhino-developer)
- **David Rutten** (Grasshopper) - **[David Rutten](http://www.grasshopper3d.com/profile/DavidRutten)** on the [Grasshopper 3D forum](http://www.grasshopper3d.com)
- **Giulio Piacentino** (GhPython) - **@piac** on [Discourse](http://discourse.mcneel.com/c/rhino-developer)
- **Andy le Bihan** (RDK) - **@andy** on [Discourse](http://discourse.mcneel.com/c/rhino-developer)
- **Curtis Wensley** (Eto) - **@curtisw** on [Discourse](http://discourse.mcneel.com/c/rhino-developer)
- **Dan Belcher** (RhinoMobile) - **@dan** on [Discourse](http://discourse.mcneel.com/c/rhino-developer)

<!-- Removing until we have something meaningful to say
## Plugin Distribution
{: .toc-header }

#### Food4Rhino
{: .toc-subheader }

Lorem ipsum

#### Yak
{: .toc-subheader }

Lorem ipsum
-->

## Developer Training
{: .toc-header }

Developer training is a custom, one-on-one session designed to help you become more familiar with the Rhino C++ SDK or the RhinoCommon (.NET) SDK, and to get help in improving your Rhino plug-in product.

Rhino Developer Training is available at both the McNeel Headquarters in **Seattle**, and at our European Headquarters in **Barcelona**.

#### We provide
{: .toc-subheader }

* A room and a desk for you to set up your computer.
* A high-speed Internet connection.
* Access to senior Rhino developers for questions and support.
* Inexpensive lodging may be available.

#### You should bring
{: .toc-subheader }

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

#### Pricing and scheduling
{: .toc-subheader }

Developer training is free. You are responsible for paying for travel, lodging, and any other expenses.

For scheduling and travel arrangements in Seattle, contact [Janet Brock](mailto:janet@mcneel.com).

For scheduling and travel arrangements in Barcelona, contact [Carlos Pérez](mailto:carlos@mcneel.com).

{% comment %}
Ported from: http://wiki.mcneel.com/developer/training
{% endcomment %}


## FAQ
{: .toc-header }

**Which SDK is right for me?**

It all depends on what you want to do.  If you are looking to automate repetitive tasks in Rhino, writing a [Python]({{ site.baseurl }}/guides/#rhinopython) script is the way to go.  If you are looking to write a full-fledged plugin or Grasshopper component, we strongly suggest the [RhinoCommon SDK]({{ site.baseurl }}/guides/rhinocommon/what_is_rhinocommon/).  If you are very proficient with C/C++, you should consider the native C/C++ SDK (only supported on Rhino for Windows).

**Can I write plugins that run on both Windows and Mac?**

Yes...even using [the same code]({{ site.baseurl }}/guides/rhinocommon/what_is_rhinocommon/).

**What is Mono/Xamarin?**

Mono is an open-source version of Microsoft's .NET runtime that runs on Linux, Mac OS X, iOS, and Android.  Check out the [What are Mono and Xamarin?]({{ site.baseurl }}/guides/rhinocommon/what_are_mono_and_xamarin/) guide for more information.

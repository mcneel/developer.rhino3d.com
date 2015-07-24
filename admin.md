---
layout: fullwidth-page
title: Administration
permalink: /admin/
order: 1
---

# Administration
{: .toc-title }

This site is the _future home_ of developer.rhino3d.com.

The goal of this site is to consolidate all the (now) scattered developer documentation into a single canonical site that is clear, easy-to-navigate, with consistent formatting and nomenclature.

The sources of content-to-be-consolidated are:

- [Rhino Developer Tools wiki](http://wiki.mcneel.com/developer/home)
- [C/C++ Knowledge Base](https://wiki.mcneel.com/developer/sdksamples/knowledgebasecpp) - a mix of samples, how-tos, and guides
- [RhinoCommon API references](http://4.rhino3d.com/5/rhinocommon/)
- [C++ SDK API references](http://4.rhino3d.com/5/rhinocppsdk/idx.html)
- [RhinoCommon samples on GitHub](https://github.com/mcneel/rhinocommon/tree/master/examples)
- [DaleF's CsCommands](https://github.com/dalefugier/SampleCsCommands/)
- [Doxygen Docs (on McNeel intranet)](http://phab.mcneel.com/docs/rhino/6/rhinocommon/)
- Dale Lear's Developer Meeting Notes
- RhinoScript and Rhino.Python Primers
- [Grasshopper SDK Help file (chm)](http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm).

---

## Dev Docs Guides
{: .toc-header }

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  <li><a class="page-link" href="https://github.com/mcneel/developer-rhino3d-com/blob/gh-pages/README.md">Getting Started with Dev Docs</a></li>
  {% for topic in guides %}
    {% if topic.apis contains 'Developer Docs' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## TODO List
{: .toc-header }

#### Guides
{: .toc-subheader }

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.TODO == 1 %}
      <li>
        <a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a>{% if topic.origin != 'unset' %} needs porting from: <a href="{{ topic.origin }}">{{ topic.origin }}</a>{% endif %}
      </li>
    {% endif %}
  {% endfor %}
  </ul>
</div>

#### Misc
{: .toc-subheader }

- [http://www.rhino3d.com/developer](http://www.rhino3d.com/developer) should redirect to [http://developer.rhino3d.com](http://developer.rhino3d.com) (this website) - the link is in all the .h files top comments

- **DO NOT** port any content that relates to pre-Rhino 5: this is old information.  Visual Studio 2010 for the C/C++ SDK was used for Rhino 5.

#### Samples

TODO TODO ...meta.

Here we could report samples that are not passing tests.

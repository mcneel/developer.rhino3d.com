---
layout: fullwidth-page
title: Administration
description: The administrator's view of the developer.rhino3d.com website.
permalink: /admin/
order: 1
---

# Administration

The goal of this site is to consolidate all the (now) scattered developer documentation into a single canonical site that is clear, easy-to-navigate, with consistent formatting and nomenclature.

The sources of content-to-be-consolidated are:

- RhinoScript and Rhino.Python Primers
- [C++ SDK API references](http://4.rhino3d.com/5/rhinocppsdk/idx.html)
- [DaleF's CsCommands](https://github.com/dalefugier/SampleCsCommands/)
- Macros documentation sources: [Macros in Helpfile](http://docs.mcneel.com/rhino/5/help/en-us/information/rhinoscripting.htm), [Macros in Wiki](http://wiki.mcneel.com/rhino/basicmacros), [Using the MacroEditor](http://wiki.mcneel.com/developer/macroscriptsetup)
- <strike>Grasshopper SDK API references (chm)</strike>
- <strike>Grasshopper SDK Help file (chm) topics</strike>
- <strike>Grasshopper Forum posts</strike>
- <strike>Rhino Developer wiki</strike>
- <strike>RhinoCommon API references</strike>
- <strike>RhinoCommon samples on GitHub</strike>
- <strike>Doxygen Docs (on McNeel intranet)</strike>

**DO NOT** port any content that relates to pre-Rhino 5: this is old information.  Visual Studio 2010 for the C/C++ SDK was used for Rhino 5.

---

## Dev Docs Guides

- [Getting Started with Developer Docs](https://github.com/mcneel/developer-rhino3d-com/blob/wip/README.md)
- [How This Site Works]({{ site.baseurl }}/guides/general/how_this_site_works)
- [Developer Docs Style Guide]({{ site.baseurl }}/guides/general/developer_docs_style_guide)

---

## TODO List

### Guides

The following guides have TODO items:

{% assign guides = site.guide_topics | sort:"title" | sort:"apis" %}
<div class="trigger">
  <ol>
  {% for topic in guides %}
    {% if topic.TODO %}
      <li>
        ({{ topic.apis }}) <a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a> {{ topic.TODO }} {% if topic.origin != 'unset' and topic.TODO == 'needs porting' %} from: <a href="{{ topic.origin }}">{{ topic.origin }}</a>{% endif %}
      </li>
    {% endif %}
  {% endfor %}
  </ol>
</div>

### Samples

The following samples have TODO items:

{% assign samples = site.samples | sort:"title" | sort:"apis" %}
<div class="trigger">
  <ol>
  {% for sample in samples %}
    {% if sample.TODO %}
      <li>
        ({{ sample.apis }}) <a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a>  {{ sample.TODO }} {% if sample.origin != 'unset'  and sample.TODO == 'needs porting' %} from: <a href="{{ sample.origin }}">{{ sample.origin }}</a>{% endif %}
    </li>
    {% endif %}
  {% endfor %}
  </ol>
</div>

### Misc

See [YouTrack: project: WWW subsystem: developer.rhino3d.com #unresolved](http://mcneel.myjetbrains.com/youtrack/issues?q=project%3A+WWW+subsystem%3A+developer.rhino3d.com+%23unresolved)

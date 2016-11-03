---
layout: fullwidth-page
title: Administration
description: The administrator's view of the developer.rhino3d.com website.
permalink: /admin/
order: 1
---

# Administration

This site is the canonical source for developer documentation relating to Rhino, Grasshopper, and other companion products.  The goal of this site is to provide a clear, easy-to-navigate, reference, with consistent formatting and nomenclature.

For contributors or administrators, the following guides are necessary reading:

- [Contributing (This Website)]({{ site.baseurl }}/guides/general/contributing/#this-website)
- [Getting Started with Developer Docs](https://github.com/mcneel/developer-rhino3d-com/blob/master/README.md)
- [How This Site Works]({{ site.baseurl }}/guides/general/how_this_site_works)
- [Developer Docs Style Guide]({{ site.baseurl }}/guides/general/developer_docs_style_guide)

---

## TODO List

The following guides and samples have [TODO items listed in their yaml]({{ site.baseurl }}/guides/general/how_this_site_works/#todo--origin-fields)...

### Guides

{% assign guides = site.guide_topics | sort:"title" | sort:"apis" %}
<div class="trigger">
  <ol>
  {% assign guides_have_todo_items = false %}
  {% for topic in guides %}
    {% if topic.TODO %}
      {% assign guides_have_todo_items = true %}
      <li>
        ({{ topic.apis }}) <a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a> {{ topic.TODO }} {% if topic.origin != 'unset' and topic.TODO == 'needs porting' %} from: <a href="{{ topic.origin }}">{{ topic.origin }}</a>{% endif %}
      </li>
    {% endif %}
  {% endfor %}
  </ol>
</div>

{% if guides_have_todo_items == false %}
*NONE!  Good job!  Check [YouTrack](http://mcneel.myjetbrains.com/youtrack/issues?q=project%3A+WWW+subsystem%3A+developer.rhino3d.com+%23unresolved).*
{% endif %}

### Samples

{% assign samples = site.samples | sort:"title" | sort:"apis" %}
<div class="trigger">
  <ol>
  {% assign samples_have_todo_items = false %}
  {% for sample in samples %}
    {% if sample.TODO %}
      {% assign samples_have_todo_items = true %}
      <li>
        ({{ sample.apis }}) <a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a>  {{ sample.TODO }} {% if sample.origin != 'unset'  and sample.TODO == 'needs porting' %} from: <a href="{{ sample.origin }}">{{ sample.origin }}</a>{% endif %}
    </li>
    {% endif %}
  {% endfor %}
  </ol>
</div>

{% if samples_have_todo_items == false %}
*NONE!  Good job!  Check [YouTrack](http://mcneel.myjetbrains.com/youtrack/issues?q=project%3A+WWW+subsystem%3A+developer.rhino3d.com+%23unresolved).*
{% endif %}

### YouTrack

Many items relating to this site are logged in [YouTrack: project: WWW subsystem: developer.rhino3d.com #unresolved](http://mcneel.myjetbrains.com/youtrack/issues?q=project%3A+WWW+subsystem%3A+developer.rhino3d.com+%23unresolved)

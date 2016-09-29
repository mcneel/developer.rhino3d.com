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

Individual guides and samples may have [TODO]({{ site.baseurl }}/guides/general/how_this_site_works/#todo--origin-fields) items listed in their yaml.  Find out how these [TODO]({{ site.baseurl }}/guides/general/how_this_site_works/#todo--origin-fields) fields work in the [How This Site Works]({{ site.baseurl }}/guides/general/how_this_site_works/#todo--origin-fields) guide.

### Guides

The following guides have [TODO]({{ site.baseurl }}/guides/general/how_this_site_works/#todo--origin-fields) items:

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

The following samples have [TODO]({{ site.baseurl }}/guides/general/how_this_site_works/#todo--origin-fields) items:

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

### YouTrack

Many items relating to the (dis?)functioning of this site are logged in [YouTrack: project: WWW subsystem: developer.rhino3d.com #unresolved](http://mcneel.myjetbrains.com/youtrack/issues?q=project%3A+WWW+subsystem%3A+developer.rhino3d.com+%23unresolved)

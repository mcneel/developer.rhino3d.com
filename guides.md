---
layout: tab-page
title: Guides
permalink: /guides/
order: 2
---

# All Guides

---

## [General]({{ site.baseurl }}/guides/general/)

<div class="trigger">
  <ul>
  {% for topic in site.guide_topics %}
    {% if topic.tags contains 'Guide' and topic.tags contains 'General' %}
      {% if topic.title  %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [RhinoCommon]({{ site.baseurl }}/guides/rhinocommon/) (Cross-Platform)

### Overview
<div class="trigger">
  <ul>
  {% for topic in site.guide_topics %}
    {% if topic.tags contains 'Guide' and topic.tags contains 'About' and topic.tags contains 'RhinoCommon' %}
      {% if topic.title  %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Getting Started
<div class="trigger">
  <ul>
  {% for topic in site.guide_topics %}
    {% if topic.tags contains 'Guide' and topic.tags contains 'GettingStarted' and topic.tags contains 'RhinoCommon' %}
      {% if topic.title  %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

- Installing the tools (Windows)
- Installing the tools (Mac)
- Hello Rhino (Cross-Platform)
- Debugging Hello Rhino (Windows)
- Debugging Hello Rhino (Mac)

### Plugin Fundamentals

- [How the Commands Work](http://wiki.mcneel.com/developer/runrhinocommandfromplugincommand) - Needs porting
- [Event Watchers](http://wiki.mcneel.com/developer/rhinocommonsamples/dotneteventwatcher) - Needs porting

### Advanced

- [Display Conduits](http://wiki.mcneel.com/developer/rhinocommonsamples/displayconduit) - Needs porting
- Rendering
- Custom Objects

---

## [Eto]({{ site.baseurl }}/guides/eto/) (Cross-Platform)

TODO


---

## [Rhino.Python]({{ site.baseurl }}/guides/rhinopython/) (Cross-Platform)

TODO


---

## [openNURBS Toolkit]({{ site.baseurl }}/guides/opennurbs/) (Cross-Platform)

TODO


---

## [C/C++]({{ site.baseurl }}/guides/cpp/) (Windows)

TODO


---

## [Grasshopper]({{ site.baseurl }}/guides/grasshopper/) (Windows)

TODO


---

## [RhinoScript]({{ site.baseurl }}/guides/rhinoscript/) (Windows)

TODO


---

## [Render Development Kit (RDK)]({{ site.baseurl }}/guides/rdk/) (Windows)

TODO


---

## [Rhino Application Platform (RAP)]({{ site.baseurl }}/guides/rap/) (Windows)

TODO


---

## [RhinoMobile]({{ site.baseurl }}/guides/rhinomobile/) (iOS & Android)

TODO


---

## [Zoo License Manager]({{ site.baseurl }}/guides/zoo/) (Windows)

<div class="trigger">
  <ul>
  {% for topic in site.guide_topics %}
    {% if topic.tags contains 'Guide' and topic.tags contains 'Zoo' %}
      {% if topic.title  %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>


---

## [Developer Docs]({{ site.baseurl }}/guides/rhinodevdocs/) (This Website)

<div class="trigger">
  <ul>
  {% for topic in site.guide_topics %}
    {% if topic.tags contains 'Guide' and topic.tags contains 'DevDocs' %}
      {% if topic.title  %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

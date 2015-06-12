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
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.platforms contains 'Cross-Platform' and topic.apis contains 'All' %}
      {% if topic.title and topic.order %}
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
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoCommon' and topic.categories contains 'Overview' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Getting Started
<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoCommon' and topic.categories contains 'GettingStarted' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Fundamentals
<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoCommon' and topic.categories contains 'Fundamentals' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>
- [How the Commands Work](http://wiki.mcneel.com/developer/runrhinocommandfromplugincommand) - Needs porting
- [Event Watchers](http://wiki.mcneel.com/developer/rhinocommonsamples/dotneteventwatcher) - Needs porting

### Advanced
<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoCommon' and topic.categories contains 'Advanced' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>
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

## [Renderer Development Kit (RDK)]({{ site.baseurl }}/guides/rdk/) (Windows)

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
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'Zoo' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>


---

## [Developer Docs]({{ site.baseurl }}/guides/rhinodevdocs/) (This Website)

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'DevDocs' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

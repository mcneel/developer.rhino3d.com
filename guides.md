---
layout: toc-page
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

## [RhinoCommon]({{ site.baseurl }}/guides/rhinocommon/) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

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

{% comment %}

## [Eto]({{ site.baseurl }}/guides/eto/) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

TODO

---

{% endcomment %}

## [Rhino.Python]({{ site.baseurl }}/guides/rhinopython/) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

TODO


---

## [openNURBS Toolkit]({{ site.baseurl }}/guides/opennurbs/) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

TODO


---

## [C/C++]({{ site.baseurl }}/guides/cpp/) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## [Grasshopper]({{ site.baseurl }}/guides/grasshopper/) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## [RhinoScript]({{ site.baseurl }}/guides/rhinoscript/) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## [Renderer Development Kit (RDK)]({{ site.baseurl }}/guides/rdk/) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## [Rhino Application Platform (RAP)]({{ site.baseurl }}/guides/rap/) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## [RhinoMobile]({{ site.baseurl }}/guides/rhinomobile/) <img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="guide_icon"> <img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="guide_icon">

TODO


---

## [Zoo License Manager]({{ site.baseurl }}/guides/zoo/) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

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

## [Developer Docs]({{ site.baseurl }}/guides/rhinodevdocs/) (This Website) <a id="dev-docs"></a>

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  <li><a class="page-link" href="https://github.com/mcneel/developer-rhino3d-com/blob/gh-pages/README.md">Getting Started with Dev Docs</a></li>
  {% for topic in guides %}
    {% if topic.apis contains 'DevDocs' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

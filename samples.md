---
layout: toc-page
title: Samples
permalink: /samples/
order: 4
---
# All Samples  

---

## [General]({{ site.baseurl }}/samples/general/)

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.platforms contains 'Cross-Platform' and sample.apis contains 'All' %}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [RhinoCommon]({{ site.baseurl }}/samples/rhinocommon/) (Cross-Platform)

### Adding Objects

### Curves
<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Curves'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Layers

### Picking and Selection

### Foo

### Bar


---

{% comment %}

## [Eto]({{ site.baseurl }}/samples/eto/) (Cross-Platform)

TODO

---

{% endcomment %}

## [Rhino.Python]({{ site.baseurl }}/samples/rhinopython/) (Cross-Platform)

TODO


---

## [openNURBS Toolkit]({{ site.baseurl }}/samples/opennurbs/) (Cross-Platform)

TODO


---

## [C/C++]({{ site.baseurl }}/samples/cpp/) (Windows)

TODO


---

## [Grasshopper]({{ site.baseurl }}/samples/grasshopper/) (Windows)

TODO


---

## [RhinoScript]({{ site.baseurl }}/samples/rhinoscript/) (Windows)

TODO


---

## [Renderer Development Kit (RDK)]({{ site.baseurl }}/samples/rdk/) (Windows)

TODO


---

## [Rhino Application Platform (RAP)]({{ site.baseurl }}/samples/rap/) (Windows)

TODO


---

## [RhinoMobile]({{ site.baseurl }}/samples/rhinomobile/) (iOS & Android)

TODO


---

## [Zoo License Manager]({{ site.baseurl }}/samples/zoo/) (Windows)

TODO

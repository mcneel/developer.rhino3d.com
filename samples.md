---
layout: toc-page
title: Samples
permalink: /samples/
order: 4
---

# Samples  

---

## General

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

## RhinoCommon

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

### Adding Objects

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Adding Objects'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

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

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Layers'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Picking and Selection

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Picking and Selection'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Viewports and Views

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Viewports and Views'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Blocks

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Blocks'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Drawing

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Draw'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Drafting

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Drafting'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Other

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Other'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>
---


## Rhino.Python

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

TODO


---

## openNURBS

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

TODO


---

## C/C++

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## Grasshopper

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## RhinoScript

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## RDK

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## RhinoMobile

**Platforms**: <img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="guide_icon"> <img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="guide_icon">

TODO


---

## Zoo

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO

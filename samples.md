---
layout: toc-page
title: Samples
permalink: /samples/
order: 4
---

# Samples  
{: .toc-title }

---

## General
{: .toc-header }

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
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

#### Adding Objects
{: .toc-subheader }
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

#### Curves
{: .toc-subheader }
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

#### Layers
{: .toc-subheader }
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

#### Picking and Selection
{: .toc-subheader }
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

#### Viewports and Views
{: .toc-subheader }
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

#### Blocks
{: .toc-subheader }
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

#### Drawing
{: .toc-subheader }
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

#### Drafting
{: .toc-subheader }
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

#### Other
{: .toc-subheader }

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
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

TODO


---

## openNURBS
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

TODO


---

## C/C++
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## Grasshopper
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## RhinoScript
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## RDK
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## RhinoMobile
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="guide_icon"> <img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="guide_icon">

TODO


---

## Zoo
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO

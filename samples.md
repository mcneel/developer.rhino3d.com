---
layout: toc-page
title: Samples
permalink: /samples/
order: 4
---
# All Samples  

---

## General
{: .group }

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

## RhinoCommon <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: .group }

#### Adding Objects
{: .subgroup }

#### Curves
{: .subgroup }

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
{: .subgroup }

#### Picking and Selection
{: .subgroup }

#### Foo
{: .subgroup }

#### Bar
{: .subgroup }

---


## Rhino.Python <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: .group }

TODO


---

## openNURBS Toolkit <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: .group }

TODO


---

## C/C++ <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: .group }

TODO


---

## Grasshopper <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: .group }

TODO


---

## RhinoScript <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: .group }

TODO


---

## Renderer Development Kit <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: .group }

TODO


---

## RhinoMobile <img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="guide_icon"> <img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="guide_icon">
{: .group }

TODO


---

## Zoo License Manager <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: .group }

TODO

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

## RhinoCommon <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: .toc-header }

#### Adding Objects
{: .toc-subheader }

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

#### Picking and Selection
{: .toc-subheader }

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


## Rhino.Python <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: .toc-header }

TODO


---

## openNURBS Toolkit <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: .toc-header }

TODO


---

## C/C++ <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: .toc-header }

TODO


---

## Grasshopper <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: .toc-header }

TODO


---

## RhinoScript <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: .toc-header }

TODO


---

## Renderer Development Kit <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: .toc-header }

TODO


---

## RhinoMobile <img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="guide_icon"> <img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="guide_icon">
{: .toc-header }

TODO


---

## Zoo License Manager <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: .toc-header }

TODO

---
layout: toc-page
title: Samples
description: All the official sample code available for Rhino and Grasshopper developers.
permalink: /samples/
order: 4
---

# Samples  

---

## RhinoCommon <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: #rhinocommon }

### Adding Objects

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Adding Objects'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

<!-- No drafting samples (yet)
### Drafting

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Drafting'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>
-->

### Drawing

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoCommon' and sample.categories contains 'Draw'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---


## Rhino.Python <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: #rhinopython }

<div class="bs-callout bs-callout-danger">
  <h4>UNDER CONSTRUCTION</h4>
  <p>Rhino.Python samples have yet to be ported to this site.  Please check back soon for updates.  
  In the meantime, you can view the original documentation here:
  <a href="http://wiki.mcneel.com/developer/python">http://wiki.mcneel.com/developer/python</a> or see the RhinoCommon samples above.</p>
</div>



---

## openNURBS <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: #opennurbs }

<div class="bs-callout bs-callout-danger">
  <h4>UNDER CONSTRUCTION</h4>
  <p>openNURBS samples have yet to be ported to this site.  Please check back soon for updates.  
  In the meantime, you can view the original documentation here:
  <a href="http://wiki.mcneel.com/developer/opennurbs/home">http://wiki.mcneel.com/developer/opennurbs/home</a> or see the openNURBS samples bundled with the SDK.</p>
</div>


---

## C/C++ <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #cpp }

### Adding Objects

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'C/C++' and sample.categories contains 'Adding Objects'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
    {% if sample.apis contains 'C/C++' and sample.categories contains 'Blocks'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
    {% if sample.apis contains 'C/C++' and sample.categories contains 'Curves'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
    {% if sample.apis contains 'C/C++' and sample.categories contains 'Layers'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
    {% if sample.apis contains 'C/C++' and sample.categories contains 'Picking and Selection'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Surfaces

<div class="trigger">
  {% assign samples = site.samples | sort:"order" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'C/C++' and sample.categories contains 'Surfaces'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
    {% if sample.apis contains 'C/C++' and sample.categories contains 'Viewports and Views'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
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
    {% if sample.apis contains 'C/C++' and sample.categories contains 'Other'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## Grasshopper <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #grasshopper }

<div class="bs-callout bs-callout-danger">
  <h4>UNDER CONSTRUCTION</h4>
  <p>Grasshopper Component samples have yet to be ported to this site.  Please check back soon for updates.  
  In the meantime, you can view the original documentation here:
  <a href="http://wiki.mcneel.com/developer/grasshopper/gha">http://wiki.mcneel.com/developer/grasshopper/gha</a></p>
</div>

---

## RhinoScript <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #rhinoscript }

### Adding Objects

<div class="trigger">
  {% assign samples = site.samples | sort:"title" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoScript' and sample.categories contains 'Adding Objects'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Blocks

<div class="trigger">
  {% assign samples = site.samples | sort:"title" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoScript' and sample.categories contains 'Blocks'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Curves

<div class="trigger">
  {% assign samples = site.samples | sort:"title" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoScript' and sample.categories contains 'Curves'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>


### Layers

<div class="trigger">
  {% assign samples = site.samples | sort:"title" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoScript' and sample.categories contains 'Layers'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Picking and Selection

<div class="trigger">
  {% assign samples = site.samples | sort:"title" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoScript' and sample.categories contains 'Picking and Selection'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Surfaces

<div class="trigger">
  {% assign samples = site.samples | sort:"title" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoScript' and sample.categories contains 'Surfaces'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Viewports and Views

<div class="trigger">
  {% assign samples = site.samples | sort:"title" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoScript' and sample.categories contains 'Viewports and Views'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Flamingo

<div class="trigger">
  {% assign samples = site.samples | sort:"title" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoScript' and sample.categories contains 'Flamingo'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Other

<div class="trigger">
  {% assign samples = site.samples | sort:"title" %}
  <ul>
  {% for sample in samples %}
    {% if sample.apis contains 'RhinoScript' and sample.categories contains 'Other'%}
      {% if sample.title and sample.order %}
        <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}" title="{{ sample.description }}">{{ sample.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## RhinoMobile <img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="guide_icon"> <img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="guide_icon">
{: #rhinomobile }

<div class="bs-callout bs-callout-danger">
  <h4>UNDER CONSTRUCTION</h4>
  <p>RhinoMobile samples have yet to be ported to this site.  Please check back soon for updates.  
  In the meantime, you can view the samples on GitHub here:
  <a href="https://github.com/mcneel/RhinoMobileSamples">https://github.com/mcneel/RhinoMobileSamples</a></p>
</div>

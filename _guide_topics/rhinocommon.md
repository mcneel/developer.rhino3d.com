---
title: RhinoCommon Guides
description: RhinoCommon is the cross-platform .NET plugin SDK for Rhino.
platforms: ['Windows', 'Mac']
layout: guide-homepage
---

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinocommon-guides-col1.png">]({{ site.baseurl }}/guides/rhinocommon/what-is-rhinocommon/)

### Overview

- [What is RhinoCommon?]({{ site.baseurl }}/guides/rhinocommon/what-is-rhinocommon/)
- [What are Mono & Xamarin?]({{ site.baseurl }}/guides/rhinocommon/what-are-mono-and-xamarin/)
- [What's New/Changes?]({{ site.baseurl }}/guides/rhinocommon/whats-new/)

### Getting Started

- Installing Tools ([Windows]({{ site.baseurl }}/guides/rhinocommon/installing-tools-windows/), [Mac]({{ site.baseurl }}/guides/rhinocommon/installing-tools-mac/))
- Your First Plugin ([Windows]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-windows/), [Mac]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-mac/), [Cross-Platform]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-crossplatform/))
- Plugin Installers ([Windows]({{ site.baseurl }}/guides/rhinocommon/plugin-installers-windows/), [Mac]({{ site.baseurl }}/guides/rhinocommon/plugin-installers-mac/))

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinocommon-guides-col2.png">]({{ site.baseurl }}/guides/rhinocommon/display-conduits/)

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'RhinoCommon' and guide.categories contains 'Fundamentals' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Advanced

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'RhinoCommon' and guide.categories contains 'Advanced' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinocommon-guides-col3.png">]({{ site.baseurl }}/guides/rhinocommon/creating-zoo-plugins/)

### Zoo

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'RhinoCommon' and guide.categories contains 'Zoo' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

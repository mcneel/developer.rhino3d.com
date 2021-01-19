---
title: RhinoCommon Guides
description: RhinoCommon is the cross-platform .NET plugin SDK for Rhino.
authors: unset
sdk: unset
languages: ['C#']
platforms: ['Windows', 'Mac']
categories: ['Unsorted']
origin: unset
order: 1
keywords: ['rhino', 'developer']
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
- [Developer samples on GitHub](https://github.com/mcneel/rhino-developer-samples)
- [Developer discussions on Discourse](https://discourse.mcneel.com/c/rhino-developer)
- [Distributing a Rhino Plug-In with the Package Manager]({{ site.baseurl }}/guides/yak/creating-a-rhino-plugin-package/)

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoCommon' and guide.categories contains 'Fundamentals' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinocommon-guides-col2.png">]({{ site.baseurl }}/guides/rhinocommon/display-conduits/)

### Rendering

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoCommon' and guide.categories contains 'Rendering' %}
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
  <li><a href="{{ site.baseurl }}/api/RhinoCommon">API Reference</a></li>
  <li><a href="https://github.com/picoe/Eto/wiki">Eto.Forms guides</a></li>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoCommon' and guide.categories contains 'Advanced' %}
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

### LAN Zoo

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoCommon' and guide.categories contains 'Zoo' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Cloud Zoo

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoCommon' and guide.categories contains 'CloudZoo' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

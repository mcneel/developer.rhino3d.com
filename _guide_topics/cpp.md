---
title: C/C++ Guides
description: Guides to the C/C++ SDK for Rhino for Windows plugins.
authors: unset
author_contacts: unset
sdk: unset
languages: ['C/C++']
platforms: ['Windows']
categories: ['Unsorted']
origin: unset
order: 1
keywords: ['rhino', 'developer']
layout: guide-homepage
---

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/cpp-guides-col1.png">]({{ site.baseurl }}/guides/cpp/what-is-the-cpp-sdk/)

### Overview

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Overview' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Getting Started

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Getting Started' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>
- [Developer samples on GitHub](https://github.com/mcneel/rhino-developer-samples)

### Troubleshooting

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Troubleshooting' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/cpp-guides-col2.png">]({{ site.baseurl }}/guides/cpp/adding-command-line-options/)

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Fundamentals' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/cpp-guides-col3.png">]({{ site.baseurl }}/guides/cpp/drawing-arrowheads-in-display-conduits/)

### Advanced

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Advanced' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Rendering (RDK)

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'RDK' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Zoo

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Zoo' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

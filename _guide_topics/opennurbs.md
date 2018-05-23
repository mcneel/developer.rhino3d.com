---
title: openNURBS Guides
description: Read/Write Rhino 3dm files in your application.
authors: unset
author_contacts: unset
sdk: unset
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Unsorted']
origin: unset
order: 1
keywords: ['rhino', 'developer']
layout: guide-homepage
---

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/opennurbs-guides-col1.png">]({{ site.baseurl }}/guides/opennurbs/what-is-opennurbs/)

### Overview

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'openNURBS' and guide.categories contains 'Overview' %}
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
    {% if guide.sdk contains 'openNURBS' and guide.categories contains 'Getting Started' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/opennurbs-guides-col2.png">]({{ site.baseurl }}/guides/opennurbs/data-from-ellipses/)

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'openNURBS' and guide.categories contains 'Fundamentals' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/opennurbs-guides-col3.png">]({{ site.baseurl }}/guides/opennurbs/superfluous-knots/)

### Advanced

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'openNURBS' and guide.categories contains 'Advanced' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

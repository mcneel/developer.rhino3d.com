---
title: Grasshopper Guides
description: Guides to creating custom Grasshopper components and plugins.
platforms: ['Windows', 'Mac']
layout: guide-homepage
---

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/grasshopper_guides_col1.png">]({{ site.baseurl }}/guides/grasshopper/what_is_a_grasshopper_component/)

### Overview

- [What is a Grasshopper Component?]({{ site.baseurl }}/guides/grasshopper/what_is_a_grasshopper_component/)

### Getting Started

- Installing Tools ([Windows]({{ site.baseurl }}/guides/grasshopper/installing_tools_windows/), [Mac]({{ site.baseurl }}/guides/grasshopper/installing_tools_mac/))
- Your First Component ([Windows]({{ site.baseurl }}/guides/grasshopper/your_first_component_windows/), [Mac]({{ site.baseurl }}/guides/grasshopper/your_first_component_mac/))

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/grasshopper_guides_col2.png">]({{ site.baseurl }}/guides/grasshopper/simple_component/)

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'Grasshopper' and guide.categories contains 'Fundamentals' %}
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
    {% if guide.apis contains 'Grasshopper' and guide.categories contains 'Advanced' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/grasshopper_guides_col3.png">]({{ site.baseurl }}/guides/grasshopper/grasshopper_data_types/)

### In Depth

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'Grasshopper' and guide.categories contains 'In Depth' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---
title: General Guides
description: Guides that apply across platforms and SDKs.
platforms: ['Windows', 'Mac']
layout: guide-homepage
---

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.platforms contains 'Cross-Platform' and guide.apis contains 'General' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

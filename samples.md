---
layout: tab-page
title: samples
permalink: /samples/
order: 4
---

<div class="trigger">
  {% for sample in site.samples %}
    {% if sample.title %}
    <a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ sample.title }}</a>
    {% endif %}
  {% endfor %}
</div>

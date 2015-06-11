---
layout: tab-page
title: Samples
permalink: /samples/
order: 4
---

<div class="trigger">
  <ul>
  {% for sample in site.samples %}
    {% if sample.title %}
    <li><a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a></li>
    {% endif %}
  {% endfor %}
  </ul>
</div>

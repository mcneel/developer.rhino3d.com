---
layout: tab-page
title: guides
permalink: /guides/
order: 2
---

<div class="trigger">
  <ul>
  {% for topic in site.guide_topics %}
    {% if topic.title %}
    <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
    {% endif %}
  {% endfor %}
  </ul>
</div>

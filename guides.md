---
layout: tab-page
title: guides
permalink: /guides/
order: 2
---

<div class="trigger">
  {% for topic in site.guide_topics %}
    {% if topic.title %}
    <a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a>
    {% endif %}
  {% endfor %}
</div>

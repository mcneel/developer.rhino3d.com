---
title: Yak Guides
description: Guides to using the Yak package manager.
authors: unset
author_contacts: unset
sdk: unset
languages: # empty
platforms: ['Windows', 'Mac']
categories: ['Unsorted']
origin: unset
order: 1
keywords: ['rhino', 'developer']
layout: guide-homepage
---

### Overview

- [What is Yak?]({{ site.baseurl }}/guides/yak/what-is-yak)

### Fundamentals

{% assign guides = site.guide_topics | where:"sdk","Yak" | where:"categories","Fundamentals" | sort %}
<ul>
{% for guide in guides %}
  <li><a href="{{ guide.url | prepend: site.baseurl }}">{{ guide.title }}</a></li>
{% endfor %}
</ul>

### Step By Step

{% assign guides = site.guide_topics | where:"sdk","Yak" | where:"categories","Step By Step" | sort %}
<ul>
{% for guide in guides %}
  <li><a href="{{ guide.url | prepend: site.baseurl }}">{{ guide.title }}</a></li>
{% endfor %}
</ul>

### Features

- [Package Restore in Grasshopper]({{ site.baseurl }}/guides/yak/package-restore-in-grasshopper)

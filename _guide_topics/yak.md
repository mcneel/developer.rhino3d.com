---
title: Package Manager Guides
description: Guides to using the Rhino package manager, mostly from a developer's perspective.
authors: unset
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

- [What is the Package Manager (a.k.a. Yak)?]({{ site.baseurl }}/guides/yak/what-is-yak)
- [Join the Discussion](https://discourse.mcneel.com/c/serengeti/yak)

### Fundamentals

{% assign guides = site.guide_topics | where:"sdk","Yak" | where:"categories","Fundamentals" | sort %}
<ul>
{% for guide in guides %}
  <li><a href="{{ guide.url | prepend: site.baseurl }}">{{ guide.title }}</a></li>
{% endfor %}
</ul>

### Getting Started

{% assign guides = site.guide_topics | where:"sdk","Yak" | where:"categories","Getting Started" | sort:"order" %}
<ul>
{% for guide in guides %}
  <li><a href="{{ guide.url | prepend: site.baseurl }}">{{ guide.title }}</a></li>
{% endfor %}
</ul>

### Features

- [Package Restore in Grasshopper]({{ site.baseurl }}/guides/yak/package-restore-in-grasshopper)

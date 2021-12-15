---
title: Compute Guides
description: Guides to developing, deploying, and contributing to Compute.
authors: unset
sdk: unset
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Unsorted']
origin: unset
order: 1
keywords: ['rhino', 'developer']
layout: fullwidth-page
---
<div class="row">
<div class="col-12" markdown="1">   

# Compute Guides

</div>
<div class="col-md-7 col-sm-12 col-sm-12" markdown="1">  

Write code to access the Rhino and Grasshopper SDKs through a stateless REST API running on Windows Servers. Use Compute to enhance any online solution you are developing to create and manipulate two and three-dimensional curves, surfaces, and solids. Install and customize Compute to run on any cloud services framework.

</div>
</div>

<div class="row-fluid">  
<div class="col-md-4" markdown="1">  

### Getting Started

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'Compute' and guide.categories contains 'Getting Started' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

</div>
</div>

<div class="row-fluid">  
<div class="col-md-4" markdown="1">  

### Production Deployment

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'Compute' and guide.categories contains 'Deployment' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

</div>
</div>

<div class="row-fluid">  
<div class="col-md-4" markdown="1">  

### Hops

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'Compute' and guide.categories contains 'Hops' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

</div>
</div>
